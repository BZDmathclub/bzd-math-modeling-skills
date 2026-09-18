# CUMCM 2022 C - Ancient-Glass Composition

## Metadata

- Sources: C题 PDF and specialist post-contest statistical review `古代玻璃制品成分分析与鉴别的统计建模`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| C22-01 | Composition preprocessing | Applies 85%-105% validity rule, principled nondetect replacement, closure to 100% and CLR/ILR or justified compositional method |
| C22-11 | Q1 categorical association | Contingency analysis of weathering versus type/pattern/color with chi-square assumptions and Fisher/exact correction where needed |
| C22-12 | Q1 composition changes | Separates glass types, tests multivariate/univariate weathering differences on transformed composition and controls assumptions/multiplicity |
| C22-13 | Q1 pre-weather prediction | States unpaired/counterfactual limitation, uses distribution matching or justified covariate model, inverse-transform closure and uncertainty/sensitivity |
| C22-21 | Q2 main-type rules | Removes/stratifies weathering effect, identifies discriminating components and reports interpretable high-potassium versus lead-barium rules |
| C22-22 | Q2 subtype clustering | Unsupervised feature selection, justified cluster count and artifact-level consistency for multiple sampling points |
| C22-23 | Q2 validation | Internal indices plus stability/noise sensitivity; avoids treating a supervised score as proof of unsupervised truth |
| C22-31 | Q3 unknown classification | Applies identical preprocessing, respects weathering strata, produces explicit labels with probabilistic/distance evidence |
| C22-32 | Q3 sensitivity | Reclassifies after de-weathering/noise/alternative plausible preprocessing and reports stability |
| C22-41 | Q4 associations | Type-specific compositional association method after log-ratio transformation and significance/uncertainty assessment |
| C22-42 | Q4 differential comparison | Quantifies how association structures differ between glass types rather than listing two correlation matrices |

## Negative anchors and validation

- Raw percentages are closed compositional data; ordinary Pearson correlations can create spurious negative dependence.
- Missing/nondetected components cannot simply be left as zero before logarithms; replacement choice requires sensitivity.
- There are no paired before/after measurements for the same weathered point. Ordinary supervised before-value prediction is unjustified without strong declared assumptions.
- PCA components are dimension reduction, not automatically meaningful component selection for clustering.
- Multiple sampled parts from one artifact are dependent and should not be split across train/test or conflicting subtypes without explanation.

## Transferable lessons

- Detect constrained data geometry (composition, simplex, proportions) before choosing statistics.
- Score preprocessing validity and data leakage at the artifact/subject level.
- Counterfactual reconstruction without paired labels must expose identifiability assumptions and uncertainty.
- For clustering, score feature choice, cluster number, internal quality, domain interpretability and stability separately.

## Limits

No official weights or score distribution were supplied. Reference chemical patterns are problem-specific.
