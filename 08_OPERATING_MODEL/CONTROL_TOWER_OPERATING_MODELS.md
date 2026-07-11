# Three Control Tower Operating Models — Cycle 11

No winner selected — per instruction, not chosen on elegance. Each is a legitimate answer
to a different scale/maturity condition.

## Model A — Site Heavy
Dedicated Contract Director, Contractor Integration Lead, Asset Performance Lead, and
Commercial Controller, all resident at the site; minimal shared/central support.
- **Dedicated site roles:** all four core roles.
- **Shared roles:** none.
- **Central roles:** none.
- **Customer-transferred work:** absorbed locally, not pooled.
- **New work:** fully loaded onto this one site.
- **Scalability:** Poor — every new site requires a full replicated team; cost scales
  roughly linearly with site count, no economies of scale.
- **Operational risk:** Low — maximum local presence and responsiveness.
- **Customer credibility:** High — the customer sees dedicated people who know their site.
- **Likely cost behavior:** highest cost per site, but the only credible model for a **first,
  single-site pilot**, since there is no portfolio to share against yet.

## Model B — Hybrid
Minimum site leadership (Contract Director + Contractor Integration Lead only — the two
roles the zero-based analysis found genuinely non-shareable) plus shared regional/central
capabilities (Asset Performance Lead, Commercial Controller, Data Analyst, VVB support
pooled across multiple accounts).
- **Dedicated site roles:** Contract Director, Contractor Integration Lead.
- **Shared roles:** Asset Performance Lead, Commercial Controller, Data Analyst, VVB
  support.
- **Central roles:** methodology maintenance (attribution logic, governance templates).
- **Customer-transferred work:** can be absorbed by shared capacity if genuinely
  transferred.
- **New work:** concentrated in the two dedicated roles.
- **Scalability:** Good — shared roles' fixed cost amortizes once a critical mass (roughly
  3+ accounts, see `CONTROL_TOWER_SCALE_CURVE.md`) exists.
- **Operational risk:** Medium — shared resources could be stretched thin during
  simultaneous peak demand across accounts (e.g. multiple Event 4 adjudications at once).
- **Customer credibility:** Medium-high — requires honest positioning that some support
  functions are shared, not a pretense that everything is dedicated.
- **Likely cost behavior:** a real fixed site-dedicated floor plus a declining shared-cost
  curve as the portfolio grows.

## Model C — Platform Heavy
Only Contractor Integration Lead resident on site; everything else — including Contract
Director relationship management, partially remote — centralized/pooled aggressively across
a large multi-site portfolio.
- **Dedicated site roles:** Contractor Integration Lead only.
- **Shared/central roles:** everything else.
- **Customer-transferred work:** absorbed centrally.
- **New work:** minimal per incremental site once the platform exists.
- **Scalability:** Best in theory — lowest marginal cost per additional site.
- **Operational risk:** Highest — thin local presence risks the orchestration-authority
  claim looking hollow to a skeptical site director, directly threatening Falsification
  Register #3/#4.
- **Customer credibility:** Lowest of the three at small portfolio scale — a customer being
  asked to consolidate scope and commit long-term may reasonably distrust a thin,
  remote-support-dependent structure. Credibility likely improves only once the platform has
  a demonstrated multi-site track record — a real chicken-and-egg problem.
- **Likely cost behavior:** high fixed central-platform investment upfront, very low
  marginal cost per site added — the model most in need of scale to look attractive, and
  most at risk of the "pilot falsely appears uneconomic" trap (`CONTROL_TOWER_SCALE_CURVE.md`).

## Observation, not a selection
Model A is the only credible shape for a genuine first pilot. Model B is the plausible
pragmatic target for the first 3-5 real accounts. Model C only becomes attractive once a
real multi-site portfolio exists — which requires surviving Model A/B economics first, not
before.
