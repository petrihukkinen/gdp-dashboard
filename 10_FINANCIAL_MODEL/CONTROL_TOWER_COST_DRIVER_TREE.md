# Control Tower Cost Driver Tree — Cycle 11

Testing which variables plausibly explain Control Tower cost. **Revenue is explicitly
tested and rejected as the primary driver.**

| Candidate driver | Plausibility | Reasoning |
|---|---|---|
| **Number of contractors/parties orchestrated** | **Primary** | Directly drives Contractor Integration Lead workload — the one role the zero-based analysis found least reducible. Largely independent of total contract revenue. |
| **Data-system fragmentation/quality** | **Primary, underrated** | If CMMS/ERP/contractor-timekeeping systems are fragmented or poor quality, reconciliation cost rises sharply regardless of revenue or site size — an IT/data-quality problem, not a scope problem. Plausibly the single most underrated driver in prior cycles' thinking. |
| **Number of work orders** | Secondary | Drives Data Analyst/reporting workload; a more honest volume proxy than revenue. |
| **Number of performance events (materiality-gated)** | Secondary, and should be structurally low | Drives Value Validation Board workload directly — but the architecture (Cycles 6-8) was specifically designed to keep this few and high-value, not frequent. |
| **Turnaround intensity** | Conditional | Near-zero driver unless the optional Turnaround Module is active. |
| **Site complexity / asset count** | Secondary | Plausible driver of Contractor Integration Lead and Reliability Lead workload, but likely correlates with (not independent of) contractor count. |
| **Number of sites / geographic dispersion** | **Not a cost driver — a *shareability* driver** | Determines whether shared/central resources are even feasible (see `CONTROL_TOWER_SCALE_CURVE.md`), not how much any one site costs. |
| **Customer governance burden** | Secondary, negotiable | How formal/demanding the joint board process is — largely under contract-design control, not fixed. |
| **Regulatory complexity** | Weak/secondary | A likely multiplier on Reliability Lead and compliance-adjacent work, not a primary Control Tower cost driver — statutory accountability stays with the customer (`ACCOUNTABILITY_BOUNDARY.md`). |
| **Annual contract revenue** | **Rejected as primary driver** | A small-revenue site with a highly fragmented contractor base could require *more* orchestration work than a large-revenue, simple, few-contractor site. Revenue should not be the basis for pricing or sizing the Control Tower. |

## Ranking
1. Number of contractors orchestrated
2. Data-system fragmentation/quality
3. Number of work orders
4. Number of sites (shareability, not cost, driver)
5. Customer governance burden (negotiable)

Revenue and general site complexity are weak, potentially misleading proxies and should not
be used to size or price the Control Tower operating layer.
