# Strategy Output Standard

## Concise question statement

For each question state:

- `任务`: action and object, not copied prose;
- `已知`: supplied conditions and inherited outputs only;
- `输出`: exact numerical, categorical, functional, graphical, or file deliverable;
- `本质`: mathematical structure plus justification.

Never mix added assumptions into known conditions.

## Required per-question sequence

For every question, keep this order:

1. `问题概述`: task, known conditions, requested result, model essence and justification;
2. `总体求解思路`: complete path from input to output and its cross-question interfaces;
3. `可用模型及选型比较`: genuinely distinct models, recommendation, reasons, fallback, and fair comparison design;
4. `创新与改进方向`: implementable change, measurable benefit, validation, risk, and fallback.

Do not begin with model names before establishing the problem structure.

## Feasible route standard

A route must specify variables/states, mechanism/formulation, assumptions/data, computation, output, validation, and cross-question interfaces. Avoid model-name lists. Merge routes that are not genuinely different.

After comparing routes, always state the recommended model and explain selection using task fit, data support, assumptions, output requirements, interpretability, validation, computational cost, and compatibility with later questions. State when the fallback becomes preferable.

## Innovation standard

An implementable innovation may improve:

- mechanism fidelity;
- coupling, risk, constraints, or multi-objective formulation;
- acceleration, decomposition, adaptive resolution, or hybrid solving;
- dependence-aware statistics, uncertainty, calibration, or leakage prevention;
- independent validation, invariance, conservation, or high-fidelity audit;
- operational interpretation or robust decision quality.

Every innovation needs a baseline, changed component, measurable comparison, and fallback. Complexity alone is not innovation.

## Whole-paper coherence checks

- One notation, coordinate, time, and unit system?
- Shared parameters estimated once and reused consistently?
- Each later question declares inherited outputs and new additions?
- Hard constraints verifiable?
- Uncertainty propagated to later decisions?
- Each optimum/prediction independently checked?
- Every requested table/file producible?
- Alternatives compared on the same target and metric?

## Table rules

- Make cells implementable; avoid `进行数据处理` or `使用优化算法`.
- Put assumptions and failure risks beside advantages.
- Put interfaces in every route row.
- Keep innovations separate from ordinary required work.
- For subquestions, retain one main section while distinguishing outputs.
