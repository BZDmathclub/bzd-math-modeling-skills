# Low-score bottom-up safeguard

## Purpose

Real judges rarely continue subtracting from an already very weak paper until it becomes zero. When the ordinary deduction-based raw score is below 20, use a second, bottom-up pass to recognize genuine completed work. This is a safeguard for very weak but substantive papers, not a general bonus.

## Trigger

Run only when:

- the ordinary raw score before the format multiplier is `< 20`; and
- no non-compensable core failure below is proven.

Do not trigger because the format multiplier alone reduces the final score below 20.

## Non-compensable core failures

Do not use the safeguard when evidence establishes one of these conditions:

- the paper materially answers a different problem or omits the central task;
- the central mathematical relationship is false and invalidates most downstream results;
- the solution uses information explicitly forbidden or unavailable in the problem;
- principal numerical results cannot arise from the stated model/data and no defensible alternative trace exists;
- a submitted plan violates central hard constraints so extensively that it cannot function as a solution;
- the paper contains no substantive model, solution process or task-facing result.

Uncertainty is not proof. If evidence is incomplete, note the limitation and allow the safeguard rather than declaring a core failure.

## Bottom-up scoring

Reuse the frozen 100-point rubric and atomic point weights. Start from zero and award only for positively demonstrated evidence:

- complete and paper-consistent abstract content;
- correct task understanding and usable assumptions;
- correctly defined variables, parameters, units, equations, objectives or constraints;
- executable data processing or algorithm steps;
- traceable intermediate or final results that answer part of a task;
- valid feasibility, diagnostic, sensitivity or independent verification;
- readable, compliant presentation and reproducibility evidence.

For each atomic point, award no more than its nominal weight and no more than the 90% judge ceiling. Give partial credit proportional to the portion actually demonstrated. Do not infer credit from model names, claimed accuracy or unsupported conclusions.

Calculate:

`bottom_up_evidenced_score = Σ awarded atomic credit`

`bottom_up_capped_score = min(35, bottom_up_evidenced_score)`

`reported_raw_score = max(ordinary_raw_score, bottom_up_capped_score)`

The bottom-up route will normally remain at or below 35. It can never raise the reported raw score above 35 when the ordinary score was below 20.

After selecting the raw score, apply the same format-quality coefficient. Competition-context adjustments occur only afterward and remain separate.

## Required audit trail

Show:

- ordinary deduction-based raw score;
- trigger status;
- any non-compensable failure decision and evidence;
- each bottom-up credit item, nominal weight, awarded credit and location;
- bottom-up evidenced total;
- 35-point cap;
- selected reported raw score;
- final score after the format coefficient.

Do not erase the original deduction ledger. The report must make clear that the safeguard changed the scoring direction from subtraction to evidence-based addition.

