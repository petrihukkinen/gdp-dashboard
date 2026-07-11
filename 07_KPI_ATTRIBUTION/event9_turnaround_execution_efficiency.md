# Event 9 — Turnaround Execution Efficiency (Cycle 4, new)

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
