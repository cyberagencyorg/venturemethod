---
name: problem-mapping
description: "Locate structural causes, stakeholders, constraints, bottlenecks, dependencies and actual outcomes before prescribing a solution. Use when: A problem is vague, repeated, cross-functional, political, technical or symptomatic of deeper causes."
---
# Problem Mapping

**Purpose:** Locate structural causes, stakeholders, constraints, bottlenecks, dependencies and actual outcomes before prescribing a solution.

## When to use

A problem is vague, repeated, cross-functional, political, technical or symptomatic of deeper causes.

## Inputs

Observed symptoms, workflows, affected actors, outcome measures, event chronology, systems and process records.

## Method

1. Separate observations from inferred root causes and stated preferences.
2. Construct causal hypotheses with disconfirming observations and feedback loops.
3. Identify incentive mismatches, permissions, handoff failures, hidden constraints and current workarounds.
4. Find intervention points, anticipated second-order effects and the cheapest falsification tests.
5. Prepare at least one viable non-software alternative.

## Outputs

Problem map with causal hypotheses, system boundary, affected stakeholders, candidate interventions and validation plan.

## Quality gates

- Correlation alone cannot establish causation.
- Avoid solution selection without a falsifiable problem statement.
- Include organizational rather than purely technical factors when relevant.
- Label observations, sourced third-party assertions, analysis and recommendations separately.
- If required information is absent, disclose it and propose next checks; never fabricate completion.
- Prefer the shortest defensible workflow appropriate to the stakes.

## Handoff contract

Include engagement ID, objective, references to source IDs and claim IDs, unresolved issues, recommended next action, and approval owner.

## Evaluation

Use `evals/problem-mapping.json` to test relevance, factual discipline and output usefulness against a no-skill baseline.
