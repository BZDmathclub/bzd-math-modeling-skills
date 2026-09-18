# Mathematical Modeling Paper Rubric

Use these anchors only as fallback guidance. The problem-specific rubric and learned official rules control the actual weights. Score intermediate quality proportionally; do not default to the midpoint.

## Fixed-category anchors

### Abstract — 10 points

Read and apply [title-abstract-keywords.md](title-abstract-keywords.md) completely. A completed abstract without a major defect starts at 3 points. Award 7-8 only when it passes the lay-reader test and communicates the concrete problem, work, models and results. Reserve 9-10 for complete, specific, concise and body-consistent task-method-result coverage.

### Formatting compliance — 10 points

Read and apply [formatting-standard.md](formatting-standard.md) completely. Run its eligibility gate first. If eligible, start at 10 and deduct 1-3 per error, capped at a 10-point deduction. Then apply its overall presentation multiplier to the raw 100-point score. Do not double-count title/keyword defects already considered under the abstract/front-matter review.

| Dimension | Weight | Full-credit evidence | Typical deductions |
|---|---:|---|---|
| Problem understanding and objectives | 8 | Correct interpretation, explicit objectives, constraints, outputs, and success criteria | Misread prompt, omitted task, vague objective |
| Assumptions and abstraction | 8 | Necessary, plausible, justified assumptions; clear scope and variable definitions | Convenience assumptions without impact analysis; contradictions |
| Data and preprocessing | 10 | Traceable sources, appropriate sampling, units, cleaning, uncertainty, and no leakage | Unverifiable data, arbitrary preprocessing, unit or leakage errors |
| Model design and mathematical correctness | 22 | Suitable formulation, correct derivation, coherent model chain, identified parameters | Formula errors, unjustified method choice, disconnected models |
| Solution, computation, and reproducibility | 12 | Correct algorithm, implementation detail, convergence/settings, reproducible outputs | Black-box computation, inconsistent tables, missing parameters/code logic |
| Validation, sensitivity, and robustness | 15 | Relevant baselines or checks, out-of-sample/diagnostic validation, sensitivity and uncertainty | Self-confirming validation, no robustness test, overclaiming |
| Results and task fulfillment | 10 | Answers every task with interpretable quantified results and sound conclusions | Results do not answer prompt; conclusions exceed evidence |
| Innovation and insight | 7 | Meaningful modeling, computational, or interpretive contribution that improves the solution | Cosmetic complexity or unsupported novelty claim |
| Communication and presentation | 8 | Strong abstract, logical narrative, readable equations/figures/tables, proper citations | Poor abstract, ambiguous notation, clutter, citation problems |
| **Total** | **100** | | |

## Score anchors

- 90–100: exceptional, correct, deeply validated, reproducible, and competition-leading.
- 80–89: strong and complete, with limited weaknesses that do not undermine the core result.
- 70–79: competent, but important gaps in validation, justification, completeness, or communication.
- 60–69: plausible core attempt with major deficiencies or weak evidence.
- 50–59: substantial work, but serious correctness, task-fulfillment, or reproducibility problems.
- 0–49: fundamentally incomplete, invalid, or unsupported.

## Caps and penalties

Apply the narrowest justified cap and explain it; do not double-punish the same defect.

- Cap total at 69 if a required major task is absent.
- Cap total at 59 if the central model is mathematically invalid or results cannot support the main conclusion.
- Cap total at 49 if the artifact contains no substantive model/result or is largely unreadable.
- Deduct 2–10 points for material internal inconsistencies, fabricated-looking/untraceable evidence, or serious citation failures, proportional to impact. Describe suspicious evidence; do not declare misconduct without verification.
- Do not penalize unavailable source code by itself unless reproducibility is a stated contest requirement; score the reproducibility evidence present in the paper.

## Award and position estimate

Read and apply [award-ranking-output.md](award-ranking-output.md). Use its 2025 score anchors, continuous percentile interpolation, uncertainty band, award interpretation, evaluation-date warning and required closing notice.
