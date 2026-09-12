"""Shared helpers for the Jarvis Phase 1 memory index.

Architecture principle (see ../README.md and research/2026-09-12-jarvis-context-memory/):

    RAW IS IMMUTABLE EVIDENCE
    KNOWLEDGE IS DERIVED
    INDEX IS DISPOSABLE

This module only *reads* files under a knowledge root and computes data to
put in the disposable SQLite index. It never writes to RAW/, INGEST/, or
KNOWLEDGE/ — that property is what "raw preservation" depends on, and it is
tested directly in EVALS/memory_tests/test_memory.py.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Environment variable naming the default knowledge root, so build_index.py
# and search.py don't need --root on every call once it's set once in your
# shell profile. See resolve_knowledge_root() below and ../README.md
# "Repository boundary" for why there is no in-repo default any more.
KNOWLEDGE_ROOT_ENV_VAR = "PETRI_JARVIS_KNOWLEDGE_ROOT"


class KnowledgeRootNotConfigured(RuntimeError):
    pass


def resolve_knowledge_root(explicit: Optional[Path]) -> Path:
    """Resolve the knowledge root to scan/search, with no silent fallback
    to "this repository" — see docs/KNOWLEDGE_FORMAT.md. Precedence:
    1. an explicit --root argument, if given
    2. the PETRI_JARVIS_KNOWLEDGE_ROOT environment variable
    Raises KnowledgeRootNotConfigured with a clear message otherwise.
    """
    if explicit is not None:
        return explicit
    env_value = os.environ.get(KNOWLEDGE_ROOT_ENV_VAR)
    if env_value:
        return Path(env_value)
    raise KnowledgeRootNotConfigured(
        "No knowledge root specified. This repository (the Jarvis system) "
        "does not contain your actual RAW/INGEST/KNOWLEDGE data — pass "
        f"--root /path/to/your/knowledge/vault, or set {KNOWLEDGE_ROOT_ENV_VAR} "
        "so you don't have to pass it every time. See docs/KNOWLEDGE_FORMAT.md."
    )


# Directories under a knowledge root that are scanned for canonical content.
# The directory name becomes the "layer" value stored in the index.
LAYERS = ("RAW", "INGEST", "KNOWLEDGE")

# Files that document a folder's purpose rather than holding content. They
# are ignored during indexing (not counted as skipped/error — they are
# expected plumbing, not data).
_IGNORED_NAMES = {".gitkeep", "README.md"}

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Split a minimal YAML-like frontmatter block from the document body.

    Only flat ``key: value`` lines are understood, plus a simple
    ``key: [a, b, c]`` list form flattened to a comma-joined string. The
    Phase 1 schema (see MEMORY_DESIGN.md) does not need nested YAML, so a
    hand-rolled parser avoids adding a PyYAML dependency for it.
    """
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("\"'") for v in value[1:-1].split(",")]
            value = ", ".join(v for v in items if v)
        else:
            value = value.strip("\"'")
        if key:
            meta[key] = value
    body = text[match.end():]
    return meta, body


@dataclass
class ParsedDocument:
    path: str          # POSIX path relative to the knowledge root
    layer: str          # RAW | INGEST | KNOWLEDGE
    title: str
    doc_type: Optional[str]
    source: Optional[str]
    tags: str            # comma-joined, "" if none
    created: Optional[str]
    modified: str         # ISO 8601 UTC, file mtime
    checksum: str         # sha256 of the raw file bytes (change detection)
    body: str             # markdown body, frontmatter stripped
    meta: dict            # full frontmatter, verbatim — for fields with no
                           # dedicated column (e.g. status, superseded_by)


def parse_document(path: Path, root: Path, layer: str) -> ParsedDocument:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    meta, body = parse_frontmatter(text)
    modified = datetime.datetime.fromtimestamp(
        path.stat().st_mtime, tz=datetime.timezone.utc
    ).isoformat()
    return ParsedDocument(
        path=path.relative_to(root).as_posix(),
        layer=layer,
        title=meta.get("title") or path.stem.replace("_", " ").replace("-", " "),
        doc_type=meta.get("type"),
        source=meta.get("source") or meta.get("source_ref"),
        tags=meta.get("tags", ""),
        created=meta.get("created") or meta.get("date") or meta.get("valid_from"),
        modified=modified,
        checksum=sha256_of(raw),
        body=body.strip(),
        meta=meta,
    )


def is_within(path: Path, root: Path) -> bool:
    """True if path resolves to somewhere inside root (guards symlinks
    that could otherwise make the indexer read or report files outside
    the knowledge root)."""
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def iter_candidate_files(layer_dir: Path):
    for path in sorted(layer_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.name in _IGNORED_NAMES:
            continue
        yield path


SCHEMA = """
CREATE TABLE documents (
    path        TEXT PRIMARY KEY,
    layer       TEXT NOT NULL,
    title       TEXT NOT NULL,
    doc_type    TEXT,
    source      TEXT,
    tags        TEXT NOT NULL DEFAULT '',
    created     TEXT,
    modified    TEXT NOT NULL,
    checksum    TEXT NOT NULL,
    body        TEXT NOT NULL,
    meta_json   TEXT NOT NULL,
    indexed_at  TEXT NOT NULL
);

CREATE VIRTUAL TABLE documents_fts USING fts5(
    title, tags, body,
    content='documents', content_rowid='rowid'
);

CREATE TRIGGER documents_ai AFTER INSERT ON documents BEGIN
    INSERT INTO documents_fts(rowid, title, tags, body)
    VALUES (new.rowid, new.title, new.tags, new.body);
END;

CREATE TRIGGER documents_ad AFTER DELETE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, tags, body)
    VALUES ('delete', old.rowid, old.title, old.tags, old.body);
END;

CREATE TRIGGER documents_au AFTER UPDATE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, tags, body)
    VALUES ('delete', old.rowid, old.title, old.tags, old.body);
    INSERT INTO documents_fts(rowid, title, tags, body)
    VALUES (new.rowid, new.title, new.tags, new.body);
END;
"""


def insert_document(conn: sqlite3.Connection, doc: ParsedDocument, indexed_at: str) -> None:
    conn.execute(
        """
        INSERT INTO documents
            (path, layer, title, doc_type, source, tags, created, modified,
             checksum, body, meta_json, indexed_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            doc.path, doc.layer, doc.title, doc.doc_type, doc.source, doc.tags,
            doc.created, doc.modified, doc.checksum, doc.body,
            json.dumps(doc.meta, ensure_ascii=False, sort_keys=True), indexed_at,
        ),
    )
