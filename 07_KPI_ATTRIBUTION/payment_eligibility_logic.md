# Payment Eligibility Logic — Cycle 4 Consolidated

**Superseded by Cycle 6, 7, and 8** (`06_COMMERCIAL_MODEL/cycle6_complexity_kill_test.md`,
`cycle7_mva_hardening.md`, `cycle8_event1_survivability.md`). Event 2 is REPORTING ONLY.
**Event 3 — original design and every restructured successor (flat reward, severity-banded
reward, annual pool) — is killed entirely.** Reliability value is managed and reported
(context/management KPIs), never individually monetized. Event 4 remains the downside
corridor — decision tree unchanged, now the subject of a commercial-to-legal drafting brief
(`cycle8_event1_survivability.md`, Task 11) separating performance economics from
catastrophic-loss liability. Events 5 and 9 are reporting-only by default, available via an
optional Turnaround Value Module with a site-wide, minimum-term anti-selection rule.

**As of Cycle 8: Event 1 is also reclassified — from core payment event to an optional
"Contractor Productivity Value Module,"** activated only for customers passing a five-
condition eligibility gate, using a time-limited (not perpetual) savings-share design on a
rolling-baseline-plus-cohort architecture, and explicitly not underwritten as guaranteed
provider revenue.

**The true, final core of AMOR is: Base-Fee-funded Control Tower + Event 4 downside
corridor. This is complete and differentiated on its own — see
`cycle8_event1_survivability.md`, Task 9. The Contractor Productivity Value Module and the
Turnaround Value Module are both optional, additive, and customer-specific.** The X/Z
naming from Cycle 6 is retired per Petri's Cycle 8 decision — there is one core architecture
plus optional modules, not a maturity ladder.

Organized around the three monetisation engines Petri named. No engine, and no event within
it, aggregates into total OEE, annual availability, or absolute maintenance cost.

## Engine 1 — Productivity Value → Verified Cost Saving / Gainshare

| Event | Payment type | Status |
|---|---|---|
| 1 — Contractor productivity delta | KPI Fee (Phase 1) → Performance Fee (Phase 3+) | Requires the job-complexity-normalized catalog (`event_stress_test.md`) before contract-ready |
| 2 — Planned work conversion | KPI Fee only | Not gainshare-eligible — no direct €-avoidance methodology exists |

Materiality threshold (€100,000 or 0.25% of Annual Contract Value, whichever higher) is
named by Petri specifically for Events 3/4. Event 1 aggregates many small work orders into a
periodic rate calculation rather than discrete per-event claims, so a per-event threshold
doesn't map cleanly — **proposed interpretation, not silently assumed:** apply the
threshold at the periodic (e.g. quarterly) claim level for Event 1, not per work order.
Requires Petri confirmation.

## Engine 2 — Reliability Value → Performance Fee / Event Reward

| Event | Payment type | Status |
|---|---|---|
| 3 — Repeat failure avoided | Gainshare, case-by-case | Subject to materiality threshold, `intervention_netting.md` hold, VVB sign-off, annual gainshare cap (20% of Base Fee), per-event cap (50% of applicable annual cap) |
| 4 — Maintenance-attributable production loss | Painshare (sole downside event) | Subject to materiality threshold, `event4_decision_tree_v3.md`, annual painshare cap (10% of Base Fee), per-event cap, zero floor, no carry-forward, 24-month clawback |
| 5 — Turnaround scope reduction | Gainshare, Phase 4 only | Subject to materiality threshold, condition (c) customer co-sign |
| 9 — Turnaround Execution Efficiency (new) | Gainshare / event reward, Phase 3-4 | Subject to materiality threshold, independent benchmark provider prerequisite |

## Engine 3 — Strategic Asset Value → Advisory / Transformation Fee

| Event | Payment type | Status |
|---|---|---|
| 6 — Lifecycle Capex deferral | **Removed from gainshare entirely**, per Petri's Cycle 4 decision | Strategic asset-life/lifecycle optimisation value is monetized as a professional advisory/transformation service fee, not as a claimed avoided-cost figure — this sidesteps the provider-set-baseline conflict of interest by not pricing it as "avoided cost" at all. Full commercial fee structure is Gate 3 work, not designed here (would violate "do not begin commercial pricing optimisation") |

## Cross-cutting gates (never payment KPIs)

| Item | Role |
|---|---|
| Event 7 — permit/customer approval cycle | Gate/SLA input — 48-hour Cycle 4 modelling default |
| Event 8 — CMMS data quality | Gate — no event is payable for a period where data quality is below threshold |
| Materiality threshold | Gate — €100,000 or 0.25% ACV (whichever higher); named for Events 3/4, proposed extension for Event 1 (needs confirmation), naturally satisfied by scale for Events 5/9 |
| Over-maintenance / under-maintenance Red Flag | Suspends related claims pending VVB review — `overmaintenance_control.md` |
| Intervention netting | Holds Event 3 (and overlapping Event 9) payment until the observation window closes or VVB accepts residual risk — `intervention_netting.md` |

## What is structurally guaranteed
No metric anywhere in this table is an aggregate (total cost, annual availability, fleet-wide
OEE). Every payable claim traces to one specific, individually-adjudicated, materiality-
gated event. This property was validated in Cycle 3 (Scenario 9) and preserved unchanged in
Cycle 4.
