# Control Tower Unit Economics — Cycle 11

Updates `alv_model_illustrative.csv` with two new rows rather than creating a conflicting
model — `accountability_single_pilot_realistic` and `accountability_portfolio_scale_realistic`.
All figures remain indexed and illustrative — no Bilfinger or real customer data.

## Incremental cost bridge, in numbers

| Scenario | Conventional mgmt cost (% revenue) | AMOR dedicated site (Category B) | AMOR shared, portfolio-amortized | AMOR shared, single-pilot unamortized | Total AMOR incremental vs. conventional |
|---|---|---|---|---|---|
| Portfolio scale (Model B/C, 5+ accounts) | 8% (baseline, same as conventional) | +2% | +1.5% | — | **~3.5%** |
| Single pilot (Model A, no sharing) | 8% | +2% | — | +5-6% | **~7-8%** |

## Cross-cycle validation
Cycle 10's stress test used 8% Control Tower cost as its pessimistic scenario, producing a
net illustrative value of ~72 (versus a 148 base case at 3% cost). **This cycle's
zero-based, bottom-up analysis independently arrives at ~7-8% as the realistic cost for a
genuine single-pilot deployment** — meaning Cycle 10's "stress test" was not a pessimistic
hypothetical, it was close to the *realistic* number for exactly the situation (a first
deal) most likely to occur first. This is a materially important finding: **the thesis's
"worst case" from Cycle 10 is likely to be encountered on day one, not as a tail risk.**

## Break-even logic
Even at single-pilot-realistic cost (~7-8%, `accountability_single_pilot_realistic` row),
the illustrative net value is **~75**, versus the conventional baseline's **~49** — still a
real, positive advantage (roughly 1.5x), just far more modest than the 3x shown at portfolio
scale (`accountability_portfolio_scale_realistic`, ~157 at 2% cost). **The thesis does not
break even at zero or negative advantage even under realistic single-pilot cost stress — it
delivers a smaller, not absent, advantage.** The advantage grows substantially only once a
real multi-account portfolio exists to amortize shared/central cost.

## Sensitivity ranking (most to least decisive)
1. **Control Tower shared-cost amortization** (single pilot vs. portfolio) — the single
   largest swing factor tested across Cycles 10-11.
2. **Whether customer-transferred work materializes** (`CUSTOMER_DUPLICATION_TEST.md`) — if
   the customer retains its own duplicate coordination staff, the system-level case weakens
   even if the provider's own P&L still works.
3. **Additional scope revenue actually captured** (Mechanism 1's realization).

## What this means for deal sequencing
The first deal should be priced and evaluated using **single-pilot economics (Model A, ~7-8%
incremental cost)**, not portfolio-scale assumptions — pricing or pitching the first customer
using Model B/C's shared-cost economics would overstate the achievable advantage and risk a
credibility failure once real costs appear. The path to the full 3x advantage runs through
survivable single-pilot economics first, not around them.
