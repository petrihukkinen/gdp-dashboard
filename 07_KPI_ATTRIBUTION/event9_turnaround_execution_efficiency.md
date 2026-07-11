# Event 9 — Turnaround Execution Efficiency (Cycle 4, new)

**Cycle 6 verdict:** deleted from core/default payment-event status. Failed Gate B
(attribution clarity — hardest of all six events to explain) and Gate C (administrative
efficiency — the Cycle 5 independence-criteria addendum's 3-year relationship check and
per-TA-cycle re-attestation is a real, disproportionate maintenance cost for an event firing
once every 4-6 years). Survives only as part of an optional, bundled **Turnaround Value
Module** (with Event 5), activated exclusively for contracts where the provider holds
genuine TA execution responsibility and TA frequency/scale justifies the fixed cost. Default
status in the core commercial model: reporting only. See
`06_COMMERCIAL_MODEL/cycle6_complexity_kill_test.md`, Tasks 2 and 5. The attribution rules
and independence criteria below remain valid and unchanged for whenever the module is
activated — this is a commercial-scope decision, not a redesign.

Distinct from Event 5 (TA scope reduction). Event 5 monetizes *what* work was removed from
scope; Event 9 monetizes *how well* the provider executes the scope that remains, once
jointly frozen. Numbered 9 to avoid collision with Events 7 (permit cycle time) and 8 (CMMS
data quality), which are gates, not payment events.

## Definition
Actual critical-path duration for the jointly-frozen TA scope vs. an **independently
benchmarked** critical-path duration set before execution begins, adjusted for verified
non-execution-attributable emergent work and for execution-attributable post-TA start-up
delay.

## Design lesson applied from Event 6
Event 6 (lifecycle Capex deferral) failed Cycle 3 review because a provider-set baseline
creates a conflict of interest. Event 9 is designed from the outset to avoid that: the
benchmark **must be set by a jointly-selected, named independent estimator or benchmark
database, agreed in the contract before the first TA cycle** — never the provider's own
estimate alone, and never selected unilaterally by either party mid-relationship (see
Scenario 13, `cycle4_red_team_scenarios.md`).

## Correction (Cycle 5 addendum, per Petri, 2026-07-11): "jointly selected" is not the same as "independent"
Petri's sharpest sparring point on this event: a benchmark provider chosen jointly by
customer and provider can still be captured, commercially dependent on one or both parties,
or simply not rigorous — joint selection is a *process* safeguard, not a *substance*
guarantee of independence. Two parties agreeing on a biased referee does not make the referee
unbiased. **Independence must be defined by criteria, not by the selection process alone.**
A benchmark source qualifies as independent only if it satisfies **all** of:
1. **No material commercial relationship** with either party (no material revenue from either
   the provider or the customer) in the preceding 3 years — a specific, checkable test, not
   a self-declaration.
2. **Publicly documented, auditable methodology** — the benchmark calculation method itself
   must be inspectable by both parties' Finance functions, not a black box.
3. Either **(a) a recognized neutral industry institution or dataset** (e.g. an established
   third-party TA-duration benchmarking service), or **(b) a named individual expert with no
   prior engagement history with either party**, or **(c) an independently validated
   multi-turnaround historical benchmark methodology** built from data spanning multiple,
   unrelated customer relationships — not derived solely from this contract's own history.

Joint selection remains necessary (neither party may impose a benchmark unilaterally) but is
no longer treated as sufficient. This tightens, not loosens, Event 9's Phase 3-4
prerequisite — it was already gated on a benchmark provider being named; it is now also gated
on that provider passing these three tests, which must be documented at contract
mobilisation and re-attested at each TA cycle (commercial relationships can change over a
multi-year contract term).

**Mid-execution benchmark changes are locked down, not merely discouraged:** any benchmark
adjustment requested after a turnaround's execution has begun requires **both** dual Finance
sign-off (customer and provider) **and** independent reviewer approval — the same
independent reviewer role defined in `08_OPERATING_MODEL/VALUE_VALIDATION_BOARD_MVP.md`.
This closes the obvious gaming window (either party trying to move the goalposts once early
execution results are visible) that a simple "benchmark is pre-agreed" rule alone doesn't
fully prevent.

## Metrics considered
- Critical-path duration (actual vs. independent benchmark)
- Planned vs. actual productive wrench time
- Schedule adherence (% of scope items completed within their scheduled window)
- Rework (subtracted from claimed gains, not merely excluded — see below)
- Emergent work attributable to execution quality (vs. genuinely unforeseeable)
- Start-up delay attributable to maintenance execution (vs. operations/process causes)

## Controllability
Primarily provider-controlled (execution planning, crew productivity, sequencing), with
defined customer dependencies: completeness/accuracy of condition data at scope freeze,
production/utilities support during the TA window, and any customer-contracted third-party/
OEM work performed outside the provider's coordination.

## Attribution rule (testable, all conditions required)
A Turnaround Execution Efficiency claim qualifies only if:
(a) scope was jointly frozen and documented before execution start, with no material
customer-driven scope change during execution (material = exceeds the €100,000 / 0.25% ACV
threshold);
(b) an independent, jointly-selected baseline critical-path duration was set before
execution start;
(c) actual critical-path duration is measured against that frozen baseline;
(d) emergent work is classified execution-attributable vs. unforeseeable via joint RCA,
reusing the same "novel/unforeseeable failure mode" exclusion logic as Event 4 Step 3;
(e) rework hours are **subtracted** from claimed productive wrench-time gains, not just
excluded from the numerator — rework is a negative adjustment;
(f) post-TA start-up delay is evaluated via joint RCA using a mini decision path mirroring
Event 4 (was the delay due to a specific maintenance execution deficiency, vs. an operations
restart procedure or process issue?) and, if execution-attributable, is subtracted as a
duration/value penalty.

## Financial value
Avoided cost of schedule overrun — extended-outage production loss at the agreed
contract-fixed standard margin (same methodology as Event 4), plus any incremental
contractor/resource cost of an extended TA — for the verified execution-attributable
duration improvement, **net of** rework cost and net of any execution-attributable start-up
delay cost.

## Payment eligibility
Reliability Value Engine — event reward / performance fee. Phase 3-4 (requires a full TA
cycle and a functioning independent-benchmark relationship, not available at Phase 1-2).

## Stress test (12-point, condensed)
- **Dispute potential:** High — similar to Event 5's multi-year comparability problem, but
  more tractable because independent (not self-set) benchmarking removes Event 6's
  conflict-of-interest failure mode.
- **Recommendation: KEEP**, designed contract-ready from the outset given the lessons
  applied, but **conditional on a named, jointly-agreed independent benchmark provider being
  selected before the first TA cycle** — without it, this event cannot be used at all.

## Red Team results (folded into `cycle4_red_team_scenarios.md`, Scenario 13)
Tests whether "independent" actually means independent (provider-selected estimators don't
qualify), and whether emergent-work/start-up-delay disputes can reuse Event 4's existing
decision-tree infrastructure rather than requiring bespoke new process — confirmed they can.
