# 📅 VOL 2 — Phased Execution Plan (Phase 0 → Phase 4)

> **The complete 90-day build plan.** This volume covers every phase of execution from foundation setup (Phase 0) through full AI pipeline (Phase 3) and international expansion (Phase 4). Do not skip ahead — each phase depends on the last.
> 

---

# 🗺️ Page Index

1. Phase 0 — Foundation (Days 1–3)
2. Phase 1 — Manual Hustle (Days 4–30)
3. Phase 2 — Semi-Automation (Days 31–60)
4. Phase 3 — Full AI Pipeline (Days 61–90)
5. Phase 4 — Scale & Expand (Day 90+)
6. Metadata & Search Tags

---

# ✅ 1. Phase 0 — Foundation (Days 1–3)

**Goal:** Get the minimum infrastructure live so you can start generating conversations on Day 1. No automation yet. No complexity. Just the basics.

| Task | Tool | Time |
| --- | --- | --- |
| Create free Slack workspace named “Nivy Alliance” | [Slack.com](http://Slack.com) | 20 mins |
| Create 6 channels: #start-here, #introductions, #opportunities, #member-spotlight, #resources, #general | Slack | 10 mins |
| Write and pin the welcome message in #start-here | Slack | 10 mins |
| Create onboarding form (5 questions) | [Tally.so](http://Tally.so) (free) | 20 mins |
| Write your first 5 LinkedIn enquiry post drafts | Notion / Docs | 30 mins |
| Identify 10 Facebook groups to post in (UK Business, Digital Marketing UK, Startups UK, etc.) | Facebook | 15 mins |
| Set up a dedicated Gmail for Nivy Alliance outreach | Gmail | 10 mins |

**Phase 0 Exit Criteria:** Slack live ✓ | Form live ✓ | 5 posts drafted ✓ | Gmail ready ✓

---

# 🔥 2. Phase 1 — Manual Hustle (Days 4–30)

**Goal:** Generate first 5 paying clients and first 20 Slack members through daily manual execution. No automation yet — understand the process before automating it.

**Daily Routine (90 minutes, Monday–Friday):**

| Time | Task | Platform |
| --- | --- | --- |
| 9:00 AM | Post 1 enquiry post | LinkedIn |
| 9:15 AM | Post in 2 Facebook / WhatsApp groups | Facebook / WhatsApp |
| 9:30 AM | Manually submit 10 contact forms (Google Maps → find companies → submit form) | Browser |
| 10:00 AM | Reply to every DM and comment from last 24 hours | All platforms |
| 11:00 AM | Send WhatsApp broadcast to 10–15 saved contacts | WhatsApp |
| 2:00 PM | Check all platforms again. DM everyone who engaged. | All |
| 5:00 PM | Log all conversations (Hot / Warm / Cold) in Lead Tracker | Notion |

**Qualification Rule:**

- **HOT** (needs your services now) → Book a call within 24 hours → Pitch accounting / marketing packages
- **WARM** (good business, not urgent) → Invite to Nivy Alliance Slack → Nurture for 30–45 days → Convert
- **COLD** (wrong fit) → Log and ignore

**Phase 1 Targets:**

| Metric | Week 1 | Week 2 | Week 3 | Week 4 |
| --- | --- | --- | --- | --- |
| Enquiry posts | 5 | 5 | 5 | 5 |
| Contact forms | 50 | 50 | 50 | 50 |
| DM conversations | 10 | 15 | 20 | 25 |
| Calls booked | 1–2 | 2–3 | 3–4 | 4–5 |
| Slack members | 3–5 | 8–12 | 15–18 | 20–25 |
| Clients closed | 0 | 0–1 | 1–2 | 2–3 |

**Phase 1 Exit Criteria:** 1+ paying client ✓ | 20+ Slack members ✓ | Process fully understood ✓

---

# 🤖 3. Phase 2 — Semi-Automation (Days 31–60)

**Goal:** Automate the high-volume, repetitive tasks so you go from 10 contact forms/day to 100+/day without extra effort. Keep human touch for DMs and calls.

## 2A — Contact Form Automation (n8n + Puppeteer)

- n8n workflow scrapes Google Maps for target businesses by city and category
- Puppeteer auto-fills and submits their website contact forms
- Volume: 50–100 submissions per day, unattended
- Cost: Free (n8n self-hosted) or $20/month (n8n cloud)

## 2B — Gmail Reply Detection (n8n)

- n8n monitors your Nivy Gmail inbox
- When a reply arrives → automatically tags it in Notion CRM
- Sends you a Slack or WhatsApp notification instantly
- You only need to check your notifications — not refresh Gmail manually

## 2C — Tally Form → Slack Auto-Invite (n8n)

- When someone submits the Alliance onboarding form on Tally
- n8n automatically sends them the Slack invite link via email
- Tags them in Notion CRM as JOINED
- Posts their intro in #introductions automatically

**Tools needed for Phase 2:**

| Tool | Purpose | Cost |
| --- | --- | --- |
| n8n (cloud or self-hosted) | All automation | Free / $20/month |
| Puppeteer (via n8n) | Contact form submission | Free |
| Gmail API | Reply detection | Free |
| [Tally.so](http://Tally.so) | Onboarding form | Free |
| Notion API | CRM database | Free |

**Phase 2 Targets:**

| Metric | Month 2 Total |
| --- | --- |
| Contact forms/day (automated) | 50–100 |
| DM conversations/week | 40+ |
| Calls booked/week | 8–10 |
| New Slack members/week | 15–25 |
| Paying clients total | 5–8 |
| Monthly revenue | $2,000–$5,000 |

**Phase 2 Exit Criteria:** Automation live ✓ | 50+ Slack members ✓ | 5+ clients ✓ | Revenue covering costs ✓

---

# 🧠 4. Phase 3 — Full AI Pipeline (Days 61–90)

**Goal:** Add AI enrichment and qualification so the entire funnel from scrape to Slack invite runs without you. You only handle calls and closing.

**The Full Automated Pipeline:**

```
STEP 1 — SCRAPE
n8n + Apify scrapes Google Maps, Clutch.co, LinkedIn company pages
Output: Company name, website, email, country, industry, size

STEP 2 — AI ENRICHMENT
Claude API generates personalised contact form message + lead score (A/B/C)

STEP 3 — AUTO OUTREACH
n8n submits personalised message to contact form OR sends cold email
Volume: 100–200 per day

STEP 4 — REPLY DETECTION & AI QUALIFICATION
Gmail reply detected → Claude reads the reply and decides:
• HOT → auto-sends your Calendly booking link
• WARM → auto-sends Alliance invite email
• COLD → archives, stops follow-up

STEP 5 — FOLLOW-UP SEQUENCE (if no reply)
Day 3: Follow-up 1 sent automatically
Day 7: Follow-up 2 sent automatically
Day 14: Marked cold, archived

STEP 6 — COMMUNITY ONBOARDING
Warm leads get automated email with Tally form link
On form submit → Slack invite sent automatically

STEP 7 — CRM LOGGING
Every lead, every action, every status change logged in Notion automatically

STEP 8 — WEEKLY COMMUNITY CONTENT
n8n posts scheduled content to Slack: Monday opportunities, Wednesday resources, Friday networking
```

**Additional tools for Phase 3:**

| Tool | Purpose | Cost |
| --- | --- | --- |
| Claude API / OpenAI | Message personalisation + reply qualification | $10–30/month |
| Apify | LinkedIn + Google Maps scraping | $49/month or free tier |
| Calendly | Auto booking link | Free |

**Phase 3 Targets:**

| Metric | Month 3 Total |
| --- | --- |
| Automated outreach/day | 100–200 |
| Slack members | 100+ |
| Paying clients | 8–12 |
| Monthly revenue | $5,000–$12,000 |
| Referrals from community | 3–5/month |
| Your daily active work | 1–2 hours (calls + closing only) |

**Phase 3 Exit Criteria:** Full pipeline automated ✓ | 100+ members ✓ | 8+ clients ✓ | System runs without daily manual input ✓

---

# 🌍 5. Phase 4 — Scale & Expand (Day 90+)

**Goal:** Once UK is working, replicate the same system for USA or UAE.

- Clone the entire n8n automation for a new country/niche
- Hire one part-time community manager for Slack moderation
- Begin LinkedIn content marketing to supplement enquiry method
- Introduce a paid “Premium Member” tier in the Alliance (£99–£199/month for priority matching)
- Explore partnerships with CPA firms and marketing agencies who can refer clients to you

---

# 🗺️ Navigation

- ← Back to: **VOL 1 — Vision, Core Idea & Workspace Structure**
- → Next: **VOL 3 — KPI Dashboard & Platform ROI**
- → Master: **MASTER INDEX**

---

# 🔍 Metadata & Search Tags

**Project:** Nivy Alliance

**Document type:** Execution Plan

**Volume:** 2 of 7

**Last updated:** 10 May 2026

**Status:** Active — Phase 0 in progress

**Owner:** Abhi

**Tags:** nivy alliance, phase 0, phase 1, phase 2, phase 3, phase 4, execution plan, 90-day plan, manual hustle, automation, AI pipeline, scale, daily routine, slack members, paying clients

**Search keywords:** nivy alliance phases, 90 day plan, what to do each day, phase 0 checklist, phase 1 daily routine, phase 2 automation, phase 3 AI, phase 4 expansion, execution roadmap