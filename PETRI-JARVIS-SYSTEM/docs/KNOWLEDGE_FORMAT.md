# Knowledge root format

This document specifies the file format `scripts/build_index.py` and
`scripts/search.py` expect to find under whatever directory you pass as
`--root` (or set via `PETRI_JARVIS_KNOWLEDGE_ROOT`). **This repository
does not contain that directory** — see `../README.md` for why, and where
it lives instead.

## Layout the indexer expects at the knowledge root

```
<knowledge-root>/
├── RAW/          immutable evidence — never edited once written
├── INGEST/       normalized staging area, not yet curated (optional)
├── KNOWLEDGE/    curated decisions, tasks, facts — what Jarvis relies on
└── INDEX/        created by build_index.py; safe to delete any time
```

`RAW/`, `INGEST/`, and `KNOWLEDGE/` are the three "layers" the indexer
scans (`scripts/common.LAYERS`); any of the three may be absent and it
will simply be skipped, but at least one must exist and contain `.md`
files for search to return anything.

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
(no nested YAML) — this is intentional, see "Non-goals" in `../README.md`.
Any field you invent (like `status`/`superseded_by` above) is still
captured verbatim and comes back in every search result under `meta`,
with no code change required.

Two filenames are treated as folder documentation, not content, and are
never indexed: `README.md` and `.gitkeep`.

## Recommended (not enforced) convention inside `KNOWLEDGE/`

Phase 1 keeps `KNOWLEDGE/` flat and uses the `type:` field instead of one
subfolder per type, because `search.py --type decision` already gives
type-filtered retrieval without the folder split. This is a deliberate
simplification — see "Architectural decisions" in `../README.md`.
