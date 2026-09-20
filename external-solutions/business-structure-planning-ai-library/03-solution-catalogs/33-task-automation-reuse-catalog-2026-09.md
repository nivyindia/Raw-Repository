# Task Automation Reuse Catalog — September 2026

**Library layer:** L2 — Task Automations  
**Master path:** Atomic Action → Micro Task → **Task Automation** → Workflow → Process → Department → Cross-Department → AI Manager → Executive → Control Tower → Autonomous Company

## Purpose

This catalog turns the L0 atomic actions and L1 micro tasks in [Catalog 32](./32-atomic-micro-automation-reuse-catalog-2026-09.md) into reusable **task-level automations**.

A task automation is larger than one atomic action or micro task but smaller than a complete business workflow.

**Governing rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## Qualification status

Status is intentionally conservative:

- **Discovery** = reusable candidates identified.
- **Cataloged** = candidate and capability are recorded.
- **Qualified** = technical/business fit has been verified.
- **Implemented** = integrated into Nivy.
- **Verified** = runtime/evidence verification passed.

Nothing in this catalog is automatically approved for production use.

---

## 1. Task automation catalog

| ID | Task automation | Inputs → actions → output | Reusable candidates | Status |
|---|---|---|---|---|
| TA-001 | Email triage task | Inbox → classify/priority → summarize → draft/reply/route → task record | gmail-agent; email_assistant; Jarvis; orderly | Cataloged |
| TA-002 | Email-to-task task | Email/thread → extract commitment/deadline → create task → assign/remind → audit | GAIA; rb81 assistant; n8n patterns | Cataloged |
| TA-003 | Calendar coordination task | Request → availability/timezone check → propose → confirm → calendar event → reminders | livia; email_assistant; NOVA; n8n | Cataloged |
| TA-004 | Meeting follow-through task | Event/transcript → decisions/actions → owners/deadlines → CRM/project update → follow-up | GAIA; meeting-agent patterns; n8n workflows | Discovery |
| TA-005 | Form intake task | Form → validate/enrich → policy/approval → create record → notify → evidence | forms-flow-ai; django-forms-workflows; Activepieces | Cataloged |
| TA-006 | Approval task | Request → policy check → approver selection → reminder/escalation → decision → audit | mcp-approval; Deliberate; forms-flow-ai | Cataloged |
| TA-007 | Notification/escalation task | Event → classify severity → route → notify → acknowledgement → escalate → close | IncidentRelay; OpenWind; workflow engines | Cataloged |
| TA-008 | Document generation task | Structured data → template → render → validate → approval → PDF/document → archive | Rendoc MCP; Typst business templates; ComPDFKit Generation; ContractSpark | Cataloged |
| TA-009 | Report distribution task | Sources → calculate/format → report → approval → scheduled delivery → archive | OpenBI; Helical Insight; GenAIReportAgent | Cataloged |
| TA-010 | Data normalization task | Records → validate → normalize → dedupe → golden record/update → exception queue | n8n Portfolio patterns; Airbyte; NocoBase/NocoDB/Directus | Cataloged |
| TA-011 | Cross-system sync task | Source event → map fields → authorization → write target → verify → retry/audit | n8n; Activepieces; Windmill; Composio | Cataloged |
| TA-012 | Lead capture/enrichment task | Lead source → extract → enrich → dedupe → CRM → owner assignment → notification | Mesh Pilot AI Sales Agent; n8n; sales workflow templates | Cataloged |
| TA-013 | Sales outreach task | Qualified lead → personalize → approval → send → detect reply/bounce/unsubscribe → update CRM | Mesh Pilot AI Sales Agent; gmail-agent; n8n | Cataloged |
| TA-014 | Proposal/quote task | CRM opportunity → collect data → generate proposal/quote → approval → send → status tracking | Axiom; ContractSpark; Typst templates; n8n | Cataloged |
| TA-015 | Employee onboarding task | Hire event → accounts/assets/tasks/docs → approvals → checklist → evidence → completion | N8N-Workflows onboarding/offboarding patterns; HR/IT workflow engines | Cataloged |
| TA-016 | Employee offboarding task | Exit event → approvals → revoke access → recover assets → handover → evidence → close | N8N-Workflows; Keycloak/OpenFGA/OPA patterns; HR↔IT automation | Cataloged |
| TA-017 | Vendor onboarding task | Vendor request → collect documents → verify → risk/approval → create vendor → notify | ProcessMaker templates; procurement workflow engines | Cataloged |
| TA-018 | Invoice approval task | Invoice → extract/validate → duplicate/3-way check → approval → ERP posting → audit | ProcessMaker templates; ERP/workflow systems; OCR pipelines | Cataloged |
| TA-019 | Expense reimbursement task | Receipt → OCR → policy validation → duplicate check → approval → reimbursement → accounting | ProcessMaker Expense Approval; ERP/expense workflows | Cataloged |
| TA-020 | Support ticket triage task | Ticket → classify → enrich → assign → SLA timer → response/escalation → resolution → knowledge update | OpenWind; Tessio; GeneralBots; ITSM workflows | Cataloged |
| TA-021 | Incident response task | Alert → dedupe/group → enrich → severity → route → remediation → verify → incident record | IncidentRelay; SRE agent/control-plane patterns | Cataloged |
| TA-022 | Research-to-evidence task | Question → multi-source search → dedupe/freshness → extract evidence → citation/evidence record → knowledge update | GPT Researcher; STORM; Perplexica; SearXNG; evidence-ledger patterns | Cataloged |
| TA-023 | Browser execution task | Intent → browser navigation → extraction/action → evidence capture → validation → result | Playwright MCP; Browser Use; Crawl4AI | Cataloged |
| TA-024 | AI run governance task | Agent request → model/tool policy → authorization/budget → execute → trace/cost → validate → audit | A2A Governance Gateway; GAIA; Langfuse; Promptfoo | Cataloged |
| TA-025 | Durable exception-recovery task | Failure → classify → retry/fallback → dead-letter/human handoff → replay/compensate → verify | Temporal; Kestra; workflow-engine patterns | Cataloged |
| TA-026 | Backup verification task | Schedule → snapshot → integrity check → restore test → evidence → alert on failure | Backup/DR workflow patterns; scheduled automation engines | Discovery |
| TA-027 | AI memory update task | Interaction/result → classify memory → provenance/scope → write/update/conflict check → retrieval index | MemoryOS; Mem0; Eidetic OS; Constitutional Memory | Cataloged |
| TA-028 | Cost/usage control task | Run → meter tokens/API/runtime → allocate → budget check → alert/cap → ledger | Langfuse; observability/FinOps patterns | Cataloged |
| TA-029 | Asset lifecycle task | Asset event → register/assign → maintenance/reminder → return/disposal → evidence | OpenWind; ERP/ITSM/asset workflows | Discovery |
| TA-030 | Contract renewal task | Contract → expiry/obligation scan → owner reminder → approval → renewal/termination → archive | Contract/workflow templates; legal-ops patterns | Discovery |

---

## 2. Task automation coverage by master layer

| Master requirement | Covered by |
|---|---|
| Email | TA-001, TA-002 |
| Calendar | TA-003 |
| Chat/meeting | TA-004, TA-020 |
| Forms/approvals | TA-005, TA-006 |
| Notifications | TA-007 |
| Documents/reports | TA-008, TA-009 |
| Data quality | TA-010 |
| Integrations/sync | TA-011 |
| Sales | TA-012, TA-013, TA-014 |
| HR | TA-015, TA-016 |
| Procurement | TA-017 |
| Finance | TA-018, TA-019 |
| Support/ITSM | TA-020 |
| Security/incident | TA-021 |
| Research/knowledge | TA-022, TA-027 |
| Browser/web | TA-023 |
| AI governance | TA-024 |
| Recovery | TA-025 |
| Backup/DR | TA-026 |
| AI memory | TA-027 |
| Cost/FinOps | TA-028 |
| Assets | TA-029 |
| Legal/contracts | TA-030 |

---

## 3. Newly discovered reusable sources

These are **candidate sources**, not production approvals.

| Source | Useful task layer | Link |
|---|---|---|
| TropaTT | CRM + tasks + projects + workflows + AI workflows | https://github.com/Anton-Barinov/TropaTT |
| Activepieces | General task/workflow automation, approvals, retries, integrations, MCP | https://github.com/activepieces/activepieces |
| n8n automation templates 5000+ | Ready-made business task/workflow patterns | https://github.com/sander2610/n8n-automation-templates-500 |
| N8N-Workflows | Concrete onboarding, offboarding, sales, document and admin tasks | https://github.com/Utsav-Donda/N8N-Workflows |
| ProcessMaker process templates | Finance, procurement and vendor task templates | https://github.com/ProcessMaker/process-templates |
| OpenWind | Workflow-native business tasks across helpdesk, HR, expenses, projects, invoicing and procurement | https://github.com/TinyPhi/OpenWind |
| TPT Free ERP | Finance, HR, CRM, procurement, projects, quality, assets and field-service task foundation | https://github.com/tpt-solutions/tpt-free-erp |
| Sentinel ERP | Cross-department workflow and AI-assisted business task foundation | https://github.com/jeevansai-hub/Sentinal-ERP |
| Mesh Pilot AI Sales Agent | Lead discovery, enrichment, outreach, approval and learning | https://github.com/Meshpilot-AGI/ai-sales-agent |

---

## 4. Reuse mapping rule

For every TA item, Nivy should prefer:

1. Existing complete task/workflow.
2. Existing open-source component that covers most of the task.
3. Existing skill/prompt/template.
4. Existing connector/API/MCP capability.
5. Adapter around an existing system.
6. Only then custom Nivy implementation.

Do not duplicate a full platform merely to obtain one task capability.

---

## 5. Qualification gates

Every candidate must eventually pass:

**G0 Identity → G1 Source/License → G2 Capability Match → G3 Integration Contract → G4 Security/Permissions → G5 Runtime Test → G6 Reliability/Error Handling → G7 Cost → G8 Nivy Fit → G9 Evidence**

Only **G9 Evidence** can move a candidate to **Verified**.

---

## 6. Remaining L2 discovery gaps

The first L2 batch is intentionally not exhaustive. Continue discovery for:

- advanced inbox security and mailbox administration
- desktop/OS automation and human-CAPTCHA handoff
- document redaction, PII and records retention
- master-data/golden-record management
- identity JML and privileged-access review
- privacy/DSAR automation
- payment/chargeback/settlement automation
- travel and resource scheduling
- localization/accessibility QA
- consent/preference synchronization
- AI safety/tool authorization/output validation
- synthetic/regression/load testing
- idempotency/compensating transactions
- tax/payroll automation
- treasury and cash operations
- enterprise risk/compliance evidence
- channel/partner/affiliate operations
- subscription and marketplace operations

## 7. Next build order

After this L2 batch:

**L2 Task Automations → L3 Workflows → L4 Value Streams → L5 Department Systems → L6 Cross-Department → L7 AI Managers → L8 AI Executives → L9 Control Tower → L10 Autonomous Company**

L0/L1 unresolved gaps continue in parallel.

**Catalog status: L2 Task Automation Discovery started.**
