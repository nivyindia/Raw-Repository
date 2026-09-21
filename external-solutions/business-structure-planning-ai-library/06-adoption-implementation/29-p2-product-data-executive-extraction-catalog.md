# P2 Product, Data & Executive — Reusable Solution Extraction Catalog

**Status:** Research catalog / reuse-first
**Date:** 2026-09-16

## 1. Product Management

Primary reusable source: Anthropic Knowledge Work Plugins — product-management.
Official source: https://github.com/anthropics/knowledge-work-plugins

The official plugin catalog describes product-management capabilities including specification writing, roadmap planning, user-research synthesis, stakeholder updates and competitive-landscape tracking. Listed connector categories include Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom and Fireflies.

| Capability | Reuse candidate | Nivy use | Gate |
|---|---|---|---|
| PRD/spec drafting | Product spec workflow | Define Nivy products/features | Product owner approval |
| Roadmap planning | Roadmap workflow | Prioritize product work | Human decision |
| User research synthesis | Research synthesis | Turn interviews/tickets into insights | Source traceability |
| Stakeholder updates | Product status workflow | Weekly/monthly updates | Accuracy check |
| Competitive research | Competitive landscape workflow | Monitor competitors | Source/date verification |
| Launch coordination | Product launch workflow | Coordinate marketing/sales/ops | Launch owner |

## 2. Data & Analytics

The Knowledge Work Plugins repository also contains a data-oriented plugin category. Use it as a reusable pattern for analysis requests, data preparation, reporting and connector-backed analytical workflows rather than building a custom analyst agent first.

Candidate atomic capabilities:
- data request intake
- data-source discovery
- data cleaning/preparation
- metric definition
- exploratory analysis
- KPI reporting
- anomaly/variance investigation
- executive data brief
- reproducible analysis handoff

Recommended Nivy implementation pattern:
`User request → Router → Data skill → approved data connector → analysis → validation → report/dashboard → human sign-off where material → system of record`.

Controls:
- least-privilege data access
- explicit metric definitions
- source and query provenance
- reproducible calculations
- no fabricated data
- separate analysis from consequential business decisions

## 3. Executive / Productivity

The official productivity plugin covers tasks, calendars, daily workflows and personal context, with connectors such as Slack, Notion, Asana, Linear, Jira, Monday, ClickUp and Microsoft 365. This is reusable as the executive coordination layer rather than creating another task-management agent from scratch.

Potential Nivy capabilities:
- daily executive briefing
- priority extraction
- meeting preparation
- action-item extraction
- weekly review
- project/status synthesis
- decision log preparation
- cross-department escalation routing

## 4. Cross-department composition candidates

| Need | Compose from |
|---|---|
| New product launch | Product spec + competitive research + marketing campaign + sales enablement + support readiness |
| Client onboarding | Sales handoff + operations checklist + finance setup + contract/approval + customer success |
| Monthly business review | CRM pipeline + marketing performance + finance KPIs + operations status + customer health |
| AI governance | AI inventory + legal/regulatory monitor + security review + executive approval |
| Customer escalation | Support triage + customer context + product issue + delivery status + executive escalation |

## Sources
- Anthropic, Knowledge Work Plugins: https://github.com/anthropics/knowledge-work-plugins
