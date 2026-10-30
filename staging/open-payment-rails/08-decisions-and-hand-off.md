# 08. Decision ledger, review status and new-repository handoff

**Status:** provisional founder review record, not an authenticated approval. As-of 2026-10-30.

## Decisions

| ID | Proposition / options | Recommendation and rationale | Status |
|---|---|---|---|
| D01 | Build new payment rail vs software on existing networks | Use existing bank settlement networks; app handles verified inbound payment evidence and reconciliation. | **Proposed** |
| D02 | 'Zero fee gateway' vs merchant-owned operations layer | Center merchant control, bank portability and reliability. Zero gateway commission is a product property, not universal bank tariff promise. | **Proposed** |
| D03 | Vietnam-only vs multi-country from first implementation | Build common data model but demonstrate one bank in one country before broad integrations. Investigate Vietnam and Thailand in parallel. | **Proposed** |
| D04 | Direct payment initiation vs receive-only | **Exclude third-party payment initiation** from MVP until specifically licensed/authorized; no custody. | **Proposed** |
| D05 | Build/partner/buy | Treat incumbent hosted providers as default baseline; use existing open-source components selectively only after license/quality check; no uncritical fork. | **Proposed** |
| D06 | Which first adapter? | Not decided; SCB/Thai QR and VietinBank/BIDV banking APIs are strongest initial public docs, but bank entitlement and demand are missing. | **Open** |
| D07 | Open-source business model | Open core + paid integration/support, optional managed hosting later; no obligatory transaction percentage. | **Proposed** |
| D08 | Cloudflare vs conventional database | Defer final hosting choice until transactional correctness, bank egress/mTLS/IP allowlist and residency are evaluated. | **Open** |
| D09 | Public marketing and brand | Keep temporary descriptive project name. Do not create a public company or trademark claim yet. | **Open** |
| D10 | Do interviews block engineering? | **No.** Complete desk research, API contract, deterministic matcher and mock tests now. Reserve external proof for production launch gate. | **Proposed** |

## Validation ledger

| Type | Evidence | Validated state |
|---|---|---|
| Public bank API design | Published bank and network websites, recorded in source register | **Documentation verified, production access not verified** |
| Competitor existence and public pricing | SePay, payOS, ApiPay, Omise, Efí public pricing/docs | **Publicly advertised, not contract audit** |
| Compliance claims | Official regulatory materials, no qualified opinion | **Legal review TODO** |
| Product behavior | Specifications and tests proposed; no bank-connected code in dossier | **Not implemented** |
| Market demand | No interviewed buyers | **TODO** |
| Sales/business economics | Price and unit models are arithmetic hypotheses | **TODO** |
| Independent adversarial audit | Structured self-challenge only | **TODO** |
| Founder approval | No express approval to spend or launch recorded | **TODO** |

## Errors and distinctions to preserve

1. Original prompt suggested the broad possibility of "zero fee" payment rails. Bank acquisition, network tariffs, licenses and API costs differ by country. We can eliminate our own toll, not bank fees.
2. Vietnam cannot be treated as an empty market; SePay/payOS/ApiPay are already meaningful local alternatives and some services are free.
3. 'Open-source gateway' is not automatically permission to consume commercial bank transaction feeds.
4. Bank receipt status, merchant invoice paid status, card authorization status, refunds and downstream fulfillment are **different events**.
5. Technically clean adapter tests do not establish merchant ROI, legal permission or bank uptime.
6. Investment forecasts require real merchant invoices/operating data, not global payment throughput statistics.

## Handoff to a dedicated repository

Do not relocate or overwrite this Venture Method framework's methods to create the product. When a standalone repo is authorized:

```text
open-payment-rails/
  README.md
  context/           # venture thesis, legal boundary, source register, claim/decision ledger
  docs/              # market, business, product, security, operations
  specs/             # versioned OpenAPI, canonical schema, bank adapter contract
  prototype/         # pure match engine, mock bank, deterministic events
  tests/             # fixtures, contract, security and resilience
  integrations/      # one per permitted bank; never real credentials in git
  evals/             # exact-commit validation and outcome evidence
  .github/           # issues, templates and CI
```

**Migration process:**
1. Copy these files unchanged with explicit source URL, date and original commit SHA.
2. Keep original [intake issue #19](https://github.com/cyberagencyorg/venturemethod/issues/19) as provenance anchor; record the new home in an append-only update.
3. Install minimum test/CI tooling; do not import Venture Method framework source code into the payment application.
4. Reevaluate license before public release; verify rights to any pasted QR library, bank SDK or open-source reference code.
5. Write an `ADRs/` decision for every consequential change to scope/permission/country; source referenced claims and compare against previous baseline.
6. Keep live credentials, bank contracts and customer records **out of public Git**.

## Specific next implementation move

Start the deterministic simulator and matching engine now, while acknowledging the bank-connected pilot remains gated. A new engineering agent can implement P0-01 through P0-04 without interviewing anyone and without exposing real funds. A real merchant bank adapter must wait for permissions but should not postpone capability schemas, security controls, test fixtures and architecture.

**Owner decisions outstanding:** dedicated repo, license, first country, engineering budget, whether to position this within Cyber Agency or independently, and when/if to seek real bank credentials. All remain open; none silently approved.
