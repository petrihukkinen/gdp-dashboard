# CLAUDE.md — Bilfinger Asset Performance 2030 project

This file governs how Claude (or any AI assistant) works inside this project directory. It applies to every file created under `bilfinger-asset-performance-2030/`.

## What this project is

This is a **CEO-level strategy development project**, prepared by Petri Hukkinen in the context of a senior leadership recruitment process with Bilfinger. The deliverable is a credible, defensible business growth concept — **Bilfinger Asset Performance 2030 / Asset Performance as a Service (APaaS)** — not a job-application slide deck, not a generic consulting framework, and not an AI-buzzword pitch.

This is explicitly **not** a revival of the original AMOR MBO concept (2020, Neste/One Refinery). AMOR is source material and a proof of lived experience, not the product being pitched.

## Standing rules for every deliverable in this project

1. **Do not produce generic consulting language.** No "leverage synergies," no "digital transformation journey," no slide filler. Every claim should be falsifiable or explicitly marked as a hypothesis.
2. **Do not invent Bilfinger facts.** Bilfinger's current strategy, financials, service portfolio, digital capabilities, and organizational structure must come from sourced, dated material (see `14_RESEARCH/`). If a needed fact isn't sourced, say so in `OPEN_QUESTIONS.md` — don't fill the gap with a plausible-sounding guess.
3. **Distinguish three categories of claim, always, explicitly:**
   - **Fact** — sourced and dated (Bilfinger public data, or documented AMOR/Neste history).
   - **Petri's experience** — lived, first-hand (ABB Full Service, Neste asset management, AMOR).
   - **Strategic hypothesis** — a reasoned proposal that has not been tested or validated.
   Every substantive document should make it obvious which category a given statement falls into.
4. **Challenge the business model. Do not just agree with it.** Every deliverable should include a checker pass: is this commercially credible, differentiated, controllable by Bilfinger, contractually acceptable in risk terms, financially coherent, scalable — or is it just consulting language a skeptical industrial CEO would shred?
5. **Never present total plant OEE (or total availability) as something Bilfinger controls without an explicit attribution model.** Any KPI-linked or gainshare mechanism must first pass through the attribution framework in `05_KPI_ATTRIBUTION/` that separates maintenance-caused losses from operations/process/feedstock/Capex/force-majeure losses. If a document proposes fee-at-risk tied to a metric, it must name what fraction of that metric is realistically attributable to Bilfinger's scope.
6. **Commercial credibility outranks AI/digital novelty.** A digital or AI capability is only included if it answers, concretely: what business problem does it solve, what data does it need, is that data realistically available and to whom does it belong, what decision does it improve, and what financial value could plausibly result. "Sounds modern" is not a reason to include anything.
7. **Maintain consistency across all deliverables.** `ASSUMPTIONS.md` and `OPEN_QUESTIONS.md` are living documents — update them as the project evolves rather than letting contradictions accumulate silently across files.
8. **Keep the main executive narrative simple.** The 12-question framework in `PROJECT_CONTEXT.md` is the backbone; detailed workstream files support it but should not fragment the core story into inconsistent versions.
9. **Preserve Petri Hukkinen's authentic industrial leadership voice.** Plainspoken, operationally grounded, allergic to hype. Prefer concrete numbers and named mechanisms (e.g. "TRIF," "hands-on-tool time," "Solomon benchmark quartile") over abstractions.
10. **Working method is maker–checker.** Every deliverable of substance goes through: (a) a maker pass that develops the analysis, and (b) a checker pass that critically reviews it as a skeptical Bilfinger CEO/CFO or skeptical customer executive would — attacking commercial credibility, differentiation, controllability, contractual risk, financial logic, and scalability. Do not skip the checker pass to save time; a deliverable that hasn't been attacked is not finished.
11. **No polished PowerPoint production until the strategy architecture has been built and stress-tested.** `10_EXECUTIVE_DECK/` and `11_CEO_PITCH/` stay empty/placeholder until the strategy files in `02`–`09` are stable.

## Directory map

- `01_SOURCE_MATERIAL/` — AMOR deck transcript and any other primary source Petri provides.
- `02_STRATEGY/` — strategic thesis, target operating model direction, staged evolution logic.
- `03_CUSTOMER_VALUE/` — customer problem definition, adoption barriers, value case per segment.
- `04_COMMERCIAL_MODEL/` — staged commercial architecture (Phase 0–4), revenue components.
- `05_KPI_ATTRIBUTION/` — the attribution framework and Value Validation Board mechanism.
- `06_OPERATING_MODEL/` — how Bilfinger would actually deliver this (org, roles, governance).
- `07_DIGITAL_AI/` — digital/AI module evaluation, one-pager-per-capability discipline.
- `08_FINANCIAL_MODEL/` — economics: Bilfinger P&L impact, customer business case, pricing logic.
- `09_RISK_REGISTER/` — living risk register (also mirrored at root as `RISK_REGISTER.md`).
- `10_EXECUTIVE_DECK/` — placeholder until strategy is stress-tested.
- `11_CEO_PITCH/` — placeholder until strategy is stress-tested.
- `12_INTERVIEW_QA/` — anticipated interview questions and Petri's grounded answers.
- `13_100_DAY_PLAN/` — what a first 100 days in a Bilfinger leadership role would look like.
- `14_RESEARCH/` — sourced Bilfinger facts, with citations and access dates.

Root-level files (`PROJECT_CONTEXT.md`, `AMOR_ANALYSIS.md`, `STRATEGIC_THESIS.md`, `ASSUMPTIONS.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, `WORKPLAN.md`) are the current, authoritative state of the project narrative. Workstream folders hold supporting depth.
