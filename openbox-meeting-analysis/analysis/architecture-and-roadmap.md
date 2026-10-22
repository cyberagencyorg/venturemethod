# Architecture and roadmap assessment

## Architecture reconstruction

OpenBox's asserted control path is:

`agent/framework → PEP interception → PDP decision using policy + PIP context → verdict/enforcement → evidence/attestation → proprietary anchor/verification`

The PEP lives in agent execution and framework adapters; the PDP is the decision/verdict engine; the PAP manages policy and fleet settings; the PIP supplies IAM, entitlement, inventory and other context ([00:05:30](../media/frames/frame-00-05-30.jpg)). The platform's claimed differentiation is not merely blocking. It joins identity, policy, risk scoring, approvals, replay/audit, cryptographic proof and verification across multiple agent frameworks ([00:05:00](../media/frames/frame-00-05-00.jpg); [00:10:15](../media/frames/frame-00-10-15.jpg)).

This is a credible conceptual architecture for runtime agent governance. It also creates hard systems requirements: deterministic enforcement around nondeterministic agents; low latency; resilient offline/local behavior; policy/version consistency; tamper-resistant evidence; framework-specific semantic coverage; and clear authority when the hosted decision service is unreachable. The visible fail-closed principle acknowledges the last of these but does not show the operating design or performance trade-off ([00:06:30](../media/frames/frame-00-06-30.jpg)).

## Open-core boundary

The proposed split is unusually concrete for an early product discussion:

- **Open:** enforcement core/PEP and verdict-attestation format.
- **Closed:** PDP and AI/VSS scoring, PAP/control plane, identity/risk systems, fleet controls, anchoring and verification service.

The strategic logic is sound on its own terms: customers can inspect the code that enforces policy and the format of the evidence, while OpenBox monetizes central decisions, management and proof verification (00:04:44–00:08:48). The artifact also recognizes fork risk, community burden and premature API freezing (00:06:03–00:06:55).

The key risk is timing. An open PEP becomes an external compatibility promise. The same document says the adapter contract, verdict schema and certificate schema must first be stabilized and proprietary coupling removed ([00:06:30](../media/frames/frame-00-06-30.jpg)). Open-sourcing before the Gate onboarding and decision semantics are proven could lock in the wrong interface; delaying too long weakens the trust/distribution thesis. This is a sequencing decision, not merely a license choice.

## What is demonstrated versus discussed

| Item | Classification | Basis |
|---|---|---|
| Architecture and open-core split | Demonstrated as a detailed internal design | Five-page brief shown at 00:05:00–00:06:30 |
| Feature status map | Asserted | Internal dashboard/map shown at 00:10:15; not tested |
| Gate UX and decisions | Mocked | Landing page and illustrative terminal shown at 00:10:45 and 00:37:00 |
| AWS deployment/purchase page | Mocked/positioned | Landing page shown at 00:02:00; no live marketplace transaction |
| Natural-language policy authoring | Reported as previously demonstrated | 00:14:14–00:15:30; not replayed here |
| Security review/recommendations | Reported as previously demonstrated | 00:14:28–00:15:30; not replayed here |
| Custom SDK in one week | Asserted implementation result | 00:43:33–00:44:14 |
| One-line Gate install | Target experience | 01:24:32–01:27:16; not shown |
| Billing | Incomplete dependency | 00:24:46–00:25:21 |

## Roadmap quality

There are real technical priorities: billing; stable PEP interfaces; policy packs; proof certificate limits/storage; approvals; SSO/SCIM; coding-agent plugin distribution; docs/videos; and completion of two external setups. What is missing is the structure that turns these into a dependable roadmap:

- one accountable product/engineering owner for Gate;
- dependency order between installer, local enforcement, hosted decisioning, identity, proof, UI and billing;
- release-quality metrics such as install success, time to first governed action, false-block rate, bypass resistance, decision latency, offline behavior, proof-verification success and rollback;
- capacity and dates grounded in engineering estimates rather than the desired website/revenue schedule;
- explicit definition of which framework/tool calls are supported at launch and which fail closed;
- threat model and security validation appropriate to a product sold on “security.”

The meeting's one-week launch aspiration (00:29:45–00:30:15) and one-line install promise (01:24:32–01:27:16) can be useful forcing functions, but they are not yet an executable technical plan.

## Recommended release logic implied by the evidence

This is an assessment, not a statement from the meeting. The narrowest evidence-consistent Gate release would require:

1. one supported coding-agent surface and a documented set of tool calls;
2. a stable local PEP/verdict contract with explicit fail-closed and offline semantics;
3. one default policy pack that reliably produces an allow, a block and an approval request;
4. a proof artifact the user can immediately inspect and verify;
5. instrumented install, first action, first proof, weekly reuse and policy/decision errors;
6. billing disabled or clearly separated until activation is proven, then tested with a small Team cohort;
7. no claims of production protection beyond the tested integration boundary.

That sequence matches the participant's late insistence on a single simple use case and visible proof (01:24:32–01:26:53) and the open-core checklist's insistence on contract stability and conformance ([00:06:30](../media/frames/frame-00-06-30.jpg)).

## Architectural strengths

- The PEP/PDP/PAP/PIP separation provides clear boundaries and a plausible open-core seam (00:05:21–00:05:40).
- Evidence/attestation is integrated into the control model rather than added as reporting, which could create durable enterprise value (00:04:44–00:05:20).
- Local enforcement plus enterprise control planes maps coherently to a bottom-up/enterprise expansion motion (00:40:24–00:42:32).
- The release brief anticipates security disclosure, secret scrubbing, conformance, interface versioning and governance, which is more operationally mature than a generic “open source for growth” plan ([00:06:30](../media/frames/frame-00-06-30.jpg)).

## Architectural risks and unknowns

- Framework breadth can become an adapter-maintenance business; semantic gaps may create false confidence.
- Fail-closed is safe in principle but can make coding agents unusable if latency, availability or policy quality is poor.
- Proof Certificates are only differentiating if keys, schemas, anchoring, replay, verification and auditor trust withstand scrutiny; none was tested here.
- An open enforcement layer may be forked, while a closed verification service must still be trusted—the meeting recognizes but does not resolve that tension (00:07:02–00:07:28).
- The feature inventory's breadth may conceal inconsistent maturity; branch presence is not production readiness ([00:10:15](../media/frames/frame-00-10-15.jpg)).
- No evidence was shown about multi-tenancy, data classification, secrets handling at runtime, observability, incident response, compliance certification, model/policy evaluation quality, or deployment upgrades.

