# Value Double-Counting Map — Cycle 3

Rule: **only the PRIMARY VALUE EVENT may be commercially monetized.** SECONDARY KPI EFFECTs
and CONTEXT EFFECTs are reported (feeding the KPI Pyramid, protocol Section 10) but never
independently priced. Every Value Validation Board submission requires a mandatory
cross-reference check against every other event category touching the same asset,
root-cause, or time period before approval.

| Event | PRIMARY monetization | SECONDARY KPI effect (reported, not paid) | CONTEXT effect (reported, not paid) | Explicit anti-double-count rule |
|---|---|---|---|---|
| **1 — Contractor productivity delta** | Contractor rate/cost pool | Schedule compliance | Maintenance cost trend, turnaround performance | TA-related contractor costs are excluded from Event 1 entirely and reserved for Event 5 — no overlap by construction |
| **2 — Planned work conversion** | None (KPI-fee only, per `event_stress_test.md`) | Wrench time, emergency-work reduction | Cost | If a Value Validation Board reviewer suspects the same underlying scheduling improvement is being claimed as both an Event 1 rate gain and an Event 2 narrative, only Event 1 may be monetized — Event 2 has no € value to double-count in the first place |
| **3 — Repeat failure avoided** | That specific asset's reliability event | MTBF, availability, production loss avoided | Maintenance cost | For the same underlying failure/root cause, **only one** of {Event 3 gainshare, Event 4 painshare-avoidance} may ever be monetized. Event 4 applies going forward only to new/different failures — it may never re-litigate an Event 3 outcome |
| **4 — Maintenance-attributable production loss** | That specific event, decision-tree-adjudicated | — (this is the "final common pathway"; no further rollup) | Annual availability (reported only — **never a payment metric**, confirmed by Scenario 9) | Cannot be triggered for the same root cause as an already-decided Event 3 claim (see above) |
| **5 — Turnaround scope reduction** | That specific TA scope item | — | Reliability improvement (if the same root cause also generated an Event 3 payout) | If an Event 3 payout already occurred for a given root cause, the same root cause cannot also generate an Event 5 payout for TA scope removal — Event 3 is treated as primary since it is typically identified first; the TA effect is context only |
| **6 — Lifecycle Capex deferral** | That specific asset's deferral | — | TA scope planning (if the deferred asset was also a candidate TA scope item) | An asset's replacement/scope item may be monetized under only one event category — whichever triggers first; mandatory cross-reference check required at submission |

## Structural design confirmation
No event in this table monetizes an aggregate metric (total maintenance cost, annual
availability, MTBF as a standalone payment trigger) — every payment-eligible claim is
traceable to one specific, individually-adjudicated event. This is a direct, structural
consequence of Petri's original instruction not to design attribution around total OEE, and
Scenario 9 in `ATTRIBUTION_DISPUTE_SCENARIOS.md` confirms why that instruction was correct:
an aggregate-availability dispute has no tractable resolution path, while a single-event
dispute does.

## Residual risk
The cross-reference check depends on Value Validation Board diligence at submission time —
it is a procedural control, not a structural impossibility of double-counting. If the VVB is
under-resourced or rushed, double-counting risk re-emerges. This is why
`VALUE_VALIDATION_BOARD_MVP.md` requires a completeness declaration and named evidence
attachments at submission, not a simple checkbox.
