# BZD Math Modeling Skills

面向数学建模竞赛的 BZD Skills 合集，支持 **Codex** 与 **Claude Code**。

本项目围绕数学建模竞赛的完整流程持续研发，目前skills分为论文点评类skills、生成类skills、自查类skills 。 
目前已完成论文点评skills，以及论文各大板块，按2026年最新规定的自查skills、高校国奖数据查询及个人备赛定位。
后续将在论文点评skills里将要引入各赛区的难度区分，以便更加符合真实的评分情况；同时准备合并自查skills，制作出Agent直出论文的评价skills，以便大家在赛中能够根据Agent指出的论文进一步自查，完成后续的修改。
同时正在制作数模字典skills，预计包含1000+种数学模型，能够根据大家的题目+数据情况判定当前选择模型是否合适，同时给出同类型其他模型的推荐。
相关 Skills 主要基于 2020—2025 年高教社杯全国大学生数学建模竞赛赛题、评分细则、评分要点、评阅概述及完整评阅流程进行归纳和蒸馏。

> 本项目不是竞赛官方工具。所有评分、位次预测和备赛建议仅供参考，最终应以当届组委会及赛区发布的正式规则为准。

## Skills 分类

部分 Skill 同时支持生成、检查或综合评审，因此会在不同分类中重复出现，并在对应分类目录中各保留一份，方便用户按使用场景直接选择和安装。

### 一、综合评审与自我定位类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-review-paper`](skills/综合评审与自我定位类/bzd-review-paper/) | 根据本次赛题独立制定评分细则，评估论文质量，并结合组别、赛区、学校历史国奖表现和指导教师集中度预测竞赛位置 | 竞赛类型、完整赛题、完整论文；国赛另需组别、赛区、学校全称和指导教师 | 论文质量得分、省奖竞争修正分、国奖竞争修正分、预估位次、详细扣分及 HTML 评审报告 |
| [`bzd-cumcm-school-awards`](skills/综合评审与自我定位类/bzd-cumcm-school-awards/) | 查询高校五年国奖数据并评估个人备赛差距 | 学校名称、赛区及个人竞赛经历 | 高校国奖画像、2026 年预测及备赛建议 |

### bzd-review-paper 最新评审机制

`bzd-review-paper` 使用2020—2025年16道高教社杯全国大学生数学建模竞赛赛题的评分细则、评分要点、评阅概述及完整评阅流程进行归纳和蒸馏。

每次评审时，Skill 会首先读取本次提供的完整赛题，重新分解任务并独立制定百分制评分细则。评分细则不得沿用用户历史对话中的解题思路、模型建议、计算结果或既有评审结论，避免历史记忆干扰本次评价。

评审结果分为三个层次：

1. **论文质量最终得分**：只评价论文本身的任务完成度、模型合理性、求解质量、结果可信度、验证情况、摘要及格式；
2. **省奖竞争修正分**：在论文质量得分基础上，结合参赛组别和所在赛区的省奖竞争强度进行修正；
3. **国奖竞争修正分**：进一步结合赛区国奖难度、学校2021—2025年国奖表现、是否为数模强校以及指导教师集中度进行修正。

其中：

- 国奖赛区修正范围最高为 **±15分**；
- 省奖赛区修正范围最高为 **±10分**；
- 本科组与高职高专组分别使用对应的赛区难度数据；
- 高职高专组的省奖评价不使用赛区985、211高校数量；
- 学校、赛区和指导教师不会改变论文质量最终得分，只影响竞赛环境下的奖项判断；
- 若学校未出现在2021—2025年国奖学校统计表中，经验国奖概率上限设为 **6.81%**，奖项预测最高为省一等奖，国奖竞争修正分最高为74.9分；
- 若学校历史国奖指导教师集中度超过30%，Skill 会判断当前指导教师是否与历史高频教师一致，并据此调整国奖竞争力；
- 所有调整均属于历史数据驱动的经验估计，不代表官方名额或获奖承诺。

> 创新盲区提示：每年都有少量论文因解题路径高度新颖、甚至超出常规评阅预期而获得国奖。AI评审难以可靠识别这类突破性价值，因此可能低估真正原创的非常规方案。

### 二、生成类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-problem-translator`](skills/生成类/bzd-problem-translator/) | 逐句翻译赛题，识别隐藏条件和跨问题关系 | 完整赛题及附件说明 | 题意翻译报告、跨问题联动链 |
| [`bzd-modeling-ideas`](skills/生成类/bzd-modeling-ideas/) | 生成贯穿全文的建模主线并比较可行模型 | 完整赛题、附件、可选题意报告 | 多模型比较、选型理由、创新与验证方案 |
| [`bzd-problem-restatement`](skills/生成类/bzd-problem-restatement/) | 根据赛题生成问题重述，也支持已有重述自查 | 完整赛题；自查时另提供已有重述 | 问题背景、问题回顾、研究综述或自查报告 |
| [`bzd-ai-usage-disclosure`](skills/生成类/bzd-ai-usage-disclosure/) | 生成或检查 AI 工具使用声明及使用详情 | 论文、真实 AI 使用情况、已有声明或详情材料 | AI 工具使用声明、使用详情文档、自查结果 |

#### 国赛前预期更新

- 增加数学建模论文各板块的生成型 Skills；
- 生成型 Skills 采用普通 Skill 形式，可独立调用，也可配合智能体针对对应板块完善内容；
- 增加“绘图推荐 Skill”：用户输入赛题背景和结果数据后，获得多种可视化方案、图形选择理由及版式建议；用户确认方案后，可继续生成绘图代码；
- 持续完善生成内容与真实数据、模型、结果和全文逻辑的一致性检查。

### 三、论文自查类

| Skill | 自查对象 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-model-dictionary`](三、论文自查类%20skills/bzd-model-dictionary/) | 根据赛题、数据与求解思路检查模型选用是否合理 | 赛题、数据结构、候选模型、求解思路 | 字典信息、适配性结论、模型缺陷、检验方法及替代模型 |
| [`bzd-abstract-checker`](skills/论文自查类/bzd-abstract-checker/) | 摘要 | 摘要，可选题目与关键词 | 严重问题警告、逐项诊断、优先修改建议 |
| [`bzd-problem-restatement`](skills/论文自查类/bzd-problem-restatement/) | 问题重述 | 完整赛题与已有问题重述 | 任务遗漏、条件失真、章节越界及修改建议 |
| [`bzd-problem-analysis-checker`](skills/论文自查类/bzd-problem-analysis-checker/) | 问题分析 | 完整赛题、附件说明与已有问题分析 | 任务映射、跨问联动、问题清单及修改优先级 |
| [`bzd-model-assumption-checker`](skills/论文自查类/bzd-model-assumption-checker/) | 模型假设 | 完整赛题、模型假设，可选模型正文 | 逐条诊断、遗漏假设、验证要求及修改优先级 |
| [`bzd-symbol-notation-checker`](skills/论文自查类/bzd-symbol-notation-checker/) | 符号说明 | 完整论文，或符号表与模型正文 | 符号遗漏、冲突、单位、上下标及版式诊断 |
| [`bzd-model-solution-checker`](skills/论文自查类/bzd-model-solution-checker/) | 模型建立、求解、检验和灵敏度分析 | 完整赛题、论文，可选附件或代码 | 核心正文诊断、复现检查及优先修改建议 |
| [`bzd-ai-usage-disclosure`](skills/论文自查类/bzd-ai-usage-disclosure/) | AI 工具使用声明与详情 | 论文、真实 AI 使用记录、已有披露材料 | 完整性、一致性、匿名性及责任边界检查 |
| [`bzd-reference-appendix-checker`](skills/论文自查类/bzd-reference-appendix-checker/) | 参考文献与附录 | 论文、参考文献、附录、程序与支撑材料 | 引用与附录检查报告、P0—P3 风险及修改建议 |
| [`bzd-review-paper`](skills/论文自查类/bzd-review-paper/) | 完整论文综合自查 | 竞赛类型、完整赛题与完整论文 | 综合得分、预估位次、评委式评价及修改顺序 |

#### 国赛前预期更新

- 增加 Agent 形式的论文内容检查能力，对论文、代码、数据和结果进行跨文件核验；
- 增加“数学建模论文全文自查”能力，将现有章节自查 Skills 的关键规则整合为一次完整检查；
- 在保留专项 Skill 深度的同时，输出全文级问题地图、风险等级和统一修改优先级；
- 加强图表、公式、结果、代码和正文结论之间的一致性检查。

### 四、数据查询与备赛辅助类

| Skill | 主要作用 | 输入 | 输出 |
|---|---|---|---|
| [`bzd-cumcm-school-awards`](skills/综合评审与自我定位类/bzd-cumcm-school-awards/) | 查询高校历史国奖数据并评估备赛距离 | 学校、赛区、竞赛经历和模拟情况 | 学校画像、国奖预测、省奖与国奖备赛建议 |

## 其他国赛前规划
```mermaid
flowchart LR
    BZD["BZD数模社<br/><b>数学建模 Skills 合集</b><br/>覆盖理解、生成、自查与评审"]

    REVIEW["① 综合评审与自我定位类"]
    GENERATE["② 生成类"]
    CHECK["③ 论文自查类"]

    R_NOW["<div style='text-align:left'><b>当前 Skills</b><br/>bzd-review-paper：论文评分、位次与评委式建议<br/>bzd-cumcm-school-awards：学校国奖画像与备赛定位</div>"]
    R_UPDATE["<div style='text-align:left'><b>国赛前预计更新</b><br/>加入赛区难度、学校实力与竞争环境<br/>联动论文质量、赛区和学校情况优化预测</div>"]

    G_NOW["<div style='text-align:left'><b>当前 Skills</b><br/>bzd-problem-translator：逐句翻译赛题<br/>bzd-modeling-ideas：评委视角的求解多模型建议集<br/>bzd-problem-restatement：生成问题重述<br/>bzd-ai-usage-disclosure：生成AI使用声明</div>"]
    G_UPDATE["<div style='text-align:left'><b>国赛前预计更新</b><br/>增加论文各板块生成 Skills<br/>增加绘图推荐、方案选择与绘图代码生成<br/>增加数模字典及同类模型推荐</div>"]

    C_NOW["<div style='text-align:left'><b>当前 Skills</b><br/>bzd-abstract-checker：摘要自查;bzd-problem-restatement：问题重述自查;bzd-problem-analysis-checker：问题分析自查<br/>bzd-model-assumption-checker：模型假设自查;bzd-symbol-notation-checker：符号说明自查;bzd-model-solution-checker：模型建立、求解、检验与灵敏度分析自查<br/>bzd-reference-appendix-checker：参考文献与附录自查;bzd-ai-usage-disclosure：AI使用披露自查;bzd-review-paper：完整论文综合自查</div>"]
    C_UPDATE["<div style='text-align:left'><b>国赛前预计更新</b><br/>增加 Agent 直出论文内容检查<br/>合并专项规则形成数模论文全文自查<br/>强化论文—代码—数据—结果一致性核验</div>"]

    BZD --> REVIEW
    BZD --> GENERATE
    BZD --> CHECK

    REVIEW --> R_NOW --> R_UPDATE
    GENERATE --> G_NOW --> G_UPDATE
    CHECK --> C_NOW --> C_UPDATE

    classDef hub fill:#172554,color:#ffffff,stroke:#1d4ed8,stroke-width:3px;
    classDef category fill:#dbeafe,color:#1e3a8a,stroke:#3b82f6,stroke-width:2px;
    classDef current fill:#f8fafc,color:#0f172a,stroke:#94a3b8,stroke-width:1.5px;
    classDef update fill:#ecfdf5,color:#065f46,stroke:#10b981,stroke-width:2px;

    class BZD hub;
    class REVIEW,GENERATE,CHECK category;
    class R_NOW,G_NOW,C_NOW current;
    class R_UPDATE,G_UPDATE,C_UPDATE update;
```

该路线图用于展示当前已经上线的能力与国赛前计划更新内容。具体上线顺序将根据实际开发和测试结果调整。
### 当前能力与国赛前更新路线图

### bzd-model-dictionary

`bzd-model-dictionary` 是基于 **BZD数模社·数模模型字典** 构建的模型查询与选型自查 Skill。

用户提供赛题、数据结构、候选模型及求解思路后，Skill 会从模型字典中查询该模型的适用场景、数据要求、关键假设、输入输出、禁忌点、模型缺陷和检验方法，并结合当前题目判断模型选择是否合理。

Skill 将模型适配性划分为以下四类：

- **合适**：模型与题目目标、数据结构及变量类型基本匹配；
- **有条件合适**：模型方向正确，但需要满足额外条件或补充处理；
- **不合适**：模型与任务目标、数据类型或核心假设明显冲突；
- **证据不足**：现有信息不足以完成可靠判断。

除适配性结论外，Skill 还会指出模型使用中容易忽略的数据结构、假设条件和检验要求，并推荐可替代或配套使用的同类模型，帮助使用者避免机械套用模型。

### 数模资料

仓库已在 [`数模资料/`](数模资料/) 中整理以下内容：

- [`2026年数学建模竞赛模板-简洁版.docx`](数模资料/2026年数学建模竞赛模板-简洁版.docx)；
- [`2026年数学建模竞赛模板-BZD数模社(证书签名).pdf`](<数模资料/2026年数学建模竞赛模板-BZD数模社(证书签名).pdf>)；
- [`数学建模竞赛论文latex模板-BZD数模社 (1).zip`](<数模资料/数学建模竞赛论文latex模板-BZD数模社 (1).zip>)；
- [`官方评阅细则评分要点-参考示例-完整训练使用近五年16道题目.zip`](数模资料/官方评阅细则评分要点-参考示例-完整训练使用近五年16道题目.zip)；
- [`数学建模论文百分制评分观察点.pdf`](数模资料/数学建模论文百分制评分观察点.pdf)；
- [`各板块详细说明文档/`](数模资料/各板块详细说明文档/)：包含摘要、问题重述、问题分析、模型假设、符号说明、模型建立与求解、模型总结、参考文献与附录、AI 工具使用声明与详情等材料。

完整文件索引、用途和适用范围见 [`数模资料/README.md`](数模资料/README.md)。后续仅增加公开、自主整理或具有明确传播授权的备赛资料。

## 当前 Skills 总览

| Skill | 综合评审 | 内容生成 | 论文自查 | 数据查询 |
|---|:---:|:---:|:---:|:---:|
| `bzd-review-paper` | ✓ |  | ✓ |  |
| `bzd-cumcm-school-awards` | ✓ |  |  | ✓ |
| `bzd-problem-translator` |  | ✓ |  |  |
| `bzd-modeling-ideas` |  | ✓ |  |  |
| `bzd-problem-restatement` |  | ✓ | ✓ |  |
| `bzd-ai-usage-disclosure` |  | ✓ | ✓ |  |
| `bzd-abstract-checker` |  |  | ✓ |  |
| `bzd-problem-analysis-checker` |  |  | ✓ |  |
| `bzd-model-assumption-checker` |  |  | ✓ |  |
| `bzd-symbol-notation-checker` |  |  | ✓ |  |
| `bzd-model-solution-checker` |  |  | ✓ |  |
| `bzd-reference-appendix-checker` |  |  | ✓ |  |

## 推荐工作流

```mermaid
flowchart LR
    A["完整赛题"] --> B["bzd-problem-translator"]
    B --> C["逐句理解与跨问题联动"]
    C --> D["bzd-modeling-ideas"]
    D --> E["整体思路与多模型比较"]
    E --> F["完成代码与论文"]
    F --> G["章节专项自查"]
    G --> H["bzd-review-paper"]
    H --> I["得分、位次与修改建议"]
```

## 安装

### Codex

下载仓库后，将需要使用的 Skill 文件夹复制到：

```text
Windows：%USERPROFILE%\.codex\skills\
macOS/Linux：~/.codex/skills/
```

仓库中的中文目录用于功能分类。安装时既可以按分类选择，也可以进入分类目录复制具体的 `bzd-...` Skill 文件夹。若多个分类中出现同名 Skill，它们是相同能力的场景化副本；安装到同一个 Skills 目录时只需保留其中一份。

例如安装全部 Skills：

```text
.codex/skills/
├── bzd-abstract-checker/
├── bzd-ai-usage-disclosure/
├── bzd-cumcm-school-awards/
├── bzd-model-assumption-checker/
├── bzd-model-solution-checker/
├── bzd-modeling-ideas/
├── bzd-problem-analysis-checker/
├── bzd-problem-restatement/
├── bzd-problem-translator/
├── bzd-reference-appendix-checker/
├── bzd-review-paper/
└── bzd-symbol-notation-checker/
```

### Claude Code

将需要使用的 Skill 文件夹复制到：

```text
项目目录/.claude/skills/
```

同样应复制具体的 `bzd-...` Skill 文件夹，并在安装后保持 Skill 目录直接位于 `.claude/skills/` 下。

评审 Skill 的 Claude Code 补充配置见 [`integrations/claude-code/`](integrations/claude-code/)。

## 调用示例

### 翻译赛题

```text
使用 $bzd-problem-translator 翻译以下完整赛题：<赛题路径>
```

### 生成整体建模思路

```text
使用 $bzd-modeling-ideas 分析以下完整赛题：<赛题路径>
请生成贯穿全文的整体思路，并比较每一问的可行模型和选型理由。
```
```text
调用 $bzd-model-dictionary 判断以下模型是否适合：

题目：<题目内容或赛题文件路径>
数据：<样本量、变量类型、数据结构及缺失情况>
候选模型：<准备采用的模型>
求解思路：<当前完整求解方案>

请查询模型字典，输出模型信息、适配性判断、使用条件、
潜在缺陷、检验方法以及可替代或配套的模型。

### 生成或检查问题重述

```text
使用 $bzd-problem-restatement，根据以下完整赛题生成问题重述：
赛题：<赛题路径>
```

```text
使用 $bzd-problem-restatement 检查：
原始赛题：<赛题路径>
我的问题重述：<问题重述内容>
```

### 检查问题分析

```text
使用 $bzd-problem-analysis-checker 检查：
原始赛题：<赛题路径>
附件说明：<附件路径或说明>
我的问题分析：<问题分析内容>
```

### 评审完整论文

```text
使用 $bzd-review-paper 评审：
竞赛类型：<高教社杯国赛或其他竞赛名称>
赛题：<赛题路径>
论文：<论文路径>
```

### 检查参考文献与附录

```text
使用 $bzd-reference-appendix-checker 检查：
论文：<论文路径>
参考文献原始资料：<文献文件或链接>
附录与支撑材料：<材料文件夹路径>
程序代码：<代码文件夹路径>
```

## 项目结构

```text
bzd-math-modeling-skills/
├── README.md
├── CHANGELOG.md
├── skills/
│   ├── 综合评审与自我定位类/
│   │   ├── bzd-review-paper/
│   │   └── bzd-cumcm-school-awards/
│   ├── 生成类/
│   │   ├── bzd-problem-translator/
│   │   ├── bzd-modeling-ideas/
│   │   ├── bzd-problem-restatement/
│   │   └── bzd-ai-usage-disclosure/
│   └── 论文自查类/
│       ├── bzd-abstract-checker/
│       ├── bzd-ai-usage-disclosure/
│       ├── bzd-problem-analysis-checker/
│       ├── bzd-problem-restatement/
│       ├── bzd-model-assumption-checker/
│       ├── bzd-symbol-notation-checker/
│       ├── bzd-model-solution-checker/
│       ├── bzd-reference-appendix-checker/
│       └── bzd-review-paper/
├── integrations/
│   └── claude-code/
└── 数模资料/
```

## 重要说明

- 本项目不是竞赛官方工具，输出不代表官方评审结果、实际排名或奖项承诺；
- 没有真实附件数据时，不应虚构模型参数、最优结果、程序运行情况和预测精度；
- 使用者应自行确认当届竞赛关于 AI 工具、论文格式、附录材料和学术诚信的最新规定；
- 请勿向公开仓库提交未公开论文、个人身份信息、API Key、Token 或无传播授权的内部材料；
- 仓库中的评分规则、历史数据和经验阈值可能随竞赛年份发生变化。
- 同一 Skill 在多个分类目录中保留副本时，维护者应同步更新所有同名副本，避免不同分组中的版本发生偏差。

## 联系方式

✨ 如需进一步详细的论文检查、赛中资料等服务，可关注 **BZD数模社** 官网：[https://bzdshumo.com/](https://bzdshumo.com/)

- QQ数模交流群（主群1）：689964173
- QQ数模交流2群（主群2）：275032074
- 资料通知群（仅推送资料/无聊天）：928949323
- 微信（个性化定制）：bzdsxjm521
- 备用微信：bzdsxjm520 / BZD661188
