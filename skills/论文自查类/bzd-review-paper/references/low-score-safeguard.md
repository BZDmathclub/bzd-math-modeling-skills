# Low-score bottom-up safeguard

## Purpose

When the ordinary deduction-based raw score is below 20, use a second bottom-up pass to recognize genuine completed work, because real judges normally do not keep subtracting a very weak substantive paper to zero. This is not a general bonus.

## Trigger and exclusion

Run only when the ordinary raw score before the format multiplier is `< 20`. Do not run if the paper answers a different central task, uses forbidden information, has a central false model invalidating downstream results, reports principal results that cannot arise from its model/data, violates central hard constraints extensively, or contains no substantive model/solution/result. Do not trigger merely because the format multiplier makes the final score below 20.

## Calculation

Reuse the frozen rubric. Start from zero and award only positively demonstrated, traceable work in task understanding, assumptions, model formulation, solution procedure, results, validation, presentation and reproducibility. Each atomic award cannot exceed its nominal weight or 90% ceiling.

`bottom_up_evidenced_score = Σ awarded atomic credit`

`bottom_up_capped_score = min(35, bottom_up_evidenced_score)`

`reported_raw_score = max(ordinary_raw_score, bottom_up_capped_score)`

Then apply the same format-quality coefficient. Keep competition-context adjustments separate.

## Audit trail

Retain the ordinary deduction ledger and additionally show every bottom-up credit, its evidence, the evidenced total, the 35-point cap, selected raw score and final score. If a core failure blocks the safeguard, show the precise evidence. Uncertainty alone is not proof of a core failure.

