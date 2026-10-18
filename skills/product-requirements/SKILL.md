---
name: product-requirements
description: "Convert validated intent into testable product requirements that implementation teams can act on without losing context. Use when: Defining a new product, feature, internal system, workflow or external build handoff."
---
# Product Requirements

**Purpose:** Convert validated intent into testable product requirements that implementation teams can act on without losing context.

## When to use

Defining a new product, feature, internal system, workflow or external build handoff.

## Inputs

Approved opportunity, customer segments, constraints, evidence, outcomes, operating context and accessibility needs.

## Method

1. Write problem, user, why, success measure, constraints and explicit exclusions.
2. Map core scenarios, critical path, permissions, data contracts, failure modes and nonfunctional requirements.
3. Separate user outcomes and acceptance criteria from speculative implementation.
4. Trace each requirement to the decision and evidence that motivated it.
5. Set acceptance tests, analytics, rollout, migration and operational ownership before handing to engineering.

## Outputs

PRD or lightweight spec; acceptance matrix; event/metric plan; unresolved decisions and implementation handoff.

## Quality gates

- No untestable adjectives in acceptance criteria.
- Mark customer claims unsupported by evidence.
- Do not conflate PRD approval with implementation verification.
- Label observations, sourced third-party assertions, analysis and recommendations separately.
- If required information is absent, disclose it and propose next checks; never fabricate completion.
- Prefer the shortest defensible workflow appropriate to the stakes.

## Handoff contract

Include engagement ID, objective, references to source IDs and claim IDs, unresolved issues, recommended next action, and approval owner.

## Evaluation

Use `evals/product-requirements.json` to test relevance, factual discipline and output usefulness against a no-skill baseline.
