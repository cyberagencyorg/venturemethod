# Opportunity Solution Tree implementation and fidelity

Canonical reference: Teresa Torres, https://www.producttalk.org/opportunity-solution-trees/ (viewed October 2026). Further reference: https://www.producttalk.org/behind-the-scenes-ai-osts/ (May 2026).

## Fidelity comparison

| Method element | Present v0.4 | Gap |
| --- | --- | --- |
| One measurable outcome and target customer segment | Yes, on starting OST | Outcome value is an operator input; no independent metric validation |
| Observed customer opportunities | Local claim references must point to an observational/interview source type | Does not inspect interview content or independently verify observations; enforces no minimum interview count |
| Hierarchical opportunity space | Nested opportunity nodes | Cannot auto-synthesize interviews or merge branches semantically |
| Multiple candidate solutions | Supports solution nodes for each opportunity | No cardinality or material-difference check |
| Assumption tests | Dedicated test nodes require measure and prospective threshold | No actual study execution, sampling, results analysis or linked experiment record |
| Continuous evolution | Proposal/review events, add, revise, move, retire, historical event comparison | Reviewers are not authenticated, no semantic merge, no downstream PRD/roadmap updates |
| Collaboration | Self-asserted review label | No permissions, concurrency controls or realtime editing |
| Visualization | Structured JSON returned by CLI | No graphical interactive tree |

## Non-negotiable semantic distinctions

- Outcome: a desired result with its measurement, not a solution metric.
- Opportunity: observed customer need, pain or desire, not a requested feature or internal strategy option.
- Solution: possible intervention designed to address a targeted opportunity.
- Assumption test: an evidence-gathering experiment with decision criteria established before observations.
- OST: a customer/product discovery instrument, not a global venture origination database, investment committee process or all-company knowledge graph.

## Event model

`start -> propose(add/revise/move/retire) -> review(accept/reject)`.

Accepted proposals change only the materialized view produced by replaying the journal. Individual events remain unchanged. Diff compares materialized views at two journal positions. Hash linking is an accident/tamper detection measure without external anchoring. A malicious writer who can rewrite the entire log can forge the history.

The same engagement stores the evidence claims separately in the existing evidence ledger. These are references, not independent corroboration. No approved opportunity automatically changes a decision, a PRD or an investor deck.

## Example sequence

```bash
python va.py new 'Demo Retail Product' --type product
python va.py ost start demo-retail-product --outcome 'Improve repeat purchase behavior' --metric '30-day repeat customer rate' --segment 'Independent retail owners'
python va.py source-add demo-retail-product --title 'Customer interview A' --locator 'research:interview-a' --kind interview
python va.py claim-add demo-retail-product --text 'A customer reported delayed order reconciliation' --source SRC-0001
python va.py ost propose demo-retail-product --kind opportunity --parent OST-ROOT --text 'Reconcile sales reliably without manual rework' --claim CLM-0001 --rationale 'Interview-derived opportunity'
python va.py ost show demo-retail-product
```

Run `ost review` only after inspecting the actual proposal ID. The tree stays a draft and the CLI labels reviews as locally self-asserted.
