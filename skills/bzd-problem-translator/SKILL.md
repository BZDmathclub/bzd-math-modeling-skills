---
name: bzd-problem-translator
description: Translate a complete mathematical modeling contest problem sentence by sentence into precise modeling language, preserve every substantive condition and definition, expose hidden constraints, draw a mandatory Mermaid cross-question flowchart, audit omissions, and deliver one easy-to-open Markdown report. Use whenever a user supplies a CUMCM or other modeling problem and asks to interpret, translate, unpack, read closely, identify requirements, or avoid missing details before modeling.
---

# BZD Problem Translator

Treat `翻译` as semantic translation from contest prose into executable modeling meaning, not merely translation between languages. Assume every sentence may carry a definition, mechanism, constraint, data clue, evaluation target, deliverable, or dependency.

This Skill is distilled from the problem statements, scoring rules, reviewer points, review summaries, and complete review workflows of 16 Higher Education Press Cup CUMCM problems from 2020-2025. Use historical patterns only to detect signals; the current problem always controls.

## Required input

Require the complete problem, including the actual problem title, background, definitions, all numbered questions, tables, figure captions, attachment descriptions, notes, and appendices. Ignore cover boilerplate appearing before the actual problem title, such as the contest name/year, `全国大学生数学建模竞赛题目`, `请先阅读“全国大学生数学建模竞赛论文格式规范”`, page headers, download watermarks, and generic submission notices. Do not include those items in the ledger or coverage count. If a referenced attachment description or page is missing, identify the missing part before claiming complete coverage.

## Required references

Read completely before analysis:

- [references/sentence-interpretation-rules.md](references/sentence-interpretation-rules.md)
- [references/historical-review-signals.md](references/historical-review-signals.md)
- [references/md-output-standard.md](references/md-output-standard.md)

## Workflow

1. Locate the actual problem-title anchor, such as `A题……`, `B题……`, or `Problem A: ...`. Exclude generic material before this anchor, then read the complete substantive problem once before interpreting any individual question.
2. Reconstruct the problem's global story: object, state, mechanism, data, decision, objective, and final deliverables.
3. Divide the source into auditable units. Keep one complete source sentence per unit; split a semicolon or enumerated clause only when it contains independently enforceable requirements. Assign stable IDs such as `B01`, `D03`, `Q2-04`, and `A01`.
4. Build a coverage ledger. Preserve the exact source sentence and translate it into concise plain Chinese modeling language.
5. For each unit, extract explicit facts, implied meaning, upstream/downstream dependencies, omission risk, and required solution evidence.
6. Resolve cross-sentence terminology. Flag synonyms, overloaded words, reference frames, time scopes, populations, repeated entities, and changing assumptions.
7. Trace every numbered question backward to supporting sentences and forward to later questions.
8. Build the mandatory cross-question dependency chain as one Mermaid flowchart. For every question, identify its incoming definitions/data/previous results and outgoing results/constraints/validation uses. Draw genuinely independent questions as parallel branches connected to shared inputs and the whole-problem objective; never omit a numbered question.
9. Run a coverage audit: every substantive source unit from the problem-title anchor onward must appear exactly once in the ledger, every explicit deliverable must appear in the requirement matrix, and every numbered question must appear in the Mermaid flowchart. Report excluded pre-title boilerplate separately only as an audit note, not as translated content.
10. Create one polished UTF-8 `.md` report following `md-output-standard.md`. Do not create XLSX, CSV, HTML, or image files unless the user separately requests them. Do not complete or export the report if the Mermaid flowchart is missing, invalid, or omits any numbered question. Return a short completion note and a clickable Markdown-file link instead of pasting the full report into chat when file creation is available.

## Required Markdown content

Use the following heading order in one Markdown document.

### 1. 整题概览

State what system is studied, what information is supplied, what decisions or estimates must be produced, and how the questions progress.

### 2. 逐句题意翻译与联动表

| 编号 | 题干原句 | 通俗而精确的翻译 | 明示条件/数据 | 隐含建模信号 | 与前后内容的联动 | 漏读后果 | 后文必须出现的证据 |
|---|---|---|---|---|---|---|---|

Never replace the exact source sentence with an ellipsis. Do not merge unrelated sentences merely to shorten the table.

### 3. 核心术语与口径表

List every defined or potentially ambiguous term with its source definition, adopted interpretation, unit/scope, and affected questions. Distinguish prompt facts from model assumptions.

### 4. 各问输入—任务—输出表

| 问题 | 直接输入 | 需要解决的任务 | 必须满足的约束 | 最终输出 | 依赖前问内容 | 将被后问复用的内容 |
|---|---|---|---|---|---|---|

### 5. 跨问题联动链

This is a mandatory Mermaid flowchart, not a text table. Draw the complete dependency structure from shared definitions/data through foundational models to later extension, optimization, prediction, or decision tasks.

Flowchart requirements:

- Place `题干共同定义/附件数据` or the actual shared source at the left/top as the starting node.
- Give every numbered question a distinct node. Use short labels containing both the question number and its core task.
- Use directed arrows to show transfer direction. Put a short label beside each arrow stating the transferred parameter, result, constraint, model, or validation evidence.
- Draw parallel questions as separate branches from the same source; do not force a false sequence.
- Draw convergence where branches jointly support a later task or final conclusion.
- Draw a clearly visible return arrow when a later question revises, validates, or corrects an earlier result.
- End at `全题最终输出/结论` or an equivalent concrete final deliverable.
- Use a fenced `mermaid` code block with `flowchart TD` or `flowchart LR`.
- Label edges with the transferred parameter, result, constraint, model, or validation evidence.
- Use Mermaid `subgraph` blocks when they materially clarify shared inputs, parallel branches, validation, or correction stages.
- Keep labels concise and quote node text containing punctuation. Avoid crossing relationships where a clearer orientation or subgraph can eliminate them.
- Do not add a separate cross-question edge table. The Mermaid flowchart itself is the required representation.

### 6. 最容易漏读或误解的句子

Prioritize 5-12 sentences. Explain the tempting misreading and correct interpretation. Include numerical limits, negations, comparison baselines, data-source restrictions, repeated-measure structure, geometry, time scope, and specified output formats where present.

### 7. 完整性核验

Report substantive source-unit count, ledger-row count, numbered questions covered, attachments/appendices covered or missing, unresolved ambiguities, excluded pre-title boilerplate, and explicit confirmation that no substantive sentence from the problem-title anchor onward was silently omitted.

## Guardrails

- Do not invent an official interpretation when wording is ambiguous; present plausible readings and downstream consequences.
- Do not jump from a sentence to a fashionable model name without explaining the semantic signal.
- Do not solve the problem or fabricate results. Model-family hints are allowed only to clarify meaning.
- Do not treat background prose as disposable. Explain whether it defines motivation, risk, mechanism, objective priority, or applicability.
- Preserve all numbers, units, intervals, directions, shapes, timing rules, information restrictions, and requested files exactly.
- If OCR or extraction is uncertain, mark the affected sentence for visual verification.
- Never count or translate generic contest headers, year labels, format reminders, page headers, download watermarks, or submission boilerplate that appears before the actual problem title.
- Do not skip a special instruction merely because it resembles boilerplate when it appears after the problem title or changes the current problem's data, constraints, allowed resources, or deliverables.
- Deliver one UTF-8 `.md` file by default.
- Escape Markdown-table cell content containing `|`, replace internal line breaks with `<br>`, and preserve formulas with inline or fenced LaTeX where useful.
- Never treat `跨问题联动链` as optional. A Markdown report without a populated, syntactically valid Mermaid flowchart covering every numbered question is incomplete and must not be delivered.
