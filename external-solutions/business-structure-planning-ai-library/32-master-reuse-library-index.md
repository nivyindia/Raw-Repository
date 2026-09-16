# Master Reuse Library Index

**Status:** v1.0 — 2026-09-16

## Purpose

This is the master navigation layer for the Existing Business Structure, Planning & AI Asset Library. It connects external reusable assets to company capabilities, departments, workflows, implementation destinations, controls, and adoption status.

**Core rule:** `DISCOVER → EVALUATE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING`

## Library layers

| Layer | Files | Purpose |
|---|---|---|
| Discovery | 01, 05, 07, 08, 15 | Sources, scope, research coverage and tracking |
| Capability | 02, 09, 18, 19 | What work can be reused |
| Asset extraction | 10–14, 22–23, 25, 28–29 | Agents, skills, prompts, SOPs, templates, workflows and systems |
| Evaluation | 04, 20, 24, 26, 30 | Licensing, quality, controls and adoption |
| Architecture | 27, 31 | Connectors, approvals, systems of record and cross-department composition |
| Master navigation | 32–33 | Unified index and implementation roadmap |

## Department-to-asset map

| Department / function | Primary reusable layers | Priority | Destination |
|---|---|---:|---|
| Executive / Strategy | strategy, planning, productivity, enterprise search | P1 | Executive OS |
| Sales / RevOps | account research, lead scoring, outreach, pipeline, forecast | P0 | Revenue Engine |
| Marketing | strategy, campaigns, content, SEO, competitive intelligence | P0 | Marketing Engine |
| Customer Success | ticket triage, customer context, escalation, knowledge capture | P2 | Client Success Engine |
| Product | research, specs, roadmap, feedback synthesis | P2 | Product Engine |
| Engineering / IT | engineering workflows, issue management, documentation | P2 | Technology Engine |
| Finance / Accounting | reconciliation, close, reporting, cash flow, margin analysis | P1 | Finance Engine |
| HR / People | recruiting, screening, onboarding, performance, people reporting | P1 | People Engine |
| Legal / Compliance | contract review, NDA triage, compliance, risk workflows | P2 | Governance Engine |
| Operations | SOPs, capacity, vendors, change, runbooks, status reporting | P1 | Operations Engine |
| Data / Analytics | SQL, analysis, validation, dashboards, data interpretation | P2 | Data Engine |
| Knowledge Management | enterprise search, documentation, source provenance | P1 | Knowledge Layer |
| Automation | n8n, MCP/connectors, scheduled workflows, event triggers | P0 | Automation Layer |

## Reusable asset taxonomy

Every discovered item should be classified into one or more of these types:

1. **End-to-end system** — complete business workflow or operating system.
2. **Agent team** — coordinated specialist agents.
3. **Agent** — autonomous/semi-autonomous role capability.
4. **Workflow** — ordered multi-step process.
5. **Skill** — atomic reusable capability, normally instruction-driven.
6. **Prompt** — focused instruction pattern.
7. **SOP/process** — human/AI repeatable operating procedure.
8. **Template/playbook** — reusable structured artifact.
9. **Framework/method** — decision or planning methodology.
10. **Connector/MCP** — access to an external system or data source.
11. **Automation** — event, schedule, routing or execution logic.
12. **Governance/control** — approval, audit, security, provenance or permission mechanism.

## Standard asset record

Each important asset should eventually have these fields:

- `asset_id`
- `asset_name`
- `asset_type`
- `department`
- `capability`
- `source_publisher`
- `source_url`
- `license_or_access`
- `maintenance_status`
- `required_inputs`
- `outputs`
- `connectors`
- `permissions`
- `data_sensitivity`
- `human_approval`
- `reuse_mode`
- `nivy_destination`
- `test_status`
- `adaptation_status`
- `production_status`
- `last_verified`

## Adoption state machine

`DISCOVERED → SOURCE-VERIFIED → LICENSE-CHECKED → FUNCTION-TESTED → Nivy-ADAPTED → CONTROLLED-INTEGRATION → PILOT → PRODUCTION → REGRESSION-MONITORED`

If a source fails at any stage, record the reason rather than silently discarding it.

## Nivy architecture mapping

| External capability | Nivy implementation candidate |
|---|---|
| AI skills / commands | Claude skills/plugins + repository-managed Markdown |
| Agent orchestration | Claude/Cowork or approved agent runtime + n8n |
| Workflow automation | n8n |
| CRM / ERP | Odoo Community where suitable |
| Accounting | Odoo / QuickBooks / Xero according to client context |
| Company knowledge | Notion + GitHub |
| Source/provenance | Git + structured metadata |
| Communication | Gmail/Microsoft 365 + Slack/Teams/WhatsApp where appropriate |
| Data / analytics | SQL/warehouse/BI layer + approved data skills |
| Local/private model runtime | Ollama where appropriate |
| Human approvals | explicit approval gates + audit logs |

These are implementation candidates, not unconditional tool commitments.

## High-value external reference

Anthropic's Knowledge Work Plugins demonstrate the desired reusable pattern: plugins package skills, connectors, commands and sub-agents; the repository currently includes functions such as sales, marketing, customer support, product management, finance, legal, data, operations, HR, productivity and enterprise search. citeturn0search0turn0search6

Anthropic also documents plugin customization through company terminology, processes and connector configuration. citeturn0search0turn0search1

## Current completion map

- P0 Sales + Marketing: **complete**
- P1 Finance + Operations + HR: **complete**
- P2 Legal + Customer Success + Product + Data + Executive: **complete**
- Cross-department composition map: **complete**
- Master index: **complete**
- Implementation roadmap: **see 33**

## Next rule

Do not immediately build every listed capability. Start with the smallest revenue-critical slice, test the source asset unchanged where permitted, then adapt and integrate only after evidence of usefulness.
