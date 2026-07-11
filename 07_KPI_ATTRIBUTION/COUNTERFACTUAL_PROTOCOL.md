# Counterfactual Protocol — Cycle 3

For every avoided-loss event (3, 5, 6), the underlying question is unfalsifiable in the
strict sense: **what would have happened without the intervention?** This protocol does not
solve that problem — no protocol can — it bounds how much weight different qualities of
evidence are allowed to carry, and defaults conservatively when evidence is weak.

## Evidence hierarchy

| Level | Evidence | Description |
|---|---|---|
| 1 | Actual prior repeat event | The specific asset itself failed this way before — documented, dated, same failure mode |
| 2 | Documented failure mode with historical occurrence | Similar assets/fleet-level history shows this failure mode occurring, even if not yet on this exact asset |
| 3 | OEM / engineering evidence | Manufacturer data or recognized engineering standards support the failure risk |
| 4 | Probabilistic engineering model | Reliability modelling (e.g. Weibull analysis) estimates failure probability |
| 5 | Expert judgment | Professional opinion unsupported by the above — the weakest tier |

## Eligibility by payment type

| Use | Levels eligible |
|---|---|
| **Reporting** (context/management KPI, no payment) | All levels (1-5) — always fine to report and discuss for continuous improvement, regardless of evidence strength |
| **KPI Fee** (Phase 2-3, lower stakes) | Levels 1-3. Level 4 eligible only with joint sign-off on the model's validity *in advance* of using it. Level 5 never eligible for any payment. |
| **Gainshare** (Phase 4 — Events 3, 5, 6) | **Levels 1-2 only.** Level 3 eligible only as corroborating evidence alongside Level 1 or 2 — never standalone. Levels 4-5 are never sufficient alone for gainshare, regardless of how sophisticated the model. |
| **Painshare** (Event 4) | Applies differently — Event 4 is adjudicated via the decision tree in `event_stress_test.md`, not this hierarchy, for the primary attribution question. Where a counterfactual defense arises within Event 4 (e.g. customer argues "it would have failed anyway regardless of the maintenance lapse"), the same Level 1-2 standard applies, and **the burden of proof sits with whichever party is claiming the payment** — the customer for painshare, the provider for gainshare. This symmetry principle directly answers the Provider CFO's fairness question in `06_COMMERCIAL_MODEL/PROVIDER_RISK_CORRIDOR.md`. |

## Conservative default
**Absent sufficient evidence tier for the payment type in question, the event defaults to NO
PAYMENT.** Not to the provider's favor, not to the customer's favor — the conservative,
dispute-minimizing default is that money does not move without meeting the evidence bar. This
is deliberately stricter than most commercial gainshare programs and is a direct response to
Petri's instruction to "be highly conservative."

## Applied to the six events
- **Event 3 (repeat failure avoided):** requires Level 1-2 evidence — directly reflected in
  the attribution rule's condition (a), the ≥3-prior-failures baseline threshold.
- **Event 5 (TA scope reduction):** requires Level 1-2 evidence (condition-monitoring/
  inspection data on the specific equipment) — Level 3 (generic OEM guidance) alone is
  insufficient to justify a scope-removal gainshare claim.
- **Event 6 (lifecycle Capex deferral):** requires Level 1-2 evidence — and even then remains
  the weakest event in the set due to the separate baseline-setting conflict-of-interest
  problem identified in `event_stress_test.md`. This protocol alone does not rescue Event 6;
  see that document's recommendation to REMOVE it from the near-term commercial model.
