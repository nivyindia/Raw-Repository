# Integration & Connector Registry

**Status:** v1.0 — 2026-09-16

## Purpose

Define the integration fabric required to connect reusable agents/workflows to systems of record without creating point-to-point spaghetti.

## Target integration architecture

`Systems of Record → Integration/Workflow Layer → Governed Tool/MCP Layer → Agents/Skills → Knowledge/Memory`

The control layer sits across all connections:

`Identity + Permissions + Policy + Approval + Audit + Observability + Cost + Exceptions`

## Core systems and roles

| System/category | Primary role | Typical connections |
|---|---|---|
| Odoo Community | ERP/CRM/operations candidate | Sales, finance, inventory, projects, HR where suitable |
| QuickBooks/Xero | Client accounting | CRM, invoices, payments, reporting |
| Email | External communication | CRM, calendar, support, outreach |
| Calendar | Scheduling | CRM, meetings, HR, delivery |
| WhatsApp/business messaging | Client/lead communication | CRM, support, notifications |
| n8n | Workflow/orchestration | Nearly every API/webhook-capable system |
| Mautic | Marketing automation candidate | CRM, forms, email, campaigns |
| GitHub | Code/docs/source control | Engineering, knowledge, automation registry |
| Notion | Knowledge/project workspace | Research, SOPs, decisions, project context |
| HR/workforce system | Employee system of record | Recruiting, onboarding, goals, performance |
| Helpdesk/ITSM | Service system of record | Tickets, assets, SLA, incidents, knowledge |
| Accounting/treasury | Financial system of record | Billing, reconciliation, cash, approvals |
| Analytics/warehouse | Reporting/semantic layer | CRM, finance, marketing, product, workforce |
| AI runtime | Model execution | Agents, skills, evaluation, routing |
| MCP/tool gateway | Governed tool access | Agents ↔ APIs/tools |

## Priority connection map

### Revenue

`Lead Source → Enrichment → CRM → Qualification → Outreach → Email/Messaging → Calendar → Meeting → CRM → Proposal → Contract → Invoice → Payment → Onboarding`

### Marketing

`Research → Content/Creative → Approval → CMS/Social/Email → Campaign → Analytics → CRM → Attribution`

### Delivery

`Won Deal → CRM → Project/Task → Knowledge/SOP → Team/Agent Work → QA → Client Update → Invoice → CS`

### Finance

`CRM/Orders → Invoice → Accounting → Bank → Reconciliation → Cash Position → Reporting`

### Workforce

`Recruiting → Candidate → Employee → Role → Goals/KRA/KPI → Tasks → Evidence → Review → Learning`

### Support/ITSM

`Email/Portal/Chat → Ticket → Classification → Assignment → SLA → Agent/Technician → Resolution → KB → Customer/Employee`

### Executive

`All Systems → Event/Metric Layer → Analytics → Exception Detection → Executive Brief → Decision → Assignment → Verification`

## Connector design rules

1. Prefer official APIs, webhooks and supported connectors.
2. Use one canonical system of record per business object.
3. Avoid duplicating master data across systems.
4. Use stable IDs and correlation IDs across workflows.
5. Store source timestamps and provenance.
6. Use idempotency for repeatable actions.
7. Separate read permissions from write permissions.
8. Require approval for high-impact writes.
9. Log actor, agent, user, tool, action, object and outcome.
10. Provide retry, timeout and dead-letter/exception handling.
11. Version schemas and workflow contracts.
12. Keep secrets outside repositories.
13. Test connectors against sandbox/synthetic data before production.
14. Provide manual fallback for business-critical paths.

## Connector maturity

`DISCOVERED → AUTHENTICATED → READ-TESTED → WRITE-TESTED → POLICY-CONTROLLED → AUDITED → INTEGRATED → MONITORED`

## Anti-patterns to prevent

- one-off API scripts with no owner
- shared credentials for multiple agents
- direct agent writes to critical systems without policy checks
- duplicated customer/employee/vendor master records
- workflows without idempotency
- silent failures
- no audit trail
- no rollback/manual fallback
- uncontrolled agent-to-agent tool access
