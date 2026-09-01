# Growth Engine — n8n / Automation Audit & Gap Report

**Scope:** `Growth-Engine/Marketing/` (22-stage marketing funnel) and `Growth-Engine/Sales Funnel/` (54-stage sales funnel), cross-checked against the 280+ template collection at `nivyindia/all_n8n_templates_collection` (a fork of `enescingoz/awesome-n8n-templates`) and the wider free/open-source automation ecosystem.

**Method:** Every stage/module folder was inspected file-by-file (not just the README) — line counts, actual content vs. placeholder text, and every n8n/tool reference were checked directly against the files on disk, not against what the tracker docs *say* was built. Several of this report's most important findings are places where the tracker disagreed with the actual files.

---

## 1. Executive Summary

You've already built something unusually good: a **76-stage** (54 Sales + 22 Marketing), **9-file-per-stage** documentation system (`README / methods / tools / automation / checklists / templates / resources / faq / references`), plus a dedicated `N8N-AUTOMATION-INDEX.md` that assigns every one of the 54 sales stages a 🟢/🟡/🔴 automation-feasibility rating and an OSS tool stack. That index file is essentially the deliverable you asked me to check for — it already exists, and it's good.

But three things need attention before this is actually "automated end-to-end with free/OSS tools":

| # | Finding | Severity |
|---|---|---|
| 1 | **Finished work is sitting unused.** M18, M19, and M20 (Growth Hacking, Community, Partnerships) are fully written — but zipped in the same folder as their own *empty placeholder stubs*. The live folders show 8-line "not built yet" placeholders while a finished 21-file, ~26KB set sits right next to them, unopened. | 🔴 Fix first — 10 minutes of work unlocks 3 stages instantly |
| 2 | **Almost no actual n8n templates are linked.** Across ~1,600 files and 76 stage folders, only **4 specific n8n.io template links** exist in total, and **zero** references to the `all_n8n_templates_collection` / `awesome-n8n-templates` repo itself, despite it being exactly the kind of library the automation index says to search. Most stages describe automation *conceptually* ("push to CRM via n8n") without pointing to a template to start from. | 🟡 High-value gap |
| 3 | **The "free/OSS-first" rule isn't actually followed in the tool tables.** The automation index names a specific OSS stack (Odoo, Mautic, Documenso, NocoDB/Baserow, Ollama, Listmonk) as the intended default — but across all 76 `tools.md` files, HubSpot appears 33 times and Odoo only 2; Mautic, Documenso, NocoDB, Baserow, and Ollama appear **zero** times. | 🟡 High-value gap |

Beyond those three, there's a structural issue worth naming: this workspace actually contains **three parallel automation documentation systems** that were built at different times and don't fully agree with each other (see §5). That's not necessarily wrong, but it's worth a deliberate decision about which one is canonical before adding a fourth.

---

## 2. What Actually Exists (verified on disk)

### 2.1 Sales Funnel (54 stages, `Sales Funnel/`)
- Full 486-file skeleton exists for all 54 stages.
- **Genuinely built to real depth:** Stages 01–33 and 47–54 (43 of 54) have substantive `automation.md`/`tools.md`/`README.md` content — not placeholders. Stage 06 (Lead Extraction) is the deepest, at 101 lines of automation content alone, and is the intended quality bar.
- **Genuinely thin/stub:** Stages 34–37 and 38–46 (13 stages) have `automation.md` files in the 21–24 line range — real content, but far shallower than the Stage 06 bar, and missing the specific-template-link layer entirely.
- **Correction to the tracker:** `IMPLEMENTATION-PLAN.md` lists Stages 47–50 as "not started" — they are not. On disk, Stage 47 has a 121-line README and Stage 50 a 167-line README, comparable in depth to stages marked "done." The tracker is stale in your favor here — more is built than the tracker credits.

### 2.2 Marketing Funnel (22 stages, `Marketing/`)
- Full skeleton exists for all 22 modules (M01–M22).
- **Genuinely built:** M04–M17, M21, M22 have real content (M22's Inbound-to-CRM Bridge is the strongest — 71-line automation.md with 4 fully specified n8n workflows already running in production per its own notes).
- **Falsely marked complete:** M01, M02, M03, M18, M19, M20 show `automation.md` (and every other file except README) at exactly **8 lines each** — the literal placeholder text ("This file is a placeholder... has not been written yet"). The tracker (`MARKETING-IMPLEMENTATION-PLAN.md` §7) marks M18 as "✅ Done, 9/9" and M19–M20 as "✅ Done, 18/18." **This is incorrect as of the live folder state.**
- **The fix is already sitting there:** `M18 Growth Hacking Experiment Engine.zip`, `M19 Community Building.zip`, and `M20 Partnerships, Co-Marketing and PR.zip` exist in the same `Marketing/` folder, each containing a complete, real 9-file set (e.g., M19's `automation.md` is 2,621 bytes of real content vs. the ~230-byte stub currently live). **These were delivered and never extracted/merged into the live folders.** See §4.1 for the exact fix.

### 2.3 The `Automation/` top-level folder
Completely empty — zero files. This sits alongside `Marketing/` and `Sales Funnel/` in the repo root and looks like it was meant to hold something (possibly exported `.json` n8n workflow files) but nothing was ever put there.

### 2.4 Legacy documentation (root-level Notion export, ~500 files)
Outside the two structured funnels, the repo root has a large, older Notion export: `SD-08 — Automation & AI Hub`, `n8n Workflow 1–8` (individual workflow specs, mostly marked "⬜ Build in Phase 4" — i.e., planned, not built), `Automations list` (a 48-automation master plan), `🛠️ CJE Tool Stack`, and a 13-stage "Customer Journey Engineering" (CJE) system with its own Stage 1–13 naming. **This predates and duplicates parts of the new 54+22 system** — see §5.

---

## 3. Cross-Check Against the n8n Template Collection

The collection you linked (`nivyindia/all_n8n_templates_collection`, forked from `enescingoz/awesome-n8n-templates`) organizes 280+ templates into 18 categories: Gmail/Email, Telegram, Google Drive & Sheets, WordPress, PDF/Document Processing, Discord, Database & Storage, DevOps, Airtable, Notion, Slack, OpenAI/LLMs, WhatsApp, Instagram/Twitter, Other Integrations, Forms & Surveys, AI Research/RAG, and Other.

**Finding:** None of your 76 stage folders reference this collection by name or link into its specific category folders. Your own `N8N-AUTOMATION-INDEX.md` correctly points people to n8n.io's *live* category pages instead (a reasonable choice, since n8n.io's own library is larger and always current) — but that means the 280+ templates you specifically asked about were never actually cross-referenced against your funnel. Below is that cross-reference, done directly against the collection's real template list.

### 3.1 Direct template matches (ready to import today)

| Your Stage | Category in the collection | Specific template | Fit |
|---|---|---|---|
| Sales 40 — Client Onboarding | Other Integrations | *"Streamline Client Onboarding with PDF, Trello, Slack, Gmail and Airtable"* | Strong — matches your own automation.md's "contract signed → project created → welcome email" pattern almost exactly |
| Sales 33 — Proposal Creation | PDF & Document Processing | *"Invoice data extraction with LlamaParse and OpenAI"* (pattern reusable for proposal generation) | Adjacent — reusable pattern, not a direct copy |
| Sales 39 — Payment and Invoicing | Other / Google Sheets | *"Airtable to Google Sheets Auto-Sync"* + Odoo/Stripe webhook pattern | Adapt |
| Sales 16 — Email Outreach | Gmail & Email Automation | *"LeadPilot Lite – AI Cold Email Writer"* (writes personalized cold emails from a Sheets lead list) | Strong |
| Sales 06/07/08 — Lead Extraction/Enrichment | Google Drive & Sheets | *"Qualify new leads in Google Sheets via OpenAI's GPT-4"* | Strong — matches your existing Stage 11 (Lead Scoring) logic |
| Sales 25 — Reply Handling and Triage | Gmail & Email | *"Auto-label incoming Gmail messages with AI nodes"*, *"InboxZero Lite – AI Email Classifier"* | Strong |
| Sales 46 — Support and Issue Resolution | Slack | *"Customer Support Channel and Ticketing System with Slack and Linear"*, *"Sentiment Analysis Tracking on Support Issues with Linear and Slack"* | Strong |
| Sales 51 — Customer Feedback and NPS | Notion / Slack | *"Add positive feedback messages to a table in Notion"* (Typeform → sentiment analysis → Notion → Slack alert) | Strong |
| Marketing M17 — Email Newsletter | Gmail/Other | *"Daily Email Notification"* (Ollama-summarized digest), general newsletter-sequence patterns | Adapt |
| Marketing M09/M10 — Content Production/Repurposing | WordPress | *"Automate Blog Creation in Brand Voice with AI"*, *"Write a WordPress post with AI (starting from a few keywords)"* | Strong — direct fit for your already-built M09 pilot |
| Marketing M11 — LinkedIn Organic Engine | OpenAI/LLMs | *"AI-Powered Social Media Amplifier"* | Adapt |
| Marketing M20 — Partnerships/PR | Notion | *"Automate Competitor Research with Exa.ai, Notion and AI Agents"* (repurposable for partner/prospect research) | Adapt |
| Sales 19 — WhatsApp Outreach | WhatsApp | Collection's WhatsApp category (n8n + Evolution API pattern, matches your own tools.md recommendation) | Strong — confirms your existing OSS choice |
| Sales 13 — CRM Setup | Database & Storage | *"Chat with Postgresql Database"*, *"Generate SQL queries from schema only – AI-powered"* | Adjacent, useful for reporting layer |

### 3.2 What the collection does *not* cover well
The collection is consumer/SMB-integration-heavy (Gmail, Slack, Notion, WhatsApp) and has almost nothing for the judgment-heavy middle of your sales funnel — Stages 29–37 (Discovery Call Execution through Closing Techniques) and Stage 35 (Negotiation) specifically. This actually **confirms** your own `N8N-AUTOMATION-INDEX.md`'s 🔴 ratings for those stages are correct, not an oversight: there is no template anywhere (in this collection or n8n.io broadly) for automating a negotiation or a sales conversation, because that's not an automatable activity. Good instinct already reflected in your docs.

### 3.3 Recommendation
Add a short "Reference collection" line to `N8N-AUTOMATION-INDEX.md` §0 linking to `nivyindia/all_n8n_templates_collection` as a second, curated (smaller, easier-to-browse) alternative to n8n.io's live library, and drop the specific template names above into the relevant stages' own `automation.md` files (this is exactly the "specific 1–2 verified templates per stage" format the index says it wants but only actually delivers for ~6 of 54 stages).

---

## 4. Priority Action List

### 4.1 🔴 Do this first (10 minutes, unlocks 3 finished stages)
Unzip and merge, overwriting the stub folders:
```
Marketing/M18 Growth Hacking Experiment Engine.zip  →  Marketing/M18 Growth Hacking Experiment Engine/
Marketing/M19 Community Building.zip                →  Marketing/M19 Community Building/
Marketing/M20 Partnerships, Co-Marketing and PR.zip →  Marketing/M20 Partnerships, Co-Marketing and PR/
```
Then delete the three `.zip` files once confirmed merged. This alone moves Marketing from "6 of 22 stages real" to "9 of 22 stages real" with zero new writing.

### 4.2 🟡 Fix the tracker so it stops lying to you
- `MARKETING-IMPLEMENTATION-PLAN.md` §7: correct M18/M19/M20 rows to reflect they were stub until the zip merge above happens.
- `Sales Funnel/IMPLEMENTATION-PLAN.md` §5: Stages 47–50 are further along than marked "not started" — update to avoid re-doing already-good work.

### 4.3 🟡 Genuinely still-needed content (real gaps, not tracker errors)
- **Sales Funnel Stages 34–37** (Pricing/Negotiation/Contract/Closing) and **38–46** (Deal Desk through Support) — thin `automation.md` (21–24 lines vs. the 101-line Stage 06 bar). These need the same specific-template-link treatment as §3.1 above, not just conceptual descriptions.
- **Marketing M01–M03** (Brand/Channel/Content Pillars) — true skeleton, no zip fix available, needs to be written from scratch (your own IMPLEMENTATION-PLAN.md already scopes this as Batch 1).
- **Empty `Automation/` folder** — either populate it with the actual exported `.json` workflow files once you start building n8n workflows for real, or delete it so it doesn't look like a broken link.

### 4.4 🟢 Quick wins using what you already have
- Import the 14 template matches in §3.1 directly — most require no adaptation.
- Add the OSS stack's missing pieces to `tools.md` files where only HubSpot is listed (see §4.5) — even just as the "free alt" column your own format already has, which is currently blank for Odoo/Mautic/Documenso/NocoDB/Ollama in the vast majority of stages.

### 4.5 🟡 Resolve the OSS-first inconsistency
Your automation index states the intended stack: **n8n · Odoo Community · PostgreSQL · Mautic · Mailcow · Cal.com · Chatwoot · Documenso · Metabase · NocoDB/Baserow · Ollama/Open WebUI · Evolution API/Wuzapi · Rocket.Chat.**
Actual mention counts across all 76 `tools.md` files:

| Tool | Mentions | Intended role |
|---|---|---|
| HubSpot | 33 / 76 | *(paid — not in the declared OSS stack at all)* |
| n8n | 35 / 76 | orchestration |
| Cal.com | 9 / 76 | scheduling |
| Apollo | 9 / 76 | *(paid)* |
| Postiz | 7 / 76 | social scheduling |
| Odoo | 2 / 76 | CRM/ERP |
| Chatwoot | 1 / 76 | support inbox |
| Listmonk | 1 / 76 | email infra |
| Mautic, Documenso, NocoDB, Baserow, Ollama | 0 / 76 each | marketing automation, e-sign, lightweight DB, self-hosted AI |

Either (a) update the individual stage `tools.md` files to actually default to the declared stack per your own stated rule, or (b) if HubSpot's free tier is the actual intended default going forward, update the master index's "Core OSS stack" paragraph to say so honestly instead of naming five tools that are never used.

---

## 5. Structural Note: Three Overlapping Systems

This workspace currently documents the same sales/marketing process three separate times, at three separate levels of maturity:

1. **Legacy Notion export (root-level, ~500 files, undated iterations):** `SD-08 — Automation & AI Hub`, `Automations list` (48 automations), the 13-stage "Customer Journey Engineering" system (`Stage 1 — Attention Engine` through `Stage 13`), `🛠️ CJE Tool Stack`. This system's tool stack is **paid-tool-first** (HubSpot/GoHighLevel, Instantly, Clay, Apollo, PhantomBuster, Buffer) — the opposite default of the newer system.
2. **Sales Funnel (54 stages)** — newest, most rigorous, OSS-first by design.
3. **Marketing (22 stages)** — same design as #2, less mature, explicitly built to feed into #2 at Stage 06.

None of these is wrong on its own, but having three means: (a) anyone new to the workspace won't know which is canonical, (b) tool recommendations actively conflict (paid CRM in system 1, Odoo in systems 2/3), and (c) the 48-automation legacy list and the 54-stage n8n index describe overlapping ground with different levels of detail and no cross-link between them.

**Recommendation:** Pick the 54+22 stage system as canonical (it's clearly the most rigorous and most recently worked on), add one line to each legacy doc ("Superseded by Sales Funnel/Marketing — see [link]") or move the legacy folder into an explicit `/Archive` subfolder, so the next person (or AI agent) working in this workspace doesn't build a fourth version of the same thing.

---

## 6. Summary Scorecard

| Area | Status |
|---|---|
| Sales Funnel stages at real pilot depth | 43 / 54 (80%) — corrected up from tracker's claimed 334/496-file count once 47–50 are credited |
| Marketing modules at real pilot depth | 9 / 22 (41%) once §4.1's zip-merge is done; 6/22 (27%) as currently live |
| Specific, verified n8n template links present | 4 total, repo-wide |
| Stages with a concrete import-ready template identified in this report | 14 (§3.1) |
| Declared OSS stack tools actually appearing in `tools.md` files | 4 of 13 tools used at all; 5 of 13 never mentioned once |
| Empty/orphaned top-level folders | 1 (`Automation/`) |
| Parallel/duplicate documentation systems | 3 (see §5) |

---

*Compiled from direct inspection of the uploaded `Growth-Engine.zip` export (1,638 files) and the public n8n template collection (`enescingoz/awesome-n8n-templates`, the upstream of your fork) as of July 23, 2026.*
