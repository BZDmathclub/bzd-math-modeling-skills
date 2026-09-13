# Integrated Modeling Patterns

Apply these historical patterns only when supported by the current problem.

## Cross-question architectures

| Progression | Typical linkage | Planning rule |
|---|---|---|
| mechanism -> computation -> precision | later questions add corrections | keep one state/frame and compare added terms |
| description -> estimation -> prediction -> decision | parameters/predictor feed choices | propagate domain and uncertainty |
| single case -> multi-agent/stage | simulator reused at scale | add coordination, assignment, union, recursion, complexity |
| deterministic -> uncertain -> robust | parameter status changes | preserve constraints; add scenarios/distributions/risk |
| one-factor -> multi-factor | later task personalizes/extends | retain an operational output and compare improvement |
| classification -> optimization | prediction controls decisions | prevent leakage and audit decisions under error |

## Problem-family routes

- **Dynamic optimization/control:** state and geometry -> feasibility -> objective -> control/assignment -> solver -> verified performance. Check signs, transients, conservation, bounds, runtime.
- **Physical inverse/measurement:** mechanism -> variable parameters -> identifiability -> multi-condition estimation -> forward reconstruction.
- **Statistical/biomedical:** observational unit -> dependence -> missing/failure mechanism -> response support -> uncertainty -> interpretable risk/threshold.
- **Experimental data:** feature construction -> design balance -> assumptions/interactions -> held-out generalization -> required outputs -> downstream optimization.
- **Planning/production:** state transition -> complete constraints -> accounting -> exact/heuristic solution -> feasibility/objective recomputation -> uncertainty.
- **Geometry/coverage:** coordinates -> paths/shapes -> recursion -> physical predicate -> event refinement -> resolution audit -> union accounting.
- **Distributed information:** knowledge/measurement protocol -> observability -> ambiguity -> legality -> convergence.

## Meaningful alternative axes

- mechanism-first analytic versus simulation-first numerical;
- interpretable parametric versus flexible nonparametric;
- exact programming versus decomposition/heuristic search;
- deterministic point estimate versus probabilistic/robust decision;
- aggregate versus hierarchical/individual model;
- low-fidelity screening versus high-fidelity final audit.

Each route must answer the same output and state what later questions reuse.

## Common断链 failures

- Incompatible parameters, coordinates, units, objectives, or feasibility definitions across questions.
- Using later outcomes to construct earlier groups/features.
- Optimizing a surrogate without original-system reevaluation.
- Treating repeated measures as independent or splitting one entity across folds.
- Solving multi-year, multi-stage, or multi-agent tasks independently despite state coupling.
- Double-counting overlap, energy, material, probability, cost, or profit.
- Claiming optimality without boundaries, convergence, repeated runs, gap, or neighborhood evidence.

## Independent validation routes

- inverse recovery or forward reconstruction;
- conservation/probability/state balance;
- symmetry, direction, and unit invariance;
- held-out entity/time/scenario validation;
- residual, significance, calibration, and interval coverage;
- noise, parameter, preprocessing, grouping, and discretization sensitivity;
- solver gap, repeated seeds, local/dense confirmation, boundary comparison;
- exported-file feasibility and objective recomputation;
- high-fidelity audit of coarse/surrogate optima.
