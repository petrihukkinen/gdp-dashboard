# Accountability Economics Tree — Cycle 10

Building the economic logic from first principles. No Bilfinger or customer numbers —
variables and relationships only.

## Definitions

- **Account Revenue** = Base scope revenue + Pull-through revenue (projects/TA/reliability/
  digital/engineering) + selective module revenue (Contractor Productivity, Turnaround).
- **Contract Duration** = initial term + expected renewal-driven extension.
- **Renewal Probability** = f(earned retention quality, competitive rebid pressure,
  relationship health) — must be *earned*, not assumed (see `EARNED_RETENTION_PROTOCOL.md`).
- **Share of Wallet** = % of the customer's total addressable industrial services spend
  captured by this provider.
- **Gross Margin** = Account Revenue − direct delivery cost (labor, subcontractor pass-
  through, materials).
- **EBITA Margin** = Gross Margin − SG&A / account management / Control Tower operating cost.
- **Sales Cost** = cost to win the account initially.
- **Rebid Cost** = cost incurred at each renewal/rebid cycle.
- **Transition Cost** = cost to mobilize new scope at contract start (data onboarding,
  decision-rights architecture, Causal Connection Map if applicable).
- **Working Capital** = cash tied up in delayed billing, module netting windows, and
  transition-phase investment.
- **Risk Cost** = expected value of Event 4 painshare exposure plus broader liability now
  carried under wider scope.
- **Performance Downside** = the bounded Event 4 corridor exposure specifically — a subset
  of Risk Cost.
- **Pull-through Revenue** = incremental revenue from projects/TA/reliability/digital/
  engineering work surfaced through the orchestration relationship.
- **Customer Concentration Risk** = the *provider's portfolio-level* risk of overweighting
  revenue/margin in a small number of large, long accounts — not an account-level variable,
  but must be modeled at the portfolio level.

## Conceptual Account Lifetime Value (ALV)

```
ALV = Σ_t [Account Revenue(t) × Gross Margin%(t) − Control Tower Operating Cost(t)
           − Risk Cost(t)] × discount factor(t)
      − (Sales Cost + Transition Cost) at t=0
      − Σ Rebid Cost at each renewal point
      weighted by cumulative Renewal Probability
      − portfolio-level Customer Concentration Risk discount
```

## The actual claim under test

The Accountability Economics Thesis does **not** claim higher margin. It claims that even
at flat or slightly lower Gross Margin%, ALV can be superior because:
1. **Sales Cost and Transition Cost amortize over more years** (longer Duration).
2. **Rebid Cost is incurred less frequently** (higher Renewal Probability, if earned).
3. **Account Revenue is larger** (higher Share of Wallet).
4. **Pull-through Revenue adds margin-accretive volume** (often higher-margin project/
   engineering work, not baseline maintenance labor) — *if* the agency-conflict safeguards
   in `PULL_THROUGH_CONFLICT_PROTOCOL.md` hold and customers actually award it without
   mandatory competitive tender every time.

This is a fundamentally different economic story than "we charge more" (Model 2) or "we earn
fees per event" (Model 1). It is a classic B2B services-scale story: fewer, larger, longer,
better-retained accounts, with a bounded downside. See `ACCOUNT_LIFETIME_VALUE_MODEL.md` for
the illustrative sensitivity test of this logic, and `FIVE_ECONOMIC_MECHANISMS.md` for each
driver's individual stress test.

## What could break this
Every term on the cost side of the ALV formula (Control Tower Operating Cost, Risk Cost,
Transition Cost, Rebid Cost) scales *with* scope and duration, not independently of them.
The thesis only holds if these costs scale *slower* than Account Revenue and Renewal
Probability do. Nothing in this project has proven that yet — it is the single largest
open question carried into Cycle 11.
