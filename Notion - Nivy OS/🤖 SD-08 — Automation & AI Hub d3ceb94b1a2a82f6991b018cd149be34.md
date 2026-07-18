# 🤖 SD-08 — Automation & AI Hub

**Parent:** [🏢 SALES & MARKETING DEPARTMENT](%F0%9F%8F%A2%20SALES%20&%20MARKETING%20DEPARTMENT%20%E2%80%94%20The%20Nivy%206d7eb94b1a2a82f4934e011a405261c4.md) | **Owner:** Abhishek Dayal | **Company:** Billion Dreams United (The Nivy) | **Website:** [www.thenivy.com](http://www.thenivy.com) | **Status:** 🟡 In Progress | **Updated:** May 8, 2026

---

> This is the complete automation nervous system of Nivy Digital. Every lead entry point, every workflow, every tool integration is documented here. The goal: 85%+ of lead handling happens automatically with zero manual touchpoints.
> 

---

# 📌 QUICK LINKS

- [Master Automation Architecture](#master-arch)
- [n8n Workflow Library](#n8n-workflows)
- [Website Form → CRM Setup](#form-crm)
- [Chatbot → CRM Integration](#chatbot-crm)
- [Social DM Automation (ManyChat)](#social-dm)
- [WhatsApp Business API Setup](#whatsapp-api)
- [Review Collection Automation](#review-automation)
- [Email Sequence Automation](#email-sequences)

---

# 🤖 MASTER AUTOMATION ARCHITECTURE {#master-arch}

```
┌──────────────────────────────────────────────────┐
│         LEAD ENTRY POINTS                        │
│  ⭕ Website form    ⭕ Chatbot (Chatwoot)           │
│  ⭕ WhatsApp         ⭕ LinkedIn DM                  │
│  ⭕ Facebook/IG DM   ⭕ Directory inquiries          │
│  ⭕ Cold email reply ⭕ Referral form                │
└──────────────────────────────────────────────────┘
                         ↓
              🤖 n8n AUTOMATION HUB
              (self-hosted on Railway.app)
                         ↓
         ┌─────────────────────────────┐
         │       OUTPUTS                    │
         │  ✔ HubSpot CRM (contact created) │
         │  ✔ Slack alert to founder         │
         │  ✔ Auto-reply email sent          │
         │  ✔ Nurture sequence started       │
         │  ✔ Cal.com booking triggered      │
         └─────────────────────────────┘
```

## n8n Setup Guide

### Step 1: Deploy n8n (Free, Self-Hosted)

**Option A: [Railway.app](http://Railway.app) (Easiest)**

1. Go to [railway.app](http://railway.app) → New Project → Deploy from template
2. Search "n8n" → Deploy
3. Set environment variables:
    - `N8N_BASIC_AUTH_ACTIVE=true`
    - `N8N_BASIC_AUTH_USER=admin`
    - `N8N_BASIC_AUTH_PASSWORD=[strong password]`
4. Your n8n URL: https://[your-app].[railway.app](http://railway.app)

**Option B: [Render.com](http://Render.com) (Free Tier)**

1. [render.com](http://render.com) → New → Web Service
2. Connect GitHub repo with n8n Docker config
3. Free 750 hours/month

### Step 2: Connect Key Services

- HubSpot: Use HubSpot API key (Settings → Integrations → API Key)
- Slack: Create Slack app → Get webhook URL
- Gmail/Brevo: SMTP credentials
- Chatwoot: API key from Chatwoot settings
- [Cal.com](http://Cal.com): Webhook URL in [Cal.com](http://Cal.com) settings
- [Tally.so](http://Tally.so): Webhook URL in form settings

---

# 📊 n8n WORKFLOW LIBRARY {#n8n-workflows}

## Workflow 1: Website Form → CRM → Welcome Email

**Trigger:** [Tally.so](http://Tally.so) / HubSpot form webhook

**Steps:**

1. Receive webhook from Tally form
2. Extract: name, email, phone, service interest, company
3. Create/Update contact in HubSpot CRM
4. Set HubSpot deal stage: "New Lead"
5. Send Slack message: "New lead: [Name] from [Company] interested in [Service]"
6. Send welcome email via Brevo:
    - Subject: "Welcome to Nivy Digital — Here's What Happens Next"
    - Body: Introduction + [Cal.com](http://Cal.com) booking link + WhatsApp link
7. Add contact to email nurture sequence in Brevo

**Status:** ⬜ Build in Phase 4

---

## Workflow 2: Chatwoot Lead → CRM

**Trigger:** Chatwoot webhook — conversation with email captured

**Steps:**

1. Chatwoot webhook fires when email label added to conversation
2. n8n extracts: email, name, conversation transcript, service interest
3. Create HubSpot contact with tag "chatbot-lead"
4. Set lead source: "Website Chatbot"
5. Send Slack alert
6. Trigger welcome email sequence

**Status:** ⬜ Build in Phase 4

---

## Workflow 3: [Cal.com](http://Cal.com) Booking → CRM Update + Reminders

**Trigger:** [Cal.com](http://Cal.com) webhook — new booking created

**Steps:**

1. Receive [Cal.com](http://Cal.com) booking webhook
2. Find/create HubSpot contact by email
3. Update deal stage to "Discovery Scheduled"
4. Send confirmation email with: call link, agenda, what to prepare
5. Schedule reminder: 24h before → send reminder email
6. Schedule reminder: 1h before → send SMS (via Brevo/Twilio free)
7. Post in Slack: "Discovery call booked with [Name] at [Time]"

**Status:** ⬜ Build in Phase 4

---

## Workflow 4: Project Complete → Review Request

**Trigger:** HubSpot deal moved to "Closed Won"

**Steps:**

1. HubSpot webhook: deal stage changed to "Closed Won"
2. Wait 3 days (n8n wait node)
3. Send review request email:
    - Subject: "Quick favor — how did we do?"
    - 3 review links: Google, Clutch, Trustpilot
4. If no click in 5 days → send 1 reminder
5. Log review request sent in HubSpot contact notes

**Status:** ⬜ Build in Phase 4

---

## Workflow 5: Blog Post Published → Social Auto-Post

**Trigger:** WordPress webhook OR RSS feed new item

**Steps:**

1. New blog post published (WordPress webhook)
2. Extract: title, excerpt, featured image URL, post URL
3. Post to LinkedIn company page (LinkedIn API)
4. Post to Twitter/X (Twitter API)
5. Post to Facebook page (Facebook Graph API)
6. Send to newsletter as "Latest Article" section

**Status:** ⬜ Build in Phase 4

---

## Workflow 6: Lead Re-engagement (14-Day Inactive)

**Trigger:** HubSpot contact — no activity in 14 days AND deal stage not "Closed Won" or "Closed Lost"

**Steps:**

1. HubSpot workflow triggers n8n webhook
2. Check: Is lead in re-engagement sequence already? If yes, skip.
3. Send Email 1: "Still thinking about it? Here's a case study"
4. Wait 3 days
5. Send Email 2: "Quick question about your business"
6. Wait 4 days
7. Send Email 3 (final): "Should I close your file?"
8. If no response: Move HubSpot deal to "Closed Lost" + tag "nurture-later"

**Status:** ⬜ Build in Phase 4

---

## Workflow 7: WhatsApp Inquiry → CRM

**Trigger:** New WhatsApp Business message (via Brevo WhatsApp API or WATI webhook)

**Steps:**

1. Receive WhatsApp webhook
2. Extract sender phone number + message
3. Create HubSpot contact (phone as primary identifier)
4. Set lead source: "WhatsApp"
5. Send Slack alert to founder
6. Send auto-reply via WhatsApp: "Hi! Thanks for reaching out to Nivy Digital. Our team will reply within 2 hours. Want to book a free call? [[Cal.com](http://Cal.com) link]"

**Status:** ⬜ Build in Phase 4

---

## Workflow 8: LinkedIn Connection → DM Sequence

**Trigger:** PhantomBuster — new LinkedIn connection accepted

**Steps:**

1. PhantomBuster export → Google Sheet new row
2. n8n monitors Google Sheet → new row = trigger
3. Wait 24 hours
4. PhantomBuster sends DM (Day 1): Personalized intro
5. Wait 5 days
6. If no reply: PhantomBuster sends follow-up DM
7. If reply: n8n creates HubSpot lead + Slack alert

**Status:** ⬜ Build in Phase 5

---

# 💬 SOCIAL DM AUTOMATION {#social-dm}

## Facebook & Instagram: ManyChat Setup

### Step 1: Connect ManyChat

1. Go to [manychat.com](http://manychat.com) → Connect Facebook Page
2. Connect Instagram Business Account
3. Free tier: up to 1,000 active contacts

### Step 2: Build Welcome Flow

```
Trigger: Someone DMs "info" OR "services" OR "price"

Message 1:
"Hi [First Name]! 👋 Thanks for reaching out to Nivy Digital.
What would you like to know about?"

Buttons:
[👤 Virtual Assistant Services]
[📊 Digital Marketing]
[🤖 AI Automation]
[💰 Pricing]

Each button → reply with relevant info + "Want a free strategy call? [Book here]"
```

### Step 3: Lead Capture Flow

```
After service info:
Bot: "Would you like us to send you our service brochure?"
→ Yes: "Great! What's your email?"
→ Capture email → ManyChat → n8n → HubSpot CRM
→ Send email with brochure via Brevo
```

---

# 📱 WHATSAPP BUSINESS API SETUP {#whatsapp-api}

## Option 1: Brevo (Free up to 1,000 conversations)

### Setup Steps:

1. Create Brevo account (free)
2. Go to Conversations → Channels → WhatsApp Business
3. Submit WhatsApp Business verification (need FB Business Manager)
4. Once approved: connect to n8n via Brevo API
5. Set up auto-replies in Brevo

### Auto-Reply Messages to Create:

- **Greeting message:** "Hi! Welcome to Nivy Digital. We help businesses grow with VA services, digital marketing, and AI automation. How can we help you today?"
- **Away message (after hours):** "Thanks for reaching out! We're currently offline (9 AM - 6 PM IST). We'll reply first thing tomorrow. Book a call: [[Cal.com](http://Cal.com) link]"
- **FAQ keyword responses:** "pricing" → send pricing info, "services" → send services list

## Option 2: WATI (Paid, $49/mo — Phase 4+)

- More advanced automation
- Drip sequences
- Better n8n integration
- Recommended when volume justifies cost

---

# ⭐ REVIEW COLLECTION AUTOMATION {#review-automation}

## Email Template — Review Request

**Subject:** Quick favor — how was your experience with Nivy Digital?

**Body:**

> Hi [First Name],
> 

> 
> 

> It's been a few days since we wrapped up [project/service], and I wanted to personally check in.
> 

> 
> 

> If you're happy with the results, could you spare 2 minutes to leave us a review? It genuinely helps us grow and helps other businesses find us.
> 

> 
> 

> ⭐ Leave a Google Review → [Link]
> 

> ⭐ Review us on Clutch → [Link]
> 

> ⭐ Review us on Trustpilot → [Link]
> 

> 
> 

> It takes less than 2 minutes and means the world to us.
> 

> 
> 

> Thank you,
> 

> [Founder Name]
> 

> Nivy Digital
> 

## Target: 5+ reviews on each platform within 90 days

---

# 📧 EMAIL SEQUENCE AUTOMATION {#email-sequences}

## Welcome Sequence (5 Emails — New Lead)

| Email | Timing | Subject | Goal |
| --- | --- | --- | --- |
| Email 1 | Immediately | "Welcome to Nivy Digital — What happens next" | Set expectations + book call |
| Email 2 | Day 2 | "Here's what our clients say" | Social proof + testimonials |
| Email 3 | Day 4 | "The most common question we get" | FAQ + education |
| Email 4 | Day 7 | "Free guide: 10 tasks to delegate today" | Lead magnet + value |
| Email 5 | Day 10 | "Still exploring? Let's talk" | Last push to book call |

## Cold Lead Re-engagement (3 Emails)

| Email | Timing | Subject | Goal |
| --- | --- | --- | --- |
| Email 1 | Day 0 | "Still thinking about it?" | Re-activate interest |
| Email 2 | Day 3 | "A case study you might like" | Proof + value |
| Email 3 | Day 7 | "Should I close your file?" | Create urgency |

## All sequences built in: **Brevo** (free) or **Mautic** (open source)

---

*Last updated: May 8, 2026 | Owner: Nivy Digital Founder*

*Part of: MASTER BUILD PLAN — World-Class Sales & Marketing Department*

---

📋 **PAGE METADATA**

- **Section:** SD-08 — Automation Systems & n8n Workflow Library
- **Parent:** [🗺️ MASTER BUILD PLAN](%F0%9F%8F%A2%20SALES%20&%20MARKETING%20DEPARTMENT%20%E2%80%94%20The%20Nivy%206d7eb94b1a2a82f4934e011a405261c4.md)
- **Owner:** Nivy Digital Founder
- **Status:** ✅ Complete — Phase 4 Metadata Updated May 8, 2026
- **Last Updated:** May 8, 2026
- **Version:** 1.1
- **Tags:** `SD-08` `automation` `n8n` `workflows` `CRM` `chatbot` `WhatsApp` `email-sequences` `nivy-digital`
- **Related Pages:** [Department Home](%F0%9F%8E%AF%20SD-00%20%E2%80%94%20Department%20Home%20&%20Master%20Index%20ac3eb94b1a2a828bb42e014281f1b2cc.md) | [SD-04 Outbound](%F0%9F%93%A3%20SD-04%20%E2%80%94%20Outbound%20Outreach%20Hub%208f3eb94b1a2a8394a3b101cba29ef1ac.md) | [SD-07 Sales](%F0%9F%92%B0%20SD-07%20%E2%80%94%20Sales%20Conversion%20Hub%20196eb94b1a2a827cb19601304d6378e8.md) | [SD-09 CRM](%F0%9F%8E%AF%20SD-07b%20%E2%80%94%20Targets,%20KPI%20Dashboard%20&%20CRM%20Setup%20f7deb94b1a2a826e919781bce9b86092.md)

---

[n8n Workflow 3 — [Cal.com](http://Cal.com) Booking → CRM](n8n%20Workflow%203%20%E2%80%94%20Cal%20com%20Booking%20%E2%86%92%20CRM%20d66eb94b1a2a82f7b6f381b90f214f1c.md)