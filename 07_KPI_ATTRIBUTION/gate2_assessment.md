# Gate 2 — Controllability and Attribution: Formal Pass/Fail Assessment (Cycle 3)

## Pass criteria assessment

| Criterion | Verdict | Basis |
|---|---|---|
| Provider influence and customer responsibility separated | **PASS** | Four-tier controllability taxonomy applied per event, with named customer-dependency lists (`event_stress_test.md`) |
| Atomic value events objectively defined | **CONDITIONS** | Events 1, 2, 4 now have testable rules/decision trees; Event 3 has a 5-condition rule; Event 5 has condition (c); Event 6 has a structural conflict-of-interest problem not fully resolved |
| Baseline logic credible | **CONDITIONS** | Freeze-timing, indexation, and outlier-year review are now specified as *required*, but not yet executed/negotiated with real numbers |
| Data source identified | **PASS** | Named per event; system-of-record ownership stated |
| Dependency carve-outs defined | **CONDITIONS** | Dependencies are named exhaustively; numeric SLA thresholds (permit cycle time, access delay) are not yet set |
| Double counting controlled | **PASS** | PRIMARY/SECONDARY/CONTEXT hierarchy with explicit anti-double-count rules per event pair (`DOUBLE_COUNTING_MAP.md`) |
| Counterfactual logic defined | **PASS** | 5-level evidence hierarchy with explicit eligibility by payment type and a conservative no-payment default (`COUNTERFACTUAL_PROTOCOL.md`) |
| Payment eligibility limited | **PASS** | Only Events 1 (KPI fee → performance fee) and 3 (gainshare, case-by-case) are near-term payment-ready; Event 2 downgraded to KPI-fee-only; Events 5, 6 pushed to Phase 4; Event 4 painshare-only and heavily gated |
| Dispute process defined | **PASS** | Value Validation Board MVP with parity voting, quorum, escalation, and independent-review trigger (`VALUE_VALIDATION_BOARD_MVP.md`) |
| Service provider downside bounded | **CONDITIONS** | Risk corridor structure (deadband/cap/collar/annual max/event max/clawback) is designed; specific percentages are not yet set by Petri/commercial team |

## Verdict: **PASS WITH CONDITIONS**

The architecture is structurally sound and materially stronger than the Cycle 2 draft — it
survives 8 of 10 Red Team dispute scenarios cleanly and correctly avoids every form of
aggregate-OEE payment metric. It is not yet contract-ready.

## Conditions to close Gate 2 fully

1. **Set numeric thresholds:** permit-cycle-time SLA, production-access-delay SLA, and the
   "material" de minimis threshold (`CONTRACT_LANGUAGE_RISK.md`) — commercial decisions for
   Petri/commercial team, not architecture work.
2. **Build the job-complexity-normalized catalog** required for Event 1
   (`event_stress_test.md`) — needed before Event 1 is genuinely objective.
3. **Set risk corridor percentages** (deadband, caps, annual maximum exposure) —
   `06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md` gives a structure and illustrative ranges
   only.
4. **Resolve or suspend Event 6:** lifecycle Capex deferral has a structural conflict of
   interest (provider-set baseline) that this cycle's work does not fully solve. Recommend
   provisionally **excluding it from any near-term payment-KPI shortlist** until an
   independent baseline-setting mechanism exists.
5. **Two unresolved design gaps carried forward, not fixed this cycle:** (a) an intervention
   that fixes one failure mode while creating another has no netting mechanism; (b)
   over-maintenance as KPI-protection has no direct control. Both are logged in
   `RISK_REGISTER.md` as open risks requiring Cycle 4 design work, not closed here.

Gate 2 should not be declared fully closed until conditions 1-4 are resolved. Condition 5's
gaps do not block a PASS WITH CONDITIONS verdict but must be resolved before Gate 3
commercial modelling treats Event 4 (painshare) as safe to finalize commercially.
