# 🚀 Nivy Digital — International Outreach Automation System

> **Purpose:** A complete, phased system to automate B2B outreach across USA, UK, Canada, Australia & UAE using open-source and free tools — built for Nivy Advisory and Nivy Next services.
> 

---

## 📋 Quick Navigation

| Section | What's Inside |
| --- | --- |
| Phase 0 | Foundation & Stack Setup |
| Phase 1 | Lead Sourcing & Scraping |
| Phase 2 | Lead Qualification & Enrichment |
| Phase 3 | AI Message Generation |
| Phase 4 | Multi-Channel Outreach |
| Phase 5 | Follow-Up Automation |
| Phase 6 | Response Handling & CRM |
| Phase 7 | Call Booking & Proposal Sending |
| Phase 8 | Tracking, QA & Optimization |
| Risk Register | All risks + mitigations |

---

## 🧰 MASTER TECH STACK (Free / Open Source First)

| Function | Tool | Cost |
| --- | --- | --- |
| Automation Engine | n8n (self-hosted) | Free |
| Email Outreach | Mautic (self-hosted) | Free |
| Lead Storage | Google Sheets | Free |
| CRM | Twenty CRM (open source) | Free |
| LinkedIn Automation | Phantombuster (free tier) | Free tier |
| Email Validation | Reoon / MillionVerifier | Paid (low cost) |
| AI Personalization | OpenAI API / Groq (free tier) | Free tier |
| Email Warm-Up | Mailwarm / Lemwarm | Paid (low cost) |
| Domain Infra | Google Workspace (secondary domain) | ~$6/mo |
| Scraping | Apify (free tier) / Clay free | Free tier |
| Google X-Ray | Manual / n8n HTTP node | Free |
| Calendar Booking | [Cal.com](http://Cal.com) | Free |
| Proposal Sending | PandaDoc free / Notion | Free |

---

## 📅 PHASE 0 — FOUNDATION SETUP (Week 1)

### 🎯 Goal

Build the infrastructure before sending a single message.

### Step-by-Step

**Step 1: Domain & Email Infrastructure**

- Buy a secondary domain (e.g. `nividigitalhq.com` or `nivityadvisory.io`)
- Create 2–3 sending email accounts on this domain
- Connect to Google Workspace
- Set up SPF, DKIM, DMARC records (essential for deliverability)
- Start email warm-up using Mailwarm or Lemwarm — minimum 3 weeks before cold outreach

**Step 2: Install n8n**

- Self-host n8n on a VPS (e.g. Hetzner €4/mo or Railway free tier)
- Or use [n8n.cloud](http://n8n.cloud) free trial
- Connect n8n to Google Sheets, OpenAI, Hunter API, Apollo (free tier)

**Step 3: Install Mautic**

- Self-host Mautic on same VPS (handles email sequences, tracking)
- Connect Mautic SMTP to your warmed domain
- Create email templates for each target market (USA, UK, Canada, AU, UAE)

**Step 4: Set Up Google Sheets CRM**

- Create Master Lead Sheet with columns:
    - Company Name, Website, Industry, Country, Size
    - Decision Maker Name, Role, LinkedIn URL
    - Email, Email Status, Phone
    - Lead Source, Date Scraped, Assigned VA
    - Status (New / Contacted / Replied / Meeting / Closed)
    - Personalization Notes, Last Activity

**Step 5: Install Twenty CRM (optional upgrade)**

- Open-source alternative to HubSpot
- Sync with Google Sheets via n8n

---

## 📅 PHASE 1 — LEAD SOURCING & SCRAPING (Week 2–3)

### 🎯 Goal

Build a clean database of 500–1,000 qualified leads per month per market.

### 🧠 Data Model — What to Collect

**Company Data**

- Company Name, Website, Industry, Location, Size, Revenue (optional)

**Decision Maker Data**

- Full Name, Role (Founder / CEO / CFO / Marketing Head)
- LinkedIn Profile URL, Company LinkedIn

**Contact Data**

- Work email (non-generic, no info@ or hello@)
- Email status (Valid / Risky / Catch-all)
- Phone (optional)

**Personalization Data**

- LinkedIn recent activity (posts, comments)
- Company recent updates (funding, hiring, news)
- Website insight (what service they offer, tech stack)

**System Data**

- Lead source, Date scraped, Assigned VA, Status

---

### 🔍 Source 1: Google X-Ray Search (Free)

**What it is:** Using Google search operators to find decision-makers.

**Search formulas:**

```
site:linkedin.com/in "CEO" "accounting firm" "United States"
site:linkedin.com/in "Founder" "digital marketing agency" "UK"
site:clutch.co "accounting" "USA" CEO contact
"@gmail.com" OR "@company.com" CEO "CPA firm" site:linkedin.com
```

**n8n Automation for X-Ray:**

1. n8n Schedule Trigger (daily)
2. HTTP Request node → Google Custom Search API (free 100 queries/day)
3. Parse results → extract LinkedIn URLs
4. Store in Google Sheets → "Raw Leads" tab

---

### 🔍 Source 2: LinkedIn Scraping (PhantomBuster)

**Steps:**

1. Set up PhantomBuster free account
2. Use "LinkedIn Search Export" phantom
3. Search: `CEO accounting firm New York` → export 100 results
4. Download CSV → upload to Google Sheets
5. n8n watches for new rows → triggers enrichment flow

**LinkedIn Search URLs to target:**

- `site:linkedin.com "CPA" "Founder" "Chicago"`
- Sales Navigator (if available): `Title: CEO, Industry: Accounting, Location: USA`

**Safety rules for LinkedIn:**

- Max 50–80 profile visits/day
- Use human-like delays (2–5 min between actions)
- Never scrape and connect same day
- Use a secondary LinkedIn account for scraping

---

### 🔍 Source 3: Google Maps (Local Business Leads)

**Best for:** Small–mid local businesses in USA, UK, Canada

**Steps:**

1. Use Apify "Google Maps Scraper" actor (free tier = 100 results)
2. Input: `"accounting firm" New York`
3. Output: Business name, address, phone, website, rating
4. Feed into n8n → find owner email via Hunter API

---

### 🔍 Source 4: Directories (Clutch, Crunchbase, Apollo)

[**Clutch.co](http://Clutch.co):** Agencies with reviews, decision maker names visible

[**Apollo.io](http://Apollo.io) free tier:** 50 contacts/month with emails

[**Hunter.io](http://Hunter.io) free:** 25 email searches/month

**Crunchbase:** Funded startups → high-intent leads

**n8n Flow for Apollo:**

1. HTTP Request → Apollo `/people/search` endpoint
2. Filter by: title contains `CEO OR Founder OR CFO`, location = `United States`
3. Extract: name, email, company, LinkedIn
4. Push to Google Sheets

---

### 🤖 n8n Master Scraping Workflow

```
[Schedule Trigger: Daily 9am]
         ↓
[Set ICP Parameters]
(Country, Industry, Role, Company Size)
         ↓
[Branch: Source Selector]
  ├── Apollo API → Fetch companies + contacts
  ├── Hunter API → Find emails by domain
  ├── Apify Actor → Google Maps / website scrape
  └── Google Custom Search → X-Ray LinkedIn
         ↓
[Merge Results]
         ↓
[Deduplication Check]
(Compare email vs. existing Google Sheet)
         ↓
[Email Validation]
(Reoon API or NeverBounce)
  ├── Valid → Keep
  ├── Risky → Flag, keep with caution
  └── Invalid → Discard
         ↓
[AI Personalization]
(OpenAI: generate 1 custom intro line per lead)
         ↓
[Write to Google Sheets]
"Clean Leads" tab
```

---

## 📅 PHASE 2 — LEAD QUALIFICATION (Week 3)

### 🎯 Goal

Score leads before outreach. Only contact high-fit prospects.

### ICP Scoring Matrix (in Google Sheets)

| Criteria | Score |
| --- | --- |
| Decision maker is Founder/CEO/CFO | +3 |
| Company size 5–50 employees | +2 |
| Located in target country | +2 |
| Email is valid (not catch-all) | +2 |
| Has LinkedIn activity in last 30 days | +2 |
| Industry matches (accounting, agency, etc.) | +3 |
| Company has website | +1 |
| **Total possible** | **15** |

**Score 10+:** Priority outreach

**Score 7–9:** Secondary outreach

**Below 7:** Archive

**n8n Qualification Flow:**

1. Read new lead from Google Sheets
2. Check each criteria via conditional nodes
3. Calculate score using Math node
4. Write score + tier (A/B/C) back to sheet
5. Move A-tier leads to "Ready to Contact" tab

---

## 📅 PHASE 3 — AI MESSAGE GENERATION (Week 3–4)

### 🎯 Goal

Create personalized, human-sounding messages at scale.

### n8n + OpenAI Flow

**Step 1:** Read lead data from Google Sheets

**Step 2:** Build prompt in n8n

**Step 3:** Send to OpenAI API (GPT-4o-mini = cheap)

**Step 4:** Store generated message in sheet column

### Prompt Template (LinkedIn)

```
You are a B2B outreach specialist for Nivy Digital.
Write a short, personalized LinkedIn connection note (under 300 chars) for:
- Name: {{name}}
- Role: {{role}}
- Company: {{company}}
- Industry: {{industry}}
- Recent LinkedIn activity: {{linkedin_activity}}

Tone: Professional, not salesy. Mention something specific.
Do NOT use generic phrases like "I came across your profile."
Output: Only the message text, no quotes.
```

### Prompt Template (Cold Email)

```
Write a cold email for a B2B service company.
Target: {{name}}, {{role}} at {{company}} ({{industry}}, {{country}})
Our service: {{service_offered}}
Personalization hook: {{personalization_note}}

Structure:
- Line 1: Specific, personalized opener (not generic)
- Line 2-3: Problem we solve for their industry
- Line 4: One-line proof/result
- CTA: Single, low-commitment ask

Tone: Conversational, peer-to-peer. Max 120 words.
```

---

## 📅 PHASE 4 — MULTI-CHANNEL OUTREACH (Week 4–5)

### 🎯 Goal

Contact leads across LinkedIn + Email in a coordinated sequence.

### ✅ The Golden Sequence

```
Day 1  → LinkedIn Connection Request (personalized note)
Day 3  → If connected: LinkedIn DM (value message)
Day 5  → Cold Email #1 (personalized)
Day 8  → LinkedIn follow-up DM (if no reply)
Day 12 → Cold Email #2 (different angle)
Day 16 → Final LinkedIn message OR Email #3 (breakup)
Day 20 → Archive if no response
```

---

### 📧 Email Outreach via Mautic

**Setup Steps:**

1. Connect Mautic to your warmed sending domain
2. Create a Segment: "USA CPA Outreach — May 2026"
3. Import leads from Google Sheets (Mautic has Google Sheets sync via n8n)
4. Create Campaign in Mautic:
    - Email 1 → Day 0
    - Wait 7 days → Email 2
    - Wait 4 days → Email 3 (breakup)
5. Set unsubscribe footer (legally required for USA/UK/Canada)
6. Track opens, clicks in Mautic dashboard

**n8n Sync Flow:**

```
[Google Sheets: New "Ready" lead]
        ↓
[n8n HTTP Request → Mautic API]
  Create contact → Add to segment → Start campaign
        ↓
[Log: "Mautic campaign started" in sheet]
```

**Email Sending Rules:**

- Max 30–50 cold emails/day per inbox
- Rotate across 2–3 inboxes
- Send between 8am–11am local time of target market
- Never send Friday afternoon or weekends
- Always use plain text or minimal HTML (no heavy templates)

---

### 💼 LinkedIn Outreach via PhantomBuster

**Setup Steps:**

1. PhantomBuster → "LinkedIn Auto Connect" phantom
2. Feed it a CSV of LinkedIn profile URLs (from your lead sheet)
3. Set: Max 20 connection requests/day
4. Add personalized note from "AI Message" column in sheet
5. Schedule: Run 9am–11am Mon–Thu only

**After Connection (DM sequence):**

- PhantomBuster "LinkedIn Message Sender" phantom
- Trigger: 2 days after connection accepted
- Message: Short value message, no pitch

**n8n LinkedIn Monitoring Flow:**

```
[Daily: Check PhantomBuster export]
        ↓
[Parse: Who connected, who didn't]
        ↓
[Update Google Sheet status]
        ↓
[If connected → trigger DM phantom]
[If not connected after 7 days → move to email-only]
```

---

## 📅 PHASE 5 — FOLLOW-UP AUTOMATION (Week 5+)

### 🎯 Goal

Automate follow-ups without being spammy.

### Follow-Up Rules

- Max 3 emails + 2 LinkedIn touches per lead
- Each follow-up is a different angle (not "just following up")
- Add value in every message (insight, case study, quick question)
- 5–7 day gaps between touches

### n8n Follow-Up Flow

```
[Daily Trigger]
        ↓
[Read Google Sheet: Leads where status = "Contacted"]
        ↓
[Check: Days since last contact]
        ↓
[If Day 5 AND no reply → Send Follow-Up Email #2 via Mautic]
[If Day 12 AND no reply → Send Final Email via Mautic]
[If Day 20 AND no reply → Update status to "Archived"]
        ↓
[Log all actions back to sheet]
```

### Follow-Up Email Templates

**Email 2 — Value Angle**

> Subject: [Specific insight] for {{company}}
> 

> Body: Share one quick, relevant insight or result from a similar client. Soft CTA.
> 

**Email 3 — Breakup**

> Subject: Should I close your file?
> 

> Body: Short, respectful. Give them an easy way to opt out OR respond.
> 

---

## 📅 PHASE 6 — RESPONSE HANDLING & CRM (Ongoing)

### 🎯 Goal

Handle replies fast. Never let a warm lead go cold.

### Response Categories

| Reply Type | Action | Who Handles |
| --- | --- | --- |
| Positive / Interested | Move to "Hot Lead" → notify team | VA → Senior |
| Asking for info | Send service one-pager → follow up in 2 days | VA |
| Not now / later | Reschedule in 30 days | n8n auto-schedule |
| Unsubscribe / Remove | Remove from all lists immediately | n8n auto |
| No reply | Continue sequence | Mautic auto |

### n8n Response Detection Flow

```
[Mautic webhook: email replied]
        ↓
[Classify reply with OpenAI]
(Positive / Negative / Info request / Unsubscribe)
        ↓
[If Positive → Update sheet to "Hot" → Send Slack/WhatsApp alert to team]
[If Unsubscribe → Remove from Mautic + mark in sheet]
[If Info → Auto-send one-pager + flag for VA follow-up]
```

---

## 📅 PHASE 7 — CALL BOOKING & PROPOSAL (Week 6+)

### Call Booking Automation

1. [**Cal.com**](http://Cal.com) (free) — create booking page
2. Include in email CTA: "Book a 20-min call: [[cal.com/nivy](http://cal.com/nivy)]"
3. n8n webhook: When booking made → notify team via WhatsApp/Slack
4. Auto-send confirmation + reminder emails via Mautic

### Proposal Sending Automation

1. Use **PandaDoc free** or **Notion** for proposal templates
2. n8n flow: After call booked → auto-send intro deck
3. After call completed → VA triggers proposal creation
4. Track proposal open via PandaDoc

---

## 📅 PHASE 8 — TRACKING, QA & OPTIMIZATION

### 📊 Weekly KPI Dashboard (Google Sheets)

| Metric | Target |
| --- | --- |
| Leads scraped/week | 200+ |
| Emails sent/week | 150+ |
| LinkedIn requests/week | 100+ |
| Open rate | 40%+ |
| Reply rate | 5–8%+ |
| Positive replies/week | 5+ |
| Calls booked/week | 2–3 |
| Proposals sent/week | 1–2 |

### n8n Reporting Flow (Weekly)

```
[Every Monday 8am]
        ↓
[Read all lead data from Google Sheets]
        ↓
[Calculate: Open rate, Reply rate, Conversion by country]
        ↓
[Generate summary → Send to team WhatsApp group]
```

### Feedback Loop

- Review what subject lines get most opens (weekly)
- Test 2 different intros each month (A/B via Mautic)
- Remove lead sources with less than 3% reply rate
- Update ICP scoring monthly based on who actually converts

---

## ⚠️ RISK REGISTER & MITIGATION PLAYBOOK

### 🔴 Platform Risks

| Risk | Mitigation |
| --- | --- |
| Email domain banned | Use secondary domain. Warm up 3+ weeks. Stay under 50 emails/day. |
| LinkedIn account restricted | Use secondary account for automation. Stay under 20 requests/day. Manual backup plan. |
| WhatsApp ban | Use WhatsApp Business. Don't blast. Only reply-based follow-ups. |
| IP blocks on scraping | Use Apify residential proxies. Rotate IPs. Limit scraping speed. |

### 🟠 Automation Risks

| Risk | Mitigation |
| --- | --- |
| Over-automation / robotic feel | Every message gets 1 custom AI line. VA reviews top 20% of messages before send. |
| Bot detection | Use human-like delays in PhantomBuster. Vary send times. |
| Loss of personalization | Enforce personalization field as required before outreach triggers. |

### 🟡 System & Operational Risks

| Risk | Mitigation |
| --- | --- |
| Duplicate outreach | Deduplication node in n8n checks email before every send. |
| Data quality issues | Validate emails before import. Score leads before outreach. |
| Team inconsistency | SOPs linked in Notion. VA daily checklist in Google Sheets. |
| No feedback loop | Mandatory weekly review meeting. KPI sheet auto-updated by n8n. |

### 🟢 Legal & Compliance

| Market | Rule | Action |
| --- | --- | --- |
| USA | CAN-SPAM | Include unsubscribe link. Physical address in footer. |
| UK | GDPR / PECR | Legitimate interest basis. Clear opt-out. No purchased lists. |
| Canada | CASL | Explicit or implied consent only. Unsubscribe in every email. |
| Australia | Spam Act 2003 | Consent-based. Unsubscribe mandatory. |
| UAE | No federal spam law yet | Be respectful. Use Mautic unsubscribe. |

### 🔵 Business Risks

| Risk | Mitigation |
| --- | --- |
| Low conversion | Test 3 different offers. Review ICP monthly. |
| Offer–market mismatch | Tailor message per country (UK tone ≠ USA tone). |
| ROI tracking issues | Track every lead source in sheet. Monthly cost vs. meetings booked. |
| Brand damage | Never send more than 3 touches. Remove complainers instantly. |

### 🟣 Scaling Risks

| Risk | Mitigation |
| --- | --- |
| Scaling too fast | Cap at 50 emails/day for first 60 days. Scale 20% per month. |
| System overload | n8n rate limits. Mautic sending queues. Add VPS RAM before scaling. |

---

## 🗓️ MASTER TIMELINE

| Week | Phase | Key Output |
| --- | --- | --- |
| Week 1 | Phase 0: Foundation | Domain, n8n, Mautic, Sheets ready |
| Week 2 | Phase 1: Scraping | 200+ qualified leads in sheet |
| Week 3 | Phase 2–3: Qualify + AI Messages | Leads scored, messages generated |
| Week 4 | Phase 4: First Outreach | Emails + LinkedIn live |
| Week 5 | Phase 5: Follow-Ups | Sequence running automatically |
| Week 6+ | Phase 6–7: Responses + Calls | Hot leads handled, calls booked |
| Ongoing | Phase 8: Optimize | Weekly review, A/B testing |

---

## 🔥 COMPLETE SYSTEM FLOW

```
[Sources: LinkedIn, Google, Maps, Directories]
                ↓
        [n8n Scraping Layer]
     (X-Ray, Apollo, Apify, Hunter)
                ↓
      [Enrichment & Qualification]
       (Score leads, enrich data)
                ↓
        [Email Validation]
     (Remove invalid, flag risky)
                ↓
      [AI Personalization Layer]
    (OpenAI: custom line per lead)
                ↓
   [Google Sheets: Clean Lead DB]
                ↓
     [Outreach Sequence Starts]
    LinkedIn (PhantomBuster) + Email (Mautic)
                ↓
      [Follow-Up Automation]
         (n8n + Mautic)
                ↓
     [Reply Classification]
          (n8n + OpenAI)
                ↓
    [Hot Leads → Team Alert]
    [Cal.com → Call Booked]
    [PandaDoc → Proposal Sent]
                ↓
      [Weekly KPI Report]
        (n8n → WhatsApp)
```

---

*Last updated: May 2026 | Owner: Nivy Digital | System: n8n + Mautic + Google Sheets + PhantomBuster*