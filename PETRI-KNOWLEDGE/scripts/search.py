#!/usr/bin/env python3
"""Search the disposable Jarvis index built by build_index.py.

Phase 1 search is deliberately plain full-text keyword search (SQLite
FTS5), not semantic/vector search — see ../README.md "Non-goals". Query
words are combined with AND, each treated as a literal token, so results
are predictable and reproducible rather than fuzzy.

Every result is a *pointer* to a canonical file (path + layer + full
frontmatter as `meta`), never a substitute for reading it — the index
holds nothing that is not also in that file.

Usage:
    python3 search.py "some query" [--limit N] [--layer RAW|INGEST|KNOWLEDGE]
                       [--type decision] [--json] [--root PATH] [--db PATH]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent

# Column weights for bm25(): title matches matter far more than an
# incidental word buried in a tag or the body. This is the one "ranking"
# decision Phase 1 makes — not semantic search, just "titles win ties".
_BM25_WEIGHTS = (10.0, 2.0, 1.0)  # title, tags, body


def _to_fts_query(query: str) -> str:
    """Turn free-text user input into a safe, literal AND-of-tokens FTS5
    query. This avoids FTS5 syntax errors on punctuation/operators in
    arbitrary input and keeps matching predictable (see module docstring).
    """
    tokens = re.findall(r"\w+", query, flags=re.UNICODE)
    if not tokens:
        return '""'
    return " AND ".join(f'"{t}"' for t in tokens)


def search(
    db_path: Path,
    query: str,
    limit: int = 10,
    layer: str | None = None,
    doc_type: str | None = None,
) -> list[dict]:
    if not db_path.exists():
        raise FileNotFoundError(
            f"No index at {db_path}. Run build_index.py first."
        )

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        sql = [
            "SELECT d.path, d.layer, d.title, d.doc_type, d.source, d.tags,",
            "       d.created, d.modified, d.checksum, d.meta_json,",
            "       snippet(documents_fts, 2, '[', ']', ' … ', 12) AS snippet,",
            f"       bm25(documents_fts, {_BM25_WEIGHTS[0]}, {_BM25_WEIGHTS[1]}, {_BM25_WEIGHTS[2]}) AS score",
            "FROM documents_fts",
            "JOIN documents d ON d.rowid = documents_fts.rowid",
            "WHERE documents_fts MATCH ?",
        ]
        params: list = [_to_fts_query(query)]
        if layer:
            sql.append("AND d.layer = ?")
            params.append(layer)
        if doc_type:
            sql.append("AND d.doc_type = ?")
            params.append(doc_type)
        sql.append("ORDER BY score LIMIT ?")
        params.append(limit)

        rows = conn.execute("\n".join(sql), params).fetchall()
    finally:
        conn.close()

    results = []
    for row in rows:
        item = dict(row)
        item["meta"] = json.loads(item.pop("meta_json"))
        results.append(item)
    return results


def _print_human(results: list[dict]) -> None:
    if not results:
        print("No results found.")
        return
    for r in results:
        print(f"[{r['layer']}] {r['title']}  ({r['path']})")
        if r.get("doc_type"):
            print(f"    type: {r['doc_type']}")
        if r.get("source"):
            print(f"    source: {r['source']}")
        if r.get("created"):
            print(f"    created: {r['created']}")
        shown = {"title", "type", "source", "created", "tags"}
        extra = {k: v for k, v in r["meta"].items() if k not in shown}
        for k, v in sorted(extra.items()):
            print(f"    {k}: {v}")
        print(f"    {r['snippet']}")
        print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--layer", choices=["RAW", "INGEST", "KNOWLEDGE"])
    parser.add_argument("--type", dest="doc_type", help="filter by frontmatter 'type' field")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--db", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    db_path = args.db or (args.root / "INDEX" / "jarvis.sqlite")
    try:
        results = search(db_path, args.query, args.limit, args.layer, args.doc_type)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        _print_human(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())
