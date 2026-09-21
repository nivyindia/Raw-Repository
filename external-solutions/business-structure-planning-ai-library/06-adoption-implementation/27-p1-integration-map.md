# P1 Integration Map

Research date: 2026-09-16

## Architecture

```text
User / Manager
      |
      v
Natural-language Router
      |
      +--> Finance skills
      +--> Operations skills
      +--> HR skills
      |
      v
Workflow / Command layer
      |
      +--> Knowledge
      +--> CRM / HRIS / ERP
      +--> Email / Calendar / Chat
      +--> Sheets / BI / Data
      |
      v
Approval + Audit layer
      |
      v
Company OS / system of record
```

## Finance

| Capability | Connector category | Example target |
|---|---|---|
| GL / journal entries | ERP/accounting | Odoo, QuickBooks, NetSuite or equivalent |
| Reconciliation | ERP + bank/data | Accounting system + bank feed |
| Reporting | Spreadsheet + BI | Excel/Sheets + BI |
| Close management | ERP + project/task | Odoo/project tracker |
| Approvals | Email/chat | Gmail/Outlook + Slack/Teams |
| Evidence | Documents | Drive/Notion/document store |

## Operations

| Capability | Connector category | Example target |
|---|---|---|
| Tasks/projects | Project tracker | Odoo/Notion/other tracker |
| Incidents | ITSM | ServiceNow/Jira/Freshservice class |
| SOP knowledge | Knowledge base | Notion/GitHub |
| Vendors | Procurement | Procurement system or structured database |
| Notifications | Chat/email | Slack/Teams + Gmail/Outlook |
| Scheduling | Calendar | Google/Microsoft calendar |

## HR

| Capability | Connector category | Example target |
|---|---|---|
| Recruiting | ATS | Greenhouse/Lever/Ashby/Workable class |
| Employee records | HRIS | Workday/BambooHR/Rippling/Gusto class |
| Onboarding | HRIS + calendar + knowledge | HRIS + Notion |
| Policies | Knowledge base | Notion/Confluence |
| Communication | Email/chat | Gmail/Outlook + Slack/Teams |
| Compensation | Compensation data | Approved compensation source |

## Nivy integration principle

Keep connector interfaces category-based. A skill should describe what data it needs, not hard-code one vendor unless that vendor is intentionally the implementation target.

## Separation of concerns

- **Skill:** knows how to perform one capability.
- **Command/workflow:** chains skills with checkpoints.
- **Router:** maps natural language requests to workflows.
- **Connector:** supplies or writes external data.
- **Policy layer:** defines permissions and approval requirements.
- **System of record:** stores the authoritative business state.
- **Audit layer:** records material decisions/actions.

## Initial Nivy stack mapping

| Layer | Initial direction |
|---|---|
| Workflow automation | n8n |
| Company knowledge | Notion + GitHub |
| ERP/CRM | Odoo Community where suitable |
| Accounting | Odoo/QuickBooks/Xero depending on client |
| HR records | Dedicated HRIS or controlled database |
| Email | Gmail/Microsoft 365 |
| Communication | Slack/Teams/WhatsApp where appropriate |
| AI runtime | Claude + other approved models |
| Local/private AI | Ollama where appropriate |
| Audit/provenance | Git + structured logs |

These are implementation candidates, not commitments. Each connector must be tested against the actual workflow and permissions before adoption.
