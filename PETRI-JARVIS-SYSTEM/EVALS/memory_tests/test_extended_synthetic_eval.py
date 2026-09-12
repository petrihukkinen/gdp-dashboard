"""Phase 1.1 hardening: extended synthetic-but-realistic evaluation.

No real Petri Jarvis knowledge was available to test against in this
session — checked via list_repos: no separate PETRI-KNOWLEDGE or
PETRI-JARVIS-SYSTEM repository exists yet. This corpus (see
fixtures_extended/) is a larger, domain-representative but entirely
fabricated stand-in (investment/broker decisions, a startup cap table, a
shareholder-agreement note), used to MEASURE — not speculate about — how
Phase 1's literal FTS5 search behaves on Finnish text, including inflected
word forms, beyond what the minimal fixtures/ corpus exercises.

Every assertion below reflects an actually-observed result from running
these queries against the actual build_index.py / search.py — including
the ones documented as *expected failures* (Finnish morphology gaps).
Encoding a known gap as a passing assertion on the *current* behavior
means a future change to that behavior is a deliberate, visible decision
instead of a silent regression.

Run with:
    python3 -m pytest PETRI-JARVIS-SYSTEM/EVALS/memory_tests -v
"""
from __future__ import annotations

from pathlib import Path

import pytest

import build_index
import search as search_mod

FIXTURES = Path(__file__).resolve().parent / "fixtures_extended"


@pytest.fixture()
def index_db(tmp_path) -> Path:
    db_path = tmp_path / "jarvis-extended-test.sqlite"
    report = build_index.rebuild(FIXTURES, db_path)
    assert not report.errors, f"fixture corpus failed to parse: {report.errors}"
    return db_path


def _paths(results: list[dict]) -> list[str]:
    return [r["path"] for r in results]


def _q(index_db, query: str, **kw) -> list[dict]:
    return search_mod.search(index_db, query, layer="KNOWLEDGE", **kw)


# ---------------------------------------------------------------------------
# Exact factual recall
# ---------------------------------------------------------------------------
def test_exact_recall_unique_name(index_db):
    results = _q(index_db, "Petri Hukkisen omistusosuus")
    assert _paths(results) == ["KNOWLEDGE/dec-2026-011-cap-table.md"]


# ---------------------------------------------------------------------------
# Cross-document retrieval: two documents share "cap table", only one
# is the actual authoritative decision — title-weighted ranking must
# still surface it first.
# ---------------------------------------------------------------------------
def test_cross_document_retrieval_ranks_authoritative_doc_first(index_db):
    results = _q(index_db, "cap table Series A")
    assert results, "expected at least one match"
    assert results[0]["path"] == "KNOWLEDGE/dec-2026-011-cap-table.md"
    # the distractor task must still be found (it does mention cap table),
    # just not ranked first
    assert "KNOWLEDGE/task-2026-006-cap-table-paivitys.md" in _paths(results)


# ---------------------------------------------------------------------------
# Current vs. stale fact
# ---------------------------------------------------------------------------
def test_current_vs_stale_broker_decision(index_db):
    results = _q(index_db, "sijoitussalkun välittäjä")
    assert set(_paths(results)) == {
        "KNOWLEDGE/dec-2026-010-valittaja.md",
        "KNOWLEDGE/dec-2025-005-valittaja-vanha.md",
    }
    by_path = {r["path"]: r for r in results}
    current = by_path["KNOWLEDGE/dec-2026-010-valittaja.md"]
    old = by_path["KNOWLEDGE/dec-2025-005-valittaja-vanha.md"]
    assert current["meta"]["status"] == "current"
    assert old["meta"]["status"] == "superseded"
    assert old["meta"]["superseded_by"] == "dec-2026-010-valittaja"


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------
def test_provenance_points_to_real_raw_file(index_db):
    results = _q(index_db, "Interactive Brokers")
    assert _paths(results) == ["KNOWLEDGE/dec-2026-010-valittaja.md"]
    source = results[0]["source"]
    assert source == "RAW/broker-vertailu-2026-03.md"
    assert (FIXTURES / source).is_file()


# ---------------------------------------------------------------------------
# Irrelevant-context resistance
# ---------------------------------------------------------------------------
def test_irrelevant_context_resistance(index_db):
    results = _q(index_db, "sijoitussalkku Interactive Brokers")
    assert "KNOWLEDGE/fact-2026-010-elakesuunnitelma.md" not in _paths(results)


# ---------------------------------------------------------------------------
# Insufficient evidence
# ---------------------------------------------------------------------------
def test_no_result_for_absent_topic(index_db):
    assert _q(index_db, "kryptovaluutta") == []


# ---------------------------------------------------------------------------
# A working, unremarkable Finnish query (baseline: literal match on the
# exact form used in a title)
# ---------------------------------------------------------------------------
def test_finnish_task_retrieval_via_title(index_db):
    results = _q(index_db, "veroilmoitus lähdevero")
    assert _paths(results) == ["KNOWLEDGE/task-2026-005-veroilmoitus.md"]


# ---------------------------------------------------------------------------
# Finnish inflected word forms — MEASURED, not speculated.
#
# "välittäjä" (nominative) appears in dec-2026-010's TITLE.
# "välittäjän" (genitive) appears in its BODY.
# "välittäjää" (partitive) and "välittäjästä" (elative) appear NOWHERE.
#
# FTS5's unicode61 tokenizer does no stemming: each inflected form is a
# distinct token. The finding is not "Finnish fails" — it is "any word
# form that was actually written down, in any case, is findable; other
# inflections of the same word are invisible unless they also appear
# somewhere verbatim."
# ---------------------------------------------------------------------------
def test_finnish_inflection_nominative_form_present_matches(index_db):
    results = _q(index_db, "välittäjä")
    assert "KNOWLEDGE/dec-2026-010-valittaja.md" in _paths(results)


def test_finnish_inflection_genitive_form_present_matches(index_db):
    results = _q(index_db, "välittäjän")
    assert "KNOWLEDGE/dec-2026-010-valittaja.md" in _paths(results)


def test_finnish_inflection_partitive_form_absent_does_not_match(index_db):
    """KNOWN LIMITATION, measured: 'välittäjää' (partitive) never appears
    verbatim in the corpus, so it does not match even though the same
    word in other cases does. Acceptable at Phase 1 scale (see final
    report) — not fixed here; no stemming/semantic search added."""
    assert _q(index_db, "välittäjää") == []


def test_finnish_inflection_elative_form_absent_does_not_match(index_db):
    """Same limitation, a different absent case form ('välittäjästä')."""
    assert _q(index_db, "välittäjästä") == []


def test_finnish_inflection_illative_form_present_matches(index_db):
    """'osakassopimukseen' (illative) appears verbatim in
    dec-2026-012's body."""
    results = _q(index_db, "osakassopimukseen")
    assert "KNOWLEDGE/dec-2026-012-sha-paatos.md" in _paths(results)


def test_finnish_inflection_nominative_form_via_title_matches(index_db):
    """'osakassopimus' (nominative) appears verbatim in
    dec-2026-012's title, not its body — still findable because it was
    written down somewhere, in some form."""
    results = _q(index_db, "osakassopimus")
    assert "KNOWLEDGE/dec-2026-012-sha-paatos.md" in _paths(results)


def test_finnish_inflection_elative_form_absent_does_not_match_2(index_db):
    """KNOWN LIMITATION, measured: 'osakassopimuksesta' (elative) never
    appears verbatim anywhere in the corpus."""
    assert _q(index_db, "osakassopimuksesta") == []


# ---------------------------------------------------------------------------
# The same literal-token limitation, shown on an English loanword with a
# Finnish case suffix attached — demonstrates this is a general property
# of FTS5 literal tokenization, not something specific to Finnish roots.
# ---------------------------------------------------------------------------
def test_code_switched_base_form_matches(index_db):
    """'cap table rakenne' (base forms, as written) matches."""
    results = _q(index_db, "cap table rakenne")
    assert "KNOWLEDGE/dec-2026-011-cap-table.md" in _paths(results)


def test_code_switched_inflected_form_does_not_match(index_db):
    """KNOWN LIMITATION, measured: 'cap tablen rakenne' — a plausible way
    a person might actually type it in Finnish, with the Finnish genitive
    suffix '-n' attached to the English loanword 'table' — does not
    match, because 'tablen' and 'table' are different literal tokens."""
    assert _q(index_db, "cap tablen rakenne") == []
