# Growth Engine — OSS/Free-Stack Upgrade Command

> **How to use this file:** Paste this entire document as your message to Claude in a new chat, with the `Growth-Engine.zip` (or the specific stage folder/s you want done) attached. Claude should treat everything below as its working instructions for the session. You can also just say "run the Growth Engine OSS Upgrade Command on stages [list]" if Claude already has this file in context/memory.

---

## 0. Context (read first)

This is the Growth Engine / Sales & Marketing Funnel knowledge base for Billion Dreams United / Nivy (Abhi). It lives in Notion and is exported as a folder tree with two funnel sections:

- `00 Marketing/M01 ... M22` — 22 marketing funnel stages
- `00 Sales Funnel/01 ... 54` — 54 sales funnel stages

Each stage folder is built to "pilot depth": a fixed set of files (`README.md`, `methods.md`, `tools.md`, `automation.md`, `checklists.md`, `templates.md`, `resources.md`, `faq.md`, `references.md`), all describing how to execute that stage of the funnel.

**The n8n template repository for this project is [`nivyindia/all_n8n_templates_collection`](https://github.com/nivyindia/all_n8n_templates_collection)** — it is a fork of `enescingoz/awesome-n8n-templates` (280+ n8n workflow templates), so it has the exact same file tree/paths as the original, just under Nivy's own repo name. **Always link to the `nivyindia` fork, never the original `enescingoz` repo**, even though the content is identical — confirm this is still true by checking `https://api.github.com/repos/nivyindia/all_n8n_templates_collection` (should show `"fork": true` and `"parent": {"full_name": "enescingoz/awesome-n8n-templates"}`) before relying on it; if the repo has since diverged or been renamed, re-derive template paths from whichever repo is now correct and say so.

---

## 1. The Standing Policy: Open-Source or Free Tools Only

**No paid SaaS tool is acceptable anywhere in this knowledge base**, unless the person explicitly says otherwise for a specific stage. Every tool named in every stage must be one of:
- Genuinely **open-source** (self-hosted, permissive/copyleft license — MIT, Apache 2.0, LGPL, AGPL, etc.), or
- A **free tier of a hosted tool** that requires no payment for the volume this funnel actually needs (e.g., Google Postmaster Tools, Gmail free tier, MXToolbox free tier)

If no OSS/free option exists for a job (this does happen — say so honestly rather than force-fitting a fake substitute or silently reverting to a paid tool). Flag it clearly as "no true OSS equivalent exists; the free-tier option below is the practical answer."

When multiple OSS/free options exist for the same job (e.g. Mautic vs. building the same thing in raw n8n; Rspamd vs. SpamAssassin; parsedmarc vs. Open-DMARC-Analyzer), **do not just pick one** — list the full field considered and name a **best pick with a one-line reason**, the same way a "best tool per category" comparison table would.

---

## 2. Per-Stage File Targets

For **every stage folder** you touch, work through this file list. If a file doesn't exist yet for that stage, create it (see §2.8) — don't skip a category just because the original 9-file build didn't include it.

### 2.1 `tools.md`
- Rebuild the tool table so every row is OSS/free (per §1).
- Link every tool name to its real website or GitHub repo — verify each link resolves (see §4) before including it.
- Add an **"OSS Option Comparison — Best Pick Per Category"** table at the end: one row per job-to-be-done in this stage, listing all OSS/free options considered, the best pick, and why.
- Note pricing/cost honestly: "free" self-hosted tools still typically need a VPS; say so rather than implying $0 total cost.

### 2.2 `methods.md`
- Go through every method category already present (Traditional, Modern/Tool-Assisted, AI-Assisted, Manual, Automated, API/Integration, Browser Automation, Scraping, Public Database/Government, Community/Referral, etc.) and make sure each one names the exact OSS/free tool and, where applicable, the n8n template link that executes it.
- **Then do a completeness audit**: ask "is there any method, technique, or resource commonly used to execute this stage of a sales/marketing funnel that this file doesn't mention yet?" Think about things like:
  - Compliance/legal automation specific to this stage's channel (e.g. List-Unsubscribe headers for email, opt-in tracking for SMS/WhatsApp, platform ToS limits for LinkedIn/social automation)
  - Pre-execution quality/risk checks (e.g. spam-content scoring before sending, duplicate/dedup checks before a batch runs)
  - Scaling mechanics specific to the channel (e.g. mailbox/domain rotation for email, account-warming for LinkedIn, rate-limit pacing for any outbound channel)
  - A cheaper/free alternative to any paid differentiator feature a competitor tool advertises for this job (e.g. Lemlist's personalized video → Cap.so; a paid AI writer → self-hosted Ollama)
  - Data-driven optimization using data the funnel is already collecting (e.g. send-time/post-time optimization from historical CRM data — this rarely needs a new tool, just reusing existing data)
  - Cross-stage/cross-channel fallback: what happens to a contact/lead that doesn't convert at this stage — does it silently die, or hand off to the next logical stage/channel?
  - Add every genuinely missing method as a new subsection, clearly marked `*(added — was missing)*` so it's visible what changed.
- End with a "Method Selection Guidance" paragraph confirming every method in the file (including newly added ones) has a working OSS/free execution path.

### 2.3 `automation.md`
- List every relevant n8n template from `nivyindia/all_n8n_templates_collection` that maps to a method in this stage — search the repo's file tree (see §3) rather than guessing filenames.
- Wherever a template uses a paid API node (commonly OpenAI), note that the node should be swapped for a self-hosted **Ollama** node to keep the workflow free — don't silently leave paid-API templates unannotated.
- Build (or rebuild) a **full end-to-end automation flow diagram** in text (`A → B → C → D`) that chains together every relevant piece: data source → AI drafting/scoring → human-approval gate where appropriate → execution tool → status sync back to CRM → alerting → fallback/handoff. This should reflect the *complete* stage, not just the original single template link.
- Include any sub-flows the completeness audit in §2.2 surfaced (e.g. a warm-up sub-flow, a monitoring sub-flow, a fallback-router sub-flow).

### 2.4 `checklists.md`, `faq.md`, `references.md`
- Sweep these for any leftover mention of a paid tool name (e.g. "Instantly," "Apollo," "Lemlist," or whatever the stage's original paid-tool references were) and replace with the OSS/free equivalent chosen in `tools.md`.
- In `references.md`, replace plain-text vendor names with hyperlinks to the OSS/free tool's real documentation.
- In `faq.md`, consider adding one FAQ entry addressing "do we need to pay for [X] to run this stage?" with a direct "No — here's the free stack" answer.

### 2.5 `README.md`
- Update the file-navigation line and add a link to `precautions.md` (see §2.7) if it's newly created for this stage.
- Leave historical "Source note" provenance references (e.g. "built from the Apollo + Instantly SOP") alone — those describe where the *original content* came from, not a tool recommendation; don't rewrite history, just make sure nothing downstream still recommends buying that tool.

### 2.6 `templates.md`, `resources.md`
- Usually don't need tool-name changes (they're mostly copy/website-library content), but scan them anyway in case a paid tool is referenced inline.

### 2.7 `precautions.md` — **create this file for every stage if it doesn't already exist**
This is a new file type, not part of the original 9-file pilot depth. Every stage needs one. Cover, in whatever subset is genuinely relevant to that specific stage (don't force sections that don't apply):

1. **Legal/compliance by market.** Nivy's funnel serves US, UK, Canada, Australia, UAE, and Singapore (check current stage/company context for the live market list). Cold outreach law is **not uniform** across these — most importantly, Canada's CASL is opt-in by default (unlike the US's opt-out CAN-SPAM), so a list-building or outreach method that's fine in the US can be a serious violation the moment a Canadian contact is on it. Build a short market-by-market table (regime name, consent model, key requirement, penalty exposure) for whichever channel/method this stage covers (email, LinkedIn, WhatsApp, SMS, cold calling, etc. — each channel has its own legal regime, e.g. TCPA for US cold calling/SMS, WhatsApp Business Policy for WhatsApp outreach). Always caveat that this is not legal advice and a local-counsel review is needed before scaling into a new market.
2. **Self-hosting operational risk**, if this stage's tools are self-hosted: patching, backups, uptime monitoring, single-point-of-failure/access risk.
3. **Risk specific to the channel/method** at hand (e.g. deliverability risk for email, account-ban risk for LinkedIn/social automation, rate-limit/ban risk for scraping, WhatsApp number-ban risk).
4. **Data security responsibility** — self-hosting shifts PII security obligations onto Nivy directly; note this plainly.
5. **Open-source maintenance / "bus factor" risk** — call out if a chosen tool is maintained by a very small team/single developer, and recommend pinning versions rather than always auto-updating.
6. **Cost reality check** — "free" ≠ literally $0; note realistic infra/hosting/time costs.
7. A closing line making clear this file is a starting orientation, not a compliance certification.

Add `precautions.md` to the file-navigation line in `README.md` and give it a numbered section in the README body (after References), same pattern as the existing sections.

### 2.8 Other new files
If, during the completeness audit in §2.2, you find a category of missing content that doesn't fit naturally into any of the existing 9 files or into `precautions.md`, **create a new file for it** rather than cramming it somewhere it doesn't belong or leaving it out. Name it descriptively (kebab-case, `.md`), link it from `README.md`'s navigation line and body, and follow it with the same rigor (verified links, OSS-only tools, best-pick comparisons where relevant) as every other file. Use judgment — this should be rare, not a default; most gaps belong inside the existing files.

---

## 3. Finding the Right n8n Templates

1. Clone/fetch the tree of `nivyindia/all_n8n_templates_collection` via the GitHub API (`GET /repos/nivyindia/all_n8n_templates_collection/git/trees/main?recursive=1`) rather than guessing filenames.
2. Search that tree for filenames/paths matching the stage's channel and job (e.g. for email stages: `Gmail_and_Email_Automation/`, `workflows/Emailsend/`, `workflows/Schedule/`; for LinkedIn: search `Linkedin`; for CRM sync: `workflows/Odoo/`, `workflows/Baserow/`, `workflows/Nocodb/`; for AI drafting: `OpenAI_and_LLMs/Ollama_Basic_Workflow.json`).
3. Only include a template link once you've confirmed the exact path exists in the tree — don't reconstruct a plausible-looking filename from memory.
4. Prefer templates that map to an *actual method already in this stage*, and prefer adding 2-3 well-matched templates over one loosely-matched one.

---

## 4. Link Verification (mandatory before delivering)

Before finalizing any file, verify every new/changed link resolves:
- For GitHub file links (n8n templates, OSS repos): `curl -s -o /dev/null -w "%{http_code}" <url>` should return `200`. Build the URL with proper percent-encoding for spaces (`%20`) in template filenames.
- For OSS project homepages/docs and vendor doc pages that the sandbox's network egress doesn't whitelist (this is common — a `403` from the sandbox's own proxy is not the same as a broken link): cross-check via `web_search` that the domain and page are real and current instead of relying on the `curl` status code alone.
- Never include a fabricated or "looks-right" URL that hasn't been checked one of these two ways.

---

## 5. Workflow / Delivery Pattern

Follow the same batch pattern already established for this project:
1. Extract/clone the relevant folder(s) from the uploaded zip or the GitHub source.
2. Work stage-by-stage (or in small batches if doing several at once) rather than trying to rewrite everything in one pass — quality over speed.
3. After each stage (or batch), re-zip just that folder (or batch of folders) and deliver it via `present_files`, so the person can review incrementally rather than waiting for all 76 stages at once.
4. If this project has an `IMPLEMENTATION-PLAN.md` tracker or session log in the repo, update it to reflect which stages have received the OSS-upgrade pass, using the same tracker conventions already in use.
5. Keep a running note (in your final summary message, not necessarily a file) of: stages completed this session, any stage where no OSS/free equivalent existed for a needed tool (flag for the person's awareness), and any new file types created beyond `precautions.md`.

---

## 6. Tone / Output Expectations

- Be honest about gaps — if an OSS tool is objectively weaker than the paid tool it replaces (e.g. a smaller warm-up pool, a single-maintainer project), say so plainly rather than oversell it.
- Don't repeat unchanged content back to the person — when reporting progress, summarize what changed per stage (new methods added, tools swapped, precautions added) rather than pasting whole files into the chat.
- If the person hasn't specified which stages to run this on, ask (or confirm an assumption) rather than silently processing all 76 — this is a large amount of work per stage and should be paced deliberately, matching how the pilot-depth build itself was originally paced batch-by-batch.
