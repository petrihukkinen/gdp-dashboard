# RAW — immutable evidence

Files here are the raw, verbatim source material Jarvis's memory is built
from: quoted messages, document excerpts, meeting notes as written down,
exported emails, etc.

**Rule: nothing in this repository ever edits a file in `RAW/` after it is
committed.** If a fact from here turns out to be wrong or outdated, that is
recorded as a *new* file in `KNOWLEDGE/` that supersedes the old
conclusion — the original evidence stays exactly as it was written. This is
what makes `RAW/` trustworthy: you can always trace a `KNOWLEDGE/` claim
back to the exact words it came from.

Suggested (not enforced) frontmatter for a RAW file:

```yaml
---
title: "Short description"
type: raw_evidence
created: 2026-09-13
tags: [optional, topic, words]
---
Verbatim content goes here.
```

Only `title` is used by the indexer if present; everything else is
optional metadata carried through search results as-is. See
`../README.md` for the full schema and `../scripts/build_index.py` to
(re)build the search index after adding files here.
