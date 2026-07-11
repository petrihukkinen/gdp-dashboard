# Model A — Base Fee + KPI Fee

High fixed Base Fee, limited variable compensation, Event 3 gainshare used selectively,
Event 4 painshare capped tightly. All figures illustrative per `modelling_assumptions.md`.

## 1. Revenue architecture

- **Base Fee:** €24,000,000/yr (high, covers most delivery cost)
- **KPI Fee:** Event 2 (€160,000, Normal Year) + Event 1 converted into a KPI-fee-style bonus
  band (not a full value-share) — max €700,000, paid at 50% of max in a Normal Year =
  €350,000
- **Performance/Gainshare fee:** Event 3 pursued **selectively** — only claims judged
  cost-effective to formally adjudicate are brought forward (deliberately reduces claims
  bureaucracy, see `cfo_tests_and_claims_bureaucracy.md`); modelled at 40% of the addressable
  Event 3 population pursued
- **Painshare:** Event 4, capped tightly — annual cap 10% of Base Fee = €2,400,000; per-event
  cap 50% of that = €1,200,000
- **Advisory/Transformation fee boundary:** Event 6 replacement, €500,000/yr, sold and priced
  entirely separately from the risk corridor — never blended into KPI/gainshare accounting

## 2. Provider economics (Normal Year)

| Line | Amount |
|---|---|
| Base Fee | €24,000,000 |
| Event 1 (KPI-bonus mechanic) | €350,000 |
| Event 2 (KPI Fee) | €160,000 |
| Event 3 (selective gainshare, provider's 40% share of the 40%-pursued portion) | €248,000 |
| Event 4 (painshare) | €0 |
| **Total Normal Year Provider Revenue** | **€24,758,000** |

Variable compensation = 3.2% of Base Fee — genuinely low-powered, as designed.

- **Gross margin logic:** the high Base Fee is priced to cover full delivery cost plus target
  margin on its own — variable comp is upside on top, not core margin.
- **Margin-at-risk:** low. Even a fully-capped painshare year (€2,400,000, i.e. the full
  annual cap consumed) reduces total revenue by <10% — the Base Fee absorbs most volatility.
- **Maximum annual downside:** €2,400,000 (annual painshare cap) against €24,000,000 Base
  Fee — a bounded 10% downside.
- **Maximum annual upside:** Event 1 bonus cap €700,000 + full Event 3 pursuit (if the
  provider chose to stop being "selective") up to the gainshare cap €4,800,000 — realistic
  practical upside closer to €1,500,000-2,000,000 given selective pursuit is the deliberate
  strategy.
- **Working-capital exposure:** low — most compensation is fixed and paid on the normal
  Base Fee invoicing cycle; only the selectively-pursued Event 3 claims carry netting-window
  exposure (see cash-flow section).
- **Payment timing:** Base Fee monthly (standard); Event 1/2 KPI fee monthly/quarterly per
  the VVB cadence table; Event 3 subject to the 180-day netting delay on whatever is pursued.

### Cash-flow effect of the 180-day netting window (Event 3 only)

On the €248,000 Model A Event 3 provider share:
| Settlement option | Provider working capital gap | Administrative cost |
|---|---|---|
| Full deferred settlement | Up to €248,000 for up to 6 months | Lowest |
| Provisional accrual (70%) with true-up | ~€74,000 (30% of claim) | Medium — requires true-up reconciliation |
| Partial payment with holdback (50/50) | ~€124,000 | Medium |

Given Model A's low reliance on Event 3 (selective pursuit, small absolute amounts), the
netting delay is not commercially material here — a genuine strength of the "primarily
KPI Fee" design.

## 3. Customer economics (Normal Year)

- **Fixed cost:** €24,000,000 (Base Fee) — highly predictable
- **Variable payment:** €758,000 (3.1% of fixed cost) — low budget variance
- **Verified gross value addressed** (value pool actually touched by pursued events): Event 1
  full value €1,400,000 (assumed delivered as ordinary good service, funded by the high Base
  Fee, not solely because of the bonus) + Event 3 pursued portion €620,000 (40% of
  €1,550,000) = €2,020,000
- **Provider compensation for that value:** €350,000 + €248,000 = €598,000
- **Customer retained value:** €2,020,000 − €598,000 = **€1,422,000**, *plus* the
  **unpursued 60% of Event 3's value (€930,000)**, which — under the "equal underlying
  delivery" assumption in `modelling_assumptions.md` — the customer still receives
  operationally (fewer repeat failures) even though it was never formally claimed or paid
  for. **Total customer benefit if delivery quality holds regardless of incentive: up to
  €2,352,000.**
- **Downside protection:** strong — tight painshare cap limits customer's *compensation* in
  a bad year (see `model_comparison_and_stress_test.md`), but the customer's *cost* exposure
  is also the most predictable of the three models.
- **Budget predictability:** highest of the three models — 96.9% of total spend is the fixed
  Base Fee.

## 4. The real trade-off this model makes
Model A structurally assumes the provider will deliver strong underlying performance because
the Base Fee funds it and the relationship/reputation depends on it — not because a large
variable payment forces the issue. That assumption is the central commercial bet of Model A,
and it is exactly the kind of assumption a skeptical provider CFO would defend (predictable
margin) and a skeptical customer CFO would attack (weak forcing function) — see
`cfo_tests_and_claims_bureaucracy.md` and `commercial_red_team.md`.
