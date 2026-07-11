# Strategic Thesis — Bilfinger Asset Performance 2030

Status: first-cycle draft, maker pass complete, checker pass complete (Section 4). This is the architecture to pressure-test with Petri directly — see `OPEN_QUESTIONS.md` for what would change it.

## 0. One-sentence thesis

Bilfinger should sell a staged, attribution-gated path from fixed-scope maintenance to KPI-linked and gainshare fees — not because "performance" is a new idea (Bilfinger already says "Your Performance Is Our Business" and runs BCAP®), but because Bilfinger, almost uniquely among industrial service providers, could credibly design the **contractual and attribution mechanism** that makes that slogan payable, using a leadership hire who has priced this risk from both the provider side (ABB) and the customer side (Neste).

## 1. What customer problem are we solving?

**Fact/experience basis:** Asset owners (from the Neste-side experience) run maintenance as a cost center they are structurally incentivized to squeeze every budget cycle, while simultaneously needing more reliability, more throughput, and lower emissions from an aging, increasingly automated asset base with a shrinking internal technical bench (retirements, fewer in-house reliability engineers). This creates a persistent mismatch: the commercial model (rate cards, fixed scope, hourly billing) rewards activity, while the customer's actual need is an outcome (fewer unplanned shutdowns, longer run length, lower total cost of ownership).

**Customer problem, stated plainly:** industrial asset owners cannot get a maintenance/reliability partner who is financially motivated to make the *plant* perform better rather than to sell more hours, more scope, or more turnaround work. The customer bears essentially all of the performance risk today; the provider bears essentially none.

## 2. Why is the traditional maintenance commercial model insufficient?

Rate-card and fixed-scope models pay for inputs (hours, headcount, scope items), not outcomes. This creates three specific failure modes, all observed in the AMOR material and in Petri's ABB/Neste experience:
- **Misaligned incentives at the margin.** A time-and-materials or even fixed-scope provider's easiest path to margin is scope creep or minimum-effort compliance, not proactive reliability investment that could reduce future work (and future revenue) for the provider.
- **No mechanism to reward genuinely differentiated performance.** AMOR itself, even after moving to fixed price, had no way to earn more by delivering a better plant — only a way to earn the same fee more efficiently. This caps the provider's upside and gives it no reason to bring its best people or its best ideas.
- **Cost-plus and even fixed-price models don't resolve the customer's real anxiety, which is unplanned loss, not unit cost.** A customer facing a €2m/day margin loss from an unplanned outage does not primarily care whether the maintenance invoice was 3% higher or lower that year.

## 3. Where is the economic value pool?

Three distinct pools, and the concept must be honest about their relative size and Bilfinger's realistic share of each (see `08_FINANCIAL_MODEL/` for the build-out):

1. **Cost-side pool (AMOR's pool):** hands-on-tool-time improvement, subcontractor consolidation, right-sizing, spares/working-capital optimization. AMOR's own figures (unaudited) suggested €43–60m/year of addressable value at a single large refinery. This pool is real but is being competed away today by every maintenance-outsourcing provider — it is not a differentiator, it's table stakes to even be considered.
2. **Reliability/availability pool:** the value of avoided unplanned downtime, extended run length between turnarounds, and reduced trip/upset frequency. This is typically an order of magnitude larger than the cost-side pool at a large continuous-process asset (a single unplanned shutdown at a refinery or cracker can cost more than a full year of maintenance-cost savings) — but it is the pool where attribution is hardest, because unplanned downtime has many non-maintenance causes.
3. **Capital-efficiency pool:** deferring, right-sizing, or avoiding Capex through better lifecycle management and integrity data — a pool that shows up on the customer's balance sheet, not P&L, and is attractive to a customer's CFO in a different way than opex savings.

**The strategic implication:** the biggest pool (#2) is also the pool with the hardest attribution problem. The commercial model has to be built so Bilfinger earns a growing share of value as attribution confidence increases (Phase 0 → 4), rather than promising day-one access to the whole pool.

## 4. What part of performance can Bilfinger credibly influence?

Bilfinger can credibly influence, and should be willing to be measured and paid on:
- Maintenance execution quality (schedule compliance, work-order backlog, PM/PdM completion rates, hands-on-tool time).
- Equipment-level reliability outcomes for equipment fully within Bilfinger's maintenance scope (MTBR/MTBF for covered assets, defect elimination close-out rate).
- Turnaround execution performance (duration vs. plan, cost vs. budget, safety incidents during the TA — areas where Bilfinger is the direct executing party).
- Spares/inventory service levels and working-capital metrics, where Bilfinger manages the function.
- Contractor/subcontractor performance where Bilfinger is the named integrator.

Bilfinger **cannot** credibly be paid on, without an attribution layer:
- Total plant OEE or total operational availability (driven heavily by operations, feedstock, process technology, and planning decisions Bilfinger does not control).
- Total production output or margin (driven by market/commercial decisions entirely outside Bilfinger's scope).
- Safety metrics for the whole site (TRIF/PSER) where Bilfinger's workforce is one of several populations on-site.

This is the direct, explicit statement CLAUDE.md rule #5 requires: **no fee should be linked to total OEE without the attribution model in `05_KPI_ATTRIBUTION/` first assigning a defensible Bilfinger-attributable share.**

## 5. What must remain the customer's responsibility?

- Production planning and scheduling decisions (run rates, feedstock choice, campaign length).
- Operations-caused losses (operator error, process upsets, off-spec feed).
- Capex sanctioning and prioritization — Bilfinger can recommend and execute, but investment decisions and the capital itself stay with the owner.
- Process technology and licensor-driven constraints.
- Force majeure, utility failures outside Bilfinger's scope, and macro/market conditions.
- Ultimate safety and regulatory accountability — Bilfinger can be measured on its own contribution to site safety performance, but statutory operator responsibility does not transfer.

## 6. How should performance attribution work?

Full detail belongs in `05_KPI_ATTRIBUTION/`; the thesis-level principle is:

- **Every KPI proposed for fee-linkage must be decomposed, before contract signature, into a loss/gain-driver tree** that separates: maintenance-caused, equipment-reliability (design/age, not upkeep), operations-caused, feedstock, production-planning, utility, process-technology, force majeure, customer-delayed-decision, and customer-controlled-Capex components.
- **Only the maintenance-caused and Bilfinger-scope-reliability branches are fee-eligible**, and only once a joint baseline has been agreed using historical data plus an agreed methodology for classifying ambiguous events (this is what a Value Validation Board is for — see below).
- **Attribution confidence should gate contract phase, not the other way around.** A customer/site with poor instrumentation, poor loss-event tagging discipline, or unclear operations/maintenance boundaries should stay in Phase 1–2 (open book / fixed scope) until attribution data quality improves — not be pushed into gainshare on hope.

**Value Validation Board (joint verification mechanism):** a standing joint committee (Bilfinger + customer reliability/finance representatives, meeting monthly/quarterly depending on phase) that: (a) reviews and classifies disputed loss events against the pre-agreed decision tree, (b) approves baseline resets when scope, feedstock, or asset configuration changes materially, (c) has an explicit, pre-agreed escalation and tie-break mechanism (e.g., a named third-party reliability auditor) for events neither side can agree on, and (d) publishes its classification decisions so the mechanism builds precedent and trust over the contract term rather than relitigating every year. This board is a cost center, not a free good — it must be resourced and its cost accounted for in the deal economics (see `08_FINANCIAL_MODEL/`).

## 7. How should contract risk be limited?

- **Painshare (if any) should be capped as a percentage of the fixed fee, never open-ended**, and should only apply to KPIs with high attribution confidence (Bilfinger's own scope, e.g., maintenance-caused trip rate for covered equipment) — never to total OEE or site-wide metrics.
- **Gainshare should be uncapped on the upside** (this is the entire point — it's what makes the model attractive to Bilfinger and differentiates it from a penalty-only SLA regime) but should only trigger above a jointly validated baseline, with a defined true-up/reconciliation cadence.
- **A phase should never advance until the prior phase's baseline and attribution data have been jointly signed off** — this is a contractual gate, not a target date, and needs to be written into the master agreement so sales cannot informally accelerate a customer into gainshare to close a deal.
- **Termination-for-convenience and re-basing clauses** need explicit provisions for major disruptions (feedstock change, major Capex, force majeure) so painshare exposure cannot be triggered by events fully outside Bilfinger's control.

## 8. What is the commercial model?

Staged architecture, matching the brief:

- **Phase 0 — Due diligence and baseline.** Paid engagement (not free) to assess maintenance data quality, current KPI baselines, attribution feasibility, and organisational readiness. Output: a joint fact base and an explicit go/no-go on which KPIs, if any, are gainshare-ready.
- **Phase 1 — Open book / transformation.** Cost-plus or transparent markup, Bilfinger builds trust and operating rhythm, same logic AMOR used for Years 1–2, but run by Bilfinger as an external provider rather than via employment transfer.
- **Phase 2 — Fixed scope / fixed baseline fee.** Table-stakes maintenance-outsourcing economics; this is where most competitors already are.
- **Phase 3 — KPI-linked performance fee.** A minority of total fee (illustratively 10–20%, to be modeled in `08_FINANCIAL_MODEL/`) at risk against Bilfinger-attributable KPIs only.
- **Phase 4 — Gainshare / selected painshare.** Only for KPIs the Value Validation Board has certified as objectively measurable and attributable, on a jointly agreed baseline, typically after 2+ years of Phase 2–3 track record at a given site.

Revenue architecture: **Base Fee + Fixed Scope + Performance Fee + Gainshare + Selected Painshare + Digital Services + Transformation Projects.** Digital Services (e.g., BCAP®-type subscriptions) and Transformation Projects (turnarounds, CMMS migrations, reliability improvement programs) are separately billed regardless of contract phase — they are not contingent on gainshare maturity and provide revenue stability while the attribution relationship matures.

## 9. How does Bilfinger make higher-quality earnings?

"Higher-quality" means: more recurring, less price-competed at re-tender, higher-margin, and less correlated with one-off project/turnarounds cyclicality. The mechanism:
- Multi-year Phase 3–4 contracts are structurally harder for a competitor to under-bid at renewal, because switching costs include losing an established attribution track record and Value Validation Board precedent.
- Performance fees and gainshare, once earned, sit at materially higher margin than fixed-scope labour delivery, because they are priced against value created, not hours worked — directly addressing the gap between Bilfinger's current ~5.5% group EBITA margin and its stated 8–9% 2030 ambition (see `14_RESEARCH/BILFINGER_FACTS.md`).
- Digital-services subscriptions (BCAP®-type) attached to the relationship add a recurring, higher-margin revenue line independent of labour headcount.

## 10. Why can Bilfinger credibly deliver this?

This is where Petri's specific background is the answer, not a generic Bilfinger capability claim:
- ABB experience proves the provider-side commercial mechanics of moving ~43 contracts from hourly to fixed/performance models are achievable in practice, not just in theory, and shows what breaks when a provider takes on that risk.
- Neste experience proves what an asset owner actually needs to trust a provider with attribution-linked fees, and where an owner's own organisation resists (procurement structure, internal politics, data reluctance) — i.e., credibility on the buy side, which most services-industry leaders pitching this concept lack.
- AMOR proves lived, hands-on design of an integrated maintenance operating model, governance cascade, and staged commercial progression at real scale (350 FTE, a full refinery) — even though AMOR itself stopped short of the attribution/gainshare mechanism, which is exactly the gap this new role would close.
- Bilfinger's own existing assets (BCAP® platform, Maintenance Concept, Maintenance Intelligence, existing customer base in energy/chemicals/pharma) provide the delivery substrate; what's missing is the commercial/contractual architecture connecting them to outcome-based fees, which is Petri's specific, provable contribution.

## 11. How can the concept be piloted?

- Select 1–2 existing Bilfinger accounts (not a new-logo win) where Bilfinger already has multi-year maintenance delivery history, a working CMMS/data relationship, and — critically — good loss-event tagging discipline, so Phase 0 due diligence has a realistic chance of producing a usable attribution baseline.
- Run Phase 0 as an explicitly paid, time-boxed engagement (e.g., 3–4 months) with a hard go/no-go gate: if attribution data quality is inadequate, the account stays in Phase 1–2 and is not forced toward gainshare.
- Treat the pilot's Value Validation Board as the proof-of-concept for the governance mechanism itself, not only for the commercial outcome — the case study needed for scaling is "the attribution and dispute-resolution mechanism worked, and both sides would sign it again," not just "Bilfinger earned a bonus."

## 12. How can it be scaled across customers and countries?

- Scale the **mechanism and playbook** (Phase 0 due-diligence methodology, attribution decision-tree template, Value Validation Board governance charter, contract templates), not a one-off bespoke deal each time — this is the main defensible reason this becomes a platform rather than a series of one-off negotiations.
- Sequence scaling by industry vertical where loss-attribution is most tractable first (continuous, well-instrumented process industries — refining, petrochemicals — before less-instrumented or more operations-dominated sectors).
- Build the internal capability (attribution methodology owners, Value Validation Board facilitators) as a shared service inside Bilfinger, not duplicated per account team, so unit economics improve as the number of Phase 3–4 accounts grows.
- Resist scaling by relaxing the attribution gate to close more deals faster — the entire credibility of the model depends on Phase 3–4 only being offered where it's earned; a diluted version sold broadly would produce exactly the disputed-baseline failures that discredit outcome contracting generally (see `RISK_REGISTER.md`).

## Section 4 — Checker pass (skeptical Bilfinger CEO / CFO / customer-CFO read)

- **Is this commercially credible?** Partially. The staged logic and the explicit attribution gate are credible and match how sophisticated performance-contracting actually gets built in other industries (e.g., aerospace power-by-the-hour, which took decades and started narrow). The unproven part is whether the attribution methodology can survive a real, adversarial dispute at Phase 4 — this document asserts a mechanism, it does not yet prove one.
- **Is this differentiated?** Only if positioned correctly. As "asset performance partnership," no — Bilfinger already says this. As "a specific, named attribution and staged-risk contracting mechanism, designed by someone who has priced this exact risk from both sides," yes — that's a narrower and more defensible claim.
- **Can Bilfinger actually control the result?** Only for the scope explicitly listed in Section 4 above. The thesis is careful about this; the risk is that sales and customer pressure erode the discipline over time (see Risk Register item on internal resistance/dilution).
- **Is the contractual risk acceptable?** Yes, as structured (capped painshare, uncapped gainshare, phase gates) — but only if Bilfinger's legal and risk functions are actually involved in designing the gate criteria, not just informed after the fact. This is currently an open question, not a settled fact.
- **Is the financial logic clear?** Directionally yes (higher-margin, more recurring revenue supporting the stated 2030 EBITA ambition); not yet quantified. `08_FINANCIAL_MODEL/` needs real modeling with ranges, not adjectives.
- **Is this scalable?** Conditionally — scalable as a playbook/mechanism, not as a promise to every account. The biggest threat to scalability is attribution being fundamentally plant-specific (see AMOR_ANALYSIS.md risk #6).
- **Is this merely consulting language?** The parts that are still at risk of being consulting language are the "Value Validation Board" (named but not yet designed as an operating mechanism with headcount, cost, and authority) and the digital/AI module list (must clear the `07_DIGITAL_AI/` discipline before being included in any pitch). Both are flagged as incomplete, not resolved, in this document.
- **What would a skeptical industrial CEO attack first?** "Show me the attribution methodology working on a real, disputed event, with real money on the line, not a slide." That is the single most important thing to build or find before this goes into a CEO-facing pitch — see `WORKPLAN.md`.
