# CUMCM A—E Problem-Type Review Prompts

Use this reference only after reading the complete current problem. These are historically distilled review prompts from 2021—2025, not prescribed answers. The current task always controls; a different method earns full credit when it is correct, suitable, evidenced and complete.

## A: engineering mechanism and numerical simulation

- Trace geometry/physics, state variables, governing equations, numerical method, optimization and engineering verification.
- Check full-object collision, coverage, visibility or interception criteria rather than center-point shortcuts.
- Require initial/boundary conditions, units, step size, tolerance, convergence and post-rounding feasibility.
- Penalize unjustified geometric simplification, black-box optimization and absent discretization checks.

## B: limited observation, inference and decision

- Audit observable, forbidden and latent information before judging methods.
- Check identifiability, uniqueness, degeneracy, noise sensitivity and cross-condition consistency.
- Match transformations and likelihoods to proportions, angles, spectra, spatial grids or defect counts.
- Require inference to become a concrete experiment, measurement, inspection, adjustment or production decision.

## C: special data structure and verifiable decision

- Identify structural zeros, missingness, compositional constraints, repeated measures, time order, hierarchy and cross-period dependence.
- Require a data-generation explanation and real transfer of outputs between questions.
- Check leakage, unsuitable ordinary correlation/regression/clustering, and separation of prediction from decision.
- Independently recompute objectives and hard constraints from the final submitted solution.

## D: dense rules and dynamic systems

- Translate natural-language rules into states, events, decisions, transitions, capacities and priorities.
- Prefer a general model plus the supplied-data solution; check static-to-dynamic and disruption-to-replanning inheritance.
- Do not accept arbitrary weighted sums when business objectives have lexicographic priority.
- Require executable schedules, sequences, coordinates or routes and perform rule/numeric/plan audits.

## E: data semantics, trustworthy validation and deployment

- Verify field meaning, sample unit, timestamp, label origin and prediction-time availability.
- Match validation to structure: stratified, grouped by subject, rolling time, or held-out region/scenario.
- Detect future leakage, near-duplicate subject leakage, imbalance, missing labels and model/sample-size mismatch.
- Require model outputs to support concrete production, monitoring, control or training actions.

## Cross-problem scoring rule

For every explicit question, independently freeze and score `模型建立`, `模型求解`, and `结果与回答`. Historical red flags may generate checks only when the current prompt and paper evidence make them relevant. Do not deduct merely because the paper does not use a historically common model.
