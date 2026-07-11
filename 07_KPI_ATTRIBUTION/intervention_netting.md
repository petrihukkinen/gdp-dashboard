# Intervention Netting Mechanism — Cycle 4

Closes Red Team gap B from Cycle 3. Design goal: an intervention that removes one failure
mode but creates, accelerates, or materially increases another must be evaluated on its
**net** outcome — the architecture never approves the successful half of an intervention in
isolation.

## Scope of what's monitored

Following an Event 3 (or Event 4-remediation) intervention, a **post-intervention
observation window** opens (illustrative default: 180 days — not specified by Petri, flagged
as needing confirmation, see `gate3_readiness_assessment.md`) during which the following are
monitored for new, documented failure modes:

- **Same asset** — the identical piece of equipment.
- **Same functional location** — per the CMMS functional-location hierarchy.
- **Causally-connected equipment** — equipment mechanically, thermally, or systemically
  linked such that a change in one could plausibly propagate to another (e.g. shared
  lubrication/cooling circuit, common control loop, mechanically coupled components).
  **Not yet resolved:** this requires a pre-agreed, jointly-built "causal connection map" per
  asset system — the architecture cannot invent this generically per asset. Absent a
  pre-built map, causal connection is assessed case-by-case via RCA judgment, which is
  weaker but functional. Logged as a remaining gap in `gate3_readiness_assessment.md`.

## What triggers netting

A **direct** failure mode (a different failure on the same component) or a **secondary**
failure mode (a new issue on causally-connected equipment) documented within the observation
window, reasonably linked via joint RCA to the original intervention.

## Net calculation

**Net Attributable Value = Original Claimed Value − Cost of New Failure Mode − Transferred
Maintenance Cost**, where:
- Original Claimed Value uses Event 3's existing avoided-cost methodology.
- Cost of New Failure Mode uses Event 4's methodology (production loss × the agreed
  contract-fixed standard margin, plus repair cost), regardless of whether the new failure
  mode independently clears the materiality threshold — netting applies at any size once a
  primary claim is already in play, though a *standalone* secondary issue below the
  materiality threshold is proposed to be logged as context only rather than triggering a
  full recalculation (**this is an extension of the materiality principle Petri didn't
  explicitly authorize — flagged as a required confirmation, not assumed silently**).
- Transferred Maintenance Cost captures any documented increase in ongoing maintenance
  burden elsewhere caused by the intervention (e.g. a fix that requires new recurring
  inspection on the connected equipment).

## Payment sequencing (the real trade-off)

**No gainshare payment is approved until either (a) the observation window closes with no
new documented failure mode, or (b) the Value Validation Board explicitly reviews and
accepts the residual risk** (including a partial net-value determination if a minor new
issue emerged). This is a deliberate delay to protect the customer, and it has a real cost:
it pushes Event 3's payment timing later than the cadence table in
`08_OPERATING_MODEL/VALUE_VALIDATION_BOARD_MVP.md` currently implies (quarterly submission,
but approval potentially delayed to the following quarter or later in the worst case). This
trade-off is disclosed here, not hidden, and should be reflected in the cadence table at the
next review of that document.

## Interaction with Event 4

If a production-loss event under review is itself a new/different failure mode on the same
asset, functional location, or causally-connected equipment within an open observation
window from a prior intervention, it is **routed to this netting mechanism instead of
standalone Event 4 adjudication** — see Step 0.5 of `event4_decision_tree_v3.md`. This
avoids running the same underlying dispute through two separate processes with potentially
inconsistent outcomes.

## If net value is negative
No payment is made. If a prior payment had already been advanced (only possible before this
mechanism existed, or if a later-discovered secondary failure mode surfaces after initial
approval), the 24-month clawback window applies (`06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`).

## Remaining gaps
1. Causal-connection map not yet built — a prerequisite for deterministic (rather than
   case-by-case judgment) netting.
2. Observation window length (180 days, illustrative) needs Petri/commercial confirmation.
3. The materiality carve-out for sub-threshold secondary issues is a proposed extension, not
   an authorized rule — requires confirmation.
