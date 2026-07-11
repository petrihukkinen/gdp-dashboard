# Decision Log

One entry per material strategic decision. Newest first.

## 2026-07-11 — Cycle 10: Accountability Economics thesis built, Gate 3A PASS WITH CONDITIONS
Following the Strategic Reframe Challenge (Control Tower as operating system, not product),
built the full economic and validation architecture for the "Accountability Economics"
thesis (renamed from "Accountability Premium" — no price premium is assumed). Full detail
across `10_FINANCIAL_MODEL/ACCOUNTABILITY_ECONOMICS_TREE.md`, `FIVE_ECONOMIC_MECHANISMS.md`,
`ACCOUNT_LIFETIME_VALUE_MODEL.md`, `03_STRATEGIC_THESIS/ACCOUNTABILITY_BOUNDARY.md`,
`ACCOUNTABILITY_ECONOMICS_RED_TEAM.md`, `SYSTEMATIC_CAPABILITY_MAP.md`, and
`08_OPERATING_MODEL/EARNED_RETENTION_PROTOCOL.md` / `PULL_THROUGH_CONFLICT_PROTOCOL.md`.

**Core finding:** the thesis claims superior Account Lifetime Value from scope, duration,
retention, and pull-through economics — explicitly not from a price premium or a separately
priced Control Tower fee. An illustrative sensitivity model found the thesis's advantage is
directionally robust to renewal-probability and pull-through failure, but **highly sensitive
to Control Tower operating cost** — a 3x cost increase erodes over half the modeled
advantage. This is now understood as the single biggest unresolved risk to the whole
strategy, more dangerous than any customer-behavior question, because it is entirely within
the provider's own control to get wrong.

**Accountability boundary formalized:** six distinct accountability types (Delivery,
Orchestration, Performance — provider-ownable; Asset Owner, Statutory, Production —
never delegable). "Single accountable provider" is now a permanently qualified phrase, not a
free-standing claim.

**Earned retention versus structural lock-in formally separated**, with required customer
protections (data ownership, portability, documentation, transition assistance) found to be
net positive for provider economics, not a tax on the model — they remove the biggest
customer objection to the whole thesis.

**Pull-through agency conflict addressed** with tiered safeguards (open-book disclosure,
independent technical challenge, competitive tender above a threshold, structural separation
of recommendation and sales incentives).

All three Cycle 9 validation protocols were rewritten in place, retiring the "would you pay
a separate Control Tower fee" question entirely and replacing it with scope-consolidation
and duration-appetite questions as the new primary validation targets.

**Gate 3A (Accountability Economics Logic): PASS WITH CONDITIONS.** The Differentiation
Falsification verdict from Cycle 9 (UNRESOLVED) is unchanged — this reframe changes where
the economics might come from, it does not prove the underlying capability is
non-replicable.

## 2026-07-11 — Cycle 9: external validation readiness built, no validation conducted
Built the falsification infrastructure needed before real external testing, per Petri's
instruction not to simulate or fabricate validation. Full detail in `18_INTERVIEW_QA/` and
companion files.

Identified and ranked 10 assumptions that could kill or materially damage the settled
architecture (`18_INTERVIEW_QA/FALSIFICATION_REGISTER.md`) — 5 CRITICAL: customer WTP for
orchestration as a distinct fee; Event 4's real differentiation from standard liability
terms; customer willingness to cede real orchestration authority (flagged as *arguably
contradicted* by AMOR 2020's own evidence — Neste retained significant control even under
trust-based conditions); provider-organization internal resistance (untested); and whether
Control Tower Economics is a systematized capability or relabeled contract management.

Built three 30-minute, problem-first (not sales-first) interview protocols — customer CFO
(12 questions), customer asset/maintenance/site director (10 questions), provider CFO/CEO
(10 questions, explicitly testing who-sells/who-owns-the-customer/who-carries-risk/who-gets-
revenue-and-margin-credit) — each question mapped to a specific falsification hypothesis
with predefined positive/warning/kill signals.

Attacked the Base-Fee-funded Control Tower packaging assumption directly — tested 5
alternative commercial structures, selected none, flagged Option E (provider-funded Control
Tower monetized only via modules) as very likely to fail Provider Executive validation
before ever reaching a customer.

Built the strongest case against Control Tower differentiation (`03_STRATEGIC_THESIS/
DIFFERENTIATION_FALSIFICATION.md`) — verdict UNRESOLVED, tilting toward "good contract
management with an unusually rigorous governance layer" absent multi-site evidence.

Mapped Petri's direct experience against every major architecture element
(`PETRI_ARCHITECTURE_EVIDENCE_MAP.md`) — found the two most load-bearing elements (Event 4's
downside corridor, Control Tower Economics as a priced capability) are both **new
hypotheses**, not proven by either ABB or Neste/AMOR experience.

Wrote `CEO_CONVERSATION_BOUNDARIES.md` (5 claims too weak to state, 5 strong enough, 3
validation-oriented questions for Petri to ask the CEO) and a predefined
`18_INTERVIEW_QA/VALIDATION_SCORECARD.md` locking scoring criteria before any interview
occurs, to prevent post-hoc narrative reinterpretation.

**No interviews were conducted. No external validation has occurred. Every deliverable this
cycle is preparation, not evidence.**

## 2026-07-11 — Cycle 8: Event 1 reclassified from core to optional module; final core architecture settled
Attempted to kill the last surviving core payment event, per Petri's explicit instruction.
Full detail in `06_COMMERCIAL_MODEL/cycle8_event1_survivability.md`.

**Verdict: RECLASSIFY, not kill.** A 10-year persistence model showed the naive "perpetual
share of a frozen baseline" design is commercially indefensible — an illustrative Scenario A
computation showed €4,480,000 cumulative payment over 8 years for a few months of Year-2
work, confirming the "perpetual rent" objection concretely. Tested perpetual / time-limited /
declining / baseline-reset / hybrid share structures — **recommended a time-limited savings
share on a rolling-baseline-plus-cohort architecture**, deliberately choosing simplicity
(Cycle 6's operability lesson) over the theoretically fuller but reset-gaming-exposed hybrid
option.

**Savings-pool exhaustion confirmed as real and structural**, not a design flaw — any
improvement-linked compensation model has this property. Response: price Base Fee to
harvest proven Event 1 gains into permanent revenue over the contract's life rather than
expecting Event 1 to remain productive indefinitely; no replacement payment event proposed.

**Administration cost sized for the first time** (30k-1m€/yr across contractor-spend scales)
and shown to reach a commercially absurd 12-24% ratio of verified value for smaller
customers in steady-state years — direct evidence for a five-condition, evidence-based
customer eligibility gate (minimum contractor spend, data quality, job-classification
stability, net-substitution measurability, Finance validation capability).

**Provider revenue concentration test concluded Event 1 must not be underwritten as
guaranteed continuous revenue** in provider financial planning — it has a natural,
finite opportunity arc.

**Differentiation claim attacked and narrowed:** "for the life of the deal" is withdrawn
(contradicted by the persistence findings); "exceeds normal maintenance-contract terms" is
withdrawn (unsupported by any benchmark evidence in this project). A narrower, evidenced
claim survives: bounded productivity-sharing plus capped downside accountability.

**Control Tower without atomic upside tested directly and found to hold:** Event 4 — not
Event 1 — is the mechanism that prevents AMOR from regressing to "Better Managed
Maintenance" (the outcome Cycle 2 explicitly rejected). **Final settled position: AMOR's core
is a Base-Fee-funded Control Tower + Event 4 downside corridor, complete and differentiated
on its own. The Contractor Productivity Value Module (Event 1) and the Turnaround Value
Module (Events 5+9) are both optional, additive, customer-specific — not required for AMOR
to be honestly AMOR.**

An external stakeholder validation test (3 interview scripts, pass/fail signals, a defined
finding that would force Event 1's full kill) was designed but explicitly not conducted —
no responses claimed or fabricated. A commercial-to-legal drafting brief for the
catastrophic-Event-4-loss/liability boundary was written for external counsel, per Petri's
instruction that this project defines the commercial boundary and drafting brief only, never
final legal language.

**The X/Z architecture naming from Cycle 6 is retired**, per Petri's explicit decision —
there is one core architecture plus optional modules, not a maturity ladder between two
named architectures.

## 2026-07-11 — Cycle 7: Event 3 killed entirely; core architecture reduced to Event 1 + Event 4
Attacked Cycle 6's "Annual Reliability Event Reward" (Event 3's restructured successor)
directly, per Petri's instruction not to protect Architecture Z if it turned out to be
semantic repackaging. Full detail in `06_COMMERCIAL_MODEL/cycle7_mva_hardening.md`.

**Verdict: SEMANTIC REPACKAGING.** The flat-reward redesign removed only the dollar-
valuation step of the original Event 3 — the actually expensive and disputed part
(proving a failure was genuinely avoided: counterfactual dependence, the Causal Connection
Map, the 180-day netting window, the ≥3-prior-failures baseline) was fully inherited
unchanged, and two new gaming risks (claim fragmentation, provider event-hunting) were
introduced. Tested all three candidate reward mechanisms (flat, severity-banded, annual
pool) — none escape the finding, because the mechanism used to *pay* doesn't fix a problem
that lives in how events *qualify*. **Event 3 is killed in every tested form, not just the
original.** Reliability value becomes a managed, reported operational discipline (context/
management KPIs only), never an individually monetized event.

**Structural consequence:** Architecture X (Event 1 + Event 4) and Architecture Z's core are
now identical. The X→Z "maturity path" as originally framed (graduating into the Reliability
Reward) is moot — there is nothing to graduate into. Architecture X is not an entry-tier
discount of Z; it is Z with the optional Turnaround Value Module switched off, a complete
and permanent offering in its own right, not a stalled migration. The Turnaround Module
readiness gate (Task 4) was redesigned around 5 evidence-based conditions unrelated to
reliability data, since the original premise no longer applies.

**Also this cycle:** Event 1 hardened against baseline-inflation, labour-substitution,
contractor-rate-vs-productivity conflation, and job-mix manipulation — real fixes, at real
added administrative cost (burden score rises from 14 to ~18 on the Cycle 6 scale); still
passes all four gates, now as the sole core upside mechanism. The Causal Connection Map was
sized for the first time (€2-11.25m initial build at large-site scale) — direct evidence
supporting the kill decision, and a second reason (provider selection bias under progressive
coverage) not to build it for this purpose. The Turnaround Module anti-selection rule was
designed (site-wide, minimum-term, pre-scope-freeze activation). The "complicated bonus
scheme" objection was engaged honestly — the honest AMOR differentiation claim is now
narrower than the original thesis: an ongoing, provider-incentivized share of measured
contractor savings, plus a real, capped, performance-linked liability that ordinary
maintenance contracts don't carry — not a claim to monetize reliability, which must not be
made. Catastrophic Event 4 losses are reframed as a **legal liability/indemnity** matter,
separate from and never overlapping with the performance corridor — Cycle 5's 26.7%-recovery
finding was a category error, not a corridor design flaw.

**Recommended Minimum Viable Commercial Architecture, final: Event 1 + Event 4 core, plus an
optional Turnaround Value Module (Events 5+9 bundled) for TA-intensive customers meeting the
5-condition readiness gate. Nothing else is monetized.**

## 2026-07-11 — Cycle 6: Commercial Complexity Kill Test — architecture reduced from 6 events to a lean core + optional module
Ran a dedicated subtraction exercise against the frozen Gate 2/3 architecture, per Petri's
explicit "Priority Zero: do not add, only remove unless resolving a fatal contradiction"
instruction. Full detail in `06_COMMERCIAL_MODEL/cycle6_complexity_kill_test.md`.

**Killed:** Event 2 as any kind of fee mechanism (downgraded to pure reporting — even the
Cycle 3 KPI-fee-only wrapper was excess machinery for €160,000/yr of stakes). **Event 3 as
originally designed** (case-by-case dollar-value gainshare) — failed attribution-clarity and
administrative-efficiency gates, specifically the unsized Causal Connection Map fixed cost
and the "paying for something that didn't happen" communication problem. **Event 9** as a
core/default payment event — failed the same two gates even more decisively once the Cycle 5
independence-criteria addendum raised its maintenance cost.

**Restructured, not killed:** Event 3 survives as a simplified **"Annual Reliability Event
Reward"** — same qualification criteria (unchanged), but a pre-agreed reward per qualifying
event counted and settled annually, instead of case-by-case dollar-value proof. This is
logged as subtraction (removing the per-event financial-proof burden), not as a new,
seventh payment event.

**Reclassified, not redesigned:** Event 4's attribution logic (the full decision tree,
including Step 3.6) is unchanged and frozen, as instructed. It is reclassified from "payment
event" to "downside corridor / liability adjustment mechanism" for commercial presentation
and governance purposes only.

**Modularized:** Events 5 and 9 (TA scope reduction, TA execution efficiency) are bundled
into an optional **Turnaround Value Module**, default-off, activated only for contracts
where TA execution responsibility and frequency justify the fixed governance cost.

**Recommended Minimum Viable Commercial Architecture: Architecture Z** — Event 1 (core
upside) + Event 3-simplified (core upside) + Event 4 (downside corridor) as the always-on
core, plus the optional Turnaround Value Module. Estimated claims volume ~13-15/year,
comfortably below the estimated 25-40/year bureaucracy break point. A 15-minute, ~180-word
CFO explanation was written and passed the test (does not require MII/RRE formulas, the full
Event 4 decision tree, VVB procedures, netting methodology, or six separate event
definitions to be credible).

**Three monetisation engines confirmed intact** (productivity/Event 1; reliability/Event
3-simplified + Event 4 + optional module; strategic asset/Event 6 advisory engine,
untouched) — Checker-verified no killed event silently re-entered through another mechanism.

**Real, unresolved risks carried forward, not solved by simplification alone:** the
architecture may still read as "a complicated bonus scheme" to a skeptical customer; a
customer can still refuse to fund reliability value even in simplified form (Architecture X
— Event 1 + Event 4 only — is the explicit fallback if so); the optional Turnaround Module
needs a minimum-term commitment rule to prevent cherry-picking easy turnarounds, not yet
designed.

## 2026-07-11 — Cycle 5 addendum: two attribution gaps fixed, market-entry recommendation partially revised
Petri re-sent the Cycle 5 brief (already fully executed in the prior turn, commit
`ab72749`) with four sparring points attached. Two were already satisfied by the existing
work (MII/RRE kept as control signals, not payment KPIs — `overmaintenance_control.md`;
netting cash-flow explicitly modelled under three settlement options — each model file's
cash-flow section). Two exposed genuine, unaddressed gaps, now fixed:
1. **"Jointly selected" independence criteria for Event 9's benchmark provider were
   underspecified** — a benchmark chosen jointly by both parties is not automatically
   unbiased. Added three explicit independence tests (no material commercial relationship
   with either party in 3 years; publicly documented/auditable methodology; a recognized
   neutral institution, named expert, or multi-relationship historical dataset) plus a
   mid-execution benchmark-change lockdown requiring dual Finance sign-off and independent
   reviewer approval — `07_KPI_ATTRIBUTION/event9_turnaround_execution_efficiency.md`.
2. **The customer maintenance-plan veto right (introduced in Cycle 4's over-maintenance
   control) was never fed back into Event 4's attribution logic** — an internal
   inconsistency: giving the customer a control lever to catch provider gaming necessarily
   also gives the customer a channel to shift real controllability onto itself if it blocks
   a genuinely necessary action. Added Step 3.6 to the Event 4 decision tree —
   `07_KPI_ATTRIBUTION/event4_decision_tree_v3.md`.

**Strategic hypothesis engaged, not deferred to:** Petri proposed Model C (not Model A) as
the likely AMOR market-entry winner, and Model B as the real Phase 3-4 competitive
advantage. Re-examined against the Cycle 5 numbers: Model C's absolute risk-corridor
exposure is in fact the smallest of the three models (caps set against the small €8m
Control Tower Fee) and its fixed-cost predictability (92.9%) is close to Model A's (96.9%)
— meaning Model C is closer to Model A on risk grounds than the original Cycle 5 chat
summary emphasized, while offering a materially better strategic narrative (it embodies
Control Tower Economics directly, rather than resembling conventional Full Service
outsourcing). **Recommendation partially revised: Model C is a legitimate, possibly superior,
market-entry candidate on a combined risk-and-narrative basis, not just a Phase 3-4 model.**
Model B's suitability as the Phase 3-4 leader is directionally agreed (it is the
architecture most aligned with genuine outcome-based economics) but remains numerically
unproven at current illustrative settings — depends on resolving the required Base
Fee/gainshare-split recalibration already logged as an open decision.

**New top risk named:** whether the attribution architecture, after five cycles of
rigor-driven additions, has become too operationally complex for any real team to want to
run — logged to `RISK_REGISTER.md` as a high-severity, high-priority Cycle 6 item, potentially
more fundamental than any single remaining design gap.

## 2026-07-11 — Cycle 5: Gate 3 commercial modelling, PASS WITH CONDITIONS
Petri set five Cycle 5 modelling decisions (180-day netting window confirmed with 90-365 day
event-specific flexibility; net-basis materiality interpretation for secondary/netting
effects, explicitly not an exclusion mechanism for damage splitting; MII/RRE bands retained
as ±15% modelling-only, not contractual, tested at ±10/15/20%; a mandatory pre-built Causal
Connection Map required before Event 3 gainshare eligibility; Event 9's benchmark
methodology/source to be pre-agreed at mobilisation, immutable without dual sign-off) and
directed full Gate 3 commercial modelling of three archetypes.

Three commercial models were built (Base Fee + KPI Fee; Base Fee + Atomic Value Share;
Control Tower + Value Modules) against an explicitly-labeled illustrative site — full detail
in `10_FINANCIAL_MODEL/`. Key findings:
1. **No model dominates in a Normal Year** — Model A earns the provider more precisely
   because it takes the least performance risk; Models B/C are designed to close the gap in
   a high-value year but, at these illustrative settings, do not fully do so even then.
2. **Catastrophic/multi-event Event 4 losses can leave the customer materially
   under-compensated** relative to real documented loss (as low as 26.7% recovery in one
   stress scenario) — the sharpest unresolved finding of this cycle.
3. **Claim bundling and customer-side damage-splitting are open gaming vectors**, directly
   tied to the still-unbuilt Causal Connection Map.
4. **Checker caught and disclosed a Maker arithmetic inconsistency** in Model B's gainshare-
   split application, which changed a substantive conclusion once corrected.
5. **Gate 3 verdict: PASS WITH CONDITIONS** — `10_FINANCIAL_MODEL/gate3_verdict.md`. Five
   remaining commercial gaps logged, none fatal, none silently resolved.

## 2026-07-11 — Cycle 4: numeric decisions set, over-maintenance and netting gaps closed
Petri set five numeric/scope decisions and directed that Gate 3 not begin until the two
surviving Cycle 3 Red Team gaps were closed:

1. **Event 6 excluded permanently from the near-term payment-KPI set.** Strategic asset-life/
   lifecycle value moves to the advisory/transformation fee engine instead of gainshare,
   unless a future independently-governed baseline methodology is developed.
2. **Materiality threshold set:** €100,000 verified value per event OR 0.25% of Annual
   Contract Value, whichever is higher — applies to Event 3/4 payment attribution and VVB
   case review.
3. **Risk corridor modelling assumptions set:** ±5% deadband; 20% annual gainshare cap / 10%
   annual painshare cap (deliberate 2:1 asymmetric ratio, reflecting "primarily" not "fully"
   provider control); per-event cap 50% of the applicable annual cap; zero painshare floor;
   no cross-year carry-forward; 24-month clawback window. Explicitly modelling assumptions,
   not universal contractual standards.
4. **SLA modelling defaults set:** 48-hour permit/customer approval cycle; 24-hour production
   access following an agreed intervention window. Architecture rule confirmed:
   contract-specific baseline → agreed SLA → attribution exclusion where the customer
   dependency exceeds the SLA.
5. **Cycle 4 design work completed before any Gate 3 modelling:**
   - Over-maintenance/KPI-gaming control (Maintenance Intensity Index + Risk Reduction
     Efficiency, three-condition Red Flag Trigger, symmetric under-maintenance detection) —
     `07_KPI_ATTRIBUTION/overmaintenance_control.md`.
   - Intervention netting mechanism (observation window, causally-connected-equipment
     monitoring, net-value calculation, payment held pending window closure or VVB
     acceptance) — `07_KPI_ATTRIBUTION/intervention_netting.md`.
   - Event 4 decision tree revised to v3, incorporating the materiality gate, netting
     interaction, SLA-driven exclusion, and over-maintenance context —
     `07_KPI_ATTRIBUTION/event4_decision_tree_v3.md`.
   - New Event 9 (Turnaround Execution Efficiency) designed from the outset with an
     independent (jointly-selected) benchmark requirement, directly applying the lesson from
     Event 6's conflict-of-interest failure — `07_KPI_ATTRIBUTION/event9_turnaround_execution_efficiency.md`.
6. **Gate 3 readiness verdict: PASS WITH CONDITIONS** — see
   `07_KPI_ATTRIBUTION/gate3_readiness_assessment.md`. Six remaining gaps logged (causal-
   connection map, independent TA benchmark provider not yet named, uncalibrated MII/RRE
   bands, unconfirmed netting observation window length, two unconfirmed materiality-
   extension interpretations, and the entirely undesigned advisory/transformation fee
   structure for strategic asset value).

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
