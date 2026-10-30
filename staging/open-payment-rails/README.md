# Open Payment Rails | venture dossier (temporary holding area)

**Status: v0.2 desk-research and design package, not an approved venture or production payment system.**  
Date: 2026-10-30. Owner / decision authority: Brad Khan.  
Temporary home: private `cyberagencyorg/venturemethod`, isolated on an unmerged research branch. Intended to be moved to a standalone repository.  
Original intake: [Venture Method issue #19](https://github.com/cyberagencyorg/venturemethod/issues/19).

## Executive conclusion

Build a **merchant-controlled, open-source inbound bank-payment reconciliation and acceptance layer**, if the product is eventually justified, **not** a competing payment network and not a new custodian. Existing country networks move money; this product reconciles merchant bank transactions to business orders and publishes verified events.

The attractive point is portability and independent control of bank payment data and operations. Generating QR codes and charging zero gateway commission are easy to imitate, and Vietnam already has capable providers with free offerings. Viable distribution may be an engineering/services wedge into companies with multiple merchant accounts, complex ERP integration and painful reconciliation. It is **not** yet established that buyers will pay for it.

**Current recommendation:** keep development research moving, produce technical specifications and a deterministic sandbox prototype, then test production access and buyer economics. External conversations and bank approvals remain marked TODO. No need to wait for interviews to finish the reproducible desk research, threat model, API contract, mock bank integration or delivery plan.

## What is done

- [x] Read Venture Method selection rules, venture-thesis, product/opportunity discovery, market landscape, business model, evidence audit and adversarial review skills.
- [x] Review market alternatives in Vietnam, Thailand and Brazil, including evidence of **incumbent free/low-cost offers**.
- [x] Inspect public primary regulations and bank API availability in multiple markets, marking unknown access and pricing.
- [x] Develop conditional venture thesis, customer segmentation, build/partner/do-nothing comparison and country screening.
- [x] Draft initial solution architecture, event-state model, core APIs, abuse cases, noncustodial limits, pricing hypotheses and staged delivery backlog.
- [x] Register evidence, counterarguments, open assumptions, invalidation conditions and technical acceptance criteria.
- [x] Stage a synthetic JavaScript matching proof with 27 test cases and draft machine-readable JSON/API contracts. This is not production readiness.
- [ ] Bank approvals or live production merchant credentials. No bank has been contacted or contract signed.
- [ ] Customer interviews, paid pilot LOIs, independent financial audit, certified legal advice and real transaction data.
- [ ] Independently verified implementation or performance benchmarks.
- [ ] Owner approval to form a venture, launch, deploy, market externally or spend money.

## Dossier navigation

1. [01-venture-thesis.md](01-venture-thesis.md): investor-style thesis, alternatives, economics of the moat, adverse cases, decision.
2. [02-market-and-bank-access.md](02-market-and-bank-access.md): current competitors, country scorecard, bank/merchant access constraints.
3. [03-evidence-regulation.md](03-evidence-regulation.md): dated evidence references, regulatory boundaries, confidence and assumptions.
4. [04-economics-and-distribution.md](04-economics-and-distribution.md): business-model options, explicit scenarios and low-cost GTM.
5. [05-product-and-technical-spec.md](05-product-and-technical-spec.md): product boundary, users, requirements, event state, API sketch, reconciliation.
6. [06-security-and-assurance.md](06-security-and-assurance.md): threat model, controls, tests, review prerequisites.
7. [07-execution-and-experiments.md](07-execution-and-experiments.md): build-ready epics, verifiable exit conditions, independent validation TODOs.
8. [specs/contracts.schema.json](specs/contracts.schema.json) and [specs/openapi.json](specs/openapi.json): unimplemented machine-readable contracts.
9. [prototype](prototype/): pure in-memory matcher and synthetic tests.
10. [08-decisions-and-hand-off.md](08-decisions-and-hand-off.md): recorded tradeoffs, approvals, open decisions, transport instructions.

## Framework use and limits

Venture Method consult level, using `ADOPT.md`, `AGENTS.md`, `docs/METHOD_SELECTION.md`, `docs/ARCHITECTURE.md` plus applicable skill documents. Source -> claim -> interpretation -> recommendation -> test is preserved. No CLI engagement, agent test score, human interview or regulatory approval is implied by writing these files. This is a focused working dossier, **not** a modification to the Venture Method framework or an activation of a new venture.

**Vocabulary:** `[SOURCE]` primary or published observation; `[INFERENCE]` interpretation; `[HYPOTHESIS]` untested future assertion; `[DESIGN]` suggested engineering contract; `[TODO]` requires real-world action; `[DECISION PROPOSED]` not approved.
