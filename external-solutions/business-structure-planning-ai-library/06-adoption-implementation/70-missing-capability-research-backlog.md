# Missing Capability Research Backlog

**Status:** v1.0 — 2026-09-16
**Purpose:** Research only the material capabilities identified by the international-company completeness audit as missing or under-covered in the existing reuse library.

## P0 discovery backlog

| ID | Missing capability | What to search for | Target reusable asset types |
|---|---|---|---|
| GAP-01 | Corporate Secretary / Board Management | board portal, board packs, resolutions, minutes, action tracking, statutory records | SaaS/open-source systems, workflows, agents, templates |
| GAP-02 | Treasury & Banking Operations | cash positioning, bank reconciliation, payment approvals, liquidity forecast, bank connectivity | treasury platforms, finance skills, APIs, workflows |
| GAP-03 | Internal Audit / Controls Testing | audit planning, control testing, evidence collection, findings, remediation | audit platforms, control frameworks, agents, templates |
| GAP-04 | Corporate Development / M&A | target sourcing, diligence, valuation, integration planning, synergy tracking | M&A platforms, research agents, diligence workflows |
| GAP-05 | Enterprise Architecture / Application Portfolio | application inventory, architecture maps, dependency mapping, technical debt, standards | EA tools, architecture repositories, agents, skills |
| GAP-06 | Software/SaaS Asset Management | SaaS inventory, licenses, renewals, spend, shadow IT, vendor overlap | SAM/SaaS-management tools, workflows, agents |
| GAP-07 | ITSM / Enterprise Service Desk depth | incident, request, problem, change, asset, SLA, knowledge workflows | ITSM platforms, AI service-desk agents, MCP/connectors |
| GAP-08 | ESG/Sustainability + Carbon Accounting | ESG data, GHG scopes, emissions factors, sustainability reporting, evidence | ESG platforms, calculators, reporting agents |
| GAP-09 | Revenue Assurance | leakage, billing validation, contract-to-invoice checks, revenue reconciliation | revenue-assurance tools, finance agents, workflows |
| GAP-10 | Corporate Transformation Portfolio | transformation initiatives, benefits, dependencies, investment, executive governance | EPM/portfolio tools, PMO agents, dashboards |
| GAP-11 | Global Entity/Subsidiary Management | entity registry, directors, ownership, filings, deadlines, intercompany governance | entity-management platforms, compliance workflows |

## P1 discovery backlog

| ID | Missing capability | What to search for |
|---|---|---|
| GAP-12 | Investor Relations | earnings calendar, shareholder communications, investor Q&A, disclosures, IR CRM |
| GAP-13 | Insurance Management | policies, renewals, claims, coverage, certificates, risk financing |
| GAP-14 | Regulatory Reporting / Disclosure | regulatory calendars, filing preparation, disclosure controls, evidence workflows |
| GAP-15 | Ethics / Whistleblower Case Management | anonymous intake, triage, investigations, case controls, reporting |
| GAP-16 | Employee Relations / Grievance | case management, investigations, policy workflows, documentation |
| GAP-17 | Global Mobility / Immigration | visas, work permits, relocation, expiry monitoring, employee mobility |
| GAP-18 | Quality Management / QMS | quality objectives, nonconformity, CAPA, audits, document control |
| GAP-19 | SLA / Service-Level Management | SLA definitions, monitoring, breach alerts, service credits, reporting |
| GAP-20 | Facilities / Workplace | work orders, space, vendors, maintenance, visitor/front desk, workplace services |
| GAP-21 | Corporate Travel / Expense | travel booking, policy enforcement, expense reconciliation, duty of care |
| GAP-22 | Supply Risk / Supplier Intelligence | supplier risk, geopolitical exposure, concentration, performance, alerts |
| GAP-23 | Crisis Command Center | crisis playbooks, incident command, emergency communications, stakeholder updates |
| GAP-24 | R&D / Innovation Portfolio | ideas, experiments, research portfolio, stage gates, investment, outcomes |
| GAP-25 | IP / Patent Portfolio | invention disclosure, patent deadlines, trademarks, IP monitoring |
| GAP-26 | Global Tax Control Tower | tax calendar, filings, obligations, evidence, country/entity matrix |

## P2 specialist backlog

- Physical security management
- Physical asset/fleet management
- Legal hold and advanced records lifecycle
- Corporate/public/government affairs
- Responsible sourcing and supplier sustainability
- Enterprise risk stress testing and scenario analysis
- Advanced stakeholder engagement

## Research method for every gap

For each missing capability search in this order:

1. Complete commercial platform
2. Open-source/self-hosted system
3. AI agent / agent team
4. Agent skill / plugin
5. MCP server / connector
6. API
7. n8n/Make/Zapier workflow
8. RPA/browser automation
9. SOP/process framework
10. Templates/playbooks/checklists
11. Calculators/datasets/reference models
12. Community/practitioner implementations

Record:

`name | URL | publisher | resource_type | license/access | capabilities | inputs | outputs | integrations | security | human approval | maintenance | cost | reuse mode | test status | Nivy destination`

## Stop rule

Do not turn this backlog into another uncontrolled discovery expansion. A gap moves to **covered** when the library has at least one credible reusable path for the capability plus enough implementation information to test it. A gap moves to **implementation** only after source/license/function testing.
