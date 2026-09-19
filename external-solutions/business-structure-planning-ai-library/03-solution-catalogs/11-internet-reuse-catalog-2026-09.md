# Internet Reuse Catalog — Nivy Company OS

**Research batch:** 2026-09-19  
**Purpose:** Capture existing internet resources that can be reused, adapted, integrated, or studied while building the Nivy Company Operating System.

> Governing rule: **DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

This is a living catalog, not a claim that the internet has been exhaustively searched. New discoveries should be added rather than rebuilding equivalent capabilities.

## A. High-priority resources discovered in this research batch

| ID | Area | Resource | Asset type | Access / license note | What Nivy can reuse | Source |
|---|---|---|---|---|---|---|
| R26-001 | Company OS / AI workforce | Bizbox | AI-native company orchestration + UI | Open-source; verify current license before production reuse | Company goals, AI-agent teams, budgets, governance, audit dashboard concepts | https://github.com/zesthq/bizbox |
| R26-002 | Marketing | SaaS Marketing Agents | 82 marketing agents + 19 skills | Open source / MIT stated by repository | Specialist marketing roles, orchestrator, ABM, launch, demand-gen and content workflows | https://github.com/shalintripathi/saas-marketing-agents |
| R26-003 | Marketing | UnifAPI Agents | Agents + SKILL.md skills + MCP | MIT stated by repository | SEO, AI visibility/GEO, local SEO, influencer, social listening, social selling, competitive intelligence, lead/company research | https://github.com/unifapi-agent/agents |
| R26-004 | Marketing | Loopmark Agent | LangGraph marketing agent | MIT stated by repository | Audience research, social content, email campaigns, content calendar, lead funnel, complaints | https://github.com/loopmark-opensource/loopmark-agent |
| R26-005 | Sales | Mesh Pilot AI Sales Agent | Sales agent | MIT stated by repository | Lead discovery, qualification, personalized outreach, human approval, reply/bounce/unsubscribe learning | https://github.com/Meshpilot-AGI/ai-sales-agent |
| R26-006 | Sales | Sales-Outreach | AI outreach application | Open repository; verify license before reuse | CRM integrations, lead research, company/LinkedIn/news/social research, qualification, personalized outreach, RAG/case-study support | https://github.com/codingaslu/Sales-Outreach |
| R26-007 | GTM | Awesome AI GTM | Curated discovery catalog | Public resource; each listed tool must be evaluated separately | AI SDRs, sales agents, AI visibility, website personalization, lead scoring/enrichment, forecasting, GTM content | https://github.com/ong/awesome-ai-gtm |
| R26-008 | Workflow | n8n | Workflow automation platform | Source-available/fair-code; current license must be checked before redistribution or embedding | CRM/email/calendar/AI integrations, deterministic workflows, triggers, approvals and reusable workflow patterns | https://github.com/n8n-io/n8n |
| R26-009 | Workflow | n8n CRM workflow catalog | Ready-made workflows | Individual workflow licenses/terms vary | Import/adapt sales, CRM, marketing and support workflows | https://n8n.io/workflows/categories/crm/ |
| R26-010 | Agent orchestration | LangGraph | Agent/workflow framework | Open-source project; verify current license/version | Stateful agents, durable execution, human-in-the-loop, graph workflows, subagents | https://github.com/langchain-ai/langgraph |
| R26-011 | Agent platform | Dify | Visual AI workflow/RAG/agent platform | Open-source repository; verify current license/version | Visual workflows, RAG, prompt IDE, agents, tools, APIs and observability | https://github.com/langgenius/dify |
| R26-012 | Agent framework | Microsoft Agent Framework | Enterprise agent orchestration | Open-source framework; current Microsoft terms/license apply | Multi-agent orchestration, multi-provider models, MCP/A2A interoperability | https://github.com/microsoft/agent-framework |
| R26-013 | Knowledge / AI workspace | AnythingLLM | AI workspace + RAG + agents | Core MIT stated by repository terms | Company knowledge workspaces, document Q&A, agents, MCP, OpenAPI/tools, multi-user permissions | https://github.com/Mintplex-Labs/anything-llm |
| R26-014 | Knowledge / UI | Open WebUI | AI interface + knowledge/tool layer | Current license includes branding restrictions for newer versions; inspect before rebranding | Knowledge bases, document chat, tools, skills, MCP, multi-user access | https://github.com/open-webui/open-webui |
| R26-015 | ERP / company backbone | Odoo | Modular ERP/business suite | Open-source core plus edition/module-specific licensing; inspect exact modules | CRM, website, sales, accounting, project, HR, marketing, operations | https://github.com/odoo/odoo |
| R26-016 | ERP alternative | ERPNext | Open-source ERP | GPLv3 stated by repository; trademark rules separate | Accounting, CRM, HR, projects, operations and enterprise records | https://github.com/frappe/erpnext |
| R26-017 | Unified internal UI | Appsmith | Low-code internal app/dashboard platform | Apache-2.0 stated by repository | Build Nivy dashboards/admin panels over APIs/databases without building every screen from scratch | https://github.com/appsmithorg/appsmith |
| R26-018 | Agent skills | Agent Skills Collection | 400+ cross-functional skills | Open-source repository; verify individual license | Engineering, product, marketing, sales, finance, HR, research, compliance and customer-success skills | https://github.com/itsual/agent-skills-collection |
| R26-019 | Business skills | astDeniss business-skills | 69 business skills | Open source repository; verify license/version | Sales, marketing, SEO, ads, analytics, content, CS, operations, product, hiring and PR | https://github.com/astDeniss/business-skills |
| R26-020 | Business operations | Vexjoy business-ops | Business operations skill | Open repository; verify license/version | Executive strategy, competitive intelligence, projects, finance, HR, legal, operations and sales decomposition | https://github.com/notque/vexjoy-agent/blob/main/skills/business/business-ops/SKILL.md |
| R26-021 | Corporate skills | Claude-Skills | Cross-functional skill library | Open repository; verify licenses | Strategy, PM, GTM, C-level, marketing, finance, HR, legal, operations and sales | https://github.com/borghei/Claude-Skills |
| R26-022 | Corporate skills | Awesome Claude Corporate Skills | Role/department skill catalog | Public repository; verify individual licenses | Executive, finance, HR, marketing, sales, legal, operations, engineering, product, data and procurement | https://github.com/w95/awesome-claude-corporate-skills |
| R26-023 | SOP | SOP Builder Kit | SOP methodology + prompts | Public repository; verify license | SOP interview, formatting, handoff and library governance | https://github.com/pro-how-ai/sop-builder-kit |
| R26-024 | Business planning | BusinessModelCanvasTemplate | Business-model template | Public repository; verify license | Business Model Canvas / Lean Canvas starting point | https://github.com/desireco/BusinessModelCanvasTemplate |
| R26-025 | OKR | Awesome OKR | Curated OKR resources | Public repository | Goal/OKR structures, templates and references | https://github.com/domenicosolazzo/awesome-okr |

## B. Architecture / discovery references

| ID | Area | Resource | Reuse purpose | Source |
|---|---|---|---|---|
| R26-026 | AI agent landscape | Open-source agent framework comparison | Compare code-first, visual and workspace approaches before selecting Nivy runtime components | https://www.firecrawl.dev/blog/best-open-source-agent-frameworks |
| R26-027 | Agent platform comparison | Open-source AI agent platforms comparison | Architecture reference for LangGraph, CrewAI, AutoGen, Dify, n8n and similar systems | https://www.sim.ai/library/open-source-ai-agent-platforms |
| R26-028 | Automation comparison | n8n vs Activepieces vs Windmill | Workflow-engine selection reference | https://kanopylabs.com/blog/n8n-vs-activepieces-vs-windmill-workflow-automation |
| R26-029 | Enterprise process architecture | APQC Process Classification Framework | Process taxonomy for ensuring Nivy does not miss company functions | https://www.apqc.org/process-frameworks |
| R26-030 | Team execution | Atlassian Team Playbook | Roles, planning, OKRs, prioritization, governance and team practices | https://www.atlassian.com/team-playbook/plays |

## C. Nivy V1 direct reuse shortlist

For the immediate digital-marketing-agency launch, inspect these first:

| Priority | Resource | V1 use |
|---|---|---|
| 1 | SaaS Marketing Agents | Marketing role/skill decomposition and reusable agent prompts |
| 2 | UnifAPI Agents | SEO/GEO, competitor intelligence, social listening, lead/company research |
| 3 | Mesh Pilot AI Sales Agent | Sales-pipeline and human-approved outreach pattern |
| 4 | Sales-Outreach | Lead research → qualification → personalized outreach architecture |
| 5 | n8n CRM workflows | Connect lead sources, CRM, email, calendar and follow-ups |
| 6 | Odoo | Optional CRM/business backbone if adopted in V1 |
| 7 | Dify | Fast visual AI workflow/RAG/agent prototyping |
| 8 | Appsmith | Fast internal Nivy dashboard over APIs/data |
| 9 | astDeniss business-skills | Reusable business/marketing skills |
| 10 | Loopmark Agent | Social/email/content/funnel patterns |

## D. Future Nivy Company OS reuse map

| Future layer | Reuse candidates |
|---|---|
| Unified UI | Appsmith, Open WebUI, AnythingLLM, custom Nivy frontend |
| ERP/transactional system | Odoo, ERPNext |
| Workflow/integration | n8n, Activepieces, Windmill, Temporal/Kestra as later candidates |
| Agent runtime | LangGraph, Microsoft Agent Framework, Dify |
| Knowledge/RAG | AnythingLLM, Open WebUI, Dify, LangGraph-based custom RAG |
| Marketing workforce | SaaS Marketing Agents, UnifAPI, astDeniss, Loopmark |
| Sales workforce | Mesh Pilot AI Sales Agent, Sales-Outreach, n8n CRM workflows |
| Company/strategy skills | Claude-Skills, Awesome Claude Corporate Skills, Vexjoy |
| SOP/process system | SOP Builder Kit, APQC, existing Nivy SOP framework |
| Goals/OKRs | Awesome OKR, Notion planning references, Atlassian Team Playbook |
| Company orchestration | Bizbox as a reference/experimental candidate |
| Internal apps | Appsmith |
| Integration protocol | MCP + A2A-compatible agent frameworks |
| Governance | Human approval gates, permissions, audit logs, evaluation/observability layers |

## E. Important reuse/license rule

A URL in this catalog means **discoverable/reusable candidate**, not automatic permission to copy its source code into Nivy.

Before copying code, prompts, skills or assets into a distributable Nivy product, record:

1. Exact source URL and commit/release.
2. License.
3. Attribution requirements.
4. Commercial-use restrictions.
5. Trademark/branding restrictions.
6. Dependencies and external services.
7. Security/privacy implications.
8. Whether the asset is copied, adapted, wrapped, or merely linked.
9. Nivy-specific modifications.
10. Verification/test status.

Prefer **link + metadata + adapter/wrapper** over copying large third-party repositories unless the license and maintenance model clearly justify vendoring.

## F. Discovery status

This file is a **living internet-reuse index**. The 2026-09-19 batch added agent systems, marketing/sales agents, workflow platforms, ERP/business systems, knowledge systems, internal UI platforms and company-operations references.

Next discovery passes should specifically search:

- finance/accounting/CFO agents
- HR/recruiting/people-ops agents
- legal/compliance agents
- procurement/vendor management
- customer success/support
- project/operations management
- cybersecurity/IT operations
- analytics/BI/forecasting
- document/contract intelligence
- MCP servers/connectors
- A2A agent catalogs
- voice/receptionist agents
- website/CRO agents
- social publishing/engagement
- proposal/quotation/contract generation
- international expansion/tax/compliance
- AI evaluation/observability
- identity/RBAC/approval/audit systems
