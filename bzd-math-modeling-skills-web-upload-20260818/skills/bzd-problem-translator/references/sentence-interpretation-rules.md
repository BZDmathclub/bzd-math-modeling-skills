# Sentence Interpretation Rules

## Source-unit classification

Start source-unit classification at the actual problem title. Exclude generic pre-title contest headers, years, format reminders, page headers, watermarks, and submission notices. Preserve any instruction after the problem title when it affects the current problem.

Classify each sentence or independent clause as one or more of:

- `context`: motivation or consequence defining priority/risk;
- `entity`: object, population, agent, component, location, or horizon;
- `definition`: term, threshold, coordinate, event, label, metric, or state;
- `mechanism`: causal, geometric, physical, biological, economic, or operational relation;
- `given`: supplied value, data field, initial condition, parameter, or empirical fact;
- `constraint`: range, feasibility, timing, direction, capacity, information, source, or format restriction;
- `task`: estimate, analyze, explain, classify, predict, optimize, compare, verify, or recommend;
- `objective`: quantity to maximize/minimize or risk/trade-off to manage;
- `validation`: significance, error, sensitivity, reliability, comparison, or rationality request;
- `deliverable`: table, figure, list, spreadsheet, attachment, precision, unit, or decision.

One sentence may serve several roles. Record every role that changes the solution.

## Translation test

A valid translation answers as many of these as the sentence supports:

1. What entity or quantity does it concern?
2. Is it known, unknown, controllable, observed, or latent?
3. What relation, boundary, or action is asserted?
4. Over what population, space, time, condition, and unit?
5. Why does it matter to a later question?
6. What must a later model, algorithm, result, or validation show?

Avoid `介绍了背景` or `要求建模`; they are too vague to prevent omission.

## Link types

- `defines`: establishes later meaning;
- `supplies`: gives later data or parameters;
- `restricts`: narrows feasible models or decisions;
- `motivates`: defines risk, priority, or objective weight;
- `extends`: adds factors, precision, scale, or constraints;
- `reuses`: later question consumes an earlier output;
- `compares`: requires a common baseline or metric;
- `validates`: provides an independent check;
- `overrides`: changes an earlier default.

## Ambiguity handling

For each ambiguity, quote the phrase, list plausible interpretations, identify changing results, select only when context supports it, and otherwise recommend scenario/sensitivity treatment.

## Coverage rules

- Include the actual problem title, substantive notes, table headings, figure captions, attachment-column definitions, and appendices when meaningful.
- Preserve `不考虑`, `仅`, `至多`, `至少`, `必须`, `不得`, and `尽量` with their exact strength.
- Preserve nested quantifiers: per object, period, group, round, or direction.
- Map every number to its entity and unit.
- For `根据上述`, `进一步`, `综合考虑`, or `仍`, identify what carries over and what changes.
