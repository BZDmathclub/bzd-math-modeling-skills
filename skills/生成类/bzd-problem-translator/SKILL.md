---
name: bzd-problem-translator
description: Translate a complete mathematical modeling contest problem sentence by sentence into precise modeling language, preserve every substantive condition and definition, expose hidden constraints, draw a mandatory Mermaid cross-question flowchart, audit omissions, and deliver one easy-to-open Markdown report. For Huawei Cup (CPGMCM) graduate-contest problems, additionally prepend a plain-language layer that rewrites the background and questions as a primary-school word problem with a mandatory term-mapping table. Use whenever a user supplies a CUMCM, CPGMCM, or other modeling problem and asks to interpret, translate, unpack, read closely, identify requirements, or avoid missing details before modeling.
---

# BZD Problem Translator

Treat `翻译` as semantic translation from contest prose into executable modeling meaning, not merely translation between languages. Assume every sentence may carry a definition, mechanism, constraint, data clue, evaluation target, deliverable, or dependency.

This Skill is distilled from the problem statements, scoring rules, reviewer points, review summaries, and complete review workflows of 16 Higher Education Press Cup CUMCM problems from 2020-2025. Use historical patterns only to detect signals; the current problem always controls.

For Huawei Cup (中国研究生数学建模竞赛, CPGMCM) problems, the dominant difficulty is not mathematical depth but entry cost: the prose comes from real engineering or research projects, runs long, is dense with unexplained domain terms, and assumes background the solver does not have. Such problems therefore require an additional plain-language comprehension layer before sentence-level translation.

## Required references

Read completely before analysis:

- [references/sentence-interpretation-rules.md](references/sentence-interpretation-rules.md)
- [references/historical-review-signals.md](references/historical-review-signals.md)
- For CUMCM A-E problems, read [references/cumcm-abcde-translation-signals.md](references/cumcm-abcde-translation-signals.md) after identifying the problem letter.
- For Huawei Cup problems, read [references/cpgmcm-plain-language-translation.md](references/cpgmcm-plain-language-translation.md) and [references/cpgmcm-translation-signals.md](references/cpgmcm-translation-signals.md).
- [references/md-output-standard.md](references/md-output-standard.md)

## Contest identification

Identify the contest before analysis, because it selects the required output structure.

Treat the problem as Huawei Cup when any of these holds: the user says 华为杯/研究生数模/中国研究生数学建模竞赛/CPGMCM; the text contains `中国研究生数学建模竞赛`, `全国研究生数学建模竞赛`, or `华为杯`; or the problem is lettered A-F and shows graduate-contest characteristics such as a real engineering/research origin, literature-style exposition, measured-data attachments, and unexplained domain terminology.

A problem letter alone is never sufficient. When signals are inconclusive, ask once: `这是华为杯（中国研究生数学建模竞赛）题目吗？` Do not assume a contest before confirmation. Do not apply Huawei Cup problem-letter assumptions: in CPGMCM the same letter maps to different subject areas across years, so derive the structural kernel from the text itself, never from the letter.

## Required input

Require the complete problem, including the actual problem title, background, definitions, all numbered questions, tables, figure captions, attachment descriptions, notes, and appendices. Ignore cover boilerplate appearing before the actual problem title, such as the contest name/year, `全国大学生数学建模竞赛题目`, `请先阅读“全国大学生数学建模竞赛论文格式规范”`, page headers, download watermarks, and generic submission notices. Do not include those items in the ledger or coverage count. If a referenced attachment description or page is missing, identify the missing part before claiming complete coverage.

## Workflow

1. Identify the contest per `Contest identification`. Locate the actual problem-title anchor, such as `A题……`, `B题……`, or `Problem A: ...`. Exclude generic material before this anchor, then read the complete substantive problem once before interpreting any individual question.
2. For Huawei Cup problems, apply `cpgmcm-plain-language-translation.md` and build the plain-language comprehension layer first: a one-sentence version, a primary-school word problem whose sub-questions align one-to-one with the original questions, a term-mapping table whose third column states what each analogy loses, and a background-knowledge card. This layer is additive: it never replaces the sentence-level ledger, and it carries the mandatory non-modeling warning line verbatim.
3. Reconstruct the problem's global story: object, state, mechanism, data, decision, objective, and final deliverables.
4. Divide the source into auditable units. Keep one complete source sentence per unit; split a semicolon or enumerated clause only when it contains independently enforceable requirements. Assign stable IDs such as `B01`, `D03`, `Q2-04`, and `A01`.
5. Build a coverage ledger. Preserve the exact source sentence and translate it into concise plain Chinese modeling language.
6. For each unit, extract explicit facts, implied meaning, upstream/downstream dependencies, omission risk, and required solution evidence. For CUMCM, use the matching A-E historical signals only as a question-generating checklist; for Huawei Cup, use the structural kernels in `cpgmcm-translation-signals.md` the same way, matched per question rather than per problem letter. Do not inject a historical condition that is absent from the current prompt.
7. Resolve cross-sentence terminology. Flag synonyms, overloaded words, reference frames, time scopes, populations, repeated entities, and changing assumptions. For Huawei Cup problems, expect genuine source-text inconsistencies: list competing wordings side by side with their locations and a recommended reading plus reason, rather than silently normalizing them to one term.
8. Trace every numbered question backward to supporting sentences and forward to later questions.
9. Build the mandatory cross-question dependency chain as one Mermaid flowchart. For every question, identify its incoming definitions/data/previous results and outgoing results/constraints/validation uses. Draw genuinely independent questions as parallel branches connected to shared inputs and the whole-problem objective; never omit a numbered question.
10. Run a coverage audit: every substantive source unit from the problem-title anchor onward must appear exactly once in the ledger, every explicit deliverable must appear in the requirement matrix, and every numbered question must appear in the Mermaid flowchart. For Huawei Cup problems, also run the self-check in `cpgmcm-plain-language-translation.md` section 7. Report excluded pre-title boilerplate separately only as an audit note, not as translated content.
11. Create one polished UTF-8 `.md` report following `md-output-standard.md`. Do not create XLSX, CSV, HTML, or image files unless the user separately requests them. Do not complete or export the report if the Mermaid flowchart is missing, invalid, or omits any numbered question, or if a Huawei Cup report is missing the plain-language layer. Return a short completion note and a clickable Markdown-file link instead of pasting the full report into chat when file creation is available.

## Required Markdown content

Use the following heading order in one Markdown document.

### 0. 小学应用题式题意还原（仅华为杯）

Required for Huawei Cup problems and omitted entirely for other contests. Place it before `整题概览` so the solver meets it first. Follow `cpgmcm-plain-language-translation.md` and include all four parts: the 40-character one-sentence version, the word problem with one-to-one question alignment, the term-mapping table whose third column states what each analogy loses, and the background-knowledge card.

Immediately after the word problem, reproduce this line verbatim:

> ⚠️ 本节是帮助理解的类比版本，已丢失精度，**不可作为建模与求解依据**。实际建模必须回到第 3 节逐句翻译表与原始题面。

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
- The plain-language layer is additive and never substitutive. Do not shorten, merge, or drop the sentence-level ledger because the word-problem version already conveys the gist.
- Do not let the word problem use any subject-specific term, including deceptively common ones such as 频谱, 协方差, or 泛化. Its highest permitted mathematics is arithmetic, ratio, simple equations, averages, area/volume, and elementary probability.
- Preserve logical strength words in the word problem exactly: 只能, 至少, 最多, 必须, 不许, 每一个. Simplify domain terms and numbers, never the direction of a constraint, the number of unknowns, the dependency order between questions, an information boundary, or whether the objective is a maximum or a minimum.
- Every simplified term needs a filled third mapping column stating what the analogy discards. `无` is not an acceptable value.
- Do not infer a Huawei Cup structural kernel from the problem letter. CPGMCM letters map to different subject areas across years.
- Do not silently normalize inconsistent Huawei Cup source wording into a single term. Record both wordings, their locations, and a recommended reading with its reason.
