# Value Validation Board — Minimum Viable Design (Cycle 3)

Minimum design only, sufficient to operate the attribution architecture in
`07_KPI_ATTRIBUTION/`. Full Asset Performance Office governance (RACI, escalation into wider
Joint Asset Performance Board structure) remains Gate 4 work, not attempted here.

**Non-negotiable principle:** the provider may submit a value claim. The provider may never
approve its own value claim. Every structural element below exists to guarantee this.

## Membership
- Customer Operations representative
- Customer Finance representative
- Provider Contract Director
- Provider Asset Performance Lead
- **Independent technical reviewer** (jointly agreed in advance — e.g. an independent
  reliability engineer or auditor), required for high-stakes/high-dispute-potential events
  (3, 4, 5, 6) per `event_stress_test.md`'s dispute-potential ratings; not required for
  low-stakes Events 1-2.

## Voting rights
Parity: 2 customer votes + 2 provider votes on every submission. The independent reviewer
votes only as a tie-breaker on a 2-2 split, and only for events requiring their presence.
**Structural guarantee:** provider votes alone (max 2 of 4-5) can never reach a majority —
at least one customer vote is always required to approve payment.

## Quorum
Minimum 1 customer + 1 provider representative present; for Events 3-6, the independent
reviewer must also be present or the vote is invalid.

## Required evidence
Per the specific data sources and evidence tier named in each event's attribution rule
(`event_stress_test.md`) and the tier required by payment type
(`COUNTERFACTUAL_PROTOCOL.md`). A submission missing named evidence is administratively
rejected before any vote occurs — evidence-completeness is a gate, not a voting factor.

## Submission process
Provider submits the claim with its full evidence package plus a **mandatory completeness
declaration** — an attestation that all qualifying events in that category during the period
were logged, not selectively chosen (this is the direct, if imperfect, mitigation for the
CFO's "selection bias" objection in `CUSTOMER_CFO_ATTACK.md`). Submission deadline: within an
agreed number of days of period close (number TBD — commercial decision).

## Cadence
| Event | Cadence | Rationale |
|---|---|---|
| 1 (contractor productivity), 2 (planned work conversion, KPI-fee only) | Monthly | Low stakes, cash-flow relevant, frequent review keeps disputes small |
| 3 (repeat failure avoided) | Quarterly | Needs the evaluation window to elapse before a claim is meaningful |
| 5 (TA scope reduction) | TA-cycle-triggered | Naturally event-driven, not calendar-driven |
| 6 (lifecycle Capex deferral) | Annual or Capex-cycle-triggered | Matches customer budget cycles |
| 4 (production loss / painshare) | Ad hoc, immediate | Cannot wait a quarter to classify a major event — initial classification within days, formal Board sign-off within an agreed window (e.g. 30 days) |

## Disagreement process
If a vote doesn't reach the required majority, the claim is tabled for one additional
evidence-gathering cycle only. If still unresolved, it **defaults to NO PAYMENT**
(consistent with the conservative default in `COUNTERFACTUAL_PROTOCOL.md`), not to
arbitration by default — arbitration is a further escalation option, not the automatic next
step.

## Escalation
Unresolved high-stakes disputes (Event 4 especially) escalate to the wider Joint Asset
Performance Board (named in the protocol's operating-model architecture, not yet designed —
Gate 4) or to a named independent expert-determination process, pre-agreed in the contract,
before any litigation. The specific independent expert/institution should be named in the
contract in advance, not selected reactively during a live dispute.

## Independent review trigger
Any single event above the materiality threshold (the same numeric threshold flagged as
undefined in `CONTRACT_LANGUAGE_RISK.md`, "material") automatically requires the independent
technical reviewer regardless of vote outcome — not just as a tie-breaker.

## Finance sign-off
Customer Finance and Provider Finance must both countersign any Board-approved claim before
payment — a second, separate control purely for financial governance (separation of duties),
independent of the Board vote itself.

## Payment approval
Payment occurs only after **both** (a) the Board vote passes under the parity rule above and
(b) dual Finance sign-off. No single-party approval path exists anywhere in this process —
this is the structural mechanism that makes "the provider may not approve its own claim" true
in practice, not just in principle.

## What is explicitly NOT designed here (Gate 4 scope)
Full RACI against the wider governance structure, the Joint Asset Performance Board's own
composition and remit, and the "KPI gaming pattern review" function flagged in
`07_KPI_ATTRIBUTION/OPERATIONS_ATTACK.md` as a needed addition to this Board's remit — logged
as a Cycle 4/Gate 4 item, not fabricated here.
