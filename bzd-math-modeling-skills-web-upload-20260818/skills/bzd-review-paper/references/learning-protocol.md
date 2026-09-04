# Scoring-Criteria Learning Protocol

Use this protocol whenever the user provides a contest problem together with official or expert scoring criteria. The goal is to learn transferable rubric-construction rules, not merely copy one answer key.

## 1. Pair and identify materials

Treat the problem statement and its scoring criteria as one training case. Record contest, year, division, problem ID/title, source authority, and completeness. Do not merge unpaired or uncertain materials.

## 2. Preserve and normalize

Extract each original scoring item without changing its meaning. Normalize it into:

- source problem task/subquestion;
- category: abstract, formatting, model assumption, model construction, model solution, or problem-specific supplementary quality;
- observable evidence expected from a paper;
- points, partial-credit levels, zero condition, deductions, dependencies, and caps;
- whether the rule is explicit or inferred.

Store both source-preserved and normalized forms in a calibration record.

## 3. Explain the weight allocation

For each scoring item, identify why it receives its weight using only supported features:

- task centrality and prominence in the wording;
- mathematical or computational difficulty;
- workload and number of required outputs;
- dependency on earlier subquestions;
- importance to the final decision/conclusion;
- official emphasis or known judge priority.

Do not learn superficial associations such as “prediction always gets 20 points.” Learn conditional rules such as “a prediction task with required validation and uncertainty receives separate points for construction, solution, and validation.”

## 4. Compare across cases

After multiple cases exist, build patterns only from compatible evidence. Track:

- stable rules repeated across contests/problems;
- contest-specific conventions;
- problem-type patterns such as optimization, prediction, evaluation, mechanism, simulation, or policy design;
- exceptions and contradictions;
- the number and identity of supporting cases.

One case creates a problem-specific precedent, not a universal rule. Promote a derived pattern only after at least two compatible cases; increase confidence as diverse supporting cases accumulate.

## 5. Generate a new-problem rubric

For a new problem without official criteria:

1. Retrieve the closest calibration cases by contest, problem type, task structure, and required outputs.
2. Start from the fixed 10/10/70–75/5–10 framework.
3. Decompose all subquestions and allocate weights using learned conditional patterns.
4. Adapt anchors to the new problem's observable outputs; never copy answer-specific numerical results from another case.
5. Cite which calibration cases influenced each non-obvious choice and state confidence.
6. Run the quality gate in `rubric-construction.md`.

When a historical case uses a different top-level weight framework, preserve its original scoring structure in the record but learn task ratios, dependencies, evidence anchors, caps, and weight rationales. Rebase these into the current user-mandated framework; never add incompatible frameworks together or relabel historical points as if they were originally scored under the current structure.

## 6. Report learning limits

State how many calibration cases were available, their relevance, and where generic judgment filled gaps. Never describe the Skill as “trained” statistically unless an actual evaluated dataset and learning method exist; call this structured rule induction and calibration.
