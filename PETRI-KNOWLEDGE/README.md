# PETRI-KNOWLEDGE — Jarvis Phase 1 memory

This is the smallest production-worthy implementation of the memory
architecture recommended in
`../research/2026-09-12-jarvis-context-memory/` (see especially
`ARCHITECTURE_OPTIONS.md` and `MEMORY_DESIGN.md` for the reasoning and
sources behind these choices). It is plain files plus one disposable
SQLite search index — no server, no vector database, no knowledge graph,
no new runtime dependency beyond the Python standard library (pytest is
only needed to *run the eval suite*, not to build or search the index).

## Architecture principle

```
RAW IS IMMUTABLE EVIDENCE
KNOWLEDGE IS DERIVED
INDEX IS DISPOSABLE
```

- **`RAW/`** — verbatim source material (quotes, document excerpts, notes
  as written down). Never edited once committed. If something here turns
  out to be wrong, that is recorded as new `KNOWLEDGE/`, not a rewrite of
  the evidence.
- **`INGEST/`** — normalized staging area for material pulled out of
  `RAW/` (cleaned up, reformatted) but not yet curated into `KNOWLEDGE/`.
  Not validated; treat search hits from here as leads, not answers.
- **`KNOWLEDGE/`** — curated decisions, tasks, and facts, each traceable
  back to `RAW/`/`INGEST/` via a `source:` frontmatter field. This is what
  Jarvis should actually rely on day to day.
- **`INDEX/jarvis.sqlite`** — a full-text search index rebuilt entirely
  from the three directories above. It is never the source of truth for
  anything: delete it and rerun `build_index.py` and you get it back with
  no loss of information (this is tested — see below).
- **`EVALS/memory_tests/`** — a small, real, repeatable test suite against
  a synthetic fixture corpus, plus the fixtures themselves.

## Source-of-truth hierarchy

1. A file under `RAW/` or `KNOWLEDGE/` (committed to Git) is authoritative.
2. `INGEST/` is a workbench — useful, searchable, but not authoritative.
3. `INDEX/jarvis.sqlite` is a cache. It is `.gitignore`d on purpose: it
   should never be the only place a piece of information lives.
4. Git history is the change log and backup for 1–3. There is no separate
   backup mechanism in Phase 1 — commit your changes.

## Document format

Every indexed file is Markdown with optional YAML-like frontmatter:

```yaml
---
title: "Short, specific title"     # weighted highest in search ranking
type: decision                      # decision | task | fact | raw_evidence | ...
project: aurora                     # your own convention, used with --type/--layer
source: RAW/some-file.md            # or source_type: user_statement
created: 2026-09-13
status: current                     # your own convention (e.g. current | superseded)
superseded_by: null                 # your own convention
tags: [topic, words]
---
The body. This is what full-text search actually indexes, along with
the title and tags.
```

Only flat `key: value` pairs and simple `[a, b, c]` lists are understood
(no nested YAML) — this is intentional, see "Non-goals" below. Any field
you invent (like `status`/`superseded_by` above) is still captured
verbatim and comes back in every search result under `meta`, with no
schema change required.

## Rebuilding the index

```bash
python3 scripts/build_index.py                       # uses this directory
python3 scripts/build_index.py --root /other/path    # index somewhere else
python3 scripts/build_index.py --db /tmp/test.sqlite  # write elsewhere (used by the eval suite)
```

Always does a full rebuild into a temp file and atomically replaces
`INDEX/jarvis.sqlite` — never a partial or corrupt file, even if
interrupted. Reports `Indexed:` / `Skipped:` (non-`.md` files) /
`Errors:` (a file that failed to parse — logged per file, does not abort
the run) and exits `1` if any file errored, `0` otherwise.

You can delete `INDEX/jarvis.sqlite` at any time; the next
`build_index.py` run recreates it from `RAW/`, `INGEST/`, and `KNOWLEDGE/`
alone.

## Searching

```bash
python3 scripts/search.py "some words"
python3 scripts/search.py "some words" --type decision --layer KNOWLEDGE --limit 5
python3 scripts/search.py "some words" --json
```

Plain full-text keyword search (SQLite FTS5): every word in the query must
appear somewhere in the matched document (title, tags, or body) — this is
literal keyword matching, not semantic search (see "Non-goals"). Results
are ranked with the title weighted far above the body, so a document
whose *title* matches beats one that only mentions the words in passing.
Every result carries its path, layer, type, source, and full frontmatter
(`meta`) — enough to decide whether to trust it and where to read the
original.

## Running the evals

```bash
pip install -r EVALS/requirements.txt   # once, if pytest isn't already installed
python3 -m pytest EVALS/memory_tests -v
```

10 tests against a small synthetic fixture corpus (not your real data —
see `EVALS/memory_tests/fixtures/`), covering: exact factual recall,
finding a fact recorded in a different document than a naive match would
suggest, temporal/latest-information selection, provenance/source
identification, stale-vs-current metadata, resistance to irrelevant
context, correct "no result" behaviour on both the search function and the
CLI, that indexing never modifies `RAW/`, and that the index is fully
disposable and rebuildable. These are real, currently-passing tests, not
a plan — see the final report in the conversation for the exact run
output. No published benchmark result is claimed anywhere in this
implementation.

## Known limitations (Phase 1)

- **Full rebuild only.** Every `build_index.py` run re-reads and
  re-inserts every file. Fine at the scale this is designed for (one
  person, hundreds of files); would need an incremental-update path
  (using the stored `checksum`) at much larger scale. Deferred on
  purpose — no evidence yet that it's needed.
- **No automatic recency/conflict resolution.** If two `KNOWLEDGE/` files
  disagree, search returns both; nothing in Phase 1 decides which one is
  right. That is a deliberate, permanent design choice per the research
  (`RESEARCH_REPORT.md` B4), not a gap to fill later — a human (or an
  agent that then asks a human) resolves conflicts, an algorithm doesn't
  guess.
- **No session-start/session-end hook wiring yet.** `MEMORY_DESIGN.md`'s
  checkpoint procedure (`SessionStart`/`SessionEnd` reading and writing a
  `PROGRESS.md`) is designed but not wired up to Claude Code hooks in this
  phase.
- **No validation gate for untrusted sources.** `MEMORY_DESIGN.md`'s
  candidate/validation pipeline for content coming from outside a direct
  user statement is designed but not implemented — Phase 1 only builds
  the storage and retrieval layer, not the write-path policy around it.
  Do not point `INGEST/`/`KNOWLEDGE/` ingestion at untrusted external
  content (web pages, emails) until that gate exists.

## Non-goals for Phase 1 (explicit)

- **No vector/semantic search.** Nothing here understands synonyms or
  meaning — only literal word matches (see `ARCHITECTURE_OPTIONS.md` for
  when this would become justified, and the concrete trigger condition).
- **No knowledge graph.** No entity/relationship modeling across documents.
- **No separate memory service, daemon, or cloud dependency.** Everything
  runs as two short-lived local scripts.
- **No multi-agent orchestration.**
- **No concurrent-write locking.** Phase 1 assumes one person, one
  process editing `KNOWLEDGE/`/`RAW/` at a time; Git conflicts (not a
  custom lock) are the mechanism if that's ever violated.
- **No automated promotion pipeline from `INGEST/` to `KNOWLEDGE/`.**

## Security notes

- No secrets are stored anywhere in this implementation or its fixtures.
- Indexed document content is **never executed**. `build_index.py` reads
  bytes, decodes them as text, and does simple string parsing
  (`common.parse_frontmatter`) — no `eval()`, no `yaml.load()`, no
  shelling out to anything derived from file content.
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
- `INDEX/jarvis.sqlite` is `.gitignore`d — it is a local cache, rebuilt on
  demand, so it is never something to accidentally commit or treat as a
  backup.

## Architectural decisions worth flagging

- **Flat `KNOWLEDGE/` with a `type:` field**, not one subfolder per type
  as `MEMORY_DESIGN.md` originally sketched — `--type`/`--layer` search
  filters make the folder split redundant, and fewer directories is
  simpler to maintain. See `KNOWLEDGE/README.md`.
- **A `meta_json`-equivalent catch-all (`meta` in search results)** stores
  the entire frontmatter verbatim, not just the columns with dedicated
  storage. This means you can invent a new frontmatter field (like
  `status` or `superseded_by`) at any time without a schema migration —
  it just shows up in `meta`.
- **Full rebuild instead of incremental update.** Simpler, fully
  deterministic, and fast enough at this scale; the stored `checksum`
  column exists specifically so an incremental mode can be added later
  without changing the schema.
- **AND-of-literal-tokens query matching**, not fuzzy or ranked-OR
  matching. Predictable and testable; a real limitation if your vocabulary
  varies (see `ARCHITECTURE_OPTIONS.md`'s vector-search trigger condition
  for when this would need to change).
