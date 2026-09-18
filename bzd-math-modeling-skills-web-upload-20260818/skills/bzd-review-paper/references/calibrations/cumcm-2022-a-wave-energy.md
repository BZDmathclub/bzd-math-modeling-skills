# CUMCM 2022 A - Maximum Wave-Energy Output

## Metadata

- Sources: A题 PDF and specialist post-contest article `波浪能最大输出功率设计模型及求解`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| A22-11 | Q1 forces/coordinates | Consistent equilibrium-referenced heave coordinates and all mass, added mass, radiation damping, hydrostatic, spring, PTO and excitation terms |
| A22-12 | Q1 coupled dynamics | Correct two-body one-DOF coupled equations with action-reaction signs for linear and nonlinear damping |
| A22-13 | Q1 solution/output | Appropriate analytic/numerical integration, initial conditions, time grid, units, specified times and both spreadsheets |
| A22-21 | Q2 power objective | Instantaneous PTO power from damping law and defensible long-run/steady-cycle average after transient removal |
| A22-22 | Q2 linear optimization | Analytic or verified numerical optimum on [0,100000] with boundary/global checks |
| A22-23 | Q2 nonlinear optimization | Joint coefficient/exponent optimization with solver convergence, repeated runs or dense validation |
| A22-31 | Q3 kinematics/energy | Correct heave-pitch geometry, center-of-mass/inertia, relative displacement/angle and kinetic/potential energy |
| A22-32 | Q3 coupled equations | Complete nonlinear two-body two-DOF equations including translational/rotational PTO, hydrodynamic and restoring terms |
| A22-33 | Q3 numerical solution | Reduces implicit/second-order system correctly, integrates stably, and supplies all requested displacement/velocity outputs |
| A22-41 | Q4 dual power/optimization | Sum of linear and rotational damping power; globally credible 2-parameter optimum with correct bounds and final verification |

## Negative anchors and validation

- Do not optimize transient-average power when the task concerns sustained output; demonstrate the averaging window is in steady state.
- Nonlinear damping must distinguish the coefficient from its velocity-dependent effective damping/force law.
- Check energy balance: input wave work should be consistent with stored, radiated and PTO-dissipated energy.
- A metaheuristic result without repeated seeds, boundary comparison and local/grid confirmation does not support a global maximum claim.
- Coupled signs and reference positions should reproduce stable/physical motion; unbounded energy or phase-inconsistent power signals indicate model errors.

## Transferable lessons

- For energy-harvesting dynamics, score force construction, coupling, solver, steady-state detection, power definition and optimization separately.
- The evaluation horizon is part of the model; justify transient removal and numerical time step.
- Add an energy-balance audit whenever the objective is extracted/dissipated power.

## Limits

No official weights or score distribution were supplied.
