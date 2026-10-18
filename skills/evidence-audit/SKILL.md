---
name: evidence-audit
description: "Check provenance, freshness, claim support, contradictions and the limits of research before a document or decision is approved. Use when: Summarizing sources, preparing public-facing claims, making decisions or receiving unstructured AI research."
---
# Evidence Audit

**Purpose:** Check provenance, freshness, claim support, contradictions and the limits of research before a document or decision is approved.

## When to use

Summarizing sources, preparing public-facing claims, making decisions or receiving unstructured AI research.

## Inputs

Source register, claims, dates, contradictions, original documents, research scope.

## Method

1. Check source existence, author/issuer, identity, document version, date and allowed use.
2. Tag each item as primary observation, direct quotation, third-party assertion, inference or estimate.
3. Map material claim IDs to evidence IDs and inspect missing, stale or contradictory support.
4. Seek disconfirming sources and check how errors propagate into decisions and outputs.
5. Separate verified, supported, disputed, unknown and rejected conclusions with follow-up actions.

## Outputs

Evidence audit, claim ledger, contradictions, refresh requests, provenance notes and publish blockers.

## Quality gates

- Citation presence is not proof of accuracy.
- Never invent dates, quotes, URLs or study findings.
- Keep private source contents out of public output.
- Label observations, sourced third-party assertions, analysis and recommendations separately.
- If required information is absent, disclose it and propose next checks; never fabricate completion.
- Prefer the shortest defensible workflow appropriate to the stakes.

## Handoff contract

Include engagement ID, objective, references to source IDs and claim IDs, unresolved issues, recommended next action, and approval owner.

## Evaluation

Use `evals/evidence-audit.json` to test relevance, factual discipline and output usefulness against a no-skill baseline.
