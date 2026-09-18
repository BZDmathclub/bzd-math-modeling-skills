# CPGMCM 2024 F - X-Ray Pulsar Photon Arrival Times

## Metadata

- Contest: 全国研究生数学建模竞赛
- Problem: F题 X射线脉冲星光子到达时间建模
- Sources: problem DOCX and detailed reviewer guidance PDF
- Ingested: 2026-08-13

## Historical structure

| Category | Points |
|---|---:|
| Abstract/writing/citations | 10 |
| Q1 orbital state | 20 |
| Q2 vacuum geometric delay | 20 |
| Q3 precise delay | 30 |
| Q4 photon simulation | 20 |

## Normalized rules

| ID | Task | Evidence | Points | Caps/anchors |
|---|---|---|---:|---|
| GF24-00 | Whole paper | Abstract includes approach, models, main results and innovation; rigorous readable writing/citations | 10 | Historical combined presentation score |
| GF24-11 | Q1 state model | Complete two-body/Kepler derivation from six orbital elements through rotations | 10 | Unneeded perturbations do not replace requested derivation |
| GF24-12 | Q1 numeric state | Correct GCRS position and velocity with units/precision | 5 | First four significant digits wrong caps at 2/5 |
| GF24-13 | Q1 consistency | Reverse orbital-element recovery, conservation or equivalent quantitative verification | 5 | Text-only verification caps at 2/5 |
| GF24-21 | Q2 geometric-delay model | TT-TDB and GCRS-BCRS transformations, pulsar unit vector, projected path delay | 10 | Respect stated parallel-ray/ignored-body assumptions |
| GF24-22 | Q2 computation | Traceable coordinates and delay result | 10 | If leading delay is not about 277.9 s, item caps at 5/10 |
| GF24-31 | Q3 precise model | Time/coordinate transformations, proper-motion correction, Roemer, Shapiro, gravitational-redshift and special-relativistic clock effects | 20 | Missing other planets caps at 15; missing planets and proper motion caps at 10 |
| GF24-32 | Q3 result analysis | Component delays, total/SSB time and interpretation | 10 | Total outside 473.8840-473.9300 caps at 5; wrong Q2 epoch with correct model loses 3-5 |
| GF24-41 | Q4 photon simulation | Nonhomogeneous-Poisson photon generation, phase computation/folding, curve and distribution | 10 | Verify stochastic model rather than show plot alone |
| GF24-42 | Q4 validation | Compare folded profile with standard profile and quantify similarity | 5 | Correlation or comparable metric expected |
| GF24-43 | Q4 improvement | Concrete implemented accuracy improvement | 5 | Text-only suggestion caps at 2; inverse transform/mixed Gaussian/weighting are examples |

## Learned patterns

- For scientific computation, divide credit among derivation, numerical result, inverse/independent validation and units/precision.
- When the prompt builds from a simplified to a precise model, later points should attach to named correction terms and their quantitative contribution.
- Reference numeric results can support deterministic cap rules when the input is fully fixed, but a correct alternative convention/sign must not be penalized if the prompt asks only magnitude.
- Simulation tasks require distributional validity, transformation/folding, visual output and comparison to a reference—not a plausible-looking curve alone.
- “Improve accuracy” requires an implemented method and comparative evidence; prose suggestions receive limited credit.

## Score distribution calibration

Reviewer guidance provides approximate bands:

| Score | Band | Approximate share | Approximate percentile interval |
|---:|---|---:|---:|
| 70+ | Excellent | 2% | 98-100 |
| 61-70 | Good | 13% | 85-98 |
| 45-60 | Fairly good | 20% | 65-85 |
| 20-44 | Successful entry | 65% | 0-65 |

The document notes that exceptionally strong papers may exceed 75 and that proportions are guidance, not a forced quota. Use as medium-confidence historical calibration for the same contest context. Ordinary non-violating papers start at 20; confirmed cheating/plagiarism is an administrative rule, not a model-quality deduction.
