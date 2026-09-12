#!/usr/bin/env python3
"""Rebuild the disposable Jarvis search index from canonical Markdown files.

    RAW IS IMMUTABLE EVIDENCE — this script never opens RAW/, INGEST/, or
    KNOWLEDGE/ files for writing. It only reads them.
    KNOWLEDGE IS DERIVED — files under KNOWLEDGE/ are curated by a human or
    an agent; this script does not judge their content, only indexes it.
    INDEX IS DISPOSABLE — this script always rebuilds INDEX/jarvis.sqlite
    from scratch into a temp file and atomically replaces the old one. You
    can delete jarvis.sqlite at any time and re-run this script to get it
    back with no loss of canonical information.

Usage:
    python3 build_index.py [--root PATH] [--db PATH]

Exit code is 0 if every file indexed cleanly, 1 if any file raised a parse
error (skipped files that are simply not .md are not treated as errors).
"""
from __future__ import annotations

import argparse
import datetime
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

import common

DEFAULT_ROOT = Path(__file__).resolve().parent.parent


@dataclass
class BuildReport:
    indexed: int = 0
    skipped: list[str] = field(default_factory=list)
    errors: list[tuple[str, str]] = field(default_factory=list)


def rebuild(root: Path, db_path: Path) -> BuildReport:
    report = BuildReport()
    docs: list[common.ParsedDocument] = []

    for layer in common.LAYERS:
        layer_dir = root / layer
        if not layer_dir.is_dir():
            continue
        for path in common.iter_candidate_files(layer_dir):
            rel = path.relative_to(root).as_posix()
            if not common.is_within(path, root):
                report.skipped.append(rel)
                continue
            if path.suffix.lower() != ".md":
                report.skipped.append(rel)
                continue
            try:
                docs.append(common.parse_document(path, root, layer))
            except Exception as exc:  # noqa: BLE001 - one bad file must not abort the run
                report.errors.append((rel, f"{type(exc).__name__}: {exc}"))

    db_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = db_path.with_suffix(db_path.suffix + ".tmp")
    if tmp_path.exists():
        tmp_path.unlink()

    conn = sqlite3.connect(tmp_path)
    try:
        conn.executescript(common.SCHEMA)
        indexed_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
        with conn:
            for doc in docs:
                common.insert_document(conn, doc, indexed_at)
    finally:
        conn.close()

    tmp_path.replace(db_path)
    report.indexed = len(docs)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=DEFAULT_ROOT,
        help="Knowledge root containing RAW/ INGEST/ KNOWLEDGE/ (default: %(default)s)",
    )
    parser.add_argument(
        "--db", type=Path, default=None,
        help="Output SQLite path (default: <root>/INDEX/jarvis.sqlite)",
    )
    args = parser.parse_args(argv)
    db_path = args.db or (args.root / "INDEX" / "jarvis.sqlite")

    report = rebuild(args.root, db_path)

    print(f"Indexed: {report.indexed}")
    print(f"Skipped: {len(report.skipped)}")
    for path in report.skipped:
        print(f"  skip  {path}")
    print(f"Errors:  {len(report.errors)}")
    for path, msg in report.errors:
        print(f"  ERROR {path}: {msg}")
    print(f"Index written to {db_path}")

    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
