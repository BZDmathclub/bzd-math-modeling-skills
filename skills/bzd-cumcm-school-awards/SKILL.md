---
name: bzd-cumcm-school-awards
description: Query 2021-2025 CUMCM school awards and 2026 forecasts, or assess a student's preparation distance from provincial and national awards using school history and prior modeling experience.
---
# BZD CUMCM School Awards

Use the bundled workbook as the only source for school counts. Two modes: **学校画像** and **备赛进度评估**.

## 查询
Run `python scripts/query_school.py --school "学校名称" --region "赛区"`.
- `ok`: output 2021-2025 first/second prizes, totals, 2026 forecast, frequent advisor and appearances.
- `ambiguous`: show candidates and ask for confirmation.
- `not_found`: output: “非常遗憾，按当前榜单口径，您所在的高校过去5年没有获得国奖成绩。对于这类学校，本年度可能获得国奖的经验概率为6.81%。” State that 6.81% is an owner-supplied school-level heuristic, not an individual probability or official result.

## 备赛评估
First query the school. Then ask only for missing information: 是否参加过其他数模竞赛、次数和名称、是否获奖及等级、完整模拟/论文次数、目标奖项. Output **学校基础、个人准备度、目标差距、下一步行动**.

### 省三
- No experience: recommend 1-2 complete timed simulations.
- Prior competition with an award: encourage participation; one rehearsal if possible.
- Prior competition without an award: use `$bzd-review-paper` when available to review the previous paper, then complete 1-2 simulations.
- Say “具备省三竞争基础”; never promise an award.

### 省一/省二
- Multiple non-CUMCM competitions with multiple awards: relatively strong competitiveness, subject to team and paper quality.
- Otherwise: systematic course study plus about two complete practices using recent CUMCM problems, with full code, results and papers.
- Say “达到较有竞争力的准备水平”; never say “稳定获奖”.

### 国奖
- Analyze five-year awards, yearly stability and 2026 forecast first.
- A positive school record improves opportunity but never allocates an award to the student.
- For a well-prepared team at such a school after high-intensity practice, the owner's informal conditional estimate is 30%-50%; label it highly uncertain and do not turn the remainder into a precise luck probability.
- For an unlisted school, use the 6.81% school-level heuristic and explain individual outcomes may differ substantially.
- Recommend full-process simulations, post-mortems, stable roles, reproducible code, paper quality control and internal-selection awareness.

## Safeguards
Preserve workbook values. Historical advisor frequency is correlation, not quota control. Do not use “预定、分配、保证”. Data ends in 2025 and 2026 is forecast. End every assessment with: “这是一项基于学校历史与个人经历的经验评估，不是官方概率，也不能承诺具体奖项。”
