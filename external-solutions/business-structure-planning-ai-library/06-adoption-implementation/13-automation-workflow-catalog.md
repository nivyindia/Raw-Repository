# Automation Workflow Catalog

**Research date:** 2026-09-16

| Workflow source | Scope | Access | Reuse value | Link |
|---|---|---|---|---|
| n8n Workflow Library — CRM | CRM, sales, marketing, support, AI | Many free | Large searchable collection of importable workflow patterns | https://n8n.io/workflows/categories/crm/ |
| n8n AI SDR Sales Pipeline | Lead-to-meeting | Free | CRM ingestion, personalized follow-up, calendar booking detection, no-show follow-up | https://n8n.io/workflows/13529-run-an-ai-sdr-sales-pipeline-with-openai-google-sheets-gmail-and-calendar/ |
| n8n Multi-platform AI Sales Agent | Omni-channel sales | Paid template | RAG + modular CRM/calendar agents + WhatsApp/Instagram/Facebook/Telegram/web | https://n8n.io/workflows/4508-multi-platform-ai-sales-agent-with-rag-crm-logging-and-appointment-booking/ |
| TaskifyLabs n8n templates | Lead gen, CRM sync, marketing, AI | Free | Importable patterns for lead enrichment, data sync, content repurposing and AI triage | https://www.taskifylabs.com/n8n-templates |
| Runlane Runbooks | SOP-to-agentic workflow | Commercial/free trial | Converts repeatable SOPs into runbooks with review and audit controls | https://runlane.app/ |

## Automation search pattern

For each Nivy process, search for reusable workflows in this order:

1. Exact process name + n8n
2. Exact process name + Make
3. Exact process name + Zapier
4. Exact process name + AI agent
5. Exact process name + MCP
6. Exact process name + open source
7. End-to-end system / marketplace

## Automation acceptance criteria

A workflow is not adopted solely because it imports successfully. Check:

- Trigger and failure handling
- Data model and source of truth
- Credentials and permissions
- External API costs
- Rate limits
- Logging and audit trail
- Human approval points
- Idempotency / duplicate prevention
- Security and privacy
- Error notifications
- Rollback/manual fallback
- KPI and business outcome
