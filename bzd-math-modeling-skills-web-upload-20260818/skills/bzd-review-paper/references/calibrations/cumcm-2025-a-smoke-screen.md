# CUMCM 2025 A - Smoke-Screen Deployment

## Metadata

- Sources: A题.pdf; 2025赛区评阅评分细则 A表; 2025 A题评阅要点
- Authority: contest problem plus regional rubric and reviewer guidance
- Ingested: 2026-08-13

## Historical structure

| Category | Points |
|---|---:|
| 摘要、论文写作 | 10 |
| Q1 | 25 |
| Q2 | 15 |
| Q3 | 15 |
| Q4 | 15 |
| Q5 | 15 |
| 特色加分 | 5 |

The base task subtotal is 95; innovation supplies up to 5. Contest rule: a paper exposing names or similar identity violations receives 1; otherwise the regional minimum is 20.

## Normalized rules

| ID | Task | Evidence | Points | Key anchors |
|---|---|---|---:|---|
| A25-11 | Q1 motion system | General missile, UAV, projectile, explosion/cloud motion models and correct given-case computation | 15 | Fast calculation preferred; quick search/heuristics alone are weak |
| A25-12 | Q1 occlusion | Geometrically correct occlusion predicate and effective-duration computation | 10 | Protected target is a cylinder; reducing it to one point loses 2-3 |
| A25-21 | Q2 single-device optimization | Explicit variables, feasible domain, objective, optimal direction/speed/drop/detonation and duration | 15 | Declare objective and all decision bounds |
| A25-31 | Q3 three-projectile coordination | Mathematical strategy for one UAV/three projectiles | 10 | Reward joint/overlapping coverage rather than three isolated choices |
| A25-32 | Q3 outputs | Complete feasible strategy, range/timing and result file | 5 | Verify at least 1 s drop interval |
| A25-41 | Q4 multi-UAV motion/results | Three UAV-specific feasible decisions and results | 8 | Each UAV has fixed post-assignment heading/speed |
| A25-42 | Q4 coordination | Joint strategy maximizing union effective coverage | 7 | Avoid double-counting overlapping intervals |
| A25-51 | Q5 assignment/strategy | Joint allocation of up to 15 projectiles across 5 UAVs and 3 missiles | 10 | Respect per-UAV and kinematic constraints |
| A25-52 | Q5 solution analysis | Efficient algorithm, feasible outputs, effective-duration verification | 5 | Missile horizon is only tens of seconds; justify heuristics and runtime |

## Learned weighting logic

- Give the foundational state/geometry model high weight because every later optimization depends on it.
- Separate `physical feasibility + predicate` from `optimization`; an optimizer cannot rescue an invalid simulator.
- As scenario scale increases, score coordination, assignment, interval union, and constraint satisfaction rather than repeatedly rewarding the same motion equations.
- Convert shape language (cylinder), timing limits, speed bounds, fixed heading, and projectile intervals into explicit acceptance tests.
- For time-critical optimization, algorithm complexity and reported runtime are part of solution quality.

## Limits

This record contains no empirical score distribution. The 5 innovation points make the historical total 100 but conflict with the current fixed presentation framework; rebase task ratios for new problems.
