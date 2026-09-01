# Sales Funnel Automation Stack — n8n-Linked Guide

**Status:** Built 2026-07-24, companion document to `AI-Marketing-Automation-Stack.md`, same table format (Free/OSS-first, one function per table). Written directly against the Nivy Empires funnel already mapped in `Automated Sales Funnel` (the ASCII "Business Operating System" doc in the Growth-Engine export) and the `Automation/README.md` decision to link live templates from **[nivyindia/all_n8n_templates_collection](https://github.com/nivyindia/all_n8n_templates_collection)** before any workflow is actually built and exported.

**Rule followed throughout:** every stage that is automatable gets the *actual* template link sitting right next to it — not a placeholder, not "search for a template." Where the repository does not have a template for a stage (flagged in §9), that gap is stated plainly instead of inventing a link.

---

## 1. How This Maps to the Existing Funnel

`Automated Sales Funnel` already defines the shape: **10 lead-source channels → Lead Collection Hub → CRM → AI Qualification Engine → Sales Pipeline → Client Onboarding → Service Delivery → Client Success → Revenue Expansion**, closed by a Master Loop back into more leads. This document is that same shape, stage by stage, with the n8n template that automates each arrow.

Everything here assumes the same Layer 2 as the marketing stack: **n8n**, self-hosted and free, is the connective tissue. Layer 1 (AI Brain — Claude/ChatGPT hosted, or Ollama self-hosted) sits behind every AI-node step below.

---

## 2. Full Funnel Automation Flow

```
LEAD SOURCES (Inbound · Outbound · Growth Hack · Paid · Marketplace · Partnerships · Referrals · Communities · Assets · Offline)
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 1 — LEAD GENERATION / SCRAPING                                     │
│  Web scrape → AI agent that can scrape webpages                          │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  OpenAI_and_LLMs/AI%20agent%20that%20can%20scrape%20webpages.json        │
│                                                                            │
│  Competitor / market scrape → Automate Competitor Research (Exa.ai +      │
│  Notion + AI Agents)                                                      │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Notion/Automate%20Competitor%20Research%20with%20Exa.ai,%20Notion%20    │
│  and%20AI%20Agents.json                                                   │
└───────────────────────────────────────────────────────────────────────────┘
        │  scraped/collected leads
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 2 — LEAD CAPTURE HUB (forms, calls, chat, manual, API)             │
│  Form → welcome email → Sheets pipeline, and AI call-log capture from    │
│  Vapi.ai/Bland.ai → Google Sheets — browse the Forms & Surveys folder    │
│  (repo doesn't expose a stable direct-file link for these two — see §9): │
│  https://github.com/nivyindia/all_n8n_templates_collection/tree/main/    │
│  Forms_and_Surveys                                                        │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 3 — CRM INGESTION + ENRICHMENT                                     │
│  Enrich company/org data → Enrich Pipedrive's Organization Data with      │
│  OpenAI GPT-4o & Notify it in Slack                                      │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Slack/Enrich%20Pipedrive_s%20Organization%20Data%20with%20OpenAI%20     │
│  GPT-4o%20&%20Notify%20it%20in%20Slack.json                              │
│                                                                            │
│  ERPNext-native lead + inquiry automation → AI-Driven Lead Management     │
│  and Inquiry Automation with ERPNext & n8n                               │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  OpenAI_and_LLMs/AI-Driven%20Lead%20Management%20and%20Inquiry%20        │
│  Automation%20with%20ERPNext%20&%20n8n.json                              │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 4 — AI QUALIFICATION ENGINE                                        │
│  (Budget · Need · Authority · Timeline · Intent · Industry · Country ·   │
│   Engagement)                                                             │
│  Qualify new leads in Google Sheets via OpenAI's GPT-4                   │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20   │
│  Sheets%20via%20OpenAI_s%20GPT-4.json                                    │
└───────────────────────────────────────────────────────────────────────────┘
        │
   ┌────┴─────┬──────────────┐
   ▼          ▼              ▼
 HOT        WARM            COLD
   │          │              │
   ▼          ▼              ▼
Sales     Auto-Nurture   Long-Term Nurture
Team      (email/WhatsApp)  (email/WhatsApp — same templates as Stage 5)
   │
   ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 5 — OUTREACH & NURTURE (Email · WhatsApp · LinkedIn)              │
│  Cold email (from a lead sheet) → LeadPilot Lite - AI Cold Email Writer   │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Gmail_and_Email_Automation/LeadPilot%20Lite%20-%20AI%20Cold%20Email%20  │
│  Writer.json                                                             │
│                                                                            │
│  Cold email (grounded in the lead's real website, no invented claims) →  │
│  Website-Grounded Cold Email Writer                                      │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Gmail_and_Email_Automation/Website-Grounded%20Cold%20Email%20Writer.json│
│                                                                            │
│  Inbound reply drafting → Compose reply draft in Gmail with OpenAI       │
│  Assistant                                                                │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Gmail_and_Email_Automation/Compose%20reply%20draft%20in%20Gmail%20with% │
│  20OpenAI%20Assistant.json                                               │
│                                                                            │
│  Human-in-the-loop reply QC → A Very Simple "Human in the Loop" Email    │
│  Response System Using AI and IMAP                                       │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Gmail_and_Email_Automation/A%20Very%20Simple%20_Human%20in%20the%20     │
│  Loop_%20Email%20Response%20System%20Using%20AI%20and%20IMAP.json        │
│                                                                            │
│  WhatsApp first-touch bot → Building Your First WhatsApp Chatbot         │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  WhatsApp/Building%20Your%20First%20WhatsApp%20Chatbot.json              │
│                                                                            │
│  WhatsApp RAG chatbot (answers from your own docs) → Complete business   │
│  WhatsApp AI-Powered RAG Chatbot using OpenAI                            │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  WhatsApp/Complete%20business%20WhatsApp%20AI-Powered%20RAG%20Chatbot%20 │
│  using%20OpenAI.json                                                     │
│                                                                            │
│  WhatsApp reply quality pass → Respond to WhatsApp Messages with AI      │
│  Like a Pro!                                                             │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  WhatsApp/Respond%20to%20WhatsApp%20Messages%20with%20AI%20Like%20a%20   │
│  Pro!.json                                                               │
│                                                                            │
│  One inbox for WhatsApp + Instagram DM + Messenger → Receive and Send    │
│  Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano  │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  WhatsApp/Receive%20and%20Send%20Messages%20Across%20WhatsApp%2C%20      │
│  Instagram%20and%20Facebook%20Messenger%20with%20Fiwano.json             │
│                                                                            │
│  LinkedIn outreach posts (from a Notion content queue) → Automate        │
│  LinkedIn Outreach with Notion and OpenAI                                │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json│
└───────────────────────────────────────────────────────────────────────────┘
        │  reply / meeting booked
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 6 — DISCOVERY CALL → MEETING PREP → NOTES                        │
│  Pre-call research pushed to WhatsApp → Automate Sales Meeting Prep with  │
│  AI & APIFY Sent To WhatsApp                                             │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  WhatsApp/Automate%20Sales%20Meeting%20Prep%20with%20AI%20&%20APIFY%20   │
│  Sent%20To%20WhatsApp.json                                               │
│                                                                            │
│  Call/meeting → tasks + client follow-up → AI Agent for project          │
│  management and meetings with Airtable and Fireflies                     │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Airtable/AI%20Agent%20for%20project%20management%20and%20meetings%20    │
│  with%20Airtable%20and%20Fireflies.json                                  │
│                                                                            │
│  Live sales-chat assistant tied to CRM → vAssistant for Hubspot Chat      │
│  using OpenAi and Airtable                                               │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Airtable/vAssistant%20for%20Hubspot%20Chat%20using%20OpenAi%20and%20     │
│  Airtable.json                                                            │
└───────────────────────────────────────────────────────────────────────────┘
        │  needs assessment → solution design
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 7 — PROPOSAL / QUOTATION / CONTRACT DRAFTING                      │
│  Draft grounded in company knowledge base → Notion knowledge base AI     │
│  assistant                                                                │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Notion/Notion%20knowledge%20base%20AI%20assistant.json                  │
│                                                                            │
│  Or, if the knowledge base lives in Drive → RAG Chatbot for Company       │
│  Documents using Google Drive and Gemini                                 │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Google_Drive_and_Google_Sheets/RAG%20Chatbot%20for%20Company%20         │
│  Documents%20using%20Google%20Drive%20and%20Gemini.json                  │
│                                                                            │
│  Client Q&A on the proposal/contract PDF once sent → Ask questions        │
│  about a PDF using AI                                                     │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  PDF_and_Document_Processing/Ask%20questions%20about%20a%20PDF%20using%20│
│  AI.json                                                                  │
│                                                                            │
│  E-signature step: no free/OSS n8n template found in this repo for this  │
│  exact stage — flagged, not invented. See §9.                           │
└───────────────────────────────────────────────────────────────────────────┘
        │  signed
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 8 — INVOICE → PAYMENT                                             │
│  Structured invoice-data extraction (for reconciliation, AP automation,  │
│  or turning a scanned invoice into CRM/accounting records) → Invoice     │
│  data extraction with LlamaParse and OpenAI                              │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20       │
│  LlamaParse%20and%20OpenAI.json                                          │
│                                                                            │
│  Same, with human-in-the-loop validation + auto-retraining → Invoice     │
│  data extraction with human-in-the-loop validation and auto-training     │
│  using Cradl AI                                                          │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20human- │
│  in-the-loop%20validation%20and%20auto-training%20using%20Cradl%20AI.json│
│                                                                            │
│  Invoice generation + payment-link send: no free/OSS n8n template found  │
│  in this repo — flagged, not invented. See §9.                          │
└───────────────────────────────────────────────────────────────────────────┘
        │  CLIENT WON
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 9 — CLIENT ONBOARDING                                             │
│  Form submit → welcome email → Sheets onboarding pipeline — browse the   │
│  Forms & Surveys folder (see §9 on why this is a folder link, not a      │
│  direct file link):                                                      │
│  https://github.com/nivyindia/all_n8n_templates_collection/tree/main/    │
│  Forms_and_Surveys                                                        │
│                                                                            │
│  Onboarding chat / doc collection over WhatsApp → reuse the WhatsApp RAG │
│  chatbot from Stage 5 (same link)                                        │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 10 — SERVICE DELIVERY / SUPPORT                                   │
│  Support ticketing from a chat mention → Customer Support Channel and    │
│  Ticketing System with Slack and Linear                                 │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Slack/Customer%20Support%20Channel%20and%20Ticketing%20System%20with%20 │
│  Slack%20and%20Linear.json                                               │
│                                                                            │
│  Client-sentiment tracking on open issues → Sentiment Analysis Tracking  │
│  on Support Issues with Linear and Slack                                 │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Slack/Sentiment%20Analysis%20Tracking%20on%20Support%20Issues%20with%20 │
│  Linear%20and%20Slack.json                                               │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 11 — CLIENT SUCCESS (feedback → review → testimonial → referral)  │
│  Feedback sentiment scoring → AI Customer feedback sentiment analysis    │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  OpenAI_and_LLMs/AI%20Customer%20feedback%20sentiment%20analysis.json    │
│                                                                            │
│  Positive feedback logged for testimonial/case-study sourcing → Add      │
│  positive feedback messages to a table in Notion                        │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20    │
│  Notion.json                                                             │
│                                                                            │
│  Google Review request automation: the Growth-Engine export references  │
│  its own "n8n Workflow 4 — Review Request Automation" as a planned       │
│  build, not a repo template — no matching free template found in this   │
│  repo either. Flagged, not invented. See §9.                            │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 12 — REVENUE EXPANSION (cross-sell, upsell, referral, content     │
│  repurposing of case studies for the top of funnel again)                │
│  One case study/article → 4 social platforms → FlowScribe Lite - AI      │
│  Content Repurposing (4 Platforms)                                       │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Instagram_Twitter_Social_Media/FlowScribe%20Lite%20-%20AI%20Content%20  │
│  Repurposing%204%20Platforms.json                                        │
│                                                                            │
│  Article/case-study → grounded X thread + LinkedIn post → Grounded       │
│  Article to Thread and LinkedIn Post                                     │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Instagram_Twitter_Social_Media/Grounded%20Article%20to%20Thread%20and%20│
│  LinkedIn%20Post.json                                                    │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STAGE 13 — MANAGEMENT DASHBOARD / WEEKLY AI REPORTS                     │
│  Auto-summarize new reporting docs into a tracker → Summarize the New    │
│  Documents from Google Drive and Save Summary in Google Sheet            │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Google_Drive_and_Google_Sheets/Summarize%20the%20New%20Documents%20from │
│  %20Google%20Drive%20and%20Save%20Summary%20in%20Google%20Sheet.json     │
│                                                                            │
│  Query the pipeline tracker in plain English → Chat with a Google Sheet  │
│  using AI                                                                 │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Google_Drive_and_Google_Sheets/Chat%20with%20a%20Google%20Sheet%20using │
│  %20AI.json                                                              │
│                                                                            │
│  Social/campaign performance → automated email report → Social Media     │
│  Analysis and Automated Email Generation                                 │
│  https://github.com/nivyindia/all_n8n_templates_collection/blob/main/    │
│  Instagram_Twitter_Social_Media/Social%20Media%20Analysis%20and%20       │
│  Automated%20Email%20Generation.json                                     │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
              MASTER LOOP → back to Stage 1 (more leads, repeat forever)
```

This is the same Master Loop shape as `Automated Sales Funnel`'s founder dashboard view — this document just puts a working, importable n8n template under every single arrow in that diagram, so no step is left as "AI Agent" in name only.

---

## 3. Stage-by-Stage Reference Tables

### 3.1 Lead Generation & Scraping

| Source Channel (from `Automated Sales Funnel`) | Automation | n8n Template |
|---|---|---|
| Google Maps, Apollo, Crunchbase, Directories (Outbound) | General-purpose scrape agent — point it at any list/directory page | [AI agent that can scrape webpages](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/OpenAI_and_LLMs/AI%20agent%20that%20can%20scrape%20webpages.json) |
| Competitor tracking (Growth Hack) | Finds similar companies, compiles overviews/reviews into a table | [Automate Competitor Research with Exa.ai, Notion and AI Agents](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Notion/Automate%20Competitor%20Research%20with%20Exa.ai,%20Notion%20and%20AI%20Agents.json) |
| Cold Calling (Outbound) | Logs Vapi.ai/Bland.ai call transcripts to a sheet automatically | Forms & Surveys folder — [browse here](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Forms_and_Surveys) (see §9) |

### 3.2 Lead Capture Hub

| Capture Point | Automation | n8n Template |
|---|---|---|
| Website form / landing page | Form submit → welcome email → adds row to Sheets pipeline automatically | [Forms & Surveys folder](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Forms_and_Surveys) (see §9) |
| Appointment/booking requests | AI qualifies the appointment request before it hits a human calendar | [Forms & Surveys folder](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Forms_and_Surveys) (see §9) |

### 3.3 CRM Ingestion & Enrichment

| Function | n8n Template |
|---|---|
| Auto-enrich a new company/org record with a website summary, then notify the team | [Enrich Pipedrive's Organization Data with OpenAI GPT-4o & Notify it in Slack](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Slack/Enrich%20Pipedrive_s%20Organization%20Data%20with%20OpenAI%20GPT-4o%20&%20Notify%20it%20in%20Slack.json) |
| ERPNext-native lead + inquiry intake and routing | [AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/OpenAI_and_LLMs/AI-Driven%20Lead%20Management%20and%20Inquiry%20Automation%20with%20ERPNext%20&%20n8n.json) |
| Chat with the CRM sheet directly for status checks | [Chat with a Google Sheet using AI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Google_Drive_and_Google_Sheets/Chat%20with%20a%20Google%20Sheet%20using%20AI.json) |

### 3.4 AI Qualification Engine (Budget/Need/Authority/Timeline/Intent)

| Function | n8n Template |
|---|---|
| Score and tag every new lead row (hot/warm/cold) as it lands in Sheets | [Qualify new leads in Google Sheets via OpenAI's GPT-4](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) |

### 3.5 Outreach & Nurture

| Channel | Function | n8n Template |
|---|---|---|
| Email | Personalized cold email from a lead list | [LeadPilot Lite - AI Cold Email Writer](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Gmail_and_Email_Automation/LeadPilot%20Lite%20-%20AI%20Cold%20Email%20Writer.json) |
| Email | Cold email grounded only in the lead's real website (flags thin/broken sites instead of inventing facts) | [Website-Grounded Cold Email Writer](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Gmail_and_Email_Automation/Website-Grounded%20Cold%20Email%20Writer.json) |
| Email | Draft replies to inbound interest for human approval | [Compose reply draft in Gmail with OpenAI Assistant](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Gmail_and_Email_Automation/Compose%20reply%20draft%20in%20Gmail%20with%20OpenAI%20Assistant.json) |
| Email | Full human-in-the-loop reply QC gate over IMAP | [A Very Simple "Human in the Loop" Email Response System Using AI and IMAP](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Gmail_and_Email_Automation/A%20Very%20Simple%20_Human%20in%20the%20Loop_%20Email%20Response%20System%20Using%20AI%20and%20IMAP.json) |
| WhatsApp | First bot / lead capture over WhatsApp | [Building Your First WhatsApp Chatbot](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Building%20Your%20First%20WhatsApp%20Chatbot.json) |
| WhatsApp | Full RAG chatbot answering from company docs | [Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Complete%20business%20WhatsApp%20AI-Powered%20RAG%20Chatbot%20using%20OpenAI.json) |
| WhatsApp | Higher-quality AI reply pass | [Respond to WhatsApp Messages with AI Like a Pro!](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Respond%20to%20WhatsApp%20Messages%20with%20AI%20Like%20a%20Pro!.json) |
| WhatsApp + Instagram DM + Messenger | One unified inbox/trigger-action set across all three | [Receive and Send Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Receive%20and%20Send%20Messages%20Across%20WhatsApp%2C%20Instagram%20and%20Facebook%20Messenger%20with%20Fiwano.json) |
| LinkedIn | Post drafting/scheduling from a Notion content queue | [Automate LinkedIn Outreach with Notion and OpenAI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) |

> Same §5 platform-risk caution as the marketing stack applies here: AI drafts and shortlists, a human sends at LinkedIn/WhatsApp connection-request volumes, to avoid account-limit risk.

### 3.6 Discovery Call → Meeting Prep → Notes

| Function | n8n Template |
|---|---|
| Pre-call research pushed straight to the rep's WhatsApp | [Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Automate%20Sales%20Meeting%20Prep%20with%20AI%20&%20APIFY%20Sent%20To%20WhatsApp.json) |
| Turn a Fireflies call transcript into Airtable tasks + client follow-up | [AI Agent for project management and meetings with Airtable and Fireflies](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Airtable/AI%20Agent%20for%20project%20management%20and%20meetings%20with%20Airtable%20and%20Fireflies.json) |
| Live chat-based sales assistant tied to the CRM | [vAssistant for Hubspot Chat using OpenAi and Airtable](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Airtable/vAssistant%20for%20Hubspot%20Chat%20using%20OpenAi%20and%20Airtable.json) |

### 3.7 Proposal / Quotation / Contract

| Function | n8n Template |
|---|---|
| Draft proposal copy grounded in your own SOPs/offers (Notion-based KB) | [Notion knowledge base AI assistant](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Notion/Notion%20knowledge%20base%20AI%20assistant.json) |
| Same, if the KB lives in Google Drive | [RAG Chatbot for Company Documents using Google Drive and Gemini](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Google_Drive_and_Google_Sheets/RAG%20Chatbot%20for%20Company%20Documents%20using%20Google%20Drive%20and%20Gemini.json) |
| Let the prospect ask questions about the sent proposal/contract PDF | [Ask questions about a PDF using AI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/PDF_and_Document_Processing/Ask%20questions%20about%20a%20PDF%20using%20AI.json) |
| E-signature | **Gap — see §9** |

### 3.8 Invoice → Payment

| Function | n8n Template |
|---|---|
| Extract structured line-items/totals from an invoice PDF | [Invoice data extraction with LlamaParse and OpenAI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) |
| Same, with a human-review gate on low-confidence fields and auto-retraining | [Invoice data extraction with human-in-the-loop validation and auto-training using Cradl AI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20human-in-the-loop%20validation%20and%20auto-training%20using%20Cradl%20AI.json) |
| Invoice *generation* + payment-link send | **Gap — see §9** |

### 3.9 Client Onboarding

| Function | n8n Template |
|---|---|
| Form → welcome email → onboarding pipeline in Sheets | [Forms & Surveys folder](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Forms_and_Surveys) (see §9) |
| Document collection / onboarding Q&A over WhatsApp | Reuse [Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/WhatsApp/Complete%20business%20WhatsApp%20AI-Powered%20RAG%20Chatbot%20using%20OpenAI.json) |

### 3.10 Service Delivery / Support

| Function | n8n Template |
|---|---|
| Turn a flagged chat message into a ticket automatically | [Customer Support Channel and Ticketing System with Slack and Linear](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Slack/Customer%20Support%20Channel%20and%20Ticketing%20System%20with%20Slack%20and%20Linear.json) |
| Track client sentiment on open issues, alert the team on negative trend | [Sentiment Analysis Tracking on Support Issues with Linear and Slack](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Slack/Sentiment%20Analysis%20Tracking%20on%20Support%20Issues%20with%20Linear%20and%20Slack.json) |

### 3.11 Client Success (Feedback → Review → Testimonial → Referral)

| Function | n8n Template |
|---|---|
| Score incoming feedback for sentiment | [AI Customer feedback sentiment analysis](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/OpenAI_and_LLMs/AI%20Customer%20feedback%20sentiment%20analysis.json) |
| Route high-scoring feedback into a Notion table for testimonial/case-study sourcing | [Add positive feedback messages to a table in Notion](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) |
| Google Review request send | **Gap — see §9** |

### 3.12 Revenue Expansion (Cross-sell / Upsell / Referral / Repurposing)

| Function | n8n Template |
|---|---|
| Turn one case study into 4 platform-native social posts | [FlowScribe Lite - AI Content Repurposing (4 Platforms)](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Instagram_Twitter_Social_Media/FlowScribe%20Lite%20-%20AI%20Content%20Repurposing%204%20Platforms.json) |
| Turn a case study/article into a grounded X thread + LinkedIn post | [Grounded Article to Thread and LinkedIn Post](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Instagram_Twitter_Social_Media/Grounded%20Article%20to%20Thread%20and%20LinkedIn%20Post.json) |

### 3.13 Management Dashboard / Weekly AI Reports

| Function | n8n Template |
|---|---|
| Auto-summarize new reports/docs into a tracking sheet | [Summarize the New Documents from Google Drive and Save Summary in Google Sheet](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Google_Drive_and_Google_Sheets/Summarize%20the%20New%20Documents%20from%20Google%20Drive%20and%20Save%20Summary%20in%20Google%20Sheet.json) |
| Query the pipeline/CRM tracker in plain English | [Chat with a Google Sheet using AI](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Google_Drive_and_Google_Sheets/Chat%20with%20a%20Google%20Sheet%20using%20AI.json) |
| Campaign/social performance → automated email report | [Social Media Analysis and Automated Email Generation](https://github.com/nivyindia/all_n8n_templates_collection/blob/main/Instagram_Twitter_Social_Media/Social%20Media%20Analysis%20and%20Automated%20Email%20Generation.json) |

---

## 4. Where These Templates Live in the Repo

Every link above resolves inside one repository: **[nivyindia/all_n8n_templates_collection](https://github.com/nivyindia/all_n8n_templates_collection)** (a fork of `enescingoz/awesome-n8n-templates`, 280+ templates across 18 categories). The relevant category folders used above, if you'd rather browse than follow a direct file link:

- [Gmail_and_Email_Automation](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Gmail_and_Email_Automation)
- [WhatsApp](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/WhatsApp)
- [Google_Drive_and_Google_Sheets](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Google_Drive_and_Google_Sheets)
- [Notion](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Notion)
- [Airtable](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Airtable)
- [Slack](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Slack)
- [OpenAI_and_LLMs](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/OpenAI_and_LLMs)
- [PDF_and_Document_Processing](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/PDF_and_Document_Processing)
- [Instagram_Twitter_Social_Media](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Instagram_Twitter_Social_Media)
- [Forms_and_Surveys](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Forms_and_Surveys)

Quick-start (same five steps the repo's own README gives): sign up for [n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) → download the `.json` → **Workflows → Import from File** → configure credentials for each connected service → activate.

---

## 5. What n8n Automates vs. What Stays Human

Same principle as the marketing stack's §5/§9: AI drafts, a human approves anything client-facing, contractual, or platform-risk-sensitive before it goes out.

| Stays human regardless of tooling |
|---|
| Final proposal/contract sign-off and negotiation terms |
| Signing the contract (e-signature step itself) |
| Sending outbound at LinkedIn/WhatsApp connection-request volumes (account-risk ceiling, not a fixed number) |
| Approving AI-drafted replies before they leave the human-in-the-loop email/WhatsApp templates above |
| Relationship-building conversation itself, on calls and in community groups |

---

## 6. Two Places This Already Lives in the Growth-Engine Repo

- `Automated Sales Funnel` — the ASCII "Nivy Empires Business Operating System" founder-dashboard view this whole document is built to automate, stage by stage.
- `Automation/README.md` — the decision (Correction Batch 0) to treat `Automation/` as the landing spot for *exported* workflow JSON once any of the templates above are actually imported into a live n8n instance and adapted to this business — one file per workflow, named after the stage it serves (their own example: `sales-06-lead-extraction.json`). This document is the template-linking step that decision assumes comes first; it is not itself the exported-workflow step.

---

## 7. Reconciliation Note

Two of the sub-stages this document names by function only, without a direct file link, both live under **Forms_and_Surveys**: the "form → welcome email → Sheets pipeline" onboarding template, and the "call log → Sheets via Vapi.ai/Bland.ai webhook" template. Both descriptions come from the upstream repo's own README, but the direct file path wasn't resolvable at write time — so those two rows point to the *folder*, not a specific file, rather than risk a broken or guessed link. Open the folder and match the description; it's a short list.

---

## 8. Cross-References

- `Automated Sales Funnel 389e5082b9d480f0bb22dc586a0249d7.md` — the founder-dashboard flow this document automates
- `Automation/README.md` — the exported-JSON landing-spot decision this document's linking work feeds into
- `AI-Marketing-Automation-Stack (1).md` — sibling document, same table format, covers the marketing side of the same funnel (content, SEO, social, email tooling)
- `#⚡ CJE Automation Flow — How Every Lead Moves Through...`, `#🔥 Sales Funnel Architecture — Enquiry Method + Fu...`, `#🔥 Nivy Digital — Complete Sales Automation via Enq...` — existing Growth-Engine files describing this same funnel in narrative form; this document is their n8n-template-linked execution layer

---

## 9. Gaps Flagged (Not Invented)

Being direct about what the repository does **not** cover, rather than forcing a link that doesn't fit:

1. **E-signature** (Stage 7) — no free/OSS n8n template for this in the repo. Handle this stage with a dedicated e-signature tool's own native automation (most offer webhooks n8n can trigger off directly), or check the repo's [Other_Integrations_and_Use_Cases](https://github.com/nivyindia/all_n8n_templates_collection/tree/main/Other_Integrations_and_Use_Cases) folder directly for anything newer.
2. **Invoice generation + payment-link send** (Stage 8) — the repo has strong invoice *data-extraction* templates (linked in §3.8) but nothing for generating and sending an invoice in the first place. Same recommendation: your accounting/invoicing tool's own webhook, triggered by n8n.
3. **Google Review request send** (Stage 11) — the Growth-Engine export itself only references this as a planned build ("n8n Workflow 4 — Review Request Automation"), not as something already sourced from a template; no matching free template turned up in this repo either.
4. **Forms & Surveys direct links** (Stages 2 and 9) — folder-level link only; see §7.

If any of these get built as custom n8n workflows in a live instance, that's exactly what `Automation/README.md` says the `Automation/` folder is for — export the JSON there, named after the stage (e.g. `sales-07-esign-trigger.json`).
