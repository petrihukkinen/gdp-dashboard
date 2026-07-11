# Customer CFO Attack — Cycle 3

Role: skeptical customer CFO, commercially sophisticated, accepts no vague language.
Answers below apply the architecture built in `event_stress_test.md`; where the architecture
doesn't yet answer the question, that is stated as a gap, not papered over.

**Are savings gross or net?**
Currently undefined in the Cycle 2 draft — a real gap. **Fix:** every event's financial
value must be stated net of provider fee, net of any customer-funded enabling investment
(Capex, transition cost), and net of Year-1 mobilization cost (already built into Event 1).
No event's financial value calculation may report a gross figure to the Value Validation
Board.

**Are savings recurring?**
Not tagged per event today. **Fix:** apply the "recurring" contract definition in
`CONTRACT_LANGUAGE_RISK.md` — no value carries forward automatically; every period requires
fresh re-verification. See Scenario 10 in `ATTRIBUTION_DISPUTE_SCENARIOS.md`.

**Are savings already included in budget?**
Real risk if baseline freeze timing isn't fixed relative to the customer's own budget cycle.
**Fix:** every baseline must be frozen in writing *before* the commercial period starts and
reconciled against the customer's approved budget for that period — a claim cannot exceed
what the customer's own budget didn't already assume.

**Are avoided losses real cash value?**
Only Event 1 produces hard cash (real invoices). Events 3, 4, 5, 6 are avoided-loss claims —
counterfactual, never certain. **Fix:** the `COUNTERFACTUAL_PROTOCOL.md` evidence hierarchy
exists precisely to stop weak counterfactual claims from being treated as cash-equivalent.

**Are we paying for normal supplier obligations?**
Real risk for Event 1: if a contractor's improved rate was already contractually scheduled
before the provider's involvement, that's not provider-created value. **Fix:** Event 1's
attribution rule must exclude rate changes that were pre-existing contractual obligations,
not provider-driven negotiation.

**Are we paying twice for fixed-fee scope and gainshare?**
Structural risk: Event 1 sits inside scope already priced into the Base Fee. **Fix:** the
gainshare benchmark must always be the frozen pre-transition baseline, never the current
Base Fee assumption — and once a rate improvement is absorbed into a renewed Base Fee at
contract renewal, it stops being gainshare-eligible. No double payment across fee resets.

**How are inflation and volume changes normalized?**
Not specified for any event today — real gap. **Fix:** every baseline is indexed to a named
cost index and, where volume materially affects the metric, expressed per-unit rather than
in absolute euros (Event 1 already is; Event 4's financial value needs explicit volume
normalization added).

**How do we treat Capex-funded improvements?**
Real risk, illustrated in Scenario 3 (`ATTRIBUTION_DISPUTE_SCENARIOS.md`): if the customer
funded the intervention (e.g. equipment replacement), the provider did not create the value
by itself. **Fix:** every Event 3/5/6 claim must declare funding source; customer-funded
Capex interventions are excluded from gainshare by default unless a separate,
explicitly-negotiated project-delivery fee applies.

**Who funded the intervention?**
Same as above — funding source tracking is now a mandatory field in every high-stakes event
submission, not optional.

**How are production margins calculated?**
Event 4's financial value must use an agreed, contract-fixed standard margin set at signing
— never the spot margin at time of the event. This protects both parties symmetrically from
market-volatility gaming.

**Can the service provider choose favorable events (selection bias)?**
Real, currently unmitigated structural risk: nothing stops a provider from only bringing
forward claims that favor it. **Fix:** the Value Validation Board submission process
(`VALUE_VALIDATION_BOARD_MVP.md`) requires a mandatory completeness declaration — the
provider attests all qualifying events in a category were logged, not cherry-picked. Not a
complete fix (self-attestation is imperfect), but the strongest available mitigation without
a full independent audit function, which would be a Gate 3/4 cost-benefit decision.

**What prevents double counting?**
See `DOUBLE_COUNTING_MAP.md` — a PRIMARY/SECONDARY/CONTEXT hierarchy where only the primary
event may be monetized, with mandatory cross-reference checks at submission.

## CFO verdict
The architecture answers most of these questions once the fixes above are applied — but as
of the Cycle 2 draft, none of these fixes existed. A real CFO reviewing the Cycle 2 version
alone would have rejected it. The Cycle 3 version is materially stronger, but three items
remain open pending Petri/commercial decisions: numeric SLA thresholds, the cost index to
use, and the de minimis materiality threshold — see `gate2_assessment.md`.
