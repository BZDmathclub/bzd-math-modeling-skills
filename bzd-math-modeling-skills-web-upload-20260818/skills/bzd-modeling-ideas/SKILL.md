---
name: bzd-modeling-ideas
description: Generate a coherent, whole-paper mathematical modeling solution framework from a complete contest problem. Use after the user supplies a CUMCM or other modeling problem and asks for modeling ideas, an overall solution plan, question-by-question analysis, candidate-model comparison, model-selection reasons, innovations, validation, or cross-question linkage. For every question, explain the task and mathematical essence, compare multiple feasible models in tables, recommend a route with explicit reasons, and keep all questions connected through shared data, variables, parameters, constraints, and validation.
---

# BZD Modeling Ideas

Produce solution ideas with a whole-problem perspective. Build one coherent paper-level modeling system instead of attaching unrelated model names to separate questions.

This Skill is distilled from the problem statements, scoring rules, reviewer points, review summaries, and complete review workflows of 16 Higher Education Press Cup CUMCM problems from 2020–2025. Use historical materials to learn transferable expectations: complete task coverage, appropriate model choice, cross-question continuity, credible computation, independent validation, and implementable innovation. Never copy a historical model or numerical conclusion into a new problem without current-problem support.

## Input

Require:

- the complete problem statement and every numbered/sub-question;
- attachment descriptions, data dictionaries, figures, notes, and required output files;
- actual attachment data when data inspection affects model choice.

If `bzd-problem-translator` output exists, use its sentence ledger, hidden conditions, input-output table, and cross-question linkage. Otherwise perform an internal sentence-coverage pass before proposing ideas.

Do not invent missing data, coefficients, results, accuracy, or official preferred methods. Mark unavailable information and give conditional branches where it changes the route.

## Required references

Read completely before generating the report:

- [references/integrated-modeling-patterns.md](references/integrated-modeling-patterns.md)
- [references/strategy-output-standard.md](references/strategy-output-standard.md)

## Core workflow

1. Reconstruct the full task graph before analyzing any single question.
2. Extract shared objects, data, indices, variables, parameters, units, coordinate/time systems, constraints, objectives, and evaluation metrics.
3. Identify each question's role: foundation, estimation, explanation, prediction, extension, optimization, decision, or validation.
4. Define interfaces between questions. State which earlier output becomes a later input, parameter, baseline, constraint, initial value, or validator.
5. Design a shared modeling backbone that can run through the whole paper. Preserve physical, statistical, temporal, spatial, recursive, and decision structures when present.
6. For each question, perform the required four-part analysis below and give genuinely distinct candidate models.
7. Compare candidate models on the same task and output. Explain selection from suitability, assumptions, data, interpretability, accuracy, implementation cost, validation, and downstream compatibility.
8. Recommend a paper-level model combination. Avoid selecting locally attractive models that create incompatible definitions or broken data flow across questions.
9. Add verifiable innovations and improvements. Every proposal must state the changed component, implementation, measurable comparison, risk, and fallback.
10. Audit every explicit requirement, sub-question, attachment, deliverable, constraint, and cross-question dependency.

## Required output

Output a Markdown report in the following order.

### 1. 整题建模主线

Explain the research object, central contradiction, final goal, foundational model, and the progression among questions. State the recommended shared backbone and why it can run through the entire paper.

### 2. 跨问题联动链

Provide a Mermaid flowchart showing common data and preprocessing, every question, outputs passed forward, independent branches, feedback/validation links, and the final result. Label arrows with the transferred parameter, data, output, constraint, or evidence. Do not draw a decorative question-number chain.

### 3. 全文统一建模口径

Use a compact table to define shared symbols, index sets, variables, parameters, units, coordinate/time conventions, preprocessing rules, constraints, objectives, and metrics. State which questions use each item.

### 4. 分问题求解思路

For every numbered question, write `问题分析` in this exact sequence.

#### 4.x.1 问题概述

Briefly state:

1. what must be solved;
2. what conditions and inherited results are known;
3. what exact result must be obtained;
4. which mathematical model family the problem essentially belongs to and why.

Separate problem-given conditions from newly introduced assumptions.

#### 4.x.2 总体求解思路

Describe the complete logic from raw data or known conditions to the requested result. Explain the main processing, formulation, solution, and validation steps and how they connect. Identify inputs inherited from earlier questions and outputs supplied to later questions.

#### 4.x.3 可用模型及选型比较

Give at least two genuinely different feasible models when possible; prefer three when meaningful mechanism, statistical, or computational alternatives exist.

| 可行模型/思路 | 模型本质与核心变量 | 完整实现步骤 | 所需数据与假设 | 优点 | 局限与失败风险 | 验证方法 | 与前后问题的接口 | 适用场景 |
|---|---|---|---|---|---|---|---|---|

After the table, provide:

- `推荐模型`：name the primary route;
- `选用理由`：explain task fit, data support, assumptions, required output, scoring concerns, and later-question compatibility;
- `备选模型`：state when another route should replace it;
- `多模型对比建议`：state how to compare models fairly using common data, constraints, metrics, uncertainty, and computational budget.

Do not list models that cannot produce the requested result. Do not treat a solver name as a model. Merge alternatives that differ only by superficial settings.

#### 4.x.4 创新与改进方向

| 创新或改进方向 | 基础方案 | 具体改动与实现步骤 | 预期改进 | 新增工作量 | 验证指标与对照实验 | 风险及备用方案 | 影响的问题 |
|---|---|---|---|---|---|---|---|

Innovations may include mechanism refinement, coupling, adaptive resolution, robust/uncertain formulation, dependence-aware statistics, hybrid solving, error propagation, independent validation, or operational decision improvement. `使用遗传算法`、`模型融合`、`增加可视化`、`考虑更多因素` alone are not innovations.

### 5. 推荐的全文技术路线

Select one coherent combination across all questions. Give the sequence from data reading and exploratory checks through formulation, solution, validation, sensitivity/uncertainty analysis, and required deliverables. Explain why this combination is globally coherent and why alternatives are retained only as comparisons or fallbacks.

### 6. 多模型对比与验证设计

Define fair comparison experiments for important alternatives. Match every important claim to an independent check such as forward reconstruction, conservation/invariance, residual/significance, held-out validation, calibration, sensitivity, uncertainty propagation, convergence, feasibility recomputation, baseline comparison, or high-fidelity audit.

### 7. 论文落地清单

List formulas, algorithms, data tables, result tables, figures, flowcharts, metrics, units, precision, files, and appendix code. Separate mandatory deliverables from optional enhancements.

### 8. 完整性与断链检查

Confirm coverage of every question, sub-question, constraint, attachment, output, and dependency. Identify missing data, unsupported assumptions, incompatible definitions, circular dependence, leakage, unvalidated conclusions, or outputs that cannot feed the next question.

## Quality rules

- Reward fit and completeness, not model prestige.
- Prefer one shared backbone plus justified extensions over unrelated per-question models.
- Preserve feasibility before optimization and verify final schemes in the original system.
- Compare candidate models on identical targets and compatible metrics.
- Reuse shared parameters consistently and propagate uncertainty when later decisions depend on estimates.
- Treat validation as part of each model, not a generic final paragraph.
- Make every table cell implementable; avoid vague steps such as `进行数据处理` or `使用优化算法`.
- State ambiguity and scenario branches rather than silently choosing an interpretation.
- Do not fabricate results or claim that a method is officially preferred.
