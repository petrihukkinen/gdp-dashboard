# Workplan — Gate Status

| Gate | Name | Pass criteria | Status |
|---|---|---|---|
| 0 | Source Integrity | AMOR source material analyzed; Petri experience separated from facts; evidence register established | **CLOSED** (2026-07-11) — Q1 resolved: AMOR 2020 did not execute, see `EVIDENCE_REGISTER.md` B4 |
| 1 | Customer Problem | ≥3 material value pools with credible measurement logic | **DRAFTED, corrected** — see `04_CUSTOMER_PROBLEM/`, `05_VALUE_POOLS/`; controllability tagging corrected 2026-07-11 per Petri (Pool 1 "primarily," not "fully," provider-controlled) |
| 2 | Controllability | Attribution Matrix completed | **SUBSTANTIVELY CLOSED (Cycle 4)** — Petri set all outstanding numeric thresholds (materiality, risk corridor, SLAs); Event 6 permanently excluded; over-maintenance control and intervention netting designed and stress-tested. Only the Event 1 job-complexity catalog remains open — see `07_KPI_ATTRIBUTION/gate2_assessment.md`. |
| 3 | Commercial Viability | Revenue logic, risk caps, value validation defined; survives CFO + Red Team | **PASS WITH CONDITIONS (Cycle 5), architecture simplified (Cycle 6)** — three archetypes modelled and Checker-verified (`10_FINANCIAL_MODEL/gate3_verdict.md`), then stress-tested for operability and cut from 6 payment events to a lean core (Event 1 + Event 3-simplified + Event 4 corridor) plus an optional Turnaround Module — `06_COMMERCIAL_MODEL/cycle6_complexity_kill_test.md`. Five Cycle 5 gaps plus one new module-gaming risk remain logged in `RISK_REGISTER.md`. |
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

## Cycle 5 (this session) — completed
1. Modelled three commercial archetypes (Base Fee + KPI Fee; Base Fee + Atomic Value Share;
   Control Tower + Value Modules) against an explicitly-labeled illustrative site — full
   revenue architecture, provider economics, customer economics, and event-level detail per
   model in `10_FINANCIAL_MODEL/`.
2. Ran 8 risk-corridor stress scenarios plus MII band sensitivity (±10/15/20%) — confirmed
   the corridor structurally survives all three band widths, but exposed that per-event and
   annual painshare caps can leave a customer materially under-compensated in
   catastrophic/multi-event years (as low as 26.7% recovery in one scenario).
3. Ran both Customer and Provider CFO test suites against all three models, and a claims-
   bureaucracy burden estimate with a proposed two-tier (fast-track/full-review) claims
   process.
4. Ran 10 commercial Red Team scenarios explicitly trying to prove each model should not be
   sold — 7 resolved acceptably, 3 exposed structural gaps (claim fragmentation/damage-
   splitting, Model C's annual-cap gaming disincentive, the customer-favoring default in
   disputed claims).
5. Checker independently verified arithmetic, cap logic, event/payment mapping, cash-flow
   timing, and customer retained-value calculations — catching and disclosing a Maker
   inconsistency in Model B's gainshare-split application that changed a substantive
   conclusion (Model B does not out-earn Model A even in a high-value year at these
   illustrative settings).
6. Formal verdict: **Gate 3 — PASS WITH CONDITIONS** — `10_FINANCIAL_MODEL/gate3_verdict.md`.

## Cycle 6 (this session) — completed
1. Ran the Commercial Complexity Kill Test against the frozen Gate 2/3 architecture — event
   economic density ranking, four-gate survival test, explicit attacks on Events 1 and 3,
   Event 4 reclassification, Event 9 modularity test, three reduced architectures (X/Y/Z),
   a 15-minute CFO explainability test, a bureaucracy break-even test, and 10 commercial Red
   Team attacks on the reduced architecture — `06_COMMERCIAL_MODEL/cycle6_complexity_kill_test.md`.
2. **Killed** Event 2 as any fee mechanism and Event 3 as originally designed; **restructured**
   Event 3 into a simplified Annual Reliability Event Reward; **reclassified** Event 4 as a
   downside corridor (logic unchanged); **modularized** Events 5/9 into an optional
   Turnaround Value Module, default-off.
3. Recommended Architecture Z (Event 1 + Event 3-simplified + Event 4 core, optional
   Turnaround Module) as the Minimum Viable Commercial Architecture — ~13-15 claims/yr,
   below the ~25-40/yr bureaucracy break point, with a passing 180-word CFO pitch.
4. Checker confirmed no killed event silently re-entered through another mechanism and that
   all three monetisation engines remain intact.

## Cycle 7 (this session) — completed
1. Attacked Event 3-simplified directly — verdict **SEMANTIC REPACKAGING**; killed in every
   tested form (original, flat reward, severity-banded reward, annual pool). Reliability
   value is now managed/reported only, never monetized.
2. **Structural consequence:** Architecture X and Z's cores are now identical (Event 1 +
   Event 4). X is not an entry-tier discount of Z — it is a complete, permanent offering.
3. Hardened Event 1 against baseline-inflation, labour-substitution, rate-vs-productivity
   conflation, and job-mix manipulation; retested against the four gates — still passes, at
   a disclosed higher administrative cost, now as the sole core upside mechanism.
4. Sized the Causal Connection Map (€2-11.25m initial build at large-site scale) — strong
   supporting evidence for the kill decision; recommended building nothing for now.
5. Designed the Turnaround Module anti-selection rule (site-wide, minimum-term, pre-scope-
   freeze activation).
6. Engaged the "complicated bonus scheme" objection directly — honest, narrower commercial
   differentiation claim written; banned claims identified (must not claim to monetize
   reliability).
7. Reframed catastrophic Event 4 losses as a legal liability/indemnity matter, structurally
   separate from the performance corridor — Cycle 5's 26.7%-recovery finding was a category
   error, not a corridor flaw.
8. **Final recommended Minimum Viable Commercial Architecture: Event 1 + Event 4 core, plus
   an optional Turnaround Value Module for TA-intensive customers meeting a 5-condition
   readiness gate. Nothing else is monetized.**

## Cycle 8 (this session) — completed
1. Attempted to kill Event 1, the last core payment event. **Verdict: RECLASSIFY, not kill.**
   A 10-year persistence model proved the "perpetual share of a frozen baseline" design
   indefensible (€4.48m over 8 years for one Year-2 action, illustrative); redesigned as a
   time-limited savings share on a rolling-baseline-plus-cohort architecture.
2. Confirmed savings-pool exhaustion is real and structural, not a flaw — addressed via
   pricing/duration design (harvest proven gains into Base Fee over time), not a new event.
3. Sized Event 1's administration cost for the first time (€30k-€1m/yr by scale); found a
   commercially absurd 12-24% ratio for smaller customers in steady-state years; designed a
   five-condition evidence-based eligibility gate in response.
4. Concluded Event 1 must not be underwritten as guaranteed provider revenue.
5. Narrowed the Cycle 7 differentiation claim — withdrew "for the life of the deal" and
   "exceeds standard maintenance-contract terms" as unsupported; a real, narrower claim
   survives.
6. Tested and confirmed: Event 4, not Event 1, is what prevents AMOR from regressing to
   "Better Managed Maintenance." **Final settled core: Base-Fee-funded Control Tower + Event
   4 downside corridor, complete on its own. Contractor Productivity Value Module (Event 1)
   and Turnaround Value Module (Events 5+9) are both optional and customer-specific.**
7. Designed (not conducted) an external stakeholder validation test — 3 interview scripts,
   pass/fail signals, and an explicit finding that would force Event 1's full kill.
8. Wrote a commercial-to-legal drafting brief for the Event 4 catastrophic-loss/liability
   boundary, for external counsel — no final legal language drafted.
9. Retired the Cycle 6 X/Z architecture naming per Petri's decision — one core architecture,
   optional modules, not a maturity ladder.

## Cycle 9 (this session) — completed
1. Built the Falsification Register — 10 ranked assumptions that could kill or damage the
   architecture, each with evidence available/missing and explicit support/weaken/kill
   answer definitions (`18_INTERVIEW_QA/FALSIFICATION_REGISTER.md`).
2. Built three problem-first (not sales-first) validation protocols for customer CFO,
   customer asset/site director, and provider CFO/CEO, each question mapped to a
   falsification hypothesis with predefined signals.
3. Attacked the Base-Fee-funded packaging assumption with 5 alternative commercial
   structures — no winner selected (`06_COMMERCIAL_MODEL/WTP_PACKAGING_TEST.md`).
4. Built the strongest case against Control Tower differentiation — verdict UNRESOLVED
   (`03_STRATEGIC_THESIS/DIFFERENTIATION_FALSIFICATION.md`).
5. Mapped Petri's direct experience against every architecture element — found the two most
   load-bearing elements (Event 4, Control Tower Economics) are new hypotheses, not proven
   by direct experience (`PETRI_ARCHITECTURE_EVIDENCE_MAP.md`).
6. Wrote CEO conversation boundaries (5 safe claims, 5 not-yet claims, 3 validation
   questions) and a predefined validation scorecard locking scoring criteria before any
   interview occurs (`CEO_CONVERSATION_BOUNDARIES.md`, `18_INTERVIEW_QA/VALIDATION_SCORECARD.md`).
7. **No interviews conducted. No external validation has occurred.**

## Strategic Reframe Challenge (between Cycles 9 and 10) — completed
Tested whether the Control Tower should be a separately monetized product versus the
operating system enabling broader-scope, longer-duration, single-accountable relationships.
Verdict: the latter is stronger, consistent with AMOR 2020's own actual deal logic. Renamed
the "Accountability Premium" working hypothesis to avoid assuming a price premium exists.

## Cycle 10 (this session) — completed: Gate 3A
1. Built the Accountability Economics Tree — Account Lifetime Value logic from first
   principles (`10_FINANCIAL_MODEL/ACCOUNTABILITY_ECONOMICS_TREE.md`).
2. Tested five economic mechanisms (scope, duration, retention, pull-through, margin
   efficiency) individually against economic logic, risk, and kill conditions
   (`10_FINANCIAL_MODEL/FIVE_ECONOMIC_MECHANISMS.md`).
3. Built the Accountability Boundary — six distinct accountability types, with Asset Owner,
   Statutory, and Production accountability explicitly non-delegable to the provider
   (`03_STRATEGIC_THESIS/ACCOUNTABILITY_BOUNDARY.md`).
4. Rewrote all three Cycle 9 validation protocols in place around scope/duration/
   accountability economics, retiring the "separate fee" framing entirely.
5. Built the Earned Retention Protocol (customer data ownership, portability, documentation,
   transition assistance — found net positive for provider economics, not a cost) and the
   Pull-Through Conflict Protocol (tiered safeguards against the recommendation/sales agency
   problem).
6. Built an illustrative Account Lifetime Value sensitivity model — found Control Tower
   operating cost, not renewal probability or pull-through, is the single most sensitive
   variable in the entire thesis (`10_FINANCIAL_MODEL/ACCOUNT_LIFETIME_VALUE_MODEL.md` +
   companion CSV).
7. Ran a 12-point Red Team against "broader accountability creates superior account
   lifetime economics" — thesis survives as coherent, not as proven.
8. Built the Systematic Capability Map — no item qualifies as a proven moat; the two
   genuine moat candidates (Control Tower replicability at scale, cross-site performance
   data) require multi-site evidence this project cannot generate.
9. **Gate 3A — Accountability Economics Logic: PASS WITH CONDITIONS.**

## Proposed Cycle 11
1. Conduct the actual external stakeholder interviews using the **revised Cycle 10**
   protocols — the real next step, not further internal design work.
2. Complete the Validation Scorecard against real responses once interviews occur,
   prioritizing the scope-consolidation and duration-appetite questions as the single most
   important test.
3. Engage external legal counsel with the Cycle 8 drafting brief for the Event 4 liability
   boundary.
4. Investigate real Control Tower delivery cost data — the model's single most sensitive,
   least-evidenced variable — through any means available short of fabrication.
5. Only after real evidence exists: calibrate real numbers and revisit Cycle 5's Model B/C.
6. Do not build the executive deck until Falsification Register items #1-5 and the Gate 3A
   scope/duration hypothesis have at least PARTIALLY SUPPORTED ratings.
