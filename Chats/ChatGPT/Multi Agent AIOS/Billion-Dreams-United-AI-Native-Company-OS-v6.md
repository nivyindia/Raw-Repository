# BILLION DREAMS UNITED
# AI-NATIVE COMPANY OPERATING SYSTEM
## Master Blueprint v6 — Revenue-First, Open-Source-First, Modular, Agentic

**Date:** 2026-09-01  
**Parent Company:** Billion Dreams United  
**Primary Operating Principle:** Build a profitable company first, then progressively automate it.  
**Architecture Principle:** Do not maximize the number of AI agents. Maximize business outcomes per unit of automation.

---

# 1. Executive Thesis

This is a complete redesign of the previous blueprint.

The objective is NOT:

> “Create a company with hundreds of AI agents.”

The objective is:

> **Create a company where humans define strategy and accountability, software handles deterministic operations, AI handles reasoning and knowledge work, and every department is connected through one business data backbone.**

The OS therefore has five fundamental layers:

```text
                    FOUNDER
                       │
                EXECUTIVE AI
                       │
             AGENT CONTROL PLANE
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      REVENUE        DELIVERY      OPERATIONS
       AGENTS         AGENTS         AGENTS
        │              │              │
        └──────────────┼──────────────┘
                       │
              AUTOMATION / EVENTS
                       │
             BUSINESS SYSTEM OF RECORD
                       │
              COMPANY DATA / MEMORY
```

The architecture is **revenue-first**:

```text
Revenue
  ↓
Delivery
  ↓
Retention
  ↓
Operations
  ↓
Intelligence
  ↓
Autonomy
```

---

# 2. Design Rules

## Rule 1 — Revenue before autonomy

If an automation does not help acquire, convert, deliver, retain or expand customers, it is lower priority while cash flow is limited.

## Rule 2 — Open-source first

Prefer self-hosted/open-source software.

Cloud/proprietary AI may be used when:
- quality is materially better,
- a task is high value,
- local models are not yet sufficient,
- or temporary speed is more valuable than infrastructure cost.

## Rule 3 — One primary system per function

Avoid maintaining five tools for the same job.

## Rule 4 — Agents are not workflows

Use an agent for:
- reasoning
- research
- judgment
- synthesis
- ambiguity
- planning

Use automation for:
- scheduling
- routing
- CRUD
- retries
- webhooks
- deterministic calculations
- notifications
- API movement

## Rule 5 — Human approval for consequential actions

Payments, contracts, legal commitments, destructive actions, production deployments and sensitive external communication must have policy controls.

## Rule 6 — Everything observable

Every important AI action should have:
- run ID
- agent ID
- inputs
- tools
- model
- output
- cost
- duration
- result
- human override
- business outcome

## Rule 7 — Reusable skills, not giant prompts

Business procedures become reusable skills.

## Rule 8 — Model-independent architecture

No department should be permanently tied to one LLM provider.

---

# 3. Company Structure

```text
BILLION DREAMS UNITED
│
├── Nivy Next
│   ├── Digital Marketing
│   ├── SEO
│   ├── PPC
│   ├── Social Media
│   ├── Web Development
│   ├── AI Automation
│   ├── SaaS / IT
│   └── Lead Generation
│
├── Nivy Advisory
│   ├── Tax
│   ├── Accounting
│   ├── Compliance
│   └── Business Advisory
│
├── Nivy Academy
│   ├── Courses
│   ├── Training
│   ├── Community
│   └── Certification
│
├── Nivy Jobs
│   ├── Recruitment
│   ├── Employer Services
│   └── Job Seeker Services
│
└── Nivy Studio
    ├── UGC
    ├── Creators
    ├── Influencer Services
    └── Production
```

Shared company functions:

- Strategy
- Sales
- Marketing
- Delivery
- Customer Success
- Finance
- HR
- Legal/Compliance
- Product/R&D
- IT/DevOps
- Data/Analytics
- AI Operations

---

# 4. The Operating Model

## Humans

Humans own:
- strategy
- final accountability
- high-value sales
- relationship building
- legal decisions
- financial authority
- exceptional cases

## AI

AI owns:
- research
- analysis
- personalization
- drafting
- classification
- planning
- recommendations
- knowledge retrieval
- repetitive knowledge work

## Automation

Automation owns:
- execution
- routing
- synchronization
- scheduling
- notifications
- record creation
- state transitions

---

# 5. Final Architecture

```text
                           ┌──────────────┐
                           │    FOUNDER   │
                           │     YOU      │
                           └──────┬───────┘
                                  │
                           ┌──────▼───────┐
                           │    HERMES    │
                           │ Executive AI │
                           └──────┬───────┘
                                  │
                      ┌───────────▼───────────┐
                      │   AGENT CONTROL PLANE │
                      │       LangGraph       │
                      └───────────┬───────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
     REVENUE                   DELIVERY                 OPERATIONS
      AGENTS                    AGENTS                    AGENTS
        │                         │                         │
   Dify / CrewAI              OpenHands                Dify / AI
   Browser / Research         GitHub / QA              Finance / HR
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                           ┌──────▼───────┐
                           │     n8n      │
                           │ Automation + │
                           │ Event Layer  │
                           └──────┬───────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                  ODOO         CHATWOOT       GITHUB
               Business OS      Support        Code
                    │
                    ▼
          ┌───────────────────────┐
          │   COMPANY DATA LAYER  │
          │ PostgreSQL            │
          │ Qdrant                │
          │ MinIO                 │
          └───────────┬───────────┘
                      │
          ┌───────────▼───────────┐
          │ OBSERVABILITY /       │
          │ EVALUATION / POLICY   │
          └───────────────────────┘
```

---

# 6. Primary Software Stack

| Layer | Primary Tool | Purpose | Status |
|---|---|---|---|
| Executive Agent | Hermes | Founder interface / Chief of Staff | Add |
| Orchestration | LangGraph | Stateful multi-agent control | Primary |
| AI Apps | Dify | RAG, visual AI apps, knowledge workflows | Primary |
| Agent Teams | CrewAI | Specialized multi-role crews | Selective |
| Coding Agents | OpenHands | Software development execution | Primary |
| Automation | n8n | Deterministic automation + events | Primary |
| Business OS | Odoo Community | CRM, sales, projects, operations | Primary |
| Structured DB | PostgreSQL | Source of truth | Primary |
| Vector DB | Qdrant | Semantic memory | Primary |
| Object Storage | MinIO | Files/artifacts | Primary |
| Model Runtime | Ollama | Easy local inference | Primary |
| GPU Runtime | vLLM | High-throughput inference | When GPU exists |
| Model Gateway | LiteLLM | Model routing/abstraction | Primary |
| Web Research | Firecrawl | Web extraction | Primary |
| Browser Agent | Browser Use | Browser interaction | Selective |
| Email Marketing | Mautic | Nurture/marketing automation | Primary |
| Mail Infrastructure | Postal | Self-hosted email | Primary |
| Booking | Cal.com | Meetings | Primary |
| E-sign | Documenso | Contracts/signatures | Primary |
| Customer Support | Chatwoot | Omnichannel support | Primary |
| Analytics | Metabase | BI | Primary |
| Files | Nextcloud | Company file layer | Primary |
| Communication | Rocket.Chat | Internal communication | Primary |
| Code | GitHub | Repositories/PRs | Primary |
| Project Management | Odoo Project | Projects/tasks/milestones | Primary |
| Passwords | Bitwarden | Credentials | Primary |

### Important

OpenProject is **not part of the primary stack**.

Odoo Project is sufficient as the default project system because Odoo integrates CRM, sales and project operations in one business suite; Odoo Project supports tasks, milestones, dependencies and profitability tracking. If future project complexity genuinely exceeds Odoo, OpenProject can be added as a specialized layer later. citeturn0search2turn0search1

---

# 7. Executive Layer — Hermes

Hermes is not the company's database and not the universal orchestrator.

It is:

> **Founder-facing Executive AI / Chief of Staff**

Responsibilities:
- daily briefing
- company questions
- task delegation
- research requests
- agent coordination
- scheduled reports
- personal/company memory
- browser/terminal work
- communication interface
- reusable skills

Example:

```text
YOU:
"Why did sales drop this week?"

HERMES:
→ Query Odoo
→ Query PostgreSQL
→ Query Metabase
→ Ask Sales Analysis Agent
→ Compare previous periods
→ Return diagnosis
→ Recommend actions
```

Hermes should delegate complex workflows instead of becoming a giant monolithic agent.

---

# 8. Control Plane — LangGraph

LangGraph is the primary programmable control layer for complex, stateful, long-running agent workflows and supports human-in-the-loop patterns. citeturn0search5turn0search14

Use it for:
- multi-step reasoning
- agent delegation
- state management
- approvals
- retries
- checkpoints
- long-running workflows
- exception handling

Do NOT use LangGraph for every simple automation.

---

# 9. AI Application Layer — Dify

Dify is the visual AI application layer.

Build reusable applications for:
- research
- knowledge assistant
- sales proposal generation
- website audit
- customer support
- internal knowledge
- report generation
- department-specific copilots

Dify applications can then be invoked from n8n/LangGraph/Hermes.

---

# 10. Agent-Team Layer — CrewAI

CrewAI is used selectively.

Good use cases:

```text
Research Crew
├── Researcher
├── Competitor Analyst
├── Market Analyst
└── Synthesizer
```

```text
Delivery Crew
├── Business Analyst
├── Architect
├── Developer
├── Reviewer
└── QA
```

Do not create a CrewAI crew when a single deterministic workflow is enough.

---

# 11. Development Workforce — OpenHands

OpenHands is the coding execution layer.

Flow:

```text
Requirement
 ↓
Architect Agent
 ↓
OpenHands
 ↓
Code
 ↓
Tests
 ↓
GitHub PR
 ↓
Review Agent
 ↓
Human approval
 ↓
Deploy
```

OpenHands is designed as an open-source AI coding-agent platform. Its current documentation should be checked for deployment/isolation requirements before using it as a multi-user production service. citeturn0search17turn0search8

---

# 12. Company Brain

```text
                         COMPANY BRAIN
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   PostgreSQL               Qdrant                 MinIO
 Structured Truth       Semantic Knowledge      Files/Artifacts
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                         Event Store
                              │
                              ▼
                     AI Retrieval Layer
```

## PostgreSQL

Authoritative:
- clients
- leads
- opportunities
- invoices
- payments
- projects
- tasks
- employees
- campaigns
- agent runs
- KPIs

## Qdrant

Semantic:
- SOPs
- research
- proposals
- call notes
- product knowledge
- company knowledge

## MinIO

Artifacts:
- PDFs
- contracts
- proposals
- reports
- datasets
- generated deliverables

---

# 13. Single Source of Truth

## Odoo owns business records

Odoo:
- CRM
- contacts
- sales
- quotations
- projects
- tasks
- invoices
- employees/operations where appropriate

Odoo officially positions Community as an open-source business suite and includes CRM, project management and other business applications. citeturn0search2

## PostgreSQL owns AI/operational data

PostgreSQL:
- agent registry
- workflow events
- model usage
- lead enrichment cache
- AI evaluations
- experiment data
- event log
- analytics warehouse structures

Do not duplicate authoritative client/invoice records in five databases.

---

# 14. Revenue Engine — Highest Priority

This is the first system to implement.

## Revenue equation

```text
Qualified Traffic
      ×
Lead Conversion
      ×
Meeting Rate
      ×
Close Rate
      ×
Average Deal Value
      ×
Retention
=
Revenue
```

The AI OS should optimize these variables.

---

# 15. SALES + REVENUE AGENTS — PRIORITY TABLE

| P | Agent | KPI | Main Tools | Automation |
|---:|---|---|---|---|
| 1 | ICP Strategist | ICP clarity / conversion | Dify + Research | Agent |
| 2 | Market/Niche Researcher | profitable niches found | Firecrawl + Browser + Dify | Agent |
| 3 | Lead Discovery Agent | qualified prospects/day | Firecrawl + Browser + n8n | Mix |
| 4 | Lead Enrichment Agent | data completeness | n8n + PostgreSQL | Mix |
| 5 | Lead Scoring Agent | qualified-lead precision | AI + Odoo | Mix |
| 6 | Account Research Agent | research quality/time | Browser + Firecrawl | Agent |
| 7 | Personalization Agent | reply rate | Dify + n8n | Mix |
| 8 | Outreach Agent | qualified replies | Mautic/email + n8n | Mix |
| 9 | Follow-up Agent | follow-up conversion | n8n + Mautic | Automation + AI |
| 10 | Meeting Booking Agent | meetings booked | Cal.com + n8n | Automation |
| 11 | Meeting Prep Agent | close rate | Odoo + Dify | Agent |
| 12 | Sales Copilot | win rate | Hermes + Dify | Human-in-loop |
| 13 | Proposal Agent | proposal turnaround | Dify + Odoo | Mix |
| 14 | Negotiation Copilot | margin / close rate | Hermes + Dify | Human-in-loop |
| 15 | Contract Agent | signed contracts | Documenso + n8n | Mix |
| 16 | Invoice Agent | payment cycle | Odoo + n8n | Automation |
| 17 | Onboarding Agent | time-to-start | Odoo + n8n | Mix |
| 18 | Free Audit Agent | audit→meeting conversion | Firecrawl + AI | Mix |
| 19 | Referral Agent | referred opportunities | Odoo + n8n | Automation |
| 20 | Renewal Agent | renewal rate | Odoo + AI | Mix |
| 21 | Upsell Agent | expansion revenue | Odoo + AI | Mix |
| 22 | Churn Risk Agent | retained revenue | Odoo + Metabase | Agent |
| 23 | Customer Success Agent | client health | Odoo + Chatwoot | Mix |

---

# 16. Revenue Agent Operating Sequence

```text
1. ICP
   ↓
2. Market Research
   ↓
3. Lead Discovery
   ↓
4. Enrichment
   ↓
5. Qualification
   ↓
6. Account Research
   ↓
7. Personalization
   ↓
8. Outreach
   ↓
9. Follow-up
   ↓
10. Meeting
   ↓
11. Sales Call
   ↓
12. Proposal
   ↓
13. Negotiation
   ↓
14. Contract
   ↓
15. Payment
   ↓
16. Onboarding
   ↓
17. Delivery
   ↓
18. Renewal
   ↓
19. Upsell
   ↓
20. Referral
```

---

# 17. First 14-Day Revenue Sprint

## Days 1–2
- Odoo CRM configuration
- PostgreSQL verification
- credentials
- n8n health check
- email infrastructure
- calendar
- website forms

## Days 3–4
- ICP
- niche selection
- offer definition
- lead criteria

## Days 5–6
- lead discovery
- enrichment
- qualification

## Days 7–8
- personalized outreach
- follow-up sequences
- CRM state machine

## Days 9–10
- meeting booking
- meeting preparation
- sales dashboard

## Days 11–12
- proposal
- contract
- invoice

## Days 13–14
- real campaign
- measure replies
- fix weak steps
- human sales calls

**No AI COO work during this sprint unless it directly supports the revenue engine.**

---

# 18. Productized Offers

Prioritize offers that are:
- easy to demonstrate
- fast to deliver
- high perceived value
- repeatable
- automatable

Priority:

1. AI Automation Audit
2. Lead Generation System
3. AI Sales Automation
4. Website/SEO Conversion Audit
5. Marketing Automation
6. Website Development
7. SEO/Growth Retainer
8. AI-native Company Automation
9. Custom AI/software implementation

The agent system should sell outcomes, not “AI agents”.

---

# 19. Marketing Engine

```text
Market Research
 ↓
ICP
 ↓
Positioning
 ↓
Offer
 ↓
Content / Distribution
 ↓
Landing Page
 ↓
Lead Capture
 ↓
Qualification
 ↓
Nurture
 ↓
Sales
```

AI:
- research
- content planning
- personalization
- SEO analysis
- competitor analysis
- campaign analysis

n8n:
- publishing
- lead capture
- CRM updates
- notifications
- scheduling
- data movement

---

# 20. Growth Engine

Retain the previous growth concepts:

### Engine A — Free Audit
Immediate business value → meeting.

### Engine B — Referral
Existing customer/partner → new opportunity.

### Engine C — Signal Outreach
Hiring/funding/website-change/business signals → targeted outreach.

### Engine D — Community
Communities → trust → leads.

### Engine E — UGC/Advocacy
Customer/creator participation → distribution.

### Engine F — Rewards/Contests
Campaign-specific acquisition.

AI improves:
- targeting
- personalization
- segmentation
- anomaly detection
- campaign optimization

n8n handles:
- execution
- tracking
- state
- notifications

---

# 21. Delivery Operating System

```text
SALE CLOSED
 ↓
Odoo Project Created
 ↓
Requirement Agent
 ↓
Scope / Acceptance Criteria
 ↓
Project Plan
 ↓
Resource Assignment
 ↓
Execution
 ↓
QA
 ↓
Client Review
 ↓
Delivery
 ↓
Feedback
 ↓
Case Study
 ↓
Renewal / Upsell
```

Odoo Project supports task management, milestones, dependencies, recurring tasks and project profitability, making it a suitable primary delivery system for this architecture. citeturn0search1turn0search10

---

# 22. Delivery Agents

| Priority | Agent | Function |
|---:|---|---|
| 1 | Requirement Analyst | Convert client input into requirements |
| 2 | Solution Architect | Design solution |
| 3 | Project Planner | Break scope into tasks |
| 4 | Developer Agent | Implement |
| 5 | Code Review Agent | Review |
| 6 | QA Agent | Test |
| 7 | Browser QA Agent | UI/browser testing |
| 8 | Documentation Agent | Documentation |
| 9 | Deployment Agent | Controlled deployment |
| 10 | Client Reporting Agent | Progress/status reporting |

---

# 23. Customer Success

```text
Client
 ↓
Odoo + Chatwoot
 ↓
Customer Health Agent
 ↓
 ├── Healthy → Upsell/Referral
 ├── Warning → Intervention
 └── Critical → Human
```

Track:
- response time
- satisfaction
- project health
- unresolved issues
- usage
- renewal date
- expansion opportunities

---

# 24. Support

Chatwoot is the customer-facing support layer.

```text
Customer
 ↓
Chatwoot
 ↓
Knowledge Agent
 ↓
Confidence
 ├── High → Answer
 └── Low → Human
 ↓
Odoo record
```

---

# 25. Finance

Odoo is the financial/business system of record.

AI may:
- explain reports
- classify/analyze
- forecast
- detect anomalies
- prepare summaries
- identify collections priorities

AI may NOT autonomously:
- transfer money
- approve refunds
- make legal financial commitments

---

# 26. HR

AI:
- job descriptions
- sourcing assistance
- candidate summaries
- interview scheduling
- onboarding
- training
- performance summaries

Human:
- hiring decision
- termination
- compensation decision
- sensitive employee decisions

---

# 27. Legal & Compliance

AI:
- document extraction
- clause comparison
- checklist generation
- compliance calendar
- draft preparation

Human:
- final legal interpretation
- contract approval
- statutory responsibility

---

# 28. Product / R&D

```text
Market Signal
 ↓
Research Agent
 ↓
Opportunity Score
 ↓
Product Manager Agent
 ↓
PRD
 ↓
Architecture
 ↓
OpenHands
 ↓
QA
 ↓
Pilot
 ↓
Feedback
 ↓
Iteration
```

---

# 29. Agent Registry

Every production agent is registered:

```text
agent_id
name
department
role
version
model_policy
prompt_version
skills
tools
memory_scope
permissions
approval_level
budget
timeout
kpi
status
owner
```

Agent lifecycle:

```text
Idea
 ↓
Prototype
 ↓
Evaluation
 ↓
Shadow Mode
 ↓
Limited Production
 ↓
Production
 ↓
Monitoring
 ↓
Retirement
```

---

# 30. Skill Registry

Skills are reusable business procedures.

```text
/company-ai/skills/

sales/
 marketing/
 research/
 finance/
 delivery/
 support/
 hr/
 legal/
 engineering/
```

Each skill:

```text
SKILL.md
INPUTS
TOOLS
PROCESS
OUTPUT
VALIDATION
FAILURE HANDLING
EXAMPLES
```

A skill should be portable across agents.

---

# 31. Tool Registry

Agents should not have arbitrary access to every API.

```text
tool_id
tool_name
description
input_schema
output_schema
permission
risk_level
rate_limit
audit_required
```

Examples:
- `odoo.search_lead`
- `odoo.create_opportunity`
- `github.create_branch`
- `github.open_pr`
- `firecrawl.extract`
- `chatwoot.create_ticket`
- `cal.create_booking`
- `postgres.query_readonly`

---

# 32. Policy Engine

```text
Agent
 ↓
Requested Action
 ↓
Policy Engine
 ├── ALLOW
 ├── REQUIRE APPROVAL
 └── DENY
```

Risk levels:

### L0 — Safe
Read data, summarize, classify.

### L1 — Low
Create internal records, draft messages.

### L2 — Medium
Send external communication, change CRM state.

### L3 — High
Contracts, production deployment, financial operations.

### L4 — Critical
Payments, destructive operations, legal commitments.

L3/L4 require explicit policy/approval controls.

---

# 33. Event Architecture

Standard event names:

```text
lead.created
lead.enriched
lead.qualified
outreach.created
outreach.sent
reply.received
meeting.booked
meeting.completed
proposal.created
proposal.sent
proposal.accepted
contract.sent
contract.signed
invoice.created
payment.received
payment.failed
client.onboarded
project.created
project.blocked
project.completed
ticket.created
ticket.resolved
renewal.due
renewal.completed
```

Every event has:

```text
event_id
event_type
timestamp
producer
entity_id
payload
correlation_id
version
```

---

# 34. n8n Architecture

n8n is the event/automation backbone.

Use n8n for:

- webhooks
- scheduling
- API integration
- CRM synchronization
- retries
- notifications
- waits
- deterministic branching
- campaign execution
- event consumers

Do not turn n8n into a giant reasoning engine.

---

# 35. AI + n8n Pattern

Preferred:

```text
n8n
 ↓
collect data
 ↓
AI Agent
 ↓
reason/classify
 ↓
structured JSON
 ↓
n8n
 ↓
validate
 ↓
execute
 ↓
store
```

This gives:
- reliability
- observability
- deterministic execution
- AI flexibility

---

# 36. Model Router

```text
                     LiteLLM
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
    Ollama             vLLM          External APIs
       │                │                │
    Local LLM        GPU LLM         fallback
```

Policy chooses model based on:
- task complexity
- privacy
- latency
- cost
- quality requirement

---

# 37. Model Strategy

## Local-first

Use local inference for:
- classification
- extraction
- routine research
- internal documents
- lead scoring
- summarization
- high-volume tasks

## Stronger models

Use when needed for:
- complex strategy
- difficult architecture
- high-value sales reasoning
- difficult synthesis
- exceptional cases

No agent should permanently depend on one provider unless technically necessary.

---

# 38. Observability

Track:

### Agent
- success
- failure
- latency
- cost
- tokens
- tool calls

### Business
- leads
- meetings
- proposals
- close rate
- revenue
- margin
- retention

### AI quality
- human override
- hallucination rate
- evaluation score
- task success
- escalation rate

---

# 39. Evaluation System

Every important agent gets a test set.

```text
Historical Cases
 ↓
Agent
 ↓
Expected Output
        VS
Actual Output
 ↓
Score
 ↓
Release / Improve / Disable
```

Key metrics:
- precision
- recall
- accuracy
- task completion
- human acceptance
- business outcome

---

# 40. Company Dashboard

Metabase should provide:

## CEO Dashboard
- revenue
- cash
- pipeline
- forecast
- active clients
- project health
- renewal risk

## Sales Dashboard
- leads
- qualified leads
- replies
- meetings
- proposals
- close rate

## Marketing Dashboard
- traffic
- lead source
- conversion
- campaign ROI

## Delivery Dashboard
- active projects
- overdue tasks
- utilization
- margin
- blockers

## AI Dashboard
- agents running
- success rate
- cost
- failures
- human overrides
- revenue influenced

---

# 41. Security Architecture

Minimum:

```text
Internet
 ↓
Reverse Proxy
 ↓
Auth
 ↓
Services
 ↓
Private Network
 ↓
Database
```

Controls:
- Bitwarden/secrets management
- service accounts
- least privilege
- network segmentation
- HTTPS
- backups
- audit logs
- sandboxing
- credential rotation

---

# 42. Backup Strategy

Back up:

### Daily
- PostgreSQL
- Odoo database
- n8n configuration
- critical service configs

### Regular
- MinIO
- Nextcloud
- Git repositories
- AI skills
- agent registry
- prompts
- evaluation datasets

Maintain at least:
- local backup
- separate backup
- off-site backup

---

# 43. Infrastructure

Start with Docker-based deployment.

Do NOT start with Kubernetes unless scale requires it.

Baseline:

```text
Linux
Docker
Reverse Proxy
PostgreSQL
Redis where required
Qdrant
MinIO
Odoo
n8n
Dify
Hermes
Ollama
LiteLLM
Mautic
Chatwoot
Cal.com
Documenso
Metabase
Nextcloud
Rocket.Chat
```

Deploy incrementally.

---

# 44. Multi-Tenant / Multi-Brand Architecture

The system should support:

```text
Company
 ↓
Brand
 ↓
Department
 ↓
Client
 ↓
Project
 ↓
Agent
```

Every relevant database record should carry:

```text
company_id
brand_id
department_id
client_id
project_id
```

This allows Nivy Next, Nivy Advisory, Nivy Academy etc. to share infrastructure without mixing business data.

---

# 45. Data Governance

Data classes:

### Public
Marketing material.

### Internal
SOPs and operations.

### Confidential
Client/business information.

### Restricted
Financial/legal/security information.

Agent access must follow data classification.

---

# 46. Autonomous Company Levels

Do not attempt full autonomy immediately.

## Level 0
Human only.

## Level 1
AI recommends.

## Level 2
AI drafts; human approves.

## Level 3
AI executes low-risk actions.

## Level 4
AI manages workflows with exception escalation.

## Level 5
AI manages a department within defined policies.

## Level 6
AI COO coordinates departments.

The company should progress department-by-department.

---

# 47. AI COO

Build only after revenue and operations are stable.

AI COO receives:

```text
Sales
Marketing
Delivery
Finance
HR
Support
Projects
```

and produces:

- priorities
- bottlenecks
- exceptions
- resource conflicts
- risk alerts
- weekly operating plan

It does NOT replace the founder.

---

# 48. AI CEO / Founder Intelligence

Build last.

The CEO intelligence layer should answer:

> Where are we making money?

> Where are we losing money?

> Which service should we push?

> Which clients are at risk?

> Which acquisition channel works?

> What should I personally do today?

> What can the company safely automate next?

---

# 49. Department Architecture

Every department follows the same template:

```text
Department
│
├── Goals
├── KPIs
├── Inputs
├── Processes
├── Agents
├── Skills
├── Tools
├── Automations
├── Human approvals
├── Data
├── Events
└── Reports
```

---

# 50. Department Priority

## Tier 1 — Revenue
1. Sales
2. Marketing
3. Customer Success

## Tier 2 — Delivery
4. Development
5. Design
6. SEO/PPC
7. Content
8. Operations

## Tier 3 — Business
9. Finance
10. HR
11. Legal/Compliance
12. Procurement

## Tier 4 — Intelligence
13. Data/BI
14. R&D
15. AI Operations
16. Strategy

---

# 51. Sales Department

Agents:
- ICP Strategist
- Lead Researcher
- Enrichment
- Qualification
- Account Research
- Personalization
- Outreach
- Follow-up
- Meeting Prep
- Sales Copilot
- Proposal
- Negotiation
- Contract
- Payment
- Renewal
- Upsell

Human:
- relationship
- final sales call
- negotiation approval
- major pricing decisions

---

# 52. Marketing Department

Agents:
- Market Research
- Competitor Research
- Content Strategist
- SEO Analyst
- Keyword Research
- Campaign Analyst
- Landing Page Optimizer
- Ad Analyst
- Distribution Agent
- Analytics Agent

Automation:
- scheduling
- publishing
- campaign events
- lead capture

---

# 53. Customer Success

Agents:
- Onboarding
- Health Score
- Support Triage
- Renewal
- Upsell
- Referral
- Case Study

---

# 54. Software Engineering

Agents:
- Requirements
- Architecture
- Coding
- Review
- Testing
- Documentation
- DevOps
- Security Review

Primary execution:
OpenHands + GitHub + CI.

---

# 55. Finance

Agents:
- Financial Analyst
- Collections
- Cash Forecast
- Expense Analyzer
- Management Reporting

System:
Odoo + PostgreSQL + Metabase.

---

# 56. HR

Agents:
- Job Description
- Candidate Research
- Interview Coordinator
- Onboarding
- Training
- HR Analytics

Human decisions remain mandatory for sensitive employment actions.

---

# 57. Legal / Compliance

Agents:
- Document Extractor
- Compliance Calendar
- Clause Analyzer
- Contract Draft Assistant
- Filing Checklist

Human approval required for legal conclusions and commitments.

---

# 58. AI Operations

This is the department that manages AI itself.

Responsibilities:
- Agent Registry
- Skill Registry
- Model Router
- Prompt/version management
- Evaluation
- Observability
- Cost control
- Permissions
- Agent retirement
- AI incident response

---

# 59. Agent Lifecycle

```text
Business Problem
 ↓
Can automation solve it?
 ├── YES → n8n
 └── NO
      ↓
Can one AI skill solve it?
 ├── YES → Single Agent
 └── NO
      ↓
Can a deterministic workflow coordinate agents?
 ├── YES → LangGraph
 └── NO
      ↓
Specialized agent team
```

This prevents unnecessary multi-agent complexity.

---

# 60. Build-vs-Buy-vs-Agent Decision

Before building anything:

```text
1. Existing Odoo feature?
2. Existing n8n node/workflow?
3. Existing open-source software?
4. Existing Dify workflow?
5. Existing agent/skill?
6. Can a simple script solve it?
7. Only then build custom agent.
```

---

# 61. What Must NOT Be Duplicated

Do not maintain:

- Odoo + another CRM as primary
- Odoo Project + OpenProject as primary
- multiple vector DBs
- multiple workflow engines
- multiple support CRMs
- multiple password managers
- multiple email marketing systems

Specialized exceptions are allowed only with documented reason.

---

# 62. Revenue-First Implementation Roadmap

## Phase 1 — CASH FLOW
**Objective: first/next client**

Implement:
1. Odoo CRM
2. Lead Discovery
3. Enrichment
4. Qualification
5. Outreach
6. Follow-up
7. Meeting
8. Proposal
9. Contract
10. Invoice
11. Onboarding

## Phase 2 — SALES AI
Implement:
12. ICP Agent
13. Research Agent
14. Account Research
15. Personalization
16. Meeting Prep
17. Sales Copilot
18. Negotiation Copilot

## Phase 3 — DELIVERY
19. Requirement
20. Architect
21. OpenHands
22. QA
23. Documentation
24. Deployment

## Phase 4 — RETENTION
25. Customer Health
26. Renewal
27. Upsell
28. Referral
29. Support

## Phase 5 — COMPANY AI
30. Hermes
31. Agent Registry
32. Skill Registry
33. Model Router
34. Observability
35. Evaluation
36. Policy Engine

## Phase 6 — AI COO
37. Cross-department intelligence
38. Resource planning
39. Exception management
40. Management reporting

## Phase 7 — AI CEO
41. Strategic intelligence
42. Company-wide planning
43. Capital allocation recommendations
44. Founder command center

---

# 63. First Deployment — Minimal Stack

If budget is extremely limited, do NOT deploy the entire stack.

Start with:

```text
Odoo
+
n8n
+
PostgreSQL
+
Dify
+
Ollama
+
Firecrawl
+
Mautic/Email
+
Cal.com
+
GitHub
```

Then add:

```text
Hermes
Qdrant
MinIO
Chatwoot
OpenHands
Metabase
```

Then add the remaining company services.

---

# 64. First Revenue Machine

The first production system should look like:

```text
                    WEBSITE / OUTBOUND
                            │
                            ▼
                    LEAD DISCOVERY
                            │
                            ▼
                     ENRICHMENT
                            │
                            ▼
                     QUALIFICATION
                            │
                            ▼
                    PERSONALIZATION
                            │
                            ▼
                       OUTREACH
                            │
                     ┌──────┴──────┐
                     ▼             ▼
                   REPLY        NO REPLY
                     │             │
                     ▼             ▼
                  MEETING       FOLLOW-UP
                     │
                     ▼
                SALES CALL
                     │
                     ▼
                  PROPOSAL
                     │
                     ▼
                 CONTRACT
                     │
                     ▼
                  PAYMENT
                     │
                     ▼
                ONBOARDING
                     │
                     ▼
                 DELIVERY
                     │
                     ▼
                RENEWAL/UPSELL
```

---

# 65. CEO Daily Command Center

Hermes should eventually provide:

```text
GOOD MORNING

Revenue:
₹ / $ ...

Pipeline:
...

New qualified leads:
...

Meetings today:
...

Proposals waiting:
...

Payments overdue:
...

Projects at risk:
...

Clients at risk:
...

AI incidents:
...

Top 3 founder actions:
1.
2.
3.
```

---

# 66. Final Strategic Rule

The company must never become:

> “A collection of AI tools.”

It must become:

> **A coordinated operating system in which business data, workflows, agents, software and humans operate on one controlled architecture.**

---

# 67. Final Blueprint in One Page

```text
                         BILLION DREAMS UNITED
                                  │
                              FOUNDER
                                  │
                              HERMES
                                  │
                           AI CONTROL PLANE
                             LANGGRAPH
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
           REVENUE              DELIVERY            OPERATIONS
           AGENTS                AGENTS               AGENTS
             │                    │                    │
       Dify / CrewAI         OpenHands/GitHub      Dify/AI
       Research/Browser       QA/DevOps             Finance/HR
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                                 n8n
                           EVENTS + AUTOMATION
                                  │
                                 ODOO
                CRM + SALES + PROJECTS + BUSINESS
                                  │
                         ┌────────┴────────┐
                         │                 │
                    PostgreSQL           Qdrant
                    STRUCTURED          SEMANTIC
                         │                 │
                         └────────┬────────┘
                                  │
                                MinIO
                               ARTIFACTS
                                  │
                       OBSERVABILITY / POLICY
                                  │
                           AI COO → AI CEO
```

---

# 68. The Core Objective

The final system is successful only when:

```text
YOU
 ↓
define strategy
 ↓
AI researches
 ↓
AI finds opportunities
 ↓
AI qualifies
 ↓
AI prepares outreach
 ↓
Automation executes
 ↓
YOU close high-value deals
 ↓
AI prepares delivery
 ↓
Agents execute
 ↓
Automation reports
 ↓
AI detects problems
 ↓
AI manages retention
 ↓
AI recommends growth
 ↓
YOU make strategic decisions
```

The target is **not 100% autonomous company**.

The target is:

> **Maximum revenue and output per hour of founder involvement.**

That is the real Billion Dreams United AI Company OS.
