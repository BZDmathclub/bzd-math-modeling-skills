---
name: bzd-model-dictionary
description: Query the bundled BZD mathematical-modeling dictionary for a user-selected model, explain its assumptions, inputs, outputs, limitations and validation, then judge whether it fits the current competition problem and data. Use when a user asks whether a proposed model is appropriate, requests model feasibility review, or wants dictionary-based alternatives for a modeling task.
---

# BZD Model Dictionary

Evaluate a user-selected model against the problem and data supplied in the current request. Base dictionary facts on `assets/model-dictionary.json`; distinguish those facts from the case-specific professional judgment.

## Required inputs

Require:

- selected model name;
- complete problem statement or relevant task text;
- involved data, data file, or enough data description to identify variables, sample unit, sample size, time/space structure, missingness, repeated measures, target and constraints.

If the model name is ambiguous, show dictionary candidates and ask the user to identify the intended one. If data are incomplete, give only a provisional judgment and list the missing evidence; do not invent distribution, sample size or variable structure.

## Current-task isolation

Treat each invocation as a fresh assessment. Ignore solution ideas, preferred models, computed results and judgments from earlier turns or other conversations unless the user explicitly includes them in the current request. Do not claim to switch the underlying AI model. Instead, state that the assessment uses only the current problem, current data evidence and bundled dictionary records. When the host supports a genuinely separate fresh task, the user may start one, but this is not required for the Skill to apply isolation.

## Workflow

1. Read the current problem and data evidence first. Extract the mathematical task, observation unit, target, explanatory variables, data type, dependence, sample size, missingness, imbalance, time/space structure, constraints and desired output.
2. Run `scripts/query_dictionary.py --model "<name>"`. Use `--exact` when an exact record is known. Do not load or reproduce the entire 5713-record asset in the response.
3. Preserve distinct records when the same algorithm appears for different purposes. Compare model name, large category, subgroup, model category, use case, inputs and outputs before selecting the relevant record.
4. Present a compact dictionary table for every materially relevant match. Include record ID, name, category/group, applicable scenarios, data requirements, plain-language principle, inputs, outputs, key assumptions, prohibitions, limitations and validation methods. Preserve any returned `资料使用声明` verbatim.
5. Read [references/fit-assessment.md](references/fit-assessment.md) and assess the current case independently. Test task alignment, data sufficiency, assumptions, dependence/leakage, output alignment, validation feasibility, interpretability, computational feasibility and competition-paper completeness.
6. Give one primary verdict: `合适`, `有条件合适`, `不合适`, or `证据不足，待人工复核`. Explain which evidence drives it. Do not treat popularity or model sophistication as suitability.
7. If not fully suitable, recommend 2-4 alternatives or companion models. Query each alternative in the dictionary before describing it. State whether the alternative replaces, preprocesses, validates or complements the selected model.
8. End with an actionable use plan: preprocessing, train/test or estimation design, parameter/constraint choices, validation metrics, sensitivity analysis and what the paper must report.

## Output structure

Use this order:

1. `当前任务隔离声明`
2. `题目与数据结构识别`
3. `字典中的模型信息` — table
4. `适配性逐项判定` — table with criterion, evidence, status and consequence
5. `最终判定`
6. `替代或配套模型`
7. `落地与论文写作建议`
8. `信息不足与待人工复核`

## Copyright and data guardrails

- The bundled JSON is read-only. Never delete, overwrite or normalize away root copyright fields, embedded BZD attribution, commercial-use prohibitions or any record's `资料使用声明`.
- Do not output the full dictionary, bulk-export records, or create a transformed database unless the user separately requests an authorized non-commercial operation that preserves every declaration.
- Keep the attribution `BZD数模社制作` when quoting dictionary content. Do not describe the dictionary as an absolute authority; encourage checking textbooks, papers and official documentation for consequential decisions.
- Do not expose or reproduce unrelated records. Return only matches and justified alternatives needed for the current task.
- For niche, new or ambiguous algorithms, verify against authoritative sources when current accuracy requires it and label unresolved claims `待人工复核`.

