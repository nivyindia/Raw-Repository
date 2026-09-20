# Business Process & Value-Stream Reuse Catalog — September 2026

**Library layer:** L4 — Business Processes / Value Streams  
**Sequence:** Atomic Action → Micro Task → Task Automation → Workflow → **Process / Value Stream** → Department → Cross-Department → AI Manager → Executive → Control Tower → Autonomous Company

## Purpose

This catalog turns the L3 workflow layer into **end-to-end business processes/value streams**. A process is broader than one workflow: it crosses multiple teams, systems, controls, decisions and measurable business outcomes.

**Governing rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## 1. L4 process catalog

| ID | Business process / value stream | Canonical end-to-end flow | Primary reusable solution families | Status |
|---|---|---|---|---|
| BP-001 | Lead-to-Cash | Demand → lead → qualify → opportunity → quote → contract → order → fulfill → invoice → collect → recognize revenue | CRM/RevOps, ERP, workflow, sales agents | Discovery |
| BP-002 | Quote-to-Order | Requirement → pricing → margin/policy → quote → approval → signature → order | CRM/CPQ, approval engines, e-signature | Discovery |
| BP-003 | Order-to-Cash | Order → fulfillment → delivery → invoice → payment → reconciliation → close | ERP/Odoo/ERPNext, billing, payment, finance workflows | Discovery |
| BP-004 | Procure-to-Pay | Need → requisition → sourcing → RFQ → comparison → approval → PO → receipt → invoice → payment → supplier review | Procurement suites, ERP, ProcessMaker, workflow engines | Discovery |
| BP-005 | Source-to-Contract | Category strategy → supplier discovery → qualification → RFQ → negotiation → risk → contract → obligations | Procurement, CLM, supplier-risk platforms | Discovery |
| BP-006 | Hire-to-Retire | Workforce plan → requisition → recruit → select → hire → onboard → develop → compensate → transfer → exit → archive | ATS/HRIS, HR workflow, identity/RBAC | Discovery |
| BP-007 | Employee-Access Lifecycle | Join/change/exit → identity → role → access → asset → periodic review → revoke → evidence | Keycloak, OpenFGA, OPA, HR/IT workflows | Discovery |
| BP-008 | Idea-to-Product | Idea → research → discovery → requirements → design → build → QA → release → adoption → retirement | Product systems, GitHub, CI/CD, agentic engineering | Discovery |
| BP-009 | Product-Feedback-to-Roadmap | Feedback → cluster → severity/value → insight → roadmap decision → prioritization → delivery → outcome | Support/CRM, analytics, product boards, AI clustering | Discovery |
| BP-010 | Campaign-to-Revenue | Strategy → audience → creative → media → lead → qualification → opportunity → revenue → attribution → optimization | Ad platforms, CRM, attribution, marketing automation | Discovery |
| BP-011 | Content-to-Distribution | Research → brief → creation → review → approval → publish → syndicate → measure → repurpose → archive | CMS, content agents, n8n/Activepieces, social APIs | Discovery |
| BP-012 | Customer-Lifecycle-to-Retention | Acquire → onboard → adopt → support → health → renew → expand → churn/win-back → offboard | CRM/CS, product analytics, lifecycle automation | Discovery |
| BP-013 | Customer-Issue-to-Knowledge | Issue → diagnose → resolve → verify → root cause → lesson → article → review → publish → reuse | ITSM/support, knowledge/RAG, research agents | Discovery |
| BP-014 | Incident-to-Resolution | Detect → triage → severity → assign → mitigate → resolve → verify → RCA → corrective action | SRE/ITSM, Temporal/Kestra, incident agents | Discovery |
| BP-015 | Problem-to-Prevention | Problem → RCA → corrective action → verification → preventive control → monitoring → effectiveness review | QMS/CAPA, incident systems, analytics | Discovery |
| BP-016 | Request-to-Fulfillment | Request → validate → policy → approve → assign → execute → evidence → close → measure | Forms/workflow, service catalogs, approvals | Discovery |
| BP-017 | Record-to-Report | Capture → classify → post → reconcile → close → consolidate → report → review → audit | ERP/accounting, BI, close automation | Discovery |
| BP-018 | Invoice-to-Cash | Billable event → invoice → delivery → payment status → dunning → dispute → settlement → reconciliation | Billing, payments, AR automation | Discovery |
| BP-019 | Cash-to-Treasury | Bank/payment feeds → cash position → forecast → liquidity → funding/FX → controls → reconciliation → reporting | Treasury, bank connectivity, finance automation | Discovery |
| BP-020 | Revenue-to-Forecast | Pipeline → bookings → billing → collections → actuals → forecast → variance → corrective action | RevOps, FP&A, BI, forecasting agents | Discovery |
| BP-021 | Payroll-to-Accounting | HR changes → payroll inputs → validation → payroll run → statutory outputs → accounting → reconciliation | Payroll/HRIS, finance ERP, tax workflows | Discovery |
| BP-022 | Tax-to-Compliance | Transaction data → jurisdiction/rules → calculation → reconciliation → filing → evidence → notice/response | Tax engines, ERP, compliance workflow | Discovery |
| BP-023 | Expense-to-Reimbursement | Receipt → OCR → policy → duplicate check → approval → reimbursement → accounting → audit | OCR, expense systems, approval workflows | Discovery |
| BP-024 | Contract-to-Renewal | Draft → legal review → risk → approval → sign → obligations → milestones → expiry → renew/amend/terminate | CLM, ContractSpark, e-signature, alerts | Discovery |
| BP-025 | Risk-to-Treatment | Identify → assess → score → prioritize → treatment → owner → monitor → accept/transfer/mitigate | GRC, risk registers, AI risk analysis | Discovery |
| BP-026 | Policy-to-Control | Policy → control objective → control → owner → implementation → evidence → test → remediation → attestation | GRC, OPA/policy-as-code, audit systems | Discovery |
| BP-027 | Compliance-to-Evidence | Obligation → control mapping → evidence request → collection → validation → gap → remediation → audit package | GRC, document/evidence systems, knowledge | Discovery |
| BP-028 | Data-to-Decision | Ingest → quality → master/semantic model → analysis → insight → decision → action → outcome → learning | Airbyte/Debezium, BI, semantic/data platforms | Discovery |
| BP-029 | Data-to-Governance | Discover → classify → owner → glossary → lineage → access → quality → retention → audit | Data catalog/governance, OpenMetadata-class systems | Discovery |
| BP-030 | Model/Agent-to-Production | Design → data/eval set → test → risk review → approval → deploy → observe → rollback/update → retire | LangGraph, LiteLLM, Langfuse, Promptfoo, governance | Discovery |
| BP-031 | AI-Run-to-Audit | Request → identity → policy/budget → model/tool → execution → validation → trace → evidence → audit | A2A governance, OPA, Langfuse, audit ledger | Discovery |
| BP-032 | Automation-Lifecycle-to-Retirement | Discover → specify → build/adapt → test → approve → deploy → observe → optimize → rollback → retire | n8n/Activepieces/Windmill, CI/CD, registries | Discovery |
| BP-033 | Asset-to-Disposal | Acquire → register → assign → maintain → inspect → depreciate/track → return → dispose → evidence | ERP/asset management, ITAM, workflow | Discovery |
| BP-034 | Supplier-to-Performance | Onboard → contract → order → delivery → quality → scorecard → remediation → renewal | SRM/procurement, ERP, analytics | Discovery |
| BP-035 | Inventory-to-Replenishment | Demand → stock visibility → forecast → reorder → approval → PO → receipt → put-away → reconciliation | ERP/WMS, forecasting, procurement workflows | Discovery |
| BP-036 | Logistics-to-Delivery | Order → allocate → pick/pack → dispatch → track → exception → delivery → proof → reconciliation | WMS/TMS, carrier APIs, field workflows | Discovery |
| BP-037 | Field-Service-to-Closure | Request → triage → schedule → dispatch → execute → parts/time → proof → invoice → feedback | FSM, scheduling, mobile workflows | Discovery |
| BP-038 | Facilities-to-Workplace | Space/service request → approval → vendor/work order → execution → inspection → invoice → asset/history | IWMS/CMMS, procurement, service workflows | Discovery |
| BP-039 | Fleet-to-Disposal | Acquire → register → assign → route/use → maintenance → incident → compliance → resale/disposal | Fleet/asset systems, telematics, workflow | Discovery |
| BP-040 | Partner-to-Revenue | Partner recruit → qualify → contract → enable → register deal → co-sell → attribute → commission → renew | PRM, CRM, partner portals | Discovery |
| BP-041 | Subscription-to-Renewal | Signup → entitlement → billing → usage → failed payment → recovery → upgrade/downgrade → renewal/cancel | Billing, entitlement, CRM/CS, payment automation | Discovery |
| BP-042 | Ecommerce Order-to-Fulfillment | Browse → cart → checkout → payment → fraud → inventory → fulfillment → delivery → return/refund | Commerce, payment, OMS/WMS, support | Discovery |
| BP-043 | Marketplace-to-Settlement | Seller onboarding → catalog → listing → order → fee → fulfillment → return/dispute → seller settlement → reconciliation | Marketplace platforms, payment/ledger systems | Discovery |
| BP-044 | Government-Tender-to-Contract | Opportunity → eligibility → bid/no-bid → compliance → proposal → approval → submission → award → contract | Tender intelligence, document agents, CLM | Discovery |
| BP-045 | Grant-to-Compliance | Opportunity → eligibility → application → budget → submission → award → milestones → evidence → reporting | Grant management, document/evidence workflows | Discovery |
| BP-046 | M&A-to-Integration | Target scan → screening → diligence → valuation → approval → close → Day-1 → systems/data/people integration → synergy tracking | Corp-dev, deal room, project/HR/IT workflows | Discovery |
| BP-047 | Fundraise-to-Close | Investor research → outreach → qualification → diligence → data room → term sheet → approvals → close → reporting | CRM, data room, document/approval workflows | Discovery |
| BP-048 | Innovation-to-Commercialization | Research → hypothesis → experiment → result → IP → business case → pilot → launch → scale/kill | Research/experiment systems, product/strategy workflows | Discovery |
| BP-049 | Crisis-to-Recovery | Signal → incident command → impact assessment → communications → decisions → continuity → recovery → verification → postmortem | BCP/DR, incident command, communication workflows | Discovery |
| BP-050 | Change-to-Adoption | Change request → impact → stakeholder map → approval → communication → training → rollout → adoption → benefits verification | Change management, LMS, project/HR systems | Discovery |
| BP-051 | Knowledge-to-Decision | Question → retrieve → verify → synthesize → decision brief → approval → action → outcome → knowledge update | RAG, research agents, BI, decision systems | Discovery |
| BP-052 | Strategy-to-Execution | Vision → objectives → OKRs/KPIs → initiatives → capacity/budget → execution → measurement → corrective action → benefits | Strategy/OKR, FP&A, project/portfolio, control tower | Discovery |
| BP-053 | Budget-to-Actuals | Plan → budget → allocation → spend → actuals → variance → forecast → reallocation → close | FP&A, ERP, BI, approval systems | Discovery |
| BP-054 | Portfolio-to-Benefits | Initiative intake → scoring → portfolio approval → funding → delivery → KPI/benefit tracking → reprioritize → close | PPM/OKR, BI, executive control tower | Discovery |
| BP-055 | Security-Event-to-Remediation | Detect → enrich → triage → severity → contain → investigate → remediate → verify → evidence → lessons | SIEM/SOAR, security agents, ITSM | Discovery |
| BP-056 | Privacy-Request-to-Closure | Request/identity verify → scope → locate → review → redact/export/delete → approval → response → evidence | Privacy/GRC, data discovery, document automation | Discovery |
| BP-057 | Legal-Matter-to-Closure | Intake → conflict/risk → assign → research → tasks → filings/contracts → spend → resolution → archive | Legal ops, matter management, knowledge | Discovery |
| BP-058 | Quality-Nonconformance-to-CAPA | Detect → contain → classify → RCA → CAPA → approve → implement → verify effectiveness → close | QMS, CAPA, workflow, analytics | Discovery |
| BP-059 | Sustainability-to-Disclosure | Activity data → emissions/impact calculation → validation → target tracking → evidence → disclosure/report → assurance | ESG systems, data pipelines, reporting | Discovery |
| BP-060 | Digital-Presence-to-Revenue | Domain/site → analytics → SEO/GEO → content → forms/chat → leads → CRM → attribution → optimization | CMS, SEO/GEO, analytics, CRM, automation | Discovery |

## 2. Process architecture contract

Every L4 process must be represented as:

**Trigger / Demand → Intake → Identity & Context → Qualification → Decision / Policy → Workflows → Cross-system transactions → Human approvals → Verification → Outcome → KPI → Exception → Audit evidence → Learning → Next cycle**

Required process objects:

| Object | Minimum fields |
|---|---|
| Process | ID, owner, purpose, trigger, scope, start/end, outcome |
| Value stream | stages, handoffs, customers, suppliers, dependencies |
| Activity | task/workflow link, role, system, input/output |
| Decision | rule/policy, authority, evidence, confidence |
| Handoff | source/target team/system, SLA, payload |
| KPI | definition, formula, target, source, owner |
| Exception | class, detection, retry/fallback, escalation |
| Control | risk, policy, control owner, evidence, test |
| Cost | resource, model/tool, transaction/run, budget |
| Evidence | source, timestamp, actor/agent, artifact, retention |
| Learning | outcome, root cause, lesson, knowledge update |

## 3. Process-to-L3 workflow mapping

| L4 process family | L3 workflow building blocks |
|---|---|
| Lead-to-Cash / Revenue | Lead-to-meeting, lead-to-opportunity, opportunity-to-proposal, quote-to-order, invoice-to-close, renewal/expansion |
| Marketing | Campaign-to-lead, content-to-distribution, report-to-decision |
| Customer | Customer onboarding, support-to-resolution, incident-to-resolution, meeting-to-execution, renewal/expansion |
| People | Hire-to-onboard, employee offboarding, employee-access lifecycle |
| Finance | Procure-to-pay, invoice-to-close, expense-to-reimbursement, payment exception |
| Data | Data-quality remediation, cross-system synchronization, research-to-knowledge |
| AI/Automation | AI-run-to-audit, automation-failure recovery, AI memory lifecycle, model/tool routing |
| Procurement/Supplier | Vendor lifecycle, procure-to-pay, cross-system synchronization |
| Governance/Risk | AI-run-to-audit, employee-access lifecycle, incident-to-resolution |

## 4. Reusable solution families to discover for every process

Do not search only for “AI agents”. For each process search all of these:

1. Open-source business systems and ERP modules.
2. Commercial SaaS and native workflow/automation.
3. n8n / Activepieces / Windmill / Kestra / Temporal templates.
4. AI agents and agent frameworks.
5. Skills and reusable prompts.
6. MCP/A2A servers and connectors.
7. APIs, webhooks and event buses.
8. RPA/browser/computer-use automation.
9. Forms, approval and policy engines.
10. Data/ETL/ELT and master-data systems.
11. BI, dashboards and report generators.
12. Document/OCR/e-signature systems.
13. Knowledge/RAG/memory systems.
14. Identity/RBAC/secrets and audit systems.
15. Observability/evaluation/testing.
16. Exception recovery, retries, DLQ, replay and compensation.
17. Backup/DR and lifecycle management.
18. Security/privacy/compliance controls.
19. SOPs, templates, playbooks, runbooks and training.
20. Industry-specific systems where generic ERP/workflow is insufficient.

## 5. High-value reusable backbone candidates

These are **reference candidates**, not automatic technology selections:

| Layer | Candidate families |
|---|---|
| ERP / business backbone | Odoo, ERPNext, ERPClaw, NocoBase |
| Workflow orchestration | n8n, Activepieces, Windmill, Kestra, Temporal |
| Forms / approvals | forms-flow-ai, django-forms-workflows, ProcessMaker |
| Integration | Composio, API/webhook patterns, Airbyte, Debezium |
| Agent orchestration | LangGraph, GAIA and comparable agent frameworks |
| Browser execution | Playwright MCP, Browser Use, Crawl4AI |
| Research | GPT Researcher, STORM, Perplexica, SearXNG |
| Documents | Rendoc MCP, ComPDFKit Generation, Typst, ContractSpark |
| BI / reporting | Metabase, Superset, OpenBI, Helical Insight |
| Governance | A2A Governance Gateway, Keycloak, OpenFGA, OPA |
| Observability / eval | Langfuse, Phoenix-class systems, Promptfoo |
| Memory / knowledge | Mem0, MemoryOS, Eidetic OS, Qdrant/Neo4j-class stores |
| Data | NocoBase/NocoDB/Directus, Airbyte, Debezium, data catalogs |
| Durable recovery | Temporal, Kestra, DLQ/replay/compensation patterns |

## 6. L4 qualification gates

**G0 Process identity → G1 Value-stream boundary → G2 Process decomposition → G3 Existing-solution discovery → G4 License/commercial terms → G5 Input/output/data contract → G6 Roles/RBAC/approvals → G7 Integrations/events → G8 KPI/SLA/SLO → G9 Exception/recovery → G10 Security/privacy/compliance → G11 Runtime/evidence → G12 Nivy fit → G13 Cost/TCO → G14 Operational ownership**

A process is not “qualified” because a workflow exists. The complete value stream, handoffs, controls and measurable outcome must be evidenced.

## 7. L4 coverage gaps still requiring deeper discovery

- Industry-specific processes: construction, accounting/tax, healthcare, education, real estate, manufacturing, logistics, hospitality and professional services.
- End-to-end statutory payroll/tax/treasury by jurisdiction.
- Manufacturing: plan-to-produce, procure-to-produce, quality-to-release, maintenance-to-availability.
- Construction/project delivery: bid-to-build, subcontract-to-payment, equipment-to-utilization, site-to-handover.
- Accounting practice: client-onboarding-to-close, tax-return lifecycle, audit lifecycle, advisory-to-billing.
- Software/SaaS: idea-to-release, usage-to-billing, incident-to-SLA, customer-success-to-expansion.
- Digital agency: brief-to-campaign, lead-to-delivery, project-to-invoice, retainer-to-renewal.
- Ecommerce: catalog-to-order, order-to-return, seller-to-settlement, fraud-to-resolution.
- International operations: entity setup, intercompany, FX, transfer pricing, cross-border tax/customs.
- Enterprise transformation: acquisition-to-integration, restructuring-to-stabilization, shared-services transition.
- Autonomous-company process control: process digital twin, simulation, capacity allocation, causal KPI, policy-constrained optimization.

## 8. Existing library relationship

This L4 catalog consolidates and extends the master value-stream checklist and the L3 Workflow Reuse Catalog. It does not replace lower-level catalogs.

- L0/L1: Atomic & Micro Automation Reuse Catalog
- L2: Task Automation Reuse Catalog
- L3: Workflow Reuse Catalog
- **L4: Business Process & Value-Stream Reuse Catalog**
- L5: Department Systems
- L6: Cross-Department
- L7: AI Managers
- L8: AI Executives
- L9: Control Tower
- L10: Autonomous Company

## 9. Completion rule

For every L4 process, eventually produce:

**Process map → workflow map → system map → reusable-solution map → data/event map → role/RBAC map → policy/control map → KPI/SLA map → exception/recovery map → evidence/audit map → cost/TCO map → runtime qualification → Nivy implementation adapter**

**Catalog status: L4 Business Process / Value-Stream Discovery started.**
