# CUMCM 2024 B - Production-Process Decisions

## Metadata

- Sources: B题赛题 PDF and post-contest specialist analysis `生产过程中的决策问题的问题解析`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| B24-11 | Q1 statistical formulation | Correct one-sided hypotheses for reject/accept decisions and binomial/hypergeometric justification |
| B24-12 | Q1 sampling plan | Explicit stopping/decision boundaries satisfying 95% reject and 90% accept requirements while controlling sample effort |
| B24-13 | Q1 operating quality | Discusses type-I/type-II errors, OC curve/claimed-quality level or sequential-plan behavior, including possible nontermination |
| B24-21 | Q2 state/strategy enumeration | Complete feasible detection, assembly, finished-product, disassembly and return/rework decision states |
| B24-22 | Q2 recursive economics | Correct expected flows/cost/revenue/profit through repeated disassembly/reassembly; prevents infinite defective loops |
| B24-23 | Q2 decisions | Six scenario decisions with consistent metric definition and plausibility checks |
| B24-31 | Q3 multistage extension | General state recursion/dynamic program or exact enumeration for m processes/n parts, then correct 2-stage/8-part instance |
| B24-41 | Q4 uncertainty propagation | Replaces known defect rates with point/interval/posterior estimates from sampling and recomputes robust/risk-aware decisions |
| B24-42 | Q4 value of sampling | Shows how sampling design affects production decisions, loss risk and possibly required sample size |

## Negative anchors and caps

- A fixed sample-size formula that ignores the observed defect count does not answer the sequential accept/reject problem.
- Generic genetic/ant/particle-swarm optimization earns little when the underlying state transitions, recursion or objective are incomplete.
- Check elementary lower bounds: costs below unavoidable purchase/assembly cost, negative cost, or implausibly high profit indicate invalid accounting.
- Define the denominator of “average cost/profit” (per purchased set versus per conforming product); inconsistent definitions invalidate comparisons.

## Transferable lessons

- In decision problems, score the stochastic information-acquisition rule separately from the downstream operating policy.
- Rework/recycling creates recursive flows; require termination, conservation and no double-counting.
- Binary decisions alone are not a model: score state transitions, probability flow and economic accounting.
- Uncertain estimated parameters should be propagated into decisions rather than substituted without risk analysis.

## Limits

No official weights or score distribution are present. The article is a strong mechanism/common-error reference, not an official scoring sheet.
