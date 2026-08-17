# Mathematical Modeling Paper Formatting Standard

Apply this standard in three stages: eligibility gate, 10-point formatting deductions, then overall presentation multiplier. Keep mandatory contest rules separate from recommended house style.

## 1. Eligibility gate: no score if failed

Check these items before scoring. If a supplied artifact clearly violates any applicable item, report `不具备获奖资格（格式硬性规则未通过）`, list the evidence, and do not calculate a numeric score or percentile.

1. Use white A4 paper with margins of at least 2.5 cm on all sides and left binding; single- or double-sided printing is allowed.
2. Page 1 is the commitment form and page 2 is the numbering-only page in the required contest form.
3. Page 3 is the abstract-only page. Title, abstract and keywords fit on one page. Pagination starts on this page at Arabic `1`, centered in the footer, and continues consecutively.
4. Body starts on page 4, contains no table of contents, should normally remain within 30 pages, and is followed by printed/bound appendices.
5. Abstract page, body and appendices contain no participant, school or competition-region identity information.
6. Every borrowed/public source, including online material, is listed in references and marked at the point of use.
7. Do not impose a font, size, line spacing or color as a contest eligibility rule when the contest does not prescribe it.

Only fail an item when the artifact proves the violation. Mark physical-paper properties, binding, unseen commitment/numbering pages or other unavailable evidence as `待人工核验`, not failed. When the user's contest differs, apply its supplied mandatory rules instead.

## 2. Formatting score: 10 points with itemized deductions

Start at 10. Deduct 1-3 points for each distinct error occurrence or repeated error class, capped at 10 total deduction; the formatting score cannot be below 0.

After calculating the ordinary formatting result, apply the universal criterion ceiling: `formatting earned = min(ordinary formatting result, 9.0)`. Label any ceiling-only difference as `评委满分保留（该项90%封顶）`; do not list it as a formatting error.

- **1 point (minor):** isolated inconsistency that does not impede reading, such as one caption alignment issue, occasional spacing mismatch, or a small numbering defect.
- **2 points (moderate):** repeated inconsistency, missing structural element, unclear unit/notation, broken cross-reference, weak citation form, or a defect that slows review.
- **3 points (major):** pervasive inconsistency, seriously unreadable visual/equation/table, missing required substantive appendix material, untraceable citation practice not already triggering the gate, or a structural defect that materially obstructs judging.

Group identical repeated defects into an error class unless their separate occurrences have independent impact. Do not deduct the same defect under abstract, formatting and model quality. Show an itemized ledger and the capped total.

## 3. Overall presentation multiplier

Formatting defects can affect holistic judging beyond the 10-point category. After computing the raw 100-point score, apply exactly one multiplier based on the whole artifact:

| Multiplier | Condition |
|---:|---|
| 1.00 | Clean or only 1-2 isolated minor errors; coherent professional reading experience |
| 0.95 | Several minor errors or one repeated moderate error class; noticeable but not disruptive |
| 0.90 | Errors occur across multiple sections or several moderate classes; consistency and reading flow are clearly weakened |
| 0.80 | Numerous repeated errors, one or more major classes, or figures/tables/equations/references repeatedly obstruct review |
| 0.70 | Pervasive major formatting and structural problems; important content is often hard to locate, read or cross-check |
| 0.60 | Severe document-wide disorder; many visuals/equations/references are unusable or the appendix/body relationship is difficult to verify |
| 0.50 | Extreme but still technically judgeable presentation failure; understanding and verification require exceptional reviewer effort |

Use `Final score = Raw score x presentation multiplier`, rounded to one decimal. Never reduce below 0 or above 100. Explain the chosen band with error counts/classes and concrete page-level evidence. Use the lowest applicable band when defects satisfy multiple bands. Do not interpolate arbitrary values between bands. Do not apply a multiplier below 1.00 merely because the paper uses a coherent house style different from the recommendations below. A paper that fails the eligibility gate receives no multiplier or score; `0.50` is reserved for a paper that remains eligible and technically reviewable.

## 4. Recommended house style, not mandatory

Use these as consistency references only:

- Chinese body: 小四号宋体; English body: 12 pt-equivalent Times New Roman; single spacing; first-line indent two Chinese characters; zero paragraph spacing.
- Chinese title: 三号黑体, centered. Abstract heading: 四号黑体, centered. Keywords: 小四号黑体 label.
- Level 1 heading: 四号黑体, centered. Level 2: 小四号黑体, left. Level 3: 小四号宋体, left.
- Keep typography, spacing and color internally consistent. A different coherent design earns no deduction.

## 5. Section-specific review checks

### Title, abstract and keywords

Use `title-abstract-keywords.md` for content scoring. Abstract normally uses prose rather than tables, charts or formulas. Keywords normally number 3-5 and represent the problem, model and algorithm. Avoid double deduction.

### Problem restatement

- Cover background, required tasks and relevant existing approaches where useful.
- Rewrite in the team's own words; do not copy the complete prompt.
- Avoid reproducing prompt figures, tables and attachments unless essential.

### Problem analysis

- Explain what must be done, the objective/principle and proposed route for each question.
- Analyze data/attachments and preprocessing where relevant.
- Establish modeling direction but do not reveal final results here; results belong in the abstract/results sections.

### Assumptions

- Include only prompt-given, prompt-derived or model-necessary assumptions.
- Keep them plausible, relevant and neatly listed; usually 4-8 is sufficient.
- Do not assume the model or chosen evaluation indicator is correct.

### Symbols

- Give symbol, meaning and unit in a compact consistent list/table, normally no more than about half a page.
- Do not list one-use symbols; remind readers when a symbol reappears after a long gap.
- Prefer conventional notation and avoid overloaded symbols.

### Tables, figures and formulas

- Prefer three-line tables. Put table number/title above, centered; put figure number/title below, centered.
- Number consistently either globally (`表1`, `图1`) or by section (`表1-1`, `图1.1`). Refer to every substantive table/figure in the text.
- Use readable text smaller/lighter than body where appropriate. State units as `quantity/unit symbol` or equivalent.
- Number formulas consistently when referenced. Accept MathType or native Word equations; judge rendering, consistency and editability rather than software choice.

### Model evaluation

- State real strengths, limitations, sensitivity/robustness, improvements and possible extensions.
- Do not manufacture innovation. A limitation can motivate but need not equal the only improvement.

### References

- Start references on a new page. Require in-text citation markers and a consistent complete bibliographic form.
- Use at least five references as a recommended benchmark, not an automatic eligibility rule unless the contest states it.
- Check books, journal articles and web resources for author/title/source/year or access date as applicable.

### Appendices

- Start appendices on a new page.
- Include all source code/commands actually needed to reproduce results, including Excel/SPSS interactions where applicable, and independently sourced data. Do not duplicate contest-provided data.
- If no program was used, explicitly state so. Missing, non-runnable or body-inconsistent code is a major error and may affect reproducibility/model-solution scoring in addition to formatting only when those are distinct impacts.

## 6. Required formatting output

Report:

1. eligibility gate table: item, status (`pass`, `fail`, `待人工核验`), evidence;
2. itemized 1-3 point deduction ledger;
3. formatting score `max(0, 10 - capped deductions)`;
4. presentation multiplier and justification;
5. raw total and adjusted final total, unless gate failed.
