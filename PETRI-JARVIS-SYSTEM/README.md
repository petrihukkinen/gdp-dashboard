# PETRI-JARVIS-SYSTEM — Jarvis memory system (Phase 1 + 1.1 hardening)

This is the smallest production-worthy implementation of the memory
architecture recommended in
`../research/2026-09-12-jarvis-context-memory/` (see especially
`ARCHITECTURE_OPTIONS.md` and `MEMORY_DESIGN.md` for the reasoning and
sources behind these choices). It is plain files plus one disposable
SQLite search index — no server, no vector database, no knowledge graph,
no new runtime dependency beyond the Python standard library (pytest is
only needed to *run the eval suite*, not to build or search the index).

## Repository boundary — read this first

```
PETRI-JARVIS-SYSTEM = how Jarvis works   (this directory: code, schema, tests, docs)
PETRI-KNOWLEDGE     = what Jarvis knows  (a separate vault — NOT in this repository)
```

**This directory contains no personal or business knowledge and never
should.** It is code: two scripts, a shared module, documentation, and a
synthetic test corpus. Your actual `RAW/`, `INGEST/`, and `KNOWLEDGE/`
folders (see `docs/KNOWLEDGE_FORMAT.md` for their format) belong in a
**separate directory or repository** that you point the scripts at with
`--root` or the `PETRI_JARVIS_KNOWLEDGE_ROOT` environment variable.

As of this hardening pass, no such separate vault exists yet under this
account (checked via GitHub repo listing — see the session's final
report). Setting one up — deciding its name, location, and whether it is
its own Git repository — is a decision for Petri to make; this pass does
not create one on its own. Earlier versions of this implementation put
example `RAW/INGEST/KNOWLEDGE/INDEX` folders directly inside this
directory; that was the exact boundary problem this review corrected, and
those folders have been removed from here (the `docs/` directory now
carries the same schema information as pure documentation, and the
scripts have no self-referential default location any more).

## Rebuilding the index

```bash
python3 scripts/build_index.py --root /path/to/your/knowledge/vault
# or, once set:
export PETRI_JARVIS_KNOWLEDGE_ROOT=/path/to/your/knowledge/vault
python3 scripts/build_index.py
```

Always does a full rebuild into a temp file and atomically replaces
`<root>/INDEX/jarvis.sqlite` — never a partial or corrupt file, even if
interrupted. Reports `Indexed:` / `Skipped:` (non-`.md` files) /
`Errors:` (a file that failed to parse — logged per file, does not abort
the run) and exits `1` if any file errored or if no knowledge root could
be resolved at all.

You can delete `<root>/INDEX/jarvis.sqlite` at any time; the next
`build_index.py` run recreates it from `RAW/`, `INGEST/`, and `KNOWLEDGE/`
alone — see `docs/KNOWLEDGE_FORMAT.md` for what those directories and
their files should look like.

## Searching

```bash
python3 scripts/search.py "some words" --root /path/to/your/knowledge/vault
python3 scripts/search.py "some words" --type decision --layer KNOWLEDGE --limit 5
python3 scripts/search.py "some words" --json
```

Plain full-text keyword search (SQLite FTS5): every word in the query must
appear somewhere in the matched document (title, tags, or body) — this is
literal keyword matching, not semantic search (see "Non-goals"). Results
are ranked with the title weighted far above the body, so a document
whose *title* matches beats one that only mentions the words in passing.
Every result carries its path, **layer** (`RAW`/`INGEST`/`KNOWLEDGE` —
always present, so you always know where an answer came from), type,
source, and full frontmatter (`meta`) — enough to decide whether to trust
it and where to read the original.

## Running the evals

```bash
pip install -r EVALS/requirements.txt   # once, if pytest isn't already installed
python3 -m pytest EVALS/memory_tests -v
```

**26 tests, all passing**, against two synthetic fixture corpora (not
your real data — see `EVALS/memory_tests/fixtures/` and
`fixtures_extended/`):

- `test_memory.py` (10 tests, Phase 1): exact factual recall, finding a
  fact recorded in a different document than a naive match would suggest,
  temporal/latest-information selection, provenance/source
  identification, stale-vs-current metadata, resistance to irrelevant
  context, correct "no result" behaviour (function + CLI), that indexing
  never modifies `RAW/`, and that the index is fully disposable and
  rebuildable.
- `test_extended_synthetic_eval.py` (16 tests, Phase 1.1 hardening): the
  same categories again on a larger, more domain-realistic corpus
  (investment/broker decisions, a startup cap table, a shareholder
  agreement — entirely fabricated, not real Jarvis knowledge, since none
  was available to test against in this session), plus explicit,
  **measured** Finnish word-form (morphology) behavior — see "Finnish
  search: measured, not assumed" below.

These are real, currently-passing tests, not a plan. No published
benchmark result is claimed anywhere in this implementation.

## Finnish search: measured, not assumed

Phase 1 search does no stemming — SQLite's `unicode61` tokenizer treats
each inflected word form as a distinct literal token. Running the
extended eval corpus against real Finnish sentences measured this
directly rather than speculating about it:

| Query form | Result |
|---|---|
| A word form that appears verbatim in a document's **title** (e.g. nominative `välittäjä`, `osakassopimus`) | **Matches** |
| A word form that appears verbatim in a document's **body**, in whatever case it was written (e.g. genitive `välittäjän`, illative `osakassopimukseen`) | **Matches** |
| A different inflection of the same word that never appears anywhere in the corpus (e.g. partitive `välittäjää`, elative `välittäjästä`/`osakassopimuksesta`) | **Does not match** |
| An English loanword with a Finnish case suffix attached, as a person might actually type it (`cap tablen` for `cap table`) | **Does not match** — same limitation, not specific to Finnish roots |

**Verdict:** the failures are real and are exactly what plain literal
full-text search implies — not a bug, and not tolerable indefinitely, but
tolerable **at Phase 1's actual scale** (one user, short curated
`KNOWLEDGE/` entries, titles that are naturally written in base form).
A query fails only when *no form of a word anywhere in the target
document* matches the form used in the query; in practice this means a
second attempt with a different case usually succeeds. No stemming,
embeddings, or semantic search were added to fix this — per this
review's explicit constraint, and because the measured failure mode
(missing a specific inflected form) is not yet materially hurting
usefulness at this scale. If real usage starts producing repeated
empty-result searches for exactly this reason, that is the concrete,
observable trigger condition `ARCHITECTURE_OPTIONS.md` already names for
reconsidering vector search — not a hypothetical one anymore, but still
not yet crossed.

## Known limitations (unchanged from Phase 1, still deferred on purpose)

- **Full rebuild only.** Every `build_index.py` run re-reads and
  re-inserts every file. Fine at the scale this is designed for; an
  incremental-update path (using the stored `checksum`) would be needed
  at much larger scale. No evidence yet that it's needed.
- **No automatic recency/conflict resolution.** If two `KNOWLEDGE/` files
  disagree, search returns both; nothing decides which one is right. A
  deliberate, permanent design choice per the research
  (`RESEARCH_REPORT.md` B4), not a gap to fill later.
- **No session-start/session-end hook wiring yet** for
  `MEMORY_DESIGN.md`'s checkpoint procedure.
- **No validation gate for untrusted sources.** `MEMORY_DESIGN.md`'s
  candidate/validation pipeline for content coming from outside a direct
  user statement is designed but not implemented. Do not point
  `INGEST/`/`KNOWLEDGE/` ingestion at untrusted external content (web
  pages, emails) until that gate exists.
- **The actual PETRI-KNOWLEDGE vault does not exist yet.** This pass
  fixed the repository *boundary* (this repo no longer pretends to hold
  real data); it did not create the separate vault itself — that is
  Petri's decision (see "Repository boundary" above).

## Non-goals for Phase 1 (explicit, unchanged)

- **No vector/semantic search** — see "Finnish search" above for the
  concrete, now-measured trigger condition for revisiting this.
- **No knowledge graph.** No entity/relationship modeling across documents.
- **No separate memory service, daemon, or cloud dependency.** Everything
  runs as two short-lived local scripts.
- **No multi-agent orchestration.**
- **No concurrent-write locking.** Phase 1 assumes one person, one
  process editing the vault at a time; Git conflicts (not a custom lock)
  are the mechanism if that's ever violated.
- **No automated promotion pipeline from `INGEST/` to `KNOWLEDGE/`.**
  Verified directly in this review: nothing in `scripts/` writes to
  `KNOWLEDGE/` at all — every write path is `INDEX/jarvis.sqlite` only.

## Security notes

- No secrets are stored anywhere in this implementation or its fixtures.
- Indexed document content is **never executed**. `build_index.py` reads
  bytes, decodes them as text, and does simple string parsing
  (`common.parse_frontmatter`) — no `eval()`, no `yaml.load()`, no
  shelling out to anything derived from file content. Re-verified by
  direct grep in this review: no `eval`/`exec`/`os.system`/`subprocess`/
  `pickle`/`yaml.load` anywhere in `scripts/`.
- A document's content — including its frontmatter — is always treated as
  **data to store and display, never as an instruction to follow**. If you
  point an agent at this system and it reads search results, nothing in
  `KNOWLEDGE/`, `INGEST/`, or `RAW/` should be able to redirect that
  agent's behavior; only your own prompt should. This matters most once
  `INGEST/` starts holding content pulled from outside sources — see
  "Known limitations" above about the missing validation gate.
- The indexer stays inside the given root: it resolves every path and
  refuses to follow a symlink that points outside it
  (`common.is_within`), so a stray symlink under `RAW/`/`KNOWLEDGE/`
  cannot make the index (or a search result) expose an unrelated file
  elsewhere on disk.
- The disposable index (`<root>/INDEX/jarvis.sqlite`) lives inside your
  knowledge vault, not in this repository, so this repository has
  nothing sensitive to `.gitignore` in the first place; the root
  `.gitignore` still carries a defensive rule in case a test index is
  ever written inside this tree by mistake.

## Architectural decisions worth flagging

- **This directory is named for what it is** (`PETRI-JARVIS-SYSTEM`, the
  system), not for what it used to also contain (a knowledge-shaped
  folder tree). The rename is the whole fix for the Phase 1.1 boundary
  review — see "Repository boundary" above.
- **Flat `KNOWLEDGE/` with a `type:` field**, not one subfolder per type
  — `--type`/`--layer` search filters make the folder split redundant.
  See `docs/KNOWLEDGE_FORMAT.md`.
- **A `meta` catch-all in every search result** stores the entire
  frontmatter verbatim, not just the columns with dedicated storage — a
  new frontmatter field needs no schema migration.
- **Full rebuild instead of incremental update.** Simpler, fully
  deterministic, and fast enough at this scale; the stored `checksum`
  column exists specifically so an incremental mode can be added later.
- **AND-of-literal-tokens query matching**, not fuzzy or ranked-OR
  matching. Predictable and testable — see "Finnish search" above for
  what this costs in practice, now measured rather than assumed.
- **No default knowledge root any more.** `--root`/`--db` must be given
  explicitly, or `PETRI_JARVIS_KNOWLEDGE_ROOT` must be set — there is
  deliberately no "index this directory itself" fallback, because that
  fallback is exactly what caused the boundary confusion this review
  fixed.
