# Sales Funnel — Marketing Layer Gap Analysis & Additions

**Source repos reviewed:** `Public_Workspace/Growth Engine/Sales Funnel` (54 stages) + `Public_Workspace/Growth Engine` (Growth Hacking Master List, SEO Keyword & Action Plan, Social Media Platform Playbooks, Referral/Viral Engine)

---

## 1. The Gap, Stated Plainly

Your 54-stage Sales Funnel (`01 Market Research` → `54 Advocacy`) is a **sales-motion funnel**: it assumes a lead already exists and takes it from research/sourcing through to renewal and referral. It has zero stages for **how demand gets created in the first place** outside of manual list-building and cold outreach.

Everything you asked about — SEO, social media, growth hacking — already exists in your workspace, but it lives in a **separate, disconnected system** (`Growth Engine` root files: Growth Hacking Master List, SEO Keyword Plan, Social Media Platform Playbooks). It was never wired into the funnel or into the n8n automation modules (W0–W8) we built earlier.

Concretely, three things are missing from the funnel:

1. **A marketing/demand-generation track that runs in parallel to Stage 05 (Lead Source Selection)** — right now Stage 05 only covers *where to pull outbound lists from*, not *how to make people find you organically*.
2. **A content engine that feeds both SEO and social** — one piece of content should fan out into blog + LinkedIn + Instagram + YouTube + email, and that fan-out should show up as an n8n module, not a manual task.
3. **A brand/awareness loop that feeds Stage 05 continuously** — SEO and social are slow-compounding channels; without a stage number and owner, they get skipped in favor of urgent outbound work (which is what's happening now).

---

## 2. Proposed Fix: Add a Parallel "Track M" (Marketing) Alongside the Existing Sales Funnel

Don't renumber your 54 stages — they're a clean sales motion and other pages already reference those numbers. Instead, add a **second track that runs beside Stages 01–05** and continuously feeds inbound leads into the same Stage 06+ pipeline (this also matches the Inbound/Outbound split already in the n8n plan — W0 Inbound Capture becomes the landing point for this new track).

```
                    ┌─────────────────────────────────────────────────────┐
                    │              TRACK M — MARKETING ENGINE               │
                    │         (runs continuously, feeds inbound leads)      │
                    ├─────────────────────────────────────────────────────┤
  M1  BRAND & POSITIONING FOUNDATION   (parallel to Stage 02-03: ICP/Persona)
        - Brand guidelines, voice, visual identity
        - Positioning statement per ICP segment
                                   ▼
  M2  SEO ENGINE                        (parallel to Stage 05: Lead Sourcing)
        - Keyword master list (Tier 1/2/3 — already in your workspace)
        - On-page SEO rollout across website
        - Off-page: 30+ directory listings, guest posts, HARO
        - Technical SEO checklist + monthly ranking report
                                   ▼
  M3  CONTENT ENGINE                    (feeds M2 + M4 simultaneously)
        - 1 blog post/week (1,500+ words, SEO-targeted)
        - AI-assisted repurposing: 1 blog → 6+ distribution assets
        - Content Marketing Calendar (already exists — needs scheduling automation)
                                   ▼
  M4  SOCIAL MEDIA ENGINE               (organic, parallel to Stage 15-21: Outreach)
        - 8-platform playbook already documented: LinkedIn, Instagram,
          Facebook, Twitter/X, YouTube, Pinterest, Threads, WhatsApp Business
        - Platform-specific cadence + hashtag/keyword strategy
                                   ▼
  M5  GROWTH HACKING EXPERIMENTS       (feeds all of M1-M4 + Stage 05)
        - 150-tactic idea bank already exists, organized by channel
        - Needs: monthly experiment tracker (Impact × Effort scoring),
          3-5 tactics tested/month, scale-or-kill after 30 days
                                   ▼
  M6  COMMUNITY & PARTNERSHIP LOOPS    (feeds Stage 05 + Stage 53 Referral)
        - Facebook/WhatsApp/Slack communities
        - Partner co-marketing (agencies, CAs, coaches)
                                   ▼
                    └──────────────► lands as INBOUND LEAD in Stage 06
                                       (same "Lead Extraction" stage outbound uses)
```

**Key architectural point:** Track M doesn't bypass your existing funnel — it's a second front door. Every marketing-generated lead (blog reader who books a call, LinkedIn commenter who DMs, referral from a community) still enters the funnel at **Stage 06 (Lead Extraction)** as an inbound record, gets scored/segmented identically to outbound leads, and flows through the same 54 stages from there. This matches the **W0 Inbound Capture** module already designed in the n8n plan — Track M is simply what generates the volume that W0 captures.

---

## 3. What Needs to Be Created vs. What Already Exists

| Component | Status | Location |
|---|---|---|
| Growth Hacking tactics (150+, categorized) | ✅ Exists | `Growth Hacking Master List (100+ Tactics)` |
| SEO keyword list + on/off-page plan | ✅ Exists | `🔍 SEO Keyword Master List & Action Plan` |
| Social media playbooks (8 platforms) | ✅ Exists | `📱 Social Media Platform Playbooks` |
| Content repurposing framework | ✅ Exists (inside the social playbook doc) | Same file, "Content Repurposing System" section |
| **Stage numbers / funnel integration for the above** | ❌ Missing | Needs to be created — this is the actual gap |
| **Growth Experiments Tracker (Impact × Effort log)** | ⚠️ Referenced but not found as a live page | Needs to be built |
| **n8n modules for M2-M6 (auto-publish, auto-repurpose)** | ❌ Missing | Not yet in the W0-W8 automation plan |
| **Link from Track M output → Stage 06 inbound intake** | ❌ Missing | This is the connective tissue that's currently absent |

---

## 4. Recommended New n8n Modules (extends the earlier W0–W8 plan)

| Module | Feeds | What it automates |
|---|---|---|
| **M-W1 — Content Repurposing Engine** | M3 → M4 | Blog post published → AI drafts LinkedIn post, IG carousel copy, YouTube script, tweet thread, newsletter section in one pass → VA reviews → auto-schedule via Buffer/Publer |
| **M-W2 — Social Publishing & Listening** | M4 | Scheduled posts across 8 platforms; monitor comments/DMs → route hot leads to Slack/Rocket.Chat alert → same reply-triage pattern as W4 |
| **M-W3 — SEO Monitoring** | M2 | Weekly Google Search Console pull → rank tracking → alert on ranking drops or new keyword opportunities |
| **M-W4 — Growth Experiment Tracker** | M5 | Each experiment logged (channel, tactic, impact score, effort score) → auto-calculates priority → 30-day auto-reminder to review and scale/kill |
| **M-W5 — Inbound-to-CRM Bridge** | M2-M6 → Stage 06 | Every inbound touchpoint (blog CTA click, social DM, community signup) lands in Odoo CRM as `crm.lead` with `source=marketing`, tagged by channel — this is the actual bridge connecting Track M to your existing funnel |

---

## 5. Immediate Next Steps

1. **Confirm this Track M structure** — happy to build it out as full Notion pages (matching your existing V3-style formatting) if this direction looks right.
2. **Build the Growth Experiments Tracker** — this is referenced across multiple files but doesn't exist as a live database yet; it's the single highest-leverage missing piece since it's what turns the 150-tactic list from an idea bank into an actual execution system.
3. **Wire M-W5 (Inbound-to-CRM Bridge)** — this is the piece that actually closes the gap; without it, Track M content sits disconnected from the sales funnel exactly like it does today.
4. **Decide: build M-W1 through M-W4 in n8n now, or sequence after W0-W8 (sales automation) is live?** Given you're currently mid-build on the outbound/inbound sales stack, recommend finishing that first and layering marketing automation in as Phase 2 — trying to build both simultaneously risks neither getting done well.

---

*Compiled from: `Growth Engine/Sales Funnel/` (54-stage funnel structure), `Growth Engine/Growth Hacking Master List (100+ Tactics)`, `Growth Engine/🔍 SEO Keyword Master List & Action Plan`, `Growth Engine/📱 Social Media Platform Playbooks — All 8 Platforms`, `Growth Engine/🔁 Stage 11 — Referral & Viral Engine`.*
