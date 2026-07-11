# Red Team Review — Cycle 1

Attacking the Cycle 1 output. Maker responses inline. Unresolved items promoted to
`OPEN_QUESTIONS.md` or `RISK_REGISTER.md`.

## "Why will the customer say no?"
Because AMOR 2020 itself shows the customer (Neste/OPP) wanted control retained — approval
rights over budget, spares ownership retained, a reversion clause on exit
(`STRATEGIC_THESIS.md`). A customer who structured that much control retention in a
trust-based MBO with its own former managers is unlikely to hand a stranger-company
gainshare rights over lifecycle Capex decisions. **Maker response:** Accepted — this is
exactly why Architecture B excludes lifecycle/reliability from payment KPIs in year 1. Not
resolved, but correctly scoped around.

## "Where can the provider lose money?"
Fixed-price years 3-5 in the 2020 model, with no visible collar or exclusion for turnaround
overruns (explicitly excluded from the savings figures, A11, but not clearly excluded from
the fixed-price scope itself). If AMOR 2030 repeats fixed-price-for-turnarounds without an
explicit TA exclusion clause, the provider inherits open-ended shutdown risk. **Maker
response:** Flagged to `RISK_REGISTER.md` — turnaround/TA pricing exclusion must be explicit
in any Phase 2+ commercial architecture; not yet resolved, correctly deferred to Gate 3.

## "Which KPI can be manipulated?"
"Budget compliance" as a KPI (A9, slide 23) can be gamed by deferring necessary spend into
future periods — exactly the reliability-erosion risk that shows up 2-3 years later as
unplanned failures. This is a real weakness in the *original* AMOR 2020 KPI set that AMOR
2030 must not inherit. **Maker response:** Accepted. Any 2030 KPI Pyramid must pair a cost
KPI with a leading reliability KPI (e.g. backlog growth, PM compliance) as a check —
substantive design work for Gate 2, not resolved here.

## "Which savings are double counted?"
Hands-on-tool-time (workflow half) and own-organisation efficiency both plausibly capture
some of the same underlying improvement (a better-organized workforce also has less waiting
time). AMOR 2020 doesn't address this overlap. **Maker response:** Accepted as a real risk;
`05_VALUE_POOLS/value_pool_tree.md` does not yet include an explicit non-overlap allocation
rule — flagged as Gate 2/3 work, not fabricated here.

## "What cannot be measured?"
The counterfactual for lifecycle/reliability avoided-Capex savings — "what would have failed
if we hadn't done this" is inherently unfalsifiable without a control group, which a single
refinery doesn't have. **Maker response:** This is why pool 4 was explicitly kept out of any
payment mechanism in Architecture B and flagged as needing a Value Validation Board even in
Architecture C. Correctly identified as a structural, not just execution, limitation.

## "What depends on customer behavior?"
Work-permit delay (pool 3b) entirely. **Maker response:** Already split out and excluded
from payment eligibility — see `value_pool_tree.md`.

## "What is impossible to standardize?"
The founder-trust governance model AMOR 2020 relied on ("mutual trust and respect," slide
26) is explicitly a single-relationship asset, not a repeatable process. If AMOR 2030's moat
turns out to rest on "the right people know the right customer," it is not a scalable
platform business — it's a collection of bespoke relationships wearing one brand.
**Maker response:** This is the sharpest unresolved critique from Cycle 1. Genuinely
unresolved — promoted to `RISK_REGISTER.md` as the "model becomes bespoke consulting"
risk, and to `OPEN_QUESTIONS.md` implicitly via Q5 (does Petri want to preserve the
relationship-driven MBO logic or move to a process-driven platform model — these have very
different answers to this exact Red Team question).

## "What is merely consulting language?"
The evolution ladder itself (Labour Provider → ... → Outcome-Based Strategic Partner) reads
as a maturity-model slide with no evidence behind rungs 4-7. **Maker response:** Accepted
and already stated plainly in `STRATEGIC_THESIS.md`'s verdict — the ladder is a hypothesis
frame, not a proven progression, and this document says so rather than dressing it up.

## Red Team's overall verdict
The Cycle 1 work does not oversell itself — its own internal documents (Strategic Thesis,
Value Pool Tree, Checker Review) already surface most of these objections before Red Team
had to. The two genuinely unresolved, high-severity issues are: (1) whether the model can
ever be more than a relationship-dependent, bespoke arrangement at scale, and (2) the
turnaround/shutdown pricing exposure. Both are correctly logged as open, not papered over.
