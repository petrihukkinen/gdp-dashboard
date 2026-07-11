# Customer Problem Tree — Cycle 1 Draft

Grounded in AMOR 2020 evidence where possible (Level A), otherwise flagged Level C
(hypothesis, generalized from the protocol's structural problem list — not yet validated
against any customer beyond the 2020 Neste/OPP case).

For each problem: economic consequence, who owns it, why unsolved internally, external
influenceability, measurability, contractual attributability.

## 1. Fragmented, hourly-rate subcontractor base (Level A — evidenced)
- **Economic consequence:** €68m/yr of the €129m baseline is subcontracting spend (A5) —
  the single largest cost category, larger than own personnel (A5: BC+WC = €32m).
  Hourly-rate structures reward time spent, not output.
- **Who owns it:** Historically the customer's own procurement/maintenance organisation
  (fragmented ownership is itself the symptom).
- **Why unsolved internally:** Requires consolidating relationships and renegotiating from a
  position of aggregated volume — hard for an internal function without integrator scale
  or mandate; AMOR 2020's own answer was to create an external entity with exactly this
  mandate (A13).
- **Can an external provider influence it?** Yes — this is the best-evidenced value pool in
  the entire source document (17-20m€/yr claimed potential, A10).
- **Measurable?** Yes — contractor spend, rate cards, hours vs. output are directly
  measurable.
- **Attributable?** Largely yes — contractor management is close to fully
  provider-controlled once mandate is granted, making it one of the cleanest candidates for
  early-phase, high-confidence contracting (see `05_VALUE_POOLS/`).

## 2. Low hands-on-tool-time / high waiting time (Level A — evidenced)
- **Economic consequence:** Largest single claimed value pool in the source (€24-29m/yr,
  A10) — larger than contractor management.
- **Who owns it:** Jointly — work-permit delay is often operations/HSE-owned, not
  maintenance-owned; workflow/scheduling delay is more directly maintenance-owned.
- **Why unsolved internally:** Requires cross-functional authority (permits sit with
  operations, not maintenance) that an internal maintenance function alone typically lacks.
- **Can an external provider influence it?** Partially — a provider can fix its own workflow
  and scheduling discipline, but work-permit delay requires customer operations cooperation.
  This is a live attribution problem: AMOR 2020 bundled "workflow" and "work permit" into one
  number without separating what's provider-controlled from what's customer-controlled
  (A10) — exactly the gap the protocol's Section 7 (Controllability and Attribution) warns
  against.
- **Measurable?** Yes, with time-and-motion / CMMS work-order data — assuming CMMS data
  quality is adequate (itself a named problem, see below).
- **Attributable?** Partially — needs a split value pool (see `05_VALUE_POOLS/`), not one
  blended number.

## 3. Aging asset base / lifecycle and statutory replacement risk (Level A — evidenced)
- **Economic consequence:** €5-10m/yr claimed (€10-15m/yr including the tank farm/T26
  project specifically) (A10).
- **Who owns it:** Jointly — Capex decisions and funding sit with the customer; the
  provider can only recommend and plan.
- **Why unsolved internally:** Requires long-horizon lifecycle/reliability engineering
  capability that's expensive to maintain in-house at less-than-fleet scale.
- **Can an external provider influence it?** Only partially — this is explicitly named as a
  Capex-dependent, customer-controlled value pool in the protocol's own attribution
  framework (Section 7, category H). AMOR 2020 does not separate the plan from the
  provider's ability to actually execute it without customer Capex approval.
- **Measurable?** Yes for the underlying condition data; the *savings* are harder to isolate
  from normal Capex cycles.
- **Attributable?** Low-to-medium — jointly influenced at best, not provider-controlled.

## 4. Organisational inefficiency / unclear roles (Level A — evidenced)
- **Economic consequence:** €2-3m/yr claimed (A10) — smallest of the four named pools, but
  real: 350 FTE with unclear WC role definition (source itself calls for "all WC will be
  evaluated, role defined, and placed in the right position").
- **Who owns it:** The customer's own organisation, historically.
- **Why unsolved internally:** Restructuring one's own function is politically harder than
  having an external, arms-length entity do it — this is arguably the *real* reason the MBO
  structure was attractive to Neste, more than the cost numbers themselves (Level C
  inference).
- **Can an external provider influence it?** Yes, directly, once given a transfer/reassign
  mandate.
- **Measurable?** Yes.
- **Attributable?** Fully provider-controlled once the transfer occurs.

## 5. CMMS / work-order data quality (Level A — named, not sized)
- **Economic consequence:** Not sized independently in the 2020 source — folded into the
  "CMMS project started" bullet with no dollar figure. This is itself notable: a properly
  sized "Digital" value pool per the protocol's Section 6 architecture does not exist yet in
  the evidence base.
- **Who owns it:** Jointly — systems are typically customer-owned platforms (ALVAR/M+
  named, A14) even when the maintenance provider is the primary user.
- **Why unsolved internally:** Systems investment competes with other Capex priorities and
  lacks a single accountable owner when maintenance is fragmented across many contractors.
- **Can an external provider influence it?** Partially — data entry discipline yes; system
  platform ownership/investment, no, unless explicitly transferred (as AMOR 2020 optioned).
- **Measurable?** Yes, but only once a baseline data-quality metric is defined — not done in
  2020 source.
- **Attributable?** Currently unclear — flagged as a gap, not a validated pool.

## Problems named in the protocol but with zero evidence in the AMOR 2020 material (Level C
— must be tested with real customers before being treated as material)
Spare parts working capital, obsolescence management, shortage of skilled personnel,
predictive/condition monitoring maturity, shutdown/turnaround overruns specifically (named
only as an exclusion, "Effects due to TA," A11, never sized), siloed maintenance
disciplines beyond the org redesign already covered above.

## Cycle 1 conclusion on Gate 1
Three material, credibly-measurable value pools exist in the evidence base (contractor
management, own-organisation efficiency, and — with a split — the provider-controlled
portion of hands-on-tool-time). That is enough to draft Gate 1 pass criteria (≥3 material
pools), **provided** the hands-on-tool-time and lifecycle/reliability pools are explicitly
split into provider-controlled vs. jointly-influenced components before being used in any
commercial model — see `05_VALUE_POOLS/value_pool_tree.md`.
