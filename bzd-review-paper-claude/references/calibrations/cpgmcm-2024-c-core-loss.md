# CPGMCM 2024 C - Data-Driven Magnetic Core Loss

## Metadata

- Contest: 中国研究生数学建模竞赛
- Problem: C题 数据驱动下磁性元件的磁芯损耗建模
- Sources: problem DOCX and official/reviewer scoring guidance PDF
- Ingested: 2026-08-13

## Historical structure

| Category | Points |
|---|---:|
| Overall writing | 10 |
| Q1 waveform classification | 15 |
| Q2 Steinmetz correction | 20 |
| Q3 factor/interaction analysis | 25 |
| Q4 cross-condition prediction | 20 |
| Q5 multi-objective optimization | 10 |

## Normalized rules

| ID | Task | Evidence | Points | Critical anchors |
|---|---|---|---:|---|
| GC24-00 | Whole paper | Abstract contains methods/results/conclusions; clear rigorous writing and citations | 10 | Historical combined writing score |
| GC24-11 | Q1 feature engineering | Distribution statistics plus waveform-shape features | 5 | Distribution 2; slope/segment/shape规律 3 |
| GC24-12 | Q1 supervised classification | Suitable supervised model and held-out validation | 5 | Unsupervised classification earns zero for model item |
| GC24-13 | Q1 required outputs | Correct test labels, counts, specified sample table and attachment | 5 | Missing requested outputs loses 3-5 |
| GC24-21 | Q2 baseline SE | Estimation method, three coefficients, baseline error | 6 | Each component 2 |
| GC24-22 | Q2 temperature correction | Explicit corrected equation and estimated coefficients | 8 | Equation 6; coefficients 2; no estimates earns no coefficient credit |
| GC24-23 | Q2 comparative error | Fair same-data comparison using mean relative error | 6 | <=0.16 strong; 0.16-0.25 medium; implausibly low is suspicious |
| GC24-31 | Q3 balanced reconstruction | Justified resampling/balancing across factor levels and sample-size discussion | 6 | Needed to address unbalanced experimental combinations |
| GC24-32 | Q3 assumptions | Log transform, normality and homoscedasticity checks | 7 | Ignoring failed assumptions sharply limits credit |
| GC24-33 | Q3 effects | Main effects, pairwise interactions and effect ranking | 8 | Analyzing only main effects or partial interactions caps this plus optimum at half |
| GC24-34 | Q3 optimum | Supported factor levels minimizing loss | 4 | Reference anchors: sine and material 4; temperature effect may be weak |
| GC24-41 | Q4 prediction model | Clear model, feature rationale and cross-material/waveform applicability | 8 | Black-box input-output use without modeling rationale loses credit |
| GC24-42 | Q4 generalization | Held-out validation, mean relative error, generalization and engineering meaning | 6 | <=16% strong; 16-25% medium; above weak |
| GC24-43 | Q4 required predictions | Accuracy of ten specified samples and complete attachment output | 6 | 8+ within 10% is strong; stated bands govern partial credit |
| GC24-51 | Q5 multi-objective model | Explicit loss/energy objectives, variables, constraints and trade-off | 3 | Do not collapse competing objectives without justification |
| GC24-52 | Q5 solution | Reproducible optimization process | 4 | Must use Q4 model coherently |
| GC24-53 | Q5 result | Feasible Pareto/compromise result and interpretation | 3 | Report temperature, frequency, waveform, peak flux and material |

## Learned patterns

- In end-to-end data-science problems, score feature construction, model validation and required test-set deliverables separately.
- When experimental factor combinations are unbalanced, allocate explicit points to sampling/design correction before inference.
- Statistical factor analysis must score assumptions, main effects, interactions, effect magnitude and optimum separately.
- Use error thresholds as calibrated anchors, but flag implausibly excellent results as possible leakage or invalid evaluation.
- A later optimization using a learned predictor must inherit its valid domain and uncertainty; score the multi-objective trade-off rather than a single arbitrary scalar optimum.

## Score distribution calibration

Reviewer guidance gives approximate bands for the reviewed population:

| Score | Band | Approximate share | Approximate percentile interval |
|---:|---|---:|---:|
| 80+ | Excellent | 2% | 98-100 |
| 65-79 | Good | 13% | 85-98 |
| 45-64 | Fairly good | 20% | 65-85 |
| 20-44 | General/weak valid entry | 65% | 0-65 |

Use only as a broad, medium-confidence historical calibration for this contest/problem context. Judges were explicitly not required to reproduce the proportions. Non-cheating entries start at 20; confirmed plagiarism/cheating follows contest rules and is outside ordinary quality scoring.
