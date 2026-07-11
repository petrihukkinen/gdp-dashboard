# Cycle 4 Red Team Scenarios (11-15)

Continues the numbering from `ATTRIBUTION_DISPUTE_SCENARIOS.md` (1-10), testing the new
Cycle 4 mechanisms specifically.

## 11. Provider ramps up PM hours sharply on an asset just before a suspected failure risk window, then reports no Event 4 exposure occurred.
- **Customer position:** suspiciously timed intensity spike suggests painshare-avoidance
  gaming, not genuine risk management.
- **Provider position:** proactive risk management should be rewarded, not penalized.
- **Attribution decision:** the Red Flag Trigger tests MII against RRE, not timing alone. If
  the spike achieved documented risk reduction (healthy RRE) and RCM/FMEA justification is on
  file, no flag fires — this is legitimate. If RRE is poor and justification is missing, the
  flag fires and any related Event 3 claim is suspended pending VVB review.
- **Contract weakness:** timing-based suspicion alone is not evidence.
- **Required rule:** RRE and documented technical justification are the deciding factors, not
  timing.

## 12. An RCA-driven Event 3 intervention fixes a pump seal failure; a new vibration issue appears on a mechanically-coupled gearbox within 60 days.
- **Customer position:** net value should be reduced or reversed.
- **Provider position:** the gearbox issue is unrelated, coincidental.
- **Attribution decision:** the gearbox qualifies as causally-connected equipment (mechanical
  coupling); joint RCA determines the causal link. If linked, `intervention_netting.md`
  applies and net value is recalculated. If RCA finds no link, the Event 3 claim proceeds
  normally once the observation window closes.
- **Contract weakness:** "causally connected" still lacks a pre-agreed engineering map — see
  remaining gaps.
- **Required rule:** case-by-case RCA judgment applies until a causal-connection map exists;
  functional but weaker than a deterministic rule.

## 13. Provider claims Event 9 (Turnaround Execution Efficiency) gainshare; customer argues the "independent" benchmark estimator was hand-picked by the provider.
- **Customer position:** a provider-selected estimator isn't truly independent.
- **Provider position:** the estimator is a recognized industry benchmarking firm.
- **Attribution decision:** the benchmark provider must be **jointly selected and named in
  the contract in advance** — a unilaterally-chosen estimator, however reputable, does not
  satisfy Event 9's attribution rule. Absent joint selection, the claim is inadmissible for
  gainshare (defaults to no payment, the standing conservative default).
- **Contract weakness:** Event 9's original design said "independent" without specifying the
  selection process — fixed by requiring joint, pre-agreed selection.
- **Required rule:** name the benchmark provider in the contract before the first TA cycle.

## 14. A production loss occurs while an over-maintenance Red Flag is already open on the same asset.
- **Customer position:** proof the maintenance program was ineffective — painshare should
  apply, possibly aggravated.
- **Provider position:** the flag was unresolved and unproven when the failure occurred;
  presuming guilt is unfair.
- **Attribution decision:** `event4_decision_tree_v3.md` Step 6 logs the active flag as
  **context for VVB review, not automatic aggravation** — deliberately, to avoid penalizing
  the provider twice for one underlying, unproven suspicion.
- **Contract weakness:** none new — this is the intended behavior of Step 6.
- **Required rule:** Red Flag context informs, but never automatically penalizes, a separate
  Event 4 determination absent independent confirmation.

## 15. A netted intervention shows a small new failure mode within the observation window; the customer's VVB representative wants to escalate anyway rather than accept residual risk.
- **Customer position:** any new issue, however small, should taint the claim.
- **Provider position:** the issue is trivial (below the materiality threshold) and shouldn't
  block an otherwise-qualifying claim.
- **Attribution decision:** proposed extension of the materiality threshold to secondary/
  netted issues — a sub-threshold secondary issue is logged for context but doesn't trigger
  a full netting recalculation. **This is a proposed interpretation, not something Petri
  explicitly authorized.**
- **Contract weakness:** the original netting brief didn't state a de minimis carve-out for
  trivial secondary issues.
- **Required rule:** requires Petri/commercial confirmation — logged in
  `gate3_readiness_assessment.md` as an open decision, not assumed silently.

## Summary
3 of 5 new scenarios (11, 13, 14) resolve cleanly using mechanisms built this cycle. 2 (12,
15) expose remaining gaps — the causal-connection map and the materiality carve-out
extension — both logged, neither hidden.
