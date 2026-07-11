# CFO Tests and Claims Bureaucracy Test — Cycle 5

## Customer CFO perspective (all three models)

**Am I paying for value I would have received anyway?**
Partially mitigated by the frozen pre-period baseline and net-basis attribution
(`CONTRACT_LANGUAGE_RISK.md`), but the "equal underlying delivery" assumption in
`modelling_assumptions.md` means this remains a live question — if the provider would have
delivered the same improvement without gainshare (Model A's bet), the customer is paying for
something they'd have gotten anyway. Sharpest against Model B/C, where more is paid for the
same activated events.

**Can the provider cherry-pick claims?**
Mitigated by the mandatory completeness declaration (`VALUE_VALIDATION_BOARD_MVP.md`), but
Model A's "selective pursuit" of Event 3 is a *sanctioned* form of the same behavior —
not cherry-picking favorable claims, but choosing not to pursue smaller ones at all. This is
a legitimate bureaucracy-reduction design choice, but it should be named as such in any sales
conversation, not left ambiguous.

**Can I budget this?**
Model A: yes, 96.9% predictable. Model B: less so, 92.3%. Model C: itemized (92.9%
predictable, but with clearer line-of-sight into what each euro buys).

**Can Finance audit every payment?**
Yes structurally — every payment traces to a specific, evidenced, VVB-adjudicated event
(`DOUBLE_COUNTING_MAP.md`), never an aggregate. The audit *burden* scales with event volume
— see the bureaucracy test below.

**Does the provider earn more by increasing maintenance activity?**
Directly tested and mitigated by `overmaintenance_control.md`'s Red Flag Trigger — but the
control's bands are uncalibrated (Cycle 4 gap), so this is a designed answer, not yet a
proven one.

**Is retained customer value clearly greater than provider compensation?**
Yes in the Normal Year scenario for all three models (customer retains €1,422,000-
€2,352,000 vs. provider variable comp of €598,000-€1,680,000) — but this comparison
inverts in the catastrophic/multi-event Event 4 scenarios, where the customer's *actual
documented loss* can exceed what the corridor pays back (Scenario 4 in
`model_comparison_and_stress_test.md`). **This is the sharpest customer CFO objection across
all three models.**

## Provider CFO perspective (all three models)

**Can one event destroy annual margin?**
No — bounded by the per-event and annual caps in all three models. Smallest absolute
protection in Model C (€400,000 per-event cap) given its small Control Tower Fee base.

**Is cash conversion delayed excessively?**
Immaterial for Model A; material for Models B and C (3.6-3.9% of Base Fee tied up to 6
months) unless provisional accrual is adopted — see each model's cash-flow section.

**Is upside sufficient for the risk accepted?**
Ambiguous for Model B specifically: it accepts real painshare exposure (up to €1,600,000/yr)
but its Normal Year upside (€1,340,000) doesn't clearly compensate for that risk relative to
Model A's near-riskless €758,000. **This asymmetry — real downside risk without
proportionate upside reward at these illustrative settings — is a genuine pricing-design gap,
not resolved by this cycle.** Flagged for Cycle 6.

**Are customer dependencies excluded reliably?**
Structurally yes (SLA-driven exclusion, Step 4 of the decision tree) but numerically
unproven — the 48h/24h SLA defaults haven't been tested against real permit/access data.

**Can the model scale without a large claims bureaucracy?**
See below — this is the dedicated test Petri asked for.

**Is the base fee sufficient to fund the operating model before uncertain value payments?**
Model A: clearly yes (highest Base Fee, lowest variable dependency). Model B: **this is a
real open question** — €16,000,000 may or may not cover full delivery cost plus target
margin without gainshare; not verifiable without real cost data, flagged rather than assumed.
Model C: Control Tower Fee alone (€8,000,000) is not meant to fund delivery — Operational
Modules do that separately, so the question applies to the Modules line, not the Control
Tower line.

## Claims bureaucracy test

Illustrative effort estimates (labeled assumptions, not measured data):

| Event | Cadence | Claims/yr (Normal Year, Model B) | Hours per claim (submission+review+VVB) | Annual hours |
|---|---|---|---|---|
| 1 | Monthly | 12 | ~3 | 36 |
| 2 | Monthly | 12 | ~1.5 | 18 |
| 3 | Quarterly | 4 | ~30 (RCA + evidence tiers + netting tracking) | 120 |
| 4 | Ad hoc | 0-2 | ~60 (full decision tree, possible dispute) | 0-120 |
| 5/9 | TA-cycle | 0 (non-TA year) | ~80 each when applicable | 0 |

**Normal Year total: ~174 hours** across all parties combined — modest and manageable at
this illustrative scale. **A "bad year" with 4 Event 4 disputes adds ~240 hours**, pushing
the total to ~414 hours — still likely absorbable, but Event 4 dominates bureaucracy cost per
unit of value whenever disputes are frequent, because it's the only event requiring the full
decision tree *and* carries the highest dispute-escalation risk.

**The point at which precision destroys scalability:** when Event 3 claim volume exceeds
roughly 15-20/year or Event 4 disputes exceed roughly 5/year, *or* when a high proportion of
claims sit near the €100,000 materiality floor — a marginal claim near the floor can cost
€5,000-15,000 in fully-loaded adjudication effort (RCA time, Finance review, VVB session,
possible independent reviewer) against a payout that may be only slightly above that floor,
meaning the administrative cost approaches or exceeds the net benefit of formally pursuing
it. This is precisely the economic logic behind Model A's "selective pursuit" design choice.

## Simplified claims tier (proposed, needed at scale)

**Tier 1 (Fast-Track):** claims comfortably above materiality but below a proposed
€300,000 fast-track ceiling (illustrative, needs confirmation) — single-meeting VVB review,
no independent reviewer required (reserved for genuinely high-stakes events per the original
`VALUE_VALIDATION_BOARD_MVP.md` design).

**Tier 2 (Full Review):** claims above the fast-track ceiling, or any claim triggering a Red
Flag or a dispute — the full process as designed in Cycles 3-4.

This directly reduces bureaucracy for the bulk of smaller, cleaner claims (Events 1, 2, and
most Event 3 claims) while preserving full rigor where the stakes justify it (Event 4, large
Event 3/5/9 claims). **Flagged as a Cycle 6 item to formalize into
`08_OPERATING_MODEL/VALUE_VALIDATION_BOARD_MVP.md`**, not designed in full detail here.
