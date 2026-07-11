# Pull-Through Conflict Protocol — Cycle 10

## The agency problem, stated plainly
A provider that controls orchestration may also recommend additional work it wants to sell
and execute. The Control Tower identifies a reliability problem. The same provider
recommends a large project. The same provider wants to execute it. The customer CFO's
question is exactly right: **"Are you optimizing my asset or your revenue?"** This is a real
conflict of interest, not a hypothetical one, and it directly threatens the trust that
Mechanisms 1-3 (`FIVE_ECONOMIC_MECHANISMS.md`) depend on if left unaddressed.

## Safeguards, tiered by materiality

**Below a defined materiality threshold** (small, routine work, consistent with the
materiality gate already used elsewhere in this architecture — `07_KPI_ATTRIBUTION/CONTRACT_LANGUAGE_RISK.md`):
normal course of business. The provider recommends and executes without additional process.

**Above the threshold:**
1. **Open-book recommendations** — full cost and scope disclosure for any recommended
   project, not a black-box quote.
2. **Independent technical challenge** — the customer's own engineering function, or a
   named third party, can challenge the recommendation's technical justification before any
   commitment.
3. **Customer approval rights** — the customer retains final sign-off on any pull-through
   scope or spend, always.

**Above a higher threshold:**
4. **Mandatory competitive tender** — even if the provider is permitted to bid, the work
   must be competitively tendered, not automatically awarded to the incumbent. This
   directly bounds Mechanism 4's realistic upside: pull-through is a *lead-generation*
   advantage (the provider sees the opportunity first and understands the asset), not a
   *guaranteed-award* advantage.

**Structural, not just contractual:**
5. **Separation of recommendation and sales incentives.** Individuals or teams identifying a
   need (reliability engineers, asset health analysts) should not be personally or directly
   incentivized on the revenue of the resulting project. This is an organizational design
   principle for the provider, not merely a contract clause — it cannot be enforced by the
   customer, only committed to by the provider's own management.
6. **Value Validation Board role.** For larger-value pull-through opportunities, the VVB's
   remit can extend to reviewing whether a recommendation was technically justified rather
   than revenue-motivated — reusing existing governance infrastructure rather than inventing
   a new one.

## What this protocol does not solve
Competitive tender requirements and independent technical challenge add real friction and
cost to pull-through work, which is exactly why Mechanism 4 in `FIVE_ECONOMIC_MECHANISMS.md`
treats pull-through as a real but bounded, not guaranteed, value driver. If customers report
in validation (`18_INTERVIEW_QA/CUSTOMER_CFO_VALIDATION.md`, Q10) that they would require
independent tender for *everything* regardless of relationship quality, Mechanism 4's
economic contribution should be modeled at or near zero, not assumed away.
