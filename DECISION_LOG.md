# Decision Log

One entry per material strategic decision. Newest first.

## 2026-07-11 — Cycle 3: Gate 2 assessed PASS WITH CONDITIONS
Ran a full Checker/Red Team stress test of the attribution architecture per Petri's Cycle 3
instructions: per-event 12-point structured challenge, Customer CFO attack, Operations
Executive attack, Contract Lawyer attack, Provider CFO risk-corridor design, a
double-counting map, a counterfactual evidence protocol, a minimum-viable Value Validation
Board design, and 10 dispute scenarios. Full detail in `07_KPI_ATTRIBUTION/` and
`06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`; formal verdict in
`07_KPI_ATTRIBUTION/gate2_assessment.md`.

Key decisions arising from this cycle:
1. **Event 6 (lifecycle Capex deferral) is provisionally excluded from the near-term
   payment-KPI shortlist.** It has a structural conflict of interest (provider-set baseline)
   that this cycle's work did not fully resolve.
2. **Event 2 (planned work conversion) is downgraded to KPI-fee-only**, not gainshare — no
   direct euro-avoidance methodology exists for it.
3. **Event 4 (maintenance-attributable production loss) is confirmed as the sole
   painshare-eligible event**, gated by a 5-step (+1) decision tree and requiring Value
   Validation Board supermajority given its "Very High" dispute potential.
4. **Two design gaps are logged as open, not fixed:** (a) no netting mechanism exists for an
   intervention that fixes one failure mode while creating another; (b) no direct control
   exists against provider over-maintenance as painshare-avoidance behavior ("KPI gaming").
   Both added to `RISK_REGISTER.md`, targeted for Cycle 4.
5. **No event in the architecture monetizes an aggregate metric** (total maintenance cost,
   annual availability, MTBF standalone) — confirmed as a structural, not incidental,
   property of the design, validated against Red Team Scenario 9.
6. **Gate 2 does not close fully** until five numbered conditions in
   `gate2_assessment.md` are resolved (numeric SLA/materiality thresholds, the Event 1
   job-complexity catalog, risk corridor percentages, Event 6's resolution, and the two
   design gaps above).

## 2026-07-11 — Cycle 2 direction set from Petri's answers to the Cycle 1 questions
Petri answered all 10 Cycle 1 questions directly (Finnish, translated/logged in full context
in this project's chat history). Material decisions extracted:

1. **AMOR 2020 is evidence of architecture, not performance.** Never present its savings
   figures as achieved results. It did not execute (`EVIDENCE_REGISTER.md` B4).
2. **Acting party = Bilfinger-scale industrial services provider**, developed in the context
   of Petri's real senior leadership discussions with Bilfinger. Do not invent Bilfinger
   capabilities beyond what's verified (`EVIDENCE_REGISTER.md` B5).
3. **Target industries broadened** to asset-intensive continuous/semi-continuous process
   industries (refining, chemicals, petrochemicals, energy-intensive process, selected pulp
   & paper, selected metals & minerals) — not all industry (`ASSUMPTIONS.md` AS5).
4. **Governance model rejects MBO/founder-trust structure.** AMOR 2030 must be a
   process-driven, replicable platform: transparent baselines, joint governance, attribution
   rules, Value Validation Board, RACI, contract architecture, data transparency
   (`ASSUMPTIONS.md` AS6).
5. **Adopted value formula:** Identified Value × Controllability × Realization Probability ×
   Time-to-Impact = Committable Value. Refines protocol Section 15 for this project.
6. **Turnarounds/major shutdowns are excluded from the baseload fixed fee by default**,
   priced separately with their own commercial model — consistent with (and clarifying) the
   2020 source's ambiguity on TA risk allocation.
7. **Gainshare/painshare design principle adopted:** gainshare wherever value is objectively
   attributable; painshare only where the provider has sufficient control, baseline/data are
   agreed, dependencies are defined, exclusions are explicit, and exposure is capped.
8. **Cycle 1 recommendation revised** (supersedes the flat "recommend Option B" verdict):
   - Strategic destination: **Selective Outcome-Based Asset Performance Platform**
     (a scoped version of Option C — selective modules, not full-scope from day one).
   - Market entry: **Asset Performance Partnership** (Option B).
   - Maturity path: **Managed Transformation → Asset Performance Partnership → Selective
     Outcome-Based Modules.**
   - The long-term thesis is explicitly NOT reduced to Option B as an endpoint.
9. **"Control Tower Economics" adopted as a core AMOR 2030 design principle** — see
   `03_STRATEGIC_THESIS/control_tower_economics.md`. The provider's value is orchestrating
   an ecosystem (own staff, main partners, specialist contractors, OEMs, turnaround
   resources, reliability experts, digital providers) and owning planning, orchestration,
   performance visibility and accountability — not just performing labor.
10. **Correction: contractor/subcontractor management is "primarily provider-controlled,
    with defined customer dependencies," not "fully provider-controlled."** Customer
    retains real influence via approved-supplier lists, procurement contracts, vendor
    lock-in, labor/union constraints, work-permit processing, work prioritization, and Capex
    decisions. Material for painshare exposure sizing — see `RISK_REGISTER.md`.
11. **Cycle 2 proceeds directly to Gate 2** (KPI/Controllability/Attribution design), no
    pause. Explicit instruction: do not design attribution around total plant OEE. Start
    from loss-event classification and provider controllability at an atomic, individually
    attributable value-event level. See `07_KPI_ATTRIBUTION/attribution_architecture.md`.

## 2026-07-11 — Proceed in `petrihukkinen/gdp-dashboard` repo, branch `claude/amor-2030-strategy-3zdqjy`
**Decision:** Build the AMOR 2030 project file structure directly in this repository/branch,
rather than waiting for a dedicated repo, after confirming no separate AMOR source repo
exists under Petri's accessible GitHub account and Petri instead supplied the genuine 2020
AMOR source PDF directly.
**Reasoning:** Session instructions designate this repo/branch as the development target.
Petri provided real Level A source material directly rather than naming an alternate repo.
**Reversibility:** Fully reversible — content can be moved to a dedicated repo later without
loss.

## 2026-07-11 — Treat AMOR 2020 outcome as unknown, not assumed executed or shelved
**Decision:** All Cycle 1 analysis proceeds without assuming whether the 2020 AMOR MBO was
ever executed. Logged as `OPEN_QUESTIONS.md` Q1, blocking full Gate 0 closure.
**Reasoning:** Source document is explicitly non-binding/discussion-only; assuming an
outcome in either direction would violate the evidence-discipline rule in `CLAUDE.md` #4/#5.
**Reversibility:** N/A — this is a discipline decision, not a strategic bet.
