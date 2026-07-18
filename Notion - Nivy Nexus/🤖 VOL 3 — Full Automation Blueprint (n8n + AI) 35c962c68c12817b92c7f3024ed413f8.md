# 🤖 VOL 3 — Full Automation Blueprint (n8n + AI)

> **What this page covers:** The complete n8n automation system — every workflow, every tool, every step. This is your zero-manual-work engine. Built in Month 2, refined in Month 3. Read this before building anything.
> 

---

# 📋 Page Index

1. [The Automation Philosophy](#philosophy)
2. [Full Tool Stack & Costs](#tool-stack)
3. [Workflow 1 — Contact Form Automation](#wf1)
4. [Workflow 2 — Reply Detection & AI Qualification](#wf2)
5. [Workflow 3 — Social Media Auto-Posting](#wf3)
6. [Workflow 4 — Tally Form → Slack Onboarding](#wf4)
7. [Workflow 5 — Follow-Up Sequence](#wf5)
8. [Workflow 6 — Slack Community Content](#wf6)
9. [Workflow 7 — LinkedIn Outreach Automation](#wf7)
10. [Workflow 8 — Daily Morning Briefing](#wf8)
11. [Build Order & Dependencies](#build-order)
12. [Page Metadata](#metadata)

---

# 🤖 The Automation Philosophy {#philosophy}

The goal is a funnel that runs without you. You do the human work (calls, closing, decisions). The machine does the volume work (finding leads, sending messages, qualifying replies, onboarding members, posting content).

**Rule:** Do everything manually in Phase 1. Understand it. Then automate it in Phase 2. Never automate something you don't understand — you won't be able to fix it when it breaks.

**Phase 2 goal:** 100 contact form submissions per day, zero human effort after setup.

**Phase 3 goal:** Full AI pipeline — scrape → write → send → qualify → route → onboard → log. You touch nothing until a HOT lead needs a call.

---

# 🛠️ Full Tool Stack & Costs {#tool-stack}

| Tool | Role | Cost/Month | Phase |
| --- | --- | --- | --- |
| n8n (cloud or self-hosted) | Master automation engine — connects everything | Free / £18 | Phase 2+ |
| Apify | Scrape Google Maps, LinkedIn, Clutch, websites | Free / £40 | Phase 2+ |
| Puppeteer / Playwright | Browser automation — fills and submits contact forms | Free | Phase 2+ |
| Claude API (Anthropic) | Message personalisation, reply qualification, screening | £10–25 | Phase 2+ |
| Gmail API | Send cold emails, detect replies, trigger workflows | Free | Phase 2+ |
| [Instantly.ai](http://Instantly.ai) or Lemlist | Cold email sequences with warm-up built in | £30–40 | Phase 3 |
| [Tally.so](http://Tally.so) | Alliance onboarding form | Free | Phase 0 |
| Notion API | CRM — all lead data logged automatically | Free | Phase 2+ |
| Slack API | Auto-post content, welcome members, send alerts | Free | Phase 2+ |
| Calendly API | Auto-send booking links to HOT leads | Free | Phase 2+ |
| Buffer or Publer | Schedule social media posts across all platforms | Free / £18 | Phase 1+ |
| PhantomBuster | LinkedIn auto-connect and auto-DM sequences | £45 | Phase 3 |
| Twilio | WhatsApp notifications to your phone | £5–10 | Phase 2+ |

---

# ⚡ Workflow 1 — Contact Form Automation (Core Engine) {#wf1}

**What it replaces:** 2 hours of daily manual Google Maps searching and form filling.

**Output:** 50–200 personalised contact form submissions per day, fully automated.

```
TRIGGER: Schedule node — runs every day at 8:00 AM

STEP 1 — SCRAPE TARGETS
Tool: Apify Actor (Google Maps Scraper)
Input: Category ("digital marketing agency") + City ("London")
Output: 50 companies — name, website, phone, address

STEP 2 — FILTER ALREADY-CONTACTED
Tool: Notion → query Lead Tracker database
Logic: Skip any company whose website URL already exists
Output: Clean list of new targets only

STEP 3 — FIND CONTACT FORM URL
Tool: HTTP Request → fetch company homepage
Tool: Code node (JavaScript) → scan HTML for /contact, /get-in-touch, /enquiry
Output: Contact form URL per company

STEP 4 — AI MESSAGE GENERATION
Tool: Claude API
Prompt: "Write a 3-sentence contact form message for [company] in the [industry] sector. You are Nivy Alliance, a UK business exchange looking for [service type] providers. Sound like a real buyer, not a template."
Output: Unique personalised message per company

STEP 5 — SUBMIT CONTACT FORM
Tool: Puppeteer (via Execute Command node)
Actions: Open browser → navigate to form URL → fill fields:
  Name: Nivy Alliance
  Email: outreach@nivallianz.com
  Subject: Business Partnership Enquiry
  Message: [from Step 4]
→ click Submit
Output: Success / fail status

STEP 6 — LOG TO NOTION CRM
Tool: Notion → Create Page in Lead Tracker
Fields: Company, website, industry, city, date, message, status = CONTACTED

STEP 7 — NOTIFY YOU
Tool: Slack or Twilio (WhatsApp)
Message: "✅ [N] contact forms submitted today. Check Notion."
```

---

# ⚡ Workflow 2 — Reply Detection & AI Qualification {#wf2}

**What it replaces:** Manually checking Gmail, reading replies, deciding what to do.

**Output:** Every reply is read, qualified, and routed automatically within 15 minutes of arrival.

```
TRIGGER: Gmail Trigger — polls inbox every 15 minutes

STEP 1 — READ NEW EMAIL
Output: Sender name, company name, email body text

STEP 2 — AI QUALIFICATION
Tool: Claude API
Prompt: "Classify this reply as HOT (wants to buy or book a call now), WARM (interested but not urgent), or COLD (unsubscribe, complaint, or wrong person). Reply with one word only."
Output: HOT | WARM | COLD

IF HOT:
  Gmail → reply with Calendly booking link
  Message: "Thanks for getting back to us. Here's a link to book a 30-min call: [link]."
  Notion → update status to HOT
  Slack → alert: "🔥 HOT LEAD: [Company] — Calendly link sent"

IF WARM:
  Gmail → send Alliance invite email
  Message: "We run a private business exchange called Nivy Alliance — UK-verified companies share outsourcing needs. Here's a 2-minute overview: [landing page link]."
  Notion → update status to WARM

IF COLD:
  Notion → update status to COLD, tag: DO NOT CONTACT
  Gmail → archive (no reply sent)
```

---

# ⚡ Workflow 3 — Social Media Auto-Posting {#wf3}

**What it replaces:** Daily manual posting across platforms.

**Output:** All pre-written posts go live at the right time, on the right platform, without you touching anything.

```
SETUP (one time):
1. Connect to Buffer or Publer:
   - LinkedIn Personal profile
   - LinkedIn Company: Nivy
   - LinkedIn Company: Nivy Alliance
   - Instagram @thenivy
   - Facebook Page: Nivy
2. Write 4 weeks of content for each platform
3. Schedule all posts in Buffer — set date, time, platform
4. Buffer auto-publishes

LINEDIN ENQUIRY POSTS (personal profile):
- LinkedIn has native scheduling — use it (free)
- OR: PhantomBuster LinkedIn Poster for full automation

FACEBOOK GROUPS (semi-manual — groups block bots):
- n8n Schedule → Slack/WhatsApp reminder at 9:05 AM:
  "Time to post in Facebook groups. Today's post: [paste post text here]"
- You copy-paste into 5 groups (10 minutes total)

INSTAGRAM:
- Buffer auto-posts Reels and carousels
- Batch-create 30 days of visuals in Canva in one session
```

---

# ⚡ Workflow 4 — Tally Form → Slack Community Onboarding {#wf4}

**What it replaces:** Manually processing applications, emailing Slack invites, welcoming members.

**Output:** Approved members are onboarded in under 5 minutes, automatically.

```
TRIGGER: Tally Webhook — fires on new form submission

STEP 1 — CAPTURE DATA
Fields: name, company, role, website, services offered, services needed

STEP 2 — AI SCREENING
Tool: Claude API
Prompt: "Review this Alliance application: Company [X], Role [Y], Services they outsource [Z]. Good fit for a UK B2B exchange targeting verified SMBs? Reply YES or NO with one sentence reason."
Output: YES or NO + reason

IF APPROVED:
  Slack API → generate Slack invite link
  Gmail → send welcome email:
    Subject: "Welcome to Nivy Alliance 🎉"
    Body: "Hi [name], you're in. Slack invite: [link]. Start in #start-here."
  Slack → post in #introductions:
    "Welcome [name] from [company] — they [what they offer]. Say hi! 👋"
  Notion → create member record: name, company, joined date, status = MEMBER

IF REJECTED:
  Gmail → polite holding email:
    "Thanks for applying. We're at capacity for [their category]. We'll reach out when a spot opens."
  Notion → create record: status = WAITLIST
```

---

# ⚡ Workflow 5 — Follow-Up Sequence (Automated) {#wf5}

**What it replaces:** Manually tracking which leads got which follow-ups.

**Output:** No lead ever falls through the cracks. Every contacted company gets followed up on Days 3, 7, and 14 automatically.

```
TRIGGER: Schedule — every morning at 7:00 AM

STEP 1 — QUERY NOTION
Filter: Status = CONTACTED
  AND Days since contact = 3 OR 7 OR 14
  AND Follow-up count < 3

STEP 2 — SEND EMAIL
Day 3: "Just following up — we're still looking for a [service type] partner. Would love a quick chat."
Day 7: "One more note — happy to share how Alliance members have sourced new clients. Worth a 20-min call?"
Day 14: "Last note from me. If timing isn't right, no worries. Feel free to reply whenever."

STEP 3 — UPDATE NOTION
Increment follow-up count. Update last contact date.

STEP 4 — AFTER 3 FOLLOW-UPS, NO REPLY
Notion → status = COLD-ARCHIVED
Stop all workflows for this lead
```

---

# ⚡ Workflow 6 — Weekly Slack Community Content {#wf6}

**What it replaces:** Manually posting in Slack 3 times per week.

**Output:** Community stays active and engaged without you logging in.

```
TRIGGER: Schedule (3× per week)

MONDAY 9:00 AM → #opportunities:
"🔍 This week's open requirements:
• [Category 1]: Looking for [service] — reply to connect
• [Category 2]: Need [service] by [date]
• [Category 3]: Evaluating [service] providers
Any members who can help? Drop a reply below."

WEDNESDAY 11:00 AM → #resources:
"📌 Resource of the week: [Title]
[2-sentence summary]
Link: [URL]"

FRIDAY 4:00 PM → #general:
"👋 Friday check-in — drop one win from this week. Doesn't matter how small."

Content source: Pre-written in Notion content calendar
n8n reads via Notion API → posts to Slack
```

---

# ⚡ Workflow 7 — LinkedIn Outreach Automation {#wf7}

**Phase 3 only.** Do not run before 500+ connections and active posting history.

**Tool:** PhantomBuster LinkedIn Network Booster + Message Sender

```
DAILY LIMITS (stay within to avoid ban):
- Connection requests: 20–25/day
- Follow-up DMs: 10–15/day
- Active hours only: 9 AM–6 PM (human-like pattern)

SEQUENCE:
Day 1: Send connection request (no message — higher acceptance rate)
Day 3 (after accept): DM:
  "Hi [name], glad to connect. I noticed [company] does [service] — we have Alliance members actively looking for this. Quick call?"
Day 7 (no reply): Follow-up DM:
  "Just a quick follow-up. Happy to share more about the Alliance if useful."

n8n integration:
PhantomBuster webhook → n8n → Claude qualifies reply → same HOT/WARM/COLD routing as Workflow 2
```

---

# ⚡ Workflow 8 — Daily Morning Briefing {#wf8}

**What it does:** Every weekday at 8:55 AM — 5 minutes before you start — sends a WhatsApp or Slack message with everything that happened overnight.

```
TRIGGER: Schedule — weekdays at 8:55 AM

DATA PULLED:
- Notion API → new leads added yesterday
- Gmail API → new replies received
- Notion API → HOT leads awaiting call
- Slack API → new members joined

MESSAGE (WhatsApp via Twilio or Slack DM):
"☀️ Nivy Alliance Morning Briefing

📬 New replies: [N]
🔥 HOT leads to call today: [N] — [names]
🟡 WARM leads to nurture: [N]
👥 New members overnight: [N]
📊 Total leads this week: [N]

Priority: [pull from Notion Today's Focus field]"
```

---

# 📊 Build Order & Dependencies {#build-order}

Build in this exact sequence. Each workflow depends on the previous one working.

| Build Week | Workflow | Dependency | Done? |
| --- | --- | --- | --- |
| Week 5 | Connect n8n to Gmail, Notion, Slack APIs | None — first step | ☐ |
| Week 5 | WF4: Tally → Slack Onboarding | Tally form live, Slack live | ☐ |
| Week 5 | WF1: Contact Form Automation | Apify account, Puppeteer, Notion CRM | ☐ |
| Week 6 | WF2: Reply Detection & Qualification | WF1 live (generates replies) | ☐ |
| Week 6 | WF5: Follow-Up Sequence | WF1 live, Notion Lead Tracker | ☐ |
| Week 7 | WF6: Slack Content Posting | Notion content calendar populated | ☐ |
| Week 7 | WF8: Daily Briefing | All APIs connected | ☐ |
| Week 8 | WF3: Social Media Scheduling | Buffer account, content written | ☐ |
| Month 3 | WF7: LinkedIn Outreach (PhantomBuster) | 500+ connections, posting history | ☐ |

---

# 🏷️ Page Metadata {#metadata}

**Page type:** Technical Blueprint | Volume 3 of 6

**Project:** Nivy Alliance

**Organisation:** Nivy | [thenivy.com](http://thenivy.com)

**Topics covered:** n8n automation, Puppeteer, Apify, Claude API, Gmail automation, Slack automation, PhantomBuster, contact form automation, social media scheduling, lead qualification, follow-up sequences, community onboarding

**Keywords:** n8n workflow, contact form automation, AI lead qualification, Claude API automation, Puppeteer form fill, Apify scraping, LinkedIn automation, PhantomBuster, Tally webhook, Notion CRM automation

**Status:** 🟡 Planned — build starts Month 2

**Depends on:** Phase 1 complete (must understand the manual process first)

**Last updated:** 10 May 2026

**Next page to read:** 📅 VOL 4 — Master Execution Plan