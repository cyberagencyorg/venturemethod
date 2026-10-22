# Technical inventory

## Platform architecture shown or stated

| Component | Purpose | Status in this meeting | Evidence |
|---|---|---|---|
| Policy Enforcement Point (PEP) | Runs in the execution path, intercepts an agent action, applies a verdict | Existing concept/code; proposed open-source boundary. Interface explicitly needs stabilization before release | 00:04:44–00:06:55; [00:05:30](../media/frames/frame-00-05-30.jpg); [00:06:30](../media/frames/frame-00-06-30.jpg) |
| Policy Decision Point (PDP) | Evaluates policy and returns the verdict; described as AI/VSS scoring and verdict logic | Proposed proprietary decision plane | 00:05:21–00:05:40; [00:05:30](../media/frames/frame-00-05-30.jpg) |
| Policy Administration Point (PAP) | Authors/manages policies, control-plane settings and fleet risk budgets | Proposed proprietary control plane | [00:05:30](../media/frames/frame-00-05-30.jpg) |
| Policy Information Point (PIP) | Supplies IAM, entitlement, and inventory context needed by decisions | Architecture shown; implementation not demonstrated | [00:05:30](../media/frames/frame-00-05-30.jpg) |
| Verdict and attestation schema | Returns ALLOW, CONSTRAIN, REQUIRE_APPROVAL, BLOCK, or HALT; emits evidence | Proposed open format | 00:04:44–00:05:20; [00:05:00](../media/frames/frame-00-05-00.jpg) |
| Proof Certificate / anchor-and-verify plane | Signed/verifiable record of authorization and actual agent behavior; Merkle anchoring and verification | Central proprietary value boundary; example and packaging shown, not executed live | 00:07:02–00:07:28; 00:41:49–00:42:03; [00:05:00](../media/frames/frame-00-05-00.jpg) |
| Identity/IAM v3 | Agent identities, organizational permissions, human/agent API keys, SSO/SCIM, Keycloak/Okta | Multiple features asserted “live on main” in inventory; no live demo | [00:10:15](../media/frames/frame-00-10-15.jpg) |
| SDK/framework integrations | Python, TypeScript, Temporal, LangChain, LangGraph, DeepAgents, Mastra, OpenRouter, CopilotKit, n8n and others | Inventory assigns mixed status; meeting reports a custom SDK built in a week for one external party | 00:43:33–00:44:28; [00:10:15](../media/frames/frame-00-10-15.jpg) |
| Coding-agent governance / Gate | Hooks into coding-agent tool calls; local fail-closed enforcement; policies; approvals; receipt/proof; possible Claude Code plugin installation | Product mockup and plan shown. Example decision log explicitly “illustrative”; not an end-to-end demo | 00:10:50–00:11:26; 01:24:32–01:27:16; [00:10:45](../media/frames/frame-00-10-45.jpg) |
| Natural-language policy/eval authoring | Create policies/evals using natural language | Reported as newly demonstrated earlier, but not demonstrated in this recording | 00:14:14–00:15:30 |
| Post-session security review | Maps a completed agent session to a security framework and recommends more policies/guardrails | Reported as newly demonstrated earlier, but not demonstrated here | 00:14:28–00:15:30 |
| Billing/licensing | Subscription/Stripe billing, usage metering/entitlements, developer seats, AWS Marketplace | Several items shown as feature-branch/not-on-develop; billing completion is a launch dependency | 00:24:46–00:25:21; [00:10:15](../media/frames/frame-00-10-15.jpg) |

## Integrations, infrastructure, deployment and security

- The AWS offer is positioned as running inside the customer’s AWS environment/VPC so data does not leave it; this is a marketing claim shown in a mockup, not deployment evidence (00:01:25–00:03:14; [frame](../media/frames/frame-00-02-00.jpg)).
- The developer distribution concept depends on coding-agent hooks/plugins and possibly MCP, skills, and user configuration. Claude Code is the clearest proposed first-class surface (00:42:00–00:42:32; [frame](../media/frames/frame-00-42-30.jpg)).
- Enterprise approval routing is proposed through Slack, ServiceNow, and custom PEPs; Team through Slack/GitHub review. SSO/SCIM and configurable/on-prem retention differentiate tiers (00:40:24–00:41:32; [frame](../media/frames/frame-00-40-30.jpg)).
- Open-core release requirements explicitly include secret/history scrubbing, a private vulnerability channel, conformance tests, versioned adapter/verdict/certificate schemas, and fail-closed behavior (00:06:03–00:06:55; [frame](../media/frames/frame-00-06-30.jpg)).
- A second external setup reportedly depended on Cloudflare configuration/ports and remained incomplete (00:44:43–00:45:28). Exact technical blockage is unclear.

## Decisions and competing approaches

1. **Open-core boundary (proposed, pending review):** open the PEP and verdict/attestation format; keep PDP, PAP, identity/risk logic, fleet controls, and verification proprietary (00:04:44–00:08:48). A reviewer named Sam was asked to review licensing and strategy, so this was not final.
2. **Fail closed:** local enforcement should deny or use a locally cached authority snapshot when the decision service is unavailable; never fail open ([00:06:30](../media/frames/frame-00-06-30.jpg)). This strengthens security but creates a reliability/UX requirement not resolved in the meeting.
3. **Local-first developer entry, managed team/enterprise expansion:** free individual enforcement and a proof receipt; paid centralized policies, storage, approvals, identity, retention and fleet management (00:40:24–00:42:32).
4. **Platform versus product:** retain the broad runtime platform, but sell distinct products/sub-brands rather than the entire capability map (00:09:25–00:16:20). OpenBox Gate is the first priority; watermarking/fingerprinting is a possible later product (00:48:01–00:49:35).

## Technical unknowns and constraints

- No code, test, latency measurement, bypass analysis, threat model, production incident history, or live policy decision was shown.
- “87 features / 62 live on main” is an internal status assertion. Feature completeness, integration coverage, and production readiness were not verified ([00:10:15](../media/frames/frame-00-10-15.jpg)).
- The PEP adapter contract and certificate/verdict schemas were not stable enough to release according to the prerelease checklist ([00:06:30](../media/frames/frame-00-06-30.jpg)).
- The desired one-line install, instant proof, and clean audit playback were acceptance ideas, not demonstrated release criteria (01:24:32–01:27:16).
- Billing was incomplete and explicitly gated monetization (00:24:46–00:25:21).
- The team acknowledged that a specific dev-house problem could be addressed by existing capabilities but required additional solution work (00:36:49–00:39:09).

