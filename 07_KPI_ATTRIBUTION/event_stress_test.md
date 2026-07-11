# Cycle 3 — Structured Stress Test of Each Atomic Value Event

Maker attempting to break its own Cycle 2 architecture, per Petri's instruction. Each event
scored on the 12-point protocol. Recommendation codes: KEEP / MODIFY / DOWNGRADE / REMOVE.

---

## Event 1 — Contractor Productivity Delta

1. **Definition:** "€/completed standard work order vs. benchmark" is not yet objective —
   "standard work order" is undefined. Two parties could classify the same job differently
   by complexity. **Gap.**
2. **Baseline:** Not yet specified — needs a frozen pre-transition period, index-adjusted for
   inflation, volume-normalized (already a rate, so volume-neutral by construction), and an
   outlier-year review before freezing.
3. **Data source:** Contractor invoicing (ERP/AP) + CMMS work-order job coding. Customer
   typically owns both platforms.
4. **Data quality:** Invoices are externally auditable and hard to game; CMMS job-coding is
   not — a provider could code jobs into more favorable "standard" buckets. Needs sampling
   audit.
5. **Controllability:** Primarily provider-controlled, with defined customer dependencies
   (see below).
6. **Customer dependencies:** approved-vendor list, procurement master agreements/rate
   floors, vendor lock-in (OEM sole-source), production-access windows affecting job cost,
   customer work prioritization.
7. **Attribution rule (testable):** A work order counts only if (a) the contractor was
   selected without customer-mandated sourcing restriction, (b) its job code exists in a
   pre-agreed standard catalog with complexity weighting, and (c) production access was
   within the agreed SLA. Fails any → hard exclusion from the calculation, not adjustment.
8. **Exclusions:** OEM-mandated sole-source jobs, customer-directed rate agreements, jobs
   during customer access restrictions, non-catalog one-off scope.
9. **Financial value:** (benchmark rate − actual rate) × catalog-eligible completed volume,
   net of Year-1 contractor transition/mobilization cost. Never extrapolated to the full
   €68m subcontracting base — only the catalog-eligible subset.
10. **Payment eligibility:** KPI Fee from Phase 1; performance-fee eligible from Phase 3 once
    the benchmark methodology is independently verified.
11. **Dispute potential:** Medium — concentrated in catalog definition and benchmark-setting.
12. **Recommendation: MODIFY.** Build the standard job-code catalog with complexity
    normalization and the named customer-dependency exclusion list before this is
    contract-ready. Strongest event in the set once modified.

---

## Event 2 — Planned Work Conversion

1. **Definition:** "% executed as planned" is objective only if "planned" has a hard,
   timestamp-locked test (e.g. released ≥7 days pre-execution with a complete work package).
   Without a lock, late reclassification is possible.
2. **Baseline:** Trailing 12-24mo actual %, normalized for known one-off disruptions.
3. **Data source:** CMMS work-order type + timestamp fields (customer-owned platform).
4. **Data quality:** Directly gated by Event 8 (CMMS data quality) — this event should never
   be payment-eligible in a period where Event 8's threshold fails. Confirms the Cycle 2 gate
   design was correct.
5. **Controllability:** Provider-controlled (planning discipline), gated by customer-
   controlled permit timing and production-access windows.
6. **Customer dependencies:** permit issuance timing, production-access/shutdown windows,
   customer-directed schedule changes, operator job-release availability.
7. **Attribution rule:** A work order enters the numerator only if released ≥7 days
   pre-execution AND permit was within SLA AND access wasn't customer-delayed beyond an
   agreed threshold. A single SLA breach removes that event from the metric entirely — it
   never counts against the provider.
8. **Exclusions:** True safety-critical emergencies — always excluded from both numerator and
   denominator; they feed Event 3/4 instead, not this metric.
9. **Financial value:** **None directly** — this is a process/leading indicator with no
   standalone euro-avoidance methodology defined. Inventing one now would violate evidence
   discipline.
10. **Payment eligibility:** KPI Fee only. Not gainshare-eligible until a direct cost
    linkage is separately built and evidenced.
11. **Dispute potential:** Medium-High — concentrated in permit-SLA breach attribution.
12. **Recommendation: DOWNGRADE to Management/KPI-Fee-only KPI.** Not gainshare material as
    currently defined.

---

## Event 3 — Repeat Equipment Failure Avoided

1. **Definition:** Reasonably objective on paper, but "failure-free" needs a hard test (does
   a minor stoppage count? a different failure mode on the same asset?).
2. **Baseline:** "2x prior MTBR" is statistically meaningless on a small failure sample.
   **Gap:** needs a minimum-failure-count qualifying threshold (e.g. ≥3 documented failures
   in the trailing 3 years) before an asset is even eligible for this event category.
3. **Data source:** CMMS failure history + RCA records (often stored outside CMMS) + agreed
   operating-envelope log (DCS/historian).
4. **Data quality:** RCA documentation quality is typically the weak link — needs a
   standardized RCA template as a prerequisite, not assumed to exist.
5. **Controllability:** Provider-controlled for intervention quality; jointly-influenced by
   operating conditions.
6. **Customer dependencies:** operator actions/process upsets, feedstock changes, production
   rate, Capex approval if intervention required parts, engineering sign-off on RCA findings.
7. **Attribution rule (5 conditions, all required):** (a) ≥3 documented prior failures, (b) a
   joint RCA identifying a specific documented root cause, (c) a specific, dated provider
   intervention addressing that cause, (d) plant operated within the agreed envelope for the
   full evaluation window, (e) no recurrence of the *same* failure mode within the evaluation
   window (≥18 months or 1.5× historical MTBR, whichever longer). Missing any condition
   disqualifies payment (reporting still allowed).
8. **Exclusions:** failures during off-envelope operation; different failure modes than the
   one addressed; assets below the 3-failure baseline threshold.
9. **Financial value:** Avoided value = agreed standard cost-per-failure-event (average of
   the documented prior incidents), not a theoretical maximum-loss estimate. Counted once per
   qualifying window per asset — see `DOUBLE_COUNTING_MAP.md`.
10. **Payment eligibility:** Gainshare-eligible, but only via individual Value Validation
    Board sign-off — never an automatic formula.
11. **Dispute potential:** High — "would it have failed again anyway" is inherently
    contestable.
12. **Recommendation: MODIFY.** Add the 3-failure baseline threshold and the 5-condition rule.
    **KEEP** as a gainshare candidate, case-by-case only.

---

## Event 4 — Maintenance-Attributable Production Loss Event

1. **Definition:** Contested by default — "maintenance-attributable" is not self-defining and
   needs a decision tree, not a label.
2. **Baseline:** Not applicable in the usual sense — evaluated per-event. A de minimis
   threshold (events below an agreed € or duration size aren't reviewed at all) is undefined
   — **gap**, needs a number from Petri/commercial team.
3. **Data source:** Process historian/DCS (timing, production impact) + CMMS (maintenance
   history on the affected equipment) + joint RCA record.
4. **Data quality:** DCS/historian data is typically high-integrity and hard to game; the
   real risk is in the human RCA classification, not the instrumentation.
5. **Controllability:** Contested by default — case-by-case joint decision required.
6. **Customer dependencies:** operating-mode changes, feedstock changes, production
   rate/utilization decisions, operator actions, equipment-release timing for repair.
7. **Attribution rule — sequential decision tree, not a narrative:**
   - Step 1: Was the failed component in the provider's contracted maintenance scope? No →
     excluded, stop.
   - Step 2: Was the most recent PM/inspection completed on schedule and to spec by the
     provider? No → provider-attributable, stop.
   - Step 3: Is the failure mode consistent with a documented, known degradation pattern PM
     should have caught? No (novel/unforeseeable) → excluded, stop.
   - **Step 3.5 (added this cycle, surfaced by the Operations Attack):** Did the provider
     issue a documented, dated risk advisory that was overridden by a customer scheduling
     decision (e.g. a delayed shutdown)? Yes → excluded/customer-attributable regardless of
     other factors.
   - Step 4: Was the plant within its agreed operating envelope at time of failure? No →
     customer-attributable or excluded, stop.
   - Step 5: If all above point to the provider → provider-attributable.
8. **Exclusions:** out-of-scope components, off-envelope operation, novel failure modes,
   force majeure, customer-overridden risk advisories (Step 3.5).
9. **Financial value:** documented production loss × an agreed, contract-fixed standard
   margin figure (set at signing, not spot market at time of event — protects both parties
   from market-volatility gaming) — for provider-attributable events only.
10. **Payment eligibility:** **Painshare-only** — the primary painshare mechanism in the
    entire architecture — and only after Value Validation Board adjudication using the
    decision tree, never automatic.
11. **Dispute potential:** **Very High** — the single highest-stakes, highest-dispute-risk
    event in the set, because real money moves against the provider.
12. **Recommendation: MODIFY substantially.** Implement the 5-step (+3.5) decision tree, cap
    exposure per event and annually (see `06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`),
    require supermajority (not simple majority) Value Validation Board sign-off given the
    stakes. **KEEP**, but only in capped, gated form.

---

## Event 5 — Turnaround Scope Reduction

1. **Definition:** A scope item either appears in both TA lists or doesn't (objective); "due
   to reliability improvement" vs. "removed for budget reasons" is a judgment call.
2. **Baseline:** Prior TA is typically 4-6 years old — operating conditions may have
   materially changed, weakening the comparison.
3. **Data source:** TA scope registers (customer-owned planning system) + joint reliability
   engineering case file.
4. **Data quality:** TA scope registers are typically well-documented (high-stakes, heavily
   reviewed) — the risk is in the "why," not the underlying data.
5. **Controllability:** Jointly-influenced — provider builds the reliability case, customer
   owns TA scope sign-off and could cut scope for cost reasons unrelated to reliability.
6. **Customer dependencies:** TA budget constraints, TA scheduling/duration decisions,
   customer engineering review and final sign-off.
7. **Attribution rule:** A scope item counts only if (a) it appeared in the immediately
   prior executed TA scope for the same equipment, (b) its removal is supported by a joint
   reliability case file with condition-monitoring/inspection evidence (not a budget memo),
   and **(c) the customer's TA planning team independently co-signs in writing that the
   removal was reliability-driven, not budget-driven.** Condition (c) is the anti-gaming
   mechanism.
8. **Exclusions:** budget-only scope cuts (documented as such), scope items that were never
   actually needed (planning error, not a reliability win), process/feedstock-driven changes.
9. **Financial value:** actual avoided TA execution cost (contractor + materials + extended
   outage time) using the prior TA's actual cost for that specific scope item, not a
   theoretical estimate.
10. **Payment eligibility:** Gainshare-eligible only at Phase 4, with joint TA scope review
    governance.
11. **Dispute potential:** High — the multi-year baseline gap and the budget-vs-reliability
    distinction are exactly where customer and provider incentives diverge.
12. **Recommendation: MODIFY** — add condition (c) as a hard gate. **KEEP** as a Phase 4
    candidate only.

---

## Event 6 — Lifecycle Capex Deferral, Validated

1. **Definition:** "Data-justified rather than budget-driven" is the same structural
   ambiguity as Event 5, plus a unique conflict-of-interest problem (see below).
2. **Baseline:** The "original risk-based replacement date" — set by whom, when, using what
   methodology? **If the provider sets this baseline itself, it has a direct incentive to
   set an aggressive original date so any deferral looks like a bigger win.** This is a
   structural conflict of interest unique to this event.
3. **Data source:** Asset health/criticality data (often provider-generated) + joint
   engineering sign-off.
4. **Data quality:** Condition-monitoring maturity varies hugely by asset type; for many
   assets "risk-based" is a euphemism for expert judgment (Level 5 evidence).
5. **Controllability:** Jointly-influenced; Capex sign-off is customer-controlled.
6. **Customer dependencies:** Capex approval/budget cycles, customer engineering review,
   customer risk-appetite decisions (a customer may accept more risk regardless of advice).
7. **Attribution rule:** An event counts only if (a) the original risk-based replacement
   date was set **before** the current commercial period began, by a methodology
   independently reviewable by the customer — never set retroactively by the provider once
   deferral value became commercially attractive — (b) the deferral decision is jointly
   signed off with documented condition-monitoring evidence, and **(c) if the asset fails
   before the eventual actual replacement, the entire claimed deferral value is immediately
   reversed/clawed back, and the failure is separately evaluated under Event 4.**
8. **Exclusions:** deferrals driven by customer Capex unavailability rather than genuine
   condition justification; deferrals on assets without a pre-existing, independently-set
   baseline date.
9. **Financial value:** time-value-of-money benefit of deferring the Capex outlay (an
   agreed discount rate), not the raw replacement cost.
10. **Payment eligibility:** Phase 4 only, gainshare-eligible, hardest event in the set,
    mandatory clawback as a standing condition of any payment.
11. **Dispute potential:** **Very High** — combines Event 3/5's counterfactual difficulty
    with a conflict-of-interest problem no other event has.
12. **Recommendation: REMOVE from the near-term commercial model.** Keep only as a long-term
    Phase 4 research candidate, and only if an **independent, non-provider** baseline-setting
    mechanism is established first. This is currently the weakest event in the set —
    recommend explicitly excluding it from any near-term payment-KPI shortlist.
