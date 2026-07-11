# Side-by-Side Comparison and Risk Corridor Stress Test — Cycle 5

## Side-by-side comparison (Normal Year, illustrative)

| | Model A | Model B | Model C |
|---|---|---|---|
| Fixed fee(s) | €24,000,000 | €16,000,000 | €22,000,000 (€8m Control Tower + €14m Modules) |
| Variable comp (Normal Year) | €758,000 | €1,340,000 | €1,680,000 |
| **Total provider revenue** | **€24,758,000** | **€17,340,000** | **€23,680,000** |
| Variable comp as % of fixed fee | 3.2% | 8.4% | 7.6% |
| Annual gainshare cap | €4,800,000 | €3,200,000 | €1,600,000 |
| Annual painshare cap | €2,400,000 | €1,600,000 | €800,000 |
| Per-event painshare cap | €1,200,000 | €800,000 | €400,000 |
| Customer retained value (activated events) | €1,422,000-€2,352,000* | €1,770,000 | €1,770,000 |
| Budget predictability (fixed as % of total spend) | 96.9% | 92.3% | 92.9% |
| Claims bureaucracy load | Lowest (selective) | Highest (full ledger) | Medium (2 events only) |

*Range reflects whether the unpursued 60% of Event 3 value is credited to the customer under
the "equal delivery" assumption — see `model_A_base_fee_kpi_fee.md`.

**Headline finding:** none of the three models dominates the others in a Normal Year. Model A
earns the provider the most in absolute terms precisely because it takes the least
performance risk; Model B and C earn less for the provider in the base case but are designed
to close the gap (or overtake) in a high-value year — tested below.

## Risk corridor stress test (8 scenarios)

All scenarios modelled primarily against **Model B** (most exposed to variability) with A/C
deltas noted, since B isolates the corridor's behavior most clearly.

### 1. Low-value year
Assume Event 1/3 realization probability drops to 0.3 (vs. 0.75/0.6 Normal Year): Event 1
value ≈ €560,000 gross (÷ ~2.5), Event 3 ≈ €620,000 gross. Provider gainshare share falls to
roughly €470,000 total (vs. €1,180,000 Normal Year) — a **60% reduction in variable comp**.
Model B provider revenue falls to ~€16,470,000 (essentially Base-Fee-only). Model A's
smaller variable share means a proportionally smaller hit (~€300,000 lower than Normal Year).
**Finding:** Model B's provider revenue volatility in a low-value year is roughly 3x Model
A's in absolute terms relative to its own Base Fee.

### 2. Normal year
As modelled in each model file — the reference case.

### 3. High-value year
Assume Event 1/3 realization probability rises to 0.9 and a TA occurs (Events 5/9 activate).
Model B: Event 1 ≈ €680,000 gross → provider share €272,000 higher than Normal; Event 3 ≈
€1,860,000 gross (all 3 claims clean, no netting deduction) → provider share ~€744,000 (vs
€620,000); plus TA year Events 5+9 gross €700,000 → provider share €280,000. Total Model B
provider revenue in a high-value TA year ≈ €16,000,000 + €832,000 + €744,000 + €280,000 ≈
**€17,856,000 (still below Model A's flat €24,758,000)** — confirming the headline finding:
even a genuinely strong year does not let Model B catch Model A at this illustrative Base
Fee gap. **This is an important pricing-design finding for Cycle 6**, not a flaw in the
stress test — it suggests Model B's Base Fee may be set too low relative to Model A for the
two to be genuinely comparable positioning options, or that the gainshare split (40%) is too
conservative for a "ledger is the primary commercial engine" model. Flagged as a required
Petri/commercial decision.

### 4. One catastrophic Event 4
A single event with a documented, fully provider-attributable loss of €3,000,000 (real
economic loss, per Event 4's fixed-margin methodology). **The per-event cap (€800,000 in
Model B) binds before the annual cap (€1,600,000) does** — the customer recovers only
**€800,000, or 26.7% of the actual documented loss.** This is a sharp, real finding: the cap
structure that protects the provider from catastrophic exposure simultaneously leaves the
customer materially under-compensated for a genuinely large, undisputed, provider-caused
loss. **This is the single most important customer-CFO objection to carry into
`commercial_red_team.md` and `gate3_verdict.md`.**

### 5. Multiple small Event 4 events
Four events, each €500,000 fully attributable (€2,000,000 gross, all individually below the
per-event cap). The **annual cap (€1,600,000)** binds instead — the customer recovers
€1,600,000 of €2,000,000 documented loss (80%), better than the catastrophic-single-event
case but still short. **Finding:** the annual cap protects the provider cumulatively even
when no single event trips the per-event cap — a second, distinct way the customer can be
under-compensated relative to real attributable loss.

### 6. Event 3 claim delayed by 180-day netting
Already modelled in each model file's cash-flow section. **Finding common to all three
models:** full deferred settlement is immaterial for Model A (small absolute amounts) but
materially affects working capital for Models B and C (3.6-3.9% of Base Fee tied up for up
to 6 months) — provisional accrual with true-up is the practical necessity for B/C, optional
for A.

### 7. High MII / low RRE Red Flag year
Modelled at three band widths, per Petri's instruction to test ±10%/15%/20% and confirm the
model doesn't fail solely because the band changes:

| Band width | Illustrative Red Flag frequency (asset-periods flagged) | Revenue at risk (Model B, Events 1+3 suspended pending review) |
|---|---|---|
| ±10% (tightest) | ~30% of periods (illustrative) | Up to €1,180,000 delayed/suspended |
| ±15% (Cycle 4 default) | ~15% | Up to €590,000 delayed/suspended |
| ±20% (loosest) | ~7% | Up to €280,000 delayed/suspended |

**Finding: the architecture survives at all three band widths** — the maximum revenue at
risk even at the tightest band (€1,180,000) is bounded by the value of the suspended events
themselves, not the whole contract, and represents at most 6.8% of Model B's total Normal
Year revenue. This satisfies Petri's requirement that the commercial model "must not
materially fail solely because the MII band changes." The band width affects **how often**
claims are delayed for review, not the structural soundness of the corridor.

### 8. Customer dependency / SLA breach-heavy year
If permit/production-access SLA breaches are frequent (per Event 4 Step 4 /
`event4_decision_tree_v3.md`), **more candidate painshare events are excluded** (protects
the provider financially) but **fewer Event 2/3 claims clear cleanly** (Event 2's planned-
work-conversion numerator shrinks; Event 3's evaluation windows are more likely to be
contaminated by envelope breaches). Net effect: provider financial exposure falls, but so
does the provider's ability to earn KPI Fee/gainshare — a real, symmetric consequence worth
naming to a skeptical customer who might otherwise assume SLA breaches only help the
provider.

## Consolidated event-level view across models

| Event | Model A role | Model B role | Model C role |
|---|---|---|---|
| 1 — Contractor productivity | KPI-bonus mechanic (capped, small) | Full gainshare (40/60 split) | Full gainshare (40/60 split), one of two activated events |
| 2 — Planned work conversion | KPI Fee (unchanged across models) | KPI Fee (unchanged) | KPI Fee (unchanged) |
| 3 — Repeat failure avoided | Selective gainshare (40% pursued) | Full gainshare | Full gainshare, one of two activated events |
| 4 — Production loss | Painshare, tightest relative caps | Painshare, full exposure | Painshare, smallest absolute caps |
| 5 — TA scope reduction | Full when TA occurs | Full when TA occurs | Not activated in this configuration |
| 6 — Lifecycle Capex deferral | Excluded — Advisory Fee | Excluded — Advisory Fee | Excluded — Advisory Fee (most explicit separation) |
| 9 — TA Execution Efficiency | Full when TA occurs, benchmark permitting | Full when TA occurs, benchmark permitting | Not activated in this configuration |
