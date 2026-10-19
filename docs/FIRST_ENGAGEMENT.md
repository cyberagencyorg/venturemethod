# Use Khan's Venture Method Framework on a real engagement

Venture Method currently works as a **private local workbench**. It can help structure research, preserve evidence and decisions, choose methods, and pass a bounded assignment to a human or compatible AI agent. It does not yet run an autonomous research team or certify the quality of a report.

You need Python 3.11+ and a clone of the private repository. Run every command below from the repository root. No Python packages or model API keys are required for the operator commands.

## 1. Verify and open an engagement

```bash
python vm.py doctor
python vm.py start "First Market Assessment" \
  --type company \
  --industry "business services" \
  --objective "Assess whether this market justifies a limited pilot" \
  --owner "Engagement principal" \
  --output "A concise, sourced assessment and recommended next steps"
python vm.py status first-market-assessment
```

The new engagement is stored under `engagements/first-market-assessment/`, which Git ignores. It is **not encrypted**. Work on a machine and filesystem appropriate for the information you hold. Do not commit, upload, or forward client material without permission.

## 2. Capture real evidence

Use your own accessible source file with permission to store it, such as an interview transcript or saved public research. `.txt`, `.md`, `.csv` and `.tsv` files are accepted, up to 512 KiB.

```bash
python vm.py research import first-market-assessment \
  --file /path/to/source.txt \
  --title "Source title" \
  --locator "https://original-source.example/report" \
  --publisher "Publisher as reported"
```

For a public HTTPS page, approve exactly the host you intend to contact:

```bash
python vm.py research fetch first-market-assessment \
  --url "https://www.example.org/" \
  --allow-host www.example.org \
  --title "Public source"
```

The restricted fetch adapter rejects redirects, IP-literal/private destinations, large responses, and unsupported content formats. Some modern sites will not work. Use a legitimate local export when necessary. A successful download is not independent source verification.

The import returns a source ID such as `SRC-0001`. Record a **literal excerpt present in that source**, along with your interpretation:

```bash
python vm.py research claim first-market-assessment \
  --source SRC-0001 \
  --excerpt "Exact text from the captured source" \
  --text "What this text may imply for the decision"
```

Source existence and exact-excerpt checks are mechanical. Corroborate important claims and keep disagreements or unknowns visible.

## 3. Choose a method when necessary

Inspect the available methods:

```bash
python vm.py frameworks --goal map_market --evidence minimal
python vm.py capabilities
```

A method is useful only if it serves the actual question. The following is an **example** choice, not a mandatory process:

```bash
python vm.py compose first-market-assessment \
  --goal map_market \
  --method market-sizing \
  --evidence minimal \
  --save
```

The returned plan contains a filename such as `plans/composition-<hash>.json`. It also identifies missing inputs and whether a method can be performed. A skill name in the plan does not prove that an agent has executed it.

## 4. Prepare the handoff to Hermes or another agent

```bash
python vm.py packet first-market-assessment
```

The command creates a versioned `deliverables/work-packet-<hash>.md` in the private engagement. It includes the objective, bounded evidence excerpts, recorded options and decisions, and the selected composition plan if exactly one saved plan exists.

When several saved plans exist, pass the specific **filename**:

```bash
python vm.py packet first-market-assessment --plan composition-<hash>.json
```

The command refuses a selected plan whose source, claim, engagement or method registry inputs have changed since it was saved. Reassess and save a current plan instead.

You can open that file in any text editor. For Hermes, load the [Venture Method skill](../.agents/skills/venturemethod/SKILL.md) alongside the packet through your configured local agent environment. The packet can also be pasted into another compatible AI tool or given to a human collaborator. **Review confidential source excerpts and tool permissions before sending them outside your machine.**

The receiving agent should return a Markdown draft with exact source references and unresolved questions. The current CLI does not invoke Hermes, send private material to an external model, or claim agents performed tasks they didn't perform.

## 5. Capture work returned for review

```bash
python vm.py submit first-market-assessment \
  --file /path/to/draft.md \
  --author "Agent or human (operator assertion)"
python vm.py status first-market-assessment
python vm.py audit first-market-assessment
```

A submitted `.md`/`.txt` document is copied to a content-hash-named private draft and recorded in the engagement journal. References such as `SRC-0001` and `CLM-0001` must belong to this engagement. Citations can still be misplaced or misleading; this check does **not** validate the narrative.

Review the draft personally or with a separate qualified reviewer. In particular check source accuracy, independent confirmation, alternatives, cost assumptions, legal or commercial risks, and whether the conclusions warrant further work.

You can also generate the current evidence register:

```bash
python vm.py research brief first-market-assessment
```

When a source changes, recapture it under the same locator. `status` detects draft and packet references to older source versions and raises a review notice. Old outputs remain intact rather than being silently replaced.

## When to use existing commands instead

- `python vm.py ost ...` for an evidence-linked Opportunity Solution Tree.
- `python vm.py compose ...` for method/capability selection without executing work.
- `python vm.py generate <engagement> --type decision-brief` for an evidence/decision register.
- `python vm.py research-benchmark ...` to prepare a blind comparison of independently produced reports (requires a human reviewer).
- `python vm.py demo` for a wholly fictional tutorial.

## What is not ready

Autonomous end-to-end research, verified finance models, execution through Hermes or other runtimes from this CLI, authenticated approvals, group collaboration, secret management, client permissions, independent expert quality evaluation, and publication controls. Use appropriate external systems and professional reviewers for those functions.
