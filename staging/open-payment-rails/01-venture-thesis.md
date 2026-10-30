# 01. Venture thesis, options and decision

**Decision:** Should Cyber Agency incubate a merchant-owned, open-source inbound bank-payment orchestration/reconciliation product?  
**Scope:** discovery and design, not launch. Date: 2026-10-30. **Decision authority:** Brad Khan.

## Thesis

[HYPOTHESIS] Some merchants and software integrators value **bank portability, reliable cash application, traceability and autonomy** sufficiently to adopt an open-source solution or pay for professional integration. Payment acceptance is a doorway into a wider merchant-owned financial operations layer, but only where a verified bank interface and real buyer need exist.

[OBSERVED] Domestic networks like Thai PromptPay, Brazilian Pix, Vietnamese VietQR and Singapore PayNow already exist. Building the QR encoder does not build the settlement network. The product sits after or alongside merchant bank event acquisition and before business fulfillment. [S01, S03, S04, S08, S12]

[OBSERVED] In Vietnam, SePay advertises 50 free transactions monthly and paid plans, and payOS advertises free unlimited usage for eligible individual/household-business users linked to Kien Long Bank. This **invalidates generic 'free QR payment gateway' differentiation** in that submarket. [S02, S05, S06]

## Precisely whom to serve

- **ICP A, first to study:** Vietnamese operators and integration agencies handling multiple bank accounts, ERP/CRM/invoicing systems, and manual matching or complicated failover. Purchasing entity: business owner, controller, CTO, or software integrator. Their alternative is SePay/payOS or custom integration.
- **ICP B, competitive second hypothesis:** Thai digitally native businesses with bank merchant profiles and meaningful volume facing 1.65% aggregator PromptPay charges. Purchasing entity: online business with development capacity. Alternatives are Omise, direct SCB merchant API, local acquiring partner.
- **ICP C, later:** software companies with multiple domestic footprints needing bank-agnostic event semantics and local custody. Higher scope/longer buying cycle.
- **NOT initial ICP:** casual one-QR merchants, enterprises requiring licensed acquiring, remittance providers, consumers needing wallets, and speculative cross-border arbitrage.

## Jobs, outcomes and evidence grade

| Job | Outcome measure | Evidence status |
|---|---|---|
| Correctly confirm bank payment before releasing order | Unverified-paid events = 0 in test; real-world missed/false confirmations | Functional problem can be defined; actual buyer pain [TODO] |
| Reconcile credits to individual invoices | Auto-match rate with zero ambiguous auto-fulfillment; exception resolution time | Demand [HYPOTHESIS] |
| Replace bank or webhook intermediary without rewriting order logic | Time and code changes to switch adapter | Feasibility can be benchmarked in synthetic sandbox; buying value [TODO] |
| Reduce cost of bank transfers | Total costs inclusive of bank tariffs, engineering, operations and support | Cost structures partly public; merchant baselines [TODO] |
| Retain bank data and audit history under merchant control | Export/replay/restore correctness under merchant ownership | Architectural requirement [DESIGN], demand [TODO] |

## Strategy options, not just build

| Option | Customer result | Strength | Weakness | Disposition |
|---|---|---|---|---|
| **Do nothing / use existing provider** | Merchant consumes SePay/payOS/Omise | Cheapest and fastest for standard needs | Dependency on provider, varies by country | **Default baseline to beat** |
| **Consulting only, direct bank APIs** | Integrator writes bespoke connectors | Immediate services revenue if bank access exists | Repeated engineering, no reusable asset | **Commercial fallback** |
| **Integrate existing open-source orchestrator** | Reuse Hyperswitch or simpler tool with plugins | Avoids reinvention | Different focus; adds complexity/PSP assumptions | **Evaluate selectively** |
| **Open-source receive-only bank reconciliation engine** | Independent, auditable merchant-owned layer | Portable platform potential, explicit noncustody | Cost of technical correctness, support, bank-specific agreements | **Recommended research/build candidate** |
| **Create payments aggregator or network** | Operate settlement/acquiring | Potential service fees | Regulatory/capital/partnership burden, contradicts project premise | **Reject for MVP** |

## Proposed product edge

1. **Bank correctness over QR generation.** Immutable receipt evidence, supported inquiry, deterministic matching, replay and exception handling.
2. **Adapters with machine-readable capabilities.** Per bank disclose \`generate_qr\`, \`verify_received\`, \`list_credits\`, \`virtual_account\`, \`refund\`, \`webhook_signature\` and production entitlement.
3. **Merchant-held boundaries.** Bank account and order record remain customer-controlled, exportable, and portable.
4. **Reliable integrations.** The same downstream event and webhooks work regardless of source, but include provenance and assurance so PSP observations are not falsely described as bank-confirmed.
5. **Deployability.** Open API, Docker or Cloudflare-supported runtime, and reference UI; no requirement to sign up for our service.

These are design aspirations, not evidence of a competitive advantage. Incumbents already have many of these features and bank relationships, especially SePay.

## Risks and adverse cases

- **Critical:** bank API access approved only for certain corporates, regulated intermediaries or approved partners; free, self-hosted software cannot bypass eligibility.
- **Critical:** Vietnamese incumbents are sufficiently cheap that business demand for another provider is negligible. [S02, S05, S06]
- **Critical:** the operating model falls within electronic gateway or payment intermediary licensing despite being described as 'software'. [S11, S13]
- **High:** payment confirmation bugs lead to irreversible fulfillment or lost revenue.
- **High:** conflicting local QR semantics mean 'one connector' abstraction hides critical bank-specific differences.
- **High:** revenues from support fail to cover 24/7 on-call and security engineering.
- **High:** building this diverts time from revenue-producing Cyber Agency projects.
- **Medium:** open-source developers adopt a project without becoming paying customers.
- **Medium:** open-source licenses, local bank contracts and trademarks limit reuse or product naming.

## Best, base and adverse paths, no invented financials

- **Best:** a narrow bank interface is available; integrators suffer real reconciliation cost; the tested core supports two bank adapters with no order integration changes; paid integration repeats and optional hosting is profitable.
- **Base:** a useful reusable library and several bespoke paid engagements emerge, but no independent venture-level economics. Keep it inside Cyber Agency services or open source.
- **Adverse:** API terms block merchant self-hosting, provider fees are negligible, compliance is costly and no buyer will fund maintenance. Retire the venture thesis while retaining the research and harmless QR/reconciliation utility.

## Recommended decision

[DECISION PROPOSED D01] Continue desk research, define exact technical contracts, produce a non-production deterministic simulator and assess alternatives. **Do not mislabel this as a merchant launch.** The interview campaign, bank contracting and legal opinion can remain TODO while work not requiring them proceeds.

A venture spinout should be **separately approved** only after there is evidence of a credible buyer, an authorized production bank path and supportable economics. Not a demand to stop all technical preparation.

**Invalidation triggers:** cheaper mature self-hosted bank product found; API contracts ban this software model; customer data shows negligible exceptions/switching pain; fraud or liability cost outweighs economic savings.
