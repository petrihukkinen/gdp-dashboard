# Provider Risk Corridor — Cycle 3

Role: service provider CFO. Status: Level C proposal — structure is a design recommendation;
specific percentages are illustrative ranges for Petri/commercial team to set, not decided
figures. Do not quote the example numbers below as commitments.

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

## Proposed risk corridor structure

| Element | Design | Illustrative range (NOT decided) |
|---|---|---|
| **Deadband** | Performance within ±X% of baseline triggers no payment either direction — filters noise from signal | e.g. first 5% deviation, either direction |
| **Threshold** | Gainshare starts only once the deadband is cleared on the favorable side; painshare (Event 4 only) starts only once cleared on the unfavorable side | Tied to deadband |
| **Cap** | Gainshare capped as a % of Base Fee per year; painshare capped materially **lower** than the gainshare cap — asymmetric, reflecting "primarily" not "fully" provider control | e.g. gainshare cap 30-40% of Base Fee/yr; painshare cap 5-15% of Base Fee/yr |
| **Collar** | Combined cap + floor: painshare floor at zero (provider fee never negative even at worst-case attribution); gainshare capped at the upside limit | — |
| **Annual Maximum Exposure** | A single hard number bounding total painshare liability for the year, regardless of how many Event 4 adjudications occur | To be set by Petri/commercial team |
| **Event-Level Maximum Exposure** | No single Event 4 adjudication may exceed a set fraction of the annual cap — prevents one catastrophic event from consuming the full year's exposure alone | e.g. no single event >50% of the annual cap |
| **Aggregate Exposure** | Sum of all painshare events in a year is hard-capped at the Annual Maximum regardless of event count | — |
| **Carry-forward** | Unused gainshare-eligible value does NOT bank forward into future years (avoids incentive to time-shift claims); painshare shortfalls in one year are NOT clawed back against future gainshare without explicit multi-year agreement — years stay largely independent to limit compounding disputes | — |
| **Clawback** | Any event found within an 18-24 month review window to rest on incomplete/incorrect data, or where Event 6's mandatory clawback trigger fires, must be reversed with repayment | Window: 18-24 months, illustrative |

## What is NOT yet resolved
The actual numeric values above are commercial decisions, not architecture work — logged as
a required Petri decision in the Cycle 3 final output. Working capital and reserve sizing
are Gate 3 financial-modelling tasks, not addressed here.
