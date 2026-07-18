# 🤖 VOL 6 — Full Automation Blueprint (n8n + AI)

> **The complete technical automation plan.** This volume covers all 8 n8n workflows that automate the entire Nivy Alliance funnel — from scraping to Slack onboarding. Build these in Month 2. Nothing here requires coding beyond basic n8n configuration.
> 

---

# 🗺️ Page Index

1. Automation Stack (Tools Required)
2. Workflow 1 — Contact Form Automation (Core Engine)
3. Workflow 2 — Reply Detection & AI Qualification
4. Workflow 3 — Social Media Auto-Posting
5. Workflow 4 — Tally Form → Slack Community Onboarding
6. Workflow 5 — Follow-Up Sequence (Automated)
7. Workflow 6 — Weekly Slack Community Content
8. Workflow 7 — LinkedIn Outreach Automation (Phase 3)
9. Workflow 8 — Daily Briefing (Your Morning Report)
10. Metadata & Search Tags

---

# 🛠️ 1. Automation Stack (Tools Required)

| Tool | Purpose | Cost | When Needed |
| --- | --- | --- | --- |
| n8n (self-hosted or cloud) | Master automation engine — connects everything | Free / £18/mo | Phase 2 Day 1 |
| Apify | Scraping Google Maps, LinkedIn, Clutch, websites | Free tier / £40/mo | Phase 2 |
| Puppeteer / Playwright (via n8n) | Browser automation — fills and submits contact forms | Free | Phase 2 |
| Claude API (Anthropic) | AI message personalisation, reply qualification, content generation | £10–25/mo | Phase 3 |
| Gmail API | Send cold emails, detect replies, trigger workflows | Free | Phase 2 |
| [Instantly.ai](http://Instantly.ai) or Lemlist | Cold email sequences with warm-up built in | £25–40/mo | Phase 3 |
| [Tally.so](http://Tally.so) | Alliance onboarding form | Free | Phase 0 |
| Notion API | CRM — all lead data logged here automatically | Free | Phase 2 |
| Slack API | Auto-post community content, welcome new members | Free | Phase 2 |
| Calendly API | Auto-send booking links to HOT leads | Free | Phase 2 |
| Buffer or Publer | Schedule and auto-post social media content across all platforms | Free / £15/mo | Phase 2 |
| PhantomBuster | LinkedIn automation — auto-connect, auto-DM sequences | £45/mo | Phase 3 |
| [Make.com](http://Make.com) (optional) | Alternative to n8n for simpler workflows if needed | Free tier | Optional |

---

# 🤖 2. Workflow 1 — Contact Form Automation (Core Engine)

**What it does:** Automatically finds target companies, extracts their contact form URL, writes a personalised message, fills the form, and submits it. Replaces 2 hours of manual work per day with zero human effort.

```
TRIGGER: Schedule — runs every day at 8:00 AM

STEP 1 — SCRAPE TARGETS
Node: HTTP Request → Apify Actor (Google Maps Scraper)
Input: Category (e.g. “digital marketing agency”) + City (e.g. “London”)
Output: List of 50 companies with name, website, phone, address

STEP 2 — FILTER ALREADY-CONTACTED
Node: Notion → Query “Lead Tracker” database
Logic: Skip any company where website URL already exists in Notion
Output: Clean list of new targets only

STEP 3 — FIND CONTACT FORM URL
Node: HTTP Request → fetch company website homepage
Node: Code (JavaScript) → scan HTML for /contact, /get-in-touch, /enquiry paths
Output: Contact form URL for each company

STEP 4 — AI MESSAGE GENERATION
Node: HTTP Request → Claude API
Prompt: “You are writing a brief, human-sounding enquiry for a business called [company name] in the [industry] sector. The enquiry is from Nivy Alliance, a UK business exchange. We are looking for [service type] providers. Write a 3-sentence contact form message that sounds like a real buyer, not a template. Do not mention automation.”
Output: Personalised message (unique per company)

STEP 5 — SUBMIT CONTACT FORM
Node: Execute Command → Puppeteer script
Actions: Open browser → navigate to contact form URL → fill in all fields → click Submit
Output: Success / fail status

STEP 6 — LOG TO NOTION CRM
Node: Notion → Create Page in “Lead Tracker” database
Fields: Company name, website, industry, city, form submitted date, message used, status = CONTACTED

STEP 7 — NOTIFY YOU
Node: Slack message OR WhatsApp (via Twilio)
Message: “✅ 50 contact forms submitted today. Check Notion for full log.”

Volume: 50–200 submissions per day, fully automated
Your effort: Zero (after setup)
```

---

# 📨 3. Workflow 2 — Reply Detection & AI Qualification

**What it does:** Monitors the outreach Gmail inbox. When a reply arrives, Claude reads it, decides if the lead is HOT/WARM/COLD, and takes the right action automatically.

```
TRIGGER: n8n Gmail Trigger — polls inbox every 15 minutes

STEP 1 — READ NEW EMAIL
Node: Gmail Trigger → fires when new email arrives
Output: Sender name, company, email body

STEP 2 — AI QUALIFICATION
Node: HTTP Request → Claude API
Prompt: “Read this email reply from [company]. Classify it as HOT (ready to buy or book a call now), WARM (interested but not urgent), or COLD (complaint, unsubscribe, or wrong person). Reply with only one word: HOT, WARM, or COLD.”
Output: HOT / WARM / COLD

STEP 3A — IF HOT
Node: Gmail → send reply with Calendly link
Node: Notion → update lead status to HOT
Node: Slack → alert: “🔥 HOT LEAD: [Company] — replied and sent Calendly link”

STEP 3B — IF WARM
Node: Gmail → send Alliance invite email with landing page link
Node: Notion → update lead status to WARM

STEP 3C — IF COLD
Node: Notion → update lead status to COLD, tag: DO NOT CONTACT
Node: Gmail → move to archive (no reply sent)
```

---

# 📱 4. Workflow 3 — Social Media Auto-Posting

**What it does:** Pre-written posts are scheduled in Buffer/Publer and automatically published to LinkedIn, Instagram, and Facebook at the right times.

```
SETUP (one time):
1. Connect LinkedIn Personal, LinkedIn Company (Nivy), LinkedIn Company (Nivy Alliance),
   Instagram, and Facebook Page to Buffer or Publer
2. Write 4 weeks of posts for each platform
3. Schedule all posts in Buffer — set time, platform, and content
4. Buffer auto-publishes at scheduled time

For LinkedIn enquiry posts:
- Use LinkedIn’s native scheduling (free, built-in)
- OR PhantomBuster LinkedIn Poster for personal profile

For Facebook group posts (cannot be fully automated):
- n8n sends you a reminder at 9:00 AM: “Time to post in Facebook groups — [paste today’s post here]”
- Copy-paste from the reminder into groups manually (10 minutes total)

For Instagram:
- Buffer auto-posts Reels and carousels
- Use Canva to batch-create 30 days of visuals in one sitting
```

---

# 🤝 5. Workflow 4 — Tally Form → Slack Community Onboarding

**What it does:** When someone fills the Alliance application form, they are automatically sent a Slack invite, welcomed in the community, and logged in the CRM.

```
TRIGGER: Tally Webhook → fires when new form submitted

STEP 1 — CAPTURE SUBMISSION
Node: Webhook → receives: name, company, role, website, services offered, services needed

STEP 2 — AI SCREENING
Node: Claude API
Prompt: “Review this Alliance application. Are they a good fit for a UK business exchange targeting verified SMBs? Reply YES or NO with one sentence reason.”
Output: YES/NO + reason

STEP 3A — IF APPROVED (YES)
Node: Slack API → generate invite link for Nivy Alliance workspace
Node: Gmail → send welcome email with Slack invite
Node: Slack → post in #introductions: “Welcome [name] from [company] — they [services they offer]. Say hi! 👋”
Node: Notion → create record: name, company, joined date, status = MEMBER

STEP 3B — IF REJECTED (NO)
Node: Gmail → send polite holding email (waitlist)
Node: Notion → create record: status = WAITLIST
```

---

# 🔄 6. Workflow 5 — Follow-Up Sequence (Automated)

**What it does:** For every lead that received a contact form submission but did not reply, sends automated follow-up emails on Days 3, 7, and 14.

```
TRIGGER: n8n Schedule — runs every morning at 7:00 AM

STEP 1 — QUERY NOTION FOR FOLLOW-UP TARGETS
Node: Notion → filter Lead Tracker where:
  Status = CONTACTED
  AND Days since contact = 3, 7, or 14
  AND Follow-up count < 3

STEP 2 — SEND FOLLOW-UP EMAIL
Day 3: “Hi [name], just following up on my note from [date]. We’re still looking for a [service type] partner for the Alliance. Would love a quick chat if timing works.”
Day 7: “One more quick note — we’ve had good interest from similar firms. Worth a 20-minute call?”
Day 14: “Last note from me — if timing isn’t right now, no worries. Happy to reconnect whenever.”

STEP 3 — UPDATE NOTION
Node: Notion → increment follow-up count, update last contact date

STEP 4 — AFTER 3 FOLLOW-UPS WITH NO REPLY
Node: Notion → update status to COLD-ARCHIVED
Node: Stop workflow for this lead
```

---

# 💬 7. Workflow 6 — Weekly Slack Community Content

**What it does:** Posts pre-written content into Slack channels on schedule so the community feels alive even when you’re not online.

```
TRIGGER: n8n Schedule (3 times per week)

MONDAY 9:00 AM → post to #opportunities:
“🔍 This week’s open requirements:
• [Category 1]: Looking for [service] — reply to connect
• [Category 2]: Need [service] by [date]
• [Category 3]: Evaluating [service] providers
Any members who can help? Drop a reply below.”

WEDNESDAY 11:00 AM → post to #resources:
“📌 Resource of the week: [Article title / tool / tip]
[2-sentence summary]
Full link: [URL]”

FRIDAY 4:00 PM → post to #general:
“👋 Friday check-in — drop one win from this week below. Community is built on momentum.”

Content source: Pre-written in Notion content calendar → n8n reads via Notion API → posts to Slack
```

---

# 🔗 8. Workflow 7 — LinkedIn Outreach Automation (Phase 3)

**What it does:** Uses PhantomBuster to automatically send connection requests and follow-up DMs on LinkedIn at safe volumes.

```
PHASE 3 ONLY — do not run before you have 500+ connections and an active posting history.

TOOL: PhantomBuster LinkedIn Network Booster + Message Sender

DAILY LIMITS (stay within to avoid LinkedIn ban):
- Connection requests: 20–25/day max
- Follow-up DMs: 10–15/day max
- Run between 9 AM–6 PM only (looks human)

SEQUENCE:
Day 1: Send connection request (no message)
Day 3 (after accepted): Send DM with value prop and Calendly/Alliance invite
Day 7 (if no reply): Send one follow-up DM

n8n Integration:
- PhantomBuster webhook → fires when DM reply received
- n8n reads reply → Claude qualifies (HOT/WARM/COLD)
- Same routing as Workflow 2
```

---

# ☀️ 9. Workflow 8 — Daily Briefing (Your Morning Report)

**What it does:** Every weekday at 8:55 AM sends you a WhatsApp or Slack message summarising everything that happened overnight.

```
TRIGGER: n8n Schedule — every weekday at 8:55 AM

DATA PULLED:
- Notion API → count of new leads added yesterday
- Gmail API → count of new replies in inbox
- Notion API → HOT leads awaiting follow-up
- Slack API → new members who joined overnight

MESSAGE SENT (to your WhatsApp via Twilio or to Slack):
“☀️ Good morning — here’s your Nivy Alliance briefing:

📩 Replies received: [N]
🔥 HOT leads to call today: [N] — [names]
🟡 WARM leads to nurture: [N]
👥 New Slack members: [N]
📊 Total leads this week: [N]

Today’s priority: [auto-populated from Notion Today’s Focus]”
```

---

# 🗺️ Navigation

- ← Back to: **VOL 5 — Website, Landing Page & Social Media**
- → Next: **VOL 7 — Master Execution Timeline & Cost Breakdown**
- → Master: **MASTER INDEX**

---

# 🔍 Metadata & Search Tags

**Project:** Nivy Alliance

**Document type:** Automation Blueprint

**Volume:** 6 of 7

**Last updated:** 10 May 2026

**Status:** Active — Phase 2 build

**Owner:** Abhi

**Tags:** nivy alliance, n8n, automation, Apify, Puppeteer, Claude API, Gmail automation, Slack onboarding, contact form automation, reply detection, AI qualification, PhantomBuster, LinkedIn automation, follow-up sequence, Tally webhook, daily briefing, social media scheduling, Buffer

**Search keywords:** nivy alliance automation, n8n workflows, how to automate contact forms, AI lead qualification, Tally to Slack automation, Gmail reply detection, LinkedIn auto DM, daily briefing workflow, Slack content automation, follow-up email sequence