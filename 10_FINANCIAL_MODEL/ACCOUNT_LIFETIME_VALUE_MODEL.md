# Account Lifetime Value Model — Cycle 10

**All figures below are indexed, illustrative modelling variables, not Bilfinger or real
customer data.** Purpose: test whether the Accountability Economics Thesis's internal logic
is coherent and identify which variables the conclusion is most sensitive to — not to
forecast real revenue. A companion illustrative CSV is at
`10_FINANCIAL_MODEL/alv_model_illustrative.csv`.

## Illustrative inputs (indexed, Year-1 base revenue = 100)

| Variable | Conventional maintenance contract | Accountability-based relationship |
|---|---|---|
| Annual base revenue (index) | 100 | 180 (larger scope, Mechanism 1) |
| Contract duration (initial term) | 3 years | 5 years |
| Renewal probability per cycle | 50% | 70% (earned retention, Mechanism 3 — tested at 50% below too) |
| Gross margin | 15% | **14%** (flat/slightly lower — no price premium assumed) |
| Sales cost (one-time, % of Yr-1 revenue) | 8% | 8% |
| Rebid cost (% of annual revenue, per renewal event) | 5% | 5% (incurred less often — every 5yrs, not every 3) |
| Transition cost (one-time, % of Yr-1 revenue) | 3% | 5% (larger, more complex mobilisation) |
| Control Tower operating cost (% of revenue) | 0% (N/A) | **3%** (tested at 8% below) |
| Risk reserve (% of revenue) | 1% | 2% (broader scope, more Event 4 exposure) |
| Pull-through revenue (% of base) | 5%, ad hoc | 12% (Mechanism 4), at an assumed 20% margin |

## 10-year illustrative comparison

**Conventional:** expected revenue-years ≈ 5.4 of 10 possible (geometric decay across 3-year
cycles at 50% renewal). Net illustrative value ≈ **49** (index units) after sales, rebid,
transition, and risk costs.

**Accountability-based (base case, 70% renewal):** expected revenue-years ≈ 8.5 of 10 (two
5-year cycles at 70% renewal). Net illustrative value ≈ **148** — roughly 3x the
conventional case, despite flat/lower margin%, purely from scope + duration + renewal +
pull-through effects.

## Sensitivity tests — what actually drives the result

| Stress test | Net illustrative value | Change vs. base case |
|---|---|---|
| Base case (as above) | ~148 | — |
| Renewal probability fails (70% → 50%, same as conventional) | ~121 | **-18%** — the model is fairly robust to this failing; scope and duration are doing more work than renewal probability alone |
| Pull-through fails entirely (Mechanism 4 = 0) | ~112 | -24% — real, but not the deciding factor |
| **Control Tower operating cost triples (3% → 8%)** | **~72** | **-51% — the single largest swing of any variable tested** |

**Finding: the thesis's advantage over a conventional contract is real and directionally
robust across most stress tests, but it depends more on controlling Control Tower operating
cost than on any other variable — more than renewal probability, more than pull-through.**
This is the sharpest, most decision-relevant output of this model: the biggest unproven risk
to the whole Accountability Economics Thesis is not customer behavior, it's whether the
Control Tower can actually be run efficiently. See `FIVE_ECONOMIC_MECHANISMS.md`, Mechanism
5, and `ACCOUNTABILITY_ECONOMICS_RED_TEAM.md`, item 5.

## What this model does not do
It does not forecast real revenue, real margin, or real Bilfinger numbers. It tests internal
logical coherence and sensitivity only. Real inputs require the external validation work in
`18_INTERVIEW_QA/` and real provider cost data neither this project nor an interview process
can produce.
