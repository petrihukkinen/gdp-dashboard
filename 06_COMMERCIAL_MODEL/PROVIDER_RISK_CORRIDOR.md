# Provider Risk Corridor — Cycle 3 design, Cycle 4 numbers decided by Petri

Role: service provider CFO. Status: structure designed in Cycle 3; **Petri set the actual
modelling figures in Cycle 4 (2026-07-11)** — these are Gate 3/Cycle 4 **modelling
assumptions**, not final contractual terms, and are explicitly labeled as such below.

## Provider CFO questions, answered against this architecture

**What is the maximum annual downside?** Bounded by the Annual Maximum Exposure cap below —
by design, never open-ended. This is the single most important fix relative to AMOR 2020,
which had no painshare at all and therefore no precedent for this question.

**Can one event wipe out contract margin?** Not if the Event-Level Maximum Exposure cap is
respected — see below. Without it, yes: a single Event 4 (production loss) adjudication
could otherwise be catastrophic, especially given how "Very High" its dispute potential is
(`event_stress_test.md`).

**Are painshare risks symmetrical with gainshare?** **No, deliberately asymmetric.** Only
Event 4 carries painshare exposure. Events 3, 5, 6 are gainshare-only — the provider is never
penalized for failing to avoid a loss where customer-side factors (Capex, operating
decisions, funding) are material co-determinants. This directly reflects the corrected
controllability tagging ("primarily provider-controlled," never "fully").

**Does the provider carry production-margin volatility?** No — Event 4's financial value
uses an agreed, contract-fixed standard margin set at signing, not the spot margin at time of
event. This protects the provider from being penalized more heavily during a high-margin
period and protects the customer from being under-compensated during a low-margin one.

**Are customer delays protected?** Yes, via the SLA exclusion logic in Events 2 and 4 (Step
3.5) — but the actual SLA numbers are not yet set (`CONTRACT_LANGUAGE_RISK.md`), so this
protection is designed but not yet operative.

**Is Capex dependency protected?** Yes for Events 3, 5, 6 — funding-source declaration is
now mandatory and customer-funded interventions are excluded from gainshare by default
(`CUSTOMER_CFO_ATTACK.md`).

**Are force majeure clauses enough?** Force majeure is listed as an Event 4 exclusion
(`event_stress_test.md`) but the clause itself is not drafted in this project — a standard
contract-law item, flagged as needed at Gate 3, not a gap specific to this architecture.

**Is the provider financing customer value creation?** Only where the provider itself funds
an intervention (e.g. Event 3's RCA-driven fix) — this is a real, deliberate feature of the
model (skin in the game), not a flaw, but it means working capital planning must account for
it. See below.

**How long is value measured?** Per-event, tied to each event's own evaluation window
(explicit per event in `event_stress_test.md`); no open-ended multi-year measurement window
exists anywhere in the architecture.

**Can gainshare be clawed back?** Yes for Event 6 by design (mandatory clawback if the asset
fails before actual replacement), and generally for any event later found to rest on
incomplete/incorrect data — see Clawback Rules below.

**What working capital is required?** Not sized in this session — flagged as a Gate 3
financial-modelling task, not fabricated here. The Control Tower Economics model
(`03_STRATEGIC_THESIS/control_tower_economics.md`) implies the provider fronts orchestration
and, for some events, intervention cost ahead of gainshare realization — this working-capital
need should be explicitly modelled, not assumed away.

**What reserves are needed?** Same — flagged for Gate 3, sized against the Annual Maximum
Exposure figure once set.

## Risk corridor structure — Cycle 4 modelling assumptions (Petri, 2026-07-11)

| Element | Design | Cycle 4 modelling value |
|---|---|---|
| **Deadband** | Performance within ±X% of baseline triggers no payment either direction | **±5%** |
| **Threshold** | Gainshare starts once the deadband is cleared favorably; painshare (Event 4 only) starts once cleared unfavorably | Tied to deadband |
| **Annual gainshare cap** | Cap on total gainshare as a % of annual Base Fee | **20% of annual Base Fee** |
| **Annual painshare cap** | Cap on total painshare as a % of annual Base Fee | **10% of annual Base Fee** — deliberate **2:1 asymmetric ratio**, reflecting that the relevant outcomes are primarily provider-controlled, with defined customer dependencies, but not fully provider-controlled |
| **Per-event cap** | No single adjudication may exceed a fraction of the applicable annual cap | **50% of the applicable annual cap** (gainshare or painshare) |
| **Painshare floor** | Provider's fee can never go negative | **Zero — Base Fee cannot become negative** |
| **Carry-forward** | Whether unused capacity/shortfall banks across years | **None — no cross-year carry-forward** |
| **Clawback window** | Period within which a paid claim can be reversed if later found unsound | **24 months** |

These are **modelling assumptions for Cycle 4/Gate 3, not universal AMOR contractual
standards** — Petri's explicit framing. Real contracts may set different figures per
customer/site.

## What is still open
Working capital and reserve sizing against these now-fixed caps are Gate 3 financial-
modelling tasks, not addressed here. The 24-month clawback window interacts with
`07_KPI_ATTRIBUTION/intervention_netting.md`'s payment-sequencing delay — both extend how
long value claims stay provisional, a cumulative effect not yet modelled together.
