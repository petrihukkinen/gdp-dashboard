# Cycle 8 — Core Economic Survivability Test (Event 1)

Attempting to kill the last core payment event, per Petri's explicit instruction. All figures
illustrative, clearly labeled, not real customer or market data.

## Task 1 — Event 1 value persistence across a 10-year contract

Let B = frozen mobilisation baseline rate, R(t) = actual rate in year t, Delta(t) = B − R(t)
(positive = saving), split = provider's illustrative 40% share (per `10_FINANCIAL_MODEL/`).

| Scenario | Verified delta pattern | Annual gross customer value | Provider compensation logic (current, unmodified) | Customer retained value | Provider incentive | Baseline relevance | Likely CFO objection |
|---|---|---|---|---|---|---|---|
| A — One-time step change (Y1-2) | Delta jumps once, then flat for 8 years | Constant, e.g. €1,400,000/yr | Provider paid 40% of a *constant* delta every year for 8 years after the work was done once | Constant 60% share | **Zero incentive after Year 2** — gets paid for doing nothing | Increasingly stale — Year-0 baseline says less and less about "what the rate should be" by Year 8 | **"You fixed this three years ago. Why am I still paying you every month?"** |
| B — Diminishing returns | Large early gain, shrinking annual increments | Rising then flattening | Cumulative payment grows even larger than A over 10 years; bulk of payment still tracks the aging initial win | Similar erosion | Weak after early years | Stale, same as A | Same objection, muted slightly by ongoing small increments |
| C — Continuous improvement | New increments every year | Growing | **Only scenario where "ongoing share" is defensible as designed** — but only if payment ties to *marginal* new delta, not the full stacked delta against Year-0 | Grows with the improvement | Strong, sustained | Baseline should track marginal improvement, not stay fixed | Minimal, if marginal-only payment is used |
| D — Savings reversal | Delta shrinks/reverses later | Falls, possibly to zero | **Genuine strength of the current design:** since delta is measured against *current* actual rate each period, deterioration automatically shrinks payment — self-correcting | Falls correspondingly | Renewed incentive to fix the regression | Baseline itself unaffected | Low — the mechanism already handles this correctly |
| E — Market catch-up | Wider contractor market improves independent of AMOR | Baseline (Year-0) becomes an easy target to beat for reasons unrelated to the provider | Provider paid for **exogenous** improvement it didn't cause | Reduced — customer overpays for market drift | Distorted — rewards being present, not being effective | Fully invalidated — Year-0 baseline reflects nothing about current market reality | "Why am I paying you for something the whole market did anyway?" |

**The naive "share of frozen-baseline delta, paid indefinitely" design fails Scenarios A, B,
and E outright, and only works as designed in Scenario C.** The worked math makes this
concrete: on Scenario A's illustrative numbers, cumulative provider payment over 8
post-improvement years = 40% × €1,400,000 × 8 = **€4,480,000** for what may have been a few
months of Year-2 contract renegotiation work — an indefensible ratio once stated plainly.

## Task 2 — Perpetual Rent Test

| | A. Perpetual share | B. Time-limited share | C. Declining share | D. Baseline reset | E. Hybrid (B/C + D) |
|---|---|---|---|---|---|
| Customer fairness | **Fails** — the €4.48m math above | Good — bounded to the value-creation window | Good, smoother cliff | Good if reset is genuine | Best, if it works |
| Provider incentive | Rewards inertia after Year 2 | **Creates pressure to keep finding new wins** to replace expiring old ones — genuinely good alignment | Similar, smoother | Strong incentive to **sandbag before a reset** (classic ratchet-effect gaming) | Same reset-gaming risk as D, on top of B/C's complexity |
| Revenue durability (provider) | High but indefensible | Requires continuous new-cohort generation | Same | Vulnerable to reset-timing disputes | Most durable in theory, most complex in practice |
| Audit burden | Low (no expiry tracking) | Moderate — needs per-improvement vintage/expiry tracking | Moderate-high — needs decay schedules | Moderate — needs reset-date governance | **Highest** — inherits all of the above |
| Baseline gaming | Low direct exposure (delta not time-boxed) | Reduced — less incentive to defend an old baseline forever | Reduced | **High** — the central weakness | High, inherited from D |
| Transformation incentive | None after initial win | Good | Good | Good, if reset isn't gamed | Good in theory |
| Continuous-improvement incentive | None | **Strong** | Moderate | Moderate, undermined by sandbagging risk | Strong in theory |
| Contract renewal effect | Provider has no reason to keep improving before renewal | Provider must keep improving to sustain revenue | Similar | Renewal date and reset date create a second gaming surface | Most renewal-aligned, most complex |

**Verdict: is ongoing lifetime savings share commercially defensible? NO for the unmodified
perpetual design (A).** A bounded design is defensible **ONLY WITH CONDITIONS.**

**Recommended architecture: Time-limited share (B), not the fuller hybrid (E).** D/E's
reset-gaming risk is serious enough — and this project has repeatedly found that operability
beats theoretical completeness (Cycle 6) — that a simpler, bounded-life-per-improvement
design is preferable even though it is not fully theoretically optimal. Each verified
improvement gets a defined monetisation life (illustrative: 3 years); payment sunsets
automatically at expiry regardless of whether the saving persists operationally; new
improvements are tracked as fresh, independently-dated cohorts.

## Task 3 — Savings pool exhaustion test

Contractor productivity opportunity behaves as a depleting resource, not a renewable one, at
any given customer: large at a high-inefficiency starting point, shrinking for an already-
mature customer, minimal for an already-optimized or low-contractor-spend customer.

**The named failure case — the provider performs exceptionally well, removes the major
productivity losses, and thereby destroys its own future Event 1 revenue — is real, and it
is not unique to AMOR.** Any compensation model tied to *improvement* rather than *steady-
state operation* has this property; it is not a design flaw specific to this project. **This
is (b) a pricing issue and (c) a contract-duration issue, combined — not (d) proof Event 1
cannot be a value mechanism, but it is real evidence Event 1 cannot be the sole PERMANENT
upside engine for a 7-10 year contract.**

The correct response is not to engineer Event 1 to last forever (Task 2 already showed that
doesn't work) but to **explicitly design the commercial model around the natural arc**:
meaningful Event 1 upside in the early transformation years (1-3), with Base Fee
periodically repriced upward to reflect the now-durably-improved, leaner cost base the
provider helped create — effectively harvesting proven Event 1 gains into permanent Base Fee
revenue — rather than expecting Event 1 to remain productive indefinitely. No replacement
payment event is proposed; this is a duration/pricing design point, not an architecture gap.

## Task 4 — Baseline decay and market catch-up

| Option | Handles market catch-up? | Handles perpetual-rent? | New risk introduced |
|---|---|---|---|
| Fixed mobilisation baseline | No | No | Staleness (Task 1E), perpetual-rent driver |
| Rolling baseline (trailing 12-24mo) | **Yes, naturally** — market-wide movement is continuously absorbed into the reference | **Yes, naturally** — old improvements roll out of the comparison window over time, producing smooth decay without an explicit expiry rule | Smooths *legitimate* provider-driven gains too, unless paired with cohort tracking |
| Indexed baseline (named cost/wage index) | Partial — handles inflation, not market-wide efficiency gains | No | Narrower fix than rolling |
| Periodic independent rebasing | Yes, if genuinely independent | Yes | Same sandbagging/ratchet risk as Task 2's Option D, plus real cost of an independent-party relationship (echoes Event 9's benchmark-cost lesson) |
| Customer-specific counterfactual benchmark | Yes, in principle | Yes, in principle | **Reintroduces exactly the counterfactual-valuation problem that killed Event 3 in Cycle 7. Avoid.** |
| No long-term baseline — defined improvement cohorts only | N/A by construction — no stale reference ever exists | Yes, if each cohort has a bounded life (Task 2) | Needs disciplined, auditable cohort documentation |

**Recommended minimum viable baseline architecture: rolling baseline + defined improvement
cohorts, combined.** The rolling baseline ensures the reference point never goes stale and
naturally absorbs exogenous market movement without paying the provider for it. Each
specific, dated, provider-driven intervention is tracked as its own bounded-life cohort
(Task 2's time-limited share), so a genuine provider-caused improvement is still credited and
paid even as the rolling average elsewhere adjusts for market drift — satisfying both "must
not pay for exogenous improvement" and "must not lose legitimate value from provider-driven
ecosystem change." Counterfactual benchmarking is explicitly excluded as an option.

## Task 5 — Event 1 administration cost test

Evidence chain (now longer than Cycle 6 assumed): work execution → timestamp-locked job
coding → resource capture across *all* labour categories (Cycle 7 hardening) → net
substitution adjustment → scope-mix adjustment → rolling-baseline/cohort-tracked
productivity calculation (this cycle's Task 4) → Finance validation → payment.

Illustrative annual governance cost by contractor-spend scale:

| Contractor spend | Provider FTE-equiv. | Customer FTE-equiv. | Independent audit | Illustrative annual cost |
|---|---|---|---|---|
| €10m | 0.1-0.2 | 0.1 | Periodic sampling | €30,000-€60,000 |
| €50m | 0.3-0.5 | 0.2-0.3 | Periodic sampling | €100,000-€180,000 |
| €150m | 0.75-1.5 | 0.5 | 1-2 weeks/yr external | €250,000-€450,000 |
| €500m | 2-3 | 1 | Substantial external | €600,000-€1,000,000 |

**Event 1 Administration Ratio = annual governance cost / verified gross productivity
value**, tested at illustrative opportunity rates: **transformation years** (~15% of
contractor spend, roughly consistent with AMOR 2020's evidenced potential range) vs.
**steady-state years** (~2.5%, a materially smaller illustrative assumption reflecting Task
3's tapering finding).

| Spend | Transformation-year ratio | Steady-state ratio |
|---|---|---|
| €10m | ~5.3% | **12-24%** |
| €50m | ~2% | 8-14% |
| €150m | ~2% | 6.7-12% |
| €500m | ~4-6% | 4.8-8% |

**The ratio is reasonable in transformation years across all scales, but degrades sharply in
steady-state years, especially for smaller customers — crossing 20%+ at the €10m scale.**
This mirrors Task 3's finding from a cost-efficiency angle: Event 1's governance apparatus
is well-justified during genuine transformation and increasingly hard to justify once the
low-hanging fruit is gone. **The ratio at which this becomes commercially absurd: roughly
20-25%**, a threshold the data shows real illustrative scenarios can cross. This cost is
real and must be visible — either reducing Event 1's net payout or explicitly priced into
Base Fee — never silently absorbed as free overhead.

## Task 6 — Customer eligibility gate

Five conditions, evidence-based, calibration-dependent where noted (not universal invented
thresholds):

1. **Minimum addressable contractor spend** — large enough that the Administration Ratio
   stays below the ~20-25% absurdity threshold at steady state (illustrative candidate:
   ≥€30-50m/yr; real calibration requires real administration-cost data, not fixed here).
2. **Sufficient work-order/resource data quality** — ties to the existing CMMS data-quality
   gate (`event_stress_test.md`, Event 8).
3. **Stable, consistently-applied job classification** — precondition for the hardened
   catalog (Cycle 7) to function at all.
4. **Demonstrated ability to measure net labour substitution** across all resourcing
   categories (data-availability precondition specific to Cycle 7's hardening).
5. **Customer Finance validation capability** — an operational readiness check, not a
   sophistication judgment, mirroring the Turnaround Module's Finance-readiness condition.

**PASS → Event 1 (as the Contractor Productivity Value Module) activates. FAIL → "Core
Service without Event 1"** — Base-Fee-funded Control Tower + Event 4 downside corridor only.

**Is Core Service without Event 1 still honestly AMOR? Yes — see Task 9.**

## Task 7 — Provider revenue concentration test

Zero Event 1 payment for two consecutive years, opportunity exhausted after Year 3, an
already-mature customer, falling contractor spend, insourced work, a 12-month disputed
delay — every one of these is a realistic, non-edge-case scenario given Tasks 1-6's
findings, not a tail risk. **A provider CFO planning margin around continuous Event 1
revenue for contract years 4-10 would be making a planning error.**

**Is Event 1 genuinely a commercial engine, or a selectively applicable value module sitting
on a Base-Fee-funded Control Tower business? The evidence points to the latter.** It has a
natural, finite opportunity arc (Task 3); it requires customer-specific eligibility to be
economically rational at all (Task 6); its administration cost is only justified at scale
and during transformation (Task 5); perpetual payment logic is indefensible and even the best
bounded design carries real residual tension (Task 2); and provider economics must not be
underwritten assuming it persists (this task). **Reclassification, not survival-as-core, is
the evidence-driven conclusion.**

## Task 8 — Attacking the differentiation claim

Cycle 7's sentence: *"AMOR ties the provider's own money to two things a normal maintenance
contract doesn't: an ongoing, measured share of real contractor savings for the life of the
deal, and a real, capped financial consequence if the provider's own maintenance failure
costs you production — everything else is delivered as accountable service, not sold as a
separate paid event."*

1. **"normal maintenance contract doesn't"** — no benchmark evidence exists anywhere in this
   project to support this comparison. **Unsupported.**
2. **"for the life of the deal"** — **directly contradicted by Task 2.** Perpetual share is
   not commercially defensible; must be removed.
3. **"real, capped financial consequence... exceeding standard terms"** — structurally, a
   capped painshare resembles liquidated damages or an SLA credit regime. Without benchmark
   evidence, claiming it *exceeds* standard terms is unsupported. What can honestly be
   claimed is that it is a **deliberate, jointly-governed, capped liability commitment** —
   not that it is unusually large relative to the market.
4. **Does the sentence overstate differentiation? Yes, on both counted claims.**

**Rewritten, using only claims proven inside this project:** *"AMOR pays the provider a
bounded, time-limited share of contractor cost improvements it demonstrably creates, and
holds the provider financially accountable, within a capped corridor, if its own maintenance
failures cause you production loss."*

A real, if narrower, differentiated claim survives: bounded productivity-sharing (evidenced
by actual mechanism design, Tasks 1-6) plus capped downside accountability (evidenced by the
Event 4 architecture) are both real, built, defensible mechanisms. The "exceeds normal
terms" and "for the life of the deal" claims do not survive and must not be used.

## Task 9 — Control Tower without atomic upside

Testing AMOR as: **Base-Fee-funded Control Tower + Accountable Operating System + Event 4
downside corridor + optional value modules** (Contractor Productivity Module, Turnaround
Module), with no guaranteed atomic upside.

| | Assessment |
|---|---|
| Commercial differentiation | Survives — see below |
| Provider economics | More resilient than assuming Event 1 revenue (Task 7); Base Fee must be priced to stand alone |
| Customer CFO credibility | **Arguably higher** — a model that says "here's what's guaranteed, here's optional upside where your data/scale supports it" is more credible than one straining to fit every customer into a monetized-upside story |
| Scalability | Higher — the core works for every customer; modules layer on selectively, exactly matching the Cycle 6 Model C philosophy |
| Sales simplicity | Higher |
| Contract operability | Higher — fewer guaranteed moving parts |
| Risk of regressing to "Better Managed Maintenance" (Cycle 2's rejected outcome) | **Real, but specifically prevented by Event 4** — genuine, capped, jointly-governed downside accountability is the one mechanism most conventional managed-maintenance arrangements don't carry in this deliberate form. Without it, AMOR would be AMOR 2020 relabeled. With it, the core stands as something distinct even with zero upside monetisation active. |

**What prevents regression to Cycle 2's rejected outcome is Event 4, not Event 1.** This is
the answer to the deeper strategic question Petri named: **AMOR's identity is a Control
Tower operating model with genuine downside accountability, to which value-sharing modules
are added only where their economics can be proven for a specific customer — not
fundamentally an atomic-upside-monetisation business.** This conclusion was reached through
Tasks 1-8's analysis independently, and converges with Petri's stated hypothesis for the same
substantive reasons.

## Task 10 — External stakeholder validation design (design only — not conducted)

**Minimum sample:** 3-5 respondents per stakeholder category, across at least 2-3 distinct
customer contexts — small and qualitative, sufficient to catch a consistent pattern rather
than a single outlier view, not statistically powered.

**Evidence capture:** structured interviews, recorded with consent or detailed
contemporaneous notes, verbatim capture of open-ended answers, coded against the pass/fail
signals below.

### A. Customer CFO (max 10)
1. If shown a signed, itemized contractor invoice showing a rate drop, would Finance approve
   a monthly payment against a pre-agreed formula without further negotiation?
2. Would you commit, in contract, to a defined multi-year sunset (e.g. 3 years) on any given
   productivity improvement's payment, even if the saving continues afterward?
3. Walk me through how your budget process would treat a variable monthly payment tied to
   contractor savings.
4. Would your Finance team audit our net-labour-substitution calculation as a condition of
   payment?
5. If we stopped finding new contractor savings after Year 3 because the obvious
   opportunities were gone, would you expect that reflected in Base Fee pricing up front, or
   would you expect us to keep finding savings indefinitely?
6. Would a capped consequence for a provider-caused production loss feel like real
   accountability, or a formality?
7. Would you accept that losses above that cap go through a standard liability clause
   negotiated separately by legal counsel, not through the performance mechanism?
8. In your own words, what makes this different from a standard maintenance contract with a
   bonus clause?
9. Would you share your actual current contractor spend and rate data before signing, so we
   can determine whether the productivity module is even viable for your site?
10. If our analysis showed your site doesn't meet the eligibility threshold, would you still
    sign the core contract without that module?

### B. Customer Maintenance/Asset Director (max 10)
1. Comfortable with monthly external access to CMMS job-order data for a rate-delta
   calculation?
2. Would you want formal veto/review rights over a proposed maintenance-plan spend increase,
   even knowing it might slow execution?
3. How would your team react if a Year-1 rate improvement was still generating a payment to
   us in Year 5?
4. Would you trust a joint, equal-vote board to adjudicate a disputed claim, or want a
   unilateral veto?
5. Would a capped financial consequence for a provider-caused failure feel like a meaningful
   deterrent, or window dressing?
6. Do you consider your contractor base currently well-managed, poorly managed, or in
   between?
7. If told your site's data quality doesn't support the productivity module, would you want
   us to fix the data first, or skip the mechanism entirely?
8. Would you want turnaround execution measured against an outside, independent benchmark
   you're not familiar with?
9. What would make you personally recommend AMOR to a peer site — savings, accountability,
   or something else?
10. If none of the value-sharing modules applied to your site, would AMOR still be worth
    doing?

### C. Provider CFO/Business Leader (max 10)
1. Comfortable underwriting this contract's margin plan assuming zero Event 1 revenue from
   Year 4 onward?
2. Accept that some eligible-gate-failing customers will generate zero Event 1 revenue at
   all?
3. Willing to resource Event 1's governance apparatus knowing the administration ratio could
   reach 12-24% of verified value for smaller customers?
4. Accept a capped, asymmetric painshare as a permanent feature of every contract, even in
   years nothing goes wrong?
5. If a competitor offered a simpler Base-Fee-plus-bonus model without this governance
   apparatus, what would you tell a customer who asked why to prefer ours?
6. Willing to walk away from a customer that fails the Event 1 eligibility gate rather than
   force-fit the mechanism?
7. How would you price Base Fee differently for a customer where no module will ever apply?
8. Comfortable being asked to guarantee a specific Event 1 revenue figure in a sales pitch,
   given the savings-pool-exhaustion dynamic?
9. Lead with the Control Tower/accountability story, or the productivity-sharing story?
10. If Event 1 is reclassified as optional rather than guaranteed core revenue, does that
    change how you'd staff or invest in the business unit delivering AMOR?

**Pass signals:** willingness to share pre-sale data; acceptance of bounded/sunset payment
logic without strong resistance; provider leadership accepting zero-Event-1-revenue planning
for mature years; no respondent describing the model as indistinguishable from "a
complicated bonus scheme" when asked the open differentiation question.

**Fail signals that would force Event 1 to be killed entirely (not just modularized):** a
consistent pattern of customer Finance functions refusing to audit/validate net-substitution
calculations under any circumstances, or provider leadership unwilling to resource the
governance apparatus at any contractor-spend scale. Either finding would mean Event 1 is not
merely customer-specific but structurally non-viable everywhere.

**This is a test design. No interviews have been conducted. No responses are claimed or
fabricated.**

## Task 11 — Commercial-to-legal drafting brief (Event 4 catastrophic-loss boundary)

**Purpose:** brief external legal counsel to draft the boundary between Event 4's
performance corridor and standard contractual liability/indemnity. This project does not
draft final legal language.

**A. Commercial intent.** Event 4 is an everyday performance-incentive-alignment mechanism.
It is not intended to be the customer's primary or sole protection against a large,
consequential, provider-caused loss.

**B. Reference architecture.** Event 4's attribution logic (`event4_decision_tree_v3.md`,
including the materiality gate, the SLA-driven exclusion, and Step 3.6's customer-veto
interaction) determines whether a given production-loss event is provider-attributable at
all. This determination is a precondition for either the performance corridor or the
liability boundary to apply.

**C. Performance corridor caps (current modelling assumptions, per `06_COMMERCIAL_MODEL/
PROVIDER_RISK_CORRIDOR.md`).** Annual painshare cap 10% of annual Base Fee; per-event cap
50% of the applicable annual cap; floor zero; no cross-year carry-forward; 24-month clawback
window. These caps apply to Event 4 as a performance-incentive mechanism only.

**D. Catastrophic escalation concept.** Losses whose documented magnitude exceeds Event 4's
per-event or annual cap should escalate out of the performance mechanism entirely and into
the standard contractual liability framework, not be adjudicated (even partially) under the
performance corridor. Counsel should define the specific trigger (e.g., a materiality
multiple of the per-event cap, or a defined severity classification) — not fixed here.

**E. Insurance interaction — open questions for counsel.** Does the provider carry
professional indemnity or general liability insurance that would respond to a catastrophic,
provider-attributable loss? Should the contract require minimum insurance coverage as a
condition precedent to the liability clause taking effect? How does any insurer's own
subrogation or notification requirements interact with the Value Validation Board's
attribution process (which determines fault before any liability claim would be made)?

**F. No double recovery principle.** A given loss must be adjudicated under either the Event
4 performance corridor or the general liability/indemnity clause, never both. Counsel should
draft an explicit election or sequencing mechanism (not designed here) preventing the
customer from recovering the capped performance amount *and* pursuing full liability for the
same loss.

**G. No waiver principle.** The existence of the annual painshare cap must not be construed,
drafted, or interpreted as waiving, capping, or otherwise limiting whatever liability
protection would otherwise apply under the general contract terms — the performance cap
bounds the performance mechanism only, not the customer's underlying legal rights.

**H. Unresolved legal questions for counsel, not this project.** Jurisdiction and governing
law; whether local law permits the proposed no-double-recovery election mechanism; the
appropriate catastrophic-loss trigger threshold; whether a liability cap (if any) on the
general clause should be tied to contract value, insurance limits, or left uncapped; force
majeure interaction; and whether the Value Validation Board's attribution finding should be
binding, persuasive, or non-binding in a subsequent legal liability proceeding.

## Task 12 — Red Team (15 scenarios)

| # | Scenario | Resolution |
|---|---|---|
| 1 | Perpetual rent on Year 1 savings | Resolved — Task 2 recommends time-limited share, killing perpetual design |
| 2 | Provider loses incentive after time-limited share expires | Real, partially mitigated by continuous-improvement pressure to create new cohorts; disclosed residual risk if no new opportunity exists (Task 3) |
| 3 | Baseline reset destroys provider economics | This is why reset (Option D) was rejected in favor of rolling+cohort (Task 4) |
| 4 | Fixed baseline pays for market improvement | Resolved — rolling baseline, Task 4 |
| 5 | Customer was already efficient | Resolved — excluded via the eligibility gate, Task 6 |
| 6 | Savings pool exhausted in Year 3 | Acceptable, expected dynamic if priced/durationed correctly — Task 3 |
| 7 | Contractor spend falls 50% | Realistic, disclosed — Event 1 revenue falls proportionally, must not be underwritten otherwise, Task 7 |
| 8 | Work is insourced | Same as above — a real, planned-for risk, not hidden |
| 9 | Administration costs consume 30% of verified value | Shown as realistic at small scale in steady-state years (Task 5) — exactly why the eligibility gate excludes such cases (Task 6) |
| 10 | Finance disputes net-substitution adjustments | Real, ongoing dispute surface inherent to Cycle 7's hardening — mitigated, not eliminated, by audit sampling |
| 11 | Customer refuses persistent savings share | Directly addressed — Task 2's redesign removes the persistence customers would object to |
| 12 | Event 1 fails eligibility gate | Explicitly designed for — "Core Service without Event 1" is the defined, non-failure fallback, Task 6 |
| 13 | Control Tower without Event 1 becomes ordinary managed maintenance | Tested directly, Task 9 — does not collapse, because Event 4 (not Event 1) is the actual regression-prevention mechanism |
| 14 | Event 4 corridor is indistinguishable from bonus/malus | **Not fully resolved** — honestly acknowledged in Task 8 as a real, only partially answered limitation |
| 15 | AMOR differentiation disappears once unsupported market claims are removed | Tested, Task 8 — a narrower but real differentiated claim survives; the strongest version of the claim does not |

**Neither Event 1 nor the core architecture is killed outright.** Event 1 is reclassified.

## Checker verification
- **Persistent savings are not counted repeatedly without explicit commercial logic:**
  confirmed — Task 2's recommended design (time-limited share) explicitly bounds every
  improvement's payment life; the perpetual design that would have violated this is rejected.
- **Exogenous market improvement is excluded:** confirmed — the rolling baseline (Task 4) is
  specifically designed to absorb market-wide movement without paying the provider for it.
- **Provider-created ecosystem change is not incorrectly treated as exogenous:** confirmed —
  cohort tracking (Task 4) credits specific, dated, provider-driven interventions
  independently of the rolling reference.
- **Event 1 administration cost is visible:** confirmed — sized explicitly (Task 5), not
  folded into Base Fee silently.
- **Event 1 eligibility is objective:** confirmed — five pass/fail conditions (Task 6), no
  subjective maturity assessment.
- **Base Fee economics are not silently subsidised by assumed Event 1 revenue:** confirmed —
  Task 7 explicitly states Event 1 must not be underwritten as continuous provider revenue;
  Task 9 requires Base Fee to stand alone.
- **Differentiation claims do not rely on unsupported market assertions:** confirmed — Task
  8 removes both unsupported claims ("normal contract doesn't," "exceeds standard terms")
  from the rewritten differentiation statement.
