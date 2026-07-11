# Control Tower Cost Red Team — Cycle 11

| # | Attack | Finding |
|---|---|---|
| 1 | Have we simply renamed existing management? | **Partially yes, and explicitly acknowledged** — Site Manager, Work Management Lead, most of Reliability Lead and Commercial Controller are Category A (`WORK_CLASSIFICATION.md`). The zero-based design was built specifically to catch this and mostly succeeds, but the risk of relabeling persists if organizational discipline isn't maintained in real delivery — this is an execution risk, not a solved problem. |
| 2 | Have we double counted customer-transferred work as provider cost? | Real risk if not tracked carefully — claiming a role as both "AMOR incremental cost" and separately as "value delivered via customer headcount reduction" would be double counting. `INCREMENTAL_COST_BRIDGE.md` and `CUSTOMER_DUPLICATION_TEST.md` are designed to prevent this, but only if applied with discipline. |
| 3 | Are shared resources genuinely shareable? | Only with multiple accounts and staggered, non-conflicting peak demand. At 1-2 accounts, "shared" resources are dedicated resources with an optimistic label — a real, current-state problem given no portfolio exists yet. |
| 4 | Does centralization reduce site credibility? | Yes — confirmed directly in `CONTROL_TOWER_OPERATING_MODELS.md`'s comparison (Model C rated lowest on customer credibility), and in direct tension with Falsification Register #3/#4. |
| 5 | Does every customer demand customization? | Plausible, and if so it erodes `PLATFORM_REUSE_TEST.md`'s "highly reusable" findings for the structural/template layer — even reusable templates can get heavily customized in practice. |
| 6 | Does governance create meeting bureaucracy? | Real risk, consistent with Cycle 6's bureaucracy-break-even findings — requires the same discipline (fast-track claims tier, lean cadence) already proposed there. |
| 7 | Does Event 4 require expensive evidence administration? | Bounded by design — Event 4 should be rare in a well-run contract (Cycle 8's own framing). If it is *not* rare, that itself signals a bigger delivery problem, not just an administrative cost problem. |
| 8 | Does the customer retain a shadow organization? | **This is the central, unresolved risk of `CUSTOMER_DUPLICATION_TEST.md`** — a live, real possibility that would gut the system-economics case even if the provider's own numbers still look acceptable in isolation. |
| 9 | Does the first customer carry platform development cost? | **Yes, explicitly confirmed** by `CONTROL_TOWER_SCALE_CURVE.md` and quantified in `CONTROL_TOWER_UNIT_ECONOMICS.md` — the single-pilot cost (~7-8% of revenue) is roughly double the portfolio-amortized cost (~3.5%). |
| 10 | Are we assuming automation before data quality exists? | Explicitly guarded against — `CONTROL_TOWER_AUTOMATION_TEST.md` gates every use case on data dependency and rejects speculative automation savings. The underlying data-fragmentation problem itself remains real and unresolved. |

## Overall verdict
Two findings are decisive and should shape everything downstream: **the model only avoids
becoming pure additive overhead if the customer genuinely reduces its own duplicate
coordination work** (item 8), and **the first real deal will look meaningfully worse than
the model's steady-state economics, for real and unavoidable reasons, not execution
failure** (item 9). Neither is fatal. Both must be disclosed up front, not discovered during
the first pilot's business case review.
