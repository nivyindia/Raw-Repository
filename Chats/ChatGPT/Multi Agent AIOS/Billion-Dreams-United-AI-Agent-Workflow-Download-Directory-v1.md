# BILLION DREAMS UNITED
# AI AGENT + WORKFLOW DOWNLOAD DIRECTORY
## Version 1 — Open-Source-First Implementation Catalog

**Date:** 2026-09-01

---

# 1. PURPOSE

This file is the implementation/download directory for:

**Billion Dreams United — AI-Native Company OS v7**

It answers four questions for every major component:

1. What agent/tool/software do we need?
2. What does it do?
3. Where in the Marketing/Sales funnel is it used?
4. Where can the implementation be obtained?

IMPORTANT:

- A framework/repository is not the same thing as a ready-made agent.
- Most AI agents in the v7 blueprint are **roles/capabilities that must be built/configured** inside the listed open-source frameworks.
- Therefore, this directory distinguishes:
  - `READY SOFTWARE`
  - `AGENT FRAMEWORK`
  - `BUILD-REQUIRED AGENT`
  - `WORKFLOW BUILD REQUIRED`
- Do not assume that a GitHub repository contains a finished production agent for the exact business task.

---

# 2. MASTER SOFTWARE / AGENT PLATFORM DIRECTORY

| ID | Software / Platform | Type | Main Purpose | Used For | Source / Download |
|---|---|---|---|---|---|
| P01 | Odoo Community | Business OS / CRM | CRM, Sales, Projects, Invoicing, Contacts | S13, S38–S42, S43–S54, M22 | https://github.com/odoo/odoo |
| P02 | n8n | Workflow Automation | Event-driven integrations and deterministic workflows | All funnel stages | https://github.com/n8n-io/n8n |
| P03 | LangGraph | Agent Orchestration | Stateful agent workflows, persistence, HITL | Agent control plane | https://github.com/langchain-ai/langgraph |
| P04 | CrewAI | Multi-Agent Framework | Agent teams and collaborative workflows | Research, marketing, sales | https://github.com/crewAIInc/crewAI |
| P05 | Dify | AI App / Agent Platform | Agentic workflows, RAG, model management | Marketing + Sales agents | https://github.com/langgenius/dify |
| P06 | Ollama | Local AI Runtime | Run local/open models | All AI agents | https://github.com/ollama/ollama |
| P07 | vLLM | LLM Inference | High-throughput self-hosted inference | Production AI | https://github.com/vllm-project/vllm |
| P08 | LiteLLM | Model Gateway | One interface for multiple LLM providers | AI model routing | https://github.com/BerriAI/litellm |
| P09 | Qdrant | Vector Database | Semantic memory / RAG | Knowledge + agent memory | https://github.com/qdrant/qdrant |
| P10 | PostgreSQL | Database | CRM events, metrics, agent state | Entire OS | https://www.postgresql.org/ |
| P11 | MinIO | Object Storage | Files, reports, media, artifacts | Proposals, reports, content | https://github.com/minio/minio |
| P12 | Mautic | Marketing Automation | Lead nurture, segmentation, campaigns | M17, inbound nurture | https://github.com/mautic/mautic |
| P13 | Postal | Email Infrastructure | Self-hosted transactional email | S16, M17 | https://github.com/postalserver/postal |
| P14 | Cal.com | Scheduling | Meeting booking | S28 | https://github.com/calcom/cal.com |
| P15 | Chatwoot | Customer Communication | Omnichannel support inbox | M19, S46 | https://github.com/chatwoot/chatwoot |
| P16 | Firecrawl | Web Data / Crawling | Web research and structured extraction | M04–M07, S01–S10 | https://github.com/mendableai/firecrawl |
| P17 | Browser Use | Browser Agent Framework | AI browser control | S05–S10, S17, research | https://github.com/browser-use/browser-use |
| P18 | OpenHands | Coding Agent | AI software development | OS engineering / automation | https://github.com/All-Hands-AI/OpenHands |
| P19 | Metabase | BI | Dashboards and analytics | M21, sales analytics | https://github.com/metabase/metabase |
| P20 | Documenso | E-signature | Contracts and signatures | S36 | https://github.com/documenso/documenso |
| P21 | Nextcloud | File Collaboration | Internal files and documents | Company OS | https://github.com/nextcloud/server |
| P22 | Rocket.Chat | Collaboration | Internal communication / community | Company OS / M19 | https://github.com/RocketChat/Rocket.Chat |
| P23 | Bitwarden / Vaultwarden | Secrets | Credential management | All integrations | https://github.com/dani-garcia/vaultwarden |
| P24 | Docker | Infrastructure | Containerized deployment | Entire stack | https://github.com/moby/moby |
| P25 | Open WebUI | AI Interface | Local LLM interface | Internal AI access | https://github.com/open-webui/open-webui |

---

# 3. IMPORTANT OPEN-SOURCE STATUS NOTES

The preferred architecture is open-source-first, but not every item has identical licensing.

## Dify

Dify describes itself as an open-source LLM application development platform with agent workflows, RAG, model management and observability. Verify the current license and edition before deployment. citeturn0search9

## LangGraph

LangGraph is an open framework for building stateful agent applications with durable execution, persistence and human-in-the-loop capabilities. citeturn0search13

## CrewAI

CrewAI is an open-source framework for orchestrating AI agent teams using Crews and event-driven Flows. citeturn0search16

## Mautic

Mautic is an open-source marketing automation platform. citeturn0search0turn0search14

## Cal.com

Cal.com is open-source, but its repository uses an open-core model with some enterprise features under commercial licensing. If strict 100% open-source is required, evaluate Cal.diy as an alternative. citeturn0search3turn0search17

## Chatwoot

Chatwoot is an open-source customer support platform with omnichannel communication and API integrations. citeturn0search12

## Browser Use

Browser Use is an open browser-agent framework for allowing AI agents to control websites. citeturn0search11

## OpenHands

OpenHands is an AI software-development agent platform capable of modifying code, running commands, browsing and calling APIs. citeturn0search18

---

# 4. AGENT DIRECTORY — STRATEGY

These are **agent roles to build**, not necessarily downloadable standalone agents.

| Agent ID | Agent | What It Does | Funnel | Recommended Platform | Build Status |
|---|---|---|---|---|---|
| A001 | Market Research Agent | Research markets, demand, trends, opportunities | S01 | Dify + LangGraph + Firecrawl | Build |
| A002 | ICP Strategist | Defines ideal customer profile | S02 | Dify | Build |
| A003 | Buyer Persona Agent | Builds decision-maker personas | S03 | Dify + Qdrant | Build |
| A004 | Competitor Intelligence Agent | Researches competitors, offers, positioning, gaps | S04 | Firecrawl + Dify | Build |
| A005 | Channel Strategy Agent | Chooses best acquisition channels | M02 | LangGraph + Metabase | Build |
| A006 | Offer Strategy Agent | Designs offer/package recommendations | M03/S34 | Dify + Odoo | Build |
| A007 | Brand Strategist | Maintains brand positioning and voice | M01 | Dify + Qdrant | Build |
| A008 | Messaging Agent | Creates ICP-specific messaging | M03/S22 | Dify | Build |
| A009 | Content Strategist | Plans content by audience/funnel stage | M03/M08 | Dify + Qdrant | Build |
| A010 | Editorial Planner | Builds content calendar | M08 | Dify + n8n | Build |

---

# 5. AGENT DIRECTORY — SEO

| Agent ID | Agent | What It Does | Funnel | Recommended Platform | Download / Build |
|---|---|---|---|---|---|
| A011 | SEO Keyword Agent | Finds and clusters keywords by intent | M04 | Dify + Firecrawl | Build |
| A012 | On-Page SEO Agent | Audits titles, headings, links, semantic coverage | M05 | Dify + Firecrawl | Build |
| A013 | Technical SEO Agent | Finds crawl/index/technical issues | M06 | Firecrawl + browser tooling | Build |
| A014 | Authority Building Agent | Finds backlink/PR/collaboration opportunities | M07 | Firecrawl + Dify | Build |
| A015 | SEO Content Gap Agent | Finds missing topics and competitor gaps | M04/M07 | Firecrawl + Qdrant | Build |

---

# 6. AGENT DIRECTORY — CONTENT

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A016 | Long-Form Writer | Creates articles, guides, whitepapers | M09 | Dify + Qdrant | Build |
| A017 | Content Research Agent | Collects research and source material | M09 | Firecrawl + Dify | Build |
| A018 | Content Editor | Improves structure, clarity and consistency | M09 | Dify | Build |
| A019 | Fact/Source Checker | Checks claims against source material | M09 | Dify + Firecrawl | Build |
| A020 | Content Repurposing Agent | Converts one asset into multi-channel content | M10 | Dify | Build |
| A021 | Video Script Agent | Creates video scripts | M13 | Dify | Build |
| A022 | YouTube SEO Agent | Optimizes titles, descriptions, topics | M13 | Dify + research tools | Build |
| A023 | Social Content Agent | Creates channel-specific social content | M11–M16 | Dify | Build |
| A024 | Content Analytics Agent | Measures content performance | M21 | Metabase + AI | Build |

---

# 7. AGENT DIRECTORY — EMAIL / GROWTH / COMMUNITY

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A025 | Email Nurture Agent | Designs nurture sequences and segmentation | M17 | Mautic + Dify | Build |
| A026 | Email Optimization Agent | Improves subject lines, content and timing | M17 | Mautic + Dify | Build |
| A027 | Growth Experiment Agent | Designs and evaluates growth experiments | M18 | LangGraph + PostgreSQL | Build |
| A028 | Community Growth Agent | Plans engagement, moderation and community growth | M19 | Dify + Chatwoot/Rocket.Chat | Build |
| A029 | Partner Discovery Agent | Finds potential partners | M20/S05 | Firecrawl + Browser Use | Build |
| A030 | Partnership Agent | Qualifies and manages partnership opportunities | M20 | Odoo + Dify | Build |
| A031 | PR Research Agent | Finds PR opportunities and relevant publications | M20 | Firecrawl + Dify | Build |
| A032 | Marketing Analytics Agent | Analyzes marketing performance | M21 | Metabase + Dify | Build |
| A033 | Attribution Agent | Connects marketing touches to revenue | M21/M22 | PostgreSQL + Metabase | Build |

---

# 8. AGENT DIRECTORY — LEAD INTELLIGENCE

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A034 | Lead Discovery Agent | Finds target accounts | S05–S06 | Firecrawl + Browser Use | Build |
| A035 | Contact Discovery Agent | Finds relevant decision makers | S07 | Browser Use + Firecrawl | Build |
| A036 | Lead Enrichment Agent | Adds company/person/business context | S08 | Dify + research tools | Build |
| A037 | Data Quality Agent | Cleans and standardizes lead data | S09 | n8n + Python + PostgreSQL | Build |
| A038 | Verification Agent | Verifies company/contact information | S10 | n8n + verification APIs | Build |
| A039 | Lead Scoring Agent | Calculates ICP + intent + engagement score | S11 | Dify + PostgreSQL | Build |
| A040 | Segmentation Agent | Groups leads by relevant attributes | S12 | PostgreSQL + Dify | Build |
| A041 | Account Research Agent | Creates account intelligence briefs | S01–S04/S15 | Firecrawl + Qdrant | Build |
| A042 | Signal Detection Agent | Detects public buying/growth signals | S05/S15 | Firecrawl + Browser Use | Build |

---

# 9. AGENT DIRECTORY — OUTREACH

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A043 | Outreach Strategy Agent | Chooses channel and sequence | S15 | LangGraph + Odoo | Build |
| A044 | Email Outreach Agent | Creates and manages personalized email campaigns | S16 | Mautic + Postal + Dify | Build |
| A045 | LinkedIn Outreach Assistant | Researches and drafts LinkedIn outreach | S17 | Browser Use + Dify | Build |
| A046 | Call Prep Agent | Prepares account/call briefs | S18 | Dify + Odoo | Build |
| A047 | WhatsApp Outreach Agent | Prepares compliant business messages | S19 | Dify + n8n | Build |
| A048 | SMS Outreach Agent | Creates and manages SMS campaign logic | S20 | n8n + messaging adapter | Build |
| A049 | Personalization Agent | Generates account/person-specific messaging | S22 | Dify + Qdrant | Build |
| A050 | Follow-Up Agent | Recommends next follow-up and drafts it | S24 | LangGraph + Odoo | Build |
| A051 | Deliverability Agent | Monitors bounce, complaints, suppression and sending health | S23 | Postal + PostgreSQL | Build |

---

# 10. AGENT DIRECTORY — ENGAGEMENT / CONVERSION

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A052 | Reply Triage Agent | Classifies incoming responses | S25 | Dify + n8n | Build |
| A053 | Objection Handling Agent | Recommends responses to objections | S26 | Dify + Qdrant | Build |
| A054 | Qualification Agent | Scores fit, need, authority, budget and timing | S27 | Dify + Odoo | Build |
| A055 | Meeting Prep Agent | Creates meeting brief and questions | S28–S29 | Dify + Odoo | Build |
| A056 | Sales Copilot | Assists during/after sales calls | S29–S37 | LangGraph + Qdrant | Build |
| A057 | Needs Analysis Agent | Extracts business problems and desired outcomes | S30 | Dify | Build |
| A058 | Solution Mapping Agent | Maps needs to services/deliverables | S31 | Dify + Odoo | Build |
| A059 | Demo Preparation Agent | Prepares demo flow and proof | S32 | Dify | Build |
| A060 | Proposal Agent | Generates proposal drafts | S33 | Dify + Odoo + MinIO | Build |
| A061 | Pricing Agent | Recommends pricing/packages | S34 | Dify + PostgreSQL | Build |
| A062 | Negotiation Copilot | Provides negotiation analysis | S35 | LangGraph + Odoo | Build |
| A063 | Contract Agent | Reviews and compares contract clauses | S36 | Dify + Documenso | Build |
| A064 | Deal Desk Agent | Routes discounts/risk/approvals | S38 | LangGraph + Odoo | Build |

---

# 11. AGENT DIRECTORY — CUSTOMER / RETENTION

| Agent ID | Agent | What It Does | Funnel | Platform | Status |
|---|---|---|---|---|---|
| A065 | Onboarding Agent | Runs client onboarding checklist | S40 | Odoo + n8n + Dify | Build |
| A066 | Requirement Agent | Extracts and structures requirements | S40–S42 | Dify + Qdrant | Build |
| A067 | Customer Success Agent | Creates success plans | S44 | Odoo + Dify | Build |
| A068 | Account Intelligence Agent | Monitors account health and opportunities | S43 | Odoo + PostgreSQL | Build |
| A069 | Support Triage Agent | Classifies support issues | S46 | Chatwoot + Dify | Build |
| A070 | Customer Health Agent | Detects churn/health signals | S44/S50 | PostgreSQL + Metabase + Dify | Build |
| A071 | Adoption Agent | Identifies adoption gaps | S45 | Odoo + Dify | Build |
| A072 | Upsell Agent | Finds expansion opportunities | S47 | Odoo + Dify | Build |
| A073 | Cross-Sell Agent | Finds adjacent service opportunities | S48 | Odoo + Dify | Build |
| A074 | Renewal Agent | Manages renewal pipeline | S49 | Odoo + n8n + Dify | Build |
| A075 | Churn Prevention Agent | Detects and recommends interventions | S50 | PostgreSQL + Dify | Build |
| A076 | Feedback/NPS Agent | Analyzes customer feedback | S51 | Odoo + Dify | Build |
| A077 | Case Study Agent | Finds clients and drafts case studies | S52 | Dify + Odoo | Build |
| A078 | Referral Agent | Identifies and activates referral opportunities | S53 | Odoo + Dify | Build |
| A079 | Advocacy Agent | Turns customers into advocates/partners | S54 | Odoo + Dify | Build |

---

# 12. PLATFORM / CONTROL AGENTS

| Agent ID | Agent | Purpose | Platform |
|---|---|---|---|
| A080 | Analytics Agent | Business intelligence | Metabase + Dify |
| A081 | Experiment Analyst | Evaluates experiments | PostgreSQL + Metabase |
| A082 | AI Evaluation Agent | Tests agent quality | LangGraph + evaluation tooling |
| A083 | AI Operations Agent | Monitors agents/workflows | n8n + LangGraph |
| A084 | Policy Agent | Checks permissions/risk | LangGraph |
| A085 | Executive Intelligence Agent | Summarizes company performance | Hermes + Dify + Metabase |
| A086 | Attribution Agent | Revenue attribution | PostgreSQL + Metabase |
| A087 | Revenue Intelligence Agent | Connects marketing, sales and delivery | PostgreSQL + Qdrant + Dify |

---

# 13. WORKFLOW DIRECTORY — MASTER WORKFLOWS

These are the workflows that should be built in n8n and/or LangGraph.

| WF ID | Workflow | What It Does | Funnel | Main Tools |
|---|---|---|---|---|
| WF001 | Lead Capture | Receives inbound leads and creates CRM record | M22 | n8n + Odoo |
| WF002 | Lead Deduplication | Detects duplicate leads/accounts | S09/S13 | n8n + PostgreSQL |
| WF003 | Lead Enrichment | Adds company/contact intelligence | S08 | n8n + Firecrawl + AI |
| WF004 | Lead Verification | Validates lead/contact data | S10 | n8n + verification tools |
| WF005 | Lead Scoring | Scores lead quality | S11 | Dify + PostgreSQL |
| WF006 | Lead Segmentation | Assigns lead segment | S12 | n8n + AI |
| WF007 | ICP Research | Creates ICP intelligence | S02 | Dify + Firecrawl |
| WF008 | Account Research | Generates account brief | S01–S04 | Firecrawl + Dify |
| WF009 | Buying Signal Detection | Finds public business signals | S05/S15 | Firecrawl + Browser Use |
| WF010 | List Builder | Builds target campaign lists | S14 | n8n + PostgreSQL |
| WF011 | Email Outreach | Sends approved outbound email | S16 | Mautic + Postal + n8n |
| WF012 | LinkedIn Outreach | Supports LinkedIn research/outreach | S17 | Browser Use + AI |
| WF013 | Cold Call Prep | Prepares call briefs | S18 | Odoo + Dify |
| WF014 | WhatsApp Outreach | Routes compliant business messages | S19 | n8n + approved API |
| WF015 | SMS Outreach | Sends approved SMS campaigns | S20 | n8n + provider |
| WF016 | Multi-Channel Sequence | Coordinates multiple touchpoints | S21 | n8n + Odoo |
| WF017 | Personalization | Creates personalized outreach | S22 | Dify + Qdrant |
| WF018 | Deliverability Monitoring | Tracks sending health | S23 | Postal + PostgreSQL |
| WF019 | Follow-Up Engine | Executes follow-up timing | S24 | n8n + Odoo |
| WF020 | Reply Triage | Classifies incoming replies | S25 | Dify + n8n |
| WF021 | Objection Response | Suggests objection responses | S26 | Dify + Qdrant |
| WF022 | Qualification | Scores qualification | S27 | Dify + Odoo |
| WF023 | Meeting Booking | Creates meeting and CRM activity | S28 | Cal.com + Odoo |
| WF024 | Meeting Prep | Generates meeting brief | S29 | Dify + Odoo |
| WF025 | Meeting Summary | Converts notes/transcript to CRM data | S29 | AI + Odoo |
| WF026 | Needs Analysis | Structures client needs | S30 | Dify |
| WF027 | Solution Mapping | Maps needs to service | S31 | Dify + Odoo |
| WF028 | Demo Prep | Creates demo package | S32 | Dify |
| WF029 | Proposal Generator | Creates proposal | S33 | Dify + Odoo + MinIO |
| WF030 | Pricing Approval | Routes pricing decisions | S34 | n8n + Odoo |
| WF031 | Negotiation Copilot | Provides deal guidance | S35 | LangGraph + AI |
| WF032 | Contract Review | Reviews contract changes | S36 | Dify + Documenso |
| WF033 | Deal Approval | Routes deal for approval | S38 | n8n + Odoo |
| WF034 | Invoice Creation | Creates invoice after deal event | S39 | Odoo |
| WF035 | Payment Confirmation | Detects payment and starts onboarding | S39/S40 | Odoo + n8n |
| WF036 | Client Onboarding | Creates onboarding tasks | S40 | Odoo + n8n |
| WF037 | Kickoff | Creates kickoff agenda and records | S41 | Dify + Odoo |
| WF038 | Delivery Setup | Creates project/tasks | S42 | Odoo |
| WF039 | Customer Health | Calculates health score | S44/S50 | PostgreSQL + AI |
| WF040 | Support Triage | Routes support requests | S46 | Chatwoot + AI |
| WF041 | Upsell Detection | Identifies expansion opportunity | S47 | Odoo + AI |
| WF042 | Cross-Sell Detection | Identifies adjacent services | S48 | Odoo + AI |
| WF043 | Renewal | Starts renewal process | S49 | Odoo + n8n |
| WF044 | Churn Prevention | Creates intervention task | S50 | AI + Odoo |
| WF045 | NPS Analysis | Analyzes customer feedback | S51 | AI + Odoo |
| WF046 | Case Study | Creates case-study workflow | S52 | Dify + Odoo |
| WF047 | Referral | Requests and tracks referrals | S53 | Odoo + n8n |
| WF048 | Advocacy | Activates advocates | S54 | Odoo + AI |

---

# 14. MARKETING WORKFLOW DIRECTORY

| WF ID | Workflow | Purpose | Marketing Module | Tools |
|---|---|---|---|---|
| MW001 | Brand Knowledge Sync | Updates brand knowledge base | M01 | Qdrant + Dify |
| MW002 | Channel Strategy | Scores channels | M02 | AI + Metabase |
| MW003 | Content Pillar Generator | Creates content pillars | M03 | Dify |
| MW004 | Keyword Research | Finds/organizes keywords | M04 | Firecrawl + AI |
| MW005 | Keyword Mapping | Maps keywords to pages | M04 | PostgreSQL + AI |
| MW006 | On-Page Audit | Audits pages | M05 | Firecrawl + AI |
| MW007 | Technical SEO Audit | Finds technical SEO problems | M06 | Firecrawl |
| MW008 | Backlink Opportunity Research | Finds authority opportunities | M07 | Firecrawl + AI |
| MW009 | Editorial Calendar | Creates content calendar | M08 | Dify + n8n |
| MW010 | Long-Form Content | Produces articles/guides | M09 | Dify + Qdrant |
| MW011 | Content Review | Reviews content | M09 | Dify |
| MW012 | Content Repurposing | Converts source content into channel assets | M10 | Dify + n8n |
| MW013 | LinkedIn Content | Creates LinkedIn queue | M11 | Dify + n8n |
| MW014 | Instagram Content | Creates Instagram queue | M12 | Dify + n8n |
| MW015 | YouTube Pipeline | Research → script → metadata | M13 | Dify + n8n |
| MW016 | X Content | Creates X content | M14 | Dify + n8n |
| MW017 | Facebook Content | Creates Facebook content | M15 | Dify + n8n |
| MW018 | Secondary Social | Handles WhatsApp/Pinterest/Threads | M16 | Dify + n8n |
| MW019 | Newsletter | Creates newsletter | M17 | Mautic + Dify |
| MW020 | Nurture Sequence | Nurtures leads | M17 | Mautic + n8n |
| MW021 | Growth Experiment | Runs growth experiment lifecycle | M18 | PostgreSQL + AI |
| MW022 | Community Engagement | Plans community activity | M19 | AI + Chatwoot/Rocket.Chat |
| MW023 | Partnership Pipeline | Manages co-marketing/partnerships | M20 | Odoo + AI |
| MW024 | PR Opportunity | Finds PR opportunities | M20 | Firecrawl + AI |
| MW025 | Marketing Analytics | Updates marketing dashboards | M21 | PostgreSQL + Metabase |
| MW026 | Inbound CRM Bridge | Connects all inbound sources to CRM | M22 | n8n + Odoo |

---

# 15. CROSS-FUNCTION WORKFLOWS

| WF ID | Workflow | Purpose |
|---|---|---|
| XW001 | Content → Lead | Connect content engagement to CRM |
| XW002 | Lead → Sales | Route qualified marketing leads |
| XW003 | Sales → Marketing Feedback | Feed objections/win-loss data back to marketing |
| XW004 | Lost Deal → Content | Turn objections into content opportunities |
| XW005 | Client → Upsell | Detect expansion opportunities |
| XW006 | Client → Referral | Activate referral engine |
| XW007 | Client → Case Study | Identify case-study candidates |
| XW008 | Client → Advocacy | Build advocates |
| XW009 | Partner → Lead | Route partner referrals |
| XW010 | Campaign → Revenue | Connect campaigns to closed revenue |
| XW011 | Revenue → Channel ROI | Calculate channel profitability |
| XW012 | CEO → Bottleneck | Detect biggest company funnel bottleneck |
| XW013 | AI Agent Evaluation | Evaluate agent performance |
| XW014 | AI Failure Escalation | Route low-confidence tasks to human |
| XW015 | Knowledge Base Sync | Keep agents updated with company knowledge |

---

# 16. DOWNLOAD / BUILD DIRECTORY

## Ready-to-install software

Use these repositories as the starting point:

- Odoo: https://github.com/odoo/odoo
- n8n: https://github.com/n8n-io/n8n
- LangGraph: https://github.com/langchain-ai/langgraph
- CrewAI: https://github.com/crewAIInc/crewAI
- Dify: https://github.com/langgenius/dify
- Ollama: https://github.com/ollama/ollama
- vLLM: https://github.com/vllm-project/vllm
- LiteLLM: https://github.com/BerriAI/litellm
- Qdrant: https://github.com/qdrant/qdrant
- Mautic: https://github.com/mautic/mautic
- Postal: https://github.com/postalserver/postal
- Chatwoot: https://github.com/chatwoot/chatwoot
- Firecrawl: https://github.com/mendableai/firecrawl
- Browser Use: https://github.com/browser-use/browser-use
- OpenHands: https://github.com/All-Hands-AI/OpenHands
- Metabase: https://github.com/metabase/metabase
- Documenso: https://github.com/documenso/documenso
- Nextcloud: https://github.com/nextcloud/server
- Rocket.Chat: https://github.com/RocketChat/Rocket.Chat
- Vaultwarden: https://github.com/dani-garcia/vaultwarden
- Open WebUI: https://github.com/open-webui/open-webui

---

# 17. WHAT "DOWNLOAD AGENT" MEANS IN THIS ARCHITECTURE

The majority of A001–A087 are not independent downloadable applications.

Instead:

```text
AGENT ROLE
   ↓
PROMPT
   +
TOOLS
   +
MEMORY
   +
POLICIES
   +
WORKFLOW
   +
MODEL
   ↓
DEPLOYED AGENT
```

For example:

**Lead Scoring Agent**

is built as:

```text
Dify/LangGraph
+
Lead Scoring Prompt
+
Odoo CRM Tool
+
PostgreSQL
+
Qdrant
+
ICP Knowledge
+
Scoring Rules
+
Human Escalation
```

So the implementation file should eventually contain:

```text
/agents/lead-scoring/
    agent.yaml
    prompt.md
    tools.yaml
    workflow.json
    evaluation.json
    README.md
```

---

# 18. RECOMMENDED GITHUB REPOSITORY STRUCTURE

Create one central repository:

```text
billion-dreams-ai-company-os/
│
├── agents/
│   ├── strategy/
│   ├── marketing/
│   ├── seo/
│   ├── content/
│   ├── social/
│   ├── lead-intelligence/
│   ├── outreach/
│   ├── sales/
│   ├── customer-success/
│   └── executive/
│
├── workflows/
│   ├── n8n/
│   ├── langgraph/
│   └── dify/
│
├── skills/
│   ├── marketing/
│   ├── sales/
│   ├── research/
│   ├── crm/
│   └── operations/
│
├── prompts/
│
├── knowledge/
│
├── schemas/
│
├── evaluations/
│
├── deployment/
│   ├── docker/
│   ├── compose/
│   └── infrastructure/
│
└── docs/
```

---

# 19. AGENT FILE STANDARD

Every agent should eventually have:

```yaml
agent_id:
name:
department:
funnel_stages:
marketing_modules:
purpose:
inputs:
outputs:
model:
framework:
tools:
memory:
permissions:
approval_required:
workflow_ids:
kpis:
failure_conditions:
escalation:
version:
```

---

# 20. WORKFLOW FILE STANDARD

Every workflow should eventually have:

```yaml
workflow_id:
name:
trigger:
inputs:
systems:
agents:
steps:
conditions:
human_approval:
outputs:
events_emitted:
failure_handling:
retry_policy:
logging:
kpis:
version:
```

---

# 21. BUILD STATUS LEGEND

| Status | Meaning |
|---|---|
| READY SOFTWARE | Install/download the software |
| FRAMEWORK | Install framework, then build agent |
| BUILD | Agent role must be configured |
| WORKFLOW BUILD | Workflow must be created |
| ADAPTER REQUIRED | External platform integration required |
| HUMAN REQUIRED | Human approval/interaction is required |

---

# 22. CRITICAL IMPLEMENTATION RULE

Do NOT download 87 random AI agents and connect them.

Instead:

```text
INSTALL CORE PLATFORMS
        ↓
CONFIGURE COMPANY KNOWLEDGE
        ↓
BUILD STANDARD AGENT SKILLS
        ↓
BUILD AGENTS
        ↓
BUILD n8n WORKFLOWS
        ↓
CONNECT ODOO
        ↓
CONNECT MARKETING CHANNELS
        ↓
CONNECT SALES CHANNELS
        ↓
TEST
        ↓
EVALUATE
        ↓
DEPLOY
```

This prevents duplicate agents, conflicting memory, uncontrolled permissions and unnecessary infrastructure.

---

# 23. FIRST INSTALLATION BUNDLE

The first installation bundle should be:

```text
01 Odoo Community
02 PostgreSQL
03 n8n
04 Dify
05 LangGraph
06 Ollama
07 LiteLLM
08 Qdrant
09 MinIO
10 Mautic
11 Postal
12 Cal.com / Cal.diy
13 Chatwoot
14 Firecrawl
15 Browser Use
16 Metabase
17 Documenso
18 Nextcloud
19 Vaultwarden
20 Docker
```

Then build the Tier-1 revenue agents:

```text
A001 Market Research
A002 ICP
A034 Lead Discovery
A035 Contact Discovery
A036 Enrichment
A038 Verification
A039 Lead Scoring
A043 Outreach Strategy
A044 Email Outreach
A049 Personalization
A050 Follow-Up
A052 Reply Triage
A054 Qualification
A055 Meeting Prep
A060 Proposal
A065 Onboarding
```

---

# 24. NEXT IMPLEMENTATION ARTIFACTS

After this directory, the implementation should create:

1. `AGENT_REGISTRY.yaml`
2. `SKILL_REGISTRY.yaml`
3. `TOOL_REGISTRY.yaml`
4. `WORKFLOW_REGISTRY.yaml`
5. `N8N_WORKFLOW_INDEX.md`
6. `DIFY_AGENT_INDEX.md`
7. `LANGGRAPH_AGENT_INDEX.md`
8. `ODOO_MODEL_MAP.md`
9. `EVENT_SCHEMA.yaml`
10. `AI_PERMISSION_MATRIX.yaml`
11. `AGENT_EVALUATION_MATRIX.yaml`
12. `DEPLOYMENT_DOCKER_COMPOSE.md`

These files turn this catalog into an actual build system.

---

# 25. FINAL RULE

The directory is the **map**.

The actual implementation repository should contain the **agents, skills, prompts, workflow JSON, schemas, tests and deployment files**.

Therefore:

```text
THIS FILE
   ↓
WHAT TO INSTALL
   ↓
WHAT TO BUILD
   ↓
WHERE IT IS USED
   ↓
WHICH FUNNEL STAGE
   ↓
WHICH WORKFLOW
   ↓
WHICH AGENT
   ↓
WHICH SOFTWARE
   ↓
IMPLEMENTATION REPOSITORY
```

The long-term objective is that a developer or AI workflow builder can open this directory, select a funnel stage, click the relevant software/repository, open the corresponding agent/workflow specification, and build the component without having to reinterpret the entire Company OS.
