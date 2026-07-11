# Model C — Control Tower + Value Modules

Control Tower/management-system base fee, separately priced operational modules, atomic
value events activated only for agreed value pools, strategic asset value sold through
advisory/transformation engagements. All figures illustrative per `modelling_assumptions.md`.

## 1. Revenue architecture

- **Control Tower Fee:** €8,000,000/yr — pure orchestration/planning/performance-visibility/
  accountability fee, per `03_STRATEGIC_THESIS/control_tower_economics.md`. This is the
  "Base Fee" for risk-corridor cap purposes in this architecture — a deliberate structural
  choice with consequences (see below).
- **Operational Modules:** €14,000,000/yr — separately priced delivery capacity (the actual
  maintenance labor/contractor-management capability), structured similarly to a service fee
  but itemized as distinct modules rather than one blended Base Fee.
- **Activated atomic value events (this configuration):** Events 1 and 3 only — the two
  events with the cleanest Cycle 3 attribution rating. This is a **modelling choice for this
  illustrative configuration**, not a structural requirement of Model C — a real Model C
  contract could activate more or fewer events by module.
- **Advisory/Transformation fee:** €500,000/yr, explicitly the home of all strategic asset
  value (Event 6's replacement) and any other lifecycle/transformation consulting — the
  clearest possible separation of the three monetisation engines of any of the three models.

## 2. Provider economics (Normal Year)

| Line | Amount |
|---|---|
| Control Tower Fee | €8,000,000 |
| Operational Modules | €14,000,000 |
| Event 1 (40% gainshare split) | €560,000 |
| Event 3 (40% gainshare split, post-netting) | €620,000 |
| Advisory/Transformation Fee | €500,000 |
| **Total Normal Year Provider Revenue** | **€23,680,000** |

This lands close to Model A's €24,758,000 — **a coincidence of the illustrative inputs
chosen, not a designed equivalence.** The point of the comparison is structural risk profile
and clarity, not revenue parity, which is not something this exercise should optimize for.

- **Gross margin logic:** the Control Tower Fee is priced as a pure orchestration margin
  (likely higher gross margin % than delivery-heavy Operational Modules, though this isn't
  quantified here — flagged as a Cycle 6 modelling item) — Operational Modules likely carry
  the delivery-cost-heavy, lower-margin bulk of revenue.
- **Margin-at-risk / structural consequence of the small Control Tower base:** because risk
  corridor caps are set against the Control Tower Fee alone (€8,000,000), not total contract
  value (€22,500,000+), the caps are proportionally much smaller in absolute euros: gainshare
  cap = 20% × €8,000,000 = **€1,600,000**; painshare cap = 10% = **€800,000**; per-event caps
  €800,000/€400,000. **This is a real design tension, not a footnote:** Model C's structure
  gives the smallest absolute room for gainshare of the three models even though its total
  contract value is comparable to Model A's — flagged explicitly for Red Team
  (`commercial_red_team.md`, Scenario 7).
- **Maximum annual downside:** €800,000 (smallest of the three models in absolute terms).
- **Maximum annual upside:** €1,600,000 (also smallest in absolute terms) — Model C as
  configured here is the **least gainshare-geared** of the three, despite "atomic value
  events activated" language, because the cap base is small.
- **Working-capital exposure:** moderate — similar per-event dynamics to Model B for the two
  activated events, but smaller absolute amounts due to the smaller cap base.
- **Payment timing:** Control Tower Fee and Operational Modules on standard cycles; Event 1/3
  subject to the same cadence and netting-window rules as the other models.

### Cash-flow effect of the 180-day netting window (Event 3, €620,000 provider share)
Identical dynamics to Model B (same absolute Event 3 share) — see that file's table. Same
recommendation: provisional accrual with true-up.

## 3. Customer economics (Normal Year)

- **Fixed cost:** €22,000,000 (Control Tower + Modules combined) — structurally itemized,
  arguably more auditable than a single blended Base Fee (a customer CFO can see exactly what
  they pay for orchestration vs. delivery).
- **Variable payment:** €1,180,000 (Events 1+3) + €500,000 (Advisory) = €1,680,000
- **Verified gross value addressed:** €2,950,000 (same underlying value pool as Model B,
  since the same two events are activated)
- **Provider compensation for that value:** €1,180,000
- **Customer retained value:** €2,950,000 − €1,180,000 = **€1,770,000** (identical to Model
  B for the activated events, since the same 40/60 split and same events apply)
- **Downside protection:** the smallest painshare cap of the three models in absolute terms
  (€800,000) — protects the provider more than it compensates the customer in a bad year.
- **Budget predictability:** itemization (Control Tower vs. Modules vs. Advisory) may improve
  *transparency* even where it doesn't improve predictability of total spend.

## 4. The real trade-off this model makes
Model C's clarity — separating orchestration, delivery, atomic value, and strategic advisory
into four distinct commercial lines — is its main selling point to a sophisticated customer,
and it is the model most consistent with `03_STRATEGIC_THESIS/control_tower_economics.md`'s
design principle. Its structural cost is the smallest risk-corridor cap base of the three,
which needs an explicit decision: should caps be set against the Control Tower Fee alone
(as modelled here) or against total contract value (Control Tower + Modules)? **This is a
required Petri decision, not resolved by this cycle** — see `gate3_verdict.md`.
