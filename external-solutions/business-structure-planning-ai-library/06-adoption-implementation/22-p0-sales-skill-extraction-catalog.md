# P0 Sales Skill Extraction Catalog

Research date: 2026-09-16

Purpose: identify reusable, executable sales assets before building Nivy-specific versions.

## Primary reusable sources

| Source | Asset | Reuse action | Notes |
|---|---|---|---|
| Anthropic Knowledge Work Plugins | Sales plugin | ADAPT | Official reference architecture: account research, call prep, outreach, competitive intelligence, call summary, pipeline review, forecast. https://github.com/anthropics/knowledge-work-plugins/tree/main/sales |
| Autter Agentic Sales | 11 agents + 48 skills | ADAPT / TEST | Covers preparation, prospecting, meetings, proposals, close and sales leadership. https://github.com/Autter-dev/agentic-sales-skills |
| n8n AI SDR workflow | End-to-end SDR automation | TEST / ADAPT | Lead ingestion, CRM sheet, personalized follow-ups, calendar/no-show handling. https://n8n.io/workflows/13529-run-an-ai-sdr-sales-pipeline-with-openai-google-sheets-gmail-and-calendar/ |
| n8n lead generation agent | Lead discovery + enrichment + outreach | TEST / ADAPT | Form -> business data -> email extraction -> sheet -> AI email -> Gmail. https://n8n.io/workflows/7423-lead-generation-agent/ |
| n8n lead qualification | Lead scoring/routing | TEST / ADAPT | Webhook -> validation/deduplication -> AI scoring -> Airtable/Slack. https://n8n.io/workflows/15418-qualify-and-route-high-intent-leads-with-openai-airtable-and-slack/ |
| n8n research/outreach | Deep research + personalized outreach | TEST / ADAPT | Airtable -> research -> decision maker -> outreach draft -> record update. https://n8n.io/workflows/6649-generate-sales-leads-and-personalized-outreach-emails-using-jina-ai-and-openai-agents/ |

## Nivy extraction targets

### Preparation
- ICP builder
- positioning and messaging
- competitive battlecard
- CRM setup
- sales playbook
- pricing strategy

### Prospecting
- lead-list builder
- account research
- buyer-persona research
- intent-signal monitor
- enrichment
- lead scoring
- tech-stack analysis
- warm-path finder

### Outreach
- cold email
- LinkedIn outreach
- cold call script
- multi-channel sequence
- follow-up cadence
- deliverability
- A/B testing

### Meetings
- discovery preparation
- demo customization
- meeting assistant
- objection handling
- meeting debrief
- follow-up
- task extraction
- champion enablement

### Close
- proposal/SOW generation
- pricing negotiation
- contract review handoff
- deal-risk analysis
- win/loss analysis
- customer-success handoff

### Leadership
- pipeline review
- forecasting
- performance analysis
- sales hiring
- compensation modeling
- onboarding

## Nivy implementation rule

Do not copy external skill text wholesale. Extract the workflow logic, inputs, outputs, quality checks, dependencies and integration pattern; then create a Nivy-specific implementation only where necessary.

## Minimum data contract for every adopted skill

- Skill name
- Business outcome
- Trigger
- Required inputs
- Optional inputs
- Knowledge sources
- Tools/connectors
- Processing steps
- Human approval gates
- Output artifact
- Evidence/logging
- KPI
- Failure/exception path
- Security/privacy considerations
- License/access
- Source URL
- Date checked
