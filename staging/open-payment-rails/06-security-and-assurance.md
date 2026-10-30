# 06. Security, correctness and regulatory assurance

**Threat model:** unauthorized payment confirmation, unauthorized banking data access, misallocation, privacy leakage, downstream duplicate fulfillment, integration outages and credential abuse. This is a draft checklist, **not** an audit or certification.

## Security invariants

1. No bank login passwords, CAPTCHA/OTP automation, screen scraping or storage of consumer banking credentials as a prerequisite to operation.
2. Inbound bank events require allowed bank/partner origin, valid signature/mTLS/token as specified by the **actual contract**, timestamp/replay checking, tenant-binding, source-account match and durable recording.
3. API client authorization is separate from bank ingress auth. No shared keys across tenants or endpoints.
4. Never mark paid from a screenshot, return URL, untrusted SMS, time-based assumption or UI click.
5. One bank credit cannot pay two orders; duplicate callbacks and delayed retries are idempotent.
6. Order paid + allocation + outbox creation are atomic; fulfillment delivered at least once with stable idempotency key, and merchant must deduplicate.
7. Correct money amounts require integer minor units, explicit currency and careful currency-specific conventions. No automatic FX.
8. All manual reconciliations are reversible only through logged compensating adjustments, never silent record deletion. High-value/manual override policy is explicit and controlled.
9. Secrets encrypted at rest and in transit, least-privilege per bank integration, rotation/revocation and breach response.
10. Every product claim of a 'verified payment' links to underlying bank evidence level and last reconfirmation time.

## Abuse-case register

| ID | Attack/failure | Impact | Required control | Verification |
|---|---|---|---|---|
| T01 | Forged bank webhook | Deliver goods without payment | HMAC/mTLS/partner-specific auth, source-account binding, bank lookup where possible | Tampered signature rejected, no paid transition |
| T02 | Replay webhook | Double allocation/fulfillment | Bank tx unique constraint, event dedup, outbox idempotency | 100 replays => one credit, one allocation, one business event |
| T03 | Valid signed event wrong account | Cross-merchant misallocation | Bind connection, bank account and merchant; enforce DB tenant filter | 0 cross-tenant allocations |
| T04 | Two pending orders same amount | Unjustified automatic allocation | Unique reference and exact matching; ambiguity queue | Under-specified reference never auto-settles |
| T05 | Transfer wrong amount / currency | Loss or dispute | Exact comparison, exception; currency bound to order | Never paid by near-match |
| T06 | Notification before bank settlement | Premature paid status | Evidence hierarchy, query/statement reconciliation | Unverified/unsigned stays pending |
| T07 | Bank callback lost or delayed | Paid customer not fulfilled | Scheduled authorized inquiry, cursor+watermark, replay | Later bank statement resolves exactly once |
| T08 | Merchant endpoint failing | Webhook lost; order unfulfilled | Durable outbox, bounded retries, DLQ, operator replay | Recovered endpoint receives once logically |
| T09 | Concurrent callbacks | Double paid/order event | DB transaction + uniqueness + compare-and-set | Stress/replay shows single committed allocation |
| T10 | PII in transfer memo | Personal information exposure | Minimal logging, data redaction, retention and audit access | Logs/API do not disclose unnecessary fields |
| T11 | Bank credentials compromised | Unauthorized bank operations | Read-only permissions; secret store, rotation, incident isolation | Least privilege and recovery verified |
| T12 | Refund/charge reversal | Incorrect net revenue | Separate reversal/refund state and evidence | Original paid remains, adjustment appended |
| T13 | Malicious QR substitution | Payer sends to attacker | Verify merchant/bank account identity; QR source pinning | QR content account must match approved bank connection |
| T14 | Integration drift/API version change | Silent incorrect parsing | Adapter contract version, schema validation, canary, fail closed | Unknown fields/statuses rejected or quarantined |
| T15 | Exception-review abuse | Fraudulent manual mark-paid | Role limitations, dual control by threshold, evidence link, immutable audit | Unauthorized reviewer denied |
| T16 | Failed data restore | Incorrect payment history | Encrypted backups, WAL/event recovery, restore drills | Replay yields same allocations and balances |
| T17 | Unauthorized public status lookup | Order/PII enumeration | Opaque public IDs, rate limiting, minimal fields | Cross-order lookups reveal no sensitive data |

## Correctness test matrix

- **Sources:** valid direct bank; valid authorized intermediary with evidence; unsigned third-party notification; forged bank; parser error.
- **Transactions:** exact one-to-one; duplicate; delayed; late after expiry; two plausible orders; no reference; truncated reference; over/underpayment; wrong currency/account; malicious memo; payment already allocated; refund/reversal; adjusted bank timestamps.
- **Concurrency:** same event on two workers; separate events for same payment request; retries during database timeout; outbox worker crash after delivery before acknowledgment.
- **Recovery:** lost webhook then inquiry; intermittent 429; bank unavailable; statement cursor regression; database restoration; API version change; unexpected response.
- **Security:** key rotation overlap; revoked merchant integration; replay timestamp expired; spoofed X-Forwarded-For; cross-tenant row access; log sanitizer; attack against webhook HMAC canonicalization.
- **Quality:** unit, property-based matching tests, bank mock contract tests, local integration test, backup restore, security review and bank-authorized pilot where allowed.

## Acceptance standards by environment

**Offline simulator:** 100% of enumerated security-critical cases pass; zero false paid transitions under tests. This is **not** proof of production accuracy or a statistical guarantee. Use deterministic clock and event fixtures. Store test receipt, exact commit, environment/runtime and fixture hashes.

**Bank sandbox:** use only approved test credentials; verify contract endpoints and idempotency with replay and failure injection. No real payer or merchant data.

**Production pilot:** only after contractual entitlement, local legal review, security review, bank confirmation, documented incident response and restricted amount/volume. Observe real outcomes and unresolved exceptions; do not describe 0 observed failures in a short pilot as certainty of 0 risk.

## Data ownership and privacy

Specify processor/controller relationship by jurisdiction; document cross-border processing and bank contract terms. Minimize payer names, phone/account data; hash or redact where operationally safe; keep merchant-controlled retention/export. Encrypt backups separately from account keys, audit all export access, and provide documented destruction procedure.

## Operational requirements

- Metrics: pending order age, webhook verification failures, bank feed staleness, reconciliation backlog, exceptions per 1,000 credits, pending vs verified discrepancy, 95/99p latency, successful replay and restore time.
- Alarms: malformed signed callback, disabled bank connection, credentials expiring, bank feed delay, unexpected payment surge, override anomaly, outbox DLQ growth.
- Runbooks: callback outage, wrong merchant bank credentials, erroneous allocation, compromised signing key, bank API outage, data breach, bank contract termination.
- SLO and legal liability must be defined before promising a managed service.

## Compliance work explicitly not complete

- [ ] Country-specific qualified legal classification of exact noncustodial, receive-only software flow.
- [ ] Bank contract review, credential use and on-prem/hosted permissions.
- [ ] Required data privacy, retention, residency, consumer rights and transfer controls.
- [ ] External penetration test and independent financial-transaction code audit.
- [ ] Merchant agreement, incident policy, indemnification and refund allocation of responsibilities.

A framework or unit test cannot certify the legal status or safety of a payment product.
