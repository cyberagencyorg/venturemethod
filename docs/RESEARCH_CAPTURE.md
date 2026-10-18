# Research capture and evidence brief

The first executable research capability in Venture Method is deliberately modest. It handles operator-provided UTF-8 source material. It does not scrape websites, independently authenticate a publisher, analyze a market with AI, or turn a quotation into a verified fact.

The distinction matters: a content hash establishes what bytes were stored, while a real investigation must still establish whether the source is accurate, representative, current, and relevant to the question.

## Run it

Create a scoped engagement or use one you already have:

```bash
python vm.py new "Example Assessment" --type company --industry logistics --mode quick
python vm.py intake example-assessment --objective "Assess whether customer demand is sufficient for a pilot" --approval-owner "Engagement owner"
```

Save a source you have the right to use as a local UTF-8 `.txt`, `.md`, `.csv`, or `.tsv` file. Preserve the source URL or other locator, and don't substitute an AI-generated summary for original evidence.

```bash
python vm.py research import example-assessment \
  --file /path/to/permitted-source.txt \
  --title "Quarterly industry bulletin" \
  --locator "https://publisher.example/industry/quarterly-bulletin" \
  --kind report --publisher "Publisher name"
```

The command returns `source_id` and a SHA-256 snapshot digest. The locator is a reference, **not** an instruction to fetch the URL. The bytes are copied to `engagements/<slug>/research/snapshots/`, which is ignored by Git.

Add an interpretation only when you can point to an exact passage in the captured source:

```bash
python vm.py research claim example-assessment \
  --source SRC-0001 \
  --text "The publisher reports an increase in customer inquiries" \
  --excerpt "exact phrase copied from source"
```

The excerpt must occur verbatim in the captured file. A match proves that the text exists in the snapshot, **not** that the statement is accurate. Claims remain explicitly unrated and unknown.

Generate a private working evidence brief and inspect source integrity:

```bash
python vm.py research audit example-assessment
python vm.py research brief example-assessment --question "What evidence exists about customer demand?"
```

The brief includes operator-written interpretations, exact excerpts, source IDs, locators and SHA-256 hashes, unresolved review questions, and a reproducible evidence version. It is not a finished commercial recommendation and cannot be published automatically.

## When new research arrives

Import new material under the **same locator**. If the captured content differs, Venture Method creates a separate source record and reports the earlier source's recorded dependents, including connected claims, decisions and evidence briefs.

Nothing is automatically declared superseded. Documents may change because of editorial corrections, formatting, or an entirely new publication. Human review must determine what changed and whether an old conclusion still holds.

`python vm.py research audit <engagement>` checks the journal, captured files, excerpt bindings, artifact hashes, and reports evidence briefs based on older snapshots as candidates for review. Existing drafts remain immutable. Creating a new brief produces a new source-linked version without rewriting the earlier one.

## Boundaries and limitations

- Only local plain UTF-8 text is accepted; maximum 512 KiB per captured file.
- Symlink source files and symlinked research directories are rejected. Files stay under one gitignored engagement.
- The publisher and locator fields are operator assertions. A source may be inaccurate, fabricated, or legally restricted despite passing hash and excerpt checks.
- The system does not verify publication rights or permission to redistribute a source. Never commit confidential sources or distribute captured third-party text without appropriate rights.
- It does not infer unsupported claims, conduct interviews, execute agents, or make outbound network calls.
- Journal and content hashes are tamper-*evident relative to recorded state*, not independently signed audit evidence. Local single-writer assumptions still apply.
- Evidence briefs need human assessment for relevance, source independence, quantitative accuracy, contradictory evidence and consequent recommendations.

A subsequent adapter may retrieve authorized public sources, but it must preserve origin, permissions, content type, date, snapshot integrity and isolation. Do not add arbitrary URL fetching without threat-modeling SSRF, redirection, credential handling and untrusted content.
