# Changelog

## Unreleased

### bzd-paper-format-checker

- 新增「中国研究生数学建模竞赛（华为杯）」特别规则：识别华为杯后，页面结构/摘要页/正文起始页以当届官方规范为准、不套用国赛固定页序；目录与英文摘要是否要求以当届规范为准；附录页数阶梯继续适用；不按题号字母预设题型。
- `agents/openai.yaml` 与 `format-review-rules.md` 同步补充华为杯分支。

### bzd-problem-translator

- 新增 `scripts/render_html.py`：把已完成的题意逐句翻译报告渲染为单文件 HTML。正文与全部表格静态渲染，断网可读；仅 Mermaid 流程图依赖 CDN，加载失败时页面给出提示并自动展开图源码。
- 渲染器内置结构校验：表格数、标题数、单行格数与表头不一致，流程图丢失，或存在未渲染的 Markdown 时拒绝写出并以非零码退出。
- `md-output-standard.md` 补充「Optional HTML rendering」一节，明确渲染器依赖的格式前提（单 H1、表格分隔行、`\|` 转义、`<br>` 换行、免责提示行与应用题版之间留空行分块）。
- 明确交付边界：Markdown 仍是默认且唯一必需交付物，HTML 只是同一份报告的视图，仅在用户另行要求时生成，不得替代 Markdown 或在其中补充 Markdown 没有的内容。

## 2026-09-07 — 2026-09-18（已推送，未打版本标签）

补记 v1.0.0 之后已入库但此前未记录的变更。

### 全流程

- 新增全流程总控 skill，各 skill 补充 CUMCM 题型专用参考。

### bzd-problem-translator

- 新增华为杯（中国研究生数学建模竞赛，CPGMCM）「小学应用题式题意还原」层，置于报告最前，用于降低题面进入成本。
- 新增 `references/cpgmcm-plain-language-translation.md`：改写方法、场景选材表、可简化与必须保住的边界、四块必需输出（一句话版、小学应用题版、术语生活化映射表、背景知识补课卡）与交付前自检。
- 新增 `references/cpgmcm-translation-signals.md`：CUMCM 与 CPGMCM 对比、题面质量问题的处理口径、六类结构内核（按题面特征匹配，不按题号字母）。
- 新增赛事识别小节，并确立三条底线：附加而非替代逐句表、术语映射第三列必须交代类比丢失了什么、免责提示行原文保留。
- `md-output-standard.md` 将 `## 0. 小学应用题式题意还原` 纳入标题顺序（仅华为杯），并新增五项华为杯专项核验行。

### bzd-review-paper

- 判分改为证据中心架构，新增 `references/evidence-centered-scoring.md`。
- 新增 AI 时代专项扣分项；同步调整 `rubric.md`、`rubric-construction.md`、`atomic-deduction-scoring.md` 与格式规范。

### 其他 skill

- `bzd-model-solution-checker`、`bzd-paper-format-checker`、`bzd-reference-appendix-checker` 同步更新评分与格式规则细节，并补充论文分节自查表。

## Collection v1.0.0 - 2026-08-18

- 将三个数学建模 Skills 合并到统一仓库；
- 新增 `skills/` 标准目录；
- 新增完整工作流、统一安装说明和调用示例；
- 保留原 `BZD-review-paper` 兼容目录，避免影响已有使用者。

### Included Skills

- `bzd-problem-translator`
- `bzd-modeling-ideas`
- `bzd-review-paper`
