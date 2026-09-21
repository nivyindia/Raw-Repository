# Workflow Reuse Catalog — September 2026

**Library layer:** L3 — Workflows  
**Sequence:** Atomic Action → Micro Task → Task Automation → **Workflow** → Process → Department → Cross-Department → AI Manager → Executive → Control Tower → Autonomous Company

## Purpose

This catalog maps complete multi-step business workflows to reusable open-source, template, agent and workflow-engine candidates.

**Rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## 1. Workflow catalog

| ID | Workflow | Canonical flow | Reusable candidates | Status |
|---|---|---|---|---|
| WF-001 | Lead-to-meeting | Capture → enrich → dedupe → qualify → outreach → reply → schedule → CRM | n8n templates; Mesh Pilot; Activepieces | Cataloged |
| WF-002 | Lead-to-opportunity | Lead → qualification → scoring → routing → meeting → opportunity → forecast | n8n CRM patterns; sales-agent systems | Cataloged |
| WF-003 | Opportunity-to-proposal | Opportunity → requirements → pricing → proposal → approval → send → follow-up | Axiom; ContractSpark; Typst; n8n | Cataloged |
| WF-004 | Quote-to-order | Quote → margin/policy check → approval → signature → order | workflow engines; CRM/ERP systems | Discovery |
| WF-005 | Campaign-to-lead | Brief → audience → creative → campaign → lead capture → CRM → attribution | n8n templates; advertising APIs; campaign agents | Cataloged |
| WF-006 | Content-to-distribution | Research → brief → create → QA → approval → publish → syndicate → measure → repurpose | n8n templates; content-agent patterns | Cataloged |
| WF-007 | Customer onboarding | Won deal → provisioning → kickoff → tasks → training → health baseline → handoff | n8n/CRM/CS workflow patterns | Cataloged |
| WF-008 | Support-to-resolution | Ticket → classify → enrich → assign → SLA → diagnose → respond → resolve → knowledge | OpenWind; Tessio; GeneralBots; ITSM workflows | Cataloged |
| WF-009 | Incident-to-resolution | Alert → dedupe → enrich → severity → owner → mitigate → resolve → verify → RCA | IncidentRelay; SRE agent patterns; Temporal | Cataloged |
| WF-010 | Hire-to-onboard | Requisition → candidate → interview → offer → acceptance → accounts/assets → onboarding | N8N-Workflows; HR workflow templates | Cataloged |
| WF-011 | Employee offboarding | Exit → approvals → access revoke → asset recovery → handover → payroll/records → audit | HR/IT workflow patterns; Keycloak/OpenFGA/OPA | Cataloged |
| WF-012 | Procure-to-pay | Need → supplier → RFQ → quote → comparison → approval → PO → receipt → invoice → payment | ProcessMaker templates; ERP/procurement workflows | Cataloged |
| WF-013 | Invoice-to-close | Invoice → validation → approval → posting → payment → reconciliation → close | ERP/accounting workflow patterns | Cataloged |
| WF-014 | Expense-to-reimbursement | Receipt → OCR → policy → duplicate → approval → reimbursement → accounting | ProcessMaker expense templates; ERP workflows | Cataloged |
| WF-015 | Contract-to-renewal | Draft → review → risk → approval → signature → obligations → expiry → renewal | ContractSpark; legal-ops/workflow templates | Cataloged |
| WF-016 | Research-to-knowledge | Question → search → evidence → dedupe → contradiction/freshness → synthesize → knowledge → review | GPT Researcher; STORM; Perplexica; SearXNG | Cataloged |
| WF-017 | Form-to-approved-record | Form → validation → enrichment → approval → create record → notify → audit | forms-flow-ai; django-forms-workflows; Activepieces | Cataloged |
| WF-018 | Data-quality remediation | Detect → profile → normalize → dedupe → reconcile → exception → approve → update | n8n; Airbyte; NocoBase/NocoDB/Directus | Cataloged |
| WF-019 | Cross-system synchronization | Event → map → authorize → transform → write → verify → retry → audit | n8n; Activepieces; Windmill; Composio | Cataloged |
| WF-020 | Meeting-to-execution | Meeting → transcript → decisions → tasks → owners → deadlines → project/CRM → reminders | GAIA; assistant patterns; workflow templates | Discovery |
| WF-021 | Report-to-decision | Collect → calculate → report → distribute → anomaly → explanation → recommendation → approval/action | OpenBI; Helical Insight; report agents | Cataloged |
| WF-022 | AI-run-to-audit | Request → policy → budget → model/tool → execution → validation → trace → evidence → audit | A2A Governance Gateway; GAIA; Langfuse; Promptfoo | Cataloged |
| WF-023 | Automation-failure recovery | Detect → classify → retry → fallback → DLQ → human escalation → replay/compensate → verify | Temporal; Kestra; durable workflow engines | Cataloged |
| WF-024 | Employee-access lifecycle | Join/change/exit → identity → RBAC → assets → access review → revoke → audit | Keycloak; OpenFGA; OPA; HR↔IT patterns | Discovery |
| WF-025 | Payment exception | Payment → status → retry/dunning → failure → dispute/refund → reconciliation → ledger | payment APIs + ERP/workflow patterns | Discovery |
| WF-026 | Backup-and-restore assurance | Schedule → snapshot → integrity → restore test → evidence → alert → remediation | backup/DR platforms + workflow engines | Discovery |
| WF-027 | AI memory lifecycle | Interaction → classify → scope → provenance → write/update → conflict/stale check → retrieval → retirement | MemoryOS; Mem0; Eidetic OS; Constitutional Memory | Cataloged |
| WF-028 | AI model/tool routing | Request → risk/context → model/tool selection → authorization → execution → quality/cost check → fallback | LiteLLM; policy engines; agent frameworks | Cataloged |
| WF-029 | Vendor lifecycle | Request → onboarding → verification → risk → approval → contract → PO → performance → renewal | procurement workflow systems; ProcessMaker templates | Discovery |
| WF-030 | Customer renewal/expansion | Health → usage → risk → renewal trigger → outreach → proposal → approval → renewal/upsell → CRM | CRM/CS workflows; sales agents | Cataloged |

## 2. Workflow coverage against the master

| Master value stream | Primary workflows |
|---|---|
| Lead-to-Cash | WF-001 → WF-004 → WF-013 |
| Quote-to-Order | WF-003, WF-004 |
| Order-to-Cash | WF-004, WF-013 |
| Procure-to-Pay | WF-012 |
| Hire-to-Retire | WF-010, WF-011, WF-024 |
| Idea-to-Product | WF-006 plus product/engineering workflow candidates |
| Incident-to-Resolution | WF-009, WF-023 |
| Request-to-Fulfillment | WF-017, WF-019 |
| Record-to-Report | WF-013, WF-021 |
| Contract-to-Renewal | WF-015 |
| Source-to-Contract | WF-029 |
| Customer-Issue-to-Knowledge | WF-008, WF-016 |
| Campaign-to-Revenue | WF-005, WF-001 |
| Content-to-Distribution | WF-006 |
| Employee-Access Lifecycle | WF-010, WF-011, WF-024 |
| Data-to-Decision | WF-018, WF-021 |
| Model/Agent-to-Production | WF-022, WF-028 |
| Policy-to-Control | WF-022, WF-024 |
| Risk-to-Treatment | WF-009, WF-015, WF-029 |
| Problem-to-Prevention | WF-009, WF-023 |
| Asset-to-Disposal | WF-011, WF-026 |
| Supplier-to-Performance | WF-012, WF-029 |
| Revenue-to-Forecast | WF-002, WF-030 |
| Cash-to-Treasury | WF-013, WF-025 |

## 3. Workflow resource families to reuse

| Category | Reusable resource families |
|---|---|
| General workflow orchestration | n8n, Activepieces, Windmill, Kestra, Temporal |
| Business workflow / approvals | forms-flow-ai, django-forms-workflows, ProcessMaker templates |
| Durable execution | Temporal, Kestra |
| Browser execution | Playwright MCP, Browser Use, Crawl4AI |
| AI-agent workflow | LangGraph, GAIA, agent frameworks |
| Integrations | Composio, n8n, Activepieces, API/webhook patterns |
| Research | GPT Researcher, STORM, Perplexica, SearXNG |
| Documents | Rendoc MCP, ComPDFKit Generation, Typst templates, ContractSpark |
| Reporting | OpenBI, Helical Insight, report-agent patterns |
| Observability | Langfuse, Phoenix-class systems, agent monitoring |
| Governance | A2A Governance Gateway, Keycloak, OpenFGA, OPA |
| Memory | MemoryOS, Mem0, Eidetic OS |
| ERP/business backbone | Odoo, ERPNext, ERPClaw, NocoBase |

## 4. Workflow qualification

Each workflow candidate must pass:

**G0 Identity → G1 Source/License → G2 Workflow Match → G3 Inputs/Outputs Contract → G4 Integrations → G5 Security/Permissions → G6 Runtime Test → G7 Failure/Recovery → G8 Cost → G9 Nivy Fit → G10 Evidence**

A workflow being listed here means **candidate reuse**, not production approval.

## 5. Remaining L3 gaps

Continue discovery for:

- full Idea-to-Product lifecycle
- manufacturing/delivery
- logistics and field service
- tax/payroll/treasury
- government procurement and grants
- partner/channel/affiliate operations
- ecommerce/marketplace/subscription
- PR/media/community/academy
- compliance/risk/BCP/crisis
- M&A/corporate development
- pricing/revenue management
- facilities/fleet/sustainability
- enterprise data governance
- AI evaluation/model lifecycle
- enterprise scenario/capacity planning

## 6. Next layer

**L3 Workflows → L4 Business Processes / Value Streams**

L0/L1/L2 unresolved gaps continue in parallel.

**Catalog status: L3 Workflow Discovery started.**
