# AI Agents, Skills, Prompts & Agentic Assets Catalog

**Research date:** 2026-09-16

This catalog separates reusable AI assets by maturity: **prompt → skill → agent → workflow → end-to-end system**.

| Resource | Asset type | Functions | Access | What to reuse | Link |
|---|---|---|---|---|---|
| AI Agents Library Skills | Skills | Operations, sales, marketing, research, planning, email, documents | Free copy | Copy/adapt individual skills and platform patterns | https://www.aiagentslibrary.com/skills/ |
| astDeniss business-skills | Skills | Sales, marketing, SEO, ads, analytics, content, CS, ops, product, hiring, PR | Open source | 69 self-contained SKILL.md playbooks plus agent chaining instructions | https://github.com/astDeniss/business-skills |
| itsual Agent Skills Collection | Skills | Engineering, product, UX, marketing, sales, finance, HR, research, compliance, CS | Open source | Large cross-functional skills corpus; useful as a reference library | https://github.com/itsual/agent-skills-collection |
| Vexjoy business-ops | Skill | Executive, strategy, competitive intelligence, finance, HR, legal, operations, sales | Open source | Umbrella business-operations skill and decomposition model | https://github.com/notque/vexjoy-agent/blob/main/skills/business/business-ops/SKILL.md |
| Prompt Matrix | Prompt library | Strategy, marketing, sales, operations, HR, finance | Free/mixed | Prompt patterns and category coverage | https://thepromptmatrix.com/ |
| Prompt Builder Business Pack | Prompt library | Strategy, market research, operations, finance, sales, HR, SOPs, automation | Commercial/free components | Broad business prompt inventory | https://promptbuilder.cc/packs/business |
| LAXIMA AI Prompt Library | Prompt library | Sales, marketing, support, analytics, HR, operations, strategy, AI systems | Free/mixed | Prompt patterns and system prompts | https://laxima.tech/tools/library |
| MarketInc AI | Agent marketplace | Marketing, SEO, ads, content, research, local business | Free | Reusable agent ideas and task decomposition; useful for India-market workflows | https://marketinc.io/ |
| Agent Marketplace | Agent marketplace | Sales, support, marketing, ops, finance, recruiting, research | Commercial/mixed | Ready-made agent architecture, permissions and deployment patterns | https://agentmarketplace.ai/ |
| Arahi AI Marketplace | Agent marketplace | Sales, marketing, support, operations, finance, HR | Commercial/mixed | Editable agent templates and integration patterns | https://arahi.ai/marketplace |
| Runlane | Agent platform | Marketing, support, sales, HR, finance, operations, growth | Commercial/free trial | Agent presets + skills + runbooks; human approval, budgets, audit trails | https://runlane.app/ |
| n8n AI SDR | Workflow/agent | Sales/RevOps | Free | CRM agent, follow-up agent, concierge/calendar agent, no-show agent | https://n8n.io/workflows/13529-run-an-ai-sdr-sales-pipeline-with-openai-google-sheets-gmail-and-calendar/ |
| n8n multi-platform sales agent | Workflow/agent | Sales | Paid | Multi-channel agent, RAG, CRM sub-agent, calendar sub-agent | https://n8n.io/workflows/4508-multi-platform-ai-sales-agent-with-rag-crm-logging-and-appointment-booking/ |
| n8n CRM catalog | Workflow library | CRM, sales, marketing, support, AI | Mixed; many free | Searchable workflow patterns and importable automations | https://n8n.io/workflows/categories/crm/ |

## AI asset selection rules

### Prompt
Use when the task is primarily cognitive and has no persistent state or external action.

### Skill
Use when the work requires a repeatable method, inputs, steps, output schema and quality checks.

### Agent
Use when the task needs tool access, decisions, state, or iterative execution.

### Workflow
Use when deterministic triggers, integrations and routing are important.

### End-to-end system
Use when multiple skills/agents/workflows, data stores, governance and KPIs are already packaged together.

## Nivy reuse pattern

For each company function:

`Business outcome → Process → SOP → Skill → Agent → Workflow → Human approval → KPI → Audit → Improvement`

Do not turn every prompt into an agent. Prefer the lowest-complexity reusable asset that reliably completes the job.
