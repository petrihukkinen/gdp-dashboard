# Control Tower Unit Economics — Cycle 11

**Corrected, Cycle 12 (epistemic audit — see `MODEL_CLAIM_AUDIT.md`).** The original version
of this file used "realistic" to describe cost assumptions that were never externally
sourced — two internally-generated illustrative models agreeing with each other is internal
consistency, not real-world validation. Corrected below. CSV scenario rows renamed
`accountability_single_pilot_unamortized` and `accountability_portfolio_scale_amortized`
(were `..._realistic`).

Updates `alv_model_illustrative.csv` with two new rows rather than creating a conflicting
model. **All figures remain indexed, illustrative modelling assumptions — no Bilfinger or
real customer data, and no external validation of any kind.**

## Incremental cost bridge, in numbers (illustrative modelling assumptions only)

| Scenario | Conventional mgmt cost (% revenue) | AMOR dedicated site (Category B) | AMOR shared, portfolio-amortized | AMOR shared, single-pilot unamortized | Total AMOR incremental vs. conventional |
|---|---|---|---|---|---|
| Portfolio scale (Model B/C, 5+ accounts) | 8% (baseline, same as conventional) | +2% | +1.5% | — | **~3.5%** |
| Single pilot (Model A, no sharing) | 8% | +2% | — | +5-6% | **~7-8%** |

## Cross-cycle internal consistency (not external validation)

Cycle 10's stress test used 8% Control Tower cost as its pessimistic scenario, producing a
net illustrative value of ~72 (versus a 148 base case at 3% cost). This cycle's zero-based,
bottom-up organizational analysis **independently arrives at a similar illustrative figure
(~7-8%) for a single-pilot deployment** using a different method (headcount/role logic
rather than top-down stress testing).

**This is internal consistency between two conceptual models built by this project, not
confirmation from any external source.** It is a mild positive signal that the two modelling
approaches don't contradict each other — it is not evidence about what Control Tower
delivery actually costs in the real world. No real delivery cost data has been obtained
anywhere in this project. The correct statement, per Petri's Cycle 12 correction:

**"The Accountability Economics Thesis remains positive in the conceptual sensitivity model
under the tested assumptions. Real-world unit economics remain unvalidated."**

## Break-even logic (within the conceptual model only)

At the single-pilot cost assumption (~7-8%, `accountability_single_pilot_unamortized` row),
the illustrative net value is **~75** in the model, versus the conventional baseline's
**~49** — a positive advantage (roughly 1.5x) *within the model's own internal logic*, more
modest than the ~3x shown at the portfolio-scale assumption
(`accountability_portfolio_scale_amortized`, ~157 at 2% cost). **Whether this advantage
exists in reality is untested.** The model does not go to zero or negative under any tested
assumption range — that is a property of the model's internal structure, not a finding about
real economics.

## Sensitivity ranking (within the conceptual model)
1. Control Tower shared-cost amortization (single pilot vs. portfolio assumption).
2. Whether customer-transferred work materializes (`CUSTOMER_DUPLICATION_TEST.md`) —
   itself entirely untested.
3. Additional scope revenue actually captured (Mechanism 1's realization) — also untested.

## What this means for deal sequencing — as a modelling caution, not a proven rule
**If** a real first deal is evaluated, it should be evaluated against the single-pilot
assumption set, not the portfolio-scale one — using portfolio-scale assumptions for a first
deal would be internally inconsistent with this project's own model, regardless of whether
either assumption set turns out to reflect reality. This is a discipline recommendation for
how to *use the model consistently*, not a claim that the model's numbers are correct.
