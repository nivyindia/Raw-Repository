# 🧠 Phase 3 — Full AI Pipeline (Days 61–90)

> This is the full end-to-end automated system. Once live, the pipeline runs from scraping to Slack invite with minimal manual input. Your only job is handling calls and closing clients.
> 

---

# The Complete Pipeline (8 Steps)

```
STEP 1 — SCRAPE
↓
STEP 2 — AI ENRICHMENT
↓
STEP 3 — AUTO OUTREACH
↓
STEP 4 — REPLY DETECTION & AI QUALIFICATION
↓
STEP 5 — FOLLOW-UP SEQUENCE (if no reply)
↓
STEP 6 — COMMUNITY ONBOARDING
↓
STEP 7 — CRM LOGGING
↓
STEP 8 — WEEKLY COMMUNITY CONTENT
```

---

# Step 1 — Scrape

**What it does:** Collects company data from multiple sources automatically.

**Tools:** n8n + Apify

**Sources:**

- Google Maps (city + category searches)
- [Clutch.co](http://Clutch.co) (UK/USA agencies, filtered by rating and size)
- LinkedIn company pages (via Apify LinkedIn Company Scraper actor)

**Output per company:**

- Company name
- Website URL
- Email (if publicly listed)
- Country and city
- Industry
- Employee count (approximate)
- LinkedIn company URL

**n8n Setup:**

- Add an Apify node → select "Google Maps Scraper" actor
- Input: list of search queries (e.g. "accounting firm London", "marketing agency Manchester")
- Schedule: run every morning at 6 AM, collect 200 new companies
- Output: pipe results into a Google Sheet or Notion database as the raw lead pool

---

# Step 2 — AI Enrichment

**What it does:** Claude API reads each company profile and generates a personalised outreach message + lead score.

**Tools:** n8n + Claude API (claude-sonnet-4-20250514)

**n8n Setup:**

- Add an HTTP Request node pointing to `https://api.anthropic.com/v1/messages`
- For each scraped company, send this prompt:

```
You are an outreach specialist for Nivy Alliance, a private business exchange network.

Company: [Company Name]
Industry: [Industry]
Location: [City, Country]
Website: [URL]

Write a short, human-sounding contact form message (under 100 words) that:
1. Mentions their specific industry and location naturally
2. Explains we run a private business network
3. Asks for a 15-minute call
4. Does NOT sound like a template

Also give this lead a score: A (high fit), B (medium fit), or C (low fit) based on whether they are likely to need accounting, tax, or digital marketing services.

Respond in JSON: {"message": "...", "score": "A/B/C", "reasoning": "..."}
```

**Output:** Personalised message + lead score for every company in the pool

**Filter:** Only submit to A and B scored companies. Skip C leads.

---

# Step 3 — Auto Outreach

**What it does:** Submits the AI-personalised message to company contact forms OR sends cold email if a direct email was found.

**Tools:** n8n + Puppeteer (contact forms) or Gmail SMTP (email)

**Contact Form Path:**

- Same Puppeteer workflow as Phase 2 (Workflow 2A)
- Now uses the AI-generated personalised message instead of fixed template
- Volume: 100–200 submissions/day

**Email Path (if direct email found):**

- n8n Gmail node sends personalised cold email
- From: [nivyalliance@gmail.com](mailto:nivyalliance@gmail.com)
- Subject line rotated from a list of 5 tested variants
- Volume: up to 500/day via Google Workspace

**Sending Rules (to avoid spam flags):**

- Randomise send time: between 8 AM–5 PM target timezone
- Randomise delay between sends: 30–120 seconds
- Rotate between 2–3 Gmail accounts if volume exceeds 200/day
- Stop sending to any domain that bounces twice

---

# Step 4 — Reply Detection & AI Qualification

**What it does:** When a reply arrives, Claude reads it and automatically decides whether to send a booking link, an Alliance invite, or to archive the lead.

**Tools:** n8n Gmail Trigger + Claude API

**n8n Setup:**

- Gmail Trigger fires when new email arrives (from Phase 2 Workflow 2B)
- Send reply content to Claude API with this prompt:

```
You are qualifying a sales lead for Nivy Alliance.

The lead received our outreach message and replied. Read their reply and classify them:

HOT: They expressed interest in accounting, tax, bookkeeping, or digital marketing services. They have budget signals. They want to connect.

WARM: They're interested in the business network / Alliance concept. They want more info. They're a legitimate business.

COLD: They're not interested, asked to be removed, or the reply is irrelevant/spam.

Reply content:
[REPLY TEXT]

Respond in JSON: {"classification": "HOT/WARM/COLD", "reasoning": "...", "suggested_response": "..."}
```

**Actions Based on Classification:**

| Classification | Automatic Action |
| --- | --- |
| HOT | Send Calendly link via Gmail automatically + flag you in Slack |
| WARM | Send Alliance invite email automatically + log in Notion as SLACK INVITED |
| COLD | Archive in Notion as COLD, stop all follow-up |

---

# Step 5 — Follow-Up Sequence (If No Reply)

**What it does:** Automatically sends follow-up messages to companies that received outreach but haven't replied.

**Tools:** n8n + Gmail

**Sequence:**

| Day | Message | Action |
| --- | --- | --- |
| Day 0 | Initial outreach sent | Status: OUTREACH SENT |
| Day 3 | Follow-up 1 sent | Status: FOLLOW-UP 1 |
| Day 7 | Follow-up 2 sent | Status: FOLLOW-UP 2 |
| Day 14 | Mark cold, stop | Status: COLD — NO REPLY |

**Follow-Up 1 Template (Day 3):**

```
Subject: Re: Partnership Enquiry — Nivy Alliance

Hi [Name],

Just following up on my message earlier this week.

We're putting together a small group of trusted [industry] businesses for our UK network — I thought [Company Name] would be a strong fit.

Would a quick 10-minute call work this week?

[Calendly Link]

[Your Name]
```

**Follow-Up 2 Template (Day 7):**

```
Subject: Last note — Nivy Alliance

Hi [Name],

I don't want to clutter your inbox, so this is my last message.

If the timing isn't right — no problem at all. I'll check back in a couple of months.

If you're open to a quick call, here's my link: [Calendly]

[Your Name]
```

---

# Step 6 — Community Onboarding

**What it does:** Warm leads are automatically sent the Alliance onboarding email, directing them to the Tally form, which triggers the Slack invite (from Phase 2 Workflow 2C).

**Alliance Invite Email (Auto-Sent to WARM leads):**

```
Subject: Invitation — Nivy Alliance Private Business Network

Hi [Name],

Thanks for your interest.

Nivy Alliance is a small, invite-only network where verified UK businesses exchange real outsourcing requirements and connect with trusted suppliers and partners.

Members:
• Post what they need (marketing, accounting, IT, logistics)
• Get matched with verified providers
• Build long-term referral relationships

To apply for membership, complete this short form (takes 2 minutes):
[Tally Form Link]

Once submitted, you'll receive your Slack invite within 24 hours.

Nivy Alliance Team
```

---

# Step 7 — CRM Logging

**What it does:** Every lead, every action, every status change is automatically logged in the Notion Lead Tracker.

**Status Flow:**

```
SCRAPED → ENRICHED → OUTREACH SENT → FOLLOW-UP 1 → FOLLOW-UP 2 → 
RESPONDED → [HOT: CALL BOOKED] / [WARM: SLACK INVITED] / [COLD: ARCHIVED]
```

**Fields logged automatically per lead:**

- Company Name, Website, Industry, City, Country
- Lead Score (A/B/C from AI enrichment)
- Source (Google Maps / Clutch / LinkedIn)
- Outreach Date, Follow-Up Dates
- Reply Date, Reply Classification
- Current Status
- Calendly booking date (if HOT)
- Slack joined date (if WARM)

---

# Step 8 — Weekly Community Content (Auto-Posted to Slack)

**What it does:** n8n posts scheduled content to Slack channels automatically, keeping the community active without daily manual effort.

**Schedule:**

| Day | Time | Channel | Content |
| --- | --- | --- | --- |
| Monday | 9:00 AM | #opportunities | Pull 1–2 recent requirements from Notion → post as opportunity |
| Wednesday | 11:00 AM | #resources | Rotate through a saved list of resource posts |
| Friday | 10:00 AM | #general | Rotate through networking prompt templates |

**n8n Setup:**

- Use Schedule Trigger node (Monday 9 AM, Wednesday 11 AM, Friday 10 AM)
- Slack node: post to the relevant channel using Slack Bot token
- For #opportunities: query Notion for leads with Status = "SLACK INVITED" who posted a requirement → format as opportunity post

---

# Phase 3 Tool Cost Summary

| Tool | Plan | Monthly Cost |
| --- | --- | --- |
| n8n Cloud | Pro | $50/month |
| Apify | Starter | $49/month |
| Claude API | Pay-per-use | $15–30/month |
| Google Maps API | Pay-per-use | $10–20/month |
| Google Workspace | Business Starter | $6/user/month |
| Calendly | Free | $0 |
| [Tally.so](http://Tally.so) | Free | $0 |
| Notion | Free | $0 |
| **Total** |  | **~$130–155/month** |

> At 8+ paying clients generating $5k+/month, this cost is well under 3% of revenue.
> 

---

# Phase 3 Exit Criteria

- [ ]  Full 8-step pipeline live and running daily
- [ ]  100–200 automated outreach submissions/day
- [ ]  AI qualification routing replies correctly (HOT / WARM / COLD)
- [ ]  Follow-up sequences firing on schedule
- [ ]  Slack community receiving automated weekly posts
- [ ]  100+ Slack members
- [ ]  8+ paying clients
- [ ]  Your daily active work reduced to 1–2 hours (calls + closing only)

**When all done → Phase 4: Scale to USA or UAE using same system**