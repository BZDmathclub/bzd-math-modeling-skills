# Mathematical Modeling Paper Rubric

Use these anchors only as fallback guidance. The problem-specific rubric and learned official rules control the actual weights. Score intermediate quality proportionally; do not default to the midpoint.

Read [evidence-centered-scoring.md](evidence-centered-scoring.md). Use its fixed `10 + 10 + 75 + 5` structure and seven core dimensions. Within each problem, label evidence as `模型建立`, `模型求解`, or `结果与回答`, but do not create a second competing set of weights. Deduct 1-3 points separately for every unmet atomic item and floor at zero. A different but valid and evidenced approach does not trigger a deduction.

## Fixed-category anchors

### Abstract — 10 points

Read and apply [title-abstract-keywords.md](title-abstract-keywords.md) completely. A completed abstract without a major defect starts at 3 points. Award 7-8 only when it passes the lay-reader test and communicates the concrete problem, work, models and results. Reserve 9-10 for complete, specific, concise and body-consistent task-method-result coverage.

### Formatting compliance — 10 points

Read and apply [formatting-standard.md](formatting-standard.md) completely. Run its eligibility gate first. If eligible, start at 10 and deduct 1-3 per error, retaining severe deductions down to a normalized score of -10. Convert that score linearly to the `0-1.00` format-quality coefficient and apply it to the raw 100-point score. Do not double-count title/keyword defects already considered under the abstract/front-matter review.

| Category/dimension | Weight | Full-credit evidence |
|---|---:|---|
| 摘要与成果概括 | 10 | 独立说明各问的问题、方法、结果与结论 |
| 论文规范与可读性 | 10 | 页面、格式、图表、公式与叙事均清晰合规 |
| 任务理解与数学抽象 | 12 | 抓住主要矛盾并建立任务特定的数学对象 |
| 模型选择的必要性 | 14 | 解释为何选用该模型、为何需要其复杂度并考虑简单基线 |
| 假设、参数与约束证据 | 12 | 关键设定可追溯至题目、数据、文献或估计过程 |
| 推理链与跨问题联动 | 12 | 输入—模型—输出闭合且各问存在真实信息传递 |
| 求解真实性与可复现性 | 10 | 预处理、参数、算法设置、中间结果与附件足以复现 |
| 检验、反证与稳健性 | 10 | 有基线、诊断、边界、扰动、不确定性或失效条件证据 |
| 洞察、创新与实际价值 | 5 | 得到阈值、瓶颈、规律、决策规则或可靠的新认识 |
| 全文整体性与应用价值 | 5 | 形成可理解、可执行且前后一致的完整建模故事 |
| **Total** | **100** | |

## Score anchors

- 90–100: exceptional, correct, deeply validated, reproducible, and competition-leading.
- 80–89: strong and complete, with limited weaknesses that do not undermine the core result.
- 70–79: competent, but important gaps in validation, justification, completeness, or communication.
- 60–69: plausible core attempt with major deficiencies or weak evidence.
- 50–59: substantial work, but serious correctness, task-fulfillment, or reproducibility problems.
- 0–49: fundamentally incomplete, invalid, or unsupported.

## Caps and penalties

Apply the narrowest justified cap and explain it; do not double-punish the same defect.

- Cap total at 69 if a required major task is absent.
- Cap total at 59 if the central model is mathematically invalid or results cannot support the main conclusion.
- Cap total at 49 if the artifact contains no substantive model/result or is largely unreadable.
- Deduct 2–10 points for material internal inconsistencies, fabricated-looking/untraceable evidence, or serious citation failures, proportional to impact. Describe suspicious evidence; do not declare misconduct without verification.
- Do not penalize unavailable source code by itself unless reproducibility is a stated contest requirement; score the reproducibility evidence present in the paper.

After ordinary scoring and any eligible low-score safeguard, apply the separate AI-era penalties and informed-outsider comprehensibility cap in `evidence-centered-scoring.md`. These must be shown separately and supported by page/formula evidence.

## Award and position estimate

Read and apply [award-ranking-output.md](award-ranking-output.md). Use its 2025 score anchors, continuous percentile interpolation, uncertainty band, award interpretation, evaluation-date warning and required closing notice.
