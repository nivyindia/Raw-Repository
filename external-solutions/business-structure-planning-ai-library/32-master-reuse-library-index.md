# Master Reuse Library Index

**Status:** v1.1 — 2026-09-16

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
| Architecture | 27, 31, 60–65 | Connectors, approvals, systems of record and cross-company AI infrastructure |
| Master navigation | 32–33, 66 | Unified index, roadmap and gap analysis |

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
| Knowledge Management | enterprise search, documentation, source provenance, memory | P1 | Knowledge Layer |
| Automation | n8n, MCP/connectors, scheduled workflows, event triggers | P0 | Automation Layer |
| AI Governance / AgentOps | registry, identity, policy, approval, audit, evaluation, cost | P0/P1 | AI Control Plane |
| Process Intelligence | process mining, conformance, exceptions, optimization | P1 | Process Intelligence Layer |
| Procurement | RFP, vendor evaluation, purchasing, supplier management | P1 | Procurement Engine |

## Cross-company infrastructure

New coverage is consolidated in:

- **60** — Cross-company AI infrastructure source catalog
- **61** — AgentOps, governance, identity and approval skill catalog
- **62** — Knowledge, memory and process intelligence catalog
- **63** — Contract, procurement and customer-success catalog
- **64** — Agent registry, identity, approval and exception catalog
- **65** — Cross-company AI infrastructure adoption map
- **66** — Master cross-company gap analysis

These files cover the infrastructure needed to make separate agents operate as one controlled company system.

## Reusable asset taxonomy

1. End-to-end system
2. Agent team
3. Agent
4. Workflow
5. Skill
6. Prompt
7. SOP/process
8. Template/playbook
9. Framework/method
10. Connector/MCP
11. Automation
12. Governance/control
13. Registry/memory/evaluation infrastructure

## Standard asset record

`asset_id, asset_name, asset_type, department, capability, source_publisher, source_url, license_or_access, maintenance_status, required_inputs, outputs, connectors, permissions, data_sensitivity, human_approval, reuse_mode, nivy_destination, test_status, adaptation_status, production_status, last_verified`

## Adoption state machine

`DISCOVERED → SOURCE-VERIFIED → LICENSE-CHECKED → FUNCTION-TESTED → CONTROLLED-TESTED → Nivy-ADAPTED → PILOT → PRODUCTION → REGRESSION-MONITORED`

## Nivy architecture mapping

| External capability | Nivy implementation candidate |
|---|---|
| AI skills / commands | Claude skills/plugins + repository-managed Markdown |
| Agent orchestration | approved agent runtime + n8n |
| Workflow automation | n8n |
| CRM / ERP | Odoo Community where suitable |
| Accounting | Odoo / QuickBooks / Xero according to client context |
| Company knowledge | Notion + GitHub + approved search/RAG layer |
| Source/provenance | Git + structured metadata |
| AI asset registry | Registry metadata + Git |
| Tool control | MCP gateway/control plane candidate |
| Human approvals | explicit approval gates + audit logs |
| Observability/evaluation | OpenLIT/Phoenix/Future AGI/mcp-eval candidates |
| Local/private model runtime | Ollama where appropriate |

These are implementation candidates, not unconditional commitments.

## Cross-company architecture rule

The target is not one giant autonomous agent. It is:

`Registry + Identity + Policy + Router + Specialist Agents/Skills + Knowledge/Memory + MCP/API + Workflows + Approval + Audit + Evaluation + Cost + Exceptions + Systems of Record`

## Research completeness

Major functional departments and asset types are covered. The remaining work is controlled source verification, functional testing, integration, governance testing and production measurement rather than another generic discovery sweep. See **66-master-cross-company-gap-analysis.md**.
