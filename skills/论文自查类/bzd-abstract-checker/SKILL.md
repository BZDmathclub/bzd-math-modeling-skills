---
name: bzd-abstract-checker
description: Review a user-provided Chinese mathematical-modeling abstract without requiring the problem statement or full paper, identify concrete writing defects, and prioritize revisions. Use when the user asks to check, diagnose, or improve a modeling-paper abstract; do not claim coverage or factual consistency that cannot be verified without the problem or paper.
---

# BZD Abstract Checker

Review only the abstract the user supplies. Do not require the competition problem, paper body, code, or results before beginning. Diagnose the existing text; do not silently rewrite it unless the user also asks for a revised abstract.

Read [references/rubric.md](references/rubric.md) before evaluating an abstract.

## First gate: independent readability

Read the abstract as a researcher outside the paper's subject area. Determine whether the abstract, by itself, makes all three items reasonably clear:

1. **Problem:** what concrete research task or decision problem is being solved;
2. **Method:** what principal model or mathematical type is used and how it is solved;
3. **Result:** what concrete result, ordering, prediction, optimum, error, performance measure, or actionable conclusion is obtained.

Also assess whether it appears capable of fitting within one A4 page. Text length is only a proxy because page fit depends on formatting. Treat roughly 800–1000 Chinese characters as guidance, not an absolute rule, unless the competition specifies otherwise.

If any of Problem, Method, or Result is substantially absent or unintelligible, begin with exactly this severity label:

> ⚠️ **严重警告：该摘要目前不能作为一篇可独立阅读的短文。**

Then state which of the three essential elements is missing or unclear and why a non-specialist cannot reconstruct the study from the abstract. Do not soften a failed first gate merely because the prose is fluent.

If all three are identifiable, state:

> ✅ **独立阅读性：通过。**

Passing this gate does not mean the abstract has no other problems.

## Evidence discipline

- Quote only short fragments from the supplied abstract as evidence.
- Distinguish **absent**, **present but vague**, and **clear**.
- Do not infer a model, result, innovation, validation, subproblem, or causal link that the abstract does not state.
- With abstract-only input, mark these as **无法仅凭摘要核验** rather than defects: coverage of every original question, consistency with the paper body, truth of reported values, and whether a claimed innovation or test was actually performed.
- Flag an internal contradiction when it is visible inside the abstract itself.
- If the user supplies title or keywords alongside the abstract, review them; otherwise omit those sections rather than requesting them.

## Required output

Use this order:

1. **摘要独立性判定** — first-gate label plus a concise explanation.
2. **问题清单** — a Markdown table with `优先级 | 位置/原文 | 问题 | 为什么影响评阅 | 修改方向`. List concrete issues only. Use `严重 / 重要 / 一般`.
3. **逐项观察** — cover problem, method/model, algorithm versus software, quantitative results, conclusions, validation, innovation/limitations, structure/linkage, language, prohibited elements, and length/page risk. For each item use `清楚 / 不充分 / 缺失 / 无法核验 / 不适用`.
4. **最优先修改的3项** — actions with the greatest likely improvement, ordered.
5. **摘要自查结论** — one compact paragraph describing the current level and the next revision target.

If there are no meaningful defects in a category, say so briefly; do not invent a criticism to fill the table. Do not output a numerical score unless the user explicitly asks for one.

## Revision boundary

When the user asks to rewrite after the diagnosis, preserve every stated model, algorithm, number, and conclusion. Do not manufacture missing results. Use placeholders such as `【补充关键数值】` only when the user requests a template or revision draft.

