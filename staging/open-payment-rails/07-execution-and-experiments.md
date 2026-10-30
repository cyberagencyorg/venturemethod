# 07. Execution backlog, acceptance evidence and experiment plan

**Status:** scoped build plan and independent checks. Not a claim that product code exists. **No bank has approved an integration.**

## Priority order: do the work that does not require interview scheduling now

| ID | Scope | Verifiable output | State |
|---|---|---|---|
| E00 | Venture dossier + evidence + risk + scenarios | Reproducible private GitHub documentation and source URLs | **DONE** |
| E01 | Canonical schema and bank capability manifest | Typed JSON schemas for request/credit/event/connection, sample records, versioned spec | **SPECIFIED, IMPLEMENTATION TODO** |
| E02 | Deterministic matching library | Pure function receiving normalized evidence + open requests, returning match/exception, with tests | **SPECIFIED, IMPLEMENTATION TODO** |
| E03 | Bank simulator and fixtures | Fake bank account, signed synthetic callbacks, query endpoint, replay/duplicate/late injection; no money | **TODO** |
| E04 | Transactional allocation and outbox | DB migration enforcing unique bank credit, allocation and downstream event | **TODO** |
| E05 | Merchant API with idempotency | OpenAPI and local API; pending/verified distinction; property tests | **TODO** |
| E06 | Operations UI | Payments, bank health, exceptions, reconciliation, secrets access limits | **TODO** |
| E07 | Direct official bank research | Public interface capability maps and up-to-date source log for Vietnam/Thailand/Brazil | **DONE for docs; production entitlement TODO** |
| E08 | One bank production entitlement | Formal merchant account + approved commercial API credentials + fee/terms sheet | **EXTERNAL TODO** |
| E09 | Customer pain and paid service model | Buyer narratives, existing costs, WTP, integrator partnership indications | **EXTERNAL TODO** |
| E10 | Legal/security owner review | Qualified opinion on exact flow and independent code security review | **EXTERNAL TODO** |
| E11 | Authorized sandbox bank adapter | Real API contract suite with test bank credentials and bank-approved endpoint | **BLOCKED ON E08** |
| E12 | Limited merchant pilot | Controlled cash transactions and measured reconciliation outcomes | **BLOCKED ON E08/E09/E10/E11** |
| E13 | Spinout decision | Recorded owner go/no-go tied to evidence and supportable economics | **NOT APPROVED** |

## Proposed engineering delivery tickets

### P0-01. Schema + package
- Introduce versioned `PaymentRequest`, `BankCredit`, `Allocation`, `BankConnection`, `Event`, `Exception`, `WebhookDelivery`.
- Derive JSON schema and TypeScript definitions, document migration/version compatibility.
- **Accept:** valid fixtures pass; wrong currency, negative amount and missing tenant fields fail validation.

### P0-02. Deterministic matcher
- Enforce exact merchant/account/currency/reference/amount match and bank-evidence grade.
- Dedup by approved bank transaction identity; never match by amount/time alone.
- **Accept:** independent replay of 20+ adversarial fixtures yields no unsupported paid event. Require property-based tests beyond provided fixtures.

### P0-03. Simulated adapter
- Ship mock API that can create a payment instruction, deliver signed callbacks, list credits, and simulate missed callbacks, pagination and retries.
- **Accept:** no secrets, bank names or fake settlement described as real. Sample runner demonstrates one happy path and five failures.

### P0-04. Atomic persistence
- Use transactional DB and outbox; unique constraints on credit identity and allocation.
- **Accept:** concurrent workers cannot double-confirm order or allocate credit twice. Recovery test after injected crash.

### P0-05. Merchant API + public checkout
- Implement scoped authentication, idempotent create, safe query, webhook config, signed outbound event.
- **Accept:** public status response hides payer account details; repeated idempotency key behavior documented; no paid from redirect/QR display.

### P0-06. Exception/reconciliation console
- List unmatched, wrong-account, amount mismatch, ambiguous, late, duplicate and untrusted events with evidence levels.
- **Accept:** operator cannot override without scoped access; all actions audited; manual financial adjustment requires policy.

### P0-07. CI / release proof
- Deterministic tests, schema tests, static checks, secret scanning, dependency/license review, build reproducibility and README warnings.
- **Accept:** exact revision, test commands, outcome/failures and known untested conditions logged in release ledger.

### P0-08. Connector contract
- Write capability matrix, permissions/entitlements and distinct auth/notification/query paths.
- **Accept:** mock adapter implements contract, unsupported methods explicitly error, provider messages cannot inflate trust level.

### P1-01. Direct bank adapter (conditional)
- After approved bank production/sandbox access, implement one bank without copying private docs or secrets into public Git.
- **Accept:** bank integration tested in permitted environment with exact entitlement and costs recorded. Must not infer production capability from sandbox alone.

### P1-02. Second country adapter
- Choose second country based on access and merchant value, not aspiration to list countries.
- **Accept:** same merchant API/status semantics without a new checkout integration; differing bank capabilities are surfaced and tested.

### P1-03. Optional managed hosting
- Only after support margin, legal/residency, tenant isolation and incident process are verified.
- **Accept:** published SLA backed by real operational capability, restore drill, isolation testing and contract.

## Technical verification fixture list

1. Valid exact-match bank-authoritative credit.
2. Same signed event delivered twice and 100 times.
3. Two invoices with same amount, only one exact reference.
4. Two possible exact references due to normalization bug; fail closed.
5. Correct amount/reference but wrong merchant or account.
6. Correct reference and wrong amount.
7. Correct reference/amount and wrong currency.
8. Truncated reference; manual exception.
9. Credit arriving after expiry or cancel.
10. Forged webhook HMAC or timestamp outside replay window.
11. Signed event from authorized delegate but not approved evidence grade.
12. Bank query returns credit already ingested by webhook.
13. Callback after frontend returns "success" but before bank evidence; do not mark paid early.
14. Bank inquiry times out, then recovers after retry.
15. Concurrent workers match same credit/order; only one allocation.
16. Outbound merchant endpoint times out after processing; retries preserve idempotency.
17. Manual override from unauthorized user denied.
18. Partial payment produces exception, not full fulfillment.
19. Refund request and later bank reversal append entries, never erase original.
20. Backup restored then reconciliation replayed without duplicate paid events.

## Discovery TODOs, precisely scoped rather than stopping work

**Bank access (EXTERNAL TODO):** one-page written requests to VietinBank, BIDV, SCB and Brazilian bank operator for exact merchant profile, pricing, sandbox/production requirements, bank account eligibility, signature, callbacks, inquiry, IP restrictions, fee schedule and reseller/hosted conditions.

**Buyer evidence (EXTERNAL TODO):** 10 to 15 genuine past-behavior conversations with operators or software implementers; collect fee invoices, exception frequency, manual reconciliation time, switching history, account types and procurement authority. These numbers are **sampling targets only**. Avoid using interview counts as a license to postpone everything else.

**Pricing and support (EXTERNAL TODO):** quote two prospective implementation packages and support burden. Record proposals and paid commitments separately.

**Legal (EXTERNAL TODO):** exact flow diagram to Vietnam/Thailand counsel, bank contract holder and data operator identified. Seek clear judgment rather than generic 'fintech regulations' review.

## Decision gates

- **Gate A, engineering-only (unblocked):** versioned schema, simulator, matcher, tests and safety documentation built. No real bank or customer is required. This work can proceed now.
- **Gate B, bank sandbox:** authorized test credentials, signed contract restrictions, technical security and reconciliation done. Dependent on bank permissions.
- **Gate C, real merchant:** buyer and bank approval, counsel, operational controls and controlled real-money safety acceptance.
- **Gate D, company/venture:** evidence of repeated paid demand and favorable unit economics; explicit owner decision.

**Stop/pivot:** blocked merchant API, inability to verify bank credit, dominant existing free provider, nonviable support cost, or costlier regulatory requirements. These are decision criteria, not blanket reasons to delay Gate A.
