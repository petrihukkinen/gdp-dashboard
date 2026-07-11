# Model B — Base Fee + Atomic Value Share

Lower Base Fee, meaningful Event 1/3 upside, real Event 4 downside, Event 9 performance
reward, the atomic event ledger is the primary commercial engine. All figures illustrative
per `modelling_assumptions.md`.

## 1. Revenue architecture

- **Base Fee:** €16,000,000/yr (lower — 33% below Model A's, reflecting that more
  compensation is earned through the ledger)
- **KPI Fee:** Event 2, €160,000 (unchanged — this is architecturally fixed by the underlying
  attribution reality, not a commercial choice; it doesn't vary by model)
- **Performance/Gainshare fee:** Event 1 and Event 3 pursued in **full** (not selectively) —
  the atomic ledger is meant to be exhaustively used, not curated for simplicity
- **Painshare:** Event 4, full exposure up to the risk corridor — annual cap 10% of Base Fee
  = €1,600,000; per-event cap 50% of that = **€800,000**
- **Advisory/Transformation fee boundary:** same as Model A, €500,000/yr, fully separate

## 2. Provider economics (Normal Year)

| Line | Amount |
|---|---|
| Base Fee | €16,000,000 |
| Event 1 (40% gainshare split of €1,400,000 verified value) | €560,000 |
| Event 2 (KPI Fee) | €160,000 |
| Event 3 (40% gainshare split of €1,550,000 post-netting value) | €620,000 |
| Event 4 (painshare) | €0 |
| **Total Normal Year Provider Revenue** | **€17,340,000** |

Variable compensation = 8.4% of Base Fee — meaningfully higher-powered than Model A, but
**note the headline finding: total Normal-Year provider revenue (€17,340,000) is still
€7,418,000 lower than Model A's (€24,758,000).** A "lower base, higher variable" model does
not out-earn a high-base model in an ordinary year — it only closes the gap, or overtakes,
in a high-value year (see `model_comparison_and_stress_test.md`). This is a genuine,
non-obvious finding, not an artifact — it should shape how this model is pitched.

- **Gross margin logic:** Base Fee alone may not fully cover delivery cost + target margin —
  the model is designed to require gainshare participation to reach target profitability,
  which is a real structural risk if a Normal Year underperforms the illustrative inputs.
- **Margin-at-risk:** higher than Model A in absolute terms relative to Base Fee — a
  painshare year consuming the full €1,600,000 annual cap is **10% of Base Fee**, same ratio
  as Model A, but against a smaller revenue base it bites harder in practice.
- **Maximum annual downside:** €1,600,000 (annual painshare cap, smaller absolute number than
  Model A because Base Fee is smaller).
- **Maximum annual upside:** gainshare cap €3,200,000 (20% of €16,000,000) — realistically
  achievable if Event 1/3/5/9 all land well in a strong year.
- **Working-capital exposure:** materially higher than Model A — the atomic ledger carries
  more of total compensation, and Event 3's 180-day netting window now delays a larger
  absolute amount.
- **Payment timing:** same cadence structure as Model A, but a larger share of total
  compensation flows through the delayed Event 3 channel.

### Cash-flow effect of the 180-day netting window (Event 3, full €620,000 provider share)

| Settlement option | Provider working capital gap | Administrative cost |
|---|---|---|
| Full deferred settlement | Up to €620,000 for up to 6 months | Lowest |
| Provisional accrual (70%) with true-up | ~€186,000 | Medium |
| Partial payment with holdback (50/50) | ~€310,000 | Medium |

At Model B's scale, full deferred settlement is a **material** working-capital item (3.9% of
Base Fee tied up for half the year) — this model needs the provisional-accrual or holdback
option to be commercially workable, unlike Model A where it barely matters. **Recommendation
carried into `gate3_verdict.md`: provisional accrual with true-up is the default
recommendation for Model B specifically, not a universal choice.**

## 3. Customer economics (Normal Year)

- **Fixed cost:** €16,000,000 — lower, but less predictable as a share of total spend
- **Variable payment:** €1,340,000 (8.4% of fixed cost) — more budget variance than Model A
- **Verified gross value addressed:** full €2,950,000 (Event 1 + Event 3, both fully pursued)
- **Provider compensation for that value:** €560,000 + €620,000 = €1,180,000
- **Customer retained value:** €2,950,000 − €1,180,000 = **€1,770,000**
- **Downside protection:** weaker in relative terms — Event 4 exposure is fully live (not
  "selectively" limited as in Model A's ethos, though the cap numbers are the same
  percentage), so more real painshare years are likely to occur.
- **Budget predictability:** lower than Model A — 92.3% fixed vs. 96.9%.

## 4. The real trade-off this model makes
Model B bets that a genuinely high-powered incentive produces better, more consistently
evidenced performance than Model A's Base-Fee-funded goodwill — at the cost of real
provider margin volatility and materially higher working-capital and claims-processing
burden. It is the model most exposed to the claims-bureaucracy question in
`cfo_tests_and_claims_bureaucracy.md`.
