# Cycle 7 — Minimum Viable Architecture Hardening

**Cycle 8 update:** Event 1, treated below as the sole surviving core upside event, was
subsequently tested for economic durability and **reclassified from core to an optional
"Contractor Productivity Value Module"** — see `06_COMMERCIAL_MODEL/cycle8_event1_survivability.md`.
The X/Z architecture naming used below is also retired per Petri's Cycle 8 decision — there
is one core architecture (Base Fee-funded Control Tower + Event 4) plus optional modules, not
two named architectures. Read this document for the Event 3 kill analysis, which remains
valid; the Event 1/X-Z conclusions are superseded.

## Task 1 — Attacking Event 3-simplified: is it semantic repackaging?

Cycle 6 killed original Event 3 (case-by-case dollar-value gainshare) and proposed a
"restructured successor" — a flat, pre-agreed reward per qualifying reliability event,
counted and settled annually. Testing whether this actually removed the problem or just
renamed it.

| Attack vector | Finding |
|---|---|
| Counterfactual dependence | **Unchanged.** Qualification still requires proving a failure "would have recurred but didn't." Removing the dollar calculation removes *how much* you pay, not *whether you're paying for an unfalsifiable counterfactual at all.* |
| "Paying for something that did not happen" | **Unchanged, arguably worse.** A flat €150,000 can look more arbitrary to a skeptical CFO than a calculated figure with a visible methodology — "where does that number come from?" |
| Repeat-failure baseline dependence | **Fully inherited.** The ≥3-prior-failures threshold and its CMMS-classification manipulation exposure carry over unchanged. |
| Causal connection requirements | **Fully inherited.** The Causal Connection Map remains a mandatory prerequisite — unsized cost, see Task 5. |
| 180-day observation/netting burden | **Inherited, and newly incompatible.** With a calculated dollar value, netting subtracts a specific amount from a specific amount. With a *flat* reward, netting has no clean partial mechanism — a secondary failure either claws back the entire flat reward (binary) or the model quietly needs dollar valuation again to determine a partial clawback. **This is a genuine design gap Cycle 6 did not think through.** |
| Event qualification disputes | **Potentially worse.** A calculated value gave both sides room to negotiate via the calculation's inputs. A flat, binary "qualifies or doesn't" structure removes that room — disputes become all-or-nothing. |
| Event fragmentation | **New, worse risk.** Under the killed original, splitting a claim didn't obviously multiply total value (the total should track total avoided loss). Under a flat **per-event** reward, splitting one real improvement into multiple "qualifying events" directly multiplies revenue. This is the claim-fragmentation risk from Cycle 5's Red Team, and the flat-reward redesign makes it *more* attractive, not less. |
| Provider event hunting | **New, unaddressed risk.** A certain, predictable flat payout per qualifying event creates a concentrated incentive to go looking for marginal "bad actor" candidates specifically because the payout is now simple and guaranteed — a Goodhart-style risk with no equivalent Red Flag control, unlike Event 4's over-maintenance control. |
| Severity manipulation | Not directly applicable to a pure flat reward, but exposes the real problem Petri named: a flat reward can't distinguish a trivial near-miss from a €20m-consequence event — see Task 2. |
| Annual revenue predictability | **Genuine improvement.** The one dimension where the simplification delivers something real. |

**Verdict: SEMANTIC REPACKAGING on every dimension that actually drove cost and dispute risk
(qualification burden, counterfactual dependence, Causal Connection Map, netting
compatibility, the core CFO objection). Genuine simplification on exactly one dimension
(payment-magnitude predictability once qualified) — which does not offset the rest, and
introduces two new problems (fragmentation, event hunting) the original design didn't have
in the same form.**

Cycle 6 simplified the wrong half of the problem: it removed the part that was already
relatively tractable (valuing a *proven* event) and left the expensive, disputed part
(proving the event happened at all) completely untouched.

## Task 2 — Reliability Reward mechanism comparison

Testing whether any payment structure escapes Task 1's finding, before concluding the
mechanism should be killed outright.

| | A. Flat fixed reward | B. Severity-banded fixed reward (≤3 bands, ex ante) | C. Annual reliability reward pool |
|---|---|---|---|
| CFO explainability | Simple, but "why this number" is unanswered | Reasonably intuitive | Familiar bonus-pool logic — which sharpens, not answers, the "just a bonus scheme" objection |
| Attribution burden | Full qualification burden inherited, unchanged | **Higher than flat** — now requires an ex ante severity classification *in addition to* full qualification | Qualification burden inherited but aggregated into one annual review rather than resolved per-claim |
| Dispute potential | High (binary, no negotiation room) | High — new dispute surface ("which band?") stacked on the existing qualification dispute | Lower frequency, higher stakes per dispute (one annual fight instead of several small ones) |
| Provider motivation | Event-hunting (new risk, Task 1) | Incentive to push ex ante classifications into higher bands — a subtler, earlier-stage version of the same gaming | Portfolio/year-end timing gaming — pushing marginal claims late in the year to maximize pool release |
| Customer retained-value credibility | Weak — no proportionality to actual consequence | Better — attempts proportionality | Weakest of the three — no clean per-event linkage at all |
| Budget predictability | Moderate (variable by count) | Moderate (variable by count and band mix) | **Best** — a capped annual pool is a known maximum |
| Claim-volume sensitivity | Same as original per-claim cadence | Same | **Lowest** — one annual review, not N claims |
| Working-capital effect | Similar to original | Similar | Cleanest — single annual settlement |
| Gaming risk | Fragmentation, event hunting | Ex ante band gaming (real, but less severe than ex post) | Portfolio/timing gaming; "quality" scoring itself needs definition or becomes pure VVB discretion |
| **Has avoided-value gainshare returned through the back door?** | **Yes** — flat reward per event is dollar valuation with the precision sanded off, not removed | **Yes, partially** — a severity band *is* a coarse (3-bucket) dollar valuation of avoided consequence, not an escape from valuing it | **Least, if kept strictly non-monetary** — but only if "quality" is scored by count/ordinal criteria, never by estimated consequence value, and even then the underlying qualification burden is unchanged |

**The mechanism used to pay does not fix the problem, because the problem is in how events
qualify, not in how they're valued.** All three options patch the payment side. None touch
Task 1's actual finding: the qualification step (counterfactual proof, Causal Connection
Map, 180-day netting, ≥3-failure baseline) is the real cost and dispute driver, and no
payment-structure choice changes that.

**Recommendation: KILL the Reliability Reward mechanism entirely — original design, flat
reward, severity bands, and pool, all four.** Reliability value moves from a monetized event
category to a **managed, operational, reported discipline** — tracked as context/management
KPIs (repeat-failure trend, bad-actor list length, MTBR) feeding the KPI Pyramid, customer
confidence, and contract renewal conversations, but never triggering an individual payment.

This directly confirms Petri's stated hypothesis. It was reached independently through
Tasks 1-2's analysis, not by deference — the two converge because the underlying finding
(qualification burden, not valuation method, is the cost driver) is the same either way.

## Structural consequence: Architecture X and Z converge

With the Reliability Reward killed in every form, Architecture Z's core (Event 1 + Event
3-simplified + Event 4) collapses to **exactly Architecture X's core (Event 1 + Event 4)**.
**Architecture X is not an entry-tier discount of Z — with this kill, X and Z now have an
identical core.** The only remaining distinction is the optional Turnaround Value Module,
which Z can activate and X, by definition, has not. This means:
- The X→Z "maturity path" as originally framed (graduating into the Reliability Reward) is
  **moot** — there is no Reliability Reward to graduate into.
- Task 4 below is re-derived around **Turnaround Module readiness**, not reliability-data
  maturity, since that premise no longer exists. This is flagged explicitly, not silently
  substituted.
- Staying on "Architecture X" forever is not a stalled migration or a failure to mature — it
  is a complete, valid, permanent commercial offering for any customer without meaningful
  turnaround exposure. Cycle 6's framing of X as a "fallback" was already wrong before this
  cycle; it is now clearly wrong.

## Task 3 — Event 1 baseline hardening

**A. Baseline inflation.** Require the frozen pre-transition baseline to have **clean
provenance** — sourced from data predating any expectation of an AMOR-style contract (so
neither party had an incentive to distort it) — cross-checked against an external,
independent rate-card or market data source for the relevant trade/region, plus a
statistical outlier review of the baseline period itself (was it an unusually high-cost
period for reasons unrelated to normal market rates?). Reduces, does not eliminate,
collusive-depression risk — a sophisticated, market-wide depression would still evade an
external cross-check tied to the same market.

**B. Labour substitution.** The event must measure **net resource substitution**, not
isolated contractor efficiency: track whether hours shifted from third-party contractors to
provider employees, customer employees, other contractor categories, engineering resources,
supervision, or temporary labour, and require a blended cost comparison across *all*
resourcing categories used for a given job code — not just the contractor invoice line. This
is a genuine, substantive complication, not a light-touch fix: Event 1's unit of measure
moves from "contractor €/job" to "total resourcing cost per job, however staffed," which is
categorically harder to administer.

**C. Contractor-rate inflation vs. productivity delta.** Explicitly separate four effects:
(1) productivity delta — same rate, less time/fewer resources for the same output (the only
component that should be payable); (2) labour-rate delta — same effort, different unit
price, often market-driven not provider-driven; (3) procurement savings — volume/contract
effects unrelated to work efficiency; (4) scope-mix effects (already addressed, Cycle 3/5).
Only (1) is payable under Event 1. (2)-(4) are excluded from its calculation entirely — not
folded into a new payment mechanism, per the instruction not to add a seventh event.

**D. Job-mix/complexity manipulation.** Minimum controls: **timestamp-locked job coding**
(assigned at work-order creation, not adjustable after completion — reusing the same pattern
already used for Event 2's original "planned work" lock); **fixed work-scope definitions**
tied to equipment tag + standard task type, preventing arbitrary bundling/splitting;
**periodic independent catalog audit sampling** by the customer's own technical team, not
solely provider self-classification; **new, uncatalogued job types default to excluded**
until jointly catalogued (the same conservative default used throughout this project).

## Task 3 continued — Event 1 four-gate retest

Hardening adds real, ongoing burden. Re-scored ordinal burden (same 8-factor scale as Cycle
6): evidence 2→3, Finance review 2→3, independent review 1→2 (periodic audits now carry an
independent-style check), comprehension 2→3 (net-substitution logic is harder to explain
than a simple rate comparison) — **burden score rises from 14 to ~18.** Recomputed density:
€1,400,000 / 18 ≈ **€77,800/burden-point** — down from €100,000/pt, but with Event 3 killed,
there is nothing left in the core to compare it against; Event 1 is not just the best
option, it is now the *only* upside mechanism carrying the entire productivity-value engine.

| Gate | Verdict |
|---|---|
| A — Material value | PASS, unchanged |
| B — Attribution clarity | PASS, weaker margin — "net resource substitution" is harder to explain simply than "we pay less for contractors," but it is still a measured cost comparison, not a counterfactual, and stays structurally clearer than Event 3 ever was |
| C — Administrative efficiency | **PASS, narrowed margin — disclosed, not hidden.** Event 1 is not the "nearly free" event the Cycle 6 density ranking implied. It is the best available option, not a costless one, and its burden is now proportionate to carrying the whole productivity engine alone |
| D — Strategic necessity | PASS, unchanged — now higher-stakes given it's the sole surviving core upside event |

**Event 1 still passes all four gates.** The honest caveat, stated plainly: it requires
meaningfully more sustained administrative discipline than Cycle 6 assumed.

## Task 4 — Redefined: Turnaround Module readiness gate (not Reliability Reward activation)

Original premise moot per the structural consequence above. Five-condition objective gate
for activating the optional Turnaround Value Module:

1. **Contracted TA execution responsibility** — provider holds documented, contracted
   responsibility for turnaround execution at the site (pass/fail, contractual fact).
2. **Minimum TA frequency/scale** — site has a minimum number of qualifying turnarounds
   per contract term (illustrative threshold, e.g. ≥1 qualifying TA per 3 years — a number
   to be negotiated, not fixed here) sufficient to amortize the independent-benchmark
   relationship's fixed cost.
3. **Available qualifying independent benchmark provider** — a benchmark source meeting the
   Cycle 5 three-part independence test (`event9_turnaround_execution_efficiency.md`)
   actually exists and is available for this customer's TA type and geography (pass/fail).
4. **Documented TA scope-freeze governance capability** — a joint scope-freeze sign-off
   process exists and has been used at least once (evidence of capability, not just intent).
5. **Finance validation readiness** — both parties' Finance functions can support a
   TA-scale settlement process (pass/fail, an operational readiness check, not a
   sophistication judgment).

**PASS:** all five conditions met → Turnaround Value Module may activate.
**FAIL:** any condition unmet → module stays inactive; core architecture (Event 1 + Event 4)
continues, which is a complete offering, not a degraded one. No automatic activation based
on contract age or tenure alone.

## Task 5 — Causal Connection Map cost

Sized independently of the kill decision — it also serves as direct evidence for why the
Reliability Reward failed Gate C.

| Scenario | Assets/functional locations | Engineering hrs (build) | Customer SME hrs | Total build hrs | Illustrative initial cost (€100-150/hr blended) |
|---|---|---|---|---|---|
| Small site | ~500 | 1,000-2,000 | 250-500 | 1,250-2,500 | €125,000-€375,000 |
| Medium industrial site | ~2,000 | 4,000-8,000 | 1,000-2,000 | 5,000-10,000 | €500,000-€1,500,000 |
| Large/complex process site (e.g. refinery scale) | ~8,000-15,000 | 16,000-60,000 | 4,000-15,000 | 20,000-75,000 | **€2,000,000-€11,250,000** |

Annual maintenance: illustrative 10-15% of assets change (new equipment, process changes,
decommissioning) per year, implying **€200,000-€1,700,000/yr recurring cost at large-site
scale** for maintaining map accuracy.

**This is the sharpest, most concrete evidence for Task 1/2's kill decision** — a
multi-million-euro, previously entirely unsized prerequisite for a mechanism whose Normal
Year value (in the Cycle 5 illustrative model) was €1,550,000 gross, €620,000 net of split.

**Recommended scope: build nothing, for now.** With the Reliability Reward killed, the map's
only identified use case is gone. Coverage Option D (progressive, triggered by repeat-
failure candidates) was tested as requested and **confirmed to create real provider
selection bias** — a provider would naturally map assets where it expects "wins,"
systematically inflating apparent reliability performance in mapped areas while leaving the
rest uncovered — a second, independent reason not to build even a progressive map for this
purpose. If a future cycle reintroduces a map-dependent mechanism, this sizing and the
selection-bias finding should gate that decision, not be silently reworked around.

## Task 6 — Turnaround Module anti-selection rule

Recommended: **Hybrid — site-wide commitment (A) for a defined minimum multi-year term**,
activated before scope-freeze planning begins for the first qualifying TA it would apply to.

- **Qualifying turnaround:** a planned major maintenance shutdown meeting a minimum
  duration/spend threshold (illustrative — real threshold needs negotiation), assessed on
  total affected asset/unit scope, not single-event duration alone (to reduce, not
  eliminate, threshold-structuring risk).
- **Commitment boundary:** site-wide, all qualifying TAs — no selection by class or
  individually once activated.
- **Activation timing:** before the scope-freeze/detailed-planning phase of the first
  applicable TA begins — a "clean slate" point with no visibility into how that TA will
  unfold.
- **Minimum term:** the longer of the remaining contract term or a fixed multi-year minimum
  (illustrative: 2 full TA cycles) — cannot be switched off after one unfavorable TA.
- **Permitted exclusions:** narrow — only a TA already substantially planned/scoped *before*
  the activation date (grandfather clause, since execution visibility already existed).
- **Approval authority for exclusions:** any claimed exclusion requires Value Validation
  Board approval against the pre-defined narrow criteria — no unilateral exclusion by either
  party, and the Board's discretion is bounded by the criteria, not open-ended.

**Red Team:** provider timing activation to a site's TA-light period is mitigated by tying
minimum term to TA-cycle count, not calendar time. Customer declining renewal right after a
good TA is mitigated by the minimum-term lock applying regardless of which party wants out.
Residual risk: gaming the "qualifying turnaround" threshold definition by structuring a
difficult TA as several smaller sub-threshold outages — reduced but not eliminated by
scoping the threshold to total affected asset/unit scope; disclosed, not solved.

## Task 7 — The "complicated bonus scheme" objection

**A. Strongest CFO objection:** "Strip away the vocabulary — Control Tower, Value Validation
Board, atomic events — and what I actually have is a base fee like any maintenance contract,
a rebate on contractor spend I could get by renegotiating contracts myself, and a liability
clause for provider-caused damage that any competent lawyer puts in any maintenance contract
regardless of what you call it. I could get the contractor rebate from a procurement
consultant for a fraction of what your Value Validation Board costs to run, and I already
have liability clauses in every vendor contract I sign. What, specifically, am I buying that
I couldn't get cheaper and simpler by just being a better-organized customer myself?"

**B. Honest AMOR answer:** After this cycle's simplification, the honest answer is narrower
than the original thesis aspired to. What genuinely differs: (1) Control Tower orchestration
of a fragmented, multi-party contractor/OEM ecosystem under single accountable ownership is
something the customer would otherwise build in-house or manage through their own
procurement function at their own administrative cost — and Event 1 ties the *provider's*
ongoing incentive to sustained rate discipline for the life of the contract, not a one-off
consultant engagement that ends when the consultant leaves. (2) The Event 4 downside
corridor is real, performance-linked liability exceeding what standard maintenance-contract
liability clauses typically carry (which usually cap or exclude consequential/production-
loss damages) — genuine skin in the game, not a restatement of default liability law. (3)
Reliability improvement, now that it is not separately monetized, is delivered as an
ordinary, expected feature of good Base-Fee-funded service — AMOR does not claim, and must
not claim, to price this differently.

**C. One-sentence commercial differentiation:** "AMOR ties the provider's own money to two
things a normal maintenance contract doesn't: an ongoing, measured share of real contractor
savings for the life of the deal, and a real, capped financial consequence if the provider's
own maintenance failure costs you production — everything else is delivered as accountable
service, not sold as a separate paid event."

**D. Claims AMOR must NOT make:** "AMOR monetizes reliability" / "AMOR pays you for
prevented failures" / any implication that individual reliability improvements are
individually priced — false as of this cycle's kill decision, and continuing to imply it
(even informally, even in sales conversation) would be a known misrepresentation. Also must
not claim to eliminate maintenance-related production-loss risk — Event 4 is capped
incentive alignment, not comprehensive insurance.

## Task 8 — Catastrophic Event 4: performance economics vs. legal liability

Compared A (current capped corridor) through E (exclude catastrophic loss from the
performance mechanism, treat under normal contractual liability).

**Recommendation: (E) is the correct conceptual boundary.** Event 4's performance corridor
(10% annual cap, 50% per-event cap) is an everyday **incentive-alignment mechanism** — its
job is to make routine performance accountability real, not to be the customer's primary
protection against catastrophic loss. Genuinely large, provider-attributable losses are a
**legal liability/indemnity matter**, governed by the underlying commercial contract's
standard liability clause (with its own, typically much higher, cap — potentially insurance-
backed), which exists independent of and prior to any AMOR performance architecture.

This reframes, rather than "solves," Cycle 5's finding that a single catastrophic event
recovers only 26.7% through the performance corridor: **that finding was not a bug — the
corridor was never designed to be catastrophic-loss protection, and treating Cycle 5's
number as a flaw was a category error.** The real customer protection for a genuinely
catastrophic loss should come from a separate liability clause, not from stretching the
performance corridor to cover a risk category it was never sized for.

**Recommendation:** (1) Event 4's performance corridor stays exactly as designed, bounded,
for its true purpose. (2) The underlying commercial contract should carry a separate,
standard liability/indemnity clause governing genuinely catastrophic provider-caused losses
— not designed here (legal drafting, outside this project's scope). (3) The contract must
state explicitly that Event 4 and the general liability clause are separate, non-overlapping
mechanisms — a given loss is adjudicated under one or the other, never both, with a defined
boundary rule (e.g. by materiality or severity threshold) to prevent double-dipping in
either direction.

## Task 9 — Red Team, 12 scenarios (post-hardening)

1. Event 3-simplified is semantic laundering → **Confirmed, Task 1. Resolved by killing it.**
2. Flat reward overpays low-severity events → confirmed, Task 2 (Option A attack); resolved.
3. Severity bands recreate valuation disputes → confirmed, Task 2 (Option B attack); a band
   is a coarse dollar valuation, not an escape from one; resolved by kill.
4. Annual reward pool weakens attribution → confirmed, Task 2 (Option C attack); resolved.
5. Event 1 baseline depressed before mobilisation → mitigated (not eliminated) by external
   provenance/outlier checks, Task 3A; residual tail risk disclosed for market-wide
   depression scenarios.
6. Contractor work shifted to provider labour → addressed by net-resource-substitution
   measurement, Task 3B — a real fix, at real administrative cost.
7. Job complexity recoded → addressed by timestamp-locking and independent audit, Task 3D.
8. X customer never reaches Z → **dissolves.** With the Reliability Reward killed, there is
   no maturity ladder to fail to climb — staying on core-only (X) is a complete, valid,
   permanent offering, not a stalled migration.
9. Provider selectively maps high-opportunity assets → confirmed as a real Option-D
   selection-bias risk, Task 5 — a second, independent reason not to build the map.
10. Customer blocks Causal Connection Map validation → moot; the map is not being built for
    this purpose.
11. Turnaround Module cherry-picking → substantially mitigated by the site-wide + minimum-
    term + pre-scope-freeze activation rule, Task 6; residual qualifying-threshold gaming
    risk disclosed.
12. Catastrophic Event 4 exceeds the performance corridor by 20x → resolved by Task 8's
    category boundary — this was never the corridor's job; the liability clause is.

**Attempt to kill Architecture X and Architecture Z:** neither dies. X (Event 1 + Event 4)
and Z (X + optional Turnaround Module) now share an identical core — X is not a lesser
version of Z, it is Z with the module switched off. Both survive as legitimate, permanent
commercial shapes, not as a maturity hierarchy.

## Checker verification
- **Original Event 3 gainshare has not returned under another name:** confirmed — all three
  Task 2 alternatives were tested and killed on the same grounds (qualification burden
  unchanged; at best a coarser dollar valuation, at worst a straight relabeling).
- **Reward mechanics do not use ex post avoided-value valuation:** N/A — the mechanism is
  killed entirely, so this check is moot by construction, not by careful design avoidance.
- **Event 1 does not pay for labour substitution, procurement savings, or rate changes:**
  confirmed — Task 3C explicitly isolates and excludes these; only genuine productivity
  delta is payable.
- **X→Z activation is evidence-based:** confirmed for the redefined (Turnaround Module)
  gate — five pass/fail conditions, no automatic activation on tenure alone.
- **Causal Connection Map scope does not create hidden selection bias:** confirmed the
  opposite finding was surfaced deliberately (Option D does create bias) and the
  recommendation is to build nothing, avoiding the bias by not building the map at all.
- **Catastrophic loss is not confused with normal performance economics:** confirmed — Task
  8 explicitly separates the two and recommends they never overlap in adjudication.
