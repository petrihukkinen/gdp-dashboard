# Workplan — Gate Status

| Gate | Name | Pass criteria | Status |
|---|---|---|---|
| 0 | Source Integrity | AMOR source material analyzed; Petri experience separated from facts; evidence register established | **CLOSED** (2026-07-11) — Q1 resolved: AMOR 2020 did not execute, see `EVIDENCE_REGISTER.md` B4 |
| 1 | Customer Problem | ≥3 material value pools with credible measurement logic | **DRAFTED, corrected** — see `04_CUSTOMER_PROBLEM/`, `05_VALUE_POOLS/`; controllability tagging corrected 2026-07-11 per Petri (Pool 1 "primarily," not "fully," provider-controlled) |
| 2 | Controllability | Attribution Matrix completed | **SUBSTANTIVELY CLOSED (Cycle 4)** — Petri set all outstanding numeric thresholds (materiality, risk corridor, SLAs); Event 6 permanently excluded; over-maintenance control and intervention netting designed and stress-tested. Only the Event 1 job-complexity catalog remains open — see `07_KPI_ATTRIBUTION/gate2_assessment.md`. |
| 3 | Commercial Viability | Revenue logic, risk caps, value validation defined; survives CFO + Red Team | **READY TO START (PASS WITH CONDITIONS on entry, per `07_KPI_ATTRIBUTION/gate3_readiness_assessment.md`)** — architecture recommendation (destination: Selective Outcome-Based Platform; entry: Asset Performance Partnership; see `03_STRATEGIC_THESIS/business_model_options.md`) plus a stress-tested attribution/payment-eligibility foundation now exist. Six parallel-track gaps remain open (causal-connection map, Event 9 benchmark provider, uncalibrated control bands, netting window length, two materiality-extension confirmations, undesigned advisory/transformation fee structure) but do not block starting. |
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

## Cycle 3 (this session) — completed
1. Full Checker/Red Team stress test of the attribution architecture: per-event 12-point
   structured challenge (`07_KPI_ATTRIBUTION/event_stress_test.md`), Customer CFO attack,
   Operations Executive attack, Contract Lawyer attack (all in `07_KPI_ATTRIBUTION/`),
   Provider CFO risk-corridor design (`06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`), a
   double-counting map, a counterfactual evidence protocol, a minimum-viable Value
   Validation Board design (`08_OPERATING_MODEL/VALUE_VALIDATION_BOARD_MVP.md`), and 10 Red
   Team dispute scenarios.
2. Formal Gate 2 verdict: **PASS WITH CONDITIONS** — see `07_KPI_ATTRIBUTION/gate2_assessment.md`.
3. Two new, unresolved design gaps surfaced and logged (not fixed): repair-creates-new-risk
   netting, and over-maintenance-as-KPI-protection ("KPI gaming"). Both added to
   `RISK_REGISTER.md`.
4. Event 6 (lifecycle Capex deferral) provisionally excluded from the near-term
   payment-KPI shortlist due to an unresolved structural conflict of interest.

## Cycle 4 (this session) — completed
1. Petri set all outstanding numeric decisions: materiality threshold (€100,000 / 0.25%
   ACV), risk corridor figures (±5% deadband, 20%/10% asymmetric gainshare/painshare caps,
   50% per-event cap, zero floor, no carry-forward, 24-month clawback), SLA modelling
   defaults (48h permit, 24h production access), and confirmed Event 6's permanent exclusion
   from the payment-KPI set.
2. Designed and stress-tested the over-maintenance/KPI-gaming control
   (`07_KPI_ATTRIBUTION/overmaintenance_control.md`) and the intervention netting mechanism
   (`07_KPI_ATTRIBUTION/intervention_netting.md`) — the two surviving Cycle 3 Red Team gaps.
3. Revised the Event 4 decision tree to v3, incorporating the materiality gate, netting
   interaction, SLA-driven exclusion, and over-maintenance context
   (`07_KPI_ATTRIBUTION/event4_decision_tree_v3.md`).
4. Designed new Event 9 (Turnaround Execution Efficiency), distinct from Event 5, built from
   the outset with an independent joint-benchmark requirement to avoid Event 6's
   conflict-of-interest failure mode (`07_KPI_ATTRIBUTION/event9_turnaround_execution_efficiency.md`).
5. Consolidated payment eligibility around the three monetisation engines (productivity/
   verified cost saving, reliability/performance fee, strategic asset/advisory fee) —
   `07_KPI_ATTRIBUTION/payment_eligibility_logic.md`.
6. Ran 5 additional Red Team scenarios (11-15) against the new mechanisms —
   `07_KPI_ATTRIBUTION/cycle4_red_team_scenarios.md`. 3 resolved cleanly, 2 exposed further
   (logged, not fixed) gaps.
7. Formal verdict: **Gate 3 readiness — PASS WITH CONDITIONS** —
   `07_KPI_ATTRIBUTION/gate3_readiness_assessment.md`.

## Proposed Cycle 5
1. Begin Gate 3 commercial modelling proper (Base Fee levels, Phase 0-4 staging, Control
   Tower fee/margin sizing per `03_STRATEGIC_THESIS/control_tower_economics.md`) using the
   Cycle 4 architecture as its foundation.
2. Design the advisory/transformation fee structure for strategic asset value (replacing
   Event 6) as an early Gate 3 workstream, not an afterthought — it now carries that entire
   monetisation engine alone.
3. In parallel, close the six remaining Cycle 4 gaps: causal-connection map, Event 9
   independent benchmark provider selection, MII/RRE band calibration, netting observation
   window confirmation, and the two proposed materiality-extension interpretations (Event 1
   periodic claims; sub-threshold secondary/netted issues) — all require Petri/commercial
   confirmation, not further architecture work.
4. Build the job-complexity-normalized catalog for Event 1 — the one item still blocking
   full Gate 2 closure.
