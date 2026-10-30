# 02. Market and bank access: research matrix

**As of:** 2026-10-30. Published fees are snapshots, not negotiated merchant offers. Claim identifiers in [03-evidence-regulation.md](03-evidence-regulation.md).

## Important counterpoint: providers already exist

| Country | Provider / substitute | Public evidence | Interpretation |
|---|---|---|---|
| Vietnam | SePay | Free plan advertised at **50 transactions/month**, startup plan **120,000 VND/month**; documented bank event webhooks, signatures, retry/replay and multi-bank connection. [S02, S03] | Payment verification and bank integration are no longer an untouched opportunity. Independent control and portability must matter. |
| Vietnam | payOS | Advertises direct-to-account checkout. Unlimited no-fee offer launched 2026-01-23 for **eligible individuals and household businesses using Kiên Long Bank**, not all merchants and all banks. [S05, S06] | 'No fee' cannot be differentiator for this segment. Do not generalize beyond eligibility. |
| Vietnam | ApiPay | Advertises 60 free successful payments/month, then paid quotas; APIs, links, bank-webhook monitoring. [S07] | Another serious low-cost alternative; public GitHub repo is not necessarily fully redistributable application software. |
| Thailand | Omise | Published **1.65% PromptPay** fee, subject to 7% VAT on its displayed pricing, plus its settlement/transfer schedule. [S09] | A plausible savings hypothesis, provided direct bank/merchant QR fees and access work. |
| Thailand | SCB direct merchant API | QR30 generation, payment confirmation and inquiry; valid merchant profile and production authorization required. [S08] | Technical building blocks exist but API access is not assumed open to all. |
| Brazil | Efí Bank Pix | Published **1.19%** fee on dynamic Pix QR/API receipts, free allowance for some app use with exceptions. [S10] | Using Pix does not establish cost-free merchant API acceptance. Bank pricing can itself be comparable to PSPs. |
| Brazil | Banco do Brasil | Pix Cob charges, dynamic QR, receipts/refunds, webhooks for BB legal-entity account holders with Pix key. [S12] | Direct bank acceptance path exists for eligible BB corporate merchants. |
| Singapore | UOB corporate APIs | Credit notifications, PayNow/FAST payments and collection-related API services for corporate clients. [S14] | Good reference market; corporate contractual eligibility and pricing remain unverified. |
| Malaysia | DuitNow QR | Merchants affiliate with registered acquirer; fees vary; PayNet's modern API onboards issuers/acquirers, not merchants directly. [S15] | Can't bypass acquiring relationships with a generic QR generator. |
| Indonesia | QRIS | BI effective **2026-10-01:** regular micro transactions <= IDR 500k: 0%; small/medium/large <= IDR 100k: 0%; higher amounts have regulated MDR. [S16] | Local MDR obligations apply regardless of our gateway commission. |

## Bank capabilities vs access

### Vietnam
- **VietinBank:** open API site advertises incoming-balance notifications, VietQR Pay and virtual accounts for corporate systems. [S01]
- **BIDV:** public developer journey allows sandbox registration, then requires integration/testing and production access. [S17]
- **VietQR:** QR generation can be generated client-side; code creation alone **cannot** prove a credit arrived. [S18]
- **SePay:** documentation lists supported accounts; some connections may require internet banking credentials or OAuth, which creates different security/contract considerations. Our product must never rely on unauthorized banking credential scraping. [S03]
- **Important:** Circular 64/2024 restricts some payment-initiation API access to banks / licensed payment intermediaries. Read-only transaction data and individually negotiated corporate APIs need separate entitlement review. [S13]

### Thailand
- **SCB:** merchant requires configured biller/merchant profile; its docs provide QR creation, callback, fallback inquiry, QR void and limited refund paths. [S08]
- **PromptPay user transfer fees** published by BOT refer to user transfers, **not** the fees for commercial bank QR acceptance and partner API service. [S19]
- **Next access test [TODO]:** SCB and KBank quote for a company with a Thai bank account, merchant profile, biller ID, partner onboarding, confirmation/inquiry endpoints, transaction ceilings, settlement and refund policy.

### Brazil
- **Banco do Brasil:** documented Pix merchant APIs require company account, active Pix key, developer portal and permissions. [S12]
- **Efí:** business Pix API may have an explicit 1.19% receiving fee; bank tariff comparisons essential. [S10]
- **Central bank:** receiving fees for legal entities are permitted and varying. [S20]
- **Next access test [TODO]:** one bank's documentation/licensing, real corporate fees, production API scope, device/certificate control, merchant charge correlation and refund support.

### Additional country shortlist
- **Singapore:** UOB company APIs are well-documented; pricing, onboarding and external software hosting terms are open. [S14]
- **Malaysia:** registered merchant acquirer path required. [S15]
- **Indonesia:** QRIS acquirer and regulated MDR required. [S16]
- **Eurozone:** SEPA Instant must not be more expensive than comparable ordinary transfer, but bank statement APIs, merchant reconciliation services and PSP permissions are distinct. [S21]
- **UK:** payer-authorized open-banking payment initiation can require authorized provider involvement; payment status and merchant bank credit records are different primitives. [S23]
- **US:** FedNow participation is bank/eligible financial entity mediated; a SaaS developer cannot join the clearing system just by implementing an API. [S22]

## Feasibility prioritization, with explicit uncertainty

Weights chosen as a **planning heuristic**, not research-backed country scores: bank API feasibility (25%), likely buyer savings (20%), incumbent gap (20%), sales/channel reach (15%), regulatory complexity (10%), repeatable technical scope (10%). Any missing data defaults to neutral/unknown rather than best-case.

| Market | Public API evidence | Buyer's cost edge | Competitive pressure | Regulatory caution | Priority |
|---|---|---|---|---|---|
| Vietnam | High | Low/uncertain (free incumbents) | Very high | High | **Joint first research**, strongest low-cost pilot convenience, weak generic cost edge |
| Thailand | High | Potentially meaningful (Omise 1.65% reference) | Medium/high | High | **Joint first research**, strongest public percentage comparison |
| Brazil | High | Uncertain (Pix bank fee can be 1.19%) | High | High | **Second wave** |
| Singapore | High corporate | Unknown | High | Medium/high | Second wave |
| Malaysia | Network yes, merchant direct no | Unknown | High | Acquirer gate | Later |
| Indonesia | Network yes, MDR regulated | Conditional | High | Acquirer gate | Later |
| EU / UK / US | Network yes, access fragmented | Unknown | High | Complex | Later |

This is **not** a numerically measured ranking. There is insufficient bank-contract or merchant data for defensible weighted scoring. The concrete consequence: select **Vietnam and Thailand as comparative proof markets**, keep Brazil as the independent second architecture, and allow the evidence to change adapter priority.

## Market size: do not confuse payment volume with software demand

TAM = number of reachable merchant integrators/operators with a demonstrated bank reconciliation need x realistic annual price for this **software/service**, not aggregate domestic payment volume. [TODO] Merchant counts, buying authority, baseline annual expense, and likely partner reach must come from sources defining geography, date, and denominator. No unsupported TAM, SAM or SOM values are published.

## Substitutes for 'open source'

- **Hyperswitch:** Apache-2.0 open-source payment orchestration and provider integration; evaluate whether it can host bank-event adapters without excessive code or model mismatch. [S24]
- **BTCPay Server:** noncustodial/self-host deployment pattern, but crypto settlement is a different operating model. Use for self-hosting/invoice design only.
- **Thai PromptPay plugins:** \`VBWD-platform/vbwd-plugin-promptpay\` advertises direct QR and bank webhook matching. Check license, code quality, regulatory eligibility, maintenance and verified integration before adaptation. [S25]
- **Unofficial MBBank scrapers:** projects advertise OTP/CAPTCHA automation and unofficial session-based APIs. **Exclude as production foundations** due to unauthorized-access and credential risks; do not infer safety from a repository's 'production ready' claim. [S26]

## Commercially useful conclusion

The strongest possible buyer is not the smallest merchant wanting to avoid a processor fee. It is the merchant/integrator facing recurring reconciliation problems or provider dependency across accounts, which can be expressed as avoided labor, avoided failure losses, onboarding and migration cost. **This remains a hypothesis until merchant operating evidence exists.**
