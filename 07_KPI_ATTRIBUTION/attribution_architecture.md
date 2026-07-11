# Performance Attribution Architecture — Cycle 2 Draft (Gate 2)

Status: **Superseded in part by Cycle 3.** This document is the original Maker pass. The
full Checker/Red Team stress test has since been completed — see
`07_KPI_ATTRIBUTION/event_stress_test.md` (per-event 12-point review with KEEP/MODIFY/
DOWNGRADE/REMOVE verdicts) and `07_KPI_ATTRIBUTION/gate2_assessment.md` (formal Gate 2
verdict: PASS WITH CONDITIONS). Read this document for the original design rationale; read
those two for the current, stress-tested status of each event. In summary: Event 2 is now
KPI-fee-only (not gainshare as this draft's table implies), Event 6 is provisionally
excluded from the near-term payment-KPI set, and Events 1, 3, 4 carry materially more
detailed attribution rules than shown below.

## The design instruction (Petri, 2026-07-11)

> "Do not design attribution around total OEE. Start from loss-event classification and
> provider controllability."

And the central question this document exists to answer:

> "What is the smallest unit of industrial value that can be objectively attributed,
> verified and commercially priced?"

Total plant OEE/availability fails this test — it is a large, multi-causal, slowly-moving
aggregate that mixes maintenance, operations, process technology, feedstock, and Capex
effects (protocol Section 7). Nothing about it is objectively attributable at the aggregate
level; it can only be made attributable by decomposing it into individually-classified,
individually-adjudicated events. That decomposition is the actual work of this document.

## Definition: atomic value event

A discrete, dateable occurrence with:
1. **A clear trigger** — something happened (a failure, a completed work order, a permit
   delay, a scope decision) that can be timestamped.
2. **A defined causal party** — even if joint, the event has a proposed classification
   (provider-controlled / jointly-influenced / customer-controlled / excluded, per protocol
   Section 7) that can be argued for or against with evidence.
3. **A measurable before/after or avoided-cost basis** — a number, not a narrative.
4. **A data source that exists or can be built cheaply** — CMMS work orders, contractor
   invoicing, permit system logs, TA scope registers. If no realistic data source exists,
   the event is not usable yet, however appealing it sounds.

## Candidate atomic value events (first pass — 8 events)

| # | Event | Controllability | Data source | KPI Pyramid level | Payment-eligible? |
|---|---|---|---|---|---|
| 1 | **Contractor productivity delta** — actual cost per completed standard work order vs. benchmarked/prior rate | Primarily provider-controlled, with customer dependency on approved-supplier list constraints (`05_VALUE_POOLS/value_pool_tree.md` Pool 1 correction) | Contractor invoicing + CMMS work-order completion records | L3 Maintenance Process | Yes — from Phase 1 (near-automatic given agreed formula) |
| 2 | **Planned work conversion** — % of executed work that was planned vs. reactive/emergency | Provider-controlled (planning/scheduling discipline); gated by customer-controlled work-permit cycle time (Event 7) | CMMS work-order type field | L3 Maintenance Process | Yes — from Phase 2, with permit-cycle-time exclusion clause |
| 3 | **Repeat equipment failure avoided ("bad actor" elimination)** — equipment on a repeat-failure list operates failure-free beyond an agreed multiple of prior MTBR, following a defined RCA/RCM intervention | Provider-controlled for intervention quality; jointly-influenced by operating conditions (only counts if plant operated within an agreed envelope) | CMMS failure history + RCA records + agreed operating-envelope log | L2 Asset Performance | Yes, but only with Value Validation Board sign-off per event — not automatic |
| 4 | **Maintenance-attributable production loss event** — a specific logged trip/derate/shutdown, root-cause-classified by joint governance as maintenance-caused or not | Contested by default — classification itself requires joint adjudication, not a formula | Process historian + CMMS + joint RCA | L1 Customer Business Outcome (the closest thing to "OEE" in this architecture, but decomposed to individual events) | Only the subset classified maintenance-caused, and only after Value Validation Board adjudication — never the aggregate |
| 5 | **Turnaround scope reduction / repeat-scope elimination** — TA scope items eliminated vs. prior TA for the same equipment class, credited to demonstrated reliability improvement | Jointly-influenced — provider drives the reliability case, customer owns TA scope sign-off | TA scope registers (current vs. prior) + reliability engineering case file | L2/L3 | Phase 4 only, with joint TA scope review governance |
| 6 | **Lifecycle Capex deferral, validated** — replacement of a specific asset deferred beyond its original risk-based date, validated by joint engineering review as data-justified rather than budget-driven | Jointly-influenced; Capex sign-off is customer-controlled | Asset health/criticality data + joint engineering sign-off | L2 Asset Performance | Phase 4 only, hardest event in the set — requires an explicit counterfactual methodology, not just before/after |
| 7 | **Work-permit cycle time** — time from permit request to issuance | Customer-controlled | Permit system logs | L4 Enabler | **Never payment-eligible.** Tracked as a joint SLA/context metric because it gates Events 2 and 4 |
| 8 | **CMMS data quality / work-order closure completeness** — % of work orders closed with complete, timestamped, correctly-coded data | Jointly-influenced — platform ownership is typically the customer's (ALVAR/M+, `EVIDENCE_REGISTER.md` A14); data-entry discipline is provider-influenced | CMMS itself (self-referential; needs an independent audit sample) | L4 Enabler | **Never payment-eligible itself — it is a gate.** If data quality for a period falls below an agreed threshold, no event in this table is payment-eligible for that period, protecting both parties from paying (or being paid) on unreliable data |

## Why 5 of the 8 events are deliberately NOT payment-eligible at launch

Events 4, 5, 6, 7, and 8 stay out of, or are heavily gated before entering, any payment
mechanism at Phase 1-2. This is intentional, not a weakness of the architecture: it is the
direct, disciplined application of Petri's corrected controllability principle
(`EVIDENCE_REGISTER.md` correction log) and the Checker's Cycle 1 finding that attribution
work was correctly deferred rather than fabricated. Events 1-3 are where **Asset Performance
Partnership (Option B, market entry)** should concentrate first. Events 4-6 are where
**Selective Outcome-Based Modules (the destination)** eventually apply — "selective" means
exactly this: only the events that survive Value Validation Board scrutiny and explicit
customer-dependency carve-outs graduate into gainshare/painshare, not the full set at once.

## Worked example: applying Petri's formula

**Identified Value × Controllability × Realization Probability × Time-to-Impact =
Committable Value**

Using Event 1 (Contractor productivity delta) against the AMOR 2020 baseline (illustrative
only — these are the 2020 proposal's own unvalidated planning figures, per
`EVIDENCE_REGISTER.md` B4, not forecasts for any real engagement):

| Factor | Value for Event 1 | Reasoning |
|---|---|---|
| Identified Value | €17-20m/yr (A10, subcontractor management pool) | Source figure, pre-due-diligence |
| Controllability | ~0.8 (high, not 1.0) | Primarily provider-controlled, discounted for the named customer dependencies (supplier list, procurement contracts) |
| Realization Probability | ~0.6 in year 1, rising in later years | New contractor consolidation programs typically underperform their business case in year 1 due to transition friction — an honest, not pessimistic, planning assumption |
| Time-to-Impact | Fast (within 12 months) | Contractor rate renegotiation is one of the quickest levers to pull, unlike lifecycle Capex deferral (Event 6), which is multi-year |
| **Committable Value (illustrative)** | **~€8-10m in year 1**, rising toward the €17-20m identified ceiling as controllability/realization mature | This is a *methodology* demonstration, not a real number — do not quote it outside this worked example without re-deriving it against real customer data |

Contrast with Event 6 (Lifecycle Capex deferral): Controllability is low (jointly-influenced,
Capex-controlled by customer), Realization Probability is uncertain without a proven
counterfactual methodology, and Time-to-Impact is multi-year. Its Committable Value today is
close to zero — not because the underlying value pool is small (€5-15m/yr identified, A10),
but because none of the other three factors are mature enough yet. This is exactly why Event
6 is a Phase 4, Selective-Outcome-Based candidate and not a launch-phase KPI.

## Addendum — first-pass Red Team stress test

- **"Who adjudicates Event 3 and Event 4?"** Both require a Value Validation Board with real
  teeth (protocol Section 8) — this architecture assumes that board exists and is resourced.
  It does not exist yet (Gate 4, Operating Model). Flagged as a dependency, not resolved
  here.
- **"What stops the customer from gaming Event 8 (data quality) to block payment on Events
  1-3?"** Needs an independent audit-sample mechanism, not self-reported CMMS completeness.
  Not yet designed — flagged for Gate 3/4.
- **"Event 1's 'benchmarked rate' — benchmarked against what?"** Undefined here. Needs either
  a documented pre-transition baseline (as AMOR 2020 did with its €129m cost breakdown,
  A5) or external market rate-card data. This is solvable but not yet solved.

## Next steps (Cycle 3 candidates, not started)
1. Design the Value Validation Board's actual adjudication process for Events 3-6.
2. Build the customer-dependency carve-out clause template flagged in `RISK_REGISTER.md`.
3. Stress-test whether 5-10 events is the right number, or whether some (e.g. Event 4) should
   be split further before they're usable.
