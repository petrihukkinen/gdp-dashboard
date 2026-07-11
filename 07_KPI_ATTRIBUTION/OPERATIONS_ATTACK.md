# Operations Executive Attack — Cycle 3

Role: skeptical customer operations executive. This attack surfaces gaps the CFO and lawyer
attacks don't — mainly around plant-level realism and incentive distortion.

**Maintenance doesn't run the plant. Why should they get credit?**
Correct challenge, and it's why credit is tied only to maintenance-controlled interventions
via Event 4's decision tree (`event_stress_test.md`), never to plant-level outcomes as a
whole. No event in this architecture pays on "the plant did well."

**What if operations changed operating mode?**
Covered by the operating-envelope exclusion (Events 3/4). **Gap identified this cycle:** the
"agreed operating envelope" was defined generically as "process envelope" — it must
explicitly enumerate throughput rate, feedstock type/quality, operating mode/campaign, and
ambient conditions if material. Not yet itemized — flagged as a required addition.

**What if feedstock changed?**
Same fix as above — feedstock must be a named envelope parameter, not implied.

**What if production rate was lower?**
This is the CFO's volume-normalization point from the other side. Confirms Event 1 is
correctly rate-based (not absolute €), and confirms the architecture should never add an
absolute-€ "total maintenance cost" payment metric — see Scenario 5 in
`ATTRIBUTION_DISPUTE_SCENARIOS.md`.

**What if we delayed a shutdown?**
This exposed a genuine gap in the Cycle 2 decision tree. A customer-directed schedule delay
against the provider's documented advice increases failure risk, but the plant may still be
technically "within envelope" — so the envelope test alone doesn't protect the provider.
**Fix (added this cycle): Step 3.5 in Event 4's decision tree** — if the provider issued a
documented, dated risk advisory that was overridden by a customer scheduling decision, the
resulting failure is excluded/customer-attributable regardless of other factors.

**What if an equipment failure was unavoidable?**
Covered by Step 3 (novel/unforeseeable failure mode exclusion) in Event 4's decision tree.

**What if a repair prevented one risk but created another?**
**Genuine, unresolved gap.** The architecture currently evaluates events independently; a
rushed repair that fixes Bad Actor A but introduces a new failure mode in Component B isn't
captured anywhere. Not solved in Cycle 3 — flagged as a required Cycle 4 design item: any
intervention that produces a new, documented issue within an evaluation window should net
against the claimed value of the original event, and there is currently no mechanism for
this.

**What if the provider recommends excessive maintenance to protect KPIs?**
This is the sharpest operations-side critique and the biggest unmitigated incentive-design
risk in the whole architecture. A painshare-exposed provider has a direct incentive to
over-maintain (gold-plate PM schedules) purely to avoid Event 4 failure-attribution risk —
which itself costs the customer money (unnecessary spend and downtime) without ever
triggering an attribution dispute, because nothing looks wrong on paper. **Not solved in
Cycle 3.** Recommended mitigation for Cycle 4: (a) track total planned-maintenance
spend/hours per asset class as a standing context KPI, (b) give the customer a review/veto
right over maintenance-plan changes that increase spend beyond an agreed year-on-year
envelope, so the provider cannot unilaterally over-maintain its way to safety.

**What if the provider optimizes the KPI rather than the plant (Goodhart's Law)?**
Same root cause as above, generalized. Recommended mitigation: add a standing "KPI gaming
pattern review" to the Value Validation Board's remit (`VALUE_VALIDATION_BOARD_MVP.md`) —
not just event-by-event adjudication, but a periodic review of whether provider behavior
patterns show KPI-optimizing rather than plant-optimizing behavior. Not yet designed in
detail.

## Operations verdict
Two of the nine challenges (repair-creates-new-risk; over-maintenance/KPI-gaming) are
genuine, unresolved architecture gaps — not fixed in this cycle, only surfaced and logged.
See `RISK_REGISTER.md` and `gate2_assessment.md` for how these affect the Gate 2 verdict.
