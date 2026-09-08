# DU research audit & Bilfinger Performance Outsourcing prototype (branch `claude/du-research-bilfinger-audit-8l1xov`)

Run date 2026-09-08. This section documents the computational audit of Suntola (2026, DOI 10.3389/fspas.2026.1827522) and the
synthetic Bilfinger prototype. The original GDP-dashboard template README is preserved below unchanged.

**Headline constraint:** the article itself (Frontiers HTML/PDF), arXiv and physicsfoundations.org were egress-blocked in this
environment; see `sources/manifest.csv`. Claims tied to the article's equations are CONDITIONAL / NOT TESTED accordingly. Update 2: article statements on Eq. 32 and the
Pantheon conversion, plus Freire+2012 / Liu+2026 numbers, were supplied externally (provenance marked EXTERNALLY SUPPLIED in
`sources/manifest.csv`) and the decisive tests were run on them.

## Layout
```
sources/manifest.csv          every source: author, title, URL/DOI, date, version, retrieved, page/eq, access, SHA-256, status
sources/fetch_sources.sh      re-download of the public Pantheon+ files (the 33 MB covariance is not committed; SHA-256 recorded)
claims/claim_register.csv     24 claims: id, category, assumptions, derivation, prediction, observable, test file, status, bounded conclusion
src/du_symbolic_checks.py     A2.1/2/4/6 + A4 construction (expansion branch, S^3 kernels, alpha, process rates, L-A vs L-B models)
src/binary_decay.py           GR Peters–Mathews (two implementations), J1738+0333 / B1913+16 / J0737-3039, e->0 constraint
src/pantheon_fit.py           Pantheon+ replication (flat & open LCDM) + DU magnitude family + candidates C1/C2 + prediction test
src/pantheon_common.py        shared loader / profiled-chi2 likelihood
src/pantheon_decisive_test.py TASK A: p=0.5 / implied p=1.5 / free p / flat LCDM, same data & likelihood; residuals; train/test
src/binary_decay_tiers.py     TASK B: DU-32-ONLY limiting bound + DU-PLUS-QUADRUPOLE two-component fit (J1738 Tier-1)
src/falsification_matrix.py   TASK C: results/falsification_matrix.csv
src/po_decision_engine.py     TASK D: 12-layer decision engine, gate mapping, BTS requirements matrix (CSV)
src/pantheon_robustness.py    verification round: absolute fit, conditional held-out, bias/selection sensitivity
src/binary_decay_sensitivity.py verification round: provenance tiers, stepwise J1738 bound, two-component fit sensitivity
src/kcorrection_audit.py      Hogg K-correction from definitions: K independent of the dilution distance
src/local_expansion_and_bh.py H0*r observables under DU scalings, LLR injection–recovery, GR ISCO/Kerr reference
src/bilfinger_prototype.py    SYNTHETIC state-space prototype, 3 policies, Monte Carlo, 9 stress tests, value accounting
src/bilfinger_gates.py        E2E gate definitions and KPI observation model (CSV)
tests/test_du_checks.py       code-correctness tests (not physics-validity tests)
tests/review_consistency.py   report-vs-results number cross-check (independent reviewer role)
results/                      machine outputs (json/csv/png) + run_manifest.json
reports/DU_AUDIT_FI.md  DU_RESEARCH_RESULT.md  BILFINGER_MODEL_FI.md  EXECUTIVE_BRIEF_FI.md  OPEN_LOOPS.csv
requirements-du.txt           pinned versions used in this run
```

## Reproduce
```
pip install -r requirements-du.txt
bash sources/fetch_sources.sh            # Pantheon+SH0ES.dat (committed) + STAT+SYS covariance (33 MB, downloaded)
python src/du_symbolic_checks.py
python src/binary_decay.py
PYTHONPATH=src python src/binary_decay_tiers.py
python src/pantheon_fit.py               # ~7 s
PYTHONPATH=src python src/pantheon_decisive_test.py
python src/kcorrection_audit.py
python src/local_expansion_and_bh.py
python src/bilfinger_prototype.py
python src/bilfinger_gates.py
PYTHONPATH=src python src/pantheon_robustness.py
PYTHONPATH=src python src/binary_decay_sensitivity.py
python src/falsification_matrix.py
python src/po_decision_engine.py
python -m pytest -q tests
python tests/review_consistency.py
```
Random seeds are fixed (20260908). No run exceeds one minute; no download exceeds 35 MB.

## Status vocabulary
TOISTETTU (reproduced) / RISTIRIITA (contradiction) / EHDOLLINEN (conditional) / EI YKSILÖIDY (not identified) / EI TESTATTU (not tested).
"Reproduced" refers to a named calculation, never to the theory as a whole. Code-correctness tests and observational tests of a
physical claim are different things; no prediction was altered after the fact to make a report green.

---

# :earth_americas: GDP dashboard template

A simple Streamlit app showing the GDP of different countries in the world.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gdp-dashboard-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
