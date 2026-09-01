# BZD-review-paper

When reviewing a mathematical modeling competition paper, first read and strictly follow:

@SKILL.md

Treat `SKILL.md` as the controlling workflow. Read every reference it marks as required before scoring. The user must supply both the complete contest problem and the complete paper.

If the user supplies an existing `bzd-paper-format-checker` report for the same paper version, pass it into the review and reuse its format score, eligibility findings and page evidence. Normalize the review-format score to `[-10,10]` and calculate the quality coefficient with `(format_score + 10) / 20`. Do not repeat or double-count the same format defects. For every problem, separately score `模型建立`, `模型求解` and `结果与回答` from their 90%-of-weight ceilings, using visible 1/2/3-point deductions for every unmet rubric item.

At the first interaction, ask whether the contest is the Higher Education Press Cup CUMCM unless the user has already stated it. Use the CUMCM position route only for that contest; use the small-contest uniform route for all others unless actual same-contest scores are supplied.

Typical request:

```text
请使用 BZD-review-paper 评审以下数学建模论文：
竞赛类型：高教社杯国赛 / 其他（请填写名称）
赛题：<赛题文件路径>
论文：<论文文件路径>
已有格式自查报告：<可选，bzd-paper-format-checker 输出路径>
请严格按照 SKILL.md 的输出顺序生成报告。
```
