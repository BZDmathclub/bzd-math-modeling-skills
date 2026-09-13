# CUMCM 2025 C - NIPT Timing and Abnormality Classification

## Metadata

- Sources: C题.pdf; 2025赛区评阅评分细则 C表 and supplement; 2025 C题评阅要点
- Authority: contest problem plus regional rubric, supplement and reviewer guidance
- Ingested: 2026-08-13

## Historical structure

| Category | Points |
|---|---:|
| 摘要、论文写作 | 10 |
| Q1 | 30 |
| Q2 | 25 |
| Q3 | 20 |
| Q4 | 15 |
| 特色加分 | up to 10, selection-oriented |

Regional floor/identity rule: identity violation 1; otherwise minimum 20.

## Normalized rules

| ID | Task | Evidence | Points | Key anchors |
|---|---|---|---:|---|
| C25-11 | Q1 association | Correlation process, repeated-measure handling, indices and significance results | 10 | Treating repeated observations as independent inflates false positives |
| C25-12 | Q1 relationship model | Y concentration versus gestational age, BMI and justified indicators | 15 | Weak raw associations make plain multiple linear regression inadequate; consider nonlinear/proportion models |
| C25-13 | Q1 validation | Significance, residual, sensitivity or comparable diagnostics | 5 | Must evaluate model effect, not only fit it |
| C25-21 | Q2 grouping/risk model | Contiguous BMI groups; risk combines successful detection and early timing; clear optimization/decision mechanism | 10 | Direct clustering is not a good default |
| C25-22 | Q2 solution/check | Suitable algorithm, concrete reasonable 3-6 groups, within-group similarity and between-group separation | 10 | State thresholds and optimal time for each group |
| C25-23 | Q2 sensitivity | Measurement-error and grouping sensitivity analysis | 5 | Biological measurement uncertainty is substantive |
| C25-31 | Q3 expanded model | Integrates height, weight, age, attainment proportion and other supported factors | 10 | Explain how secondary factors enter; compare with Q2 is rewarded |
| C25-32 | Q3 solution/check | Clear solution and rationality checks | 5 | Same core requirements as Q2 |
| C25-33 | Q3 sensitivity | Error and stability analysis | 5 | Same core requirements as Q2 |
| C25-41 | Q4 female abnormality model | Mechanism, normal/abnormal difference analysis, relevant factor selection | 10 | Label uses AB aneuploidy; reflect measurement mechanism and applicability |
| C25-42 | Q4 decision method | Clear algorithm, explicit indicator thresholds/rule and quality evaluation | 5 | Report an operational判定方法, not only classifier metrics |

## Repeated-measure and domain anchors

- Accept mixed-effects models, generalized estimating equations, or carefully justified subject-level averaging; mixed effects is strongest. Handle within-subject outlying Y values when averaging.
- Y concentration is proportion data on [0,1]; a logit transformation/appropriate bounded-response model is plausible.
- Pure machine-learning or generic big-data evaluation is inadequate when measurement error, clinical mechanism, risk definition, and interpretability are ignored.
- Do not perform gratuitous cleaning, deletion, or balancing beyond obvious blanks/errors; real biological measurements contain meaningful error.
- For Q4, require abnormal/normal sample difference analysis and an explicit decision threshold or operational rule.

## Learned weighting logic

- Repeated-measure dependence must receive explicit points whenever multiple records belong to the same subject/device/site.
- A grouping task should score risk/objective construction separately from partition output and sensitivity.
- When a later task expands an earlier model, reward integration of new factors and comparative insight, not duplicated exposition.
- In high-stakes classification, score label definition, mechanism, operational threshold, applicability and error analysis—not predictive accuracy alone.
- Domain measurement uncertainty should influence model choice, optimization and sensitivity criteria.

## Limits

No score distribution or official award thresholds were supplied. Medical reference statements are case-specific judging anchors, not clinical advice.
