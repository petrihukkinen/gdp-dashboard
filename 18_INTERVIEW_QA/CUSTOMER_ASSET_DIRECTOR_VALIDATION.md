# Customer Asset/Maintenance/Site Director Validation Protocol — 30 Minutes

For Asset Director, Maintenance Director, or Site Director roles. Operational, not
commercial framing — but still a problem interview, not a pitch.

## Q1 — Actual pain of fragmented accountability
*"Describe the last time a contractor, an OEM, and your own maintenance team disagreed about
who was responsible for a delay or a failure. How was it resolved, and how long did it
take?"*
- **Testing:** whether fragmented accountability is real, operational, costly pain.
- **Positive:** real, costly friction, slow resolution.
- **Warning:** happens but resolves quickly through informal relationships.
- **Kill:** essentially never happens — accountability is already clear.

## Q2 — Willingness to cede orchestration authority
*"If an external party had the authority to select, direct, and reprioritize your
contractors and specialist providers day-to-day — not just advise, but actually decide —
how would your organization react?"*
- **Testing:** Falsification Register #3, operationally.
- **Positive:** openness, framed as relief rather than threat.
- **Warning:** conditional openness, wants veto rights retained.
- **Kill:** strong resistance — "we would never give up that control."

## Q3 — Control Tower decision-rights boundary
*"Which specific decisions would you never delegate to an external provider, no matter how
much you trusted them — approved vendor lists, Capex, work prioritization, something else?"*
- **Testing:** the real boundary of the decision-rights architecture.
- **Positive:** names a short, specific, negotiable list.
- **Warning:** names a long list that would gut the orchestration role.
- **Kill:** "everything" — no delegation acceptable at all.

## Q4 — Work-permit/customer-dependency reality
*"How often does work-permit timing or production-access scheduling actually delay planned
maintenance work at your site, and who usually owns fixing that?"*
- **Testing:** whether the customer-dependency exclusion logic (Event 4's SLA-driven
  exclusions, Event 1's access dependencies) is solving a real or imagined problem.
- **Positive:** frequent, well-understood, ownable friction.
- **Warning:** occasional, multi-causal.
- **Kill:** essentially never an issue — the dependency-exclusion architecture may be
  solving a non-problem.

## Q5 — Data transparency willingness
*"Would you be comfortable giving an external provider real-time or near-real-time access to
your CMMS, work-order, and contractor invoicing data?"*
- **Testing:** a hard precondition for the entire attribution architecture.
- **Positive:** yes, with reasonable controls.
- **Warning:** yes, but only with heavy restrictions/anonymization.
- **Kill:** no — data sharing at this level is off the table.

## Q6 — Internal organizational resistance
*"If your own maintenance or procurement team's role changed significantly under this model
— some work moving to the external provider — how would your organization respond
internally?"*
- **Testing:** real, human, political resistance risk.
- **Positive:** describes a plausible transition path, existing appetite for change.
- **Warning:** real but manageable resistance.
- **Kill:** fundamental, likely fatal internal political resistance (union, headcount
  protection, etc.).

## Q7 — Fear of provider lock-in
*"What would concern you most about depending heavily on one external provider for this
orchestration role over a 5-10 year contract?"*
- **Testing:** lock-in fear as a standalone blocker.
- **Positive:** names manageable, addressable concerns (exit terms, data portability).
- **Warning:** significant, harder-to-address concerns.
- **Kill:** lock-in fear alone would block signing regardless of value proposition.

## Q8 — KPI gaming risk / operational trust
*"What would make you trust that a provider recommending additional preventive maintenance
is doing it because it's genuinely needed, not because it protects the provider from a
performance penalty?"*
- **Testing:** whether the over-maintenance control concept (`overmaintenance_control.md`)
  would actually satisfy a real operations leader, not just an internal Red Team.
- **Positive:** names a specific, addressable form of evidence/governance that would satisfy
  them.
- **Warning:** skeptical, wants more than what's currently designed.
- **Kill:** no governance mechanism would fully resolve their distrust.

## Q9 — Operational credibility / precedent
*"Has an external maintenance or service provider ever successfully run something like this
orchestration role for you before, even informally? What worked and what didn't?"*
- **Testing:** operational credibility grounded in real precedent, not theory.
- **Positive:** describes a positive precedent.
- **Warning:** mixed precedent.
- **Kill:** describes a clearly negative precedent that colors this proposal.

## Q10 — Closing: core-only operational value
*"If this provider only delivered the base maintenance service and the accountability
guarantee — no contractor savings-sharing, no reliability rewards — would you still see real
operational value in it?"*
- **Testing:** Falsification Register #10, operationally.
- **Positive:** yes.
- **Warning:** conditional.
- **Kill:** no — without upside modules there's no operational case either.
