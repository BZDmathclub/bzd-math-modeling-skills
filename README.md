# BZD Math Modeling Skills

面向数学建模竞赛的 BZD Skills 合集，支持 **Codex** 与 **Claude Code**。

本项目围绕数学建模竞赛的完整流程持续研发，目前覆盖赛题理解、建模思路生成、模型选型、论文分章节自查、全文格式检查、综合评审、竞赛位次预估和高校国奖数据查询等场景。

相关 Skills 主要基于 2020—2025 年高教社杯全国大学生数学建模竞赛赛题、评分细则、评分要点、评阅概述及完整评阅流程进行整理和蒸馏，并结合 2026 年竞赛论文格式与 AI 工具披露要求持续更新。

> 本项目不是竞赛官方工具。所有模型建议、论文得分、位次预测和备赛建议仅供参考，最终应以当届组委会及赛区发布的正式规则为准。

## 三个核心 Skills

| Skill | 核心作用 | 主要输入 | 主要输出 |
|---|---|---|---|
| [`bzd-model-dictionary`](skills/论文自查类/bzd-model-dictionary/) | 查询模型字典并判断候选模型是否适合当前题目与数据 | 赛题、数据结构、候选模型、求解思路 | 模型档案、适配性结论、使用条件、缺陷、检验方法和替代模型 |
| [`bzd-review-paper`](skills/论文自查类/bzd-review-paper/) | 根据本次赛题重新制定百分制细则，并以评委视角评审整篇论文 | 竞赛类型、完整赛题、完整论文；国赛可补充组别、赛区、学校和指导教师 | 原始得分、格式质量系数、最终得分、位次估计、逐项扣分和 HTML 报告 |
| [`bzd-paper-format-checker`](skills/论文自查类/bzd-paper-format-checker/) | 对整篇论文的结构、排版和各章节格式合规性进行一次总检 | 完整 PDF；可选 Word 文档 | 格式检查报告、逐项扣分、格式规范分、格式质量系数和自查表 |

### bzd-model-dictionary

`bzd-model-dictionary` 是基于 **BZD数模社·数模模型字典** 构建的模型查询与选型自查 Skill。

用户提供赛题、数据结构、候选模型和求解思路后，Skill 会查询该模型的适用场景、数据要求、关键假设、输入输出、禁忌点、模型缺陷和检验方法，并结合当前任务判断模型选择是否合理。

适配性结论分为：

- **合适**：模型与题目目标、数据结构和变量类型基本匹配；
- **有条件合适**：模型方向合理，但需要补充预处理、假设检验或适用条件；
- **不合适**：模型与任务目标、数据类型或核心假设明显冲突；
- **证据不足**：当前信息不足，无法作出可靠判断。

除适配性结论外，Skill 还会推荐可替代或配套使用的同类模型，帮助使用者减少机械套用模型的情况。

### bzd-review-paper

`bzd-review-paper` 使用近五年国赛评阅资料和完整评阅流程进行归纳和蒸馏。每次评审时，Skill 会重新读取当前赛题、分解任务并独立制定评分细则，不沿用历史对话中的既有解题思路或评价结论。

每一道问题均拆分为：

1. **模型建立**；
2. **模型求解**；
3. **结果与回答**。

各板块先执行 90% 得分封顶，再根据当前赛题的评分细则逐条检查：局部轻微缺失扣 1 分，实质性缺失或明显不一致扣 2 分，核心步骤错误、无法复现或严重影响该板块扣 3 分，最低扣至 0 分。若某一板块根本答非所问、违反核心条件且没有成立的替代论证，可将该板块直接判为 0 分。

格式规范分统一为 `-10～10`，并线性映射为 `0～1.00` 的格式质量系数：

```text
格式质量系数 = (格式规范分 + 10) / 20
最终得分 = 原始得分 × 格式质量系数
```

若用户已经运行同版本论文的 `bzd-paper-format-checker`，`bzd-review-paper` 可以直接接入其格式得分、资格审查结果和页码证据，避免重复检查和重复扣分。

> 创新盲区提示：每年都有少量论文因解题路径高度新颖而获得较高评价。AI评审可能无法充分识别超出常规评阅预期的原创方案，因此存在低估非常规创新路径的可能。

### bzd-paper-format-checker

`bzd-paper-format-checker` 用于整篇论文的格式与写作规范总检，主要检查：

- 摘要是否超过规定页面，能否独立阅读；
- 页码、正文起始页、目录、页眉页脚和页面结构；
- 标题层级、编号连续性、字号、字体、行距和缩进；
- 图题、表题、三线表、公式编号、公式标点和图表重复表达；
- 正文篇幅与各问题篇幅分配是否合理；
- 图表、公式与正文是否存在必要的引出、说明和分析；
- 匿名信息、PDF元数据、隐藏批注和修订记录；
- 参考文献、附录、支撑材料和程序呈现的格式完整性。

> **使用边界：** `bzd-paper-format-checker` 主要检查各板块是否按照论文规范组织和呈现，属于“全文格式总检”。它不会替代各章节专项 Skill 对内容正确性、逻辑完整性和专业质量的深入检查。若需要详细检查摘要、问题重述、问题分析、模型假设、符号说明、模型建立与求解、AI工具披露、参考文献或附录，仍建议分别调用对应的专项 Skill。

## Skills 分类

### 一、综合评审与自我定位类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-review-paper`](skills/论文自查类/bzd-review-paper/) | 根据赛题制定评分细则并完成论文综合评审 | 竞赛类型、赛题、论文；国赛可补充组别、赛区、学校和指导教师 | 得分、格式质量系数、竞赛位次、详细扣分和 HTML 报告 |
| [`bzd-cumcm-school-awards`](skills/综合评审与自我定位类/bzd-cumcm-school-awards/) | 查询高校五年国奖数据并评估个人备赛差距 | 学校名称、赛区和个人竞赛经历 | 高校国奖画像、2026 年预测和备赛建议 |

### 二、生成类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-problem-translator`](skills/生成类/bzd-problem-translator/) | 逐句翻译赛题，识别隐含条件和跨问题关系 | 完整赛题及附件说明 | 题意翻译报告、跨问题联动链 |
| [`bzd-modeling-ideas`](skills/生成类/bzd-modeling-ideas/) | 生成贯穿全文的建模主线并比较可行模型 | 完整赛题、附件、可选题意报告 | 多模型比较、选型理由、创新与验证方案 |
| [`bzd-problem-restatement`](skills/生成类/bzd-problem-restatement/) | 根据赛题生成问题重述，也支持已有重述自查 | 完整赛题；自查时另提供已有重述 | 问题背景、问题回顾、研究综述或自查报告 |
| [`bzd-ai-usage-disclosure`](skills/生成类/bzd-ai-usage-disclosure/) | 生成或检查 AI 工具使用声明与使用详情 | 论文、真实 AI 使用情况、已有披露材料 | AI工具使用声明、使用详情材料和自查结果 |

### 三、论文自查类

建议先使用 `bzd-paper-format-checker` 完成全文格式总检，再根据发现的问题调用对应的章节专项 Skill。

| 推荐顺序 | Skill | 自查对象 | 输入 | 输出 |
|---:|---|---|---|---|
| 1 | [`bzd-paper-format-checker`](skills/论文自查类/bzd-paper-format-checker/) | 全文结构、排版及各章节格式规范 | 完整 PDF；可选 Word | 全文格式报告、扣分明细、格式规范分和自查表 |
| 2 | [`bzd-abstract-checker`](skills/论文自查类/bzd-abstract-checker/) | 摘要、题目和关键词的内容质量 | 摘要；可选赛题、题目和关键词 | 独立性判断、逐项诊断和优先修改建议 |
| 3 | [`bzd-problem-restatement`](skills/论文自查类/bzd-problem-restatement/) | 问题重述 | 完整赛题和已有问题重述 | 任务遗漏、条件失真、章节越界和修改建议 |
| 4 | [`bzd-problem-analysis-checker`](skills/论文自查类/bzd-problem-analysis-checker/) | 问题分析 | 完整赛题、附件说明和已有问题分析 | 任务映射、跨问联动、问题清单和修改优先级 |
| 5 | [`bzd-model-assumption-checker`](skills/论文自查类/bzd-model-assumption-checker/) | 模型假设 | 完整赛题、模型假设；可选模型正文 | 逐条诊断、遗漏假设、验证要求和修改优先级 |
| 6 | [`bzd-symbol-notation-checker`](skills/论文自查类/bzd-symbol-notation-checker/) | 符号说明 | 完整论文，或符号表与模型正文 | 符号遗漏、冲突、单位、上下标和版式诊断 |
| 7 | [`bzd-model-solution-checker`](skills/论文自查类/bzd-model-solution-checker/) | 模型建立、求解、检验和灵敏度分析 | 完整赛题、论文；可选附件或代码 | 核心正文诊断、复现检查和优先修改建议 |
| 8 | [`bzd-ai-usage-disclosure`](skills/论文自查类/bzd-ai-usage-disclosure/) | AI工具使用声明与使用详情 | 论文、真实AI使用记录、已有披露材料 | 完整性、一致性、匿名性和责任边界检查 |
| 9 | [`bzd-reference-appendix-checker`](skills/论文自查类/bzd-reference-appendix-checker/) | 参考文献与附录 | 论文、参考文献、附录、程序和支撑材料 | 引用与附录检查、风险等级和修改建议 |
| 10 | [`bzd-model-dictionary`](skills/论文自查类/bzd-model-dictionary/) | 模型选型及适用性 | 赛题、数据、候选模型和求解思路 | 字典信息、适配性结论、缺陷、检验方法和替代模型 |
|11 | [`bzd-paper-aigc-auditor`](skills/论文自查类/bzd-paper-aigc-auditor/) | 论文AI痕迹与建模模板化审计 | 完整数模论文；可选赛题、代码、数据和AI使用记录 | AI风格风险区间、逐板块证据、模型真实性分类和修改建议 |
| 12| [`bzd-review-paper`](skills/论文自查类/bzd-review-paper/) | 完整论文综合评审 | 竞赛类型、完整赛题和完整论文 | 综合得分、格式系数、预估位次、评委评价和修改顺序 |

### 四、数据查询与备赛辅助类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-cumcm-school-awards`](skills/综合评审与自我定位类/bzd-cumcm-school-awards/) | 查询高校历史国奖数据并评估备赛距离 | 学校、赛区、竞赛经历和模拟情况 | 学校画像、国奖预测、省奖与国奖备赛建议 |

## 推荐工作流

```mermaid
flowchart LR
    A["完整赛题"] --> B["bzd-problem-translator"]
    B --> C["bzd-modeling-ideas"]
    C --> D["bzd-model-dictionary"]
    D --> E["完成代码与论文"]
    E --> F["bzd-paper-format-checker"]
    F --> G["章节专项自查 Skills"]
    G --> H["bzd-review-paper"]
    H --> I["得分、位次与修改建议"]
```

## 安装

### Codex

下载仓库后，将需要使用的具体 Skill 文件夹复制到：

```text
Windows：%USERPROFILE%\.codex\skills\
macOS/Linux：~/.codex/skills/
```

例如：

```text
.codex/skills/
├── bzd-model-dictionary/
├── bzd-paper-format-checker/
├── bzd-review-paper/
└── 其他需要使用的 Skill/
```

### Claude Code

将需要使用的具体 Skill 文件夹复制到：

```text
项目目录/.claude/skills/
```

安装时应直接复制 `bzd-...` 文件夹，不要把外层中文分类目录一起作为 Skill 安装目录。

## 调用示例

### 查询模型字典

```text
调用 $bzd-model-dictionary 判断以下模型是否适合：

题目：<题目内容或赛题路径>
数据：<样本量、变量类型、数据结构及缺失情况>
候选模型：<准备采用的模型>
求解思路：<当前完整求解方案>
```

### 检查整篇论文格式

```text
使用 $bzd-paper-format-checker 检查以下论文：
论文：<PDF或Word路径>

请输出逐项格式检查结果、格式规范分和优先修改建议。
```

### 检查论文专项章节

```text
使用 $bzd-model-solution-checker 检查：
赛题：<赛题路径>
论文：<论文路径>
附件或代码：<可选路径>
```

### 评审完整论文

```text
使用 $bzd-review-paper 评审：
竞赛类型：<高教社杯国赛或其他竞赛名称>
赛题：<赛题路径>
论文：<论文路径>
已有格式自查报告：<可选，bzd-paper-format-checker输出路径>
```

## 项目结构

```text
bzd-math-modeling-skills/
├── README.md
├── CHANGELOG.md
├── skills/
│   ├── 综合评审与自我定位类/
│   ├── 生成类/
│   └── 论文自查类/
│       ├── bzd-paper-format-checker/
│       ├── bzd-abstract-checker/
│       ├── bzd-problem-restatement/
│       ├── bzd-problem-analysis-checker/
│       ├── bzd-model-assumption-checker/
│       ├── bzd-symbol-notation-checker/
│       ├── bzd-model-solution-checker/
│       ├── bzd-ai-usage-disclosure/
│       ├── bzd-reference-appendix-checker/
│       ├── bzd-model-dictionary/
│       └── bzd-review-paper/
└── 数模资料/
```

## 数模资料

仓库中的 [`数模资料/`](数模资料/) 提供论文模板、LaTeX模板、评分观察点、评阅细则示例及各板块详细说明文档。完整索引和使用范围见 [`数模资料/README.md`](数模资料/README.md)。

## 重要说明

- 本项目不是竞赛官方工具，输出不代表官方评审结果、实际排名或奖项承诺；
- 没有真实附件数据时，不应虚构模型参数、最优结果、程序运行情况和预测精度；
- 使用者应自行确认当届竞赛关于AI工具、论文格式、附录材料和学术诚信的最新规定；
- 请勿向公开仓库提交未公开论文、个人身份信息、API Key、Token或无传播授权的内部材料；
- 仓库中的评分规则、历史数据和经验阈值可能随竞赛年份发生变化。

## 联系方式

✨ 如需进一步详细的论文检查、赛中资料等服务，可关注 **BZD数模社** 官网：[https://bzdshumo.com/](https://bzdshumo.com/)

- QQ数模交流群（主群1）：689964173
- QQ数模交流2群（主群2）：275032074
- 资料通知群（仅推送资料/无聊天）：928949323
- 微信（个性化定制）：bzdsxjm521
- 备用微信：bzdsxjm520 / BZD661188
