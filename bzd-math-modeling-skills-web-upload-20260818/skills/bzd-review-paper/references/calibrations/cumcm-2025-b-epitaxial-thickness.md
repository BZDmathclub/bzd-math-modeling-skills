# CUMCM 2025 B - Epitaxial-Layer Thickness

## Metadata

- Sources: B题.pdf; 2025赛区评阅评分细则 B表; 2025 B题评阅要点
- Authority: contest problem plus regional rubric and reviewer guidance
- Ingested: 2026-08-13

## Historical structure

| Category | Points |
|---|---:|
| 摘要、论文写作 | 10 |
| Q1 physical model | 25 |
| Q2 algorithm/reliability | 25 |
| Q3 multi-beam extension | 40 |
| Innovation | reference only |

Regional floor/identity rule: identity violation 1; otherwise minimum 20.

## Normalized rules

| ID | Task | Evidence | Points | Key anchors |
|---|---|---|---:|---|
| B25-11 | Q1 refractive index | Wavelength-dependent refractive-index estimation model | 10 | Treating it as a constant is unacceptable even if results look close |
| B25-12 | Q1 thickness physics | Thickness relation correctly includes incidence angle, refractive index and interference geometry | 15 | Derivation and assumptions required |
| B25-21 | Q2 computation | Computes wavelength-dependent index and thickness on both SiC datasets | 10 | Reference thickness 7-8 µm is a plausibility check, not answer-only proof |
| B25-22 | Q2 algorithm quality | Practical, automatic, noise-robust and consistent algorithm | 5 | No manual intervention; two angles should agree closely |
| B25-23 | Q2 reliability | Independent reliability analysis, preferably forward-reconstructing reflectance and comparing observations | 10 | A number inside the reference range alone is insufficient |
| B25-31 | Q3 condition | Derives necessary multi-beam interference conditions | 10 | Explain physical mechanism; large layer/substrate index ratio is relevant |
| B25-32 | Q3 refractive models | Estimates layer and substrate refractive indices from supplied attachments | 10 | External data is disallowed |
| B25-33 | Q3 diagnosis | Determines and justifies whether multi-beam interference occurs | 10 | Silicon data should show it; provide data evidence |
| B25-34 | Q3 corrected model/result | Builds appropriate thickness model/algorithm and reports verified results | 10 | Silicon reference 3-4 µm; address SiC influence if claimed |

## Learned weighting logic

- In mechanism/measurement problems, divide credit among physical derivation, parameter identification, numerical algorithm, and independent reliability verification.
- An explicit statement that a parameter varies forbids an unjustified constant simplification; encode it as a critical anchor or cap.
- When the same specimen is measured under multiple conditions, cross-condition consistency is a built-in validation criterion.
- Reference numeric ranges are plausibility anchors, never substitutes for derivation or reproducibility.
- Give a later extension more weight when it requires condition derivation, phenomenon diagnosis, new parameter estimation, and corrected computation.
- Treat data-source restrictions as hard constraints; correct-looking answers obtained using forbidden external data do not earn full credit.

## Limits

No score distribution was provided. Named physical reference ranges are problem-specific.
