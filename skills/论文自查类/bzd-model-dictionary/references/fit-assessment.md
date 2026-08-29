# Model-to-Problem Fit Assessment

Judge the selected model on the following independent dimensions.

| Dimension | Questions |
|---|---|
| Task alignment | Does the model solve the actual task: description, inference, prediction, classification, ranking, optimization, simulation, control, or explanation? |
| Observation unit | Is the modeled unit consistent with the data? Are repeated persons, sites, devices, panels, time points or spatial neighbors dependent? |
| Target and output | Does the model output the quantity requested by the problem, including uncertainty, feasible decisions or operational thresholds? |
| Data sufficiency | Are sample size, event count, feature count, class balance, coverage and measurement resolution adequate? |
| Assumptions | Are distribution, independence, stationarity, linearity, proportional hazards, convexity, smoothness or other requirements plausible and testable? |
| Leakage and causality | Are future information, duplicate subjects, target-derived variables or post-outcome features improperly used? Are causal claims stronger than the design permits? |
| Constraints and mechanism | Does the formulation preserve units, conservation laws, geometry, capacity, timing, integrality and other hard constraints? |
| Validation | Can the result be checked with suitable residuals, held-out/grouped/rolling validation, stability, convergence, sensitivity, baselines or simulation? |
| Interpretability | Is the explanation adequate for the competition question and domain stakes? |
| Computation | Can the model be solved reproducibly within available time and resources? Are convergence and randomness controlled? |
| Paper completeness | Can the team explain assumptions, formulation, solution, parameter selection, results, checks, limitations and reproducibility? |

## Verdict rules

- `合适`: task/output align, core assumptions are supported, data are sufficient, validation is feasible, and no major structural defect exists.
- `有条件合适`: the model is usable only after specific preprocessing, dependence handling, constraint additions, threshold design, validation or combination with another model.
- `不合适`: it solves a different task, violates a central data structure or hard constraint, or cannot yield the required result even after reasonable adjustment.
- `证据不足，待人工复核`: essential data facts or model identity are unavailable or ambiguous.

Do not average these dimensions mechanically. A single fatal mismatch can determine the verdict. Avoid claiming causality from association, generalization from in-sample fit, or optimality from a heuristic result without a bound or comparison.

## Metric routing

- Classification: Accuracy only with class balance context; also Precision, Recall, F1, ROC-AUC, PR-AUC, confusion matrix, calibration and group-aware validation where relevant.
- Regression: R², RMSE, MAE, MAPE only when denominators are valid, residual diagnostics and grouped/out-of-sample validation.
- Time series: stationarity, residual white noise, rolling-origin validation, horizon-specific error and structural-break checks.
- Clustering: silhouette, DBI, CH, stability, interpretability and whether clusters form usable intervals/segments.
- Optimization: constraint feasibility, objective recomputation, convergence, runtime, repeated runs, baseline and optimality gap or best-known comparison.
- Evaluation/ranking: weight sensitivity, ranking stability, consistency and redundancy among indicators.
- Dynamic/numerical models: stability, error order, convergence, conservation/invariance and observed/simulation comparison.

