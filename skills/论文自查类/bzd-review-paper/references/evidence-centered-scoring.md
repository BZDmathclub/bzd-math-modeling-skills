# 2026 Evidence-Centered Paper Scoring

Use this standard for the paper-quality rubric. AI can cheaply produce complete-looking processes and numerical outputs, so reward modeling judgment, evidence, reproducibility and insight rather than model-name prestige or procedural length.

## 1. Mandatory questions

For every major modeling decision, ask:

1. 为什么这样抽象问题？
2. 为什么必须选这个模型？
3. 为什么不选择更简单的模型？
4. 数据是否真的支持模型复杂度？
5. 关键参数和约束从哪里来？
6. 结果是否经过独立证据验证？

Do not require the paper to use these exact sentences. Score whether nearby text, equations, data, citations, experiments or appendices provide a substantive answer.

## 2. Model-independent requirement matrix

Before reading the paper for quality, extract and freeze:

- 必须回答的核心任务；
- 不可违反的题目条件；
- 必须输出的结果；
- 结果成立必须具备的证据；
- 必须处理的数据问题；
- 必须验证的风险；
- 各问之间必须传递的信息；
- 方案可实施所需的约束。

Do not freeze a preferred algorithm as the answer. Historical solutions and problem-letter patterns may identify omissions or risks, but a different method receives full consideration when it satisfies the same requirements with valid evidence.

## 3. Required 100-point architecture

| Category | Nominal points |
|---|---:|
| 摘要与成果概括 | 10 |
| 论文规范与可读性 | 10 |
| 核心问题回答 | 75 |
| 全文整体性与应用价值 | 5 |
| **Total** | **100** |

The core problem-answering score must remain within the user's required 70–80 range; use 75 by default. Its dimensions are fixed as follows:

| Core dimension | Points | Judge question |
|---|---:|---|
| 任务理解与数学抽象 | 12 | 是否抓住主要矛盾，而非仅复述题目 |
| 模型选择的必要性 | 14 | 为什么选择该模型，复杂度是否必要 |
| 假设、参数与约束证据 | 12 | 每项设定是否有题目、数据或文献依据 |
| 推理链与跨问题联动 | 12 | 输入—模型—输出是否闭合，各问是否真实联动 |
| 求解真实性与可复现性 | 10 | 参数、代码、算法配置和结果能否复现 |
| 检验、反证与稳健性 | 10 | 是否主动寻找模型失效情形 |
| 洞察、创新与实际价值 | 5 | 是否产生超出计算结果的有效认识 |
| **Total** | **75** | |

Distribute each dimension across the actual questions using the frozen requirement matrix. Keep the existing per-question views of `模型建立`, `模型求解`, and `结果与回答` as evidence-location tags, not as a competing second set of weights. Every core criterion must belong to exactly one of the seven dimensions and one problem/task, while its evidence may appear in any of the three locations.

Apply the existing 90% judge ceiling to every numeric criterion. Keep judge reserve separate from paper defects.

## 4. What the seven dimensions require

### 4.1 任务理解与数学抽象 — 12

Reward identification of the decision object, state variables, mechanisms, scales, objectives, boundaries and essential simplifications. Mere restatement, generic background or copying the prompt does not demonstrate abstraction.

### 4.2 模型选择的必要性 — 14

Require a task-specific reason for the chosen model and a proportionate complexity argument. Ask whether a simpler baseline would solve the same task. Complexity, fashionable algorithms, ensembles and renamed combinations do not earn points by themselves.

When a complex method is used, require evidence that:

- the task needs the added capability;
- the sample size and data quality support it;
- parameters are identifiable or estimable;
- a simpler baseline was considered or compared where feasible;
- the improvement is stable and practically meaningful.

### 4.3 假设、参数与约束证据 — 12

Trace assumptions, parameter values, boundary conditions and constraints to the problem, data, defensible domain reasoning, a verifiable source or a disclosed estimation procedure. Penalize convenient constants and constraints whose effect is not examined.

### 4.4 推理链与跨问题联动 — 12

Audit the complete chain from raw conditions and data through intermediate outputs to conclusions. A claimed dependency earns no credit unless the earlier output actually enters the later model with consistent symbols, units and scale.

### 4.5 求解真实性与可复现性 — 10

Require enough detail to reproduce material results: preprocessing rules, algorithms, parameters, initialization, solver settings, stopping rules, random control where relevant, intermediate outputs and consistency with code or appendices. Do not equate polished pseudocode with reproducibility.

### 4.6 检验、反证与稳健性 — 10

Reward attempts to disconfirm the model: baseline comparison, out-of-sample checks, residual diagnostics, constraint audits, boundary cases, perturbations, uncertainty and failure regions. A self-generated result checked only by the same model is not independent validation.

### 4.7 洞察、创新与实际价值 — 5

Reward new information produced by the model, such as a threshold, turning point, bottleneck, stable interval, failure condition, transferable decision rule or a justified unconventional abstraction. Do not require novelty for ordinary correctness, and do not reward cosmetic renaming or unsupported innovation claims.

## 5. Abstract composition requirement

For every problem paragraph in the abstract, use these ranges as diagnostic proportions rather than mechanical word-count targets:

- 10–20%: describe what the subproblem asks and its essential condition;
- 50–60%: describe the modeling and solution chain;
- 20–30%: state the result and conclusion.

The abstract must stand independently from the body. If one or more problem paragraphs omit the corresponding problem statement so a reader cannot know what was solved, apply one post-score penalty of 5 points and identify every affected paragraph. Do not deduct 5 repeatedly for the same abstract-level root defect. Continue to score missing methods or results under the ordinary abstract criteria.

## 6. AI-era post-score penalties

Apply these only after calculating the ordinary 100-point raw score and before the format-quality multiplier. Display them in a separate ledger so they are not hidden inside atomic deductions.

### 6.1 Unexplained equation or symbol occurrence: −5 each

For every materially separate equation or local formula block, inspect the preceding page, current page and following page. Apply a 5-point penalty when either:

- the body gives no nearby explanation of what the equation represents, why it is introduced or how it connects to the task; or
- a symbol necessary to understand that equation is neither defined on first use nor explained in nearby prose, an equation annotation or a directly connected local table.

- A global symbol table does not satisfy first-use explanation in the body.
- Defining only some symbols does not cure the undefined material symbols.
- Group several consecutive equations that share the same undefined-symbol root cause as one occurrence; do not multiply penalties for every repeated glyph.
- Record page, equation number or visible formula cue, the missing equation explanation and/or the undefined symbols.
- Do not penalize universally obvious mathematical constants or standard operators unless the paper assigns them a special meaning.

This penalty targets unreadable compressed modeling exposition, not the mere presence of an equation.

### 6.2 Major evidence-integrity failure: −10

Apply 10 points only for a distinct severe issue not already fully captured by the equation-symbol penalty, such as a central result that cannot be traced to any stated model/data, a fabricated-looking unsupported parameter chain, or a claimed validation whose evidence contradicts the result. State the evidence and avoid alleging misconduct without verification.

Do not double-punish the same root defect under both the atomic ledger and post-score ledger. If the ordinary criterion already deducted for a local weakness, use a post-score penalty only when the defect is a repeated, paper-wide AI-era presentation failure or independently severe integrity failure.

## 7. Narrative comprehensibility gate

Read the paper as an informed outsider who has not worked on the problem and is not a specialist in the paper's chosen method. Ignore the symbol table during this pass and ask whether the body itself tells a coherent modeling story:

- what is being modeled;
- why each mathematical object is introduced;
- what each equation means;
- how one step leads to the next;
- what the computed result means for the original task.

If the full paper is understandable, it may compete above 80 subject to all other evidence. If persistent missing definitions or logical jumps make the central model impossible to understand after reading the nearby pages, cap the paper-quality raw score after post-score penalties at **49.9**. A few awkward sentences do not trigger the cap; the failure must affect understanding of the central solution chain. Give representative page-level evidence and explain which links cannot be reconstructed.

This is a comprehension gate, not a writing-style preference. Dense but fully defined technical writing may pass; fluent AI-style prose with missing mathematical links may fail.

## 8. Calculation order

1. Freeze the model-independent requirement matrix and 100-point rubric.
2. Apply the 90% judge ceiling and ordinary atomic deductions.
3. If eligible, apply the existing low-score bottom-up safeguard.
4. Apply the separately listed AI-era post-score penalties.
5. Apply the narrative comprehensibility cap of 49.9 when triggered.
6. The resulting value is the reported `原始得分`.
7. Apply the existing format-quality multiplier to obtain `论文质量最终得分`.
8. Keep CUMCM region, school, division and advisor competitiveness adjustments separate from paper quality.

Never let post-score penalties produce a negative raw score: floor at 0. Do not use competition-context factors to cancel or intensify these paper-quality deductions.
