# Gate 3 Modelling Assumptions — Cycle 5

**Every number in this file and everything derived from it is an illustrative modelling
assumption, not real customer data, not a market benchmark, and not a forecast for any
actual contract.** Built to test whether the architecture is arithmetically and structurally
sound — per Petri's explicit instruction not to invent market data. Where a real number would
be needed for an actual deal, that is flagged, not guessed at as fact.

## Illustrative Site

- Annual Contract Value (ACV): **€40,000,000**
- Annual Base Fee (Models A/B reference point): **€20,000,000** (Models A/B/C vary this — see
  each model file)
- Materiality threshold check: max(€100,000, 0.25% × €40,000,000 = €100,000) = **€100,000**
  — both criteria coincide by construction of this illustrative ACV, which keeps the worked
  example transparent.

This scale is loosely informed by the *shape* of the AMOR 2020 baseline (a large single-site
refinery maintenance contract, `EVIDENCE_REGISTER.md` A5) but is **not** the AMOR 2020
figures reused as fact — it is roughly 30% of AMOR 2020's €129m total maintenance cost
baseline, reflecting that Base Fee here covers core managed delivery, not full pass-through
subcontracting and materials spend.

## Cycle 4 risk corridor, applied

Deadband ±5%; annual gainshare cap 20% of the model's own Base Fee; annual painshare cap 10%
(2:1 asymmetric ratio); per-event cap 50% of the applicable annual cap; painshare floor
zero; no cross-year carry-forward; 24-month clawback.

## Illustrative atomic value-event inputs (Normal Year)

Not the AMOR 2020 figures — independently scaled illustrative inputs for this exercise,
using the Identified Value × Controllability × Realization Probability × Time-to-Impact =
Committable Value formula (`05_VALUE_POOLS/value_pool_tree.md`).

| Event | Identified Value | Controllability | Realization Probability | Time-to-Impact | Committable/Verified Value (Normal Year) |
|---|---|---|---|---|---|
| 1 — Contractor productivity delta | €2,500,000 | 0.8 | 0.75 (mature year) | 1.0 (fast) | **€1,400,000** (after ~5% deadband haircut, rounded) |
| 2 — Planned work conversion | N/A — no €-avoidance methodology (per `event_stress_test.md`) | — | — | — | **KPI Fee pool €200,000; paid at 80% achievement = €160,000** |
| 3 — Repeat failure avoided | 3 qualifying claims × €600,000 = €1,800,000 gross | 0.7 | 0.6 (case-by-case VVB uncertainty) | delayed by 180-day netting (cash-flow effect modelled separately) | **€1,550,000 post-netting** (2 claims paid in full €1,200,000; 1 claim reduced to €350,000 after a documented secondary failure mode nets against it) |
| 4 — Production loss (painshare) | Variable, event-specific | Contested by default | N/A | N/A | **€0 in Normal Year** (assumed no qualifying provider-attributable events — modelled explicitly in stress scenarios) |
| 5 — TA scope reduction | €400,000 when a TA occurs | 0.6 | 0.65 | TA-cycle only | **€0 in Normal (non-TA) Year** — modelled in TA-year note |
| 9 — TA Execution Efficiency | €300,000 when a TA occurs | 0.75 | 0.6 | TA-cycle only, requires pre-agreed independent benchmark | **€0 in Normal Year; not activatable at all until benchmark provider is contractually named (Petri's Cycle 5 decision 5)** |
| 6 — Lifecycle Capex deferral | Excluded from gainshare entirely | — | — | — | **N/A — routed to Advisory/Transformation Fee, €500,000/yr illustrative flat fee** |

## Gainshare split assumption (new, required for Gate 3, not previously set)

Modelling assumption: **40% of verified net value to provider, 60% retained by customer**
for gainshare-type events (1, 3, 5, 9). This is a conventional gainshare split shape, not a
benchmark claim — **flagged as a required Petri/commercial decision**, not fixed. Event 2
(KPI Fee) and Event 4 (painshare) are not value-shares and are not subject to this split —
Event 2 is a flat fee for hitting a target; Event 4 flows from provider to customer when
attributable.

## Cash-flow settlement options for the 180-day netting window (Petri's decision 1)

Modelled explicitly, not assumed to be immediate payment — see each model file's cash-flow
section:
1. **Full deferred settlement** — provider receives nothing until the window closes.
2. **Provisional accrual with final true-up** — provider receives a partial amount (modelled
   at 70%) on submission, trued up (or clawed back) after the window closes.
3. **Partial payment with holdback** — a fixed 50/50 split between submission and window
   close.

## Explicit simplifying assumption (disclosed, not hidden)

This model assumes **equal underlying operational performance across all three commercial
architectures** in the Normal Year scenario — the same improvements are assumed to occur
regardless of how they are commercially packaged. This is necessary for a clean comparison,
but it is not free: weaker variable incentives (Model A) carry a qualitative risk that the
provider is less motivated to pursue and evidence value diligently over time (the classic
principal-agent problem in fixed-price contracting). This risk is named, not quantified —
see `commercial_red_team.md`.
