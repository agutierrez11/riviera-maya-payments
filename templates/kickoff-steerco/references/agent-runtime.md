# Agent runtime brief — Write a Kickoff and SteerCo Deck like a Bain Project Manager

## Core principle

SteerCo time is the most expensive client time on the engagement. Every slide that isn't a decision-driver is cut.

## Context the agent must establish before generating

> Before producing the deck, the agent must know each item below.
> - If the user's prior messages already supply an item, use it; do NOT re-ask.
> - If an item can be reasonably inferred from the user's stated topic, infer it and state the assumption inline on slide 2.
> - Ask only what is missing AND cannot be inferred — one targeted question at a time, not a script.

1. **Engagement name + client + sponsor** — sponsor named individually (the CEO or named CXO who owns the engagement on the client side). Vague "client leadership" is rejected.
2. **Duration + cadence** — total weeks of engagement, SteerCo frequency (weekly, bi-weekly, monthly), Monthly Progress to whom (Audit Committee, Board, CEO).
3. **The 3-5 workstreams** — each must have a name, a workstream lead on the consultant side, a workstream lead on the client side, a one-sentence purpose. The agent rejects workstreams without bilateral leadership.
4. **Decision gates** — at minimum, week 4 (scope confirmation), week 8 (interim findings), week 12 (final readout). Larger engagements get more gates.
5. **Top 3 risks at start** — political, data-access, talent. Each goes on slide 09 with a mitigation owner.
6. **Deck mode for THIS instance** — Kickoff, SteerCo, or Monthly Progress? The agent swaps cover sheet, slide 02 framing, and slide 14 closeout accordingly.
7. *(optional)* **Last SteerCo's decisions** — for SteerCo / Monthly mode, the agent puts the previous decisions + their status on slide 02 (Recap), so the meeting starts on continuity.

## Mandatory checks (during generation)

- ✅ Slide 03 (Gantt) has named owners on BOTH consultant and client side for every workstream. "TBD client" is flagged for the partner to escalate before the SteerCo.
- ✅ Slide 04 (RAG) uses literal red `#C9252D`, amber `#D9881E`, green `#2E7D34` color tokens (color-blind sensitivity: shapes / icons also encode the status, never color alone).
- ✅ Every red or amber item links to a slide later in the deck that addresses it. Reds with no follow-up slide are flagged.
- ✅ Slide 13 (Decisions Required) lists exactly 1-3 decisions, each phrased as a binary "Approve / Modify / Defer". Decks with 0 decisions are flagged ("then why is this SteerCo happening?").
- ✅ Every milestone date is a real date with a year. "End of Q2" is rewritten to "30 June 2026".
- ✅ Workstream slides (slides 05-08) follow identical layout: workstream name, week 0-12 mini-Gantt, key activities this period, blockers, decisions needed. Consistent layout across workstreams trains the room to read quickly.
- ✅ Cover slide shows the deck mode prominently: "KICKOFF — DAY 1" or "STEERCO #4 — WEEK 6" or "MONTHLY PROGRESS — MONTH 2". The mode is also encoded in the slide footer.
- ✅ Kickoff mode (Day 1) includes a "How we will work together" slide (operating model: meeting cadences, decision rights, escalation path). SteerCo / Monthly modes omit it.

## Template selection

- **Kickoff — Day 1** (default sub-template, bundled): white background, navy `#1F2A44` chrome, RAG color tokens. Slide 02 = "Why this engagement exists"; slide 14 = "What we will have produced by week 12".
- **SteerCo — Bi-weekly** (sub-template, bundled): same body slides; slide 02 = "Recap of last SteerCo + status of decisions"; slide 14 = "Decisions log + next SteerCo date".
- **Monthly Progress** (sub-template, bundled): same body slides + a stronger written narrative on slide 12 (Findings to date); slide 14 = "Forecast next 4 weeks + escalations".

## Use the bundled deck as a starting point

The included `deck/kickoff-steerco.slides/` is a complete, ready-to-use reference deck on **a 12-week post-merger integration engagement, sponsor = CFO** — chosen because it stress-tests every slot (four workstreams with bilateral leads, an Audit Committee monthly cadence, an active data-access risk, and a Day-30 scope-revision gate). The agent should copy this deck into the new project and replace slide-by-slide content, preserving:

- The 14-slot order (Gantt at slide 03, RAG at slide 04, Decisions at slide 13 are normative)
- Color tokens: navy `#1F2A44`, RAG red `#C9252D` / amber `#D9881E` / green `#2E7D34`, slate `#5A6271`, white background
- Typography: Source Serif 4 for headings, Inter for body, IBM Plex Mono for week numbers, dates, owner initials
- Three cover/header variants for Kickoff vs. SteerCo vs. Monthly

## Recommended 14-slide structure

| # | Page | Purpose | Required? |
|---:|---|---|:---:|
| 1 | Cover | Mode (Kickoff / SteerCo #N / Monthly) + week + sponsor | yes |
| 2 | Recap / Why | Mode-dependent: Why this engagement (Kickoff) OR last SteerCo recap | yes |
| 3 | 12-Week Workplan (Gantt) | Workstreams × owners × milestones × gates | **yes** |
| 4 | RAG Dashboard | Workstream status with reasons | **yes** |
| 5 | Workstream 1 | Mini-Gantt + activities + blockers | yes |
| 6 | Workstream 2 | Mini-Gantt + activities + blockers | yes |
| 7 | Workstream 3 | Mini-Gantt + activities + blockers | yes |
| 8 | Workstream 4 | Mini-Gantt + activities + blockers | yes |
| 9 | Risks & Issues (RAID) | Top 3-5 risks, owners, mitigations | yes |
| 10 | Dependencies | Cross-workstream, client-side, vendor-side | yes |
| 11 | Stakeholder Map | Power × Position grid; engagement plan | optional (Kickoff only) |
| 12 | Findings / Value Tracking | Mode-dependent: scope (Kickoff) OR findings + $-tracking | yes |
| 13 | Decisions Required Today | 1-3 binary asks with recommendations | **yes** |
| 14 | Decisions Log + Next Meeting | Cumulative decisions; next SteerCo date | yes |
