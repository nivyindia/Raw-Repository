# Master Reuse Library Index

**Status:** v1.4 — 2026-09-16

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
| Workforce | 67–68 | Employee/manager/department dashboards, roles, responsibilities, KRA/KPI, daily work and workforce AI |
| Completeness audit | 69–71, 74–75 | Ideal-company capability audit, missing-capability backlog, capability model and final enterprise audit |
| Targeted gap research | 72–73 | P0/P1 missing-capability research and adoption map |
| Master navigation | 32–33, 66 | Unified index, roadmap and cross-company gap analysis |

## Department-to-asset map

| Department / function | Primary reusable layers | Priority | Destination |
|---|---|---:|---|
| Executive / Strategy | strategy, planning, productivity, enterprise search | P1 | Executive OS |
| Corporate Affairs / Board / IR | board management, corporate records, investor relations, disclosures | P1 | Corporate Affairs Engine |
| Corporate Development | M&A, diligence, valuation, integration | P1 | Corporate Development Engine |
| Treasury / Corporate Finance | liquidity, banking, financing, insurance | P0/P1 | Treasury & Corporate Finance Engine |
| Sales / RevOps | account research, lead scoring, outreach, pipeline, forecast | P0 | Revenue Engine |
| Marketing | strategy, campaigns, content, SEO, competitive intelligence | P0 | Marketing Engine |
| Customer Success | ticket triage, customer context, escalation, knowledge capture | P2 | Client Success Engine |
| Product / R&D | research, specs, roadmap, innovation portfolio | P2 | Product & Innovation Engine |
| Engineering / IT | engineering workflows, ITSM, application portfolio, documentation | P2 | Technology Engine |
| Finance / Accounting | reconciliation, close, reporting, cash flow, margin analysis | P1 | Finance Engine |
| HR / People | recruiting, screening, onboarding, performance, workforce OS | P0/P1 | People + Workforce Engine |
| Legal / Compliance / Audit | contracts, compliance, controls testing, audit, risk | P1/P2 | Governance Engine |
| Operations | SOPs, capacity, vendors, change, runbooks, status reporting | P1 | Operations Engine |
| Data / Analytics | SQL, analysis, validation, dashboards, data interpretation | P2 | Data Engine |
| Knowledge Management | enterprise search, documentation, source provenance, memory | P1 | Knowledge Layer |
| Automation | n8n, MCP/connectors, scheduled workflows, event triggers | P0 | Automation Layer |
| AI Governance / AgentOps | registry, identity, policy, approval, audit, evaluation, cost | P0/P1 | AI Control Plane |
| Process Intelligence | process mining, conformance, exceptions, optimization | P1 | Process Intelligence Layer |
| Procurement / Supply Risk | RFP, vendor evaluation, purchasing, supplier management, supply risk | P1 | Procurement Engine |
| Workforce Management | role architecture, org structure, employee cockpit, manager cockpit, KRA/KPI, goal cascade, task queue, performance evidence, workforce analytics | P0/P1 | Workforce Operating System |
| ESG / Sustainability | ESG data, carbon accounting, sustainability reporting, supplier sustainability | P1 | Sustainability Engine |
| Facilities / Travel / Physical Ops | workplace, travel, assets, physical security | P2 | Workplace Operations Engine |
| Quality | QMS, CAPA, quality audits, SLA management | P1/P2 | Quality Engine |

## Employee & Workforce Operating System

Dedicated research is consolidated in:

- **67** — Employee & Workforce Operating System reuse catalog
- **68** — Employee/Workforce adoption map

## International Company Completeness Audit

- **69** — Ideal international company completeness audit
- **70** — Missing capability research backlog
- **71** — Ideal company vs Nivy coverage matrix
- **72** — Targeted international company gap research
- **73** — Targeted gap adoption map
- **74** — Ideal international company capability model
- **75** — Final enterprise completeness audit

The targeted audit covers corporate secretary/board, treasury, internal audit, corporate development/M&A, enterprise architecture, SaaS management, ITSM, ESG/carbon, revenue assurance, transformation portfolio, entity/subsidiary management, investor relations, insurance, regulatory reporting, ethics, employee relations, global mobility, QMS, SLA management, facilities/travel, supply risk, crisis command, R&D/innovation, IP/patents and global tax control.

## Key newly verified reusable paths

- LQGovernance-OpenBoard — board governance with human approval and audit trail
- Decidiq — governance decisions/meetings/voting
- EIOS — entity-centered information architecture
- Agent-skills-collection — treasury, working capital, banking, FX, controls and audit skills
- Tessio / FreeITSM — self-hosted ITSM candidates
- security-atlas / riskready-community — GRC/control/audit candidates
- sustainability-project — ESG reporting candidate
- Rapo / revenue_leakage_system — revenue-assurance candidates
- legal-skills-open corporate skill — corporate legal/entity/governance skill

These are **candidates**, not automatically adopted production components; license, security, maintenance and functional testing remain mandatory.

## Cross-company infrastructure

New coverage is consolidated in:

- **60** — Cross-company AI infrastructure source catalog
- **61** — AgentOps, governance, identity and approval skill catalog
- **62** — Knowledge, memory and process intelligence catalog
- **63** — Contract, procurement and customer-success catalog
- **64** — Agent registry, identity, approval and exception catalog
- **65** — Cross-company AI infrastructure adoption map
- **66** — Master cross-company gap analysis

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
| Workforce / employee OS | HRKit/WorkSphere/SmartHR Nexus + reusable HR skills + Nivy-independent role/KRA/KPI schema |
| Corporate/enterprise gaps | 72–75 targeted research and audit |

## Cross-company architecture rule

The target is not one giant autonomous agent. It is:

`Registry + Identity + Policy + Router + Specialist Agents/Skills + Knowledge/Memory + MCP/API + Workflows + Approval + Audit + Evaluation + Cost + Exceptions + Systems of Record`

## Research completeness

The ideal international-company capability model has now been explicitly compared with the existing library. The targeted gap research provides a reuse path for the material P0/P1 gaps. The next default mode is **verification/testing/integration**, not endless generic discovery.

New discovery is justified only when a new capability, jurisdiction, industry requirement, obsolete candidate, or material implementation gap appears.
