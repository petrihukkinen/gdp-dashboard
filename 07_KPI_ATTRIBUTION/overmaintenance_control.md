# Over-Maintenance / KPI Gaming Control — Cycle 4

Closes Red Team gap A from Cycle 3 (`RISK_REGISTER.md`). Design goal: detect whether the
provider is inflating maintenance intensity primarily to avoid Event 4 painshare exposure —
**without creating a new incentive to under-maintain in order to pass the check.** Both
directions are gaming; both are tested.

## Composite metrics

**Maintenance Intensity Index (MII)** — a weighted composite of PM/PdM hours, work-order
count, parts consumption €, and production-access-hours demanded, per criticality-weighted
asset unit, trended quarterly against a rolling baseline band (illustrative default: baseline
± 15%, to be calibrated against real asset data before go-live — not yet done, see
`gate3_readiness_assessment.md`).

**Risk Reduction Efficiency (RRE)** — documented asset risk-score improvement ÷ MII for the
same period. This is the metric that prevents the control from rewarding minimum activity:
a provider that legitimately does *less* work because the asset genuinely needs less (risk
score stable or improving, MII appropriately low) shows a healthy RRE. A provider that cuts
activity while risk scores degrade shows a collapsing RRE — caught by the same instrument
that catches over-maintenance, not a separate one-sided rule.

## Signals tested (per Petri's list)

1. **Intervention intensity vs. risk-adjusted asset criticality** — MII benchmarked per
   criticality tier, not fleet-wide, so a genuinely high-criticality asset isn't flagged for
   receiving more attention than a low-criticality one.
2. **Maintenance cost and labour-hour trend** — rolling trend, flagged if it moves outside
   the baseline band net of agreed inflation/volume indexation (same indexation principle as
   `CONTRACT_LANGUAGE_RISK.md`'s "improvement" fix).
3. **PM/PdM task additions and frequency changes** — net new tasks/frequency increases
   tracked against whether a documented RCM/FMEA technical justification exists on file.
   Absence of justification is itself a signal input, not just a documentation nicety.
4. **Parts consumption** — spend/volume trend per asset class; spikes without corresponding
   condition or failure evidence are a signal input.
5. **Repeat intervention rate** — tests whether increased activity is actually *effective*.
   High activity with a still-elevated repeat-intervention rate is a stronger gaming signal
   than high activity with a falling repeat rate (the latter suggests real problem-solving).
6. **Production intrusion / access demand** — access-hours requested for PM per criticality
   unit; disproportionate increases are a signal input.
7. **Risk reduction achieved per intervention** — the RRE metric itself, the central
   discriminator between legitimate intensity and padding.

## Red Flag Trigger (explicit, testable)

**Over-maintenance variant** fires only if, within a rolling 2-quarter window overlapping an
open or pending Event 4 exposure period for a given asset/class, **all three** hold:
(a) MII rises above the baseline band ceiling, **and**
(b) RRE for the same period falls below an agreed floor (activity rose, documented risk
reduction did not rise proportionally), **and**
(c) the PM/PdM task additions driving (a) lack the required RCM/FMEA justification on file.

Requiring all three avoids false positives: a genuine, justified reliability campaign shows
(a) but not (b), and has (c) satisfied — it does not trigger.

**Under-maintenance variant** fires if MII falls below the baseline band floor **and**
documented asset risk scores trend upward (declining health) **and** repeat-intervention
rate is rising. This is the mechanism that satisfies Petri's instruction not to reward
minimum maintenance activity — the same framework, not a separate one-sided rule.

## Consequence for payment eligibility

- **Over-maintenance trigger fires:** all Event 3/4 claims for that asset/period are
  suspended pending Value Validation Board review, not automatically rejected. Provider may
  submit a retroactive RCM/FMEA justification; if the Board accepts it, the flag clears and
  normal processing resumes. If rejected, the associated cost increase is presumptively
  excluded from any future Base Fee cost-pass-through or renewal baseline, and a second
  trigger on the same asset class within a rolling 12 months escalates to a mandatory joint
  maintenance-plan review with customer veto rights over further PM/PdM scope changes for
  that class.
- **Under-maintenance trigger fires:** Event 1 gainshare/performance-fee eligibility is
  suspended for the affected asset class (cost "savings" driven by declining maintenance
  intensity correlated with declining asset health is not real productivity value), and an
  immediate joint asset-health review is triggered.
- An active trigger is logged as **context, not automatic penalty**, in any related Event 4
  adjudication — see Step 6 of the revised decision tree in `event4_decision_tree_v3.md`.
  This avoids double-penalizing on an unresolved, unproven flag.

## Residual risk
The baseline bands (±15%) and the RCM/FMEA-justification standard are not yet calibrated
against real asset/fleet data — this control is a design, not a validated instrument. Flagged
in `gate3_readiness_assessment.md`.
