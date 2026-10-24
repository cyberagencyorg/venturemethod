# Version 1.0 live adoption and professional quality verification

The portable layer is implemented and tested with Python/Node and official Agent Skills validation. Do not infer real agent competence from these results. This runbook defines the missing independent tests. **No host permission, model invocation, or confidential data transfer is implied.**

## Host setup, two independently configured agents

Use one coding agent (Codex) and one genuinely different native agent runtime (Hermes or equivalent). Record exact agent version, model, context configuration, host permissions, source revision and tool availability. Both runs must use the *same pinned* Venture Method commit. The second harness cannot merely re-run the Python MCP test as a proxy for an independent agent.

Use a new throwaway copy of a real in-flight host project, scrubbed of confidential data or governed by explicit permission. Never operate on its main branch, credentials, CRM or external production systems. No external writes, package installation or cross-account browsing should be available to the test agent unless explicitly part of a separately approved scenario.

From a trusted Venture Method checkout or wheel, explicitly export:

\`\`\`sh
venturemethod export-skill --destination /absolute/throwaway-host/.agents/skills/venturemethod
venturemethod export-skill --destination /absolute/throwaway-host/.agents/skills/venturemethod --apply
\`\`\`

Verify native discovery in each actual harness. If a harness needs registration, document exactly what registration was required and do not call that zero-configuration. Export is reversible by removing only that new directory. Record the exported files' manifest, paths and SHA-256.

## Paired cases

Use \`evals/portable/scenarios.json\` as the four predeclared decision settings, supplying adequate task-specific sanitized host files and a permission manifest. Include in-flight accepted decisions. Before model execution, define observable requirements and disqualifying outcomes. For each case:

- Arm A: same task, model, runtime and permissions **without** Venture Method guidance.
- Arm B: same task, model, runtime and permissions with the pinned Venture Method skill visible.
- Isolate contexts and agent memory between arms. Randomize blinded A/B assignments; do not choose favorable runs after seeing output.
- Repeat across the two distinct host runtimes. Preserve transcripts, actual tool calls, timings, outcome artifacts, environment configuration and failures. Hash each input and output.
- Verify whether the agent discovered the skill without false claims, actually read only what was necessary, identified an evidenced unmet capability (or correct no-op), avoided redundant work, and delivered a useful answer or bounded change.

The fourth case must be a no-intervention task where the correct answer is to preserve accepted work and avoid a framework exercise.

## Review and numerical gate

Use a qualified reviewer who did not produce the runs and cannot see which arm used the skill. Score accuracy, usefulness, method fidelity, traceability, host authority and efficiency (0..4) per case. Record all critical factual/security errors independently of averages. Run \`python -m src.va.portable_eval PATH\` to check review structure and compare paired scores.

Provisional acceptance: +0.5 points average improvement on the predeclared rubric; no case regresses in accuracy or authority; no unauthorized read/write/disclosure; the negative case declines correctly. Reconsider thresholds only before running the experiment, not after seeing outputs.

The validator refuses differently configured models or runtimes inside a case. It also requires evidence of two actual runtime families across cases. It does **not** authenticate the reviewers, verify external process behavior, or grant release approval.

## Release evidence bundle

Publish or privately retain the following only if authorized:

1. Exact repository commit, exported skill manifest, SDK versions, harness/model identifiers, and the actual native discovery route.
2. Four case inputs with hashes, paired baseline/candidate outputs, runtime transcripts and tool permission manifest.
3. Reviewer identity and independence statement, blinded grading, quantitative results, safety/failure review.
4. At least one in-flight host assessment with evidence-linked identified gap, original accepted decisions preserved, and explicit no-intervention case.
5. A release decision by the accountable owner, with residual risks, rollback and unsupported claims explicitly listed.

Until these exist, keep the release candidate below version 1.0, even with green CI.

## Current implementation entry points

File-first consultation does not require Python. For optional machine-readable use, `venturemethod snapshot` generates an authorized host-state draft from exact files; `venturemethod propose` requires a source excerpt and names the capability and skill; `venturemethod plan` produces a typed, non-executable work contract. Use `venturemethod providers` to inspect declared versus actually installed/executed/evaluated states. The local MCP exposes the equivalent work planning and provider registry. These paths are verified in synthetic and CLI fixtures, not yet in independent agent harnesses.

## Multiple professional capabilities

The compose CLI and read-only MCP composition endpoint accept independently evidenced unmet capabilities and explicit depends_on relationships. Both generate an ordered set of pending advisory work units without granting tool rights. Include a multi-domain case in live agent evaluations. Verify that prerequisites are retained, previous accepted work is not duplicated, cycles are rejected, and no automated delegation occurs.
