# Portable adoption compatibility, 2026-10-24

Version being verified: 0.9.0, implementation candidate and not 1.0 certified.
Verified CI revision: 6a70fc78f6b92de2164eccba3f76df3c08d38815.

## Actual tests

| Consumer | Executed evidence | Remaining limitation |
| --- | --- | --- |
| Python 3.11 wheel and CLI | Clean installation outside checkout; project snapshot, exact-source gap proposal, typed work unit, multi-domain composition, export and integrity verification | No independent specialist task scoring |
| Python MCP server | In-memory SDK protocol discovery, no-op and typed read-only calls | Not a real human-directed agent |
| Node MCP v2 client | Actual stdio round trip into Python server, including composition | No model-driven tool selection |
| Agent Skills | Pinned official validator checks 26 first-party skills and portable adapter | Native harness discovery is untested |
| External Open ASS host | Pinned public BradKhan/open-ASS checkout at 35f10ba4cb7556b96f98e334ecce64a5f945c975; explicit exported skill, integrity and official format validation, no execution of host code, no tracked changes | Agent discovery or independent execution not proven |
| Data contracts | 12 JSON Schema 2020-12 contracts; Python and Node validation | No complete externally executed signed work receipt |

## CI result

151 deterministic and integration tests passed in GitHub Actions at PR #14 on the pinned revision. Source checks cover bounded POSIX file reads, symlink/FIFO denial, exact excerpt matching, conflicting gap rejection, no-op behavior, dependency ordering, and export integrity.

External host checkout compatibility verifies static distribution only. It is not equivalent to native Codex/Hermes consumption or independent professional quality improvement.

## Blocked release gates

Independent Codex/Hermes agent evaluation, blinded baseline comparisons, real host permission probes, and accountable release approval remain unverified. See issue #16 and docs/V1_HOST_VALIDATION_RUNBOOK.md.

Security adjustment: workflow permissions are limited to contents:read; GitHub checkout credentials are not persisted. External-host smoke uses pinned source as static fixture only and does not execute external repository scripts.

This review series additionally validated advisory-only schemas and semantic plan verification, search across capability/skill/method identifiers, and source-anchored CLI composition with explicitly covered prerequisites. See [stabilization review](V1_STABILIZATION_2026-10-24.md).
