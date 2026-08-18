# Agent runtime brief — Write a New Product GTM Deck like a GTM Strategist at Bain

## Core principle

GTM strategy is the art of saying *no* to most of the addressable market for 12-18 months so the team can win one segment completely. Optimise for *concentration*, not coverage.

## Context the agent must establish before generating

> Before producing the deck, the agent must know each item below.
> - If the user's prior messages already supply an item, use it; do NOT re-ask.
> - If an item can be reasonably inferred from the user's stated topic, infer it and state the assumption inline on slide 2.
> - Ask only what is missing AND cannot be inferred — one targeted question at a time, not a script.

1. **Product + stage** — pre-launch / post-launch in beta / GA Q+0-Q+4. The deck's risk and learning loops adjust to stage.
2. **Candidate segments** — 4-6 buyer segments with company-size, vertical, role, and use-case dimensions. The agent will flag if the user names <4 (too narrow) or >8 (too unfocused).
3. **TAM estimate per segment** — addressable revenue size with methodology (top-down, bottom-up, or analogue). Vague "huge market" is rejected.
4. **Accessibility per segment** — how easy is it to find and reach buyers? Channel availability, sales-cycle length, decision-maker accessibility.
5. **Willingness-to-pay signals** — pilot revenue, LOIs, comparable-product pricing, customer-interview data.
6. **Founder's beach-head gut call** — which segment the founder believes is the first to win. The agent will pressure-test this against the scoring math.
7. *(optional)* **Competitive landscape per segment** — who else is targeting these buyers? Differentiation per segment.

## Mandatory checks (during generation)

- ✅ Slide 06 is the **Segmentation matrix** — 4-6 segments × 3 scoring axes (TAM, Accessibility, Willingness-to-pay). Decks without scoring math are flagged.
- ✅ Slide 09 is **Targeting** — picks ONE beach-head segment, explicitly defers the others. "We target three segments equally" is rewritten.
- ✅ Slide 12 is the **Positioning Statement** in canonical Kotler form. Multi-clause statements with `and` chains are rewritten.
- ✅ The deck includes **explicit phase-2 / phase-3 criteria** for moving beyond the beach-head — typically "100 paying customers in beach-head" or "% retention threshold".
- ✅ Pricing slide (slide 16) names the **packaging tier**, the **anchor price**, and the **discount discipline**. "TBD pricing" is rejected for a GTM-ready deck.
- ✅ The deck names the **5 first-100 customer acquisition channels** specifically. "Multi-channel demand generation" is rewritten.
- ✅ Risk slide (slide 20) names the three most likely reasons the GTM fails — wrong beach-head, weak positioning, missing channel-fit — and the experiments that test each.
- ✅ ROI scenario (slide 19) shows base / good / great cases for Year 1 with assumptions named.

## Template selection

- **Bain STP** (default, bundled): consulting-style, white + navy, dense tables. For board-ready GTM plans.
- **a16z Founder-GTM** (alternate): narrative-led, fewer tables, more customer-quotes; for founder-led GTM at Series A-B.
- **Enterprise B2B** (alternate): adds detailed ABM segmentation, account-tier breakdown, sales / marketing SLA. For enterprise sales motions.

## Use the bundled deck as a starting point

The included `deck/new-product-gtm.slides/` is a complete reference GTM plan for a hypothetical Series B SaaS company chosen because it cleanly demonstrates a 5-segment matrix and a deferred-segment phase plan. The agent should copy this deck and replace content while preserving the 22-slot playlist — slide 06 (Segmentation), slide 09 (Targeting), slide 12 (Positioning), and slide 16 (Pricing) are slot-locked.

## Recommended 22-slide structure

| # | Page | Purpose | Required? |
|---:|---|---|:---:|
| 1 | Cover | GTM plan title, date | yes |
| 2 | TL;DR — the one segment we pick | yes |
| 3 | Product summary | yes |
| 4 | Total Addressable Market | yes |
| 5 | Customer interviews / discovery summary | yes |
| 6 | Segmentation matrix | **yes** |
| 7-08 | Segment deep dives (top 2) | yes |
| 9 | Targeting — beach-head + deferral | **yes** |
| 10 | Phase-2 / Phase-3 triggers | **yes** |
| 11 | Buyer personas in the beach-head | yes |
| 12 | Positioning Statement (canonical) | **yes** |
| 13 | Messaging architecture | yes |
| 14 | First-100 customer acquisition channels | yes |
| 15 | Sales motion (PLG / founder-led / inside) | yes |
| 16 | Pricing + packaging | **yes** |
| 17 | Customer-success / activation model | yes |
| 18 | Team + hiring plan | yes |
| 19 | ROI scenarios (base / good / great) | yes |
| 20 | Risks + experiments | **yes** |
| 21 | 90-day execution plan | yes |
| 22 | Closing — beach-head restated | **yes** |
