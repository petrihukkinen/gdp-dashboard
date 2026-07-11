# Attribution Dispute Scenarios — Cycle 3

Ten scenarios (as specified by Petri), each resolved against the architecture built this
cycle. Where the architecture doesn't yet resolve a scenario cleanly, that is stated as a
gap, not concealed.

## 1. Provider claims an avoided production loss. Customer says the equipment would not have failed.
- **Customer position:** No hard evidence the failure trajectory was real.
- **Provider position:** RCA identified a documented degradation pattern consistent with a
  known failure mode; intervention was documented.
- **Attribution decision:** Apply `COUNTERFACTUAL_PROTOCOL.md`. If evidence is only Level 3
  (OEM data) without Level 1/2 (actual prior occurrence), the claim does **not** qualify for
  gainshare under the conservative default — reported only, not paid.
- **Contract weakness (pre-Cycle-3):** no objective resolution path existed without evidence
  tiers.
- **Required rule:** mandatory evidence-tier declaration at submission; Level-3-only claims
  auto-route to "reported, not paid."

## 2. Contractor productivity improves. Customer says lower job complexity caused it.
- **Customer position:** the job catalog didn't control for an easier job mix in the period.
- **Provider position:** catalog was pre-agreed and job mix was consistent with baseline.
- **Attribution decision:** requires the complexity-normalized catalog identified as a gap in
  `event_stress_test.md`, Event 1. Without it, claim must be recalculated on a
  mix-normalized basis or rejected.
- **Contract weakness:** Event 1's original Cycle 2 definition didn't specify complexity
  normalization.
- **Required rule:** catalog must include a job-mix normalization step; VVB reviews mix-shift
  data as standard evidence on every Event 1 claim.

## 3. MTBF improves. Customer funded a major Capex replacement.
- **Customer position:** the customer paid for the new equipment — the provider didn't create
  the improvement, the Capex did.
- **Provider position:** provider specified the replacement and manages ongoing maintenance
  discipline to sustain it.
- **Attribution decision:** per the funding-source rule (`CUSTOMER_CFO_ATTACK.md`), a purely
  Capex-funded improvement with no material provider maintenance contribution does **not**
  generate an Event 3 gainshare claim — at most a separately negotiated project-delivery fee.
- **Contract weakness:** the original Event 3 design didn't exclude Capex-funded gains.
- **Required rule:** funding-source declaration is mandatory on every Event 3 claim;
  customer-funded interventions are excluded from gainshare by default.

## 4. Turnaround finishes early. Customer removed scope.
- **Customer position:** the early finish was due to a scope cut, not provider efficiency.
- **Provider position:** execution efficiency also contributed.
- **Attribution decision:** "early finish" alone is not evidence for any existing event.
  Event 5's condition (c) already requires customer co-sign that scope removal was
  reliability-driven, not budget-driven; if it wasn't, no Event 5 payment. Genuine TA
  execution-efficiency (distinct from scope reduction) has **no defined event at all** in the
  current 6-event set.
- **Contract weakness:** "early finish" conflates two different value claims that the
  architecture doesn't currently separate.
- **Required rule:** do not accept "early finish" as evidence for Event 5. If TA execution
  efficiency is to be monetized, it needs its own atomic event — **flagged as a Cycle 4
  candidate**, not designed here.

## 5. Maintenance cost falls. Production volume also fell.
- **Customer position:** lower cost is just lower activity, not provider efficiency.
- **Provider position:** cost per unit or per work order still improved.
- **Attribution decision:** this dispute shouldn't arise under the current architecture,
  because Event 1 is deliberately defined as a **rate** (€/completed standard work order),
  not an absolute cost figure, and there is no "total maintenance cost" payment event at all
  in the 6-event set.
- **Contract weakness:** none specific to the current events — this scenario is a warning for
  any *future* proposed event, not a live gap.
- **Required rule:** standing design rule — no absolute-€ cost metric may ever enter the
  payment KPI set; only normalized (rate, per-unit, or event-specific avoided-cost) metrics
  qualify.

## 6. Provider recommends preventive replacement. Customer says it was unnecessary over-maintenance.
- **Customer position:** provider is padding scope/spend, possibly to protect itself from
  future painshare exposure.
- **Provider position:** replacement was risk-based and justified.
- **Attribution decision:** this is not an attribution-architecture dispute at all — it's a
  scope/spend governance question. If it proceeds and no failure occurs, no Event 3/4 claim
  is even triggered; the real risk (higher cost base) is indirect.
- **Contract weakness:** **genuine, unmitigated gap** — the architecture has no direct control
  against over-maintenance-as-KPI-protection. Directly connects to the Operations Attack's
  sharpest finding.
- **Required rule:** documented, criticality-based justification required for any PM/
  replacement scope increase beyond an agreed year-on-year envelope, subject to customer
  review — **not solved in Cycle 3**, a Cycle 4 design item.

## 7. Customer delays equipment release. Provider misses a KPI.
- **Customer position:** the KPI miss is real regardless of cause.
- **Provider position:** the delay was outside its control.
- **Attribution decision:** covered directly by the SLA exclusion logic already built for
  Event 2 (permit/access SLA) and Event 4 (Step 3.5 override logic) — if documented and
  outside the agreed SLA, the affected events are excluded from the metric entirely.
- **Contract weakness:** the exclusion logic exists conceptually, but the actual SLA numbers
  (days, hours) are not yet set — a commercial negotiation, not an architecture gap.
- **Required rule:** SLA numeric thresholds must be named in the contract before go-live.

## 8. CMMS data is incomplete. Provider creates its own baseline.
- **Customer position:** a provider-created baseline is inherently self-serving.
- **Provider position:** no usable customer baseline existed, so one was created to do the
  job.
- **Attribution decision:** this is exactly why **Event 8 (CMMS data quality) was designed as
  a hard gate in Cycle 2** — below-threshold data quality makes **no event in the table**
  payment-eligible for that period, regardless of any substitute baseline. A provider-created
  baseline is never contractually valid for payment purposes.
- **Contract weakness:** none — the gate works as designed. A good sign the Cycle 2
  architecture anticipated this correctly.
- **Required rule:** reaffirm the Event 8 gate explicitly in contract language; any
  provider-proposed baseline requires independent validation before future use.

## 9. One major event destroys annual availability. Root cause is disputed.
- **Customer position:** wants painshare based on annual availability impact.
- **Provider position:** root cause is contested, possibly multi-causal.
- **Attribution decision:** confirms why **total annual availability is explicitly not a
  payment metric** in this architecture — Event 4 operates at the individual-event level via
  the decision tree, never as an annual aggregate. The real dispute is narrower: this
  specific event's decision-tree classification, not an annual number.
- **Contract weakness:** none structural — this scenario validates Petri's original
  instruction not to design around total OEE.
- **Required rule:** reaffirm no annual/aggregate availability payment metric; all Event 4
  claims are single-event, decision-tree-adjudicated only.

## 10. Provider creates value in Year 1. Benefit continues for 5 years. Gainshare duration is disputed.
- **Customer position:** the provider shouldn't be paid every year for one Year-1 action.
- **Provider position:** the ongoing benefit is real and continuing.
- **Attribution decision:** the "recurring" contract-language fix
  (`CONTRACT_LANGUAGE_RISK.md`) applies directly — no value carries forward automatically; if
  the underlying condition (e.g. Event 1's rate improvement or Event 3's failure-free
  operation) is re-verified as still holding in Years 2-5, it requalifies each period as a
  fresh, evidence-based re-submission, not an automatic multi-year annuity.
- **Contract weakness:** needs an explicit re-verification cadence statement per event type in
  the contract, cross-referenced to `VALUE_VALIDATION_BOARD_MVP.md`'s cadence table.
- **Required rule:** explicit multi-year re-verification clause; no automatic multi-year
  gainshare annuities without periodic re-proof.

## Summary
8 of 10 scenarios are resolved cleanly by the architecture as corrected this cycle. 2 expose
genuine, unresolved gaps (#4 — no TA execution-efficiency event exists; #6 —
over-maintenance/KPI-gaming has no direct control) that are logged, not hidden, and carried
into `gate2_assessment.md` and `RISK_REGISTER.md`.
