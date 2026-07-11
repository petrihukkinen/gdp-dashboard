# Model Claim Audit — Cycle 12

## The error
Across Cycles 10-11, the word "realistic" (and related fact-implying language — "confirms,"
"validates") was repeatedly applied to figures that were never externally sourced. The
specific failure pattern: Cycle 10 built an illustrative sensitivity model and stress-tested
Control Tower cost at 8% as a "pessimistic scenario." Cycle 11 independently built a
different, bottom-up (zero-based organizational) model and arrived at a similar figure
(~7-8%). **Two internally-generated conceptual models agreeing with each other is internal
consistency between this project's own reasoning — it is not external validation.** Calling
the resulting number "realistic" implied the project had learned something true about the
world. It had not. Nothing in this project has obtained real Control Tower delivery cost
data from any source outside this project's own modelling.

## The corrected standard statement
Per Petri's Cycle 12 instruction, the only accurate framing of every conceptual sensitivity
result in this project, going forward, is:

**"The Accountability Economics Thesis remains positive in the conceptual sensitivity model
under the tested assumptions. Real-world unit economics remain unvalidated."**

Any file that states or implies otherwise is corrected below or flagged for correction.

## Files corrected
| File | What was corrected |
|---|---|
| `10_FINANCIAL_MODEL/CONTROL_TOWER_UNIT_ECONOMICS.md` | Full rewrite — removed "realistic" as a fact-claim throughout; reframed the Cycle 10/11 convergence as internal consistency, not validation; added the standard corrected statement explicitly |
| `10_FINANCIAL_MODEL/alv_model_illustrative.csv` | Renamed scenario rows `accountability_single_pilot_realistic` → `accountability_single_pilot_unamortized`, `accountability_portfolio_scale_realistic` → `accountability_portfolio_scale_amortized` — the label itself was making a fact-claim, not just the prose around it |
| `DECISION_LOG.md` (Cycle 11 entry) | Corrected "realistically ~7-8%" and "the realistic day-one number" to describe the figure as an internally-convergent modelling assumption |
| `WORKPLAN.md` (Cycle 11 entry) | Same correction applied |
| `RISK_REGISTER.md` (single-pilot cost risk row) | Corrected to state the cost figure is modelled/assumed, not evidenced, and added a caveat to the risk's own probability/mitigation columns reflecting that the underlying assumption is itself unvalidated |

## Files reviewed and found acceptable (hedged appropriately, not corrected)
- `10_FINANCIAL_MODEL/FIVE_ECONOMIC_MECHANISMS.md` — "realistic upside" used to describe a
  bounded *range* within the model's own logic (lead-generation vs. guaranteed-award), not a
  claim about real-world magnitude.
- `10_FINANCIAL_MODEL/CONTROL_TOWER_SCALE_CURVE.md` — "explicitly confirmed by this
  analysis" refers to a logical consequence of the model's own structure (the pilot-cost-
  loading effect is a mathematical property of unamortized fixed cost, true by construction),
  not an empirical claim about the world. Left as is.
- `08_OPERATING_MODEL/CUSTOMER_DUPLICATION_TEST.md` — "realistically transferable" is a
  section header meaning "plausible in principle," immediately followed by explicit
  instruction not to assume the outcome. Left as is.
- `10_FINANCIAL_MODEL/gate3_verdict.md` — "confirmed" is used exclusively for Checker
  arithmetic/logic verification (re-deriving a sum, checking a cap rule applies as designed)
  — legitimate use, since these are properties of the model's own internal consistency, not
  claims about external reality.

## The broader pattern this project must guard against
This is not the first time internal modelling language has drifted toward fact-like framing
in this project — the entire multi-cycle discipline (Level A/B/C evidence tagging since
Cycle 1, the repeated "illustrative, not real data" labels since Cycle 5) exists specifically
to prevent this drift. Cycle 12's finding is that the discipline held at the level of
explicit disclaimers ("all figures illustrative") but **failed at the level of individual
word choice within the surrounding prose** — a disclaimer at the top of a document does not
protect against "realistic," "confirms," or "validates" appearing three paragraphs later in
a way that contradicts it. **Going forward: any sentence describing a modelled figure's
plausibility must use language scoped to the model ("within this model," "under these
assumptions," "this project's two internal methods agree") and must never use unscoped
fact-language ("realistic," "confirmed," "validated," "proven") unless the claim is
externally sourced and cited.**
