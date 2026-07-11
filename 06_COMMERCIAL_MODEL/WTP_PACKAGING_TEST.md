# Willingness-to-Pay Packaging Test — Cycle 9

Attacking the assumption that the Control Tower can be Base-Fee funded as currently
conceived. Five packaging alternatives assessed. **No winner selected — this requires
external evidence, not internal preference.**

## A. Standalone Control Tower fee (separate, visible line item)
- **Customer procurement logic:** requires the customer to create or approve a genuinely new
  budget category — the hardest procurement path of the five.
- **Budget owner:** unclear/contested — could be Operations, a new digital/transformation
  budget, or Procurement itself.
- **Revenue quality:** potentially high — clean, visible, defensible pricing, *if* it
  survives procurement scrutiny.
- **Margin logic:** cleanest attribution of margin to the orchestration capability
  specifically.
- **Risk:** highest go/no-go risk of the five — easiest for a skeptical CFO to simply refuse
  to create the line item at all.
- **Scalability:** good once one customer accepts the model — repeatable pricing logic.
- **Likely objection:** "We don't pay separately for coordination — that's what we already
  assume a competent contractor does as part of the job."

## B. Embedded premium in the integrated maintenance contract (blended fee)
- **Customer procurement logic:** easiest — fits existing procurement categories, no new
  approval needed.
- **Budget owner:** existing maintenance/Opex budget.
- **Revenue quality:** weaker — orchestration value is invisible, hard to defend or grow
  independently, easily commoditized in the next competitive RFP.
- **Margin logic:** blended, harder to track the orchestration margin specifically —
  undermines the "Control Tower is a distinct capability" narrative internally, not just
  externally.
- **Risk:** lower sales risk, higher strategic-erosion risk — looks like ordinary Full
  Service pricing to everyone, inside and outside the deal.
- **Scalability:** easy to scale commercially, but doesn't build the differentiated
  positioning the whole thesis depends on.
- **Likely objection:** minimal — but this is precisely the failure mode
  `DIFFERENTIATION_FALSIFICATION.md` tests: "just good contract management," not a business
  model.

## C. Transformation fee (Years 1-2) followed by a reduced recurring fee
- **Customer procurement logic:** familiar — resembles a consulting/implementation
  engagement customers already budget for.
- **Budget owner:** transformation/project budget initially, folding into steady-state Opex
  later.
- **Revenue quality:** front-loaded, tapering — consistent with (not fighting) Cycle 8's own
  finding that improvement-linked value naturally tapers.
- **Margin logic:** highest margin in transformation years, compressed in steady state — the
  provider must plan for this arc explicitly, echoing the savings-pool-exhaustion lesson
  applied to the whole Control Tower fee, not just Event 1.
- **Risk:** moderate — customer may resist an enforced fee reduction later, or may question
  paying anything once the transformation is "done."
- **Scalability:** good — a well-understood commercial shape.
- **Likely objection:** "What exactly are we still paying for in Year 4 if the
  transformation is already complete?" — echoes the "what am I still paying €24m for" finding
  from Cycle 6's Red Team.

## D. Subscription / site fee (flat, recurring, independent of scope)
- **Customer procurement logic:** simple, predictable, resembles SaaS/platform commercial
  logic.
- **Budget owner:** could sit in a "digital/platform" budget rather than traditional
  maintenance Opex — an interesting reframe, entirely untested whether industrial customers
  have or want such a category.
- **Revenue quality:** very predictable for the provider.
- **Margin logic:** simple but disconnects fee from actual orchestration effort/value
  delivered — risk of appearing arbitrary.
- **Risk:** real category-mismatch risk — a flat "platform fee" for something operationally
  entangled and physical may feel wrong to industrial buyers used to cost-plus/fixed-scope
  logic.
- **Scalability:** excellent, if it works at all.
- **Likely objection:** "Why would we pay a fixed platform fee for something that's actually
  variable and operational, not software?"

## E. Provider-funded Control Tower, monetized only through value modules
- **Customer procurement logic:** easiest possible sale — customer pays nothing extra
  upfront for orchestration.
- **Budget owner:** N/A for the Control Tower itself.
- **Revenue quality:** worst of the five — entirely dependent on module activation and
  performance, extending exactly the "provider revenue concentration" risk Cycle 8 flagged
  for Event 1 alone to the *entire* business model.
- **Margin logic:** provider bears 100% of Control Tower delivery cost with no guaranteed
  recovery.
- **Risk:** highest financial risk of the five to the provider; directly requires the
  assumption Cycle 8 explicitly rejected (Event 1 must not be underwritten as guaranteed
  revenue) — Option E structurally requires exactly that assumption for the whole business.
- **Scalability:** attractive to sell, likely untenable to run at scale.
- **Likely objection:** none from the customer — the objection here is internal, from the
  provider's own CFO, and should surface directly in
  `18_INTERVIEW_QA/PROVIDER_EXECUTIVE_VALIDATION.md` Q2/Q5.

## Reading across the five
B and C are the most procurement-compatible. A is the cleanest test of genuine
differentiation but carries the highest go/no-go risk — it is also the packaging that most
directly tests Falsification Register #1. D is the most novel and least precedented. E is
very likely to fail the Provider Executive validation protocol before it ever reaches a
customer. **No selection is made here** — this is exactly what external validation must
resolve.
