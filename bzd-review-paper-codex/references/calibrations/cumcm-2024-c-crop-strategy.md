# CUMCM 2024 C - Crop Planting Strategy

## Metadata

- Sources: C题赛题 PDF and post-contest specialist review `农作物的种植策略赛题评述`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| C24-11 | Q1 variables/economics | Area/activation/sales variables and correct profit accounting for waste and 50%-discount scenarios |
| C24-12 | Q1 hard constraints | Land compatibility, seasons, capacity, no consecutive cropping, three-year legume coverage and water/greenhouse rules |
| C24-13 | Q1 management constraints | Explicit concentration/minimum-area measures that make plans operable without imposing unsupported full-land use |
| C24-14 | Q1 solution/deliverables | Feasible 2024-2030 plans, spreadsheets, independently recomputed production/sales/profit and solver gap/status |
| C24-21 | Q2 uncertainty model | Correct ranges/trends and dependence over years for demand, yield, cost and price |
| C24-22 | Q2 risk decision | Stochastic/robust/scenario formulation or well-designed simulation with explicit risk measure and feasible plan |
| C24-23 | Q2 evaluation | Scenario/sensitivity distribution of profit, feasibility and comparison with deterministic plan |
| C24-31 | Q3 dependence | Defensible crop substitution/complementarity and demand-price-cost dependence, with simulated-data generation documented |
| C24-32 | Q3 coupled optimization | Incorporates dependence into the optimization rather than changing inputs informally |
| C24-33 | Q3 comparison | Quantified comparison with Q2 in profit, risk, crop mix, feasibility and management burden |

## Negative anchors and caps

- A submitted schedule violating any mandatory agronomic constraint is not a valid optimization result, regardless of claimed objective value.
- Model, algorithm and spreadsheet must agree; independently recompute all constraints and profits.
- Solving each year/season separately generally misses rotation and three-year legume coupling.
- Do not assume all land must be planted; idle land may be optimal when excess production has low/no value.
- A heuristic without feasibility checks, computational resources, benchmark/gap and repeated experiments cannot support optimality claims.
- A formal MIP abandoned in favor of an unrelated heuristic does not earn full model-solution credit.

## Transferable lessons

- For large planning problems, allocate substantial points to machine-checkable feasibility before objective quality.
- Separate hard constraints from soft management preferences and expose their trade-off.
- Require solver status/bound/gap for mathematical programming and benchmark statistics for heuristics.
- Multi-year decisions must preserve intertemporal coupling.
- Uncertainty and correlation tasks need reproducible scenario generation plus out-of-sample/risk evaluation.

## Limits

The article reports evaluation practices and common failures but no official point allocation or score distribution. Do not infer historical weights.
