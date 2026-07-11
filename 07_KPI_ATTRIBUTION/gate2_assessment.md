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

## Conditions to close Gate 2 fully — STATUS AFTER CYCLE 4

1. ~~Set numeric thresholds~~ — **RESOLVED (Petri, Cycle 4):** materiality €100,000/0.25%
   ACV; SLA defaults 48h permit / 24h production access. See `DECISION_LOG.md`.
2. **Still open:** the job-complexity-normalized catalog for Event 1 has not been built.
3. ~~Set risk corridor percentages~~ — **RESOLVED (Petri, Cycle 4):** see
   `06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`.
4. ~~Resolve or suspend Event 6~~ — **RESOLVED (Petri, Cycle 4):** permanently excluded from
   the payment-KPI set; strategic asset value moved to the advisory/transformation engine.
5. ~~Two unresolved design gaps~~ — **RESOLVED at a design level, Cycle 4:** the
   over-maintenance control and intervention netting mechanism are now built and stress-
   tested — see `overmaintenance_control.md`, `intervention_netting.md`. Each carries its own
   sub-prerequisites (baseline calibration, causal-connection map) that remain open — see
   `gate3_readiness_assessment.md`.

**Updated overall status: Gate 2 substantively closed.** Condition 2 (Event 1 catalog) is
the one item on this list still fully open; it does not block Gate 3 from starting, since
Event 1 can operate at KPI-Fee level without it — only its escalation to performance-fee
status needs the catalog resolved first.
