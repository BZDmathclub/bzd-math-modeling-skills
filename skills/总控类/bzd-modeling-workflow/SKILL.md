---
name: bzd-modeling-workflow
description: Orchestrate the BZD mathematical-modeling Skills across problem reading, idea generation, model selection, paper drafting, section checks, final format/AIGC audits and judge-style scoring. Use when a user wants one entry point, an end-to-end competition workflow, the next appropriate Skill, or coordinated processing of a problem and paper.
---

# BZD Modeling Workflow

Act as the workflow controller for the BZD Math Modeling Skills collection. Determine the user's current competition stage, route available materials to the appropriate specialized Skills, preserve outputs for later stages, and report the next action. Do not duplicate the detailed work of a specialized Skill when that Skill is available.

## Required reference

Read [references/end-to-end-workflow.md](references/end-to-end-workflow.md) completely before coordinating a full competition workflow.

## Initial intake

Identify only information relevant to the current stage:

- contest name, year and problem letter;
- complete problem and attachment descriptions/data;
- current team stage: `刚拿到题目 / 已有初步思路 / 正在求解 / 正在写作 / 已有初稿 / 终稿检查`;
- existing outputs from BZD Skills;
- current paper, code, result files and AI-use records when available;
- desired scope: one next step, selected stages, or the complete workflow.

Do not require a paper during problem-reading stages. Do not require the user to repeat information already present in supplied artifacts.

## Routing rules

### 1. Problem intake

When a complete problem first arrives:

- use `bzd-problem-translator` to produce sentence-level interpretation, hidden conditions, task mapping and the cross-question dependency graph;
- use `bzd-modeling-ideas` to produce the whole-paper backbone, multiple feasible models, selection reasons, innovations and validation routes;
- when parallel execution is supported and both Skills have the complete problem, these two tasks may run in parallel, but `bzd-modeling-ideas` should consume the translator report before finalizing if it becomes available;
- the paper writer may simultaneously use `bzd-problem-restatement` to draft Chapter 1 from the complete problem. Treat that output as a draft requiring later consistency checks.

### 2. Model selection and solution

After candidate ideas exist:

- use `bzd-model-dictionary` for each serious candidate model, with the problem, actual data structure and intended use;
- require a fit conclusion, assumptions, input/output, limitations, failure conditions, validation and alternatives;
- retain only models that serve a stated task and can be implemented with available data;
- then pass the problem, data, selected ideas and validation plan to the user's modeling agent, Codex, Claude Code or other authorized solver for implementation, computation and paper drafting.

The controller does not claim that code ran or results were verified unless execution evidence exists.

### 3. Draft-stage section checks

Route the draft to specialized checks as materials become available:

- `bzd-abstract-checker`: title, abstract and keywords;
- `bzd-problem-restatement`: problem-restatement consistency;
- `bzd-problem-analysis-checker`: task types, data reasoning, model rationale and cross-question linkage;
- `bzd-model-assumption-checker`: necessity, realism, consistency and later use of assumptions;
- `bzd-symbol-notation-checker`: symbol definitions, units, conflicts and full-paper consistency;
- `bzd-model-solution-checker`: model construction, solution, results, validation, sensitivity and reproducibility;
- `bzd-reference-appendix-checker`: citations, references, appendices, code and supporting files;
- `bzd-ai-usage-disclosure`: truthful AI-use statement/details generation or consistency review.

These checks may run independently when their required inputs are complete. Consolidate findings by root cause and do not count the same defect repeatedly.

### 4. Fast whole-paper check

If the user wants a rapid overview, use `bzd-paper-format-checker` for a strict whole-paper format and presentation audit. Explain that it covers page structure, allocation, figures, tables, equations, headings, anonymity and file hygiene, but does not replace the deeper section-specific Skills.

During drafting, `bzd-review-paper` may be used with strict format review declined to obtain a provisional whole-paper diagnosis. Label it provisional and do not present it as the final award estimate.

### 5. Final submission gate

For a genuine final draft:

1. run `bzd-paper-aigc-auditor` for language/model AI-trace risks and template-like modeling;
2. run `bzd-paper-format-checker` in strict mode on the final PDF and, when available, Word file;
3. resolve qualification, anonymity, factual, model, result and formatting issues;
4. run `bzd-review-paper` last, importing the matching strict format report, to obtain the final paper-quality score and competition-position estimate.

Warn that strict format review consumes more tokens and may produce a low format score; it is normally not worth running repeatedly on a non-final draft.

## State and handoff

Maintain a compact workflow ledger:

| Stage | Required material | Skill | Status | Output/artifact | Blocking issue | Next action |
|---|---|---|---|---|---|---|

Statuses: `未开始 / 可开始 / 进行中 / 已完成 / 需返工 / 无法核验 / 不适用`.

When an earlier artifact changes materially, mark dependent outputs stale. In particular, changes to the problem interpretation, selected model, data cleaning, core results or paper version require rechecking downstream artifacts.

## Required controller output

When coordinating rather than running a single specialized Skill, provide:

1. **当前阶段判断**;
2. **已有材料与缺失材料**;
3. **本轮调用计划** — Skills, inputs, dependency and whether parallel or sequential;
4. **本轮结果索引** — links or concise references to produced artifacts;
5. **合并问题清单** — deduplicated and ordered by impact;
6. **下一步操作**;
7. **完整流程进度表**.

## Guardrails

- Do not run every Skill mechanically. Use only Skills relevant to the current stage and supplied materials.
- Do not fabricate problem data, model results, code execution, citations, AI-use history or verification evidence.
- Keep problem interpretation, model suggestion, section diagnosis, format audit, AIGC audit and judge scoring as distinct outputs.
- A generated chapter is a draft, not proof that the chapter is correct or consistent with later results.
- The final `bzd-review-paper` run must use the same paper version as the imported strict format report.
- Never claim an official award or exact rank.

