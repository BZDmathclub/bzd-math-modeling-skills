# Atomic deduction scoring

Use this procedure after freezing the problem-specific rubric and before estimating position.

## 1. Importing `bzd-paper-format-checker`

If a complete format-checker report exists for the same paper version, reuse it instead of repeating the format audit.

1. Verify that the report identifies the same paper filename/version and is complete rather than provisional.
2. Import its eligibility findings, page evidence, atomic deductions and final format score. Preserve the original score in the audit trail.
3. Normalize the imported result to the review-format scale `[-10, 10]`. If the imported checker uses the 15-point scale `F15`, use:

   `format_score = clamp(F15 × 10 / 15, -10, 10)`

   If the imported report already supplies a `[-10,10]` score, use it directly after clamping.
4. The formatting contribution to the raw 100-point score cannot be negative and remains subject to the 90% category ceiling:

   `format_earned = min(9.0, max(0, format_score))`

5. Map the normalized format score linearly and deterministically to the whole-paper format-quality coefficient:

   `format_multiplier = clamp((format_score + 10) / 20, 0, 1.00)`

   Thus `-10 → 0.00`, `-5 → 0.25`, `0 → 0.50`, `5 → 0.75`, and `10 → 1.00`. Round the displayed coefficient to two decimals only after calculation. Do not replace this mapping with qualitative bands.
6. Carry proven eligibility risks into `资格与格式审查`. Do not infer failure from items marked `无法核验`.
7. Do not deduct the imported format defects again under abstract or model work. The multiplier is not a second discretionary deduction: it is the required deterministic consequence of `format_score`.
8. If the paper changed after the format report, import only unaffected findings and recheck changed pages before recalculating `format_score` and the coefficient.

When no complete matching report exists, use `formatting-standard.md` normally.

## 2. Per-problem block structure

Every problem must contain three score-bearing blocks:

- `模型建立`: mathematical abstraction, assumptions, variables, mechanism, equations, objectives, constraints and problem-specific mapping;
- `模型求解`: data processing, algorithm, parameters, implementation, convergence, reproducibility and validation needed to obtain the answer;
- `结果与回答`: numerical or qualitative answer, units, requested tables/files/plans, interpretation, feasibility and direct response to every subtask.

Allocate weights according to the frozen rubric. Example for a 25-point problem:

| Block | Weight | 90% ceiling |
|---|---:|---:|
| 模型建立 | 15 | 13.5 |
| 模型求解 | 5 | 4.5 |
| 结果与回答 | 5 | 4.5 |

This is an example, not a universal ratio. Preserve the problem's actual difficulty and deliverables.

## 3. Freeze atomic checks before scoring

For every problem and every one of its three blocks, write several observable atomic checks before reading the paper for quality. Do not reuse one undifferentiated checklist for the entire paper. Each check must come from that problem's frozen rubric, state what evidence satisfies it, and carry a prospective 1/2/3 deduction level.

### 模型建立

- the mathematical object matches the task and physical/statistical mechanism;
- key variables, sets, parameters, units and domains are defined;
- assumptions are necessary and compatible with the problem;
- objective/equations/constraints are complete and problem-specific;
- dependencies on earlier questions are implemented rather than merely claimed;
- the model is identifiable, feasible and internally consistent.

### 模型求解

- preprocessing has rules, quantities and reasons;
- algorithm and parameter settings are disclosed;
- initialization, random seed, termination and solver settings are reproducible where relevant;
- computation respects constraints and units;
- convergence, diagnostics, validation or sensitivity match the model type;
- intermediate results support the final answer.

### 结果与回答

- every requested subtask is answered;
- results contain the required values, units, ranges, rankings, plans or files;
- results follow from the stated model and computation;
- feasibility and real-world meaning are explained;
- uncertainty, error or limitations are reported where material;
- values are consistent across abstract, body, tables, figures and appendix.

## 4. Deduction scale

List every defect under its corresponding block, then calculate the score at the problem level from the problem's `90% ceiling`.

| Deduction | Use when |
|---:|---|
| 1 | 局部轻微缺失；主体推理仍然可用 |
| 2 | 实质性缺失、依据不足或明显不一致；可信度明显下降 |
| 3 | 核心步骤错误、无法复现或严重影响该板块 |

Formula:

First assign nominal weights to all atomic points. Their sum must equal the nominal problem weight, but the nominal weight is not the operational deduction for a defect.

`problem_nominal_weight = Σ atomic_nominal_weights`

`problem_deduction = Σ all 1-3 point atomic deductions in 模型建立、模型求解、结果与回答`

`problem_earned = max(0, 0.90 × problem_nominal_weight - problem_deduction)`

Do not cap the diagnostic deduction sum at 10. For example, a 15-point problem may contain approximately 15 one-point nominal checks; if every check has a severe failure, the visible deduction ledger may total about 45 points. The earned score is simply floored at zero.

Every unmet atomic item receives its own 1-3 point entry. A rubric block containing five requirements therefore needs five separately verifiable rows, unless one requirement must be split further to remain observable. Do not replace the ledger with a vague holistic score. Repeated manifestations of one root defect may be grouped, but distinct failures must be deducted separately. Never report an earned score below zero.

## 5. Central-error handling

A central error does not replace the atomic ledger. Split its observable consequences into distinct scoring points and assign 3 points to each genuinely separate failure, for example: wrong mathematical target, unusable solution procedure, missing required result, or violated hard constraint. Do not create duplicate deductions for multiple symptoms of one root error.

A novel alternative remains valid when it satisfies the task, respects all constraints, is mathematically coherent and is supported by reproducible evidence. Different model names or numerical routes are not deductions by themselves.

## 6. Required scoring ledger

For every problem, output at least:

| Problem | Block | Atomic check | Weight/ceiling | Evidence | Deduction | Earned |
|---|---|---|---|---|---:|---:|

After all rows, show:

- problem and block weights;
- every separate 1-3 point deduction;
- uncapped problem deduction sum;
- total operational deduction, even when it exceeds the nominal problem weight;
- problem 90% ceiling and final problem score.

The arithmetic must be reproducible from visible rows. Keep `评委满分保留` separate from paper defects.
