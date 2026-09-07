# BZD 数模竞赛端到端工作流

## 一、完整路线

```text
完整赛题与附件
├─ bzd-problem-translator：逐句题意、隐藏条件、跨问联动
├─ bzd-modeling-ideas：全题主线、多模型方案、创新与验证
└─ bzd-problem-restatement：论文第一章初稿（可与前两项并行）
             ↓
候选模型 + 实际数据结构
└─ bzd-model-dictionary：模型适配、假设、缺陷、检验、替代模型
             ↓
数模智能体 / Codex / Claude Code / 人工建模
└─ 数据处理、代码求解、结果验证、论文写作
             ↓
章节专项自查
├─ bzd-abstract-checker
├─ bzd-problem-restatement
├─ bzd-problem-analysis-checker
├─ bzd-model-assumption-checker
├─ bzd-symbol-notation-checker
├─ bzd-model-solution-checker
├─ bzd-reference-appendix-checker
└─ bzd-ai-usage-disclosure
             ↓
终稿闸门
├─ bzd-paper-aigc-auditor
├─ bzd-paper-format-checker（严格）
└─ bzd-review-paper（导入同版本格式报告）
             ↓
最终得分、竞争位次与优先修改建议
```

## 二、阶段路由表

| 阶段 | 优先 Skill | 必要输入 | 核心输出 | 下一阶段条件 |
|---|---|---|---|---|
| 刚拿题 | translator + modeling-ideas | 完整赛题、附件说明/数据 | 题意报告、全题建模路线 | 任务、约束和跨问接口清楚 |
| 论文起稿 | problem-restatement | 完整赛题 | 第一章初稿 | 与题目一致且不提前求解 |
| 模型选型 | model-dictionary | 题目、数据、候选模型、用途 | 适配结论和替代模型 | 数据与假设可满足 |
| 建模求解 | 外部求解环境 | 题目、数据、选定路线 | 代码、结果、验证、论文 | 结果可复现并回答题目 |
| 初稿自查 | 章节专项 Skills | 对应章节及其依赖材料 | 分章节问题和修改建议 | 严重问题已修复 |
| 快速总检 | paper-format-checker | 完整论文 | 全文格式与呈现风险 | 决定后续专项检查 |
| 中期评估 | review-paper（不严格格式） | 题目、论文、竞赛信息 | 临时得分和主要短板 | 仅作修改方向参考 |
| 终稿检查 | AIGC auditor + strict format | 最终PDF/Word、赛题、可选代码 | AI痕迹与严格格式报告 | 文件版本冻结 |
| 最终评审 | review-paper | 同一版本题目、论文、格式报告 | 最终评审HTML | 提交前人工复核 |

## 三、并行与串行关系

- 可并行：题意翻译、建模思路初稿、问题重述初稿。
- 建议串行：模型思路 → 模型字典适配 → 代码求解。
- 可分章节并行：摘要、重述、分析、假设、符号、正文、文献附录检查。
- 必须后置：最终严格格式审查和最终综合评审。
- 严格格式报告与最终评审必须对应同一论文版本。

## 四、返工触发

- 题意解释改变：建模思路、重述、问题分析及后续结果全部复核。
- 数据清洗改变：模型参数、结果、图表、摘要和结论复核。
- 核心模型改变：符号、代码、验证、摘要和AI披露复核。
- 最终结果改变：摘要、正文表格、图、附录和评审重新核对。
- PDF重新导出：严格格式、匿名信息和元数据重新检查。

## 五、快速模式与完整模式

### 快速模式

适合比赛中期：`problem-translator → modeling-ideas → model-dictionary → review-paper（不严格格式）`。

### 完整模式

适合终稿：完成全部章节专项自查，再运行 AIGC 审计、严格格式审查和最终综合评审。

