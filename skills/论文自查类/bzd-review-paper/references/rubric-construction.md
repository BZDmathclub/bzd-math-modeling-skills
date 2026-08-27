# Problem-Specific Rubric Construction Standard

Build the rubric before evaluating the paper. The rubric must total exactly 100 points and be usable by another judge with substantially similar results.

## 1. Build from the supplied problem

Derive the rubric from:

1. every explicit task, constraint and required output in the supplied problem;
2. dependencies, difficulty and modeling work implied by the problem structure;
3. the closest learned cases in `calibrations/` and transferable patterns in `cross-case-patterns.md`; and
4. generic anchors in `rubric.md` where the problem leaves a quality dimension implicit.

The current problem always controls. Historical cases may suggest how to decompose or validate a task, but may not impose a model, numerical answer or weight that the current problem does not justify. Label criteria as `problem-explicit`, `problem-derived`, `historically calibrated`, or `generic quality`.

## 2. Decompose the problem

Create a requirement matrix containing:

- task/subquestion ID;
- required decision, prediction, explanation, design, or other output;
- explicit constraints, definitions, units, time/space scope, and supplied data;
- expected evidence needed to verify completion;
- dependencies between tasks;
- phrases indicating emphasis, such as “must,” “justify,” “compare,” “evaluate,” or “recommend.”

Split compound requirements into independently scorable items. Do not invent a preferred model family. Reward fitness, correctness, and evidence rather than method prestige.

## 3. Allocate 100 points

Use this required default framework:

The rubric weights must still total 100, but every numeric criterion has a mandatory earned-score ceiling of 90% of its weight. For a criterion weighted `w`, record `0.90w` as its maximum earnable score. This judge-reserve rule applies to abstract, formatting, model work and supplementary quality. It is not evidence of a paper defect, must not be reallocated, and makes 90/100 the theoretical raw-score maximum.

- **Abstract: exactly 10 points.** Read and apply `title-abstract-keywords.md`. Use its 3-point completed-abstract floor, lay-reader test, adaptive paragraph structure and 0-10 anchors.
- **Formatting compliance: exactly 10 points.** Read and apply `formatting-standard.md`: eligibility gate, itemized 1-3 point deductions capped at 10, then the holistic presentation multiplier.
- **Model construction and solution: 70–75 points.** This must contain model assumptions, model construction, and model solution. Allocate most points to the explicit subquestions and their mathematical/computational completion.
- **Problem-specific supplementary quality: 5–10 points.** Allocate the remainder needed to reach 100 among validation/sensitivity, result analysis, model evaluation, generalization, innovation, or another explicit deliverable. Do not create an irrelevant category merely to fill points.

The model construction and solution block must be decomposed rather than scored holistically:

- **Model assumptions:** judge necessity, rationality, consistency, scope, and impact. Typical share: 5–10 points of the full paper.
- **Model construction:** judge variable/parameter definitions, mechanism or mathematical formulation, method suitability, derivation, constraints, and mapping to each subquestion. Typical share: 35–45 points.
- **Model solution:** judge algorithms, parameter estimation, computation, numerical correctness, convergence/settings, results, and reproducibility. Typical share: 20–30 points.

Adjust those three internal shares to the problem, but keep their sum within 70–75. If a problem is primarily theoretical, data-driven, simulation-based, or optimization-based, move points toward the work that is genuinely central.

Avoid double counting. A subquestion-specific criterion should score its formulation, solution, and required result exactly once. Cross-cutting supplementary criteria should score only qualities not already captured.

## 4. Write criterion anchors

For every criterion specify:

- stable ID and source task;
- weight;
- observable full-credit evidence;
- partial-credit anchors, preferably at roughly 75%, 50%, and 25%;
- zero-credit condition;
- critical error or cap, if applicable;
- provenance and rationale.

Use measurable language. Replace “good model” with properties such as correct formulation, justified parameters, appropriate comparison, verified result, or complete required output.

## 5. Define failure rules

Derive task-specific caps before scoring. At minimum consider:

- omission of a required major subquestion;
- failure of a prerequisite that invalidates downstream tasks;
- violation of an explicit hard constraint;
- central mathematical or computational invalidity;
- results that cannot be traced to the stated model/data.

Prevent double punishment: deduct the direct criterion first, then apply a global cap only when the defect undermines the paper as a whole.

## 6. Quality gate

Freeze the rubric only if all checks pass:

- weights sum exactly to 100;
- abstract equals 10 and formatting equals 10;
- model assumptions, construction, and solution are explicit and together equal 70–75;
- remaining categories equal 5–10 and are justified by the problem;
- formatting eligibility has been checked before numeric scoring, and the presentation multiplier is declared before finalizing the adjusted total;
- every explicit problem deliverable maps to at least one criterion;
- every criterion maps to a source requirement or declared cross-cutting quality;
- criteria are non-overlapping enough to avoid duplicate deductions;
- full, partial, and zero anchors are observable;
- all problem requirements are preserved and criterion derivation is visible;
- no specific algorithm is required without support from the current task;
- caps and dependencies are declared before reading paper quality;
- two competent judges could apply the rubric without guessing its intent.

If the problem is ambiguous, show the ambiguity and the adopted interpretation before scoring.
