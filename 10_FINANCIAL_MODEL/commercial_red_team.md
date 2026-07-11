# Commercial Red Team — Cycle 5

Ten commercial failure scenarios. Instruction followed: do not defend the architecture — try
to prove each model should not be sold.

## 1. Margin erosion (Model B)
If Base Fee (€16,000,000) was set without solid delivery-cost data — a real risk given this
entire exercise uses illustrative, not real, cost figures — and actual delivery cost runs
even 10-15% above assumption, Model B's provider margin could be thin-to-negative *before*
any gainshare is earned, forcing the provider to chase every possible Event 1/3 claim
aggressively just to reach breakeven. That pressure is exactly the incentive-distortion
risk `overmaintenance_control.md` was built to catch — but the control watches maintenance
*intensity*, not claims-pursuit *aggressiveness* on Events 1/3, which is a gap.
**Verdict: Model B should not be sold until real delivery-cost data validates the Base Fee
is sufficient standalone.**

## 2. Customer overpayment (Model C)
Model C's Control Tower Fee (€8,000,000) is priced as a pure orchestration fee, but nothing
in this architecture proves a customer can't get equivalent orchestration value from a
smaller, less formal management layer. If the Control Tower Fee is not clearly and
separately justified against what a customer would otherwise pay for coordination overhead
inside its own organization, this is simply a new fee with no proven customer counterfactual.
**Verdict: Model C should not be sold without a customer-facing "orchestration value"
business case distinct from delivery value — not built in this cycle.**

## 3. Working-capital stress (Model B/C)
Full deferred settlement on Event 3 (up to 6 months on €560,000-€620,000) compounds with
the 24-month clawback window: a provider could have *multiple years* of claims simultaneously
in a provisional, reversible state. If the provider is thinly capitalized (plausible for a
newer or smaller unit within a large services company), this creates genuine balance-sheet
strain that this architecture has not sized against real working-capital cost of capital.
**Verdict: not fundable without a working-capital cost model — flagged, not built, in
`06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`.**

## 4. Claims inflation (all models)
Nothing in the architecture prevents a provider from investing disproportionate effort into
maximizing the *evidence quality* of claims specifically to clear VVB scrutiny, independent
of whether the underlying intervention was actually a good use of resources. A well-resourced
claims function could out-argue a thinly-resourced customer VVB representative on borderline
cases over time, even with parity voting, simply through preparation asymmetry.
**Verdict: parity voting does not guarantee parity of expertise or resourcing — a real,
unaddressed risk in all three models.**

## 5. Claim fragmentation (all models) — Petri's explicit Red Team requirement
**Upside fragmentation:** could a provider split a large claim into several sub-€100,000
pieces to dodge scrutiny? No — this is self-defeating, since sub-threshold events are
**ineligible for payment entirely**, not just lighter review (`gate2_assessment.md`). This
gaming vector is structurally closed.
**Bundling risk (new finding, not previously addressed):** could a provider *bundle* several
small, unrelated improvements into one submission specifically to clear the materiality gate
in aggregate, when none individually qualifies? Current design has no rule against this.
**Required new rule (not yet formalized): bundled claims must share a common root
cause/intervention to count as one event for materiality purposes — arbitrary bundling of
unrelated small wins is prohibited.** Logged as a Cycle 6 gap.
**Damage-splitting risk (customer side, Petri's explicit concern):** could a customer inflate
netting deductions against a valid Event 3 gainshare claim by documenting multiple
loosely-connected "secondary issues" to erode the claim's net value? The causal-connection
requirement in `intervention_netting.md` should prevent this, **but without the mandatory
Causal Connection Map (Petri's Cycle 5 decision 4) actually built, this remains
case-by-case and contestable** — the very gap Petri flagged.
**Verdict: the upside fragmentation vector is closed; the bundling and damage-splitting
vectors are open until the bundling rule and the Causal Connection Map exist.**

## 6. Delayed settlement (Models B/C)
A customer facing budget pressure could have a structural incentive to slow-walk Value
Validation Board scheduling or evidence requests specifically to push a claim's true-up past
a fiscal year-end, deferring cash cost recognition. Nothing in the architecture obligates a
minimum adjudication pace from the customer side — only the provider's submission deadline is
specified.
**Verdict: needs a customer-side adjudication SLA, symmetric to the provider's submission
SLA — not currently designed.**

## 7. Annual-cap gaming (Model C especially)
Because Model C's caps are set against the small Control Tower Fee (€8,000,000) rather than
total contract value, a provider under Model C has a much *lower* absolute ceiling to protect
than under Model A/B — which could perversely discourage genuine value-creation effort once
the (low) annual gainshare cap is reached early in a year, since further Event 1/3 wins
beyond the cap earn nothing. **Verdict: Model C's smaller cap base creates a real "why bother
after the cap is hit" disincentive in a strong year — the model as configured should not be
sold on a "high-powered incentive" pitch, because its incentive ceiling is the lowest of the
three in absolute terms.**

## 8. Contract-year timing manipulation (all models, especially around TAs)
Since Events 5/9 only activate in TA years (every 4-6 years) and carry meaningfully large
values relative to a Normal Year, either party has an incentive to negotiate TA timing
(accelerate or delay by months) to land favorably relative to contract renewal dates,
annual-cap resets, or the "no cross-year carry-forward" rule — e.g. a provider might push to
have TA completion (and its gainshare) land just after a new contract year opens, maximizing
the annual cap headroom available to absorb it. **Verdict: TA timing versus contract-year
boundaries is a real, unaddressed gaming surface across all three models.**

## 9. Low-value contract years (Model A specifically)
In a year where genuinely little addressable value exists (a mature, already-optimized site),
Model A's provider revenue is barely affected (96.9% fixed), but the customer is paying a
large fixed fee for a period of comparatively low incremental value creation, with the
"selective pursuit" logic potentially masking whether that's because little value exists or
because the provider chose not to look hard. **Verdict: Model A is the model most exposed to
a customer eventually asking "what exactly am I still paying €24m for" in a mature,
low-opportunity contract phase — a real long-term customer-retention risk, not just a Year-1
concern.**

## 10. Customer refusing valid high-value claims
The Value Validation Board's parity-voting structure means a customer can, in principle,
block a legitimate, well-evidenced claim indefinitely by simply refusing to vote yes, forcing
escalation. The disagreement process (`VALUE_VALIDATION_BOARD_MVP.md`) allows one additional
evidence cycle before defaulting to **no payment** — which is deliberately conservative, but
it also means a customer acting in bad faith is structurally advantaged: the default outcome
of an unresolved dispute favors the customer (no payment), not the provider, regardless of
claim quality. **Verdict: the conservative default that protects against weak claims equally
protects against a customer refusing strong ones — this asymmetry favors the customer
structurally and should be disclosed to the provider explicitly, not left as an implicit
"fairness" claim.**

## Summary
None of the ten findings are individually fatal, but 3 (fragmentation/damage-splitting,
annual-cap gaming in Model C, and the parity-voting default asymmetry) are structural, not
cosmetic, and should shape the Gate 3 verdict rather than being filed as footnotes.
