# Host-owned brand identity contracts

## Purpose
A project may have an approved mark, imagery, typography, color tokens, writing rules and a named art-director skill. Venture Method must discover and respect that source of authority rather than recreate it with generic brand-architecture or copywriting procedures.

The host project owns the identity. Venture Method supplies composable methods, not substitute logos, claims or visual decisions.

## Minimum consuming-project contract
1. **Approved identity standard:** an owner-designated source file identifying what is locked, its version and status.
2. **Agent-facing brand skill:** project-specific instructions for preserving visual and verbal identity, especially logo configuration, hierarchy, image treatment and forbidden practices.
3. **Machine-readable tokens:** role-based colors, grid and typography fallbacks, logo usage and access guidance. Keep the original token file immutable.
4. **Asset manifest:** source versus derivative roles, file paths, byte sizes, SHA-256, logo variant, approval, provenance, allowed use, rights and known missing formats.
5. **Persistent marketing context:** positioning, buying alternatives, validated offer claims, voice samples, owner restrictions and rejected copy.
6. **Release gate:** validate file identity and visibly inspect final output in its real destination, including mobile and color modes. Do not substitute source-code readback for rendered review.

Choose project-native filenames. A reasonable example is `brand/standards/`, `brand/assets/source/`, `brand/tokens/`, `brand/asset-manifest.json`, `brand/skills/<name>/SKILL.md` and `AGENTS.md`.

## Precedence
Recent explicit owner approval > documented approved mark/source > approved brand skill/tokens > accepted channel examples > proposed experiments. Marketing heuristics are lower priority than these locked assets and constraints. Some brand material may be working official while commercial copy remains a proposal; do not merge their approval statuses.

## Activation
- `brand-architecture` handles company/entity structure, positioning alignment and channel coherence.
- The **host-specific art-direction/brand skill** controls execution of its identity. Read it before generating or editing branded design work.
- `marketing-context` and `competitive-positioning` ground commercial arguments and buyer alternatives.
- `marketing-copywriting`, `brand-voice-preservation`, `copy-editing` and `human-writing-audit` work under the host brand and writing restrictions.
- `artifact-quality` checks the resulting artifact, including use of exact logo, real imagery, readability and functioning links.

## Prohibitions
Do not regenerate or vectorize a locked logo from a reference photo, improvise a replacement wordmark, append decoration to fill space, claim fake credentials or results, import fonts without redistribution rights, or call a resized raster the source vector master.

Do not alter the host repository, source files or published accounts merely by loading a skill. Respect the user's requested scope and approvals.

## Evidence of completion
A finished brand task should show the actual artifact or verified destination, the original-source provenance, material changes and any genuine limitations. Inspect the image, not only the Markdown that references it. When no browser screenshot is available, clearly distinguish validated asset paths from verified end-user rendering.

## Example implementation
`cyberagencyorg/ca-brand` contains a brand-specific director skill, original working-official standards, immutable C/A logo rasters, machine-readable tokens, source/derivative hashes and a validator. This is a host example, not a Cyber Agency look-and-feel imposed on unrelated projects.
