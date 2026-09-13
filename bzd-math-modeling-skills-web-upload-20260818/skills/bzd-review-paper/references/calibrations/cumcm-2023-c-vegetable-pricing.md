# CUMCM 2023 Problem C - Vegetable Pricing and Replenishment

## Metadata

- Contest: 高教社杯全国大学生数学建模竞赛（CUMCM）
- Year: 2023
- Division/track: 广东赛区评阅材料；C题
- Problem title: 蔬菜类商品的自动定价与补货决策
- Source set: `C题.pdf`; `2023C高教社杯全国大学生数学建模竞赛C题评分细则.doc`; `2023-C题评阅细则补充说明.docx`; `出题人评阅综述.docx`
- Source authority: contest problem plus regional judging rubric/supplement and problem-author review summary
- Date ingested: 2026-08-12
- Completeness: problem and three judging documents available; legacy DOC table was partially recovered and cross-checked against the complete supplement

## Source-preserved scoring structure

The historical rubric uses a framework different from the Skill's current default:

| Historical category | Points |
|---|---:|
| 摘要、论文写作 | 10 (摘要与写作各5) |
| 问题1 | 25 |
| 问题2 | 35 |
| 问题3 | 25 |
| 问题4 | 5 |
| Total | 100 |

Do not misrepresent this as `摘要10 + 格式10`. Preserve it for historical scoring. For a newly generated rubric under the current user standard, retain the task-point ratios and evidence anchors but rebase the task block into 70-75 points after assigning abstract 10 and formatting 10.

## Normalized scoring rules

| Rule ID | Problem task | Category | Observable evidence | Historical points | Explicit/inferred | Confidence |
|---|---|---|---|---:|---|---|
| C23-00 | Whole paper | Abstract/writing | Standard, complete, clear, attractive presentation; abstract and paper writing each 5 | 10 | explicit | high |
| C23-11 | Q1 data preparation | Model solution/data | Handles anomalies, discounts, returns, and zero-sale items clearly and reasonably | 5 | explicit | high |
| C23-12 | Q1 distribution | Model construction/solution | Gives category and item distributions; models time effects; discusses/fits distribution types | 15 | explicit | high |
| C23-13 | Q1 association | Model construction/validation | Analyzes category/item association with method assumptions; testing earns stronger credit | 5 | explicit | high |
| C23-21 | Q2 demand-price-replenishment relation | Model construction | Qualitative and quantitative relation; mechanism/economic law; uses loss rates to infer historical replenishment | 10 | explicit | high |
| C23-22 | Q2 joint decision optimization | Model construction/solution | Uses Q1 distributions and newsvendor logic for a correct stochastic joint pricing-replenishment optimization; clear suitable algorithm; time effects | 20 | explicit | high |
| C23-23 | Q2 outputs | Model solution/results | Gives plausible daily category replenishment and pricing for July 1-7; distinguishes weekdays/weekends | 5 | explicit | high |
| C23-31 | Q3 substitutability/complementarity | Model construction | Identifies substitute/complement item groups, e.g. association-based subclassification/dimension reduction | 7 | explicit | high |
| C23-32 | Q3 diversity constraints | Model construction | Quantifies variety and expresses demand/diversity constraints, potentially with binary variables | 8 | explicit | high |
| C23-33 | Q3 item optimization | Model construction/solution | Distinguishes item-level from category-level decisions; valid selection, replenishment, pricing model and solution; respects 27-33 SKUs and 2.5 kg minimum | 10 | explicit | high |
| C23-41 | Q4 new data | Problem-specific supplementary | Proposes operational, external, and consumer data and explains how each improves models | 3 | explicit | high |
| C23-42 | Q4 feasibility | Problem-specific supplementary | Evaluates collection feasibility and economics, preferably with model/data support | 2 | explicit | high |

## Partial-credit and cap anchors

- Q1 that contains only descriptive statistics and visualization, without distribution law and deeper analysis, is generally capped at 10/25.
- Q2 that uses only simple regression/fitting for the coupled pricing-replenishment relation is generally capped at 7/10 for C23-21.
- Give priority to papers that: model temporal distribution effects in Q1; use mechanism-based coupling and stochastic/newsvendor optimization in Q2; compare models or optimization schemes in Q3.
- Deduct materially when correlation methods ignore assumptions, especially Pearson without normality/linearity considerations.
- Treat separated forecast-then-price pipelines as weak when they fail to represent coupled price-demand-replenishment decisions.

## Weight rationale learned from the problem

| Task | Historical share | Why it was weighted this way |
|---|---:|---|
| Q1 exploratory distribution/association foundation | 25 | Supplies stochastic demand structure used downstream; distribution analysis is the dominant work (15/25) |
| Q2 category-level joint optimization | 35 | Central business decision and hardest coupled stochastic optimization; core model alone is 20 points |
| Q3 constrained item-level optimization | 25 | Adds discrete selection, diversity, substitute/complement relations, and operational constraints |
| Q4 data recommendations | 5 | Short qualitative extension; must still connect proposed data to model improvement and collection cost |

This case demonstrates dependency-aware weighting: Q1 is not merely descriptive because its distributions feed Q2; Q2 receives the highest weight because it is the central coupled decision; Q3 receives substantial weight because it changes decision granularity and adds combinatorial constraints.

## Problem-author review evidence

Common high-impact failures include:

- missing or unreasonable cleaning of sales gaps and abnormal wholesale prices;
- mean-filling non-sales records and thereby distorting demand/profit;
- shallow distribution analysis without seasonality, holidays, or probability fitting;
- correlation measures used without applicability tests;
- pricing and replenishment modeled independently instead of jointly;
- ignoring variety when interpreting “meet category demand”;
- unclear decision variables/optimization structure and unexplained metaheuristics;
- implausible profit, pricing, or replenishment results and no weekday/weekend distinction.

These observations explain what the formal criteria are intended to detect and may be used as negative anchors for similar retail inventory-pricing problems.

## Transfer rules for new problems

1. Convert each explicit subquestion into independently observable scoring items; a single subquestion may require data treatment, formulation, solution, and output criteria.
2. Give greater weight to a task when its results are prerequisites for later optimization.
3. For data-driven problems, allocate explicit points to anomaly/missing/zero/return handling when those choices materially affect demand estimates.
4. When the problem states coupled decisions, reward a joint mechanism-based model; cap shallow sequential fits if they break the coupling.
5. Turn every numeric operational statement in the prompt into an explicit scoring constraint.
6. Require result plausibility and scenario distinctions explicitly signaled by dates, weekdays, seasons, or operating conditions.
7. Score “collect more data” tasks by both usefulness to a named model component and acquisition feasibility/economics.
8. Treat recommended methods and reference distributions as judge anchors, not mandatory algorithms, unless the source explicitly requires them; mathematically sound alternatives remain eligible for full credit.

## Rebase example under the current framework

When creating a new rubric patterned on this case, do not add 20 presentation points on top of the historical 90 task points. Rebase the four-task block proportionally into the selected model/supplement allocation. For example, if model construction/solution is 75 and supplementary Q4 is 5, allocate Q1-Q3 proportionally from historical `25:35:25` into 75 (approximately `22:31:22`) and retain Q4 as 5, then refine internal points from the new problem's actual demands. This is a starting calculation, not a substitute for problem decomposition.

## Conflicts and limits

- Historical presentation weighting (10 combined) conflicts with the current default (abstract 10 plus formatting 10). Preserve the historical score when reproducing 2023 judging; use the current framework for newly generated rubrics unless the user directs otherwise.
- The regional supplement names reference best-fit distributions. Use them to evaluate this problem, not as universal vegetable-demand laws.
- No complete contest score distribution or award cutoff was supplied, so this record does not calibrate percentile rankings.
