---
name: adversarial-review
description: "Independently challenge assumptions, strategy, evidence and decisions rather than validating the author’s preferred answer. Use when: Before material commitments, investor/client delivery, strategic recommendations or release of high-impact artifacts."
---
# Adversarial Review

**Purpose:** Independently challenge assumptions, strategy, evidence and decisions rather than validating the author’s preferred answer.

## When to use

Before material commitments, investor/client delivery, strategic recommendations or release of high-impact artifacts.

## Inputs

Complete underlying claims, sources, draft recommendation, alternatives, success criteria and risk appetite.

## Method

1. Identify strongest assumptions and incentives favoring the preferred answer.
2. Construct credible failure scenarios, counterfactuals and neglected alternatives.
3. Challenge source provenance, base rates, causal logic and costs of being wrong.
4. Separate fatal flaws, important uncertainty and optional improvements.
5. Specify the cheapest independent checks that would reverse or improve the recommendation.

## Outputs

Adversarial review with ranked findings, affected claim/decision IDs, severity, tests and disposition.

## Quality gates

- Reviewer must not silently rewrite evidence.
- Never declare validation on behalf of an unavailable expert.
- No infinite questioning over low-stakes ambiguities.
- Label observations, sourced third-party assertions, analysis and recommendations separately.
- If required information is absent, disclose it and propose next checks; never fabricate completion.
- Prefer the shortest defensible workflow appropriate to the stakes.

## Handoff contract

Include engagement ID, objective, references to source IDs and claim IDs, unresolved issues, recommended next action, and approval owner.

## Evaluation

Use `evals/adversarial-review.json` to test relevance, factual discipline and output usefulness against a no-skill baseline.
