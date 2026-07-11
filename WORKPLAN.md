# Workplan — Gate Status

| Gate | Name | Pass criteria | Status |
|---|---|---|---|
| 0 | Source Integrity | AMOR source material analyzed; Petri experience separated from facts; evidence register established | **CLOSED** (2026-07-11) — Q1 resolved: AMOR 2020 did not execute, see `EVIDENCE_REGISTER.md` B4 |
| 1 | Customer Problem | ≥3 material value pools with credible measurement logic | **DRAFTED, corrected** — see `04_CUSTOMER_PROBLEM/`, `05_VALUE_POOLS/`; controllability tagging corrected 2026-07-11 per Petri (Pool 1 "primarily," not "fully," provider-controlled) |
| 2 | Controllability | Attribution Matrix completed | **IN PROGRESS (Cycle 2)** — first-pass atomic value-event architecture drafted, see `07_KPI_ATTRIBUTION/attribution_architecture.md`. Not yet Checker/Red-Team-hardened to gate-closing standard. |
| 3 | Commercial Viability | Revenue logic, risk caps, value validation defined; survives CFO + Red Team | NOT STARTED — revised architecture recommendation drafted this cycle (destination: Selective Outcome-Based Platform; entry: Asset Performance Partnership; see `03_STRATEGIC_THESIS/business_model_options.md`), not yet stress-tested to gate standard |
| 4 | Operating Model | Governance, RACI, Asset Performance Office architecture | NOT STARTED |
| 5 | Scale | Standard core vs. configurable modules separated | NOT STARTED |
| 6 | Executive Narrative | Strategy explainable in 10 minutes, no technical detail | NOT STARTED |
| 7 | Executive Deck | 10-12 slide CEO deck | **BLOCKED — do not start before Gate 3 passes** |
| 8 | Pilot | First customer pilot architecture | NOT STARTED |
| 9 | 100-Day Plan | Execution roadmap | NOT STARTED |

## Cycle 1 (this session) — completed
1. Inspected project directory (found no prior AMOR material; flagged to Petri).
2. Received and read the genuine 2020 AMOR source PDF in full.
3. Reconstructed the AMOR 2020 business model — `02_AMOR_ORIGINAL/AMOR_2020_ANALYSIS.md`.
4. Identified 10 strongest principles, 10 outdated assumptions, 10 major commercial risks,
   10 ideas worth carrying forward.
5. Built the AMOR 2020 → AMOR 2030 logic bridge.
6. Built first Customer Problem Tree — `04_CUSTOMER_PROBLEM/customer_problem_tree.md`.
7. Built first Value Pool Tree — `05_VALUE_POOLS/value_pool_tree.md`.
8. Drafted three alternative business model architectures —
   `03_STRATEGIC_THESIS/business_model_options.md`.
9. Ran Checker review — `03_STRATEGIC_THESIS/checker_review.md`.
10. Ran Red Team review — `03_STRATEGIC_THESIS/red_team_review.md`.
11. Recommendation delivered to Petri (see chat output, Cycle 1).

## Cycle 2 (this session) — completed
1. Logged Petri's direct answers to all 10 Cycle 1 questions into governance files
   (`EVIDENCE_REGISTER.md`, `ASSUMPTIONS.md`, `OPEN_QUESTIONS.md`, `DECISION_LOG.md`,
   `PROJECT_CONTEXT.md`, `PETRI_EXPERIENCE.md`, `HYPOTHESIS_REGISTER.md`).
2. Corrected the Cycle 1 overreach on AMOR 2020 evidence scope, and formally logged the
   AMOR (Level A) + ABB (Level B) evidentiary combination as the project's actual core case.
3. Corrected contractor-management controllability tagging from "fully" to "primarily
   provider-controlled, with defined customer dependencies" across `05_VALUE_POOLS/` and
   added the corresponding painshare-exposure risk to `RISK_REGISTER.md`.
4. Adopted and documented "Control Tower Economics" as a core design principle —
   `03_STRATEGIC_THESIS/control_tower_economics.md`.
5. Revised the business model recommendation: destination = Selective Outcome-Based Asset
   Performance Platform; entry = Asset Performance Partnership; path = Managed
   Transformation → Asset Performance Partnership → Selective Outcome-Based Modules — see
   `03_STRATEGIC_THESIS/business_model_options.md`.
6. Built the first-pass Performance Attribution Architecture from atomic, loss-event-level
   value events (not total OEE) — `07_KPI_ATTRIBUTION/attribution_architecture.md` —
   including a worked example of the adopted Identified Value × Controllability ×
   Realization Probability × Time-to-Impact = Committable Value formula.

## Proposed Cycle 3
1. Checker + full Red Team pass on `07_KPI_ATTRIBUTION/attribution_architecture.md` — this
   cycle's version is a Maker-only first pass (see its addendum).
2. Design the Value Validation Board's actual adjudication process (needed for attribution
   Events 3-6 and for Gate 4 Operating Model work).
3. Build the customer-dependency carve-out clause template flagged in `RISK_REGISTER.md`.
4. Begin Gate 3 commercial modelling using the corrected, event-level attribution
   architecture as its foundation — not before, since a commercial model without attribution
   is not fundable.
5. Size what a Control Tower fee/margin actually looks like commercially — flagged, not yet
   done, in `03_STRATEGIC_THESIS/control_tower_economics.md`.
