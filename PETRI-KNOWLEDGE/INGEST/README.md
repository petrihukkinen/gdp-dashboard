# INGEST — normalized staging area

`INGEST/` holds material that has been pulled out of `RAW/` and cleaned up
(OCR'd, transcribed, reformatted to Markdown, split into smaller pieces)
but has **not yet been curated** into a `KNOWLEDGE/` decision, task, or
fact.

Nothing here is guaranteed to be validated or even correct — it is a
workbench, not a source of truth. The indexer (`../scripts/build_index.py`)
scans it as its own `layer` so it is searchable, but a search result from
`INGEST/` should be treated as a lead to verify, not an answer.

Phase 1 does not implement automatic promotion from `INGEST/` to
`KNOWLEDGE/` — that happens by a human (or an agent, with a human
confirming) writing a new file in `KNOWLEDGE/` that cites the `INGEST/` or
`RAW/` material it is based on via a `source:` frontmatter field.

This directory is intentionally empty in Phase 1 (no example file) — there
is nothing generic to demonstrate here that `RAW/` and `KNOWLEDGE/`'s
examples don't already cover.
