# Architecture and ontological boundaries

## Primary objects

- **Entity:** legal company, organization, individual, product, jurisdiction, market, capability or other explicitly typed real-world referent. Entity resolution must distinguish legal identity and trade name.
- **Engagement:** one bounded mandate with an objective, beneficiaries, permissions, intended decisions, context and data classification. One entity can occur in many engagements. Engagements must never be silently merged.
- **Source:** identifiable evidence location, author/publisher, time, scope, access rights and verification state. A source is not equivalent to truth.
- **Claim:** proposition about the world. Linked sources, support/conflict status, explicit falsification route, currency and confidence. Direct assertion and agent inference should be typed separately in a later schema version.
- **Hypothesis:** testable proposed explanation, with predicted observations, alternatives and outcomes. Not automatically a supported claim.
- **Option:** a candidate action including do-nothing, buy, partner, build, process change or design alternative.
- **Decision:** question, authorized owner, chosen option, supporting and contradicting claims, alternatives, rationale, review condition and reversibility.
- **Artifact:** memo, deck, prototype, financial model, interview guide, strategy map, PRD or specification, generated for a defined audience and decision.
- **Action:** accountable task or experiment linked to a decision, producing an observable result.
- **Outcome:** observed effect and whether the original hypothesis held. This feeds back into the knowledge system.

A company or client is *not* a product, a deliverable is *not* an engagement, a source is *not* an approved claim, and output volume is *not* evidence of impact.

## Separation of concerns

| Plane | What it owns | Should never own |
| --- | --- | --- |
| Domain model | Typed entities and relationships | Third-party claims treated as facts |
| Engagement | Client/project scope, permissions and policy | Global reusable method source |
| Evidence | Provenance, observations, conflicts | Unsourced narrative conclusions |
| Methods | Why/when to use a technique | Execution permissions or secret credentials |
| Skills | Task procedure and outcome contract | Permanent exclusive store of client context |
| Orchestration | Routing, checkpoints, state, authorization | Professional judgment delegated implicitly |
| Adapters | Connected tools and exports | Methodology-specific business truth |
| Evaluation | Baselines, criteria, reproducibility | Self-reported agent success as proof |

## Selection rather than checklist accumulation

The router makes two decisions: **what intellectual work is needed** and **what effort is warranted**. A focused memo may need only source audit and independent critique. Venture incubation may need multiple cycles of customer research, economics, experiments, business architecture and execution planning. This avoids bureaucratic overproduction.

A later version should compute routing from engagement purpose, evidence coverage, downside risk, novelty, irreversibility and required output, while permitting justified human override. Version 0.1 chooses from `kind` and `mode` deterministically, without pretending this is sophisticated AI selection.

## Planned knowledge fabric

A typed graph can represent:

`Entity --participates_in--> Engagement`

`Source --supports/challenges--> Claim --informs--> Option --selected_by--> Decision`

`Decision --authorizes--> Action --produces--> Outcome --updates--> Claim`

`Claim/Decision --included_in--> Artifact`

Canonical data starts as local JSON and Markdown. Graph indexes, embeddings or SQL are **derived projections** to enable retrieval, never a parallel ungoverned source of truth. Version and record relevant changes as explicit events.

## Interfaces to other systems

Downstream adapters should emit a signed/approved task contract to software, creative, CRM, financial or project management runtimes. The receiving tool must return artifacts, evidence and verification results, not merely a completion message.

- Open ASS: accepts scoped engineering spec and acceptance criteria; returns revision, tests, approvals and implementation status.
- Creative Studio: accepts approved strategy, audience, claims, brand profile and distribution brief; returns masters, QA and editorial outcomes.
- GitHub/Linear/Drive: optional issue, document and decision synchronization with explicit write permission.
- Research/finance systems: read-only first, source-level provenance and as-of timestamps.

## Review contract

A structurally valid output is *eligible for review*. It is not proof that facts have been verified, decisions are correct, legal obligations are met or users validated the idea. Consequential recommendations require an independent reviewer and approval owner.
