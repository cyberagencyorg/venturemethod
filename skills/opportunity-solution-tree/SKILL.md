---
name: opportunity-solution-tree
description: "Maintain a Teresa Torres style outcome, evidence-backed customer opportunities, solution alternatives and assumption tests. Use for focused ongoing product discovery, not portfolio-wide opportunity origination."
---
# Opportunity Solution Tree

## When to use

Use when a team has a specified customer segment, measurable product outcome and actual customer interviews or equivalent observed behavior. The method is designed for a focused product outcome, not a corporate strategy map or VC pipeline. Source: https://www.producttalk.org/opportunity-solution-trees/

Do not mistake a tree for evidence. Do not invent quotes, interviews, opportunity frequency, customer needs or impact scores. Do not substitute desk research for primary customer observation. A draft generated from customer information still requires review and refinement with practitioners.

## Inputs

Defined outcome, metric, customer segment, actual interview or observational material, traceable claims, research permission, relevant constraints, and people empowered to review findings.

## Method

1. Identify the product or customer outcome, its measurement and intended segment. Check if there are at least 3 to 4 story-based interviews, the starting point recommended by Teresa Torres; if not, organize interviews first and mark all tree work provisional.
2. Independently synthesize individual interviews into key moments, observed needs, pains and desires with source references, then synthesize across interviews. Keep contradictions and minority perspectives.
3. Organize opportunities as a revisable hierarchy. Each new opportunity must point to a claim tied to an actual observational or interview record, not invented AI assertions.
4. Select the target opportunity using relevance to the outcome, evidence quality, underserved magnitude, strategic constraints and explicit tradeoffs. Record what was excluded.
5. Develop multiple materially different solutions to the target opportunity, not one preferred feature disguised as several options.
6. Unpack assumptions for each solution, define thresholds before tests, select informative and proportionate experiments, capture observations and adjust the tree.
7. When new interviews arrive, propose additions, revisions, moves or retirements in a change set. Review each proposal before adopting it. Maintain the history and reconsider downstream decisions.

## Local workbench (v0.4)

```sh
python va.py ost start ENGAGEMENT --outcome "Reduce customer onboarding abandonment" --metric "Completed activations / started activations" --segment "Small business admins"
python va.py source-add ENGAGEMENT --title "Interview 1" --locator "research:interview-1" --kind interview
python va.py claim-add ENGAGEMENT --text "Customer described an onboarding obstacle" --source SRC-0001
python va.py ost propose ENGAGEMENT --kind opportunity --parent OST-ROOT --text "Onboarding obstacle" --claim CLM-0001 --rationale "Observed customer friction"
python va.py ost show ENGAGEMENT
python va.py ost review ENGAGEMENT --proposal OSTP-00002 --decision accept --reviewer "local-operator" --rationale "Provisional local review"
python va.py ost diff ENGAGEMENT --from-event 1
```

Record IDs are returned at runtime; do not assume examples match actual IDs. The CLI validates references and journals proposals, but neither proves interview authenticity nor provides authenticated approvals. An opportunity linked to a claim is **referenced, not fact-verified**.

## Outputs

A working draft tree, interview source map, opportunity hierarchy, contrasting solutions, assumptions and test cards, knowledge gaps, reviewed change sets and a list of decisions that should be reconsidered.

## Quality gates

- No product outcome or real customer evidence: initiate discovery research, do not fabricate a tree.
- Reject proposals without source-grounded opportunity claims.
- Distinguish opportunities from solutions; never phrase a feature request as a customer need by default.
- Every proposed test has an operational measure and prospective criterion.
- Never silently rewrite prior versions; preserve open issues and reviewer decisions.
- Prefer a focused tree per product outcome over a studio-wide supertree.
