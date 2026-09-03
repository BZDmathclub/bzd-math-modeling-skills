# BZD 数模论文 AI 痕迹审计 · 完整离线 Prompt

> **v2.2 严格判分版** | BZD 数模社制作
> 本文档是一份**自包含的审计指令**。无需安装任何 skill，把本文档全文
> 连同你的论文一起发给任意支持长文本的 AI（Claude / ChatGPT / Gemini /
> Kimi / DeepSeek / 豆包等），即可获得一份带标红的 HTML 审计报告。

---

## 📋 怎么用（三步）

**第 1 步**：复制本文档**全部内容**，粘贴进 AI 对话框。

**第 2 步**：在同一条消息末尾追加你的论文——
- 支持上传 PDF/Word 的平台：直接上传附件
- 不支持的平台：粘贴论文全文文本

**第 3 步**：在最后加上这句话：

```
请严格按照上述《BZD 数模论文 AI 痕迹审计 v2.2》执行审计，
输出一个完整的、可直接保存为 .html 的单文件报告。
不要输出报告以外的解释性文字。
```

AI 会返回一段 HTML 代码。复制它 → 新建记事本 → 粘贴 → 另存为
`审计报告.html`（编码选 UTF-8）→ 双击用浏览器打开。

**可选增强输入**（能显著提高判定置信度，有就一起给）：
赛题原文与附件 · 代码文件 · 中间结果 · 参考文献清单

---

## 🎯 这个工具判什么、不判什么

| ✅ 判 | ❌ 不判 |
|---|---|
| AI **拼装**痕迹 | 是否**使用过** AI |
| 结论能否被追溯和复算 | 作者身份概率 |
| 模型选择是否华而不实 | 模型是否有学术创新 |
| 引文与数值是否真实 | 替代查重 / 官方 AIGC 检测 |

**核心分界线**：一篇声明用了 AI 辅助、但建模主线由人主导、参数可溯源、
结果可复算的论文，判为低风险；一篇没用 AI 但引文造假、参数对不上的论文，
直接触发一票否决。

**数模竞赛的本质原则**：能用基础模型解决的，就不该上复杂模型。
判断模型是否华而不实，是第二层的核心结论。

---

## 🧮 评分总架构

```
                 ┌─ 语言层面 60%（6个维度）
第一层（9维）────┤
                 └─ 事实层面 40%（3个维度）

第二层（5项等权）── 建模逻辑深度审查

最终风险分 = (第一层风险分 + 第二层风险分) / 2
```

### ⚠️ 分数方向约定（最容易出错，务必先读）

本框架有**两套方向相反**的分数，严禁混用：

```
质量分：各维度直接打出的分，越高越好
        100 = 完全无 AI 特征     0 = 严重 AI 特征

风险分：用于查等级表，越高越危险
        风险分 = 100 − 质量分
        0 = 无风险              100 = 极高风险
```

**三步计算，不可跳步**：

```
第1步  给每个维度打质量分（0-100）
第2步  加权求和 → 该层质量分
第3步  100 − 质量分 = 该层风险分 → 再查等级表
```

**风险等级表（对风险分）**：

| 风险分 | 等级 | 含义 | 处理 |
|---|---|---|---|
| 0–15 | 🟢 低风险 | 语言规范、事实可核验 | 可直接接收 |
| 16–30 | 🟡 中低风险 | 有局部套话或个别存疑项 | 可接收，需补充改进 |
| 31–50 | 🟠 中风险 | 多维度问题 | 需深度检查后再定 |
| 51–70 | 🔴 中高风险 | 明显 AI 特征 | 强烈建议强制改稿 |
| 71–100 | ⛔ 高风险 | 确认 AI 拼装迹象 | 建议拒稿 |

---

# 第一层：九维检测

## 【语言层面 · 权重 60%】

### 维度 1 · 高频连接词（权重 20%）

**基础词库**（Humanizer-zh，★表示 AI 高频程度）：

```
★★★★★  综上所述 / 综合上述
★★★★    进一步 / 可以看出
★★★      此外 / 与此同时 / 值得注意的是 / 一般来说 / 由此可见
★★        当然 / 不仅…而且
```

**数模特化增补词**：

```
"具有…特性"   → 听起来科学，后面通常没有数据
"相对而言"     → 模糊对比，无具体数字
"显然"         → 跳过推导的信号
"毋庸置疑"     → 强行下结论
"众所周知"     → 学术写作应避免
```

**计算**：`密度 = 高频词总出现次数 ÷ 全文总句数`

**判分**：

| 密度 | 得分 | 标记 |
|---|---:|---|
| < 8% | 100 | 🟢 |
| 8–12% | 85 | 🟢 |
| 12–16% | 60 | 🟡 |
| 16–20% | 35 | 🟠 **标红** |
| 20–25% | 15 | 🔴 **标红** |
| > 25% | 0 | ⛔ **标红** |

**附加扣分**：同一高频词在 3 页内出现 > 2 次，每处额外 −5 分（下限 0）

**豁免**：优化模型末尾的"综上，式(1)–(3) 构成完整模型"是数模写作的
**规范要求**，不计为套话。

---

### 维度 2 · 排比与同构句式（权重 12%）

**三级分类**：

```
🔴 L1 高风险
"该方法具有以下优点：(1)准确度高、(2)效率快、(3)鲁棒性强"
   → 排比后全是抽象形容词，一个数据都没有

🟡 L2 中等
"约束条件：(1)螺距 p≥0.30m、(2)转向半径 R<4.5m、(3)速度 v≤2m/s"
   → 有数字，但没说这些值从哪来

🟢 L3 安全
"约束：(1)p≥0.30m(赛题给出)、(2)R<4.5m(由题意推导)、(3)v≤2m/s(安全系数)"
   → 每项都有数据 + 来源
```

**判分**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| 全部 L3 | 100 | 🟢 |
| L3 为主，个别 L2 | 80 | 🟢 |
| L2 为主 | 55 | 🟡 |
| 存在 1 处 L1 | 30 | 🟠 **标红** |
| 存在 ≥2 处 L1 | 0 | 🔴 **标红** |

**⭐ 附加扣分（v2.2 新增，容易被漏掉的模板化信号）**：

同一组织词（"其一/其二/其三"、"首先/其次/最后"、"一方面/另一方面"）
在 **≥4 个不同章节**机械复用 → 额外 **−20**
在 **≥6 个不同章节**机械复用 → 额外 **−30**

> 此项**即使各项内部都有数据也照扣**。理由：跨章节复用同一组织词
> 本身就是可观察的模板化痕迹，与项内是否有数据是两件事。
> v2.1 只按 L1/L2/L3 分级，会完全漏掉这类问题。

---

### 维度 3 · 拔高词五级分类（权重 12%）

```
L1 【最高风险】绝对化 + 零数据
   ❌ "模型精度最高"  "算法最优"  "效果最好"
   ✅ 改为："与基准相比，RMSE 从 0.34 降至 0.12，精度提升 64.7%"

L2 【高风险】相对化 + 泛泛对比
   ❌ "相比传统方法，性能有很大提升"
   ✅ 改为："相比蛮力搜索 O(n²)，二分搜索 O(log n) 在 224 个对象上快约 100 倍"

L3 【中风险】定量 + 无基准
   ❌ "精度为 99%"
   ✅ 改为："在 500 样本测试集上精度 99.2%（基准 89.5%）"

L4 【中低风险】定量 + 有数字无对比
   ❌ "计算时间 0.5 秒"
   ✅ 改为："0.5 秒 vs 竞品 2.3 秒，快 3.6 倍"

L5 【低风险】完整定量 + 充分对比
   ✅ "与 KNN(k=3) 相比，F1 在 3 个数据集上提升 12.5%–18.7%，D1 上最高 20.1%"
```

**判分（v2.2 大幅收严）**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| L5 为主且拔高词密度 < 8% | 100 | 🟢 |
| L4–L5 为主 | 80 | 🟢 |
| L3 为主 | 55 | 🟡 |
| **存在 1 个 L1** 或 2 个 L2 | 30 | 🟠 **标红** |
| 存在 ≥2 个 L1 | 0 | 🔴 **标红** |

> v2.1 要 >3 个 L1 才归零，v2.2 改为 **1 个 L1 即标红**。

---

### 维度 4 · 被动句占比（权重 9%）

```
❌ 高风险："该模型被应用于… 结果被验证… 参数被优化… 方案被采用…"
   → 整段被动，生硬

✅ 正常："我们建立了该模型… 结果验证了… 通过灵敏度分析，我们发现…"
   → 主被动混合，自然
```

**方法**：抽取 5 个代表段落（摘要 / 建模 / 求解 / 结果 / 结论各一），统计占比。

**判分**：

| 占比 | 得分 | 标记 |
|---|---:|---|
| < 15% | 100 | 🟢 |
| 15–22% | 85 | 🟢 |
| 22–27% | 55 | 🟡 |
| 27–33% | 30 | 🟠 **标红** |
| > 33% | 0 | 🔴 **标红** |

**附加扣分**：出现连续 ≥4 句被动语态的段落，每处 −10 分

---

### 维度 5 · 段落结构规律性（权重 6%）

**方法**：抽取 20 段，统计**段落开头方式**的重复率。

| 重复率 | 得分 | 标记 |
|---|---:|---|
| < 15% | 100 | 🟢 |
| 15–28% | 80 | 🟢 |
| 28–40% | 50 | 🟡 |
| 40–55% | 25 | 🟠 **标红** |
| > 55% | 0 | 🔴 **标红** |

**⚠️ 重要豁免**：数模论文各建模章节遵循"建模思路 → 模型建立 → 模型求解
→ 结果分析 → 检验与灵敏度"五段式，属**文体常规**，竞赛评审明确期待
这一结构，**不计入本项**。本项只统计**段落级**的开头方式重复。

---

### 维度 6 · 文本复杂度（权重 1%）

**A. 词汇多样性 TTR** = 不同词数 ÷ 总词数

**B. 3-gram 重复率**：
```
"本文采用… 本文选择… 本文利用… 本文验证…"  → "本文+动词" > 3 次即警戒
"通过…方法… 通过…算法… 通过…分析…"        → "通过+名词" > 4 次即警戒
```

**判分**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| TTR > 0.55 且 3-gram < 4% | 100 | 🟢 |
| TTR 0.45–0.55 或 3-gram 4–8% | 65 | 🟡 |
| TTR 0.35–0.45 或 3-gram 8–13% | 30 | 🟠 **标红** |
| TTR < 0.35 或 3-gram > 13% | 0 | 🔴 **标红** |

---

## 【事实层面 · 权重 40%】

> ⚠️ 本层任一维度触发**一票否决项**时，直接判定论文风险等级，
> 不再按加权分核算。详见后文《一票否决清单》。

### 维度 7 · 引文验证（权重 15%）

**L1 快速检查（30 秒）**
```
✓ DOI 格式正确？（10.XXXXX/…）
✓ 作者名规范？（Lastname, F. I. 或 中文姓名, 等）
✓ 期刊名拼写与大小写正确？
✓ 发表年份合理？（非经典文献一般不超过 20 年）
```

**L2 存在性验证（2–3 分钟）**
```
途径：Google Scholar / 知网 / PubMed / 期刊官网 / OpenAlex
核对：文献是否存在？作者、题名、年份、卷期页码是否全部匹配？

🚨 无法找到 → 虚构可能性极高，直接触发一票否决
```

**L3 主张-支撑匹配（5 分钟，抽查不少于 5 篇关键文献）**
```
1. "根据文献[X] 的方法，本文采用…"
   → 查该文献是否真的提出了这个方法
2. "数据集包含 XXX 个样本"
   → 验证数据集是否存在、规模是否一致
3. "在文献[X] 的基础上改进"
   → 改进点是否说清楚了
```

**数模特化检查点**：
```
• "根据题意" → 是否真有赛题原文支撑？
• 引用的算法论文，其应用场景与本题是否可比？
  （如：某算法原用于图像识别，本题用于路径优化，
    需说明"为什么该算法在本题也适用"）
• 若文献全是综述和教科书、没有一篇具体算法论文
  → 说明作者对方法理论理解不深，−15 分
```

**判分**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| 全部通过 L1–L3，无未引用的凑数文献 | 100 | 🟢 |
| 全部存在，但有 1–2 篇列入文献表却未在正文引用 | 80 | 🟡 |
| 有 1 篇作者/年份/期刊信息不符 | 25 | 🔴 **标红 + 否决** |
| 有任 1 篇**确认不存在** | 0 | ⛔ **强制高风险** |

**附加检查**：文献总数 < 6 篇 或 > 25 篇 → −10 分

---

### 维度 8 · 数值一致性追踪（权重 15%）

**做法**：建一张参数溯源表，逐一追踪并**复算算术关系**。

| 参数 | 数值 | 来源层级 | 出现位置 | 一致？ |
|---|---|---|---|---|
| 例：p | 0.55 m | L1 赛题给出 | 摘要/P3/表1/公式(2) | ✓ |
| 例：t* | 412.474 s | L2 问二推导 | P8/P11/表3 | ✓ |
| 例：Δt | 0.5 s | L3 物理约束 | P6/代码/表2 | ✓ |

**来源三级体系**：
```
L1【赛题给出】  "螺距 p=0.55m（题目给出）"                    风险低
L2【前问推导】  "Q2 推导出 t*=412.474s，Q3 以此为初值"        风险低
L3【物理约束】  "Δt=0.5s 由速度 v=1m/s 与精度要求 <10⁻⁴s 推导" 风险中
🔴 无来源      "设步长 Δt=0.5s"（无任何解释）                 风险极高
```

**必做的算术复算**（AI 编造的数字往往过不了这关）：
```
• 各分项之和 = 总计？
• 占比 = 分子 ÷ 分母？
• 差值 = 两数相减？
• 极差 = 最大 − 最小？
```

**判分**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| 全部一致 + 算术自洽 + 来源清晰 | 100 | 🟢 |
| 一致但个别参数来源未说明 | 75 | 🟡 |
| 存在 1–5% 偏差且**未加解释** | 35 | 🟠 **标红** |
| 存在 >5% 偏差且**未加解释** | 0 | 🔴 **标红 + 否决** |

**幽灵参数**：任一关键参数无法追溯到 L1/L2/L3 任一层级 → 每个 −15 分

**⭐ 加分项（v2.2 新增，上限 +5）**：

论文**主动披露**数值差异并解释其来源的，**不触发否决，反而加分**。例如：

> "问题四独立重解确定性基准时目标值为 1,106.9，与问题三的 1,105.7
> 相差 0.1%，来自分支定界在间隙容差内的数值差异。"

> "灵敏度脚本为独立简化实现，其基值与主算存在微小数值差异
> （常数项初始化方式不同），但结论方向完全一致。"

> **为什么这是加分项**：AI 生成的文本会让数字直接对齐，不会制造这种
> "无必要的麻烦"。能写出这种披露，说明作者真实运行过两套独立实现、
> 观察到差异、并判断了它的性质。这是人工复算最有力的证据。

---

### 维度 9 · 术语一致性（权重 10%）

**做法**：提取 5–7 个核心概念，追踪全文表述方式。

| 核心术语 | 摘要 | 第5章 | 第9章 | 一致性 |
|---|---|---|---|---|
| 例：算法名 | GA | GA | GA | 🟢 一致 |
| 例：运次数 | 运次 | 班次 | 运次 | 🟡 混用 |

**典型 AI 特征**：
```
❌ P1: "采用遗传算法 GA"
   P5: "利用进化策略 ES"
   P10: "该种群智能算法…"
   → 到底用的是哪个？概念混乱，说明缺乏统一理解

✅ 全文统一叫"约束优化框架"，各问是它的不同变体
```

**判分**：

| 情况 | 得分 | 标记 |
|---|---:|---|
| 完全一致 | 100 | 🟢 |
| 仅存在领域公认同义词（如"粗差/过失误差"） | 85 | 🟢 |
| 1 个核心术语有 2 种表述 | 55 | 🟡 |
| 1 个核心术语有 ≥3 种表述 | 25 | 🟠 **标红** |
| 多个核心术语混乱（尤其算法名称） | 0 | 🔴 **标红** |

---

## 第一层汇总公式

```
第一层质量分 =
    维1×0.20 + 维2×0.12 + 维3×0.12 + 维4×0.09 + 维5×0.06 + 维6×0.01
  + 维7×0.15 + 维8×0.15 + 维9×0.10

第一层风险分 = 100 − 第一层质量分
```

**⚠️ 上面的百分数已经是占总分 100% 的最终权重，直接用即可。
不要再乘 0.60！** 那会让语言层塌缩到 36%、事实层被隐性放大到 53%。

**校验示例**（照着算一遍，确认方向没搞反）：
```
设：维1=100 维2=50 维3=80 维4=100 维5=80 维6=100 维7=80 维8=100 维9=85

质量分 = 100×.20 + 50×.12 + 80×.12 + 100×.09 + 80×.06 + 100×.01
       + 80×.15 + 100×.15 + 85×.10
       = 20.0 + 6.0 + 9.6 + 9.0 + 4.8 + 1.0 + 12.0 + 15.0 + 8.5
       = 85.9

风险分 = 100 − 85.9 = 14.1  →  🟢 低风险  ✓ 方向自洽
```

---

# 🚨 一票否决清单

以下任一情形成立，**直接判定为对应等级，不再按加权分核算**。
理由：这些是**造假**而非文风问题，不应被其他维度的高分稀释。

| 触发条件 | 强制等级 | 理由 |
|---|---|---|
| 参考文献经 L2 验证**确认不存在** | ⛔ 高风险 | 学术造假 |
| 引文**作者/年份/期刊与真实文献不符** | 🔴 中高风险 | 幻觉特征或治学不端 |
| 同一参数在不同位置**矛盾且无解释**（>5%） | 🔴 中高风险 | 数据虚构或计算错误 |
| 声称的**数据集/规模与实际不符** | ⛔ 高风险 | 结果不可信 |
| 结果数值**无法由所述方法复现**（量级错误） | 🔴 中高风险 | 结果可能为编造 |

**豁免**：论文**主动披露**数值差异并解释来源的（求解器容差、独立实现
初始化差异等），**不触发否决**——主动披露是人工复算的正面证据。

---

# 第二层：建模逻辑深度审查

> **核心命题**：数学建模竞赛的本质是，**能用基础模型解决的，
> 就不该上复杂模型**。判定模型是否华而不实，是本层的核心结论。

五项**等权**，各 20 分，合计 100 分质量分。

## 2.1 模型常用性判断

**🟢 数模常用模型库（安全）**

```
统计类     线性/非线性回归 · 逻辑回归 · 主成分分析 · 时间序列(ARIMA/指数平滑)
聚类       K-means · 层次聚类 · 谱聚类
优化       线性规划 · 整数规划 · 混合整数规划 · 动态规划 · 贪心
几何/搜索  SAT 碰撞检测 · 二分搜索 · 扫描线 · 蒙特卡洛
系统       微分方程 · 差分方程
评价决策   AHP · 熵权法 · TOPSIS · 模糊综合评价
数据处理   加权最小二乘 · 数据协调 · 卡尔曼滤波
鲁棒       区间鲁棒 · Bertsimas 预算不确定集 · 情景分析
自定义     基于物理/几何约束推导的专门模型（需有明确问题驱动）
```

**🔴 AI 高频但数模不适用（命中即高风险）**

| 模型 | 为什么 AI 爱推 | 为什么数模不该用 |
|---|---|---|
| 深度学习 DNN/CNN/RNN/LSTM | 看起来高级 | 数据少、不可解释、易过拟合 |
| 强化学习 | 听起来智能 | 本题通常不是策略学习问题 |
| 遗传算法 / 粒子群 / 蚁群 | 名字新颖 | 比二分搜索复杂 10 倍，还不保证最优 |
| 支持向量机 SVM | 被夸大 | 高维才有优势，本题数据量小 |
| 随机森林 / XGBoost | 集成学习光环 | 样本不足，容易过拟合 |
| 贝叶斯网络 | 听起来高深 | 因果链通常不明确 |

**判分**：全部为常用模型 → 20 分；命中 1 个 AI 高频模型且无充分理由
→ 10 分 🟠；命中 ≥2 个 → 0 分 🔴 **标红**

---

## 2.2 复杂度 vs 收益评估

对每个模型问三个问题：

| 问题 | ✅ 好回答 | ❌ 坏回答 |
|---|---|---|
| 复杂度是多少？ | "时间 O(log n)，代码 10 行，流程 3 步" | "该算法高效" |
| 能否更简单？为何没用？ | "线性搜索需 50 次迭代；二分只需 4 次" | "该算法是最优选择" |
| 复杂度提升的收益？ | "精度提升 10%，计算量翻倍，综合为正" | "模型准确度更高" |

**判分**：全部模型复杂度与问题规模匹配 → 20 分；1 处过度工程化
→ 12 分 🟡；≥2 处 → 5 分 🟠 **标红**

**加分观察**：识别出模型为线性后改用解析直解、放弃通用优化器，
是**简化**而非复杂化——与 AI"上更重工具"的倾向相反，应视为人工主导证据。

---

## 2.3 华而不实五特征

| # | 特征 | ❌ 症状 | ✅ 正常 |
|---|---|---|---|
| 1 | 模型名复杂但实现不透明 | "采用改进的遗传算法"（改进了什么？答不出） | "标准 GA，Pc=0.8, Pm=0.01，来自文献[X]" |
| 2 | 效果声称无对比基线 | "该模型准确性高、鲁棒性强" | "相比蛮力搜索速度提升 15 倍（表8）" |
| 3 | 超参数调优过度 | "网格搜索调优 5 个超参数"（为什么调？） | "参数取文献推荐值，12 组扰动证明不敏感" |
| 4 | 通用化无边界 | "可广泛应用于各种工程优化问题" | "在螺距 [0.30,0.56]m 内有效，超出需分段" |
| 5 | 模型数与问题数不匹配 | 5 问建了 7–8 个模型，几乎无复用 | 1 个核心框架 + 5 个变体 |

**判分**：0–1 项 → 20 分；2 项 → 12 分 🟡；3 项 → 6 分 🟠 **标红**；
≥4 项 → 0 分 🔴 **标红**

---

## 2.4 模型选择"三问法"

对**每个**模型逐一回答：

```
【问1】本问的问题性质是什么？（目标 + 约束是否明确）
  ✅ "问题1要求在螺距 p=0.55m 约束下计算 224 把手的位置"
  ❌ "问题1需要建立位置模型"

【问2】本问有什么特殊的数据或结构特征？（为什么这个模型适合）
  ✅ "本问碰撞对象都是凸多边形且 ≤3 个，SAT 复杂度仅 O(n)"
  ❌ "选 SAT 因为它精度高、速度快"（通用套话，没指本题）

【问3】为什么不用替代方案？
  ✅ "线性搜索 O(n) 需 50 次；三叉搜索仅快 10% 但代码复杂度翻倍；
      启发式不保证最优。故选二分搜索。"
  ❌ "采用改进的粒子群优化"（不说为什么不用二分搜索）
```

**⭐ 标准答案形态**：先指出本题的结构特征 → 说明常规做法为何失效
→ 给出替代方案及其数学依据。例如：

> "网络含环（如 A1–A2–A4–A3 回路），不存在天然的追溯顺序，
> 故将节点碳强度方程改写为不动点迭代形式求解。"

**判分**：全部模型三问皆可答 → 20 分；1 个模型缺 1 问 → 14 分 🟡；
多个模型缺问 → 7 分 🟠 **标红**；普遍答不出 → 0 分 🔴 **标红**

---

## 2.5 建模路径风格十项对照

| 对比方面 | H：人主导的渐进建模 | A：AI 式复杂化倾向 |
|---|---|---|
| 建模路径 | 先建基线，再依暴露的问题改进 | 追求一步到位，同时上多种方法 |
| 出发点 | 抓主要矛盾，有依据地简化 | 尽量覆盖更多变量，未说明必要性 |
| 模型选择 | 可解释、可实现、与题匹配 | 倾向热门算法，叠加多个模型名 |
| 模型假设 | 主动忽略次要因素并说明边界 | 为"更真实"引入大量来源不清的参数 |
| 数据适配 | 按样本量、缺失、噪声调整 | 忽略样本量与参数可辨识性 |
| 求解过程 | 主线连贯，步骤输入输出明确 | "模型菜单"或方法拼盘，接口不清 |
| 结果解释 | 说得清每步的目的与现实含义 | 能列步骤，说不清必要性 |
| 论文表达 | 结构清晰，便于复现验证 | 篇幅长术语多，掩盖核心贡献 |
| 稳健性 | 结构简洁，易定位错误做敏感性 | 环节多，误差累积却未分析 |
| 评审效果 | 体现完整逻辑与清晰取舍 | 易被评为算法堆砌 |

**执行**：逐项标 `H`（有证据）/ `M`（混合或证据不足）/ `A`（有证据）。
**每项必须附页码、章节或具体模型证据，不得凭模型名称直接标记。**

| A 项数量 | 得分 | 判断 |
|---:|---:|---|
| 0–2 | 20 | 🟢 人主导的渐进建模 |
| 3–4 | 13 | 🟡 局部复杂化 |
| 5–6 | 6 | 🟠 **标红** 主线被方法拼盘削弱 |
| 7–10 | 0 | 🔴 **标红** 系统性复杂化 |

> **复杂 ≠ AI**。若复杂模型由题目规模、非线性、动态性或精度要求驱动，
> 并具备基线对比、参数来源和量化收益，应降低该项风险。

---

## 第二层汇总

```
第二层质量分 = 2.1 + 2.2 + 2.3 + 2.4 + 2.5   （各 20 分，合计 100）
第二层风险分 = 100 − 第二层质量分
```

---

# 📐 最终评分

```
最终 AI 风险分 = (第一层风险分 + 第二层风险分) / 2
```

**置信度声明**（必须在报告中写明）：

| 输入材料 | 置信度 | 误差 |
|---|---|---|
| 仅论文 | 中 | ±8–12 分 |
| 论文 + 赛题 | 中 | ±6–10 分 |
| 论文 + 赛题 + 代码/结果 | 中高 | ±5–8 分 |
| 再加版本历史或对话记录 | 高 | ±3–5 分（仍非身份鉴定） |

---

# 🎨 报告标红规范（强制）

报告必须让问题**一眼可见**，不得把风险项混在通过项里平铺呈现。

| 状态 | 色值 | 触发 | 呈现要求 |
|---|---|---|---|
| 🔴 严重 | `#c0392b` | 维度 < 30 或触发否决 | 红底红框卡片 + 置于报告最前 + 列证据位置 |
| 🟠 警示 | `#e67e22` | 维度 30–54 | 橙色左边框 + 写明改进动作 |
| 🟡 注意 | `#f39c12` | 维度 55–79 | 黄色标记 + 一句话说明 |
| 🟢 通过 | `#27ae60` | 维度 ≥ 80 | 常规呈现，不占视觉重心 |

**五条硬性要求**：

1. 任一维度 `< 55` 时，报告顶部**必须**有红色警示区，汇总全部标红项
2. 每个标红项必须含三要素：**问题描述 + 证据位置（页/节）+ 具体改法**
3. **不得**用"建议优化""可以更好"这类模糊措辞描述标红项
4. 评分表中标红行须用**红色背景**，不能只靠一个小图标区分
5. 只有全部维度 ≥ 80，才可在结论区使用绿色通过卡片

---

# 🖥 HTML 报告模板

> AI 请以下面这份骨架生成报告，把 `{{...}}` 替换为实际内容。
> 保持双版本切换（简洁版 / 完整版）与科研蓝白配色。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{论文标题}} AI痕迹审计报告 | BZD数模社</title>
<style>
:root{--primary:#1a3a52;--secondary:#2c5aa0;--sev:#c0392b;
  --warn:#e67e22;--note:#f39c12;--ok:#27ae60;--text-dark:#1c2e3e;--text-light:#555}
*{margin:0;padding:0;box-sizing:border-box}
html{font-size:14px;scroll-behavior:smooth}
body{font-family:'STIX Two Text','Times New Roman','宋体',serif;line-height:1.75;
  color:var(--text-dark);background:linear-gradient(135deg,#f5f7fa,#e9ecef);padding-bottom:40px}
header{background:linear-gradient(135deg,var(--primary),var(--secondary));color:#fff;
  padding:38px 30px;text-align:center;border-bottom:3px solid var(--sev)}
header h1{font-size:29px;font-weight:700;margin-bottom:8px}
header .sub{font-size:15px;opacity:.95;margin-bottom:6px}
header .meta{font-size:12.5px;opacity:.82}
.version-tabs{display:flex;justify-content:center;gap:15px;margin-top:24px;flex-wrap:wrap}
.version-tabs button{background:rgba(255,255,255,.15);color:#fff;
  border:1.5px solid rgba(255,255,255,.3);padding:11px 22px;cursor:pointer;
  font-size:14px;font-weight:600;border-radius:6px;font-family:inherit;transition:all .3s}
.version-tabs button.active{background:#fff;color:var(--primary);font-weight:700}
.container{max-width:1020px;margin:28px auto;background:#fff;padding:42px;
  border-radius:8px;box-shadow:0 4px 16px rgba(0,0,0,.08);border-left:4px solid var(--secondary)}
section{margin-bottom:36px}
h2{font-size:21px;color:var(--primary);border-bottom:2.5px solid var(--secondary);
  padding-bottom:10px;margin:32px 0 18px;font-weight:700}
h3{font-size:16px;color:var(--secondary);margin:22px 0 12px;font-weight:700}
h3.flag-sev{color:var(--sev)}
p{margin-bottom:12px} ul,ol{margin:10px 0 14px 24px} li{margin-bottom:7px}

/* 顶部红色警示区（维度<55时必须出现） */
.alert-zone{border:2.5px solid var(--sev);background:linear-gradient(135deg,#fdf3f2,#fbe9e7);
  border-radius:10px;padding:22px 26px;margin:20px 0 28px}
.alert-zone .hd{font-size:17px;font-weight:700;color:var(--sev);margin-bottom:14px;
  display:flex;align-items:center;gap:9px}
.alert-zone .hd .cnt{background:var(--sev);color:#fff;border-radius:12px;padding:1px 11px;font-size:13px}
.alert-item{background:#fff;border-left:5px solid var(--sev);border-radius:0 6px 6px 0;
  padding:14px 18px;margin-bottom:12px}
.alert-item:last-child{margin-bottom:0}
.alert-item .ti{font-weight:700;color:var(--sev);margin-bottom:7px;font-size:14.5px}
.alert-item .row{font-size:13.3px;margin-bottom:5px}
.alert-item .row b{color:var(--primary);display:inline-block;min-width:64px}

/* 结论卡 */
.verdict{display:flex;align-items:center;gap:30px;flex-wrap:wrap;border-radius:10px;padding:26px 30px;margin:20px 0}
.verdict.v-ok{background:linear-gradient(135deg,#eafaf1,#d5f4e6);border:2px solid var(--ok)}
.verdict.v-warn{background:linear-gradient(135deg,#fef7f0,#fce4d0);border:2px solid var(--warn)}
.verdict.v-sev{background:linear-gradient(135deg,#fdf3f2,#f9d5d0);border:2px solid var(--sev)}
.verdict .score{font-size:60px;font-weight:700;line-height:1}
.verdict.v-ok .score{color:var(--ok)}
.verdict.v-warn .score{color:var(--warn)}
.verdict.v-sev .score{color:var(--sev)}
.verdict .score small{font-size:20px;color:var(--text-light);font-weight:400}
.verdict .desc{flex:1;min-width:260px}
.verdict .desc .lv{font-size:21px;font-weight:700;margin-bottom:6px}
.verdict .desc .note{font-size:13.5px;color:var(--text-light)}

table{width:100%;border-collapse:collapse;margin:16px 0;font-size:13.4px}
th{background:var(--primary);color:#fff;padding:11px 12px;text-align:left;font-weight:600}
td{padding:9px 12px;border-bottom:1px solid #e3e8ec;vertical-align:top}
tr:nth-child(even) td{background:#f8fafb}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.ctr,th.ctr{text-align:center}
/* 标红行：必须用背景色，不能只靠图标 */
tr.r-sev td{background:#fdecea !important}
tr.r-sev td:first-child{border-left:4px solid var(--sev);font-weight:700}
tr.r-warn td{background:#fef5eb !important}
tr.r-warn td:first-child{border-left:4px solid var(--warn);font-weight:700}
tr.r-note td{background:#fffbf0 !important}
tr.r-note td:first-child{border-left:4px solid var(--note)}

.badge{display:inline-block;padding:2px 9px;border-radius:10px;font-size:11.5px;font-weight:700}
.b-ok{background:#d5f4e6;color:#186a3b} .b-note{background:#fdebd0;color:#9c640c}
.b-warn{background:#fae5d3;color:#a04000} .b-sev{background:#fadbd8;color:#943126}

.box{border-left:4px solid var(--secondary);background:#f4f8fb;padding:16px 20px;
  border-radius:0 6px 6px 0;margin:16px 0}
.box.good{border-left-color:var(--ok);background:#f0faf4}
.box.warn{border-left-color:var(--warn);background:#fef7f0}
.box.sev{border-left-color:var(--sev);background:#fdf3f2}
.box .t{font-weight:700;margin-bottom:8px;font-size:14.5px}
blockquote{border-left:3px solid #95a5a6;background:#fafbfc;margin:12px 0;
  padding:11px 18px;color:#33475b;font-size:13.4px}
.formula{background:#f7f9fb;border:1px solid #e1e8ed;border-radius:5px;padding:13px 16px;
  margin:12px 0;font-family:'Consolas',monospace;font-size:12.8px;overflow-x:auto;line-height:1.85}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12.5px;margin:14px 0;
  padding:12px 16px;background:#f8fafb;border-radius:6px;border:1px solid #e3e8ec}
.legend span{display:flex;align-items:center;gap:6px}
.legend i{width:13px;height:13px;border-radius:3px;display:inline-block}
footer{text-align:center;color:var(--text-light);font-size:12.5px;padding:26px 20px;line-height:1.9}
.hidden{display:none}
@media print{body{background:#fff}.version-tabs{display:none}
  .container{box-shadow:none;margin:0;max-width:100%}.hidden{display:block !important}}
@media(max-width:640px){.container{padding:24px 18px;margin:16px}
  .verdict .score{font-size:46px}table{font-size:12.4px}}
</style>
</head>
<body>

<header>
  <h1>数学建模论文 AI 痕迹审计报告</h1>
  <div class="sub">{{论文标题}}</div>
  <div class="meta">BZD 审计框架 v2.2 严格判分版 · 九维融合检测 · {{审计日期}}</div>
  <div class="version-tabs">
    <button id="tab-brief" class="active" onclick="showView('brief')">简洁版</button>
    <button id="tab-full" onclick="showView('full')">完整版</button>
  </div>
</header>

<!-- ═══ 简洁版 ═══ -->
<div class="container" id="view-brief">

  <!-- 有维度<55时必须出现；否则整块删除 -->
  <div class="alert-zone">
    <div class="hd">⚠ 需要处理的问题 <span class="cnt">{{N}} 项</span></div>
    <div class="alert-item">
      <div class="ti">🔴 严重 · {{维度名}} — 得分 {{X}}/100</div>
      <div class="row"><b>问题：</b>{{具体描述}}</div>
      <div class="row"><b>证据：</b>{{页码/章节}}</div>
      <div class="row"><b>改法：</b>{{可直接执行的具体动作}}</div>
    </div>
  </div>

  <section>
    <h2>一、审计结论</h2>
    <div class="verdict v-ok">
      <div class="score">{{风险分}}<small>/100</small></div>
      <div class="desc">
        <div class="lv">{{🟢 低风险}}</div>
        <div class="note">{{一句话总评}}<br><strong>建议：{{处理意见}}</strong></div>
      </div>
    </div>
    <table>
      <tr><th>层级</th><th class="num">质量分</th><th class="num">风险分</th><th>核心判断</th></tr>
      <tr><td>第一层：九维语言+事实</td><td class="num">{{}}</td><td class="num">{{}}</td><td>{{}}</td></tr>
      <tr><td>第二层：建模逻辑</td><td class="num">{{}}</td><td class="num">{{}}</td><td>{{}}</td></tr>
      <tr style="font-weight:700;background:#eef4f9"><td>最终</td><td class="num">{{}}</td><td class="num">{{}}</td><td>{{}}</td></tr>
    </table>
    <p style="font-size:13px;color:var(--text-light)">置信度：<strong>{{}}</strong>（{{材料说明}}）</p>
  </section>

  <section>
    <h2>二、九维评分速览</h2>
    <div class="legend">
      <span><i style="background:var(--sev)"></i>严重 &lt;30</span>
      <span><i style="background:var(--warn)"></i>警示 30–54</span>
      <span><i style="background:var(--note)"></i>注意 55–79</span>
      <span><i style="background:var(--ok)"></i>通过 ≥80</span>
    </div>
    <table>
      <tr><th>维度</th><th class="ctr">权重</th><th class="num">得分</th><th class="ctr">状态</th><th>依据</th></tr>
      <tr><td>1 高频连接词</td><td class="ctr">20%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>2 排比/同构句式</td><td class="ctr">12%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>3 拔高词（5级）</td><td class="ctr">12%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>4 被动句占比</td><td class="ctr">9%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>5 段落规律性</td><td class="ctr">6%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>6 文本复杂度</td><td class="ctr">1%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>7 引文验证</td><td class="ctr">15%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>8 数值一致性</td><td class="ctr">15%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>9 术语一致性</td><td class="ctr">10%</td><td class="num">{{}}</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
    </table>
  </section>

  <section>
    <h2>三、一票否决项核查</h2>
    <table>
      <tr><th>否决条件</th><th class="ctr">本文</th><th>结论</th></tr>
      <tr><td>参考文献确认不存在</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>引文作者/年份/期刊不符</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>参数矛盾且无解释（&gt;5%）</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>数据集/规模与实际不符</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
      <tr><td>结果无法由所述方法复现</td><td class="ctr">{{}}</td><td>{{}}</td></tr>
    </table>
  </section>

</div>

<!-- ═══ 完整版 ═══ -->
<div class="container hidden" id="view-full">
  {{完整版内容：
    一、审计对象与边界（含置信度说明）
    二、第一层九维逐维展开（每维给出：检测过程表格 + 判分依据 + 得分）
    三、第二层五项逐项展开（含三问法表、十项对照表、跨问数据流图）
    四、最终评分（formula 块展示完整计算过程）
    五、改进清单（按 严重/警示/注意 排序，每项含 位置+改法+工作量）
    六、审计边界声明}}
</div>

<footer>
  <strong>BZD 数模社制作</strong><br>
  审计框架 v2.2 严格判分版 · 九维融合检测（语言 60% + 事实 40%）· 一票否决 + 强制标红<br>
  {{审计日期}} · 置信度 {{}} · 支持打印与存档
</footer>

<script>
function showView(v){
  document.getElementById('view-brief').classList.toggle('hidden', v!=='brief');
  document.getElementById('view-full').classList.toggle('hidden', v!=='full');
  document.getElementById('tab-brief').classList.toggle('active', v==='brief');
  document.getElementById('tab-full').classList.toggle('active', v==='full');
  window.scrollTo({top:0,behavior:'smooth'});
}
</script>
</body>
</html>
```

---

# ✅ 交付前自检清单

AI 生成报告后，请对照本清单核对：

**计算正确性**
- [ ] 语言层六维权重用的是 20/12/12/9/6/1，**没有**再乘 0.60
- [ ] 已执行 `风险分 = 100 − 质量分` 的转换
- [ ] 用风险分（不是质量分）查的等级表
- [ ] 最终分 = 两层**风险分**的平均

**证据完整性**
- [ ] 每个维度的判分都附了论文中的具体位置
- [ ] 每个标红项都有「问题 + 证据位置 + 具体改法」三要素
- [ ] 一票否决五项逐条核查并给出结论
- [ ] 参数溯源表列出了不少于 8 个关键参数并复算了算术关系
- [ ] 引文抽查了不少于 5 篇并标注 L1/L2/L3 结果

**呈现规范**
- [ ] 任一维度 < 55 时，顶部有红色警示区
- [ ] 标红行用了红色背景，不是只加图标
- [ ] 没有用"建议优化""可以更好"等模糊措辞描述标红项
- [ ] 简洁版 / 完整版双标签可正常切换
- [ ] 报告标注了"BZD 数模社制作"与置信度

---

# ❓ 常见问题

**Q：论文里写了"使用了 AI 工具声明"，是不是直接算高风险？**
A：不是。本工具判的是 AI **拼装**痕迹，不是是否用过 AI。声明使用
AI 辅助、但建模主线由人主导、参数可溯源、结果可复算的论文，
完全可以是低风险。合规的 AI 辅助应当被鼓励，而非惩罚。

**Q：论文用了深度学习就一定高风险吗？**
A：不一定。若题目本身是大规模非线性预测任务、数据量充足，
且论文给出了与基础模型的量化对比（说明为什么回归/ARIMA 不够用），
应降低该项风险。判断标准是**必要性论证**，不是模型名称。

**Q：数值有 0.1% 的差异，算不算造假？**
A：看有没有解释。**主动披露**并说明来源（求解器容差、独立实现
初始化差异等）→ 不但不扣分，反而是人工复算的**加分证据**。
未加解释的 1–5% 偏差 → 35 分标红；>5% → 触发否决。

**Q：找不到某篇参考文献，是不是就判虚构？**
A：先排除检索方式问题——换 Google Scholar / 知网 / OpenAlex 各试一次，
核对年份和作者拼写。三个渠道都查不到，才判定虚构并触发一票否决。
报告中应写明"经 X、Y、Z 三个渠道检索未果"。

**Q：AI 没按格式输出，或者报告很敷衍怎么办？**
A：追加一句：「请严格按照文档中的九维框架逐维给出得分和证据位置，
不要跳过任何维度；标红项必须包含问题、证据位置、具体改法三要素。」

**Q：论文很长，AI 说超出长度限制？**
A：分两次发。第一次发本文档 + 论文前半（至各问建模），
让 AI 先做第一层语言层面检测；第二次发论文后半 + 参考文献，
补做事实层面与第二层，最后让它汇总出完整报告。

---

# ⚠️ 使用边界

- 本评分**不是作者身份概率**，不能替代查重或官方 AIGC 检测服务
- 仅凭成稿无法证明某句话由 AI 生成
- 数模论文的规范句式、模型名称、专业术语天然可能重复，
  框架已在维度 1 和维度 5 设置豁免
- 模型的**创新性** ≠ AI 拼装，本工具只判断模型选择的**合理性**
- 报告中的每一项判定都必须附证据位置，无证据的判定不成立

---

**BZD 数模社制作** · 审计框架 v2.2 严格判分版
适用：CUMCM 国赛 / 美赛 / 研赛 / 校赛等各类数学建模竞赛
平台：Claude · ChatGPT · Gemini · Kimi · DeepSeek · 豆包 等任意长文本 AI
