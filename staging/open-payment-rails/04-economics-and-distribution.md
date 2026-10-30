# 04. Business model, economics and acquisition strategy

**Status:** Structured model, no merchant financials or sales evidence. **As-of:** 2026-10-30.

## Pricing models compared

1. **Open source and professional services:** core downloadable and self-hostable; paid bank connector customization, ERP/ecommerce integration, training, upgrade/support contracts. Best short-term fit with Cyber Agency existing strengths.
2. **Optional managed operations:** charge subscription for hosting, monitoring, SLA, backups, on-call and reconciliation tooling. Must have explicit bank hosting and data processing rights and operational cost recovery.
3. **Enterprise integration agreements:** fixed annual maintenance for approved bank connectors and compatibility guarantees; suitable once bank matrix is maintained.
4. **Transaction percentage:** monetizes payment volume but conflicts with desired independence and may trigger additional obligations. Avoid initial offer.
5. **Community-only:** compatible with open-source ethos but not independently a business without sustainable funding.

**Initial recommendation:** A first, B optional, C later. Selling merchant services remains a hypothesis. Never take custody or collect a provider settlement balance to mimic a free bank.

## Cost comparator

For a merchant with `N` paid invoices in a month, average eligible transaction value `A`, percent provider fee `p`, fixed fee per receipt `f`, bank charges `b`, monthly subscription `s`, monthly integration operations `o`, and exceptions `e` costing `c` each:

- Current cost = `N * (A * p + f + b) + s + o + e * c`.
- Open-source cost = `monthly amortized setup + infrastructure + bank/API tariffs + maintenance + support + exception handling + expected incident loss`.
- Incremental monthly value = avoidable current cost minus open-source cost, adjusted for latency, reconciliation quality and migration risk.
- Net implementation margin = contracted implementation fee minus engineer time, security/legal review, partner charges, hardware/hosting and expected support warranty.
- Managed recurring contribution = subscription receipts minus infrastructure, bank partner fees, ongoing security work, customer support and customer-specific processing labor.

**Never mix customer payment volume with our revenue.** The platform should not book the gross merchant transfers as its own revenue.

## Transparent illustrative cases, NOT projections

These calculations are purely arithmetic, not observed merchant usage or promised savings. Assume direct bank tariffs and integration/support costs are separately added.

| Example | Transactions/month | Avg payment | Published proxy fee | Proxy fees/mo | Caveat |
|---|---:|---:|---:|---:|---|
| Thailand Omise PromptPay-like | 500 | THB 800 | 1.65% | **THB 6,600** | Public advertised Omise rate, before VAT, settlement and direct bank charges. [S09] |
| Thailand Omise PromptPay-like | 3,000 | THB 800 | 1.65% | **THB 39,600** | Savings are not equal to this; bank rates and migration/support can consume advantage. |
| Brazil Efí Pix API-like | 500 | BRL 100 | 1.19% | **BRL 595** | Illustrative using published Efí tariff; bank alternatives may charge too. [S10] |
| Vietnam SePay free entry | 50 | VND 250,000 | Free plan, published cap | **VND 0 subscription at cap** | Not proof all bank charges zero; volumes above cap incur charges. [S02] |
| Vietnam payOS eligible Kien Long | 500 | VND 250,000 | Advertised unlimited free | **VND 0 gateway fee** | Only eligible individual/household businesses under published offer. [S06] |

Break-even direct-bank calculation for Thai illustration: if a merchant has 500 x THB 800 monthly PromptPay transactions and zero change in payment volume, potential provider charge of THB 6,600 is the *maximum naive fee saving before* bank tariffs, development, operating costs, VAT effects, incident risk and changeover. If ongoing direct integration costs exceed that, it is not economical. For 3,000 transactions, the gross comparison rises to THB 39,600, making bank contracting worth testing.

**Important:** Where percentage pricing is shown, obtain the actual provider's agreement; do not compare Omise with unrelated merchant bank product as though transaction quality/coverage/guarantees were identical.

## Explicit variable sensitivity tests (future spreadsheet)

- `N`: 50, 500, 3,000 monthly transactions.
- `p`: 0%, 0.5%, 1.65% incumbent processing as hypothetical cases, not market averages.
- `bank_fee`: 0%, 0.3%, 1% or flat transfer cost as **assumptions** only.
- `integration_effort`: 1, 4, 12 engineer-weeks as scenario variables.
- `support_per_month`: 2, 10, 40 engineer-hours as scenario variables.
- `reconciliation_error_rate`: estimated baseline required; no fabricated probability.
- `acquisition`: channel, response, close rate and paid customer acquisition cost remain unknown.

Worst-case stress: a 1.65%-fee customer pays its bank 1% for API-acquired QR plus a large setup retainer, with frequent reconciliation support. 'Zero platform fee' saves little and creates new liability.

## Route to first revenue

**Service-led approach:** Cyber Agency offers a fixed-scope audit of merchant bank-payment operations, produces a reconciliation architecture and proposes implementation only if a buyer has real inefficiency or integration cost. The open-source library reduces repeat work. Do not invent an offer price without a first documented scope.

Channel hypotheses:
- Existing Cyber Agency relationships and engineering engagements in payment-adjacent businesses.
- Developers/integrators whose software already creates invoices but struggles with bank credit matching.
- Transparent code and realistic how-to examples as inbound developer distribution.
- Targeted local accounting/ERP implementers and WooCommerce agencies as trusted distribution partners.
- Avoid growth dependent on hypothetical app-store virality.

**Buyer objections to preempt in product and delivery:** 'Bank already does this'; 'SePay/payOS are free'; 'who carries liability when the order is marked paid?'; 'does my bank allow it?'; 'who is on-call?'; 'can my financial records be exported?'; 'what happens when callbacks fail?'

## Metrics and traction discipline

Measure **paid engagements, time to first reconciled transfer, merchant bank access secured, percentage of externally verified credits correctly matched, exceptions resolved, recurring support hours, retained margin**. GitHub stars, raw payments observed and public network transaction counts do not prove buyer adoption.

## Decision on financial commitment

No seed forecast, gross-margin target or valuation is supportable without real delivery costs and buyer payments. [TODO] Obtain first contractual bank pricing and real merchant invoice/transfer counts before changing the business model from hypothesis to plan.
