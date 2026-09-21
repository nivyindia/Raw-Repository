# Atomic & Micro Automation Reuse Catalog — September 2026

## Purpose

This catalog starts implementation of the canonical **MASTER BUSINESS AUTOMATION LIST** at the bottom of the hierarchy:

**ATOMIC ACTION → MICRO TASK → TASK AUTOMATION**

It maps reusable platforms, skills, workflow templates and implementation references to the master coverage instead of building these primitives from scratch.

**Governing rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING

**Qualification rule:** A resource is **Cataloged** here only as a reusable candidate. It becomes **Qualified** only after license, dependencies, runtime, security, integration and business-fit evidence is checked.

---

## 1. Atomic action families

| ID | Atomic capability | Reuse candidates / references | Current status |
|---|---|---|---|
| AT-001 | Read/search web | Playwright MCP, Browser Use, Crawl4AI, SearXNG | Cataloged |
| AT-002 | Browser navigate/click/fill/download | Playwright MCP, Browser Use, n8n browser patterns | Cataloged |
| AT-003 | Call API / webhook | n8n, Activepieces, Windmill, Composio, Pipedream | Cataloged |
| AT-004 | Run script/function | Windmill, n8n Code, Temporal, Trigger.dev | Cataloged |
| AT-005 | Schedule job | n8n, Kestra, Temporal, Trigger.dev, Airflow | Cataloged |
| AT-006 | Queue/event | Kestra, Temporal, Node-RED, Kafka-class event infrastructure | Discovery |
| AT-007 | Read/write database | NocoBase, NocoDB, Directus, n8n, Airbyte | Cataloged |
| AT-008 | Transform/normalize data | n8n, Airbyte, dbt-class transformation, Windmill | Discovery |
| AT-009 | Extract text/OCR | OCR/document AI ecosystems; Rendoc MCP and document pipelines | Discovery |
| AT-010 | Generate document/PDF | Rendoc MCP, ComPDFKit Generation, Typst business templates | Cataloged |
| AT-011 | Send notification | n8n, workflow engines, channel connectors | Cataloged |
| AT-012 | Send email/message | n8n, Gmail/Calendar assistant patterns, channel connectors | Cataloged |
| AT-013 | Create task/record | n8n, CRM/ERP connectors, forms-flow-ai | Cataloged |
| AT-014 | Request approval | mcp-approval, Deliberate, forms-flow-ai | Cataloged |
| AT-015 | Authenticate/authorize | Keycloak/OpenFGA/OPA references already in architecture catalog | Discovery |
| AT-016 | Store/retrieve memory | MemoryOS, Mem0, AnythingLLM, Eidetic OS | Cataloged |
| AT-017 | Log/audit action | GAIA, A2A Governance Gateway, Langfuse/observability stack | Cataloged |
| AT-018 | Measure run/cost/latency | Langfuse, Phoenix-class observability, agent monitoring systems | Cataloged |
| AT-019 | Validate output | Promptfoo/evaluation stack, typed agent frameworks | Cataloged |
| AT-020 | Retry/fallback/replay | Temporal, Kestra, workflow engines, durable workflow patterns | Cataloged |
| AT-021 | Human handoff | Approval inboxes, Deliberate, Sphynx workflow patterns | Cataloged |
| AT-022 | Version/archive | Git/GitHub, workflow versioning, document repositories | Cataloged |
| AT-023 | Deduplicate records | CRM/data-quality workflow patterns in Catalog 31 | Discovery |
| AT-024 | Enrich record | Sales/lead enrichment agents, browser/API workflows | Cataloged |
| AT-025 | Classify content/record | LLM classification + rules/workflow templates | Cataloged |

---

## 2. Micro automation coverage

| ID | Master micro capability | Reusable implementation families | Status |
|---|---|---|---|
| MI-001 | Email classify/summarize/reply | gmail-agent, email_assistant, Jarvis, orderly | Cataloged |
| MI-002 | Email attachment extraction/routing | Gmail assistants + document/OCR pipelines | Discovery |
| MI-003 | Email follow-up/bounce/unsubscribe | gmail-agent, orderly, sales outreach patterns | Cataloged |
| MI-004 | Calendar scheduling/reschedule | email_assistant, livia, NOVA, n8n | Cataloged |
| MI-005 | Calendar reminders/prep/follow-up | gaia, rb81 assistant, calendar-agent patterns | Cataloged |
| MI-006 | Chat/message classify/respond/route | GeneralBots, NovaBot, channel workflow platforms | Cataloged |
| MI-007 | Voice transcription/intent/CRM update | NovaBot, ORBIT, voice-agent ecosystems | Cataloged |
| MI-008 | Document rename/classify/metadata | document AI + workflow engines | Discovery |
| MI-009 | OCR/extraction/validation | Rendoc/document-generation ecosystem + OCR tools | Discovery |
| MI-010 | File duplicate/version/archive/permissions | NocoBase/NocoDB/Directus + storage automation | Discovery |
| MI-011 | Form validation/enrichment/approval | forms-flow-ai, django-forms-workflows | Cataloged |
| MI-012 | Notification routing/escalation | IncidentRelay, workflow engines, notification connectors | Cataloged |
| MI-013 | Data entry/cross-system copy | n8n, Activepieces, Windmill, Composio | Cataloged |
| MI-014 | Data cleaning/normalize/deduplicate | n8n Portfolio patterns, data integration tools | Cataloged |
| MI-015 | Contact creation/enrichment/dedup | sales agents, CRM workflows, enrichment APIs | Cataloged |
| MI-016 | Task extraction/prioritization/deadline | gaia, email assistants, project workflow templates | Cataloged |
| MI-017 | Approval request/reminder/escalation/audit | mcp-approval, Deliberate, forms-flow-ai | Cataloged |
| MI-018 | Report generation/distribution | OpenBI, Helical Insight, report agents | Cataloged |
| MI-019 | Meeting transcript → decisions/tasks | meeting agents, assistant patterns, CRM workflows | Discovery |
| MI-020 | Search → evidence → answer | GPT Researcher, STORM, Perplexica, SearXNG | Cataloged |
| MI-021 | Knowledge capture/update/retirement | AnythingLLM, MemoryOS, Eidetic OS, RAG systems | Cataloged |
| MI-022 | Translation/terminology QA | LLM translation workflows + localization pipelines | Discovery |
| MI-023 | Template-driven proposal/invoice/report | Typst templates, ContractSpark, Axiom, Rendoc | Cataloged |
| MI-024 | Recurring scheduled automation | n8n, Kestra, Temporal, Trigger.dev | Cataloged |
| MI-025 | Identity provisioning/revocation | Keycloak/OpenFGA/OPA + HR↔IT workflow patterns | Discovery |
| MI-026 | Secret lifecycle | secret managers + policy/rotation workflows | Discovery |
| MI-027 | Browser evidence capture | Playwright MCP, Browser Use, Crawl4AI | Cataloged |
| MI-028 | Media transform/caption/transcribe/publish | media agents + workflow engines | Discovery |
| MI-029 | Localization/timezone/currency | workflow + application localization layers | Discovery |
| MI-030 | Accessibility QA/remediation | accessibility testing/tooling + CI workflows | Discovery |
| MI-031 | Backup/restore verification | backup platforms + scheduled workflow/test patterns | Discovery |
| MI-032 | Cost meter/budget/alert/cap | Langfuse/observability + FinOps workflows | Discovery |
| MI-033 | Consent/opt-out synchronization | CRM/marketing automation + policy workflows | Discovery |
| MI-034 | Payment status/retry/refund/reconciliation | payment APIs + workflow/ERP integrations | Discovery |
| MI-035 | Expense receipt → approval → reimbursement | OCR + expense/ERP workflow patterns | Discovery |
| MI-036 | Asset assignment/return/maintenance | ERP/ITSM/asset workflows | Discovery |
| MI-037 | Research source dedup/freshness/contradiction | research agents + source/evidence ledgers | Discovery |
| MI-038 | AI model/tool routing | LiteLLM + agent frameworks + policy gates | Cataloged |
| MI-039 | AI memory scope/provenance/conflict | MemoryOS, Constitutional Memory, Eidetic OS | Cataloged |
| MI-040 | Prompt-injection/tool authorization/output validation | agent governance + evaluation/security layers | Discovery |
| MI-041 | Trace/replay/token/cost attribution | Langfuse + agent observability stack | Cataloged |
| MI-042 | Synthetic/regression/load testing | Promptfoo + workflow/agent test harnesses | Cataloged |
| MI-043 | Retry/circuit-breaker/dead-letter/replay | Temporal/Kestra/durable workflow patterns | Cataloged |
| MI-044 | Idempotency/compensating action | Temporal/workflow transaction patterns | Discovery |

---

## 3. Ready-made workflow/resource sources to reuse

| Source | Reuse scope | Status |
|---|---|---|
| n8n Templates | CRM, email, calendar, sales, marketing, support, data and AI workflows | Cataloged |
| awesome-n8n-templates | Large third-party workflow collection | Cataloged |
| AOT forms-flow-ai | Forms + workflow + analytics + notifications | Cataloged |
| django-forms-workflows | Multi-stage forms, validation and approvals | Cataloged |
| mcp-approval | Multi-stage approval, quorum, delegation, escalation, SLA, audit | Cataloged |
| Deliberate | LangGraph approval, notifications, timeouts, escalation, policy routing, audit | Cataloged |
| IncidentRelay | Alert routing, deduplication, grouping, escalation, notification and replay | Cataloged |
| Sphynx | Durable workflows, human task inbox, SLA, delegation, escalation and connectors | Cataloged |
| Tessio | AI ITSM, email-to-ticket, workflow, SLA, dashboard/report patterns | Cataloged |
| OpenBI | Data sources, AI agents, dashboards, PDF/PPTX and scheduled reports | Cataloged |
| Helical Insight | Dashboards, reports and scheduled distribution | Cataloged |
| GeneralBots | Self-hosted multi-agent workspace with CRM, mail, drive, calendar, RAG and channels | Cataloged |
| Trinyx | Agents, workflows, forms, dashboards, approvals, tables and integrations | Cataloged |

---

## 4. First implementation backlog

These are the first reusable building blocks to qualify before building custom equivalents:

1. Email triage + approval + calendar assistant
2. Form → validation → approval → notification → audit
3. Notification router + escalation
4. Document generation service
5. Report generation + scheduled distribution
6. Data normalization + deduplication workflow
7. Cross-system record synchronization
8. Research → evidence → knowledge capture
9. Human approval service
10. Durable retry/replay/exception service
11. Agent memory + provenance
12. Agent observability + cost ledger
13. Browser automation + evidence capture
14. Identity/permission lifecycle automation
15. Backup/restore verification

---

## 5. Qualification gates

Each candidate must pass:

**G0 Identity → G1 Source/License → G2 Capability Match → G3 Integration Contract → G4 Security/Permissions → G5 Runtime Test → G6 Reliability/Error Handling → G7 Cost → G8 Nivy Fit → G9 Evidence**

Only G9 makes the candidate **Verified**.

---

## 6. Relation to master progress tracker

This catalog advances the master list in two layers:

- **L0 Atomic actions:** Discovery started; reusable candidates are now mapped.
- **L1 Micro tasks:** Discovery started; 44 concrete micro capabilities are mapped.
- **L2+** remain pending until the corresponding workflow/process/department layer is systematically cataloged.

Next batch should continue from **L2 Task Automations → L3 Workflows**, while unresolved L0/L1 discovery gaps continue in parallel.

