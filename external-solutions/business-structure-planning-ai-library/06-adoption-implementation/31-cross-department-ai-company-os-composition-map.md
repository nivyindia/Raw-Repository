# Cross-Department AI Company OS Composition Map

**Date:** 2026-09-16
**Status:** Architecture candidate based on reusable external solutions

## Core composition

```text
Human / Manager
      ↓
Natural-Language Router
      ↓
Department Skill / Agent
      ↓
Workflow / Command Layer
      ↓
Connectors + Systems of Record
      ↓
Validation / Approval / Audit
      ↓
Company OS Knowledge + Logs
```

## Department capability layer

| Department | Reusable capability families | Likely system targets |
|---|---|---|
| Executive | briefing, priorities, meeting prep, decisions | Notion, calendar, Slack/Teams |
| Strategy | research, planning, competitive intelligence | Notion, GitHub, data sources |
| Marketing | campaigns, content, SEO, performance | CRM, analytics, CMS, social tools |
| Sales/RevOps | research, scoring, outreach, pipeline | Odoo/CRM, email, calling/research |
| Customer Success | triage, context, responses, escalations, KB | Helpdesk/CRM, Notion |
| Product | specs, roadmap, research, launch coordination | Notion, Jira/Linear, Figma |
| Engineering/IT | tickets, documentation, runbooks, automation | GitHub, ITSM, knowledge base |
| Finance | reconciliation, close, reporting, variance | Accounting/ERP, spreadsheets, BI |
| Operations | SOPs, capacity, vendors, status, change | Odoo/project/task systems |
| HR | recruiting, screening, onboarding, reviews | ATS/HRIS, calendar, knowledge base |
| Legal/Compliance | contracts, renewals, privacy, AI governance, monitoring | CLM, DMS, research, e-sign |
| Data/Analytics | data intake, analysis, KPI reporting | warehouse, BI, spreadsheets |
| Knowledge | search, synthesis, documentation | Notion + GitHub |
| Automation | routing, triggers, integrations | n8n |

## Cross-functional workflows

### 1. Lead → Client
`Lead research → qualification → outreach → discovery → proposal → contract review → signature → finance setup → onboarding → customer success`

### 2. Content → Revenue
`Market research → campaign plan → content production → publication → lead capture → qualification → CRM → sales → attribution/reporting`

### 3. Customer issue → Learning
`Ticket → customer context → triage → response → escalation if needed → resolution → QA → KB article → SOP/process improvement`

### 4. Product launch
`Research → PRD → roadmap/task breakdown → build → QA → launch readiness → marketing → sales enablement → support readiness → launch → performance review`

### 5. Monthly business review
`Sales KPIs + marketing KPIs + finance KPIs + operations + customer health + product delivery → validation → executive brief → decisions → assigned actions → tracking`

### 6. AI governance
`AI system inventory → use-case classification → risk/control review → approved implementation → monitoring → periodic policy/regulation review → executive/compliance review`

## Shared control plane

Every agent/workflow should expose:
- identity and owner
- trigger
- inputs
- permitted tools/connectors
- data sensitivity
- expected output schema
- validation rules
- human approval requirement
- action/write permissions
- provenance/citations
- audit log
- rollback/recovery path
- version
- test status

## Nivy implementation principle

Do not create one giant autonomous agent. Compose small, testable capabilities behind a router and workflow layer. Keep knowledge, execution and system-of-record responsibilities separate.

Candidate stack from prior planning:
- **AI/runtime:** Claude plus other approved models; Ollama where private/local inference is appropriate
- **Automation:** n8n
- **Knowledge/source control:** Notion + GitHub
- **CRM/ERP:** Odoo Community where suitable
- **Accounting:** Odoo/QuickBooks/Xero according to client/system requirements
- **Communication:** Gmail/Microsoft 365 + approved Slack/Teams/WhatsApp integrations
- **Audit/provenance:** Git + structured execution logs

These are architecture candidates, not irreversible technology commitments.

## Reuse gate

Before custom development ask:
1. Does an existing plugin/skill/agent/workflow already perform the task?
2. Is the implementation inspectable?
3. Is its license/access compatible?
4. Can its connectors and permissions be safely used?
5. Can it pass a synthetic-data functional test?
6. Can it be adapted without losing reliability?
7. Is the remaining gap genuinely Nivy-specific?

Only then build the missing component.
