# BZD数模论文AI痕迹审计 - 离线Prompt指南

## 📋 使用说明

**适用场景：** 当无法使用Claude Code或Codex的skill时，用户可以将本文档和论文一起发给任何AI（ChatGPT、Claude Web、Gemini等），AI将按照此指南进行分析并输出HTML报告。

**使用方法：**
1. 复制本文档全部内容
2. 连同论文内容一起发给AI
3. AI将生成HTML格式的审计报告
4. 用浏览器打开HTML文件查看结果

---

## 🎯 审计目标

对数学建模竞赛论文进行两层递进式AI痕迹检测：
- **第一层（权重60%）：** 语言特征扫描 + 其他四维评价
- **第二层（权重40%）：** 建模逻辑深度审查

最终输出：AI风险评分（0-100）+ 分层HTML报告

---

## 📊 第一层：五维框架评分标准

### 1. 语言模板化（权重60%）

#### 检查项1：高频连接词密度
**高频连接词清单：**
- 超高频（5星）：综上所述、综合上述、进一步、此外、与此同时、值得注意的是、可以看出、由此可见
- 高频（4星）：一般来说、不仅如此、所以说、因此可见、不得不说、需要指出的是、不容否认
- 中频（3星）：当然、显然、毋庸置疑、不言而喻、众所周知、相比之下、而言之

**评分标准：**
```
密度 < 15%  → 90-100分（正常）
密度 15-20% → 70-89分（注意）
密度 20-25% → 50-69分（需改）
密度 > 25%  → 0-49分（高风险）
```

#### 检查项2：排比与同构句式
**特征识别：**
- 三项以上排比：具有XX、YY、ZZ等特点
- 同构句式重复：采用方法A进行XX，采用方法B进行YY，采用方法C进行ZZ

**风险判定：**
- 排比后无数据支撑 → 风险
- 连续4个同构句式 → 风险

#### 检查项3：被动句占比
**评分标准：**
```
10-20% → 低风险
20-30% → 中风险
> 30%  → 高风险
```

#### 检查项4：拔高词检查
**拔高词清单：** 具有XX性、显著提高、大幅、奠定基础、彰显价值、完美实现、取得成果、有效解决

**风险标准：** 拔高词后无量化数据 → 风险

#### 检查项5-8：其他四维（合计40%）
- **结构与论证（12%）：** 逻辑链条完整、假设合理、问题分析清晰
- **建模专属性（15%）：** 是否说明本题特征、为什么选这个模型
- **求解与验证（10%）：** 结果验证充分、灵敏度分析、数据合理
- **来源与一致性（3%）：** 参考文献数量（推荐10+篇）、参数溯源清晰

**第一层总分计算：**
```
第一层分数 = 语言模板化得分×60% + 其他四维平均得分×40%
```

---

## 🔍 第二层：建模逻辑深度审查

### 2.1 模型常用性判断

**竞赛常见模型（绿色清单）：**
- 基础类：线性回归、非线性回归、ARIMA、K-means、分类算法、傅里叶
- 几何类：SAT、二分搜索、扫描线、蒙特卡洛、微分方程、差分方程
- 优化类：线性规划、整数规划、动态规划、贪心算法
- 评价类：AHP、TOPSIS、熵权法、模糊综合评价
- 自定义类：基于几何约束的特殊曲线、基于物理过程的动力学方程

**AI高频但不适合数模的模型（红色清单）：**
- 深度学习：DNN、CNN、RNN、LSTM → 🔴高风险
- 强化学习 → 🔴高风险
- 遗传算法、蚁群算法、粒子群优化 → 🔴高风险
- 支持向量机、随机森林、XGBoost → 🟠中风险

**评分标准：**
```
全为常见模型 → 90-100分
含有1-2个高频模型 → 50-70分
含有3+个高频模型 → 0-50分
```

### 2.2 复杂度vs收益评估

**评分标准：**
- 复杂度与问题规模匹配 → 80-100分
- 有一定过度工程化 → 50-79分
- 严重过度工程化 → 0-49分

**判定方法：** 用O(n)符号或说明，检查是否与问题数据量匹配

### 2.3 华而不实识别（五大特征）

**特征1：模型名复杂，实现细节不清**
- 出现"改进的""融合的""混合的" → 检查后续是否说明改进点
- 无改进说明 → 风险

**特征2：效果声称无对比基线**
- 出现"精度高""效率高""鲁棒性强" → 检查是否有具体数值
- 无量化数据 → 风险

**特征3：超参数调优过度**
- 出现"网格搜索""贝叶斯优化""参数调整" → 检查是否说明必要性
- 无必要性说明 → 风险

**特征4：模型通用化无边界**
- 出现"广泛应用于""适用范围广" → 检查是否明确限定条件
- 无条件限定 → 风险

**特征5：问题与模型个数不匹配**
- 5个问题却有7-8个不同模型 → 检查是否存在复用
- 复用少 → 风险

**评分标准：**
```
无高风险特征 → 90-100分
有1-2个特征 → 60-89分
有3-5个特征 → 0-59分
```

### 2.4 模型选择"三问法"

对每个模型提出三个问题：

**问1：问题明确吗？**
- 良好示例："问题要求在约束条件下计算位置"
- 风险示例："采用该模型进行求解"

**问2：本题数据特征是什么？**
- 良好示例："本题有螺距恒定、数据量2000等特征"
- 风险示例："该模型可处理各种数据"

**问3：为什么选这个而不选替代方案？**
- 良好示例："相比线性搜索O(n)，二分搜索O(log n)更高效"
- 风险示例："缺少此说明"

**评分标准：**
```
5个问题都能清晰回答三问 → 90-100分
3-4个问题完全通过 → 60-89分
<3个问题通过 → 0-59分
```

**第二层总分计算：**
```
第二层分数 = (模型常用性 + 复杂度评估 + 华而不实 + 三问法) ÷ 4
```

---

## 📈 最终评分计算

```
最终AI风险分 = (第一层得分 + 第二层得分) ÷ 2

风险等级划分：
0-20    🟢 低风险      → 可直接接收
21-35   🟡 中低风险    → 可接收，建议改进
36-54   🟠 中风险      → 需深度检查
55-74   🔴 中高风险    → 强烈建议拒稿或改稿
75-100  ⛔ 高风险      → 建议拒稿
```

---

## 📝 参数溯源检查清单

所有参数应能追溯来源：
- **L1：赛题直接给出** ✓ 最佳
- **L2：前问推导结果** ✓ 良好
- **L3：物理约束推导** ✓ 可接受
- **L4：来源不明** ❌ 高风险

---

## 📋 问间对接检查

检查Q1→Q2→Q3→Q4→Q5的数据流是否明确：
- 明确说明"Q_i的结果X用于Q_{i+1}的约束Y" → 低风险
- 含糊其辞或无说明 → 高风险

---

## 🔧 具体执行步骤

### 第1步：基本信息采集
```
论文标题：[X]
参赛队名：[X]
问题数：5题（Q1-Q5）
总页数：[X]页
参考文献数：[X]篇
```

### 第2步：逐部分扫描
- **摘要部分**：检查第一层5项 + 其他四维
- **问题分析部分**：同上
- **Q1-Q5部分**：分别检查第一层 + 第二层（2.1-2.4）
- **求解验证部分**：检查参数溯源表、问间对接

### 第3步：评分汇总
```
第一层：
- 语言模板化：[X]/100
- 结构与论证：[X]/100
- 建模专属性：[X]/100
- 求解与验证：[X]/100
- 来源与一致性：[X]/100
→ 第一层总分 = 语言×60% + 其他×40% = [X]/100

第二层：
- 2.1 模型常用性：[X]/100
- 2.2 复杂度评估：[X]/100
- 2.3 华而不实：[X]/100
- 2.4 三问法：[X]/100
→ 第二层总分 = ([X]+[X]+[X]+[X])÷4 = [X]/100

最终分数 = ([第一层]+[第二层])÷2 = [X]/100
```

---

## 📊 输出HTML模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BZD数学建模论文AI痕迹审计报告</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'STIX Two Text', 'Times New Roman', serif;
            line-height: 1.75;
            color: #1c2e3e;
            background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
            padding: 40px;
        }
        header {
            background: linear-gradient(135deg, #1a3a52 0%, #2c5aa0 100%);
            color: white;
            padding: 40px;
            text-align: center;
            border-bottom: 3px solid #e74c3c;
            margin-bottom: 30px;
            border-radius: 8px;
        }
        header h1 { font-size: 32px; margin-bottom: 10px; }
        header p { font-size: 15px; opacity: 0.95; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
        h2 { color: #1a3a52; border-bottom: 2px solid #2c5aa0; padding-bottom: 10px; margin: 25px 0 15px 0; }
        h3 { color: #2c5aa0; margin: 15px 0 10px 0; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th { background: linear-gradient(135deg, #1a3a52 0%, #2c5aa0 100%); color: white; padding: 12px; text-align: left; }
        td { padding: 10px; border-bottom: 1px solid #ecf0f1; }
        tr:nth-child(even) { background: #f9fafb; }
        .badge { display: inline-block; padding: 5px 10px; border-radius: 10px; font-weight: bold; font-size: 11px; margin: 0 5px; }
        .badge-low { background: #d4edda; color: #155724; }
        .badge-mid { background: #fff3cd; color: #856404; }
        .badge-high { background: #f8d7da; color: #721c24; }
        .section { margin: 20px 0; padding: 15px; border-left: 4px solid #2c5aa0; background: #f9fafb; border-radius: 4px; }
        .problem { margin: 10px 0; padding: 10px; background: #f0f4f8; border-left: 3px solid #e74c3c; }
        footer { text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #bdc3c7; color: #666; font-size: 12px; }
    </style>
</head>
<body>
    <header>
        <h1>🔐 BZD数学建模论文AI痕迹审计报告</h1>
        <p>两层递进式检查 | 学术科研级分析 | v2.0</p>
    </header>

    <div class="container">
        <h2>📍 核心结论</h2>
        <div class="section">
            <p><strong>论文标题：</strong> [论文标题]</p>
            <p><strong>最终AI风险分：</strong> <span style="font-size: 20px; color: #2c5aa0; font-weight: bold;">[X]/100</span></p>
            <p><strong>风险等级：</strong> 
                <span class="badge badge-low">🟢 低</span> / 
                <span class="badge badge-mid">🟡 中低</span> / 
                <span class="badge badge-high">🔴 中高</span>
            </p>
            <p style="margin-top: 10px;"><strong>最终建议：</strong> 
                <span style="color: #27ae60; font-weight: bold;">可直接接收</span> / 
                <span style="color: #f39c12; font-weight: bold;">需改进</span> / 
                <span style="color: #c0392b; font-weight: bold;">建议拒稿</span>
            </p>
        </div>

        <h2>⚠️ 问题定位（优先级排序）</h2>
        
        <h3>🔴 P0优先级（影响最大，必须改进）</h3>
        <div class="problem">
            <strong>位置：P[X] - [章节名]</strong><br>
            ❌ 问题："[原文问题句子]"<br>
            ✓ 改为："[改进建议]"
        </div>
        <div class="problem">
            <strong>位置：P[X] - [章节名]</strong><br>
            ❌ 问题："[原文问题句子]"<br>
            ✓ 改为："[改进建议]"
        </div>

        <h3>🟠 P1优先级（快速可改，容易优化）</h3>
        <div class="problem">
            <strong>位置：P[X] - [章节名]</strong><br>
            ❌ 问题："[原文问题句子]"<br>
            ✓ 改为："[改进建议]"
        </div>

        <h3>🟢 P2优先级（锦上添花，可选改进）</h3>
        <div class="problem">
            <strong>位置：P[X] - [章节名]</strong><br>
            ❌ 问题："[原文问题句子]"<br>
            ✓ 改为："[改进建议]"
        </div>

        <h2>📊 第一层：五维框架评分</h2>
        <table>
            <tr>
                <th>维度</th>
                <th>权重</th>
                <th>得分</th>
                <th>说明</th>
            </tr>
            <tr>
                <td><strong>语言模板化</strong></td>
                <td>60%</td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td>高频连接词、拔高词、排比句、被动句</td>
            </tr>
            <tr>
                <td><strong>结构与论证</strong></td>
                <td>12%</td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td>逻辑完整、问题分析清晰</td>
            </tr>
            <tr>
                <td><strong>建模专属性</strong></td>
                <td>15%</td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td>本题特征与模型选择对应度</td>
            </tr>
            <tr>
                <td><strong>求解与验证</strong></td>
                <td>10%</td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td>结果验证、灵敏度分析</td>
            </tr>
            <tr>
                <td><strong>来源与一致性</strong></td>
                <td>3%</td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td>参考文献、参数溯源</td>
            </tr>
            <tr style="background: #f0f4f8; font-weight: bold;">
                <td colspan="2">第一层总分</td>
                <td style="color: #2c5aa0;">[X]/100</td>
                <td></td>
            </tr>
        </table>

        <h2>🔍 第二层：建模逻辑审查</h2>
        <table>
            <tr>
                <th>检查项</th>
                <th>得分</th>
                <th>评价</th>
            </tr>
            <tr>
                <td><strong>模型常用性</strong><br><small>是否为竞赛常见模型</small></td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td><span class="badge badge-low">✓ 常见</span> / <span class="badge badge-high">✗ 高频</span></td>
            </tr>
            <tr>
                <td><strong>复杂度评估</strong><br><small>是否过度工程化</small></td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td><span class="badge badge-low">✓ 合理</span> / <span class="badge badge-high">✗ 过度</span></td>
            </tr>
            <tr>
                <td><strong>华而不实识别</strong><br><small>五大特征检查</small></td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]/100</td>
                <td><span class="badge badge-low">✓ 通过</span> / <span class="badge badge-high">✗ 存在</span></td>
            </tr>
            <tr>
                <td><strong>三问法评价</strong><br><small>模型选择论证完整度</small></td>
                <td style="color: #2c5aa0; font-weight: bold;">[X]%</td>
                <td>[X]个问题通过 / [X]个问题缺失</td>
            </tr>
            <tr style="background: #f0f4f8; font-weight: bold;">
                <td>第二层总分</td>
                <td style="color: #2c5aa0;">[X]/100</td>
                <td></td>
            </tr>
        </table>

        <h2>📈 最终评分与推荐</h2>
        <div class="section" style="border-left-color: #27ae60;">
            <p><strong>最终AI风险分：</strong> <span style="font-size: 18px; color: #2c5aa0; font-weight: bold;">([第一层] + [第二层]) ÷ 2 = [X]/100</span></p>
            <p style="margin-top: 10px;"><strong>风险等级对应：</strong></p>
            <ul style="margin-left: 20px; margin-top: 8px;">
                <li><span class="badge badge-low">🟢 0-20</span> 低风险 — 语言规范、建模清晰、无AI迹象</li>
                <li><span class="badge badge-mid">🟡 21-35</span> 中低风险 — 有改进空间，但无严重问题</li>
                <li><span class="badge badge-high">🔴 36-54</span> 中风险 — 多维度问题，需深度检查</li>
                <li><span class="badge badge-high">🔴 55-74</span> 中高风险 — 可能涉及AI拼装</li>
                <li><span class="badge badge-high">⛔ 75-100</span> 高风险 — 确认有AI拼装迹象</li>
            </ul>
            <p style="margin-top: 12px;"><strong>最终推荐：</strong></p>
            <ul style="margin-left: 20px;">
                <li>✅ 接收 — 评分 < 20，无明显AI痕迹</li>
                <li>⚠️ 有条件接收 — 评分 20-35，改进后可接收</li>
                <li>❌ 强制改稿或拒稿 — 评分 > 35，多维度问题</li>
            </ul>
        </div>

        <h2>📋 参数溯源表</h2>
        <table>
            <tr>
                <th>参数名</th>
                <th>符号</th>
                <th>数值</th>
                <th>来源</th>
                <th>位置</th>
            </tr>
            <tr>
                <td>[参数1]</td>
                <td>α</td>
                <td>[数值]</td>
                <td>✓ 赛题直接给出</td>
                <td>P[X]</td>
            </tr>
            <tr>
                <td>[参数2]</td>
                <td>β</td>
                <td>[数值]</td>
                <td>✓ Q1推导</td>
                <td>P[X]</td>
            </tr>
            <tr>
                <td>[参数3]</td>
                <td>γ</td>
                <td>[数值]</td>
                <td>❌ 来源不明</td>
                <td>P[X]</td>
            </tr>
        </table>

        <h2>💡 最优先修改的五项</h2>
        <ol style="margin-left: 20px;">
            <li><strong>P0-1：</strong> [具体问题] → [改进方向]</li>
            <li><strong>P0-2：</strong> [具体问题] → [改进方向]</li>
            <li><strong>P1-1：</strong> [具体问题] → [改进方向]</li>
            <li><strong>P1-2：</strong> [具体问题] → [改进方向]</li>
            <li><strong>P2-1：</strong> [具体问题] → [改进方向]</li>
        </ol>

    </div>

    <footer>
        <p><strong>🔐 BZD数学建模社制作</strong> | 学术评审级精细分析工具</p>
        <p style="margin-top: 8px;">版本：v2.0 | © 2024 BZD数学建模社 | 本报告仅供学术评审和教学参考</p>
    </footer>
</body>
</html>
```

---

## 🚀 使用流程

### 步骤1：准备文件
- 复制本Prompt文档全部内容
- 准备要审计的论文（可以是文本、PDF内容复制、Word内容复制）

### 步骤2：发送给AI
```
我有一篇数学建模论文需要进行AI痕迹审计。

【审计指南】
[粘贴本Prompt文档的全部内容]

【论文内容】
[粘贴论文全文或核心部分]

请按照上述指南进行完整审计，最后生成HTML格式的审计报告。
```

### 步骤3：等待AI生成报告
AI将：
1. 按第一层标准逐部分扫描
2. 按第二层标准深度评审
3. 计算两层评分
4. 生成完整的HTML报告

### 步骤4：保存和查看
- 将AI生成的HTML代码复制
- 保存为 `.html` 文件（例：`审计报告.html`）
- 用浏览器打开查看报告

---

## ✅ 质量保证清单

AI在执行审计时应检查：
- [ ] 按五维标准逐一评分
- [ ] 第一层和第二层都有具体的证据支撑
- [ ] 给出P0/P1/P2优先级排序
- [ ] 参数溯源表完整
- [ ] 最终评分在0-100之间
- [ ] HTML格式正确，可在浏览器打开
- [ ] 所有[X]都已填入具体数值

---

## 📞 常见问题

**Q：如果AI生成的HTML打不开怎么办？**
A：检查HTML是否完整（应以 `<!DOCTYPE html>` 开头，`</html>` 结尾），复制整个代码块。

**Q：评分不一样怎么办？**
A：可以多次发送论文给不同AI，取平均分以获得更可靠的结果。

**Q：论文太长怎么办？**
A：可以分章节提交，先做单独评分，再综合计算总体评分。

---

## 🎯 最后提醒

- 本指南是参考，AI的判断也会受其理解能力影响
- 对于重要决策（录取/拒稿）建议人工复核
- 评分不是身份鉴定，仅反映论文的AI风格特征
- 本方法专针对数学建模竞赛，不适用其他领域

---

**版本：** v2.0 | **最后更新：** 2024年  
**维护人：** BZD数学建模社

