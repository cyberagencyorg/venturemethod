# 05. Product and technical specification

**Type:** discovery-stage specification; no live bank approval. **Owner:** Brad Khan. **Status:** draft, not production certified.  
**Target:** a transparent, permissioned, receive-only account-to-account payment reconciliation engine.

## Product principles and boundaries

- Money moves on the existing bank/network rail. **This application does not settle, store or initiate payer funds.**
- Source-of-truth for a bank credit is the authorized merchant bank interface or a documented, properly authenticated delegate with stated evidence level.
- No QR code, payer screenshot, raw SMS, web browser return URL, or user action can automatically make an order paid.
- All amounts use integer minor units plus explicit ISO 4217 currency; never float.
- A credit can be allocated at most once; retries never duplicate an allocation or emit a second irreversible business action.
- A bank callback is a notification to reconcile, **not** an unconditional payment confirmation. Query and statement reconciliation must converge eventually within documented provider limits.
- All bank-specific features are **capabilities**, not universally promised features; no automatic refund if the bank cannot do one.
- Merchant must be able to run code on its own infrastructure and export complete relevant event history.

## Scope

**P0:** create pending invoice/payment request; generate bank payment instruction/QR when permitted; normalize signed bank credit; independently match to the order; maintain append-only event history; expose safe read/status API; authenticated merchant webhook via durable outbox; bank inquiry reconciliation; exceptions dashboard; role-based access; export; scripted bank simulator.

**P1:** second independent adapter, multiple bank accounts, ERP integration, connector health checks, capability matrix, scoped merchant tenancy, dry-run migration, observability and alerting.

**P2:** optional managed hosting, WooCommerce plugin, multi-country dashboards, automated refund requests **only where contractually and legally permitted**, support/SLA.

**Out of scope:** live customer pay-by-bank initiation; storing bank login passwords; card PAN/PCI payments; crypto wallets; stored value; global acquiring; actual merchant funds; pooled transfers; FX; cross-border remittance; arbitrary scraping; unsupported merchant claims.

## User roles and permissions

- **Merchant owner:** connect authorized bank accounts, approve config, access financial export, invite/revoke operators, approve manual exceptions and view full audit.
- **Finance operator:** view and reconcile bank credit events, approve or reject candidate allocation within limits; no credential export/rotation.
- **Developer/integrator:** manage sandbox keys, webhooks, application config and diagnostics, not receive unrestricted payer identity fields.
- **Read-only auditor:** export/inspect reconciliation history, never trigger fulfillment or approve credits.
- **Platform administrator:** only for an optional managed service with explicit tenancy separation; cannot silently perform merchant-side approvals.

All actions require explicit scoped authorization; failed access and high-impact changes are audited.

## Canonical domain records

| Object | Essential fields | Invariants |
|---|---|---|
| Merchant | \`merchant_id\`, display_name, legal_entity, country, data_policy | All bank connections and payment requests belong to one merchant |
| BankConnection | \`connection_id\`, merchant_id, bank, account_reference, currency, credential_reference, entitlement, capability manifest, verified_at | No raw login password in event rows; explicit permission state |
| PaymentRequest | \`payment_id\`, merchant_id, external_order_id, amount_minor, currency, target_bank_connection_id, unique_reference, \`expires_at\`, \`status\`, created_at | Stable idempotency key; immutable amount/reference after display |
| BankCredit | \`credit_id\`, connection_id, bank_transaction_id, amount_minor, currency, bank_timestamp, received_timestamp, reference, evidence_level, raw_payload_hash | Dedup on bank transaction key scoped to bank/account; signed ingress provenance |
| Allocation | \`allocation_id\`, merchant_id, payment_id, credit_id, allocated_minor, decision_type, reviewer_id, created_at | \`unique(credit_id)\` for full-credit single allocation MVP; cannot auto-allocate ambiguous payments |
| Exception | \`exception_id\`, reason, candidate_ids, assigned_to, evidence_references, resolution, timestamp | No silent dismissal or paid flag |
| Event | \`event_id\`, entity_type/id, event_type, schema_version, actor, correlation_id, created_at, canonical_data_hash | Append only; immutable published history |
| WebhookDelivery | \`delivery_id\`, event_id, endpoint_id, attempt_no, state, next_retry_at, result_code | Retry safely, idempotent event IDs, signed outbound body |
| ReconciliationRun | \`run_id\`, connection_id, requested_window, source_cursor, started/completed, missing_count, duplicate_count, exception_count | Cursor and fetched evidence persisted, not counted as new transfers twice |

No mutable "balance" from ourselves is authoritative; record merchant bank observations and matching decisions, not a parallel custodian ledger.

## Data trust hierarchy

**T1:** direct bank account query, bank statement or securely authenticated bank webhook, with explicit bank transaction ID and account context.  
**T2:** bank-authorized partner event carrying transaction ID and verifiable evidence, with stated rights, provenance and documented trust.  
**T3:** unsigned notification, import, user image, free-form claim.

**Only T1 or explicitly qualified T2 may result in automatic paid status.** T3 starts an unverified exception. Trust is adapter-specific and cannot be elevated merely by labeling an event "confirmed".

## State model

Payment request: \`CREATED -> AWAITING_PAYMENT -> VERIFYING -> PAID\`. A request may also be \`EXPIRED\`, \`CANCELED\` or \`UNDER_REVIEW\`. A late bank credit on expired/canceled request must enter exception review. Refunds are a separate \`RefundRequest\` with a bank-confirmed outcome and never reverse or delete the original PAID event.

**Monotonicity rule:** order fulfillment is triggered once by the first committed \`payment.verified\` transition, never by a raw webhook and never on a downstream HTTP response. Disallow transitions from \`PAID\` back to \`AWAITING_PAYMENT\`. If money later reverses, append compensating evidence with separate status and merchant action.

**Idempotency:** enforce unique \`(merchant_id,external_order_id)\` within agreed namespace, \`(connection_id,bank_transaction_id)\`, allocation key, event key, and outbox event + endpoint key. Retry with same idempotency key and changed request parameters returns a conflict.

## Matching algorithm, deterministic first

1. Normalize bank timestamp, exact account, bank transaction identity, currency, amount_minor and transfer reference. Persist source evidence and authentication verdict; dedup before matching.
2. Filter eligible pending requests **for that merchant and bank connection**, exact currency, exact amount, unique reference. Bank's reference length/casing rules are adapter-specific.
3. **Automatically allocate only if one and only one request has exact approved bank evidence, authorized bank/account, exact reference and exact amount, and no prior credit allocation.** Use a transaction/unique index to commit request paid + allocation + event + outbox record atomically.
4. If evidence is absent, two candidates exist, reference is truncated or amount under/overpays, create an exception. Never fall back to matching by amount/time alone for real financial fulfillment.
5. Bank query/statement reconciliation reads source records and repeats step 1; event processing is replay-safe.
6. For partial payments, multi-credit orders, reversals and fees deducted from receipt, use a **later explicit capability** with validated accounting semantics. No silent shortcuts.

An imported event can be useful for locating a likely credit, but its authority must not exceed its underlying source.

## Proposed HTTP API (subject to architecture review)

\`\`\`http
POST /v1/payment-requests
Idempotency-Key: 3cf8...
Authorization: Bearer <merchant-scoped-api-token>

{
  "external_order_id": "INV-4821",
  "bank_connection_id": "bc_test_123",
  "amount_minor": 890000,
  "currency": "VND",
  "expires_in_seconds": 900,
  "metadata": {"invoice_id": "INV-4821"}
}
\`\`\`

Return \`payment_id\`, \`status=AWAITING_PAYMENT\`, \`payment_reference\`, a payment instruction or authorized bank QR payload, bank capability details, expiry and total fee representation where known. **No claim of a completed transfer.**

\`\`\`http
GET /v1/payment-requests/{id}
GET /v1/bank-connections/{id}/capabilities
GET /v1/bank-credits?from=&to=&cursor=
GET /v1/exceptions?status=open
POST /v1/exceptions/{id}/resolve
POST /v1/webhook-endpoints
POST /v1/bank-ingress/{adapter}
POST /v1/reconciliation-runs
GET /v1/reconciliation-runs/{id}
GET /v1/exports/{id}
\`\`\`

Merchant outbound event payload: \`id\`, \`type=payment.verified\`, \`version=1\`, \`merchant_id\`, \`payment_id\`, \`external_order_id\`, \`amount_minor\`, \`currency\`, \`bank_credit_id\`, \`evidence_level\`, \`occurred_at\`. Signed over timestamp + raw JSON bytes with per-endpoint secret, replay window and key rotation mechanism. Do not expose full bank customer details.

## Bank adapter interface

\`\`\`ts
type AdapterCapabilities = {
  bankId: string;
  country: string;
  currency: string;
  merchantAccountType: "business" | "individual" | "both";
  createQr: boolean;
  verifyIncomingCredit: boolean;
  listCredits: boolean;
  creditWebhook: boolean;
  officialVirtualAccount: boolean;
  refunds: "none" | "manual_only" | "bank_api";
  evidence: "direct_bank" | "authorized_delegate" | "notification_only";
  productionEntitlement: "unverified" | "approved" | "denied";
  apiVersion: string;
};
\`\`\`

Adapter methods: \`validateConfiguration\`, \`getCapabilities\`, \`createPaymentInstruction\`, \`authenticateIncomingEvent\`, \`normalizeCredit\`, \`lookupCredit\`, \`listCredits\`, \`health\`. Optional \`requestRefund\` requires explicit feature approval.

**Fail closed:** unsupported methods return \`UNSUPPORTED\`; unauthorized methods return \`ENTITLEMENT_REQUIRED\`, not empty successful responses. No decorator can convert a screenshot or notification-only adapter into direct-bank evidence.

## UX surfaces

- **Merchant overview:** verified paid totals, pending, overdue, anomalies, bank connectivity, reconciliation freshness; numbers scoped to bank currency, no fake consolidation across currencies.
- **Payments:** sortable order list, amount, bank connection, reference, verification state, source type, audit trail.
- **Exceptions:** explicit reasons, evidence side by side, approved manual allocation/reject, dual-control for high-risk actions.
- **Integrations:** bank entitlements and health, API keys, webhook replay/logs, supported capabilities, fees and access restrictions where known.
- **Audit/export:** reproducible transaction window export with source timestamps, IDs, matching outcomes and gaps.
- **Checkout widget:** simple merchant-branded payment instructions; don't imply our status proves network settlement before verification.

Mobile: readable payment references, copy-and-open-bank-app affordances, explicit pending state, accessible 320px width, no confirmation based on app return.

## Deployment topology hypothesis

**Single-merchant self-hosted** is simplest. Postgres or another transactional database is favored for durable unique constraints and atomic allocation/outbox commit. Cloudflare Workers + D1 + Queues could be explored, but must demonstrate transactions, event delivery, bank API egress/IP allowlisting, certificate/mTLS, data residency and operational observability with the chosen bank. Do not blindly assume a Worker runtime satisfies a corporate bank network contract.

**First executable test:** standalone deterministic bank simulator using signed synthetic events and fake accounts, no real credentials or funds. If production API access is granted, implement **exactly one** adapter with contract tests before generalizing.
