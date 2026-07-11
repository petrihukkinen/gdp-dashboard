# Contract Language Risk — Cycle 3

Role: highly skeptical industrial contract lawyer. For each ambiguous term: why it creates
dispute risk, a measurable replacement definition, and the residual risk that remains even
after the fix — no term is claimed to be made perfectly dispute-proof.

| Term | Dispute risk | Measurable definition | Remaining risk |
|---|---|---|---|
| **attributable** | No causal threshold defined — 30% contribution? Sole cause? | "The sole or predominant (>50% contribution, as jointly determined by the Value Validation Board via the Event 4 decision tree) proximate cause, excluding factors separately classified as customer-controlled or excluded." | Joint determination of "predominant" in genuinely mixed-cause events still requires judgment — bounded, not eliminated, by requiring VVB supermajority. |
| **avoided** | Inherently counterfactual, unfalsifiable on its face. | Usable only where evidence meets Level 1 or 2 of the `COUNTERFACTUAL_PROTOCOL.md` hierarchy. | Even Level 1/2 evidence is probabilistic, not certain. Mitigated via conservative discounting, never fully eliminated. |
| **improvement** | Improvement vs. what baseline, over what period, normalized how? | "The delta between the frozen pre-period baseline (index-adjusted, volume-normalized per the agreed methodology) and the measured value in the commercial period, from named data sources only." | Baseline freeze date and index selection are themselves negotiated points — a pre-contract dispute risk, not a post-contract one. |
| **baseline** | Which period, whose data, adjusted or raw? | Jointly agreed, frozen in writing before the commercial period starts, sourced only from named systems, with a mandatory outlier-year review before freezing. | Atypical baseline years (unusually good or bad) remain a dispute risk even with outlier review — reduced, not removed. |
| **controllable** | Binary language hides a real spectrum, inviting disputes about which side of the binary an event falls on. | Replace entirely with the four-tier taxonomy (provider-controlled / primarily provider-controlled with named dependencies / jointly-influenced / customer-controlled / excluded) — never used alone; every reference must cite the specific tier and the named dependency list. | A new situation not anticipated by the dependency list at signing needs an amendment/escalation path — see `VALUE_VALIDATION_BOARD_MVP.md`. |
| **material** | No numeric threshold — invites disputes over trivial events. | A numeric de minimis threshold (specific € or % figure — **not yet set; a commercial decision for Petri**, not invented here) below which events aren't reviewed at all. | Threshold-setting itself can be gamed by structuring claims just above/below the line — needs periodic review. |
| **reasonable** | Classic unresolvable contract-law ambiguity — no objective test exists. | Replaced wherever possible by the specific testable rules already built (SLA timings, decision trees, evidence hierarchies). Where unavoidable (e.g. "reasonable engineering judgment" in an RCA), require it be exercised by a named, credentialed role with documented rationale, subject to VVB review. | Any human-judgment element retains irreducible ambiguity — the goal is minimizing its surface area, not eliminating it. |
| **verified** | Verified by whom, to what standard? | "Reviewed and approved by the Value Validation Board per its defined process, with evidence meeting the minimum tier specified for the event/payment type." | VVB itself could deadlock or be perceived as biased — mitigated by the escalation/independent-review trigger, not eliminated. |
| **recurring** | Does a one-time fix "recur" as an annual payment forever? | "Recurring value must be re-verified against current-period actual data each measurement period; no value carries forward automatically without re-measurement." | Administratively heavier — a real cost/effort trade-off, disclosed rather than hidden. |
| **provider-caused / customer-caused** | Implies binary causation in what are usually multi-causal industrial events. | Replaced entirely by the decision-tree/evidence-hierarchy approach — never used as a stand-alone contract trigger. | Same residual judgment risk as "attributable" in genuinely mixed-cause events. |

## Lawyer's overall verdict
None of these terms can be made fully dispute-proof — that is not achievable in an
industrial performance contract, and claiming otherwise would itself be a credibility
failure. What this pass achieves is converting ten sources of open-ended ambiguity into a
smaller number of bounded, procedurally-governed judgment calls, each routed through the
Value Validation Board rather than left to unilateral interpretation by either party. The
`material` threshold and several SLA numbers referenced above are not yet set — these are
commercial decisions, not further legal drafting, and are logged as required Petri decisions
in the Cycle 3 final output.
