---
name: bzd-problem-restatement
description: Generate a compliant Chinese mathematical-modeling problem-restatement chapter from a complete problem statement, or review a user's restatement against the original problem. Covers research background, problem review, and research overview; does not perform the separate problem-analysis chapter.
---

# BZD Problem Restatement

Work in one of two modes based on the user's request:

- **生成模式**: the user supplies the original problem and asks to write or translate it into a problem-restatement chapter;
- **自查模式**: the user supplies both the original problem and a drafted problem-restatement chapter and asks for diagnosis or review.

Do not confuse **问题回顾** with the separate **问题分析** chapter. A restatement explains what the problem asks; it does not select models, analyze variable relationships, describe algorithms, or report results.

Read [references/restatement-rules.md](references/restatement-rules.md) before either mode. In review mode also read [references/review-checklist.md](references/review-checklist.md).

## Generation mode

Use the complete problem statement as the factual source. Preserve every material task, number, unit, time range, sample size, constraint, attachment role, and required output form. Reorganize and paraphrase instead of replacing isolated synonyms.

Output:

```markdown
# 1 问题重述

## 1.1 研究背景

【1—3段，与任务直接相关】

## 1.2 问题回顾

根据题目提供的数据、条件和任务要求，需要解决以下问题：

（1）【问题一的独立表述】

（2）【继续覆盖全部问题】

## 1.3 研究综述

【总体研究现状、主要方法方向、适用任务、局限与本文可能切入点】

## 待核对事项

- 【歧义、缺少的附件说明或待核验文献；无则写“无”】
```

### Research-overview evidence

- Never invent authors, papers, journals, years, findings, or URLs.
- When the user provides verified literature, use only those sources unless they authorize additional research.
- When browsing is available and the user requests cited literature, search real primary or authoritative sources and cite them.
- When no verified literature is available, write a method-level overview without fabricated citations and explicitly mark `具体文献需要补充并核验`. Do not make citation-looking placeholders appear real.

The generated chapter should normally fit within 1–2 pages, including a research overview of roughly 500 Chinese characters, unless the competition specifies otherwise.

## Review mode

Compare the draft against the original problem. Do not rewrite the chapter unless the user asks for a revision after diagnosis.

Use this order:

1. **审查结论** — 2–4 sentences on completeness and highest risk;
2. **问题清单** — Markdown table: `等级 | 位置/原文 | 类型 | 说明 | 评阅影响 | 修改建议`;
3. **题意保持核对** — tasks, conditions, numbers, units, constraints, attachments, output forms;
4. **章节边界核对** — whether models, algorithms, analysis, formulas, or results leaked into the restatement;
5. **研究综述核对** — relevance, balance, evidence and fabricated-citation risk;
6. **修改优先级** — the three highest-value actions;
7. **待核对事项** — items that cannot be established from the supplied material.

Use `严重问题 / 重要问题 / 一般问题 / 优化建议`. Every serious or important issue needs a location and concrete evidence. If a level has no issue, do not invent one.

## Shared safeguards

- Do not change the problem merely to reduce textual similarity.
- If the original problem is incomplete or an attachment is missing, retain what is certain and list the gap; do not guess.
- Treat a literature survey as part of the requested restatement format, not as permission to fabricate external facts.
- Use objective third-person academic Chinese.
- If the user says “检查” or “点评”, diagnose first. Provide a revised version only when explicitly requested.

