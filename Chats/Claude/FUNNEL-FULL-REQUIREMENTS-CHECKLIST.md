# Funnel Ko Fully Run Karne Ke Liye — Complete Requirements Checklist

> **Short jawab: Haan.** Email/message templates (`EMAIL-TEMPLATES-and-Message-Library.md`)
> sirf ek piece hain. Funnel ko end-to-end live chalane ke liye 6 aur categories
> ki cheezein chahiye — infra, third-party accounts, data/config, missing
> automation modules, content/legal collateral, aur process/human pieces.
> Neeche sab kuch cross-check karke likha hai (5 uploaded zips: Gap_Fill,
> RECONCILED-star-topology-v6, 00_Sales_Funnel, 00_Marketing,
> Nivy-Next-Sales_and_marketing_Research).

**Legend:** ✅ already done/exists in your files · ⬜ still open/missing · 🔴 blocker (funnel is unsafe/broken without this)

---

## 1. Hosting Infra (koi bhi workflow chalne se pehle chahiye)

| Item | Status | Detail |
|---|---|---|
| VPS provision | ⬜ | Min 16GB RAM / 4vCPU / 100GB SSD (Ollama 7B ke saath chalane ke liye) — Hetzner/DigitalOcean/Contabo |
| Domain + DNS | ⬜ | Apna domain chahiye; 10 subdomains ke A-records: `n8n.`, `odoo.`, `mail.`, `files.`, `sign.`, `social.`, `bi.`, `cal.`, `wa.`, `bot.` |
| Reverse proxy + SSL | ⬜ | Caddy (auto Let's Encrypt) — sab subdomains ke liye |
| Firewall + backups | ⬜ | UFW/fail2ban + daily Postgres dump + off-site volume backup (n8n, Odoo, Nextcloud, Postal mail data) |

## 2. Self-Hosted Tool Stack (13 services — sab install + configure karne hain)

| Service | Kya karta hai | Status |
|---|---|---|
| PostgreSQL | Central `growthengine` DB — sab funnel data yahi store hota hai | ⬜ |
| n8n | Automation engine — 36 workflows ka ghar | ⬜ install, ✅ workflows already built |
| Odoo (CRM/Sales/Invoicing/Project/Website/Discuss) | CRM backbone — leads, deals, invoices, projects | ⬜ |
| Ollama | Local LLM (AI summarize/personalize/score) — no API key, but model pull chahiye | ⬜ |
| Postal | Email sending server (SPF/DKIM/DMARC pending) | ⬜ |
| Nextcloud | Client file/folder delivery | ⬜ |
| Documenso | Contract e-signature | ⬜ |
| Metabase | BI dashboards/reporting | ⬜ |
| Cal.com | Booking/scheduling | ⬜ |
| WAHA | WhatsApp gateway (real WhatsApp number chahiye) | ⬜ |
| Typebot | Website chat/lead-capture forms | ⬜ |
| Mixpost | Social media scheduling/posting | ⬜ |
| Gotenberg | HTML→PDF conversion (proposals, invoices) | ⬜ |
| Redis | Queue/cache layer | ⬜ |

**Har service ke liye:** admin account banana → API key/token generate karna →
n8n me credential save karna → **`Automation/n8n API Keys.txt`** me exact
steps already likhe hain (reuse karo, dobara mat likho).

## 3. Third-Party Paid/Free Accounts (self-hosted stack ke bahar)

Ye external services hain jo Phase 3 (Lead Intelligence) aur Marketing modules
me use hote hain — inke apne accounts/API keys chahiye:

| Service | Kis liye | Module |
|---|---|---|
| Apify (or similar scraper) | Google Maps / LinkedIn / website scraping | 3.5 Lead Extraction, 3.3 Competitor Monitor, M07 |
| Hunter.io / Snov.io | Email-finding from name+company | 3.6 Contact Discovery |
| Clearbit / Apollo.io | Firmographic enrichment | 3.7 Lead Enrichment |
| ZeroBounce / NeverBounce | Email verification (bounce-risk) | 3.9 Lead Verification |
| Google Search Console | SEO tracking/keyword data | 1.2 SEO Automation, M04 |
| Google Analytics 4 | Traffic/conversion analytics | M21 Marketing Analytics |
| LinkedIn (personal/company + automation tool) | Outreach, org organic posting | 17, 2.1, M11 |
| Payment gateway (Razorpay/Stripe/etc.) | Invoice payment webhook (2.6, 2.9) | 🔴 signature verification abhi missing |
| Social platform API keys (X/Twitter, Instagram, Facebook, YouTube) | Native posting via Mixpost | M11–M16 |
| SMS gateway (agar WhatsApp/email se alag SMS bhi chahiye) | Stage 20 SMS Outreach | Sales 20 |
| Backlink/off-page monitor tool (free-tier) | Competitor/authority tracking | 9.3, M07 |

## 4. Data & Config Setup (ek-baar ki setup, code nahi)

| Item | Status |
|---|---|
| `DB-SCHEMA-ADDENDUM-Full-Funnel.sql` run karna | ⬜ file ready hai, execute nahi hua |
| `00-MASTER-MIGRATIONS.sql` / `00-COMBINED-DB-SCHEMA-ADDENDUM.sql` (RECONCILED) run karna | ⬜ |
| Odoo custom fields + CRM stages + Won-stage ID + Activity Types | ⬜ |
| **Real pricing/rate card** (🔴 blocker) | ⬜ — abhi 2.4 Proposal module Ollama-hallucinated numbers bhej raha hai, client ko wrong price ja sakta hai |
| `odoo_partner_id` per-lead real linking (🔴 blocker) | ⬜ — 2.4/2.6/2.7 abhi generic fallback contact use kar rahe hain |
| Odoo Contacts portal-access enable | ⬜ — payment/proposal login-less links iske bina fail |
| `renewal_date` column auto-population process | ⬜ — decide + implement karna hai, warna renewal reminders/churn detection kaam nahi karega |
| Payment webhook + failed-payment webhook signature verification (🔴 blocker) | ⬜ — dono jagah abhi koi auth check nahi hai |
| Contract accept-link token verification (🔴 blocker) | ⬜ — Module 2.5 |
| Gotenberg binary-conversion wiring (manual step) | ⬜ — Module 2.4 |
| 2.6 → 2.7 Execute Workflow node manually add karna | ⬜ — bina iske onboarding auto-trigger nahi hoga |
| ICP/Persona structured store (Odoo tags/custom fields) | ⬜ — research files me content hai, system me load nahi hua |
| Hub-Dispatcher placeholder workflow IDs fill karna | ⬜ — `REPLACE_WITH_..._WORKFLOW_ID` sab jagah replace karne hain import ke baad |

## 5. Automation Modules Jo Abhi Bane Nahi Hain

`RECONCILED-star-topology-v6` me 36 workflows already ban chuke hain (Phases
0,1,2,4,5,6,7). Lekin `N8N-IMPLEMENTATION-PLAN-SalesMarketing.md` khud confirm
karta hai ki ye poore phases **abhi missing** hain:

| Phase | Kya missing hai | Kitne modules |
|---|---|---|
| **Phase 3 — Lead Intelligence & Research Foundation** | Market research digest, ICP store, competitor monitor, lead-source registry, lead extraction→scoring→segmentation pipeline, CRM field sync | 14 modules |
| **Phase 8 — Sales-Cycle Judgment Layer** | Objection lookup, call-transcript sync, needs-analysis extraction, demo scheduling automation, pricing/quote calc, deal-desk approval, CS milestone reminders | 9 modules |
| **Phase 9 — Marketing Foundation & Content Engines** | Brand/positioning store, keyword research automation, off-page tracking, editorial calendar automation, platform-specific social engines, YouTube engine, growth-experiment tracker, community/PR trackers | 10 modules |

Total: **33 modules abhi n8n workflow ke roop me exist nahi karte** — sirf plan
document me design hai. Build-order (waves) already `N8N-IMPLEMENTATION-PLAN-SalesMarketing.md`
Section 5 me di hai.

## 6. Content & Legal Collateral (templates se aage)

| Item | Status | Location |
|---|---|---|
| Email/message templates | ✅ | `Gap_Fill/EMAIL-TEMPLATES-and-Message-Library.md` |
| MSA, NDA, SOW templates | ✅ | `research/06-Trust-Compliance/` |
| Data Handling + InfoSec policy | ✅ | `research/06-Trust-Compliance/` |
| Vendor Security Questionnaire answer bank | ✅ | `research/06-Trust-Compliance/` |
| Pricing/package sheets | ✅ (draft, not final rate card) | `research/04-Positioning-Offers/` — **Ollama proposal module ke saath sync karna zaroori** |
| Messaging house / value props by ICP | ✅ | `research/04-Positioning-Offers/` |
| Pillar articles, keyword map, content calendar | ✅ | `research/05-Channels-Sales-Systems/` |
| Case study template | ✅ (template only, real case studies pending) | `research/05-Channels-Sales-Systems/Case_Study_Templates_v1.md` |
| Cold email + LinkedIn outreach sequences | ✅ | `research/05-Channels-Sales-Systems/` |
| Proposal/quote PDF design (visual, not just text) | ⬜ | Gotenberg HTML template banana hai |
| Contract template loaded into Documenso | ⬜ | Legal text ✅ hai par Documenso me template ID set nahi hua |
| Brand assets (logo, brand guide, social templates) | ⬜ | M01 Brand Foundation me strategy hai, visual assets nahi |

## 7. People / Process (automation se bahar)

| Item | Status |
|---|---|
| RACI (who owns what) | ✅ `research/01-Foundation/RACI.md` |
| KPI definitions | ✅ `research/07-Metrics-Dashboards/KPI_Definitions_Master.md` |
| Decision log | ✅ `research/08-Governance-Decision-Log/` |
| Sales rep(s) assigned in Odoo (`ODOO_SALES_USER_ID`) | ⬜ |
| Approval-threshold amounts for Deal Desk (8.8) | ⬜ |
| LinkedIn automation safety decision | ⬜ | `phase-7/7.3-linkedin-safety-review/DECISION-MEMO.md` — open decision, account-ban risk |
| End-to-end live test (S3.5, S4.9/10, S6.13, S7.4) | ⬜ | Sirf live n8n instance par ho sakta hai — files se nahi |
| Metabase dashboard build (S7.3) | ⬜ | Same — live instance chahiye |
| DNC (Do-Not-Call/Contact) list + country-wise compliance (GDPR/CAN-SPAM/etc.) | ⬜ | Country playbooks research me hain, DNC list operational nahi hai |

---

## 8. Warm-Up, Verifier & Channel-Health Tools (cross-channel)

Ye poori tarah **kisi file me consolidated nahi tha** — sirf email ke liye
scattered mentions the (`23 Deliverability`, `16 Email Outreach` modules).
LinkedIn ke liye sirf "daily limits" ka zikr hai, koi actual warm-up schedule
nahi. WhatsApp/Telegram ke liye kuch bhi nahi. Neeche channel-wise poori
list hai — jo files me mila wo ✅, baaki mera apna recommendation hai.

### 8.1 Email — domain/inbox warm-up

| Item | Status | Note |
|---|---|---|
| Mailwarm / Warmup Inbox / Instantly.ai (bundled warm-up) | ✅ mentioned in KB | `~$15-30/mo`, automated inbox warm-up |
| Google Postmaster Tools | ✅ mentioned | Free — Gmail-side reputation, set up for **every** sending domain |
| MXToolbox | ✅ mentioned | SPF/DKIM/DMARC + blacklist check |
| Dedicated sending sub-domain (not primary company domain) | ✅ mentioned as rule | e.g. `mail.nivynext.com`, not `nivynext.com` — protects core domain if burned |
| Warm-up ramp curve (volume schedule day 1→30+) | ✅ found in `Growth-Engine.zip` | See §8.4 below — real 2-week ramp + daily caps documented in `Account Safety — Platform Limits & Ban Prevention.md` |
| Email verifier | ✅ mentioned | Hunter.io, NeverBounce, ZeroBounce, or self-hosted `check-if-email-exists` (OSS, free) |

### 8.2 LinkedIn — account/outreach warm-up

**✅ Correction from earlier answer:** Ek exact schedule already maujood tha —
maine pehle miss kar diya tha. `Growth-Engine.zip` → **`Account Safety —
Platform Limits & Ban Prevention.md`** me poora daily-limit + weekly warm-up
table hai:

| Week | Connection Requests/Day | Messages/Day |
|---|---|---|
| Week 1 | 5–10 | 5–10 |
| Week 2 | 10–15 | 10–20 |
| Week 3+ | 15–20 | 20–30 |

Steady-state hard limits: connections 15–20/day (max 25), DMs 20–30/day (max
40), InMails 5–10/day (max 15). Warning signs + incident-response steps
(restriction message → stop → wait 5–7 days → escalate, never auto-create a
new account) bhi documented hain.

- **Tools:** Dux-Soup, We-Connect, Expandi, Zopto have built-in warm-up
  ramps. PhantomBuster/TexAu (already in your KB) do **not** — ramp manually.
  **Open-source option (genuinely found via search):** GitHub has small
  community LinkedIn-automation toolkits tagged `phantombuster-alternative`
  (browser-extension based, free) — lower feature depth than paid tools,
  worth evaluating if budget is tight, but community-maintained = less
  reliable long-term than a paid vendor.
- Sales Navigator subscription needed for advanced search (already noted).
- `phase-7/7.3-linkedin-safety-review/DECISION-MEMO.md` — ban-risk decision
  still open in the actual n8n build, even though the SOP-level limits exist.

### 8.3 WhatsApp — number warm-up

**✅ Also found in the same Account Safety doc:**

| Action | Safe Daily Limit |
|---|---|
| New cold contacts messaged | 20–30 (new numbers only) |
| Follow-up messages | 30–40 (existing contacts only) |
| Group messages | Avoid unless approved |

Ban triggers + response steps documented (number banned ≠ phone banned, new
SIM needed, no unapproved virtual numbers).

- WAHA is still just the gateway — doesn't enforce this schedule for you;
  your n8n workflow/team process has to.
- **No credible open-source "WhatsApp warm-up automation" tool exists** —
  confirmed via search. This stays a manual/process discipline, not a tool
  gap.

### 8.4 Email — confirmed limits (same doc)

| Action | Safe Daily Limit |
|---|---|
| Cold outreach emails | 20–30 (new account), 50 (warmed account) |
| Follow-up emails | 30–40, spaced 3+ days apart |
| Emails/hour | 10 max |

Plus: never use @gmail.com for bulk cold email, plain text not HTML, mandatory
unsubscribe line, verify before send, 2-week warm-up before >30/day.

- **Genuinely open-source options found (new, worth evaluating):**
  - **Warmbly** (github.com/warmbly/warmbly, Apache 2.0) — self-hostable
    cold-email + warmup platform; note the shared warmup *pool* itself runs
    on their cloud (needs a network of other warmed mailboxes), so
    self-hosting alone doesn't replicate the full effect on day one.
  - **BillionMail** (github.com/Billionmail/BillionMail) — fully open-source
    self-hosted mail server + newsletter/email-marketing platform, no
    monthly fees. Doesn't do "warmup simulation" specifically but gives full
    control over a dedicated sending domain, which is half the battle.
  - Still no fully-mature self-hosted equivalent of Mailwarm/Instantly's
    *automated reciprocal warm-up network* (needs many other real inboxes
    replying to each other) — that network effect is inherently hard to
    replicate solo/self-hosted.

### 8.5 Instagram/Facebook — confirmed limits (bonus, not asked but same doc)

Instagram 15–20 DMs/day (10/day new accounts, week 1), Facebook DMs 15–20/day,
don't DM inside groups.

### 8.6 Universal safety rules (from the same doc — apply everywhere)

One lead → one platform per day (don't hit the same lead on LinkedIn +
WhatsApp same day) · no automation without approval · space sends 10–20 min
apart · stop immediately on any platform warning · report same-day, don't
self-fix.

### 8.7 Calling/SMS — number health

| Item | Status |
|---|---|
| Twilio number health / carrier lookup | ✅ mentioned in KB |
| Caller-ID reputation / spam-likely flagging | ⬜ not mentioned |

### 8.8 Central health dashboard

Module 23's `sending identity health` table (email_domain/mailbox/phone_number/whatsapp_number)
is well designed. **Recommendation unchanged:** extend `type` to include
`linkedin_account` so LinkedIn gets the same rotation/retirement discipline —
it's the one channel with a real warm-up SOP but no automated health-tracking
in the actual n8n build yet.

---

## 9. Open-Source Tool Deep-Dive — What's Findable/Improvable (new, from Growth-Engine.zip)

`Growth-Engine.zip` had a file the earlier pass never saw:
**`Growth-Engine-Unified-Automation-Blueprint v.0.md`** — a properly
researched free/OSS tool map, cross-checked against a live GitHub repo of
**2,750+ ready n8n workflow templates**
(`github.com/nivyindia/all_n8n_templates_collection`). This materially
changes the "33 modules not built yet" picture from Section 5 above — a lot
of that work may already exist as an importable template, not something to
build from scratch. Worth browsing this repo **before** hand-building
Phase 3/8/9 modules.

### 9.1 OSS tools already found in your files, not yet in the deployed stack

Your actual `RECONCILED-star-topology-v6` stack uses: Odoo, Postal, Nextcloud,
Documenso, Metabase, Cal.com, WAHA, Typebot, Mixpost, Gotenberg, Ollama,
Redis, n8n. The blueprint file surfaces OSS tools that solve real gaps but
**aren't wired into that stack yet:**

| Gap | OSS tool found | Why it matters |
|---|---|---|
| Live chat / helpdesk widget | **Chatwoot** (self-hosted, free) | Current stack has no live-chat widget — Typebot is form/bot-style, not a real-time chat inbox. Chatwoot also connects WhatsApp via 360Dialog/Meta. |
| Invoice generation + payment link | **Invoice Ninja** (OSS) | Has a native n8n trigger node in the template repo — could replace/support Module 2.6's custom invoice logic |
| E-signature alternative | **DocuSeal** (AGPLv3, self-hosted) | Alternative/backup to Documenso — has an official `n8n-nodes-docuseal` community node |
| Privacy-friendly web analytics | **Matomo** | GA4 alternative if data-residency/privacy is a concern for any client vertical |
| Uptime/infra monitoring | **Uptime Kuma** | Nothing currently watches whether Postal/Odoo/n8n/Nextcloud itself is up — genuine operational blind spot |
| Internal wiki/SOP docs | **BookStack** or **Wiki.js** | Your SOPs currently live as scattered `.md`/Notion exports — a real wiki would centralize them for the team |
| Password/secrets management | **Vaultwarden** | 13 services × credentials (per your own `n8n API Keys.txt`) need a shared secrets vault, not loose notes |
| AI agent/workflow builder (no-code) | **Flowise / Langflow / Dify Community** | For AI logic too complex for a single n8n HTTP-node call to Ollama |
| Vector DB (for RAG over your own KB) | **Qdrant** | If you ever want an internal "chat with our SOPs" agent (mentioned as a goal in `AI-First-Company-Blueprint.md`) |
| Team chat (if not using Slack/Discuss) | **Rocket.Chat** | Odoo Discuss already covers this internally — only relevant if you want something dedicated |

### 9.2 Confirmed: no viable OSS replacement exists for these (don't waste time searching)

- **B2B contact database** (Apollo/ZoomInfo/Clearbit-class) — verified via
  fresh search, 2026 landscape still has no open-source contact database;
  paid tools/credits are unavoidable here, at whatever tier fits budget.
- **LinkedIn automation with a managed, ban-resistant cloud session** —
  small OSS toolkits exist on GitHub but are hobby-maintained; the
  paid category (Dux-Soup/Expandi/We-Connect) exists specifically because
  LinkedIn's anti-automation detection changes faster than a volunteer repo
  can track.
- **Reciprocal email warm-up network** (Mailwarm/Instantly-class) — the
  mechanism itself needs many other real, active mailboxes to send
  to/reply-from; a solo self-hosted tool can't replicate that network
  effect. Warmbly (above) is the closest OSS attempt but still leans on a
  cloud-hosted shared pool for full effect.

### 9.3 Practical next step

Before building any of the 33 "not yet built" modules from Section 5, grep
`nivyindia/all_n8n_templates_collection` for the stage first — the Unified
Automation Blueprint file already did this for the original 12-stage legacy
funnel and found working templates for ~10 of 13 previously-flagged gaps.
Same exercise against the current 54-stage/22-module numbering would likely
cut real build time significantly.

**Telegram note (unchanged from before):** checked across all files again —
still only appears as an internal team notification channel, not a
lead-outreach channel. No warm-up needed unless you decide to add it as a
new outbound channel.

---

## 10. Open-Source Email Validation + Multi-Mailbox Sending (specific follow-up)

### 10.1 Open-source email validation/verification tools

Your own KB already points to `check-if-email-exists` repeatedly — confirmed
current and real. Full picture, verified fresh:

| Tool | Language/Type | What it checks | Self-host? |
|---|---|---|---|
| **Reacher** (formerly `check-if-email-exists`) | Rust, CLI + REST API | Syntax + MX + SMTP mailbox-exists check, disposable/catch-all detection | ✅ Docker self-host, or their hosted free tier |
| **Truemail** | Ruby gem, self-hostable as an API | Regex + DNS + SMTP validation, actively maintained | ✅ |
| **python-email-validator** | Python library | Syntax + deliverability checks | ✅ (library, not a standalone service) |
| **email-validator-js** | TypeScript/Node | MX + SMTP + disposable/free-provider detection | ✅ |
| **validate-email** (PHP) | PHP script | Wraps multiple commercial verification APIs in one script — useful if you want to mix free self-checks with a paid API fallback for the "risky" bucket | ✅ |

**Recommendation for your stack specifically:** Reacher is the best fit —
it's a proper REST API (not just a library), Docker-deployable, and n8n can
call it with a plain HTTP Request node exactly like it currently calls
ZeroBounce/NeverBounce in Module 10 (Lead Verification). Swap-in, not a
redesign — same input (email) → same output shape (valid/risky/invalid),
just self-hosted and free instead of pay-per-verify. **Caveat:** SMTP-level
checks can get rate-limited or blocked by some mail providers (Gmail/Outlook
increasingly throttle unknown IPs doing verification pings) — for very
large lists, plan on Reacher catching the easy majority and routing only the
genuinely ambiguous "risky" ones to a paid API as a fallback (same pattern
your `validate-email` PHP tool above already builds in).

### 10.2 Sending from many email IDs (mailbox rotation) — the honest answer

**There is no free/OSS tool that does what Instantly.ai/Smartlead/Saleshandy
do out of the box** (rotate sends across dozens of warmed mailboxes with a
polished UI) — confirmed via fresh search, this is genuinely a paid-tool
category in 2026, all the players (Mailforge, Infraforge, Maildoso, HotHawk,
Saleshandy, Salesforge) are commercial.

**But you don't actually need a separate tool — you already have the two
pieces, they just need to be connected:**

1. **Postal** (already in your stack) already supports multiple sending
   domains/mailboxes under one server — the "many email IDs" infra problem
   is already solved by what you have.
2. **The rotation logic** is what's missing, and that's a straightforward
   **n8n build**, not a new tool:
   - A Postgres table of active sending identities (this can literally
     extend Module 23's existing `sending identity health` table — add a
     `daily_sent_count` and `last_used_at` column)
   - A small Code node in your outreach workflow (2.1 Multichannel Outreach)
     that picks the identity with the lowest `daily_sent_count` today (or
     round-robins), checks it's under its cap and not in `warning`/`suspended`
     status, sends via that identity's Postal credential, then increments
     the counter
   - Reset `daily_sent_count` to 0 on a scheduled midnight cron
   - This is maybe 20-30 lines of Code-node logic — genuinely small, and it
     plugs directly into your existing Module 23 health-tracking design
     instead of bolting on a separate paid platform

**Closest all-in-one OSS options if you'd rather not build it yourself:**

| Tool | What it gives you | Caveat |
|---|---|---|
| **Warmbly** (github.com/warmbly/warmbly, Apache 2.0) | Self-hostable sending + rotation + basic CRM + inbox, built specifically for this use case | The shared warm-up *pool* still needs their cloud — self-hosted alone won't warm mailboxes the same way |
| **BillionMail** (fully OSS mail server + campaigns) | Full control, no fees, unlimited sending | Built for newsletter/marketing-blast sending, not 1:1 personalized cold-sequence rotation — would need adaptation |

**Not a fit for this specific need (flagging so you don't waste time):**
phpList / listmonk / Mailtrain — all excellent OSS tools, but they're
**bulk newsletter** senders (one email → many recipients), not **cold-outreach
sequencers** (personalized email → one recipient at a time, rotated across
sender identities). Different job.

---

## Priority Order — Agar Sabse Pehle Kya Karna Hai Pooche

1. **VPS + DNS + Postgres + n8n + Odoo + Ollama** (core infra, sab kuch iske upar khada hai)
2. **Postal (email sending) + domain SPF/DKIM/DMARC** — bina iske koi bhi outreach/template bhej nahi sakte
3. **Import 36 existing workflows in the documented order**, wiring placeholder IDs fill karo
4. **🔴 3 blockers close karo:** real pricing rate card, payment/contract webhook signature verification, `odoo_partner_id` real linking — ye sab client-facing risk hain
5. Cal.com + WAHA + Typebot (lead-capture/booking ke liye zaroori)
6. Documenso + Metabase (baad me, Phase 2 ke later modules ke liye)
7. Phase 3 (Lead Intelligence pipeline) — highest ROI naya build, existing patterns reuse karta hai
8. Phase 8 aur 9 — baad me, lower urgency

---

*Source files cross-checked: `Gap_Fill.zip` (N8N-IMPLEMENTATION-PLAN, EMAIL-TEMPLATES, DB-SCHEMA), `RECONCILED-star-topology-v6.zip` (PHASE-0/PHASE-A reports, taxonomy, 36 workflows), `00_Marketing.zip` (DEPLOYMENT-GUIDE, n8n API Keys, README blockers), `00_Sales_Funnel.zip` (N8N-AUTOMATION-INDEX, IMPLEMENTATION-PLAN), `Nivy-Next-Sales_and_marketing_Research.zip` (Trust-Compliance, Positioning-Offers, Metrics, RACI).*
