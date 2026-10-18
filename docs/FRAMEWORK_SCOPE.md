# Framework scope and organizing model

This document states what Venture Method is responsible for. It is intended to prevent the framework from gradually becoming a collection of disconnected prompts, a copy of an existing PM methodology, or an unfinished substitute for every business application.

## Purpose

Venture Method helps a practitioner take on unfamiliar or complex work across disciplines, establish an adequate understanding of the situation, choose and apply suitable methods, coordinate specialist work, produce useful outputs, and retain the knowledge and decisions as circumstances change.

It must work for a small bounded task as well as an extended venture, client, or executive engagement. The practitioner owns the mandate and consequential decisions. Agent support is optional.

## Organizing concepts

| Concept | What it means | Example |
| --- | --- | --- |
| **Mandate** | Why the work exists, for whom, with which constraints | Assess a business for expansion; improve product retention |
| **Engagement** | The scoped body of ongoing work, people, permissions and context | A fractional CPO assignment |
| **Capability** | The type of expertise or work required | Market research; sales operations; finance |
| **Framework** | A representation or lens that structures a problem | Opportunity Solution Tree; business model canvas |
| **Method** | A procedure for investigating, designing, testing or deciding | Interview synthesis; pricing study; scenario analysis |
| **Skill** | Agent-usable instructions and resources for a bounded task | Analyze interview transcript; produce a competitive brief |
| **Workflow** | Coordination of skills, methods, people, tools and reviews | Customer discovery cycle; quarterly planning |
| **Work product** | A document, model, map, analysis, decision or executable change | Market assessment; forecast; PRD; proposal |
| **Knowledge record** | Versioned facts, claims, assumptions, relationships and outcomes | An interview finding that changes the growth thesis |

These are distinct things. The same method can be supported by different skills or performed manually. A workflow can combine different methods. An engagement may require several capability domains.

## Capability domains

This is a practical coverage map, not a claim that the capabilities have already been implemented. Categories can evolve without rewriting the core data model.

| Domain | Representative work | Execution boundary |
| --- | --- | --- |
| Research and intelligence | Market, company, competitor, customer and institutional research | Research tools and sources |
| Strategy and business design | Competitive strategy, business models, positioning, scenario work | Decisions and plans |
| Venture architecture | Thesis, discovery, feasibility, incubation and validation | Venture-specific workflows |
| Product and experience | Discovery, OSTs, product strategy, prioritization, experiments | Product teams and delivery systems |
| Marketing and growth | Brand, messaging, campaigns, channels, measurement | Creative and marketing tools |
| Sales and revenue | ICP, account research, discovery, offers, pipeline, forecasting | CRM and sales tools |
| Finance and capital | Business cases, operating models, unit economics, funding, allocation | Financial systems and qualified review |
| Operations and organization | Processes, org design, hiring, capacity, service delivery | Operational systems and teams |
| Customer and service | Customer experience, support, retention, service improvements | Service tools |
| Data and technology | Data analysis, systems diagnosis, technical planning and requirements | Specialist analysis and engineering tools |
| Governance, risk and legal | Rights, obligations, compliance questions, controls and diligence | Qualified legal, financial and compliance professionals |
| Geography and institutions | Local markets, jurisdictions, policy, partnerships and country context | Regional specialists and official sources |

No single engagement should load every domain. The system selects the necessary work and explains why. Users may substitute their own methods and domain packs.

## What belongs in the core

1. **Engagement definition and state.** Mandate, scope, stakeholders, permissions, current questions, work history.
2. **Method registry and selection.** Framework definitions, use cases, prerequisites, cautions, supporting procedures and attribution.
3. **Capability contracts.** What a skill or workflow needs, what it returns, what resources and permissions it may use, how it is evaluated.
4. **Work composition.** Plan work across skills, people and external applications; support manual intervention, review and resumption.
5. **Evidence and knowledge lifecycle.** Provenance, hypotheses, claims, decisions, versioning, proposed changes, dependency impacts.
6. **Output and review contracts.** Audience, evidence basis, quality requirements, reproducibility, approvals and actual outcomes.
7. **Evaluation.** Reproducible cases, baselines, content assessments, failure cases, time and cost, observed utility.

The core should not require a specific AI vendor, project manager, database UI, CRM or browser. A functional CLI is enough to begin.

## What belongs outside the core

An entire CRM, accounting system, marketing platform, video editor, IDE, scheduling service, or client portal is a separate product or existing system. Venture Method can use such tools through explicit adapters and record their results.

Dedicated operational skills can live in optional packages. They should not all be embedded in the core or loaded into every agent context. The same holds for specialized knowledge in medicine, law, agriculture, energy, or a particular jurisdiction.

Open ASS handles specialized software delivery. Cyber Agency's creative studio handles specialized creative production. Venture Method should pass accepted task specifications to them, verify results at the engagement boundary and preserve relevant decisions.

## Working with existing skill libraries

Different libraries cover overlapping but distinct territory:

- **Paweł Huryn and Product on Purpose:** structured product management methods, discovery, delivery and quality practices.
- **Anthropic knowledge-work plugins:** role-specific operational workflows and connectors. The current root README lists 11 plugins, spanning productivity, sales, support, product, marketing, legal, finance, data, enterprise search, life sciences research and plugin management. The repository also contains a small-business package with additional operational skills. Catalog totals depend on which packages and versions are counted.
- **BMAD, Spec Kit and Agent Skills:** workflow organization, handoffs, portable skill conventions and engineering constraints.
- **Domain authors and practitioners:** original methods must be understood and attributed, including disagreements and different evidentiary requirements.

Treat external libraries as selectable providers of capabilities, not as a universal method. Before use or redistribution, check the exact version, license, source, permissions, fit and execution behavior. A catalog entry is not an implementation.

## Adaptive work, including operations

A client's request to develop a new offering might require market research, positioning, pricing, sales enablement, marketing launch, account feedback and product iteration. Those activities should share context and outcomes.

That does not mean Venture Method needs to invent its own CRM or run every marketing campaign. It should retain the choices and learning while letting appropriate specialists and systems perform the work.

One-off outputs remain possible. The default expectation for continuing engagements is that work products represent dated views of knowledge, and consequential revisions can be proposed and reviewed.

## Test the architecture against actual work

At minimum, the same framework should support:

1. A solo practitioner researching an unfamiliar company and producing a scoped recommendation.
2. A fractional CPO using customer research to maintain an Opportunity Solution Tree and product decisions.
3. A founder going from business hypothesis to customer tests, unit economics, pricing and launch.
4. A venture studio comparing opportunities in several countries with separated confidential context.
5. An ongoing operational assignment involving sales, marketing and finance, where results update earlier assumptions.
6. A short client request that should be finished without unnecessary process.

Success requires substantive quality, evidence integrity, useful results, adaptation to stakes, low operator effort, and the ability to carry work forward. Counts of methods, files or agent runs do not establish quality.

## Status of the repository

The current offline CLI implements only a small portion of this scope: engagement records, method metadata, draft outputs, basic event history, proposed claim changes, and a working-draft OST. Specialized operational execution, integrated research, live agent runs, empirical skill evaluations, authenticated collaboration, and a professional deliverables system are planned or unverified.

Keep those distinctions explicit in the README, capability status and release notes. The portal and hosted infrastructure have their own future workstreams and should not dominate this framework repository.
