# Cross-Department System & End-to-End Integration Reuse Catalog — September 2026

**Library layer:** L6 — Cross-Department Systems  
**Sequence:** L5 Department Systems → **L6 Cross-Department** → L7 AI Managers → L8 AI Executives → L9 Control Tower → L10 Autonomous Company

## Purpose

L6 connects department systems into **end-to-end enterprise value streams**. The goal is not point-to-point integration alone; every cross-department flow must preserve identity, context, data contracts, policy, approvals, ownership, observability, auditability and reconciliation.

**Rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## 1. Cross-department system catalog

| ID | End-to-end cross-department system | Departments | Canonical flow | Reuse families | Status |
|---|---|---|---|---|---|
| XD-001 | Lead-to-Revenue | Marketing → Sales → Finance → Customer Success | Campaign → lead → opportunity → contract/order → invoice → collection → retention | CRM, marketing automation, ERP, CS | Discovery |
| XD-002 | Campaign-to-Cash | Marketing → Sales → Finance | Campaign → lead → deal → booking → billing → cash → attribution | Ad APIs, CRM, ERP, BI | Discovery |
| XD-003 | Quote-to-Cash | Sales → Legal → Finance → Operations | Quote → approval → contract → order → delivery → invoice → payment | CPQ, CLM, ERP, workflow | Discovery |
| XD-004 | Order-to-Delivery | Sales → Operations → Procurement → Logistics → Finance | Order → allocation → procure/produce → deliver → invoice | ERP, WMS/TMS, procurement | Discovery |
| XD-005 | Customer-Onboarding-to-Adoption | Sales → Legal → Finance → IT/Ops → Customer Success | Closed deal → contract → billing → provisioning → onboarding → adoption | CRM, CLM, ERP, ITSM, CS | Discovery |
| XD-006 | Customer-Issue-to-Product-Fix | Support → Engineering → Product → QA → Customer Success | Issue → triage → bug/requirement → fix → test → release → customer verification | ITSM, GitHub, product tools, CI/CD | Discovery |
| XD-007 | Incident-to-Executive-Decision | IT/Security → Operations → Department Head → Executive | Detection → severity → response → impact → decision → recovery → board/executive report | SIEM/SOAR, ITSM, control tower | Discovery |
| XD-008 | Hire-to-Ready-Employee | HR → Recruitment → IT → Facilities → Finance → Manager | Requisition → hire → identity → access/assets → payroll → workspace → manager handoff | ATS, HRIS, IAM, ITSM, ERP | Discovery |
| XD-009 | Employee-Change-to-Access | HR → IT/Security → Manager | HR change → role determination → access change → approval → verification → audit | HRIS, Keycloak, OpenFGA, OPA | Discovery |
| XD-010 | Employee-Offboarding-to-Closure | HR → IT/Security → Finance → Manager → Legal | Exit → revoke access → recover assets → payroll/final dues → legal records → evidence | HRIS, IAM, ITAM, ERP, records | Discovery |
| XD-011 | Procure-to-Pay Enterprise | Requesting Dept → Procurement → Legal → Finance → Receiving | Need → sourcing → contract → PO → receipt → invoice → payment → supplier performance | ERP, procurement, CLM, workflow | Discovery |
| XD-012 | Supplier-Onboarding-to-Performance | Procurement → Legal → Finance → Security → Operations | Supplier request → due diligence → contract → vendor master → payment → scorecard | SRM, GRC, CLM, ERP | Discovery |
| XD-013 | Contract-to-Operations | Sales/Procurement → Legal → Finance → Operations | Draft → risk → approval → signature → obligation → billing/delivery → renewal | CLM, ERP, workflow | Discovery |
| XD-014 | Contract-to-Compliance | Legal → Compliance → Operations → Audit | Contract → obligations → controls → evidence → review → renewal/remediation | CLM, GRC, evidence systems | Discovery |
| XD-015 | Revenue-to-Forecast | Sales → Finance → Operations → Executive | Pipeline → bookings → delivery/billing → actuals → forecast → variance → action | CRM, ERP, FP&A, BI | Discovery |
| XD-016 | Budget-to-Execution | Strategy → Finance → Department → PMO → Executive | Objective → budget → allocation → initiative → execution → benefits | OKR/PPM, ERP, BI | Discovery |
| XD-017 | Strategy-to-Company-KPI | Executive → Strategy → Departments → Analytics | Strategy → OKRs → departmental KPIs → runs → outcomes → executive review | OKR/BI/control tower | Discovery |
| XD-018 | Data-to-Executive-Decision | All departments → Data/Analytics → Executive | Source data → quality → semantic model → insight → decision → action → outcome | ETL/ELT, BI, knowledge, control tower | Discovery |
| XD-019 | Customer-Data-to-Marketing | CRM/CS → Data → Marketing → Sales | Customer signals → segmentation → audience → campaign → lead → attribution | CDP/CRM, ETL, ad APIs | Discovery |
| XD-020 | Support-Data-to-Product-Roadmap | Support → Knowledge/Data → Product → Executive | Tickets → clusters → root cause → opportunity → prioritization → roadmap | ITSM, analytics, product tools | Discovery |
| XD-021 | Finance-to-Management-Control | Finance → Analytics → Executive → Departments | Actuals → variance → diagnosis → recommendation → approval → corrective action | ERP, FP&A, BI, workflow | Discovery |
| XD-022 | Payroll-to-Finance-to-Compliance | HR → Payroll → Finance → Tax/Compliance | HR changes → payroll → accounting → statutory outputs → reconciliation → evidence | HRIS, payroll, ERP, tax | Discovery |
| XD-023 | Expense-to-Accounting | Employee → Manager → Finance → Accounting | Receipt → policy → approval → payment → journal → reconciliation | Expense/OCR, workflow, ERP | Discovery |
| XD-024 | Tax-Data-to-Filing | Finance → Tax → Accounting → Compliance | Transactions → calculation → reconciliation → filing → evidence → notices | ERP, tax engine, GRC | Discovery |
| XD-025 | Security-Event-to-Business-Response | Security → IT → Legal → HR → Executive | Alert → triage → containment → legal/privacy assessment → communication → recovery | SIEM/SOAR, GRC, incident command | Discovery |
| XD-026 | Privacy-Request-to-Data-Action | Customer/Employee → Privacy → Data → Legal → IT | Verify → locate → review → export/delete/redact → approval → response → evidence | privacy tools, data discovery, records | Discovery |
| XD-027 | Risk-to-Budget-Control | Risk → Strategy → Finance → Department | Risk → impact → treatment → budget → control → test → residual risk | GRC, FP&A, policy engines | Discovery |
| XD-028 | Compliance-to-Operational-Control | Compliance → Legal → Operations → IT/Security | Obligation → policy → control → implementation → evidence → test → remediation | GRC, OPA, workflow | Discovery |
| XD-029 | Knowledge-to-Execution | Knowledge/Research → Department → AI Workforce → Human | Research → verified knowledge → recommendation → approval → execution → outcome | RAG, research agents, workflow | Discovery |
| XD-030 | AI-Run-to-Enterprise-Audit | AI Platform → Department → Governance → Audit | Request → identity → policy/budget → model/tool → action → verification → evidence | A2A governance, OPA, Langfuse | Discovery |
| XD-031 | AI-Agent-to-Human-Workforce | AI Platform → Manager → Human → Department | Agent detection → task creation → delegation → human action → result → feedback | agent orchestration, task systems | Discovery |
| XD-032 | Automation-Failure-to-Manual-Fallback | Any Dept → Automation Platform → Human Owner | Failure → classify → retry → fallback → human escalation → recovery → replay | Temporal/Kestra, DLQ, approvals | Discovery |
| XD-033 | KPI-Anomaly-to-Corrective-Action | Data → Analytics → Department Head → Executive | Detect → diagnose → recommend → approve → act → verify | BI, causal analytics, control tower | Discovery |
| XD-034 | Capacity-to-Work-Allocation | Strategy → Finance/HR → Department → PMO/Operations | Demand → capacity → constraints → allocation → execution → utilization → replan | workforce planning, PPM, optimization | Discovery |
| XD-035 | Marketing-Budget-to-Allocation | Marketing → Finance → Sales → Analytics → Executive | Budget → channel plan → spend → leads/revenue → marginal performance → reallocation | ad APIs, attribution, BI, approvals | Discovery |
| XD-036 | Product-Idea-to-Revenue | Customer/Marketing/Sales → Product → Engineering → Marketing/Sales → Finance | Signal → idea → discovery → build → launch → acquisition → revenue → feedback | product/engineering, CRM, ERP | Discovery |
| XD-037 | Partner-to-Revenue-to-Commission | Partnerships → Sales → Finance → Customer Success | Partner → registration → deal → attribution → close → commission → renewal | PRM, CRM, ERP | Discovery |
| XD-038 | Procurement-to-Asset-to-Retirement | Procurement → Finance → IT/Operations → Asset Mgmt | Buy → capitalize/register → assign → maintain → return → dispose | ERP, ITAM, CMMS | Discovery |
| XD-039 | Project-to-Cash | Sales → PMO/Operations → Finance → Customer Success | SOW → plan → delivery → acceptance → invoice → collection → renewal | CRM, PPM, ERP, CS | Discovery |
| XD-040 | Project-to-Resource-Capacity | Sales → Finance → HR → PMO → Operations | Pipeline → demand → skill/capacity → staffing → utilization → forecast | CRM, HRIS, PPM, BI | Discovery |
| XD-041 | Change-to-Company-Adoption | Strategy/Executive → HR/L&D → IT → Departments | Change → impact → communications → training → rollout → adoption → benefits | change mgmt, LMS, ITSM, BI | Discovery |
| XD-042 | Crisis-to-Enterprise-Recovery | Executive → Operations → IT/Security → Legal/Comms → Finance | Crisis → command → impact → continuity → communications → recovery → financial/legal closure | BCP/DR, incident command | Discovery |
| XD-043 | M&A-to-Day-1 | Corp Dev → Legal → Finance → HR → IT → Operations | Diligence → approval → close → Day-1 → people/systems/data → controls | deal room, CLM, HR/IT, PPM | Discovery |
| XD-044 | M&A-to-Synergy | Corp Dev → Strategy → Finance → Departments | Target → baseline → synergy plan → initiatives → savings/revenue → verification | PPM, FP&A, BI | Discovery |
| XD-045 | Innovation-to-Commercialization | R&D → Product → Legal/IP → Finance → Marketing/Sales → Operations | Research → experiment → IP → business case → pilot → launch → scale | research, PPM, CLM, CRM | Discovery |
| XD-046 | Data-to-AI-Production | Data → AI/ML → Security/Governance → IT → Department | Data → quality → training/eval → approval → deployment → monitoring → retirement | data pipelines, eval, observability | Discovery |
| XD-047 | Model-Drift-to-Business-Action | AI Platform → Data → Department → Governance | Drift → impact → diagnose → retrain/reroute → approval → deploy → verify | eval/observability, workflow | Discovery |
| XD-048 | Knowledge-Change-to-Workforce | Research/Knowledge → HR/L&D → Department → AI Workforce | New knowledge → validate → curriculum/SOP → training → skill update → verification | KM, LMS, skill registry | Discovery |
| XD-049 | Audit-Finding-to-Remediation | Audit → Department → Risk/Compliance → Finance/IT | Finding → owner → remediation → evidence → retest → closure | GRC, workflow, evidence | Discovery |
| XD-050 | Policy-Change-to-System-Control | Legal/Compliance → Security/IT → Operations → AI Governance | Policy → impact → rule/control → implementation → test → evidence | OPA, IAM, workflow, config management | Discovery |
| XD-051 | Customer-Churn-to-Company-Response | CS → Support → Product → Marketing → Finance → Executive | Risk → root cause → save action → product/marketing/finance response → retention outcome | CS, analytics, CRM, product | Discovery |
| XD-052 | Renewal-to-Expansion | CS → Sales → Finance → Product | Health → renewal → expansion opportunity → quote → contract → billing | CRM/CS, CPQ, CLM, ERP | Discovery |
| XD-053 | Cash-Exception-to-Resolution | Finance → Sales/Customer → Bank → Accounting | Failed/mismatched payment → investigate → contact → retry/refund/adjust → reconcile | payments, ERP, workflow | Discovery |
| XD-054 | Inventory-Exception-to-Customer-Resolution | Inventory/Operations → Sales → Customer Success → Procurement | Stock exception → impact → allocation/reorder → customer communication → resolution | ERP/WMS, CRM, procurement | Discovery |
| XD-055 | Field-Service-to-Revenue | Customer Success → Operations → Field Service → Inventory → Finance | Request → schedule → dispatch → parts → service → proof → invoice → feedback | FSM, ERP, inventory | Discovery |
| XD-056 | Digital-Presence-to-Lead-to-Cash | Web/SEO/Social → Marketing → Sales → Finance → CS | Traffic → conversion → lead → deal → cash → retention | CMS, analytics, CRM, ERP | Discovery |
| XD-057 | Research-to-Strategy-to-Execution | Research → Strategy → Executive → Finance → Departments | Evidence → synthesis → strategic decision → budget → initiatives → KPI | research agents, PPM, BI | Discovery |
| XD-058 | Board-Decision-to-Execution | Board/Executive → Strategy → Finance → Departments → Analytics | Decision → owner → initiative → budget → execution → KPI → board feedback | board tools, PPM, ERP, BI | Discovery |
| XD-059 | Company-Wide Automation Registry | All departments → Automation Platform → Governance | Discover → qualify → register → deploy → observe → evaluate → retire | automation registry, n8n/Temporal, GitHub | Discovery |
| XD-060 | Enterprise Event-to-Action Fabric | All systems → Event Bus → Policy → AI/Human → Target System | Event → normalize → route → policy → action → verify → audit | webhooks, queues, event bus, workflow | Discovery |

## 2. Enterprise integration contracts

Every L6 flow must define:

**Source → Event/Request → Identity → Context → Data Contract → Policy → Routing → Target → SLA → Acknowledgement → Outcome → Reconciliation → Audit**

Required integration objects:

| Object | Required fields |
|---|---|
| Event | event_id, type, source, timestamp, tenant/entity, correlation_id |
| Request | requester, purpose, priority, deadline, authority |
| Data Contract | schema, owner, version, validation, compatibility |
| Integration | source, target, protocol, auth, retry, timeout |
| Policy Gate | rule, threshold, approver, evidence |
| Handoff | source owner, target owner, SLA, acknowledgement |
| Reconciliation | expected vs actual, mismatch, resolution |
| Audit Event | actor/agent, action, timestamp, evidence, policy |
| Exception | class, retry, fallback, escalation, replay |
| KPI | end-to-end outcome, latency, quality, cost, owner |

## 3. Integration patterns to discover/reuse

1. API-to-API.
2. Webhooks.
3. Event bus / queues.
4. Scheduled synchronization.
5. CDC / data replication.
6. ETL/ELT pipelines.
7. Shared canonical data model.
8. Master-data synchronization.
9. Workflow orchestration.
10. Durable execution.
11. MCP tool integration.
12. A2A agent integration.
13. Browser/computer-use fallback.
14. RPA for legacy systems.
15. File/SFTP integration.
16. Email/document integration.
17. Human approval handoff.
18. Compensation transactions.
19. DLQ/replay.
20. Audit/evidence propagation.

## 4. Enterprise backbone candidates

| Capability | Candidate families |
|---|---|
| ERP / system of record | Odoo, ERPNext, ERPClaw, NocoBase |
| Workflow | n8n, Activepieces, Windmill, Kestra, Temporal |
| Integration | Composio, APIs/webhooks, Airbyte, Debezium |
| Eventing | queues/event-bus patterns, webhooks, CDC |
| Identity | Keycloak |
| Authorization | OpenFGA, OPA |
| Agent governance | A2A Governance Gateway |
| Agent orchestration | LangGraph, GAIA-class systems |
| Browser | Playwright MCP, Browser Use, Crawl4AI |
| Data | NocoBase/NocoDB/Directus, Airbyte, Debezium |
| BI | Metabase, Superset, OpenBI, Helical Insight |
| Observability | Langfuse, Phoenix-class systems |
| Evaluation | Promptfoo and comparable eval frameworks |
| Memory/knowledge | Mem0, MemoryOS, Eidetic OS, Qdrant/Neo4j |
| Durable recovery | Temporal, Kestra, DLQ/replay/compensation |
| Documents | Rendoc MCP, Typst, ContractSpark, ComPDFKit Generation |

## 5. L6 qualification gates

**G0 Flow identity → G1 Source/target departments → G2 Value-stream boundary → G3 Event/data contract → G4 Existing integration discovery → G5 License/commercial review → G6 Identity/RBAC → G7 Policy/approval → G8 Reliability/retry/idempotency → G9 Reconciliation → G10 Security/privacy/compliance → G11 Observability/evidence → G12 KPI/SLA/SLO → G13 Cost/TCO → G14 Runtime test → G15 Nivy adapter**

A point-to-point connector is **not** a qualified cross-department system until the business outcome, ownership, controls, reconciliation and failure path are defined.

## 6. Critical Nivy integration layer gaps

These should be treated as shared platform capabilities rather than rebuilt independently in every department:

1. Universal Company Data Model.
2. Canonical entity IDs and master-data rules.
3. Universal Event Envelope.
4. Enterprise Event Bus / Queue abstraction.
5. Universal Connector Registry.
6. API/MCP/A2A adapter layer.
7. Identity + session + RBAC/ABAC.
8. Universal Policy/Approval Engine.
9. Universal Human Approval Inbox.
10. Universal Audit/Evidence Ledger.
11. Universal Exception/Recovery/DLQ service.
12. Cross-system reconciliation engine.
13. Universal KPI/Metric contract.
14. Cost/usage ledger.
15. Automation/Agent Registry.
16. Knowledge/Memory context propagation.
17. Cross-department notification/routing.
18. Integration health/dependency monitor.
19. Schema/version compatibility registry.
20. Digital Twin/event simulation layer.

## 7. Completion rule

For every L6 system eventually produce:

**End-to-end map → department map → process/workflow map → system map → data contract → event contract → identity/RBAC → policy/approval → integration adapters → retry/idempotency → reconciliation → security/privacy/compliance → KPI/SLA → observability/audit → cost/TCO → runtime evidence → Nivy adapter**

**Catalog status: L6 Cross-Department Discovery started.**
