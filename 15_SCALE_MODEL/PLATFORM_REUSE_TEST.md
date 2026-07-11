# Platform Reuse Test — Cycle 11

Attacking the word "platform." A platform exists only if capabilities can genuinely be
reused, not merely reapplied with heavy customization.

| Capability | Classification | Reasoning |
|---|---|---|
| Loss-event taxonomy (Event 4's decision-tree structure, materiality gates) | **HIGHLY REUSABLE** | The decision-tree structure and exclusion logic are customer-agnostic; only specific SLA numbers/thresholds are customer-specific |
| Customer-dependency taxonomy (permit timing, production access, approved vendor lists as categories) | **HIGHLY REUSABLE** as a category list | The actual dependency values (which vendors, what SLA) are configurable per customer |
| Accountability boundary templates (Delivery/Orchestration/Performance/Asset-Owner/Statutory/Production) | **HIGHLY REUSABLE** | Close to a universal industrial-services legal/commercial framework — plausibly the single most reusable artifact this project has built |
| Governance templates (VVB structure, parity voting, escalation) | **HIGHLY REUSABLE** structurally | Configurable on cadence and materiality thresholds only |
| KPI architecture (the Pyramid, context/management/contract/payment classification) | **HIGHLY REUSABLE** | Structure is customer-agnostic |
| Risk corridor design (deadband/cap/collar/clawback) | **CONFIGURABLE** | Structure is reusable; the actual percentages are customer/deal-specific, as this project has treated them throughout (illustrative-only) |
| Performance analytics (dashboards, reporting logic) | **CONFIGURABLE** | Depends heavily on each customer's own data systems' quality and format |
| Contractor benchmarking (rate-card comparisons) | **CUSTOMER-SPECIFIC today; potentially the real network-effect candidate later** | Not reusable with zero portfolio — becomes more reusable only as cross-site data accumulates, which requires multiple customers and time neither of which exist yet |
| Work management standards (planning/scheduling discipline) | **CONFIGURABLE, bordering table stakes** | General industry good practice already exists; not unique AMOR IP |
| Reliability methods (RCA/FMEA templates) | **CONFIGURABLE** | Standard industrial reliability methodology; this project's documentation rigor may exceed typical practice, but the methods themselves are not proprietary |
| Data models (CMMS/ERP/contractor-data mapping into the attribution architecture) | **NON-REUSABLE in practice** | Every customer's underlying systems differ; the integration/mapping work is likely bespoke each time, even where the target data model (what fields are needed) is reusable in concept |

## Verdict

Most of the *capability* layer — taxonomy, accountability boundary, governance, KPI
architecture, risk corridor structure — is genuinely **HIGHLY REUSABLE or CONFIGURABLE**.
This is real, legitimate reusable process and governance IP, not nothing.

But the two things that would make this an actual *operating platform* — contractor
benchmarking data and data-model integration — are **not reusable today**. One requires
portfolio scale that doesn't exist; the other is inherently bespoke to each customer's IT
landscape.

**Conclusion: this is closer to a CONFIGURABLE OPERATING MODEL than a REAL PLATFORM at this
stage.** Calling it a full "platform" today would overstate what has actually been built.
"Configurable operating model" is the honest, defensible label — real, valuable, reusable
process IP, not yet plug-and-play technical reuse.
