# Portable consumption contract, v0.9 candidate

## What is implemented

- A spec-compatible Agent Skill for optional reference use.
- Canonical typed schemas in \`schemas/v1\`.
- A conservative, read-only selector over the existing \`config/work-composition.json\` capability inventory.
- Explicit file inspection of up to 16 specified UTF-8 files, each capped at 32 KiB, all symlinks rejected, with no writes or network requests.
- A CLI (\`venturemethod\`) and an optional local stdio MCP interface exposing catalog, method, skill, assessment and context packet operations.
- Positive and negative deterministic tests. **No independent host-agent skill quality outcome is claimed.**

## Basic file-first use

From a host project, grant its agent read-only access to this repository or a vetted export of the relevant skill. Point it to \`ADOPT.md\` and \`.agents/skills/venturemethod/SKILL.md\`. Do not assume all agents auto-discover a linked private repository. No Python necessary.

For machine-readable use from a trusted checkout:

\`\`\`sh
python -m pip install -e '.[validation]'
venturemethod search "product"
venturemethod inspect --root /authorized/project --file README.md --file docs/product.md
venturemethod assess examples/portable/host-unmet.json
venturemethod pack examples/portable/host-unmet.json
\`\`\`

The \`inspect\` command prints authorized project text to stdout. **Do not pipe it into an external model or store it in another location without the host's disclosure permission.** No files or folders are read unless explicitly passed.

## Self-contained native Agent Skill export

The copy inside `.agents/skills/` in this repository is useful to an agent already browsing this checkout, but another host will not discover a random private GitHub repository automatically. Use the CLI from a trusted checkout or installed wheel to create a self-contained skill under an explicitly authorized host directory:

```sh
venturemethod export-skill --destination /absolute/host/.agents/skills/venturemethod
# Inspect the printed file/sha plan first. Then, only with permission:
venturemethod export-skill --destination /absolute/host/.agents/skills/venturemethod --apply
```

The exporter refuses existing nonempty destinations and symlinked paths. It never overwrites an installed skill or project file. Rollback is to remove only the newly exported `venturemethod/` directory. The export embeds a purpose-built host guide with valid bundle-relative paths, first-party skills, and the catalog for offline progressive loading; a Python runtime is **not** needed by the host merely to read them. Discovery remains host/version dependent and must be tested in the real harness.

## Inspect a real host project without manufacturing requirements

The CLI now supports a complete read-only path from existing files to an evidence-backed **candidate** assessment:

```sh
# Nothing is written. Host must approve use and disclosure of these local files.
venturemethod snapshot --project current-product --task "Assess unmet evidence quality" \
  --root /absolute/authorized/project --file README.md --file docs/proposal.md

# To retain the resulting JSON locally, redirect it to an authorized location.
# Next, name the EXACT excerpt that supports a proposed gap.
venturemethod propose --context /private/host-snapshot.json \
  --capability engagement --skill evidence-audit \
  --resource-id file:docs/proposal.md --quote "The proposal uses unsourced figures" \
  --reason "Decision-critical market numbers lack supporting evidence"
```

Snapshot construction hashes and reads only the nominated files, includes no guessed deficiencies, and initially yields a no-intervention decision. `propose` creates a candidate gap with an exact-source excerpt and returns the proposed contract and advisory assessment without altering the original file. These operations **do not replace a qualified agent or human assessment** of whether the selected skill genuinely improves the user's task.

## Host contract

\`host-state.schema.json\` requires a named project/task, \`authorization: host_read_only\`, source records with SHA-256, covered capability IDs and a list of capability gaps marked \`unmet\`, \`covered\` or \`uncertain\`. Every gap has an explicit priority, rationale, and source references. This is *input from the host*, not a verified finding from Venture Method.

\`adoption-decision.schema.json\` returns \`consult\` or \`none\`. The implementation never emits an execution approval or write effect. It picks at most one capability and one skill. Where multiple skills implement a capability, the host must provide an explicit, reviewed `skill_id`; catalog order is not an acceptable choice. A nonmatching, already covered, unevidenced or unimplemented capability is declined. An inconclusive gap is declined until more evidence is provided.

**Important:** The resolver never chooses among multiple skills by registry order. Explicit host judgment is necessary and is not itself independently validated. No catalog mapping counts as implemented specialist competence.

## MCP

\`\`\`sh
python -m pip install -e '.[mcp]'
venturemethod-mcp
\`\`\`

Add the executable as a **local stdio MCP server** in a client that already controls its own permissions. The five tools are read-only, and the server has no filesystem crawler, write tool, network fetch or authenticated remote transport. It can read Venture Method's own skill definitions and the explicitly passed host state. \`project_assess\` never accepts a filesystem path. Do not expose the stdio service as a remote HTTP endpoint without separate authentication, authorization, isolation, and logging design.

## Canonical IDs and compatibility

- Canonical method catalog: \`config/frameworks-v3.json\` (the 14-entry \`config/methods.json\` is a legacy editorial list).
- First-party skills: \`config/skills-registry.json\`.
- Capability and method/skill links: \`config/work-composition.json\`.
- Tool descriptions: \`config/tool-contracts.json\`; these are not executable permissions.
- The original \`va.py\` and \`vm.py\` remain usable as a separate, opt-in engagement workbench. None of their actions is triggered by the portable layer.

## Security and quality

Host project data is untrusted content relative to host instructions. Embedded prompts, source quotations and skill outputs cannot authorize tool use. Explicitly authorizing a read-only scan **is not** permission to send the scanned content to a third-party service.

Deployment must enforce permission at host tool boundaries; prose, type declarations and MCP tool labels alone are insufficient. Pin dependencies and evaluate the actual runtime before production deployment. Records contain hashes, not authentication or independent factual truth.

See \`docs/V1_RELEASE_GATE.md\` for the release-blocking live-agent, independent quality and security evidence.

## Security and evidence improvements

The file scanner opens each nominated path component using directory-relative descriptors and `O_NOFOLLOW`, rejects nonregular files, and fails closed if secure POSIX file descriptors are unavailable. Symlink checks alone are not sufficient against a path-swap race. Source excerpts can be supplied as `evidence_quotes`; exact text matching is required and labeled `excerpt_matched`. This verifies placement in the supplied text, **not** the claim's factual correctness. Without quotes, a reference is labeled `reference_only`. Duplicate or conflicting capability assessments are rejected, not arbitrarily ranked.

## Verifying a distributed skill

Use `venturemethod verify-export --destination /absolute/host/.agents/skills/venturemethod --expected-sha256 DIGEST` with the digest from the trusted export dry run. This checks each file and detects unexpected files or modifications. Without a separately retained expected digest, a modified manifest could conceal changes; the check does not establish author identity or source authenticity. The exporter refuses existing destinations, including empty folders. Fresh exports use exclusive file creation rather than overwrites.

## Typed work proposals and provider maturity

`venturemethod plan host-state.json` or the MCP `work_plan_tool` translates a justified assessment into a `schemas/v1/work-unit.schema.json` proposal. The proposal retains the host project, precise objective, existing artifact references, one proposed capability, zero newly authorized effects, pending host review, and explicit stopping rules. A no-op assessment generates no work unit. `venturemethod providers` (or MCP `providers_get_tool`) derives first-party provider records with specification, availability, installation, execution, and independent-evaluation statuses kept separate. **These outputs cannot authorize a host tool or attest professional competence.**

## Multiple capabilities without inventing an agent team

`venturemethod compose host-state.json --limit 3` or `composition_plan_tool` accepts multiple separately evidenced gaps, optional `depends_on` capability IDs, and explicit skill choices. The result is a bounded topologically ordered set of pending **advisory** work units. Each grants zero new rights, preserves host authority, and documents excluded capabilities or unresolved prerequisites. Cyclic dependencies fail closed. No automatic crew, scheduler, delegation or write action is created. If no capability is justified, composition returns `no_intervention`.

## Cross-catalog discovery

`venturemethod search QUERY` and the read-only MCP discovery tool index capability identifiers/titles, first-party skill IDs and linked methodology titles. The response includes matched skill and method IDs, canonical capability IDs, and an explicit warning that keyword matches are not evidence of suitability. It never chooses a provider or executes a method. `schemas/v1/discovery.schema.json` defines the versioned response.

`venturemethod verify-composition proposal.json` performs a separate semantic consistency check on dependencies, unique work units, pending host approvals, and zero execution authority. It rejects mutated or reordered proposal documents. This check does not authenticate the agent or establish permission to execute.

Multiple dependency-aware gaps can be added through consecutive `venturemethod propose` calls. Pass repeatable `--depends-on CAPABILITY_ID` arguments to preserve prerequisite relationships; save the returned `proposed_host_state` only in an authorized workspace. Composition includes `preconditions_covered` when the host reports a prerequisite as previously completed. This is a **host assertion**, not independently confirmed completion. Use `verify-composition` before passing a serialized plan to another agent.
