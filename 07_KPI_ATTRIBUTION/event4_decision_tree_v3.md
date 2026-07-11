# Event 4 Decision Tree — v3 (Cycle 4, canonical version)

Supersedes the tree in `event_stress_test.md`. Incorporates the Cycle 4 materiality
threshold, SLA defaults, netting-mechanism interaction, and over-maintenance context.

- **Step 0 (materiality gate, new):** Is the estimated financial value of this event ≥
  €100,000 **or** ≥ 0.25% of Annual Contract Value, whichever is higher? No → excluded from
  Value Validation Board case review entirely; logged for reporting/context only. Stop.
- **Step 0.5 (netting interaction, new):** Is this event a documented new/different failure
  mode on the same asset, same functional location, or causally-connected equipment, within
  an open observation window from a prior Event 3 (or Event 4-remediation) intervention? Yes
  → route to `intervention_netting.md` instead of standalone adjudication here. Stop (for
  this process).
- **Step 1:** Was the failed component within the provider's contracted maintenance scope?
  No → excluded, stop.
- **Step 2:** Was the most recent PM/inspection for that component completed on schedule and
  to specification by the provider? No → provider-attributable, stop.
- **Step 3:** Is the failure mode consistent with a documented, known degradation pattern PM
  should have caught? No (novel/unforeseeable) → excluded, stop.
- **Step 3.5:** Did the provider issue a documented, dated risk advisory that was overridden
  by a customer scheduling decision? Yes → excluded/customer-attributable, stop.
- **Step 3.6 (new, Cycle 5 addendum, per Petri):** Did the customer exercise its
  maintenance-plan review/veto right (`overmaintenance_control.md`'s over-maintenance
  mitigation) to block, reduce, or delay a specific provider-proposed PM/CM action, **and**
  is that blocked/reduced action the one that would have prevented this failure mode? Yes →
  excluded/customer-attributable, stop. **This closes a gap the veto-right control itself
  created:** giving the customer a review/veto right over maintenance-plan spend increases
  (to catch over-maintenance gaming) necessarily also gives the customer a channel to shift
  real controllability onto itself if it exercises that right and a preventable failure
  follows. Without this step, the architecture would have added a customer control lever in
  Cycle 4 without updating the attribution logic that lever interacts with — an internal
  inconsistency, not just a theoretical risk.
- **Step 4 (revised — SLA-driven, new):** Was the plant within its agreed operating envelope,
  **and** were all named customer dependencies within their agreed SLA at the relevant time —
  permit/customer approval cycle ≤ 48 hours; production access following an agreed
  intervention window ≤ 24 hours (Cycle 4 modelling defaults, contract-specific in practice)?
  If any customer dependency exceeded its agreed SLA → customer-attributable or excluded,
  stop. This directly implements the architecture rule: **contract-specific baseline → agreed
  SLA → attribution exclusion where the customer dependency exceeds the agreed SLA.**
- **Step 5:** If all above point to the provider → provider-attributable. Proceed to
  financial value calculation (documented production loss × the agreed, contract-fixed
  standard margin), subject to the risk corridor: per-event cap = 50% of the annual
  painshare cap; annual painshare cap = 10% of annual Base Fee; floor = zero (Base Fee
  cannot go negative); no cross-year carry-forward; 24-month clawback window.
- **Step 6 (context, new):** Is there an active over-maintenance Red Flag Trigger
  (`overmaintenance_control.md`) for this asset/class? If yes, logged as context for the
  Board's review — informative, not an automatic penalty multiplier — and may inform whether
  escalation to the Joint Asset Performance Board is warranted.

## Why context, not penalty, at Step 6
An unresolved, unproven Red Flag should not aggravate a separate painshare determination —
that would punish the provider twice for one underlying suspicion before either is proven.
Tested directly in Scenario 14, `cycle4_red_team_scenarios.md`.
