# Gate 3 Commercial Viability — Checker Verification and Formal Verdict (Cycle 5)

## Checker verification

Independently re-derived the key totals in `model_A_base_fee_kpi_fee.md`,
`model_B_atomic_value_share.md`, `model_C_control_tower_value_modules.md`.

**Arithmetic:** Model A €24,758,000; Model B €17,340,000; Model C €23,680,000 — all
re-verified by summing each line item independently; consistent.

**Checker catch (disclosed, not smoothed over):** the Maker's first pass at Model B applied
the 40/60 gainshare split *inconsistently* — an early draft summed Events 1 and 3 at their
**full** value (€1,400,000 + €1,550,000 = €2,950,000 variable comp, implying total revenue
€19,110,000) before the split assumption was applied uniformly. Checker re-derivation applied
the 40% provider share consistently across Events 1, 3, 5, 9 in all three models, correcting
Model B's Normal Year provider revenue down to **€17,340,000**. This matters: it is also what
produced the cycle's most important finding — that Model B does not out-earn Model A even in
a high-value year at these illustrative settings. **Flagging this catch explicitly because it
changed a substantive conclusion, not just a number.**

**Cap logic:** verified per-event caps (50% of applicable annual cap) bind before annual caps
in single-large-event scenarios (Stress Scenario 4), and annual caps bind independently in
multi-small-event scenarios (Stress Scenario 5) — both mechanisms checked arithmetically and
confirmed to interact as designed, not merely as asserted.

**Event/payment mapping:** cross-checked against `payment_eligibility_logic.md` — no event
or engine monetizes an aggregate metric in any of the three models; confirmed structurally
intact through Cycle 5.

**Cash-flow timing:** verified the three settlement options' working-capital figures are
proportionate to each model's Event 3 share (Model A ~€248,000 base; Models B/C ~€620,000
base) — consistent with each model's own P&L.

**Customer retained-value calculations:** re-derived independently — confirmed Models B and C
produce identical customer retained value (€1,770,000) for the activated events, as expected
since both use the same 40/60 split and same events; Model A's range (€1,422,000-€2,352,000)
correctly reflects the "selective pursuit" ambiguity about whether unpursued value still gets
delivered.

## Gate 3 verdict: **PASS WITH CONDITIONS**

The atomic value-event architecture produces three internally consistent, arithmetically
sound, CFO-testable commercial models. It survives 7 of 10 commercial Red Team attacks
outright and exposes 3 structural (not cosmetic) gaps. It is not fully contract-ready.

## Top 5 remaining commercial design gaps

1. **Catastrophic/multi-event Event 4 under-compensation.** The per-event and annual
   painshare caps can leave a customer with real, documented, undisputed loss materially
   under-compensated (as low as 26.7% recovery in the single-catastrophic-event scenario).
   This is the sharpest unresolved customer-CFO objection from this entire cycle.
2. **Claim bundling and damage-splitting are open gaming vectors** — the Causal Connection
   Map (Petri's decision 4) is not yet built, and no rule yet prevents bundling unrelated
   small wins to clear the materiality gate.
3. **Model B's risk/reward asymmetry is unresolved** — real painshare exposure without
   proportionate upside at the illustrative 40% split and €16,000,000 Base Fee.
4. **Model C's cap base (Control Tower Fee only vs. total contract value) is undecided** —
   materially changes both the "annual-cap gaming" disincentive risk and the model's
   competitiveness as a genuinely high-powered-incentive offer.
5. **No customer-side adjudication SLA exists**, creating a structural asymmetry where a
   customer can slow-walk or refuse a valid claim with the conservative default (no payment)
   working in their favor.

## What Gate 3 did NOT do (deliberately, per Petri's constraints)
No total OEE/availability/absolute-cost aggregate was monetized anywhere. Event 6 was not
repaired into gainshare — its value stays in the advisory/transformation engine. No market
benchmark percentages or real customer data were invented — every figure in
`10_FINANCIAL_MODEL/` is explicitly labeled illustrative. No deck was built.
