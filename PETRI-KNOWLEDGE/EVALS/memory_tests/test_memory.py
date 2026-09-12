"""Phase 1 memory evaluation suite.

These are REAL tests against a real (synthetic) fixture corpus and a real
SQLite index built by the actual build_index.py / search.py scripts —
not a mock, and no result here is fabricated. Run with:

    python3 -m pytest PETRI-KNOWLEDGE/EVALS/memory_tests -v

Each test function maps to one of the required eval categories from the
Phase 1 task (see the docstring above each test). Two extra tests check
the architecture's own structural guarantees: that the index is fully
disposable/rebuildable, and that indexing never mutates RAW evidence.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

import build_index
import search as search_mod

FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture()
def index_db(tmp_path) -> Path:
    db_path = tmp_path / "jarvis-test.sqlite"
    report = build_index.rebuild(FIXTURES, db_path)
    assert not report.errors, f"fixture corpus failed to parse: {report.errors}"
    return db_path


def _paths(results: list[dict]) -> list[str]:
    return [r["path"] for r in results]


# ---------------------------------------------------------------------------
# 1. Exact factual recall
# ---------------------------------------------------------------------------
def test_exact_factual_recall(index_db):
    """A specific fact stated exactly once must be found exactly once."""
    results = search_mod.search(index_db, "Petri Hukkinen", layer="KNOWLEDGE")
    assert _paths(results) == ["KNOWLEDGE/dec-2026-002-budget.md"]


# ---------------------------------------------------------------------------
# 2. Finding a fact recorded in a different document than a naive keyword
#    match might land on
# ---------------------------------------------------------------------------
def test_fact_ranked_above_incidental_mention(index_db):
    """Both the real budget decision and an unrelated task mention
    'Aurora' and 'budjetti'. The decision's title also says 'budjetti';
    the task's title does not. Title-weighted ranking must put the
    decision first."""
    results = search_mod.search(index_db, "Aurora budjetti", layer="KNOWLEDGE")
    assert results, "expected at least one match"
    assert results[0]["path"] == "KNOWLEDGE/dec-2026-002-budget.md"


# ---------------------------------------------------------------------------
# 3. Temporal / latest-information selection
# ---------------------------------------------------------------------------
def test_temporal_latest_information_selection(index_db):
    """Both the current and the superseded hosting decision match a
    generic query. Phase 1 search does not itself resolve "which is
    current" (that is a non-goal — see README) but every result must
    carry enough metadata (created date, status) for the caller to do so.
    """
    results = search_mod.search(index_db, "Aurora hosting", layer="KNOWLEDGE")
    assert set(_paths(results)) == {
        "KNOWLEDGE/dec-2026-001-hosting.md",
        "KNOWLEDGE/dec-2025-001-hosting-old.md",
    }
    by_path = {r["path"]: r for r in results}
    current = by_path["KNOWLEDGE/dec-2026-001-hosting.md"]
    old = by_path["KNOWLEDGE/dec-2025-001-hosting-old.md"]
    assert current["created"] > old["created"]
    assert current["meta"]["status"] == "current"


# ---------------------------------------------------------------------------
# 4. Provenance / source identification
# ---------------------------------------------------------------------------
def test_provenance_source_identification(index_db):
    """The current hosting decision must point at real RAW evidence, and
    that evidence file must actually exist (no dangling citation)."""
    results = search_mod.search(index_db, "AWS hosting", layer="KNOWLEDGE")
    assert _paths(results) == ["KNOWLEDGE/dec-2026-001-hosting.md"]
    source = results[0]["source"]
    assert source == "RAW/evidence-hosting-email.md"
    assert (FIXTURES / source).is_file()


# ---------------------------------------------------------------------------
# 5. Stale vs. current information
# ---------------------------------------------------------------------------
def test_stale_vs_current_metadata(index_db):
    """The superseded decision must be clearly marked as such, including
    a pointer to what replaced it — this is what lets a consumer avoid
    treating stale information as current."""
    results = search_mod.search(index_db, "Azure hosting", layer="KNOWLEDGE")
    assert _paths(results) == ["KNOWLEDGE/dec-2025-001-hosting-old.md"]
    meta = results[0]["meta"]
    assert meta["status"] == "superseded"
    assert meta["superseded_by"] == "dec-2026-001-hosting"


# ---------------------------------------------------------------------------
# 6. Irrelevant-context resistance
# ---------------------------------------------------------------------------
def test_irrelevant_context_resistance(index_db):
    """A document that shares only the generic word 'Aurora' — not the
    distinctive term 'budjetti' — must not appear for a query that names
    both."""
    results = search_mod.search(index_db, "Aurora budjetti", layer="KNOWLEDGE")
    assert "KNOWLEDGE/fact-2026-001-team.md" not in _paths(results)


# ---------------------------------------------------------------------------
# 7. No-result / insufficient-evidence behaviour
# ---------------------------------------------------------------------------
def test_no_result_when_nothing_matches(index_db):
    """A query about something absent from the corpus must return an
    empty result set, never a fabricated best guess."""
    results = search_mod.search(index_db, "kvanttitietokone")
    assert results == []


def test_cli_reports_no_results_without_crashing(index_db, capsys):
    exit_code = search_mod.main(["kvanttitietokone", "--db", str(index_db)])
    assert exit_code == 0
    assert "No results found." in capsys.readouterr().out


# ---------------------------------------------------------------------------
# Structural guarantees (RAW preservation, index disposability)
# ---------------------------------------------------------------------------
def test_raw_evidence_is_never_modified_by_indexing(tmp_path):
    raw_dir = FIXTURES / "RAW"
    before = {
        p: hashlib.sha256(p.read_bytes()).hexdigest() for p in raw_dir.rglob("*.md")
    }

    build_index.rebuild(FIXTURES, tmp_path / "jarvis-test.sqlite")

    after = {
        p: hashlib.sha256(p.read_bytes()).hexdigest() for p in raw_dir.rglob("*.md")
    }
    assert before == after
    assert before, "sanity check: fixture RAW/ must not be empty"


def test_index_is_disposable_and_rebuildable(tmp_path):
    """Deleting jarvis.sqlite and rebuilding it must reproduce exactly
    the same rows — the index carries no information the source files
    don't already have."""
    db_path = tmp_path / "jarvis-test.sqlite"

    build_index.rebuild(FIXTURES, db_path)
    first = search_mod.search(db_path, "Aurora", layer="KNOWLEDGE", limit=50)

    db_path.unlink()
    assert not db_path.exists()

    build_index.rebuild(FIXTURES, db_path)
    second = search_mod.search(db_path, "Aurora", layer="KNOWLEDGE", limit=50)

    key = lambda rows: sorted(json.dumps(r, sort_keys=True) for r in rows)
    assert key(first) == key(second)
    assert first, "sanity check: query must actually match fixture content"
