# CUMCM 2024 A - Bench Dragon

## Metadata

- Sources: A题赛题 PDF and post-contest specialist review article `板凳龙运动轨迹模型的分析研究`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| A24-11 | Q1 head motion | Correct equidistant-spiral arc-length/ODE relation for constant 1 m/s head speed |
| A24-12 | Q1 body recursion | Robust recursive geometric solution for all 224 handle centers, correct long/short handle spacing and branch selection |
| A24-13 | Q1 velocity | Rigid-body/tangent-based velocity recursion or differentiated constraints, with numeric verification |
| A24-14 | Q1 deliverables | Complete per-second spreadsheet and specified time/body-point tables with units and six decimals |
| A24-21 | Q2 collision | Geometrically valid oriented-rectangle collision predicate for nonadjacent benches; accounts for width and end overhang |
| A24-22 | Q2 terminal event | Locates first collision boundary accurately; bisection/event search preferred over one-second stepping |
| A24-31 | Q3 minimum pitch | Feasibility test for entering the 9 m turning region and monotone/bisection search for minimum pitch |
| A24-41 | Q4 S-turn geometry | Two tangent arcs satisfy spiral tangency, mutual tangency and radius relation; proves or optimizes path shortening |
| A24-42 | Q4 piecewise motion | Continuous position/velocity propagation across inbound spiral, arcs and outbound spiral plus required outputs |
| A24-51 | Q5 maximum speed | Uses linear velocity-scaling property or verified search so every handle remains at most 2 m/s |

## Transferable lessons

- For chained rigid-body geometry, score path parameterization, recursive constraints, velocity propagation and numerical branch stability separately.
- Collision must be tested on physical shapes, not only handle-center distance; accept segment intersection, point-in-rectangle or separating-axis methods when complete.
- Event time and threshold parameters deserve continuous refinement; grid stepping without error control is a partial-credit method.
- Piecewise paths require continuity checks at every tangent junction.
- Repeated spreadsheet outputs are substantive reproducibility/deliverable criteria.

## Limits

The review article supplies reference models and alternatives but no official weights or score distribution. Use it to generate evidence anchors, not historical point claims.
