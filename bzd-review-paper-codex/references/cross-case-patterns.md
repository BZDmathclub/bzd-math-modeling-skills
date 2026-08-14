# Cross-Case Rubric Construction Patterns

The Skill knowledge base was distilled from the scoring rules, scoring points, review summaries and complete review workflows of 16 Higher Education Press Cup CUMCM problems from 2020-2025. Bundled calibration files may expose only a task-relevant subset. Treat patterns supported by at least two compatible cases as provisional transferable rules, and treat CUMCM-derived ranking calibration as inapplicable to other contests.

## Stable patterns

1. **Weight dependencies, not question count.** Give foundational models substantial credit when downstream tasks reuse them; later tasks earn additional credit for genuinely new constraints, scale, mechanism or decisions.
2. **Translate every explicit requirement into observable evidence.** Shapes, parameter variability, allowed data, number of groups, timing, speed, quantity, file output and scenario distinctions become rubric checks.
3. **Separate model correctness from result plausibility.** Reference ranges and expected phenomena validate outputs but never replace derivation, algorithms or evidence.
4. **Score validation explicitly.** Cross-condition consistency, forward reconstruction, significance/residual tests, sensitivity, feasibility checks and interval-union verification vary by problem type but serve the same role.
5. **Use negative anchors and caps for tempting shortcuts.** Examples: one-point target geometry, constant refractive index, independent treatment of repeated measures, sequential modeling of coupled decisions, descriptive plots without distribution analysis.
6. **Reward method suitability, not model name.** Officially suggested methods are strong anchors; an alternative can receive full credit when it satisfies mechanism, assumptions, constraints and validation.
7. **Increase weight when a task adds multiple reasoning layers.** A task combining condition derivation, diagnosis, estimation and corrected solution deserves more than a short qualitative extension.
8. **Make computational credibility visible.** Score algorithm steps, convergence/complexity where relevant, reproducibility, constraint satisfaction and runtime feasibility.
9. **Score required deliverables independently.** Classification lists, specified sample tables, spreadsheets, units and precision are contest outputs, not optional presentation details.
10. **Use calibrated numeric caps only for fixed-input tasks.** Reference values and error bands can anchor partial credit when the official material supplies them; do not transfer those numbers to a new dataset.
11. **Treat validation as an independent route back to the model.** Reverse parameter recovery, forward signal reconstruction, held-out prediction, standard-profile comparison and sensitivity are stronger than restating the fitted result.
12. **Separate ordinary quality scoring from misconduct administration.** Preserve contest rules about plagiarism/identity, but never infer misconduct merely from low quality or suspiciously good metrics.
13. **Feasibility precedes optimality.** In physical and planning problems, an infeasible result cannot earn high solution points even if its claimed objective is excellent.
14. **Cross-check artifact against model.** Recompute constraints, accounting, units and selected outputs from spreadsheets/tables; prose claims are not sufficient evidence.
15. **Preserve intertemporal and recursive structure.** Rotation, repeated rework and chained-body motion cannot be safely replaced by independent one-period/local calculations.
16. **Distinguish expert commentary from official scoring.** Use specialist reviews for anchors and failure modes; never invent historical points when no point sheet exists.
17. **Audit approximations on the original system.** Layouts optimized with coarse rays, fitted planes or surrogate predictors require final high-fidelity/original-data evaluation.
18. **Apply invariance and conservation checks.** Direction reversal should not change a symmetric overlap measure; staged optical losses must not remove the same energy twice.
19. **Score numerical resolution.** Ray density, spatial discretization, candidate neighborhoods and terrain partitions require convergence/error evidence when they affect results.
20. **Respect information and observability.** Agent knowledge, sensor outputs, unknown identities and coordinate gauges define what can be inferred; forbidden information invalidates a solution.
21. **Detect constrained data geometry.** Compositions, proportions, repeated subjects and other structured samples require suitable transformations/dependence handling before generic statistics.
22. **Expose counterfactual assumptions.** Reconstructing an unobserved pre-state without paired data is not ordinary prediction; score identifiability, assumptions and uncertainty.
23. **Audit energy/probability/state balance.** Coupled dynamic power, recursive production flows and staged optical losses should satisfy appropriate conservation identities.

## Problem-type routing

- **Dynamic optimization/control:** prioritize state/geometry model, feasibility predicate, objective, coordination, assignment, efficient solution and verified union performance.
- **Physical measurement/inverse problem:** prioritize mechanism derivation, variable parameter estimation, signal algorithm, identifiability, multi-condition consistency and forward validation.
- **Statistical/biomedical decision:** prioritize dependence structure, measurement error, appropriate response model, risk/objective construction, interpretability, thresholds and sensitivity.
- **Data-driven operations:** prioritize cleaning choices, time/distribution structure, decision coupling, operational constraints and plausible decisions.
- **End-to-end machine learning/experimental data:** prioritize feature rationale, dependence/design balance, leakage-free validation, calibrated errors, required test outputs and downstream optimization validity.
- **Scientific timing/simulation:** prioritize coordinate/time systems, units, correction terms, deterministic precision, stochastic validity and independent reference-profile comparison.
- **Geometric chain/trajectory:** prioritize path parameterization, recursive kinematics, physical collision predicates, event refinement and piecewise continuity.
- **Quality-control/production policy:** prioritize hypothesis and stopping rules, probability/state flows, recursive rework accounting, policy comparison and uncertainty propagation.
- **Multi-period resource planning:** prioritize complete hard constraints, linearization/state coupling, machine-checked feasibility, objective recomputation, solver evidence and risk scenarios.
- **Optical field design:** prioritize coordinate/ray geometry, staged loss accounting, finite receiver/source integration, high-fidelity recomputation and design constraints.
- **Coverage-route design:** prioritize invariant coverage definitions, direction rationale, boundary/interior construction, original-terrain audit and separate coverage/overlap/length metrics.
- **Coupled energy dynamics:** prioritize force/energy consistency, steady-state detection, numerical integration, power definition and credible global parameter optimization.
- **Bearing-only/distributed localization:** prioritize legal observations, observability, ambiguity resolution, minimum-sensor proof, protocol legality and convergence.
- **Compositional classification:** prioritize closure/log-ratio preprocessing, dependence-aware splits, unpaired reconstruction limits, clustering stability and differential association.

## Weight-generation procedure under the current 100-point framework

1. Reserve abstract 10 and formatting 10.
2. Put 70-75 into assumptions, construction and solution, allocating by dependency, centrality, difficulty and required outputs.
3. Put the remaining 5-10 into problem-relevant validation, sensitivity, evaluation, generalization or innovation.
4. Use nearest historical cases only as ratios/anchors; reconstruct criteria from the new problem wording.
5. Declare every borrowed pattern and its confidence. The 16-problem CUMCM knowledge base supports broader provisional rules, not universal contest laws or non-CUMCM ranking distributions.
