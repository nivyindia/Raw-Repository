# AI Marketing Automation Stack — Consolidated Guide

**Status:** Built 2026-07-24 from the raw `AI-Marketing-Automation-Guide.md` chat export (three overlapping passes, 2026-07-23) — de-duplicated into one reference doc and reconciled against the live Growth Engine Marketing Track M architecture.
**Supersedes:** the raw export as a working reference. Keep the export as a historical log if you want, but build from this doc going forward.

---

## 1. What Changed From the Raw Export

The raw export was three passes at the same question, each restating tools with growing overlap:

1. Pass 1 — a mixed proprietary + free stack (Claude/ChatGPT, Canva, Publer, Ahrefs, Veo, ElevenLabs, HeyGen, etc.)
2. Pass 2 — a "free/OSS only" rebuild of the same stack (~38 categories)
3. Pass 3 — a cleaner reorganization of Pass 2 into tables (~29 categories), the best-organized of the three

This doc merges all three into **one table per function**, each with a Free/OSS column and a Paid/Proprietary alternative column — the same pattern the Growth Engine repo already uses in `MARKETING-IMPLEMENTATION-PLAN.md` §2. Nothing from any of the three passes was dropped; where a category appeared in more than one pass under a different name (e.g. "Documentation" and "Knowledge Base" were split inconsistently across passes), it's merged here into one row with both names noted.

### Reconciliation against the existing repo tool stack

`MARKETING-IMPLEMENTATION-PLAN.md` §2 already has a shared 10-row free/OSS table that every Track M stage's `tools.md` points back to. It mostly agrees with this guide, with two differences worth flagging rather than silently resolving:

- **Social scheduling**: the repo's §2 table picks **Postiz** as the OSS scheduler; this guide's source export picks **Mixpost Community**. Both are legitimate self-hosted OSS options — this is a genuine open choice, not an error, and is left as two options rather than one silently overwriting the other (same principle used when the M18 tactic bank had conflicting numbers).
- **AI brain**: the repo's §2 table assumes Claude/ChatGPT's hosted free tiers; this guide's export leans toward a fully local stack (Ollama + Open WebUI + AnythingLLM) for the ₹0 case. Both are valid depending on whether local hosting is available — noted in §7 below.

Everything else (n8n, Odoo Community, Google Search Console, Screaming Frog, GA4 + Looker Studio, WhatsApp Business, Discord) already matches between the repo and this guide.

---

## 2. The AI Marketing Department — What's Automatable

| Function | AI Automation Level |
|---|---|
| Marketing Strategy | High — AI drafts, human still decides (see M01–M03's own "decision-layer, not automatable" framing) |
| Content Research | Very high |
| Content Calendar | Full |
| Social Media Design | Very high |
| Caption Writing | Full |
| Hashtag Research | Full |
| Image Creation | Very high |
| Video Creation | High |
| Short Reels | High |
| Publishing | Full |
| Community Management | Moderate — drafts only, human reviews before reply (see M19 and the Facebook Groups caution in §6) |
| SEO | High |
| Local SEO | Moderate |
| Analytics & Reporting | Full |

This table is the same shape as the Marketing Tasks table in §9, kept separate because it's function-level rather than task-level — both are included since they answer slightly different questions ("what department" vs. "what specific task").

---

## 3. Layered Architecture

### Layer 1 — AI Brain

Generates strategy, content, copy, and planning. Two viable setups:

- **Hosted (simpler to start):** Claude, ChatGPT, or Gemini — no infrastructure to run, but not free at volume
- **Self-hosted (₹0 ongoing, needs a machine to run it):** Ollama + Open WebUI (ChatGPT-style interface) + AnythingLLM (retrieval over your own docs) + LibreChat (multi-provider front end)

Either way, the brain's job list is the same: marketing strategy, campaign planning, content calendar, blog/SEO articles, email copy, landing page copy, ad copy, scripts, hooks, CTAs, keyword work.

### Layer 2 — Automation

**n8n** (self-hosted, free) is the connective layer — already standard across the whole Growth Engine repo, not something this guide is introducing. Typical chain:

```
AI Brain → Content drafted → Image/video generated → Uploaded to WordPress/CMS
→ Scheduled to social channels → Email sent → CRM updated → Report generated
```

Activepieces and Node-RED are viable OSS alternatives to n8n if you ever need a second option, but there's no reason to run two automation engines in parallel — pick one.

### Layer 3 — Knowledge Base

The AI brain needs your company's actual material to work from — SOPs, brand guidelines, templates, products/services, offers, pricing, FAQs. Options: Notion (already in use across this whole repo), AnythingLLM (if self-hosting the AI brain and want RAG over the same docs), Wiki.js / BookStack (documentation-first alternatives), Nextcloud (file storage), GitHub (version-controlled docs).

### Layer 4 — Image Creation

| Free / OSS | Paid / Proprietary |
|---|---|
| Stable Diffusion, ComfyUI, AUTOMATIC1111, Fooocus, InvokeAI | Adobe Firefly, Midjourney, Ideogram, ChatGPT Image Generation |

### Layer 5 — Video Creation

| Free / OSS | Paid / Proprietary |
|---|---|
| ComfyUI Video workflows, Wan2.1, Stable Video Diffusion, CogVideoX | Veo, Runway, Kling, Pika, Luma |

### Layer 6 — Voice

| Free / OSS | Paid / Proprietary |
|---|---|
| Piper TTS, Coqui TTS, XTTS | ElevenLabs, PlayHT |

### Layer 7 — AI Avatar / Presenter

No credible free/OSS avatar tool was in any of the three source passes — this is genuinely a paid-only category right now (**HeyGen, Synthesia**). Flagging rather than inventing a free alternative; verify current landscape before assuming this stays paid-only.

### Layer 8 — Design (Canva-class)

| Free / OSS | Paid / Proprietary |
|---|---|
| Penpot, GIMP, Krita, Inkscape | Canva |

Workflow once wired: AI writes the design prompt → design tool (Canva API, or a Penpot template) generates it → download → publish.

---

## 4. Social Media Scheduling & Publishing

| Type | Tool |
|---|---|
| Open Source (self-hosted) | Mixpost Community *(see §1 reconciliation note vs. repo's Postiz pick)* |
| Free tier | Buffer Free, Publer Free, Metricool Free |

Publishes to: Facebook, Instagram, LinkedIn, X, Pinterest, Google Business Profile, TikTok.

### Channel-specific automation patterns

- **Facebook:** AI drafts caption → generates image → schedules → publishes → monitors comments → drafts inbox replies for human approval
- **Instagram:** caption, hashtags, publish, story, carousel, reel caption — same drafting-then-scheduling pattern
- **LinkedIn:** article, company post, personal-branding post, poll, newsletter — cross-ref M11 (LinkedIn Organic Engine) and M18's LinkedIn tactic bank for the actual content playbook; this layer only covers the publishing mechanics
- **WordPress:** AI drafts blog → SEO pass → featured image → auto-publish → internal linking → search-engine indexing ping

---

## 5. Facebook/LinkedIn Groups — Platform-Risk Caution

This caution from the raw export is worth keeping verbatim in substance, because it directly overlaps a live tension already flagged in M18's tactic bank (the "50 connections/day" vs. "20 connections/day" LinkedIn variants logged there):

AI can find and shortlist relevant groups, and can draft posts for them. **Auto-joining groups, auto-posting into them, or posting at spam-like volume risks the platform limiting or banning the account** — this applies to Facebook Groups and to LinkedIn's connection/DM limits alike. Safer pattern:

- AI builds the candidate group list
- AI drafts the post
- A human reviews and posts manually, or the post goes through an official scheduling/API path where the platform actually offers one

This is the same reasoning behind M11/M18 keeping connection-request-volume tactics as scored experiments rather than a fixed daily number — the ceiling depends on account risk tolerance, not a universal "safe" figure.

---

## 6. SEO

| Function | Free / OSS | Paid / Proprietary |
|---|---|---|
| Keyword research | Google Keyword Planner, Google Trends, Keyword Surfer, SEO Minion, Ubersuggest (free tier — verify current daily-query cap) | Ahrefs, SEMrush |
| Technical SEO audit | Screaming Frog (free up to 500 URLs — verify current cap), SiteOne Crawler, SEO PowerSuite (free tier) | — |
| Search Console | Google Search Console (free, unlimited for owned domain) | — |
| Content, meta, schema, FAQ, internal links, content clusters | AI-drafted, human-reviewed | — |

SEO workflow: keyword → SERP analysis → outline → article draft → image → meta → FAQ → internal links → publish → index → track ranking. This is the same shape as M04–M07's intended build (still skeleton-only per `MARKETING-IMPLEMENTATION-PLAN.md`'s tracker) — once M04–M07 get built to pilot depth, this workflow is their execution detail, not a separate system.

**Local SEO (Google Business Profile):** review-reply drafts, FAQ maintenance, photo uploads, weekly posts, performance reporting — all AI-draftable, human-approved before publish.

---

## 7. Email Marketing

| Free / OSS | Notes |
|---|---|
| Mautic | Full marketing-automation suite, not just sending |
| Listmonk | Lighter weight, avoids subscriber-count cliffs some free ESPs impose — verify current terms |
| Mailtrain, Postal | Additional OSS options if Mautic/Listmonk don't fit |

Matches `MARKETING-IMPLEMENTATION-PLAN.md` §2's existing pick (Mailchimp free tier or Listmonk) — this guide adds Mautic and the other OSS options as further alternatives, doesn't replace the repo's existing choice. AI's role: subject line → email body → sequence → follow-up → performance analytics, same pattern as everywhere else in this doc — draft, then a QC gate before send.

---

## 8. The Rest of the Stack (Supporting Infrastructure)

These aren't marketing tools directly, but the raw export includes them as the infrastructure marketing automation runs on top of — kept here for completeness since dropping them would leave gaps in anyone following the ₹0–₹5,000 build.

| Category | Free / OSS Options |
|---|---|
| CRM | Odoo Community (matches repo's existing pick), ERPNext, EspoCRM |
| Project management | Plane, OpenProject, Taiga, Vikunja |
| Documentation / SOPs / Knowledge Base | BookStack, Wiki.js, Outline, Docusaurus, MkDocs |
| Cloud storage | Nextcloud (matches repo), Seafile, Syncthing |
| Password management | Vaultwarden, KeePassXC |
| Website / landing pages | WordPress + Gutenberg or Elementor Free |
| Video editing | Kdenlive, Shotcut, Olive, Blender |
| Audio editing | Audacity, Ardour |
| Screen recording | OBS Studio |
| Speech-to-text | Whisper, Faster Whisper |
| Analytics / dashboards | Matomo, Umami, Plausible (self-hosted), Google Analytics, Looker Studio, Metabase, Grafana, Superset |
| Forms | Formbricks, Form.io, OhMyForm |
| Helpdesk / live chat | Chatwoot, FreeScout, Zammad, Rocket.Chat, Mattermost |
| Browser automation | Playwright, Selenium, Puppeteer — *for internal workflow automation and permitted data collection only; not for ToS-violating actions, same caution as §5 above* |
| Monitoring | Uptime Kuma, Grafana, Prometheus |
| API testing | Bruno, Hoppscotch |
| Version control | Git, Gitea, Forgejo |
| Hosting | Docker, Portainer CE, Coolify |
| Reverse proxy | Nginx Proxy Manager, Traefik, Caddy |
| Database | PostgreSQL, MariaDB, SQLite |
| AI agent/workflow builders | Flowise, Langflow, Dify Community, Open WebUI Pipelines |
| Free stock assets | Images: Unsplash, Pexels, Pixabay · Videos: Pexels, Pixabay, Mixkit · Icons: SVG Repo, Iconify, OpenMoji · Illustrations: unDraw |

---

## 9. Marketing Tasks You Can Automate

| Task | Automation Level |
|---|---|
| Marketing Strategy | High (drafts only — decision stays human, per M01–M03) |
| Content Ideas | Very high |
| Blog Writing | Very high |
| SEO Articles | Very high |
| Social Media Captions | Very high |
| AI Images | Very high |
| AI Videos | High |
| Email Marketing | Very high |
| WordPress Publishing | Very high |
| CRM Updates | Very high |
| Analytics Reports | Very high |
| Lead Management | Very high |
| Internal Documentation | Very high |
| Content Calendar | Very high |
| Keyword Research | High |
| Technical SEO Audits | High |
| Social Media Scheduling | Very high |
| Community Replies (drafts) | High — draft only, human sends (§5) |
| Review & Approval Workflows | Very high |

Tasks that stay human regardless of tooling: final brand-quality check, complex video editing, community relationship-building conversations, influencer negotiations, platform-policy-sensitive posting/account safety (§5), and periodic strategy-direction changes.

---

## 10. Two Complete Reference Stacks

### A. Simplest to start (hosted AI, some paid tools)

n8n · Claude/ChatGPT (hosted) · Odoo Community · Notion + GitHub + Nextcloud · Canva · ChatGPT Images/Ideogram/Adobe Firefly · Veo/Runway/Kling · ElevenLabs · Publer or Metricool · WordPress · Ahrefs/SEMrush + Google Search Console · Google Analytics + Looker Studio · Mautic or Brevo

### B. ₹0–₹5,000, fully free/OSS

Ollama + Open WebUI · AnythingLLM + Wiki.js · n8n · Odoo Community · Nextcloud · Mixpost Community (or Postiz per repo §2) · Penpot + GIMP + Inkscape · ComfyUI + Stable Diffusion · ComfyUI + Wan2.1 · Piper TTS · Faster Whisper · Kdenlive · Screaming Frog Free + Google Search Console + Google Trends · Matomo + Metabase · Mautic · Chatwoot · BookStack · Docker + Portainer CE · Uptime Kuma

Full workflow (Stack B):

```
Company Knowledge (BookStack / Wiki.js / Nextcloud)
        ↓
AnythingLLM (RAG over that knowledge)
        ↓
Ollama (local model) → Open WebUI / LibreChat
        ↓
   ┌────────────┬──────────────┬──────────────────┐
   ▼            ▼              ▼
Content      SEO           Marketing
Writing    Optimization    Strategy
   └────────────┬──────────────┘
                ▼
          n8n Automation
   ┌────────┬─────────┬─────────┬─────────┐
   ▼        ▼         ▼         ▼
WordPress  Social    Email      CRM
Publishing Scheduling Marketing (Odoo)
   ▼        ▼         ▼         ▼
Facebook  LinkedIn  Mautic   Customer
Instagram X                  Data
Pinterest
                ▼
            Analytics
   (Matomo + Metabase + Looker Studio)
                ▼
         Weekly AI Reports
```

This diagram is functionally identical to the flow already described in `MARKETING-IMPLEMENTATION-PLAN.md` §2/§4 for Track M — this doc just makes the infrastructure layer underneath it explicit.

---

## 11. Cross-References

- `MARKETING-IMPLEMENTATION-PLAN.md` §2 — the repo's existing shared free/OSS tool table every Track M stage's `tools.md` points to; this guide is the expanded version of that table, not a replacement for it
- `M18 Growth Hacking Experiment Engine/resources.md` — Automation & Leverage tactic category; this guide is the infrastructure those tactics assume is already running
- `M19 Community Building` — the Facebook Groups/platform-risk caution in §5 above applies directly to M19's community-recruitment tactics
- `M09 Long-Form Content Production` / `M10 Content Repurposing and Distribution Engine` — the content layer this guide's Layer 1/4/5 tools feed into
- `M04–M07` (SEO Engine, not yet built to pilot depth) — §6 above previews the workflow those stages will formalize
- `M17 Email Newsletter and Lead Nurture` — §7 above overlaps this stage's own tool choices; reconciled, not duplicated
