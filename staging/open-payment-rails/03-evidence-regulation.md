# 03. Evidence register, country rules and unresolved claims

**Scope:** Public research observed on 2026-10-30. URLs here are source locations, not warranties of pricing or eligibility. Never describe public API documentation as a contract or a legally cleared integration.

## Sources (source -> claim -> interpretation)

| ID | Issuer and observed assertion | Source | Confidence in published fact |
|---|---|---|---|
| S01 | VietinBank corporate Open API markets real-time credit notifications, VietQR Pay, virtual accounts | https://openapi.vietinbank.vn/ | High, bank vendor statement |
| S02 | SePay lists 50 free monthly transactions and 120,000 VND/month startup tier | https://sepay.vn/bang-gia.html | High, advertised only |
| S03 | SePay describes webhook signatures, 7 retries, monitoring, multi-account support | https://developer.sepay.vn/en/sepay-webhooks | High, product docs not independently tested |
| S04 | SePay details signature verification, timestamp, raw bytes | https://developer.sepay.vn/en/sepay-webhooks/xac-thuc | High, technical docs |
| S05 | payOS direct-to-bank merchant acceptance and no-fee offer by eligibility | https://payos.vn/thu-ho/ | High, current advertisement |
| S06 | payOS unlimited no-fee Kien Long Bank offer launched 2026-01-23 for personal/household business | https://payos.vn/cong-thanh-toan-mien-phi-payos-2026/ | High, explicit eligibility |
| S07 | ApiPay documents 60 free transactions/month, webhooks, bank support and paid quota | https://docs.apipay.vn/en | High, advertised |
| S08 | SCB QR30 creation/callback/inquiry and valid merchant profile | https://developer.scb/assets/documents/documentation/qr-payment/thai-qr.html and https://developer.scb/assets/documents/api-reference-index/qr-payments/post-qrcode-create.html | High, published API design |
| S09 | Omise Thai PromptPay published fee 1.65% per successful transaction, listed pricing subject to VAT | https://www.omise.co/en/pricing/thailand | High, public price not contract |
| S10 | Efí Bank Brazil Pix API dynamic QR receipt 1.19% advertised tariff | https://efibank.digital/tarifas | High, tariff subject to change |
| S11 | Vietnam Decree 52/2024 on non-cash payments, payment-intermediary scope | https://vanban.chinhphu.vn/?classid=0&docid=210262&pageid=27160 | High, official regulation; requires legal interpretation |
| S12 | Banco do Brasil corporate Pix API lists Cob, received funds, refunds, webhooks and business prerequisites | https://www.bb.com.br/site/developers/api-pix/ | High, bank docs |
| S13 | Vietnam Circular 64/2024 on banking Open API, effective 2025-03-01; payment-initiation API access limits | https://chinhphu.vn/?classid=1&docid=212621&pageid=27160 | High, official circular; translation/counsel review required |
| S14 | UOB Singapore corporate banking APIs include bank-to-customer credit notification and PayNow/FAST | https://www.uob.com.sg/business/digital/uob-api-services.page | High, bank docs |
| S15 | PayNet Malaysian merchant onboarding is through registered acquirers; fee varies by acquirer | https://knowledgebase.paynet.my/hc/en-us/articles/50438548943001-Enabling-DuitNow-Products-Services-via-Modernised-API and https://paynet.my/business-solutions/duitnow-qr.html | High, network operator |
| S16 | Bank Indonesia 2026-10-01 QRIS MDR tier changes | https://www.bi.go.id/id/publikasi/ruang-media/cerita-bi/pages/mdr-qris.aspx | High, regulator |
| S17 | BIDV public journey permits sandbox then requires testing and separate go-live request | https://www.bidv.net/bidvorg/service/en/landing-page | High, bank docs |
| S18 | VietQR API describes QR and bank-payment reconciliation services | https://api.vietqr.vn/en | Medium/high, operator self-description |
| S19 | BOT PromptPay transfer fee table, distinct from merchant acquiring | https://www.bot.or.th/en/financial-innovation/digital-finance/digital-payment/promptpay.html | High, regulator |
| S20 | Banco Central do Brasil permits legal-entity Pix send/receive fees | https://www.bcb.gov.br/meubc/faqs/s/pix | High, regulator |
| S21 | ECB explains EU instant-transfer fee parity, not merchant API access rights | https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.em.html | High, central bank |
| S22 | Federal Reserve FedNow serves participating financial institutions and their customers | https://www.frbservices.org/financial-services/fednow/organizations/ | High, operator |
| S23 | UK Open Banking defines VRP authorizations through regulated providers | https://www.openbanking.org.uk/variable-recurring-payments-vrps/ | High, ecosystem body |
| S24 | Hyperswitch Apache-2.0 open-source payments orchestration | https://github.com/juspay/hyperswitch | High, repo README/license, no security audit conducted |
| S25 | VBWD PromptPay plugin claims QR + KBank/SCB webhooks | https://github.com/VBWD-platform/vbwd-plugin-promptpay | Medium, maintainer assertion |
| S26 | Unofficial MBBank gateway claims automated CAPTCHA/session login | https://github.com/tuanminhhole/mbbank-payment-gateway | High that it advertises this, **not** safe/authorized |
| S27 | Bank of Thailand licensing overview for payment services including accepting electronic payments on behalf of others | https://www.bot.or.th/en/our-roles/payment-systems/payment-act-oversight.html | High, regulator |
| S28 | MAS says pure data-only payment service infrastructure may be outside Payment Services Act licensing, depending on scope | https://ask.gov.sg/mas/questions/clx8ktis400btryoze6894qcp | High, regulator, country-specific |
| S29 | Brazilian central bank distinguishes Pix participants, payment initiators, and end-user account providers | https://www.bcb.gov.br/en/financialstability/pixparticipants?modalAberto=pix_regulations | High, regulator |
| S30 | EU Regulation 2024/886 text | https://eur-lex.europa.eu/eli/reg/2024/886/oj | High, law; applicability to project unknown |

## What we can reasonably infer

- [SOURCE] Domestic QR and instant-transfer networks are mature; bank merchant APIs and some webhook paths exist in several countries.
- [SOURCE] Providers advertise actual zero/low fee products. Not all bank/API merchant acceptance is free.
- [INFERENCE] A custom merchant-controlled reconciliation component is technically plausible if bank data access is contractually available.
- [INFERENCE] Portability plus lower total operating effort is a stronger potential product proposition than QR generation.
- [HYPOTHESIS] A noncustodial self-hosted merchant solution avoids payment-service licensing in any particular country.
- [HYPOTHESIS] Buyers will pay enough for deployment/support to offset incident response and engineering.
- [TODO] Validate legal and commercial consequences of account ownership, contractual operator, software host, credentials holder, and who handles funds.

## Regulatory boundary by market

**Vietnam:** Decree 52/2024 regulates payment intermediaries, including electronic payment gateway and collection/payment support services. Circular 64/2024 sets banking Open API rules and limits the prescribed payment-initiation group to banks and payment intermediaries. **Action:** remove third-party payment initiation from MVP. Even merchant self-hosted receive-only reconciliation needs local legal classification because technology packaging and operator's role may matter. Do not claim an exemption.

**Thailand:** BOT oversees designated payment services such as accepting electronic payments on behalf of others. **Action:** merchant owns the bank account; software only ingests authorized transaction information; a licensed provider/bank handles any acquiring. Validate whether a third-party hosted integration differs legally from on-prem software. [S27]

**Brazil:** merchant receipt through a bank account is distinct from participation in Pix's settlement infrastructure and from a payment initiator. Merchant fees may exist. **Action:** treat the bank as Pix participant; use the eligible merchant's approved API, never claim we join Pix. [S12, S20, S29]

**Singapore:** MAS describes a data-only technical service distinction, while merchant acquisition and money transfer may be regulated. **Action:** require case-specific review before offering managed services that go beyond data processing. [S28]

**Malaysia/Indonesia:** merchant acquirer and QRIS participation rules apply regardless of our software license. QR formats do not waive those rules. [S15, S16]

**Europe:** EU instant transfer fee parity is not permission for an unrelated software company to initiate payments or scrape bank feeds. Avoid conflating transfer pricing, API access, privacy, and PSD2 permissions. [S21, S30]

**US/UK:** bank-backed integrations, open-banking permissions and FedNow participant access remain separate from an open-source developer's software capabilities. [S22, S23]

## Data and privacy classification

Likely merchant data: account identifiers, transaction references, payer names where provided, transfer memos, order IDs, amounts/currencies, timestamps, source bank/connector metadata. **Avoid storing customer bank secrets and unnecessary personal information.** Create field-level retention and redaction policy; residency, incident reporting, data protection obligations and customer contracts are country-specific TODOs.

## Claims that must not appear on a site today

- "No bank fees" or "free in all countries."
- "Licensed/compliant globally" or "regulation-free because we never touch money."
- "Production banking integrations in 10 countries."
- "Bank-confirmed" for transaction data observed only through an untrusted intermediary or user screenshot.
- "Guaranteed same-second settlement."
- "50% cheaper" without a measured buyer baseline.
- "Open source" for code we have not written, licensed and published.

## Uncertainty and review log

| ID | Open question | Evidence needed | State |
|---|---|---|---|
| U01 | Which exact merchant accounts qualify for bank callback/inquiry production APIs? | Written bank terms | TODO |
| U02 | Does support software become a regulated electronic gateway or payment intermediary? | Country-specific counsel on actual flow | TODO |
| U03 | How much pain do merchants experience with incumbent webhooks and reconciliation? | Observed buyer operations / customer interviews | TODO |
| U04 | Are existing self-hosted products mature enough to fork or integrate? | Code/license/security review and build | TODO |
| U05 | Does hosted multi-tenant model change legal scope and privacy/residency obligations? | Counsel + bank contracts | TODO |
| U06 | What does 'zero fee' mean by country, merchant type, and transaction band? | Bank tariff statements and merchant contracts | TODO |
| U07 | Which provider gives best customer experience in a controlled production pilot? | Approved pilot and comparative metrics | TODO |
