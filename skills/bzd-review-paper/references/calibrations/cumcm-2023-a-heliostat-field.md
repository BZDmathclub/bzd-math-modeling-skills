# CUMCM 2023 A - Heliostat-Field Optimization

## Metadata

- Sources: A题赛题 PDF and specialist post-contest analysis `定日镜场的优化设计`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| A23-11 | Q1 solar/geometry | Correct sun position, incident/reflected vectors, mirror normal and coordinate conventions at all prescribed dates/times |
| A23-12 | Q1 efficiency factors | Correct cosine, shadow-blocking, atmospheric, truncation and reflectivity factors without duplicate loss accounting |
| A23-13 | Q1 shadow/blocking | Three-dimensional candidate-neighbor selection and ray/mirror intersection or equivalent area computation |
| A23-14 | Q1 truncation | Models cylindrical receiver and finite solar cone or justified converged discretization; computes accepted reflected energy |
| A23-15 | Q1 aggregation | Correct DNI, area-weighted field power, monthly/yearly averages and unit-area output in required tables |
| A23-21 | Q2 design model | Tower location, common mirror size/height/count/layout variables; 60 MW constraint and unit-area objective |
| A23-22 | Q2 physical constraints | Circular boundary, 100 m exclusion, 2-8 m sides, width>=height, 2-6 m height, ground clearance and center spacing |
| A23-23 | Q2 optimization/evidence | Reproducible search with feasible spreadsheet, recomputed power, objective and sensitivity/discretization evidence |
| A23-31 | Q3 heterogeneous design | Mirror-specific dimensions/heights/positions with all Q2 physics and meaningful benefit over homogeneous design |
| A23-32 | Q3 complexity control | Explains parameterization/reduction, computational cost and verifies every mirror-level constraint/output |

## Negative anchors and validation

- Shadow/blocking and truncation must use the energy remaining at the relevant stage; do not count the same blocked ray twice.
- A center-ray or parallel-ray-only truncation calculation is incomplete when the problem explicitly describes conical sunlight, unless approximation error is quantified.
- Optical efficiency, total power and power per mirror area are different objectives; do not substitute one for another.
- Meeting 60 MW on a coarse surrogate is not sufficient: recompute the submitted layout using the final optical model.
- Report convergence with respect to mirror/solar-cone discretization and candidate-neighbor radius.

## Transferable lessons

- For ray/energy systems, score coordinate geometry, loss components, numerical integration and aggregation separately.
- Define the denominator and ordering of multiplicative efficiencies to prevent double counting.
- A design optimization must be audited using the same or a higher-fidelity simulator than the optimizer used.
- Heterogeneous-design freedom deserves points only when each element remains feasible and improves the declared objective.

## Limits

The article provides reference modeling and results but no official weights or score distribution. Do not infer historical points.
