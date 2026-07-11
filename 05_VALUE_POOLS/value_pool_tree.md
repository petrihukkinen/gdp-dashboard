# Value Pool Tree — Cycle 1 Draft

For each pool: baseline, value driver, controllability, measurement, financial value,
attribution, contract suitability. Financial values are AMOR 2020's own "potential" figures
(A10) — Level A as claims made in the source, Level C as validated economics (the source
itself states due diligence was never performed, A11). Treat all € figures below as
illustrative of the shape of the opportunity at one refinery site, not as forecasts for
AMOR 2030.

## Pool 1 — Contractor Management
- **Baseline:** €68m/yr subcontracting spend (largest cost category, A5).
- **Value driver:** Consolidation to fewer, larger partners; hourly-rate → lump-sum
  conversion; integrator-managed KPIs and productivity targets.
- **Controllability:** **CORRECTED (2026-07-11, per Petri): "Primarily provider-controlled,
  with defined customer dependencies"** — not "fully provider-controlled" as Cycle 1
  originally stated. The customer retains real influence via: approved-supplier lists,
  procurement contracts, vendor lock-in situations, labor/union constraints, work-permit
  processing, work prioritization, and Capex decisions. Any commercial model using this
  pool must carve out these dependencies explicitly rather than assume clean provider
  control. See `RISK_REGISTER.md` for the painshare exposure this correction protects
  against.
- **Measurement:** Contractor spend by category, rate-card benchmarking, output-per-hour
  where measurable, contractor KPI scorecards.
- **Financial value:** €17-20m/yr claimed potential (A10).
- **Attribution:** Strong but not clean — best candidate in the pool set for early-phase
  fixed-fee contracting, and a credible performance-fee candidate **once the customer
  dependencies above are named and excluded** from the attribution formula, not before.
- **Contract suitability:** High — suitable from Phase 1 (Transformation) onward; Phase 3/4
  performance-fee eligible only with explicit customer-dependency carve-outs in the contract.
- **Design note:** this pool is the clearest example of "Control Tower Economics" — the
  provider's value is in orchestrating and holding accountable a network of contractors it
  does not fully control end-to-end, not in performing the work itself. See
  `03_STRATEGIC_THESIS/control_tower_economics.md`.

## Pool 2 — Own-Organisation Efficiency
- **Baseline:** ~350 FTE own resources; €32m/yr combined BC+WC personnel cost (A5).
- **Value driver:** Role redefinition, right-sizing, org restructuring from technical-
  discipline silos to maintenance-function structure.
- **Controllability:** **Provider-controlled once the workforce transfers to the provider,
  subject to labor/union agreement constraints** (softened per the same 2026-07-11
  correction — this pool is cleaner than Pool 1 but still not unconditionally "fully"
  controlled where collective agreements constrain restructuring pace or method).
- **Measurement:** Headcount vs. plan, cost per FTE, role-utilization tracking.
- **Financial value:** €2-3m/yr claimed potential (A10) — smallest pool in dollar terms, but
  cleanest attribution in the set.
- **Attribution:** Highest-confidence pool in the set, labor/union constraints aside.
- **Contract suitability:** High for a fixed-fee model; too small alone to anchor a
  performance-fee story, but a good "prove the model works" pool for Phase 1-2.

## Pool 3 — Hands-on-Tool-Time (SPLIT — this is the pool the 2020 source got wrong by
bundling)
The source bundles "workflow" and "work permit" delay into one €24-29m/yr figure (A10).
These have different owners and must be split for any credible commercial model:

### 3a. Workflow / scheduling delay
- **Controllability:** **Provider-controlled** (planning quality, material staging,
  scheduling discipline are maintenance-execution functions).
- **Attribution:** Clean.
- **Contract suitability:** Good Phase 2-3 candidate.

### 3b. Work-permit delay
- **Controllability:** **Jointly influenced** — permits are typically issued by customer
  operations/HSE, not maintenance.
- **Attribution:** Requires a joint improvement commitment (e.g. permit-issuance SLA from
  the customer) before any part of this can enter a payment mechanism. Cannot be a pure
  provider KPI.
- **Contract suitability:** Context/management KPI only until a joint SLA exists — not
  payment-eligible in early phases.

**Combined financial value:** €24-29m/yr claimed potential (A10), but this number should not
be presented as a single provider-attributable figure until split and re-sized. Flag to
Petri as a specific fix versus the 2020 original.

## Pool 4 — Lifecycle & Reliability Management
- **Baseline:** Not separately costed in source; value pool is framed as risk-based Capex
  avoidance/deferral.
- **Value driver:** Lifecycle plans for critical rotating equipment, risk-based replacement
  for statutory equipment, reliability engineering (RCM/FMEA/RCA-type discipline — named in
  protocol, not detailed in 2020 source).
- **Controllability:** **Jointly influenced at best** — the provider can recommend and plan,
  but Capex funding and approval sit with the customer (protocol Section 7, category H).
- **Measurement:** Asset health/criticality indices, MTBR trend (A9), deferred/avoided Capex
  events.
- **Financial value:** €5-10m/yr claimed potential (€10-15m/yr incl. tank farm/T26 project,
  A10).
- **Attribution:** Genuinely hard — avoided-Capex savings require a credible counterfactual
  baseline, which is one of the harder value validation problems in the entire protocol
  (Section 8). Do not put this pool into a gainshare model without a Value Validation Board
  and an agreed avoided-loss methodology.
- **Contract suitability:** Phase 4 candidate at the earliest, and only with strong joint
  governance — not a Phase 1-3 pool.

## Pool 5 — Digital / CMMS Data Quality (named, not sized)
- **Baseline:** Unsized in source; qualitative bullet only ("CMMS project started").
- **Value driver:** Data quality as an enabler of every other pool's measurement — this pool
  doesn't generate savings directly, it makes every other pool's attribution possible.
- **Controllability:** Jointly influenced — platform ownership typically sits with customer
  (ALVAR/M+ named, A14), but the provider's data discipline drives quality.
- **Measurement:** Not defined in source — needs a data-quality baseline methodology before
  Gate 2.
- **Financial value:** Unknown — flagged, not fabricated.
- **Attribution:** N/A until sized.
- **Contract suitability:** Foundational — belongs in the Standard Core (Section 13),
  not a payment-linked pool itself.

## Reconciliation note (answers `OPEN_QUESTIONS.md` Q4 — updated 2026-07-11)
Sum of the "potential" figures across pools 1-4: €48-62m/yr at one site. The AMOR 2020
source's own committed target was ~€17m/yr improvement by year 5 (from €129m to €112m,
A6) — roughly a **third of the low end** of its own stated potential, and per Petri's direct
confirmation (`EVIDENCE_REGISTER.md` B4), **neither number was ever achieved** — the
proposal was never executed. Both figures are proposal-stage estimates only.

Petri's instruction: stop treating "potential" and "committed" as two competing numbers to
reconcile after the fact, and instead build every value pool through his adopted formula:

**Identified Value × Controllability × Realization Probability × Time-to-Impact =
Committable Value**

This refines the protocol's Section 15 Realized Value formula for this project by splitting
"provider influence" into two distinct factors (Controllability — is this pool
provider-controlled, jointly-influenced, or customer-controlled, per the corrected tagging
above — and Realization Probability — given control, how likely is the value to actually
materialize) and adding Time-to-Impact (some value, like contractor rate renegotiation, lands
in months; some, like avoided lifecycle Capex, takes years — a commercial model that treats
them identically will misprice both). First worked application of this formula is in
`07_KPI_ATTRIBUTION/attribution_architecture.md`.
