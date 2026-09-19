# Deep Dive — Agent Marketplaces & Ready-Made Business Automation

Research date: 2026-09-16

## Objective

Find deployable business agents and workflow components so Nivy does not recreate common automation from scratch.

## Marketplace map

| Source | Current discovery | Functions | Access model | Recommended use |
|---|---:|---|---|---|
| Arahi AI Marketplace | 226 templates | Sales, marketing, support, operations, finance, HR, analytics, etc. | Commercial marketplace | Search first for common cross-tool workflows |
| AgentMarketplace.ai | 23 listed agents | Sales, support, marketing, ops, recruiting, coding, finance, ecommerce, research | Commercial + selected open listings | Evaluate agent-by-agent; inspect permissions/integrations |
| MarketInc AI | 2,720 free agents | Marketing, SEO, ads, WhatsApp, research, content and local business workflows | Free to start | Mine for task-level reusable patterns |
| Salesforce AgentExchange | Agent/app/MCP ecosystem | Enterprise CRM, Slack and agent workflows | Commercial ecosystem | Enterprise reference and future client integrations |

## Search categories for every department

For each department, search marketplaces in this order:

1. End-to-end agent
2. Multi-agent workflow
3. Single-task agent
4. Workflow automation
5. Skill/prompt
6. Template/playbook
7. Framework
8. Build custom only after the above are exhausted

## Minimum evaluation record

For every candidate capture:

- resource name
- exact URL
- publisher
- function
- task
- trigger
- inputs
- outputs
- systems connected
- permissions required
- model/provider dependency
- human approval support
- audit/logging support
- free/freemium/paid
- license
- deployment model
- data location
- maintenance signal
- integration effort
- Nivy reuse action

## Red flags

Do not automatically deploy a marketplace agent because it is labelled autonomous. Check whether it:

- requires broad credentials
- writes directly to production systems
- has no approval step
- lacks audit logs
- has unclear data retention
- has no versioning
- cannot be tested safely
- depends on one vendor/model
- hides its prompt/logic when inspection is necessary

## High-priority Nivy searches

### Revenue engine

- AI SDR
- lead enrichment
- ICP research
- outbound personalization
- email sequencing
- CRM hygiene
- proposal/quote generation
- meeting preparation
- sales call analysis
- pipeline review
- follow-up automation

### Marketing engine

- market research
- competitor research
- SEO audit
- keyword research
- content planning
- content generation
- repurposing
- social scheduling
- ad creative
- landing page generation
- analytics/reporting

### Delivery engine

- client onboarding
- project setup
- requirements extraction
- task creation
- status reporting
- QA
- customer support triage
- invoice preparation
- renewal/upsell detection

### Corporate engine

- finance reporting
- HR screening
- recruiting
- policy/SOP generation
- knowledge management
- executive briefing
- risk monitoring
- compliance checklists

## Decision rule

A ready-made agent should be preferred over custom development when it meets the required task with acceptable permissions, reliability, auditability, integration effort and cost.

A ready-made agent should be adapted when its workflow is sound but its prompts, schema, brand rules or integrations need modification.

Custom development is justified only when a required capability is absent, materially constrained, or strategically differentiating.
