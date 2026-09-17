# -*- coding: utf-8 -*-
"""Render a 题意逐句翻译 Markdown report as one standalone HTML file.

The Markdown report is the default deliverable. Run this only when the user asks
for an HTML rendering as well; it never replaces the `.md` file.

Body text and every table are rendered statically, so the report stays fully
readable offline. Only the mandatory Mermaid cross-question flowchart needs the
network; when the CDN is unreachable the page says so and auto-expands the
diagram source instead of showing a blank box.

Usage:
    python render_html.py <report.md> [-o <report.html>]

Exit codes:
    0  rendered
    1  bad input (missing file, unreadable, not a translation report)
    2  structural check failed (see stderr)
"""
from __future__ import unicode_literals

import argparse
import codecs
import html as _html
import io
import os
import re
import sys

# --- stdout/stderr must survive Chinese on a GBK console -------------------
for _s in ("stdout", "stderr"):
    _st = getattr(sys, _s)
    if hasattr(_st, "buffer"):
        setattr(sys, _s, io.TextIOWrapper(_st.buffer, encoding="utf-8", errors="replace"))


# --------------------------------------------------------------------------
# inline markdown
# --------------------------------------------------------------------------
def inline(text):
    """Escape HTML, then re-apply the inline Markdown we actually emit."""
    out = _html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\$([^$]+)\$", r"<span class='math'>\1</span>", out)
    # the output standard writes <br> literally inside table cells
    out = out.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>")
    return out


def split_row(line):
    """Split a Markdown table row, honouring pipes escaped as \\|."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [p.strip().replace(r"\|", "|") for p in re.split(r"(?<!\\)\|", body)]


def is_sep(line):
    return bool(re.match(r"^\s*\|[\s\-:|]+\|\s*$", line))


def row_class(cells):
    """Colour-code priority rows and pass/fail verdicts."""
    first = cells[0].strip()
    second = cells[1].strip() if len(cells) > 1 else ""
    joined = " ".join(cells)
    if first == "P0":
        return " class='p0'"
    if first == "P1":
        return " class='p1'"
    if "不通过" in joined:
        return " class='fail'"
    if second == "通过":
        return " class='pass'"
    return ""


# --------------------------------------------------------------------------
# block parser
# --------------------------------------------------------------------------
def convert(md):
    lines = md.split("\n")
    out, toc, diagrams = [], [], []
    i, n, sec = 0, len(lines), 0

    while i < n:
        line = lines[i]

        # ---- fenced mermaid -> diagram figure + collapsible source
        if line.strip().startswith("```mermaid"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(buf)
            diagrams.append(code)
            esc = _html.escape(code, quote=False)
            out.append(
                "<figure class='diagram'>\n"
                "<div class='mermaid'>\n" + esc + "\n</div>\n"
                "<details class='src'><summary>查看 Mermaid 源码"
                "（图未渲染时可复制到 mermaid.live）</summary>"
                "<pre><code>" + esc + "</code></pre></details>\n"
                "</figure>"
            )
            continue

        # ---- any other fenced block
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + _html.escape("\n".join(buf), quote=False) + "</code></pre>")
            continue

        # ---- table
        if line.strip().startswith("|") and i + 1 < n and is_sep(lines[i + 1]):
            head = split_row(line)
            ncol = len(head)
            i += 2
            body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            t = ["<div class='tablewrap'><table>", "<thead><tr>"]
            t += ["<th>" + inline(h) + "</th>" for h in head]
            t.append("</tr></thead><tbody>")
            for cells in body:
                cells = (cells + [""] * ncol)[:ncol]
                t.append("<tr%s>" % row_class(cells))
                t += ["<td>" + inline(c) + "</td>" for c in cells]
                t.append("</tr>")
            t.append("</tbody></table></div>")
            out.append("\n".join(t))
            continue

        # ---- blockquote: a truly blank line ends it; ">"-only lines are separators
        if line.strip().startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            text = "\n".join(buf)
            cls = "warn" if "不可作为建模与求解依据" in text else ""
            paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
            out.append(
                "<blockquote class='%s'>%s</blockquote>"
                % (cls, "".join("<p>" + inline(p.replace("\n", " ")) + "</p>" for p in paras))
            )
            continue

        # ---- heading
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1:
                out.append("<h1>" + inline(txt) + "</h1>")
            else:
                sec += 1
                anchor = "s%d" % sec
                if lvl == 2:
                    toc.append((anchor, txt))
                out.append("<h%d id='%s'>%s</h%d>" % (lvl, anchor, inline(txt), lvl))
            i += 1
            continue

        # ---- rule
        if re.match(r"^\s*---+\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # ---- list
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            items = []
            while i < n and re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[i]):
                items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>" + inline(x) + "</li>" for x in items), tag))
            continue

        if line.strip() == "":
            i += 1
            continue

        # ---- paragraph
        buf = [line]
        i += 1
        while i < n and lines[i].strip() != "" and not re.match(
            r"^\s*(?:#{1,4}\s|\||>|```|---+\s*$|[-*]\s|\d+\.\s)", lines[i]
        ):
            buf.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

    return "\n".join(out), toc, diagrams


# --------------------------------------------------------------------------
# summary chips, derived from the report itself
# --------------------------------------------------------------------------
def build_chips(md):
    chips = []

    if re.search(r"中国研究生数学建模竞赛|华为杯|CPGMCM", md):
        chips.append("中国研究生数学建模竞赛（华为杯）")
    elif re.search(r"全国大学生数学建模竞赛|高教社杯|CUMCM", md):
        chips.append("全国大学生数学建模竞赛（高教社杯）")

    year = re.search(r"(20\d{2})\s*年?", md)
    letter = re.search(r"([A-F])\s*题", md)
    if year and letter:
        chips.append("%s 年 · %s 题" % (year.group(1), letter.group(1)))
    elif year:
        chips.append("%s 年" % year.group(1))

    # ledger rows live in the section-2 table
    ledger = re.search(r"##\s*2\..*?(?=\n##\s|\Z)", md, re.S)
    if ledger:
        rows = [
            l for l in ledger.group(0).split("\n")
            if l.strip().startswith("|") and not is_sep(l)
        ]
        if len(rows) > 1:
            chips.append("逐句表 %d 行" % (len(rows) - 1))

    # 问题一 and 问题1 are the same question; normalise before counting
    cn2ar = dict(zip("一二三四五六七八九", "123456789"))
    qs = set()
    for tok in re.findall(r"问题\s*([一二三四五六七八九]|十[一二]?|\d+)", md):
        if tok.startswith("十"):
            qs.add(str(10 + (int(cn2ar[tok[1]]) if len(tok) > 1 else 0)))
        else:
            qs.add(cn2ar.get(tok, tok))
    if qs:
        chips.append("%d 问全覆盖" % len(qs))

    audit = re.search(r"##\s*7\..*?\Z", md, re.S)
    if audit:
        rows = [
            l for l in audit.group(0).split("\n")
            if l.strip().startswith("|") and not is_sep(l)
        ]
        # subtract one header row per table in the section
        ntable = len(re.findall(r"(?m)^\s*\|[\s\-:|]+\|\s*$", audit.group(0)))
        nitem = max(0, len(rows) - ntable)
        nfail = len(re.findall(r"不通过", audit.group(0)))
        if nitem:
            chips.append("核验 %d 项 · %s" % (nitem, "%d 项不通过" % nfail if nfail else "无不通过"))

    return chips


# --------------------------------------------------------------------------
CSS = """
:root{
  --ink:#152238; --ink2:#3d4f6b; --muted:#6b7b95;
  --blue:#1d4ed8; --blue-d:#12327d; --blue-l:#eef3fd; --blue-b:#c7d8f6;
  --line:#dbe3ef; --bg:#f6f8fc; --card:#fff;
  --warn:#b4530a; --warn-bg:#fff6ec; --warn-b:#f0c48a;
  --ok:#0f7a52; --ok-bg:#eefaf4;
  --p0:#b3243a; --p0-bg:#fff0f2;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif;
  font-size:15px; line-height:1.75; -webkit-font-smoothing:antialiased;
}
.layout{display:flex; align-items:flex-start; max-width:1680px; margin:0 auto}
nav.toc{
  position:sticky; top:0; flex:0 0 268px; height:100vh; overflow-y:auto;
  background:var(--card); border-right:1px solid var(--line); padding:26px 0 40px;
}
nav.toc .brand{padding:0 22px 16px; border-bottom:1px solid var(--line); margin-bottom:12px}
nav.toc .brand b{display:block; font-size:14px; letter-spacing:.06em; color:var(--blue-d)}
nav.toc .brand span{display:block; font-size:11.5px; color:var(--muted); margin-top:4px; letter-spacing:.04em}
nav.toc a{display:block; padding:8px 22px; color:var(--ink2); text-decoration:none; font-size:13.5px; border-left:3px solid transparent}
nav.toc a:hover{background:var(--blue-l); color:var(--blue-d); border-left-color:var(--blue)}
main{flex:1 1 auto; min-width:0; padding:34px 40px 90px}
h1{font-size:25px; line-height:1.45; margin:0 0 8px; color:var(--blue-d); padding-bottom:18px; border-bottom:3px solid var(--blue)}
.meta{display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 30px}
.meta span{background:var(--card); border:1px solid var(--blue-b); color:var(--blue-d); border-radius:999px; padding:4px 13px; font-size:12.5px}
h2{
  font-size:19px; margin:46px 0 14px; color:var(--blue-d);
  padding:9px 0 9px 14px; border-left:5px solid var(--blue); background:var(--blue-l);
  border-radius:0 5px 5px 0; scroll-margin-top:16px;
}
h3{font-size:15.5px; margin:26px 0 10px; color:var(--ink); scroll-margin-top:16px}
h3::before{content:"\\258D"; color:var(--blue); margin-right:6px}
p{margin:10px 0}
hr{border:0; border-top:1px dashed var(--line); margin:34px 0}
code{
  background:#eef1f7; border:1px solid var(--line); border-radius:4px; padding:1px 5px;
  font-size:12.5px; font-family:"Cascadia Mono",Consolas,Menlo,monospace; color:#1f3a6e; word-break:break-all;
}
.math{font-family:"Cambria Math",Cambria,Georgia,serif; font-style:italic; color:#1f3a6e; white-space:nowrap}
strong{color:var(--blue-d)}
ul,ol{margin:10px 0 10px 22px; padding:0}
li{margin:5px 0}
blockquote{margin:14px 0; padding:14px 18px; background:var(--card); border:1px solid var(--line); border-left:4px solid var(--blue-b); border-radius:0 6px 6px 0}
blockquote p{margin:7px 0}
blockquote p:first-child{margin-top:0}
blockquote p:last-child{margin-bottom:0}
blockquote.warn{background:var(--warn-bg); border-color:var(--warn-b); border-left:4px solid var(--warn); color:var(--warn); font-weight:600}
blockquote.warn strong{color:#8f3f04}
.tablewrap{overflow-x:auto; margin:16px 0; background:var(--card); border:1px solid var(--line); border-radius:7px; box-shadow:0 1px 2px rgba(21,34,56,.04)}
table{border-collapse:collapse; width:100%; font-size:13px; min-width:640px}
thead th{
  background:var(--blue-d); color:#fff; text-align:left; font-weight:600; padding:10px 11px;
  border-right:1px solid rgba(255,255,255,.16); position:sticky; top:0; z-index:2; white-space:nowrap;
}
thead th:last-child{border-right:0}
tbody td{padding:9px 11px; border-top:1px solid var(--line); border-right:1px solid #eef1f7; vertical-align:top; line-height:1.68}
tbody td:last-child{border-right:0}
tbody tr:nth-child(even){background:#fbfcfe}
tbody tr:hover{background:var(--blue-l)}
tbody td:first-child{white-space:nowrap; color:var(--blue-d); font-weight:600}
tr.p0{background:var(--p0-bg)!important}
tr.p0 td:first-child{color:var(--p0)}
tr.p1 td:first-child{color:var(--warn)}
tr.pass td:nth-child(2){color:var(--ok); font-weight:600; background:var(--ok-bg)}
tr.fail td{background:var(--p0-bg); color:var(--p0)}
figure.diagram{margin:20px 0; padding:20px; background:var(--card); border:1px solid var(--line); border-radius:8px; text-align:center; overflow-x:auto}
figure.diagram .mermaid{min-height:40px}
details.src{margin-top:14px; text-align:left}
details.src summary{cursor:pointer; font-size:12.5px; color:var(--muted); padding:5px 0; outline:none}
details.src summary:hover{color:var(--blue)}
details.src pre{background:#f4f6fa; border:1px solid var(--line); border-radius:6px; padding:12px; overflow-x:auto; font-size:12px; line-height:1.6; margin:8px 0 0}
details.src pre code{background:none; border:0; padding:0}
@media (max-width:1000px){
  .layout{flex-direction:column}
  nav.toc{position:static; height:auto; flex:none; width:100%; border-right:0; border-bottom:1px solid var(--line); padding-bottom:14px}
  nav.toc a{display:inline-block; border-left:0; padding:6px 13px}
  main{padding:24px 18px 70px}
}
@media print{
  nav.toc,details.src{display:none}
  body{background:#fff; font-size:10.5px}
  main{padding:0}
  .tablewrap{overflow:visible; box-shadow:none}
  table{min-width:0; font-size:9px}
  thead th{position:static; background:#12327d!important; -webkit-print-color-adjust:exact; print-color-adjust:exact}
  tbody tr{page-break-inside:avoid}
  h2{page-break-after:avoid; -webkit-print-color-adjust:exact; print-color-adjust:exact}
}
"""

JS = """
(function(){
  var figs = document.querySelectorAll('figure.diagram');
  if (!figs.length) return;
  if (typeof mermaid === 'undefined') {
    figs.forEach(function(f){
      var box = f.querySelector('.mermaid');
      if (box) box.innerHTML = '<p style="color:#6b7b95;font-size:13px;margin:0">'
        + '流程图需要联网加载 Mermaid 才能渲染。可展开下方源码，粘贴到 mermaid.live 查看。</p>';
      var d = f.querySelector('details.src'); if (d) d.open = true;
    });
    return;
  }
  mermaid.initialize({
    startOnLoad: true,
    securityLevel: 'loose',
    flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' },
    themeVariables: {
      primaryColor: '#eef3fd', primaryTextColor: '#152238', primaryBorderColor: '#1d4ed8',
      lineColor: '#3d4f6b', fontSize: '14px',
      fontFamily: '-apple-system,"Segoe UI","Microsoft YaHei",sans-serif'
    }
  });
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="layout">
<nav class="toc">
  <div class="brand"><b>题意逐句翻译</b><span>{subtitle}</span></div>
{nav}
</nav>
<main>
{body}
</main>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>{js}</script>
</body>
</html>
"""


# --------------------------------------------------------------------------
def check(html, md):
    """Refuse to ship a rendering that silently lost structure."""
    problems = []

    if md.count("```mermaid") and "class='mermaid'" not in html:
        problems.append("源报告含 Mermaid 流程图，但渲染结果中不存在图块")

    md_tables = len(re.findall(r"(?m)^\s*\|[\s\-:|]+\|\s*$", md))
    if md_tables != html.count("<table>"):
        problems.append("表格数量不一致：Markdown %d，HTML %d" % (md_tables, html.count("<table>")))

    if len(re.findall(r"(?m)^##\s", md)) != len(re.findall(r"<h2 ", html)):
        problems.append("二级标题数量不一致")

    for pat, name in ((r"\*\*", "未渲染的加粗标记"), (r"(?m)^#{1,4} ", "未渲染的标题"),
                      (r"(?m)^\|", "未渲染的表格行")):
        if re.search(pat, html):
            problems.append(name)

    # every table must keep a consistent cell count
    for idx, t in enumerate(re.findall(r"(?s)<table>.*?</table>", html), 1):
        ncol = len(re.findall(r"<th>", re.search(r"(?s)<thead>.*?</thead>", t).group(0)))
        for r in re.findall(r"(?s)<tr(?: class='[^']*')?>(?!.*?<th).*?</tr>", t):
            c = len(re.findall(r"<td>", r))
            if c and c != ncol:
                problems.append("第 %d 张表存在 %d 格行，表头为 %d 列" % (idx, c, ncol))
                break
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render a 题意逐句翻译 Markdown report as standalone HTML.")
    ap.add_argument("source", help="path to the .md report")
    ap.add_argument("-o", "--output", help="output .html path (default: alongside the source)")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.source):
        sys.stderr.write("找不到源文件：%s\n" % args.source)
        return 1
    try:
        md = codecs.open(args.source, encoding="utf-8").read()
    except UnicodeDecodeError:
        sys.stderr.write("源文件不是 UTF-8 编码：%s\n" % args.source)
        return 1

    h1 = re.search(r"(?m)^#\s+(.*)$", md)
    if not h1:
        sys.stderr.write("源文件缺少一级标题，不像是题意逐句翻译报告\n")
        return 1

    body, toc, diagrams = convert(md)
    chips = build_chips(md)

    title = h1.group(1).strip()
    nav = "\n".join("  <a href='#%s'>%s</a>" % (a, _html.escape(t, quote=False)) for a, t in toc)
    html = PAGE.format(
        title=_html.escape(title, quote=True),
        subtitle=_html.escape(chips[1] if len(chips) > 1 else title[:24], quote=True),
        css=CSS,
        nav=nav,
        body=body,
        js=JS,
    )
    if chips:
        html = html.replace(
            "</h1>",
            "</h1>\n<div class='meta'>%s</div>"
            % "".join("<span>%s</span>" % _html.escape(c, quote=False) for c in chips),
            1,
        )

    problems = check(html, md)

    dst = args.output or os.path.splitext(args.source)[0] + ".html"
    if problems:
        sys.stderr.write("结构校验未通过，已放弃写出：\n")
        for p in problems:
            sys.stderr.write("  - %s\n" % p)
        return 2

    with codecs.open(dst, "w", encoding="utf-8") as f:
        f.write(html)

    print("已生成：%s" % dst)
    print("体积：%d 字节" % os.path.getsize(dst))
    print("章节：%d   表格：%d   流程图：%d" % (len(toc), html.count("<table>"), len(diagrams)))
    if chips:
        print("摘要：%s" % " / ".join(chips))
    return 0


if __name__ == "__main__":
    sys.exit(main())
