# Correction Implementation Plan — Growth Engine Automation Audit Fixes

> Companion to `Growth-Engine-Automation-Audit.md`. Same batching convention your own `IMPLEMENTATION-PLAN.md` files already use, so this can be run the same way — one batch per work session, tracker updated at the end of each.

---

## How to use this plan

Each batch below has: **what's wrong**, **what "done" looks like**, **exact steps**, and **effort estimate**. Batches are ordered by leverage — highest-value/lowest-effort first. Do Batch 0 before anything else; it's free (no writing, just merging work you already paid for/did).

---

## Batch 0 — Emergency Fixes (no new content, ~1 hour)

**What's wrong:** Finished work is sitting unused; two tracker files claim things that aren't true on disk; one folder is dead weight.

### Tasks
- [ ] Unzip and merge `Marketing/M18 Growth Hacking Experiment Engine.zip` → overwrite the stub folder of the same name
- [ ] Unzip and merge `Marketing/M19 Community Building.zip` → overwrite the stub folder
- [ ] Unzip and merge `Marketing/M20 Partnerships, Co-Marketing and PR.zip` → overwrite the stub folder
- [ ] Spot-check each merged folder's `automation.md` is no longer the 8-line placeholder text (confirm real content landed)
- [ ] Delete the three `.zip` files once confirmed merged
- [ ] Correct `Marketing/MARKETING-IMPLEMENTATION-PLAN.md` §7 tracker: M18/M19/M20 rows should read "✅ Done (merged from delivered zip, corrected on [date])" — add a session-log line noting the discrepancy and fix, same convention as your existing log
- [ ] Correct `Sales Funnel/IMPLEMENTATION-PLAN.md` §5 tracker: Stages 47–50 are further along than "not started" — re-verify each of the 4 stages' actual file depth and update the batch row accordingly (do this before deciding whether Batch 4 below still needs to touch them)
- [ ] Decide + act on `Automation/` (empty top-level folder): either delete it, or repurpose it as the landing spot for exported `.json` n8n workflow files once Batch 1 starts producing them
- [ ] Delete the leftover `Export-8a3184bc-...-Part-1.zip` raw backup from the repo root once you've confirmed it's a duplicate of content already live elsewhere (it's a 5.4MB full Notion export snapshot — fine to keep elsewhere as a personal backup, just shouldn't sit inside the working repo)

**Done when:** Marketing shows 9/22 modules at real depth (up from 6/22) with zero new writing, and both tracker files match what's actually on disk.

---

## Batch 1 — n8n Template Linking Pass (~2–3 hours, highest ROI)

**What's wrong:** Only 4 specific n8n.io template links exist across the entire 76-stage system; the 14 concrete matches identified in the audit (§3.1) aren't in any stage file yet.

### Tasks
- [ ] Add a "Reference collection" line to `Sales Funnel/N8N-AUTOMATION-INDEX.md` §0, linking `nivyindia/all_n8n_templates_collection` as a second, curated template source alongside n8n.io's live library
- [ ] For each of the 14 stages below, add the named template as a real link inside that stage's own `automation.md` (not just the summary index) — one line each, in the same "n8n template(s)" format the index already uses:

| Stage | Template to add |
|---|---|
| Sales 06/08 — Lead Extraction/Enrichment | "Qualify new leads in Google Sheets via OpenAI's GPT-4" |
| Sales 13 — CRM Setup | "Chat with Postgresql Database" / "Generate SQL queries from schema only" |
| Sales 16 — Email Outreach | "LeadPilot Lite – AI Cold Email Writer" |
| Sales 19 — WhatsApp Outreach | Collection's WhatsApp category (Evolution API pattern) |
| Sales 25 — Reply Handling and Triage | "Auto-label incoming Gmail messages with AI nodes" / "InboxZero Lite" |
| Sales 33 — Proposal Creation | "Invoice data extraction with LlamaParse and OpenAI" (adapted pattern) |
| Sales 39 — Payment and Invoicing | "Airtable to Google Sheets Auto-Sync" + Stripe/Odoo webhook pattern |
| Sales 40 — Client Onboarding | "Streamline Client Onboarding with PDF, Trello, Slack, Gmail and Airtable" |
| Sales 46 — Support and Issue Resolution | "Customer Support Channel and Ticketing System with Slack and Linear" / "Sentiment Analysis Tracking" |
| Sales 51 — Customer Feedback and NPS | "Add positive feedback messages to a table in Notion" |
| Marketing M09/M10 — Content Production/Repurposing | "Automate Blog Creation in Brand Voice with AI" / "Write a WordPress post with AI" |
| Marketing M11 — LinkedIn Organic Engine | "AI-Powered Social Media Amplifier" |
| Marketing M17 — Email Newsletter | "Daily Email Notification" (Ollama digest pattern) |
| Marketing M20 — Partnerships/PR | "Automate Competitor Research with Exa.ai, Notion and AI Agents" |

- [ ] For each link added, actually open the template in n8n.io/GitHub once to confirm it still resolves (templates get renamed/removed — the index itself already warns about this) — note "verified [date]" next to each

**Done when:** 14 stages have a real, checked, clickable template link in their own `automation.md`, not just a category search suggestion.

---

## Batch 2 — OSS Tool Table Correction (~1 session for Sales, ~1 session for Marketing)

**What's wrong:** The declared OSS stack (Odoo, Mautic, Documenso, NocoDB/Baserow, Ollama) is barely used in practice (0–2 mentions across 76 files) while HubSpot — not part of the declared stack at all — appears 33 times.

### Tasks
- [ ] **Make the decision first, before editing 76 files:** is HubSpot's free tier now the actual intended default, or is Odoo still the goal? This determines which direction Batch 2 edits go. (Recommendation: if HubSpot's free tier already works for you in practice, it's fine to keep — just update the "Core OSS stack" paragraph in `N8N-AUTOMATION-INDEX.md` to say so honestly, rather than silently ignoring five named tools you don't actually use.)
- [ ] Batch 2a (Sales, ~54 `tools.md` files): pass through and add the "OSS/Free Alt" column value wherever it's currently blank, per the decision above
- [ ] Batch 2b (Marketing, ~22 `tools.md` files): same pass
- [ ] Update `N8N-AUTOMATION-INDEX.md`'s "Core OSS stack referenced throughout" paragraph to match reality once the decision is locked in

**Done when:** every `tools.md` file's OSS/Free-alt column is filled in consistently with whatever stack you actually decided on, and the index paragraph doesn't name tools nobody uses.

---

## Batch 3 — Sales Funnel Depth: Stages 34–37 (~1 session)

**What's wrong:** Pricing, Negotiation, Contract & Legal, Closing Techniques sit at 21–22 lines vs. Stage 06's 101-line bar. This is your own Batch 6 remainder, already scoped in `Sales Funnel/IMPLEMENTATION-PLAN.md` §2 — this just re-confirms it and folds in the template-linking step from Batch 1's method.

### Tasks
- [ ] 34 Pricing and Packaging — expand `automation.md`/`tools.md` to Stage-06 depth; this stage is mostly 🔴 (strategic/negotiated) per the index, so focus depth on the *price-list lookup* automation that legitimately can run, not on fabricating automation for the judgment call
- [ ] 35 Negotiation — same 🔴 treatment; depth here means better logging/prep automation, not more "automation," per the index's own honest framing
- [ ] 36 Contract and Legal — 🟡 per index; build out the Documenso webhook → CRM status-update pattern to real depth (this one has genuine automation potential the current 22 lines don't reflect)
- [ ] 37 Closing Techniques — 🔴; same treatment as 34/35
- [ ] Update `Sales Funnel/IMPLEMENTATION-PLAN.md` tracker row for Batch 6 remainder

**Done when:** all 4 stages match Stage 06's depth convention, with the same honest 🟢/🟡/🔴 framing already established.

---

## Batch 4 — Sales Funnel Depth: Stages 38–46 (~1–2 sessions, largest remaining batch)

**What's wrong:** This is your own Batch 7 (9 stages, 81 files), currently "⬜ Not started" in the tracker — and unlike Stages 47–50, this one really is thin on disk, not just mis-tracked.

### Tasks
- [ ] 38 Deal Desk and Approval Workflows — 🟢 per index; build the approval-routing n8n pattern to full depth (the placeholder version already sketches the right flow — flesh it out, don't restart)
- [ ] 39 Payment and Invoicing — 🟢; pair with Batch 1's Stripe/Airtable template link
- [ ] 40 Client Onboarding — 🟢, flagged in the index as "the highest-ROI n8n build in the whole 54-stage funnel" — prioritize this one first within the batch; pair with Batch 1's onboarding template
- [ ] 41 Kickoff and Expectation Setting — 🟡
- [ ] 42 Implementation and Delivery Setup — 🟡
- [ ] 43 Account Management — 🟡; build out the Metabase health-check digest pattern
- [ ] 44 Customer Success Planning — 🟡
- [ ] 45 Product and Service Adoption — already at pilot depth per the index; verify and leave as-is
- [ ] 46 Support and Issue Resolution — already at pilot depth; verify, then pair with Batch 1's Slack/Linear template link
- [ ] Update tracker for Batch 7

**Done when:** 38–44 reach Stage-06-equivalent depth (45–46 just need verification, not rebuilding).

---

## Batch 5 — Marketing Foundation: M01–M03 (~1 session)

**What's wrong:** The only 3 Marketing modules with no zip-fix available and no real content anywhere — true from-scratch writes. This is your own Batch 1 in `MARKETING-IMPLEMENTATION-PLAN.md` §4.

### Tasks
- [ ] M01 Brand and Positioning Foundation — cross-reference existing Sales Funnel Stages 02/03 (ICP/Persona) rather than duplicating; this module is mostly 🔴 (strategic), so keep automation.md honest about that
- [ ] M02 Channel and Platform Selection — 🔴/decision-layer; output feeds M11–M17's channel choices
- [ ] M03 Content Pillars and Messaging Framework — 🔴; output feeds M09 (already built) as structured input
- [ ] Update tracker for Batch 1

**Done when:** Marketing reaches 12/22 modules at real depth (9 from Batch 0 + these 3).

---

## Batch 6 — Structural Consolidation (~1 session, do last)

**What's wrong:** Three parallel documentation systems (legacy Notion/CJE, Sales Funnel, Marketing) with conflicting tool defaults and no cross-links, per audit §5.

### Tasks
- [ ] Confirm the 54+22 stage system as canonical (recommended — it's the most rigorous and most recently maintained)
- [ ] Add a one-line pointer to the top of each legacy doc that's been superseded: `SD-08 — Automation & AI Hub`, `Automations list`, the 13-stage CJE system's Stage 1–13 files, `🛠️ CJE Tool Stack` → "Superseded by [Sales Funnel/Marketing link]"
- [ ] Either move all legacy Notion-export files into an explicit `/Archive` subfolder, or leave in place but fully cross-linked — pick one, don't half-do it
- [ ] Final pass: re-run the same line-count/stub check used in this audit across all 76+22 files one more time to confirm no other tracker-vs-disk mismatches slipped through during Batches 1–5's edits

**Done when:** anyone (human or AI agent) opening this repo cold can tell in under a minute which system is canonical and that the older one is intentionally archived, not abandoned.

---

## Summary Timeline

| Batch | Focus | Effort | Depends on |
|---|---|---|---|
| 0 | Zip merges + tracker truth + dead folder | ~1 hr | Nothing — do today |
| 1 | n8n template linking (14 stages) | ~2–3 hrs | Batch 0 |
| 2 | OSS tool table correction (76 files) | ~2 sessions | A decision call, then independent |
| 3 | Sales 34–37 depth | ~1 session | Independent |
| 4 | Sales 38–46 depth | ~1–2 sessions | Independent (largest remaining gap) |
| 5 | Marketing M01–M03 | ~1 session | Independent |
| 6 | Consolidate legacy vs. new systems | ~1 session | Do last, after 0–5 |

**Total:** roughly 8–10 working sessions to close every gap the audit identified, with Batch 0 alone recovering 3 "finished but hidden" stages for free.
