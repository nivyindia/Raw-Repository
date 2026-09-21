# Department System Reuse Catalog — September 2026

**Library layer:** L5 — Department Systems  
**Sequence:** Atomic Action → Micro Task → Task Automation → Workflow → Process → **Department System** → Cross-Department → AI Manager → Executive → Control Tower → Autonomous Company

## Purpose

L5 converts the L4 value streams into complete **department operating systems**. A department system is not merely a collection of agents: it combines capabilities, processes, workflows, data, roles, policies, KPIs, applications, integrations, controls, knowledge, approvals, observability and human/AI workforce.

**Rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## 1. Department system catalog

| ID | Department / system | Core operating scope | Primary process families | Reusable backbone candidates | Status |
|---|---|---|---|---|---|
| DS-001 | CEO / Executive Office OS | goals, decisions, priorities, executive briefings, board, exceptions | Strategy-to-Execution, Knowledge-to-Decision, Crisis-to-Recovery | control towers, BI, decision agents, unified workspace | Discovery |
| DS-002 | Strategy & Corporate Planning OS | strategy, OKR/KPI, initiatives, scenarios, benefits | Strategy-to-Execution, Portfolio-to-Benefits, Budget-to-Actuals | OKR/PPM, BI, scenario engines | Discovery |
| DS-003 | Finance OS | accounting, AP/AR, close, cash, FP&A, tax, controls | Record-to-Report, Invoice-to-Cash, Cash-to-Treasury | Odoo, ERPNext, ERPClaw, ERP/accounting systems | Discovery |
| DS-004 | Accounting OS | GL, AP, AR, reconciliation, close, audit evidence | Record-to-Report, Invoice-to-Cash | ERP/accounting, reconciliation, document/OCR | Discovery |
| DS-005 | Treasury OS | cash, banks, liquidity, FX, funding, payment controls | Cash-to-Treasury | treasury/bank connectivity, ERP, workflow | Discovery |
| DS-006 | Tax & Statutory OS | tax data, calculation, filing, notices, evidence | Tax-to-Compliance, Payroll-to-Accounting | tax engines, ERP, compliance workflow | Discovery |
| DS-007 | FP&A / Performance OS | budgets, forecasts, variance, scenarios, management reporting | Revenue-to-Forecast, Budget-to-Actuals | BI, planning, forecasting agents | Discovery |
| DS-008 | Sales / RevOps OS | ICP, leads, enrichment, outreach, pipeline, proposals, forecast | Lead-to-Cash, Quote-to-Order, Revenue-to-Forecast | CRM, n8n, sales agents, CPQ | Discovery |
| DS-009 | Marketing OS | brand, content, SEO/GEO, campaigns, ads, social, attribution | Campaign-to-Revenue, Content-to-Distribution | CMS, ad APIs, n8n, content agents, analytics | Discovery |
| DS-010 | Growth / Demand Gen OS | acquisition, experimentation, funnels, attribution, CRO | Campaign-to-Revenue, Digital-Presence-to-Revenue | analytics, experimentation, ad platforms | Discovery |
| DS-011 | Customer Success OS | onboarding, adoption, health, renewals, expansion, churn | Customer-Lifecycle-to-Retention | CRM/CS, product analytics, lifecycle automation | Discovery |
| DS-012 | Customer Support / Service OS | intake, triage, SLA, diagnosis, escalation, knowledge | Customer-Issue-to-Knowledge, Incident-to-Resolution | ITSM/helpdesk, knowledge/RAG, AI support | Discovery |
| DS-013 | Product Management OS | discovery, roadmap, requirements, prioritization, lifecycle | Idea-to-Product, Product-Feedback-to-Roadmap | product boards, analytics, research agents | Discovery |
| DS-014 | Engineering / Development OS | code, review, CI/CD, releases, architecture | Idea-to-Product, Model/Agent-to-Production | GitHub, CI/CD, agentic coding, workflow engines | Discovery |
| DS-015 | QA / Quality Engineering OS | test strategy, automation, regression, release quality | Idea-to-Product, Problem-to-Prevention | test frameworks, CI/CD, eval systems | Discovery |
| DS-016 | IT / Internal Technology OS | endpoints, apps, service desk, identity, assets, infrastructure | Request-to-Fulfillment, Employee-Access-Lifecycle | ITSM, MDM, Keycloak, asset systems | Discovery |
| DS-017 | Cybersecurity / SecOps OS | SOC, vulnerabilities, incidents, IAM, threat response | Security-Event-to-Remediation | SIEM/SOAR, security agents, ITSM | Discovery |
| DS-018 | HR / People OS | workforce, employee lifecycle, performance, benefits | Hire-to-Retire | HRIS, ATS, LMS, workflow | Discovery |
| DS-019 | Recruitment / Talent OS | sourcing, screening, interviews, offers, talent pools | Hire-to-Retire | ATS, sourcing tools, AI recruiting | Discovery |
| DS-020 | Learning / L&D OS | skills, training, certification, capability development | Hire-to-Retire, Change-to-Adoption | LMS, skills graph, AI tutors | Discovery |
| DS-021 | Payroll / Compensation OS | payroll, compensation, benefits, statutory handoff | Payroll-to-Accounting | payroll/HRIS, finance ERP | Discovery |
| DS-022 | Procurement / Sourcing OS | category, suppliers, RFQ, bids, negotiation, PO | Source-to-Contract, Procure-to-Pay | procurement suites, ProcessMaker, ERP | Discovery |
| DS-023 | Supplier / Vendor Management OS | onboarding, risk, performance, renewal | Supplier-to-Performance | SRM, procurement, contract systems | Discovery |
| DS-024 | Legal / Legal Ops OS | matters, contracts, research, deadlines, spend | Legal-Matter-to-Closure, Contract-to-Renewal | CLM, legal ops, document AI | Discovery |
| DS-025 | Compliance / GRC OS | obligations, controls, risk, evidence, audits | Policy-to-Control, Compliance-to-Evidence | GRC, OPA, evidence systems | Discovery |
| DS-026 | Privacy OS | consent, DSAR, data mapping, retention, deletion | Privacy-Request-to-Closure, Data-to-Governance | privacy/GRC, data discovery | Discovery |
| DS-027 | Operations / COO OS | service delivery, capacity, SOPs, exceptions, performance | Request-to-Fulfillment, Strategy-to-Execution | ERP, workflow, control tower | Discovery |
| DS-028 | Project / PMO OS | intake, planning, resources, dependencies, delivery, benefits | Portfolio-to-Benefits, Change-to-Adoption | PPM, project tools, BI | Discovery |
| DS-029 | Data / Analytics OS | ingestion, quality, semantic layer, BI, metrics | Data-to-Decision, Data-to-Governance | Airbyte, Debezium, NocoDB/NocoBase, BI | Discovery |
| DS-030 | AI / ML / Agent Platform OS | model/agent lifecycle, evals, routing, memory, governance | Model/Agent-to-Production, AI-Run-to-Audit | LangGraph, LiteLLM, Langfuse, Promptfoo | Discovery |
| DS-031 | Knowledge Management OS | taxonomy, search, RAG, content lifecycle, provenance | Knowledge-to-Decision, Customer-Issue-to-Knowledge | RAG, knowledge graph, Mem0/MemoryOS | Discovery |
| DS-032 | Document / Records OS | capture, OCR, authoring, approval, retention, legal hold | Compliance-to-Evidence, Record-to-Report | OCR, document generation, e-signature, records systems | Discovery |
| DS-033 | Business Intelligence / Reporting OS | metrics, dashboards, alerts, reporting, executive packs | Data-to-Decision, Revenue-to-Forecast | Metabase, Superset, OpenBI, Helical Insight | Discovery |
| DS-034 | Facilities / Workplace OS | space, maintenance, vendors, access, safety, occupancy | Facilities-to-Workplace | IWMS/CMMS, access control, workflow | Discovery |
| DS-035 | Fleet / Mobility OS | vehicles/assets, assignment, maintenance, fuel, incidents | Fleet-to-Disposal | fleet systems, telematics, workflow | Discovery |
| DS-036 | Logistics / Supply Chain OS | inventory, warehouse, transport, delivery, exceptions | Inventory-to-Replenishment, Logistics-to-Delivery | ERP/WMS/TMS, carrier APIs | Discovery |
| DS-037 | Manufacturing / Delivery OS | planning, production/service delivery, quality, maintenance | Idea-to-Product, Problem-to-Prevention | ERP/MRP/MES/QMS | Discovery |
| DS-038 | Field Service OS | scheduling, dispatch, technicians, parts, proof, billing | Field-Service-to-Closure | FSM, mobile workflows, maps | Discovery |
| DS-039 | Ecommerce / Commerce OS | catalog, pricing, checkout, fulfillment, returns | Ecommerce Order-to-Fulfillment | commerce/OMS/WMS/payment systems | Discovery |
| DS-040 | Marketplace Operations OS | seller lifecycle, catalog, orders, fees, disputes, settlement | Marketplace-to-Settlement | marketplace platforms, ledger/payment systems | Discovery |
| DS-041 | Subscription / Billing OS | entitlement, usage, billing, dunning, renewals | Subscription-to-Renewal | billing/subscription platforms, payment APIs | Discovery |
| DS-042 | Partnerships / PRM OS | partner onboarding, deal registration, co-sell, commissions | Partner-to-Revenue | PRM, CRM, partner portals | Discovery |
| DS-043 | Affiliate / Referral OS | tracking, attribution, fraud, commission, payout | Partner-to-Revenue | affiliate platforms, analytics, payments | Discovery |
| DS-044 | Community / Membership OS | membership, onboarding, moderation, engagement, renewal | Customer-Lifecycle-to-Retention | community platforms, CRM, automation | Discovery |
| DS-045 | PR / Corporate Communications OS | messaging, media, announcements, approvals, reputation | Digital-Presence-to-Revenue, Crisis-to-Recovery | media monitoring, CMS, workflow | Discovery |
| DS-046 | Investor Relations / Fundraising OS | investor CRM, KPI packs, diligence, data room, reporting | Fundraise-to-Close | CRM, data room, document/approval systems | Discovery |
| DS-047 | Corporate Development / M&A OS | target scan, diligence, valuation, approvals, integration | M&A-to-Integration | research, data rooms, PPM, workflow | Discovery |
| DS-048 | Innovation / R&D OS | research, experiments, IP, pilots, commercialization | Innovation-to-Commercialization | research/eval systems, PPM, knowledge | Discovery |
| DS-049 | Sustainability / ESG OS | environmental/social data, targets, evidence, disclosure | Sustainability-to-Disclosure | ESG systems, data pipelines, BI | Discovery |
| DS-050 | Government / Public Sector Bid OS | tender discovery, eligibility, bid, compliance, submission | Government-Tender-to-Contract | tender intelligence, document AI, CLM | Discovery |
| DS-051 | Grants Management OS | opportunity, eligibility, application, milestones, reporting | Grant-to-Compliance | grant systems, workflow, evidence | Discovery |
| DS-052 | International Trade OS | customs, classification, sanctions, documentation, shipment | Logistics-to-Delivery, Tax-to-Compliance | trade compliance, ERP/TMS | Discovery |
| DS-053 | Risk / Insurance OS | risk register, policies, claims, coverage, renewals | Risk-to-Treatment | GRC, insurance systems, workflow | Discovery |
| DS-054 | Business Continuity / Crisis OS | BIA, continuity, crisis command, communications, recovery | Crisis-to-Recovery | BCP/DR, incident command, workflow | Discovery |
| DS-055 | Enterprise Architecture OS | capability map, application portfolio, dependencies, standards | Strategy-to-Execution, Data-to-Governance | EA repositories, graph/CMDB | Discovery |
| DS-056 | Master Data / Data Governance OS | golden records, ownership, lineage, quality, retention | Data-to-Governance | MDM/data catalog, ETL, policy | Discovery |
| DS-057 | AI Governance / Responsible AI OS | inventory, risk tiers, evaluations, approvals, monitoring | Model/Agent-to-Production, AI-Run-to-Audit | policy/eval/observability platforms | Discovery |
| DS-058 | Knowledge / Research Intelligence OS | external research, evidence, synthesis, publishing | Research-to-Knowledge, Knowledge-to-Decision | GPT Researcher, STORM, SearXNG, RAG | Discovery |
| DS-059 | Digital Presence / Web OS | domains, website, SEO/GEO, forms, chat, listings, analytics | Digital-Presence-to-Revenue | CMS, SEO/GEO, analytics, automation | Discovery |
| DS-060 | Corporate Administration OS | correspondence, calendars, travel, records, assets, approvals | Request-to-Fulfillment, Asset-to-Disposal | workflow, document, calendar, ERP | Discovery |

## 2. Department system contract

Every L5 department system must define:

**Mission → Capabilities → Processes → Workflows → Roles → Human workforce → AI workforce → Systems → Data → Events → Integrations → Policies → Approvals → Controls → KPIs → SLAs/SLOs → Knowledge → Exceptions → Audit → Cost → Continuous improvement**

Minimum system objects:

| Object | Required fields |
|---|---|
| Department | owner, mission, scope, authority, budget |
| Capability | outcome, process links, maturity, owner |
| Process | L4 ID, trigger, stages, outcome, KPI |
| Role | human/AI role, permissions, authority |
| System | application, module, owner, data domain |
| Integration | source, target, event/API, auth, SLA |
| Policy | rule, risk level, authority, evidence |
| Approval | action, threshold, approver, delegation, timeout |
| KPI | definition, formula, source, target, owner |
| Knowledge | source, scope, freshness, provenance |
| Incident | severity, owner, response, RCA, learning |
| Cost | people, SaaS, compute, transaction, budget |
| Audit | actor, action, evidence, timestamp, retention |

## 3. Standard department layers

Every department should be evaluated across:

1. Strategy and objectives.
2. Organization and roles.
3. Core capabilities.
4. L4 business processes.
5. L3 workflows.
6. L2 task automations.
7. L1/L0 atomic building blocks.
8. Human workforce.
9. AI employees/agents.
10. Business applications.
11. Data and knowledge.
12. Integrations/connectors/APIs/MCP/A2A.
13. Identity/RBAC/secrets.
14. Policies and approvals.
15. Risk/security/privacy/compliance.
16. KPI/OKR/SLA/SLO.
17. Reporting and dashboards.
18. Exception/recovery/self-healing.
19. Observability/evaluation/testing.
20. SOPs/templates/playbooks/runbooks.
21. Cost/FinOps.
22. Backup/DR.
23. Lifecycle/versioning/retirement.
24. Training/change/adoption.
25. Continuous discovery and optimization.

## 4. Department system architecture

Canonical pattern:

**User / Customer / Event → Identity & Context → Department Workspace → AI Manager / Human Manager → Process → Workflow → AI Employee / Human → Tool / System / API → Policy & Approval Gate → Action → Verification → KPI / Outcome → Audit / Evidence → Knowledge / Learning**

Cross-department handoffs must use explicit contracts:

**Source Department → Event / Request → Data Contract → Policy Check → Target Department → SLA → Acknowledgement → Outcome → Reconciliation → Audit**

## 5. Reusable technology families

| Layer | Candidate families |
|---|---|
| ERP/business backbone | Odoo, ERPNext, ERPClaw, NocoBase |
| CRM/RevOps | CRM platforms, n8n sales workflows, sales agents |
| Workflow | n8n, Activepieces, Windmill, Kestra, Temporal |
| Forms/approvals | forms-flow-ai, django-forms-workflows, ProcessMaker |
| Agent orchestration | LangGraph, GAIA and comparable frameworks |
| Integrations | Composio, API/webhooks, Airbyte, Debezium |
| Identity/policy | Keycloak, OpenFGA, OPA |
| Browser/computer use | Playwright MCP, Browser Use, Crawl4AI |
| Research | GPT Researcher, STORM, Perplexica, SearXNG |
| Documents | Rendoc MCP, ComPDFKit Generation, Typst, ContractSpark |
| BI/reporting | Metabase, Superset, OpenBI, Helical Insight |
| Observability/evaluation | Langfuse, Phoenix-class systems, Promptfoo |
| Memory/knowledge | Mem0, MemoryOS, Eidetic OS, Qdrant/Neo4j |
| Data/MDM | NocoBase/NocoDB/Directus, Airbyte, Debezium, data catalogs |
| Durable recovery | Temporal, Kestra, DLQ/replay/compensation |
| Unified workspace | Nivy shell + role-aware dashboards + embedded specialized systems |

## 6. Department qualification gates

**G0 Department identity → G1 Mission/scope → G2 Capability map → G3 L4 process coverage → G4 L3 workflow coverage → G5 L2/L1/L0 coverage → G6 Existing-solution discovery → G7 License/commercial review → G8 System/data/integration architecture → G9 Roles/RBAC/approval → G10 KPI/SLA/control → G11 Security/privacy/compliance → G12 Exception/recovery → G13 Observability/evaluation/testing → G14 Cost/TCO → G15 Runtime evidence → G16 Nivy fit → G17 Ownership/adoption**

Department systems remain **candidate architectures** until qualification evidence exists.

## 7. Department completeness matrix

| Domain | Minimum department systems |
|---|---|
| Executive | CEO, Strategy, Corporate Performance |
| Revenue | Sales/RevOps, Marketing, Growth, Customer Success, Support |
| Product/Delivery | Product, Engineering, QA, Operations, Projects |
| People | HR, Recruitment, L&D, Payroll/Compensation |
| Money | Finance, Accounting, Treasury, Tax, FP&A |
| Enterprise control | Legal, Compliance/GRC, Privacy, Risk/Insurance, Security |
| Technology/Data | IT, Data/Analytics, AI/ML/Agent, Knowledge, AI Governance |
| Supply/Physical | Procurement, Supplier, Inventory/Logistics, Manufacturing/Delivery, Field Service, Fleet, Facilities |
| Commerce | Ecommerce, Marketplace, Subscription/Billing |
| Ecosystem | Partnerships/PRM, Affiliate/Referral, Community |
| Corporate | PR/Communications, IR/Fundraising, Corp Dev/M&A, Innovation/R&D |
| Public/International | Government Bids, Grants, International Trade |
| Enterprise architecture | EA, MDM/Data Governance, BCP/Crisis, Sustainability |
| Digital | Digital Presence/Web, Research Intelligence, Corporate Administration |

## 8. L5 remaining discovery gaps

- Deep resource discovery for **each department**, not just department names.
- Industry-specific department systems and vertical SaaS.
- Exact open-source/commercial module qualification by department.
- Department-level AI employee/agent rosters and skills.
- Department data models, event contracts and integration maps.
- Department-specific KPI trees and benchmark sources.
- Department-level approval matrices and policy-as-code.
- Runtime qualification of candidate systems.
- Cost/TCO and migration/adapter assessment.
- Complete cross-department contracts before L6.

## 9. Completion rule

For every L5 department system eventually produce:

**Department charter → capability map → process map → workflow map → task/atomic map → system map → data model → event/integration map → human/AI workforce map → role/RBAC map → policy/approval map → KPI/SLA map → knowledge map → exception/recovery map → security/privacy/compliance map → observability/evaluation map → cost/TCO → implementation adapter → runtime evidence**

**Catalog status: L5 Department System Discovery started.**
