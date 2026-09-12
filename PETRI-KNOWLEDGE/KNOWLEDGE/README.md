# KNOWLEDGE — curated, derived knowledge

Files here are the actual memory Jarvis is meant to draw on: decisions,
open tasks, and validated facts. Every file should be traceable back to
where it came from via a `source:` frontmatter field pointing at a `RAW/`
or `INGEST/` file (or `source_type: user_statement` if it came directly
from a conversation with no separate evidence file).

Phase 1 keeps `KNOWLEDGE/` flat and uses the `type:` frontmatter field
(`decision` | `task` | `fact`) instead of one subfolder per type, because
`../scripts/search.py --type decision` already gives type-filtered
retrieval without needing the folder split that
`research/2026-09-12-jarvis-context-memory/MEMORY_DESIGN.md` originally
sketched. This is a deliberate simplification for Phase 1 — see the Phase
1 README's "Architectural decisions" section.

Minimum frontmatter fields (see the full schema in `../README.md`):

```yaml
---
title: "Short, specific title — this is weighted highest in search"
type: decision            # decision | task | fact
project: aurora            # or "personal" — used for --type/--layer filtering later
source: RAW/some-file.md   # or source_type: user_statement
created: 2026-09-13
status: current            # current | superseded (optional, your convention)
superseded_by: null        # id/path of the record that replaced this one
tags: [optional, topic, words]
---
Human-readable content. This is what search actually full-text-indexes,
along with the title and tags.
```

Any frontmatter field not listed above (like `status` and `superseded_by`)
is still captured and returned by search via the `meta` field — see
`../README.md` for how the index stores this.
