# ⚙️ Phase 2 — n8n Automation Blueprint (Days 31–60)

> This is your semi-automation setup. Three workflows handle the highest-volume, most repetitive tasks. You still manage DMs, calls, and closing manually.
> 

---

# Overview — What Gets Automated

| Workflow | What It Does | Volume |
| --- | --- | --- |
| 2A — Contact Form Bot | Scrapes Google Maps → submits contact forms | 50–100/day |
| 2B — Gmail Reply Detector | Monitors inbox → tags replies in Notion → alerts you | Every reply |
| 2C — Tally → Slack Auto-Invite | New Alliance applicant → sends Slack invite + logs to CRM | Every form submission |

---

# Workflow 2A — Contact Form Automation

## What It Does

n8n scrapes Google Maps for target businesses by city and category. Puppeteer (via n8n) visits each website, finds their contact form, and submits your personalised message automatically.

## Step-by-Step Setup

**Step 1: Google Maps Scraper Node**

- In n8n, add an HTTP Request node
- Use Google Maps Places API or the SerpAPI Google Maps endpoint
- Query: `"digital marketing agency" + city` (rotate through your target cities)
- Output: Company name, website URL, address, phone

**Step 2: Website Contact Form Finder**

- For each website URL: use an HTTP Request node to fetch the page HTML
- Use a Code node (JavaScript) to find the contact page URL (look for `/contact`, `/contact-us`, `/get-in-touch` in links)
- If no contact page found → skip to next company

**Step 3: Puppeteer Form Submission**

- Use n8n's "Execute Command" node to run a Puppeteer script
- Script visits the contact URL, fills in name/email/message fields, submits the form
- Personalisation variables: `{{companyName}}`, `{{city}}`, `{{industry}}`
- Add a 30–60 second random delay between submissions (avoids detection)

**Step 4: Log to Notion**

- After each submission: create a new row in your Lead Tracker database
- Fields: Company Name, Website, City, Industry, Date Submitted, Status = "FORM SENT"

**Message Template for Automation:**

```
Subject: Partnership Enquiry — Nivy Alliance

Hi [Team],

I came across [Company Name] while researching [industry] businesses in [city].

We run Nivy Alliance — a small private network where verified UK businesses share outsourcing requirements and connect with trusted service providers.

We're currently looking for reliable [accounting / marketing / IT] partners to refer to our members.

Would a 15-minute call this week be possible?

[Your Name]
[Phone]
[Calendly Link]
nivyalliance@gmail.com
```

**Volume target:** 50 submissions/day in Week 1 → 100/day by Week 4

---

# Workflow 2B — Gmail Reply Detector

## What It Does

Monitors your Nivy Alliance Gmail inbox. When a reply arrives, it automatically tags the lead in Notion, updates their status, and sends you a WhatsApp or Slack notification so you respond within minutes.

## Step-by-Step Setup

**Step 1: Gmail Trigger Node**

- In n8n: add a Gmail Trigger node
- Connect your Nivy Alliance Gmail account via OAuth
- Trigger: "New Email" in Inbox
- Poll every 15 minutes (free tier) or use Gmail Push via Google PubSub (real-time)

**Step 2: Parse Sender Details**

- Use a Code node to extract: sender name, sender email, company (from email domain), reply content
- Strip quoted reply text (keep only the new message)

**Step 3: Update Notion Lead Tracker**

- Search for existing lead by email in Notion
- If found: update Status from "FORM SENT" to "RESPONDED"
- If not found: create new row with Status = "INBOUND RESPONDED"
- Log: Reply Date, Reply Snippet (first 100 chars)

**Step 4: Send You a Notification**

- Add a Slack node: post to your personal Slack DM or a private #alerts channel
- Message: `🔴 New reply from [Name] at [Company] — [Reply snippet] → [Notion link]`
- Alternative: WhatsApp via Twilio or CallMeBot API

**Why This Matters:** Speed of response is critical. Leads who get a reply within 5 minutes are 9x more likely to convert than those who wait an hour.

---

# Workflow 2C — Tally Form → Slack Auto-Invite

## What It Does

When someone submits the Nivy Alliance onboarding form on Tally, they're automatically sent a Slack invite, logged in Notion as a new member, and their intro is prepared for posting in #introductions.

## Step-by-Step Setup

**Step 1: Tally Webhook Trigger**

- In Tally: go to Integrations → Webhooks → Add webhook URL from n8n
- In n8n: add a Webhook trigger node, copy the URL into Tally
- Test by submitting the form yourself

**Step 2: Send Slack Invite Email**

- Add a Gmail node: send an email to the applicant
- Subject: `Welcome to Nivy Alliance — Your Slack Invite`
- Body:

```
Hi [Name],

Thanks for applying to Nivy Alliance.

Your application has been reviewed. Here's your invite to join the community:

[SLACK INVITE LINK — paste your permanent invite link here]

Once inside, head to #start-here and then post your intro in #introductions.

Looking forward to having you in the network.

Nivy Alliance Team
```

**Step 3: Log to Notion**

- Create a new row in your Lead Tracker
- Fields: Name, Company, Country, What They Outsource, What They're Looking For, Status = "SLACK INVITED", Date

**Step 4: Notify Yourself**

- Slack alert: `✅ New Alliance member: [Name] from [Company] — [Country]`

---

# Cost Summary for Phase 2

| Tool | Plan | Monthly Cost |
| --- | --- | --- |
| n8n Cloud | Starter | $20/month |
| Google Maps API | Pay-per-use | ~$5–15/month |
| SerpAPI (alternative) | Hobby | $50/month |
| Gmail (standard) | Free | $0 |
| [Tally.so](http://Tally.so) | Free | $0 |
| Notion | Free | $0 |
| **Total** |  | **~$25–35/month** |

---

# Phase 2 Exit Criteria

- [ ]  All 3 workflows live and tested
- [ ]  Submitting 50+ forms/day unattended
- [ ]  Every Gmail reply triggers a Notion update and your notification
- [ ]  Every Tally form submission triggers a Slack invite automatically
- [ ]  50+ Slack members in the community
- [ ]  5+ paying clients secured

**When all done → move to Phase 3: Full AI Pipeline**