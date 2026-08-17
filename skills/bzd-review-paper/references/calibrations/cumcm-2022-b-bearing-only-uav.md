# CUMCM 2022 B - Bearing-Only UAV Formation

## Metadata

- Sources: B题 PDF and specialist post-contest article `无人机遂行编队飞行中的纯方位无源定位方案研究`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| B22-11 | Q1(1) observation model | Uses only receiver-measured pairwise bearing angles and known transmitter identities/ideal locations; states coordinate gauge |
| B22-12 | Q1(1) localization | Unified polar/sine-law/geometric equations with branch/ambiguity resolution and uniqueness conditions |
| B22-21 | Q1(2) minimum transmitters | Proves necessity and sufficiency; center+FY01 plus one unknown-ID transmitter is enough under stated geometry |
| B22-22 | Q1(2) identity resolution | Shows how angle pattern distinguishes transmitter identity and candidate receiver branches |
| B22-31 | Q1(3) adjustment protocol | Each round respects FY00 plus at most three circular transmitters, receiver-only angle information and no forbidden sharing |
| B22-32 | Q1(3) convergence/result | Explicit update, step size/stopping rule, concrete sequence on supplied data and final radius/angular-spacing error |
| B22-41 | Q2 formation decomposition | Represents cone formation with identifiable local geometric primitives while preserving intended equal spacing |
| B22-42 | Q2 protocol/convergence | Bearing-only iterative adjustment for all UAVs with feasibility, convergence and final formation-error evidence |

## Negative anchors and validation

- Using coordinates as observations, rather than only to generate allowed angles for simulation, violates the information constraint.
- Do not share angle observations between receivers or let a transmitter simultaneously receive unless the protocol explicitly permits it.
- A nonlinear least-squares fit without a clear geometry, branch analysis and uniqueness argument is incomplete.
- A special-case model for one receiver/transmitter numbering is not a general localization model.
- Validate under perturbations/noise and report convergence behavior, not only the final plotted formation.

## Transferable lessons

- Information constraints are hard modeling constraints: score what each agent knows, transmits and receives.
- Minimum-sensor questions require separate necessity and sufficiency proofs.
- Inverse geometry needs observability/uniqueness and ambiguity-resolution criteria.
- Distributed adjustment should be evaluated by protocol legality, convergence and formation error.

## Limits

No official weights or score distribution were supplied.
