# New Agentic Business Systems & Skills — Discovery Batch 04

**Date:** 2026-09-16  
**Purpose:** Capture additional reusable AI-native business operating systems, agent skills, MCP servers, CRM/ERP systems, sales intelligence, marketing systems and professional skill libraries discovered after the earlier catalogs.

## Reuse rule

`DISCOVER → VERIFY SOURCE → CHECK LICENSE/ACCESS → EXTRACT PATTERNS → TEST → ADAPT → INTEGRATE`

These are **research candidates**, not production approvals. Repository existence and README claims are recorded; Nivy must separately verify maintenance, security, licensing, API terms, data/privacy constraints and functional fit before adoption.

## New candidates

| ID | Capability | Candidate | Type | Scale | Source | License/access | Reusable value | Nivy action |
|---|---|---|---|---|---|---|---|---|
| B04-001 | Agentic GTM operating system | GTM Skills | Skills + MCP + workflows | SMB→Enterprise | https://github.com/gtm-skills/gtm | MIT | 400+ SDR/BDR prompts, 500+ AE, RevOps, CSM and founder workflows; methodologies, signal targeting, MCP | Extract skills/workflow patterns; compare with files 22–24/49–55/86 |
| B04-002 | Unified business OS | FlowWink | Business OS + MCP + agent operator | SMB→Enterprise | https://github.com/magnusfroste/flowwink | MIT | CMS, CRM, commerce, finance, HR, operations, support and growth; 500+ MCP-exposed skills; A2A/MCP federation | Architecture extraction + sandbox evaluation |
| B04-003 | Agent-native business OS | FusionClaw | Business OS + MCP | SMB/agency | https://github.com/Fusion-Data-Company/FusionClaw | MIT | CRM, employee ops, content, marketing, bookkeeping; 234 MCP tools; skill-generation/evaluation concept | Compare against Nivy Company OS architecture |
| B04-004 | Agent-native CRM | Relaticle | CRM + MCP + REST | SMB→Mid-market | https://github.com/Relaticle/relaticle | AGPL-3.0 | Self-hosted CRM, AI-agent operations, 37 MCP tools, custom fields, multi-workspace | Candidate CRM adapter; compare with Odoo |
| B04-005 | AI-first CRM | crmkit | CRM + portable skills + MCP | Solo→SMB | https://github.com/crmkit/crmkit | MIT | AI-first CRM with portable digest/import/backup/inbox-sync skills | Extract portable CRM skill patterns |
| B04-006 | AI CRM / work OS | TropaTT | CRM + tasks + projects + wiki + MCP | SMB→Enterprise | https://github.com/Anton-Barinov/TropaTT | Open-source; verify exact license | CRM, task/project management, knowledge base, chat, calendar, analytics; 620 MCP tools; agent memory and guarded writes | Architecture/security evaluation |
| B04-007 | Sales intelligence MCP | sales-intelligence-mcp | MCP | SMB→Mid-market | https://github.com/aria-agentworks/sales-intelligence-mcp | MIT | Company lookup, contact finding, outreach generation, lead scoring, A/B outreach, HubSpot sync | Add to sales acquisition comparison; test data provenance |
| B04-008 | Sales research agent | sales-research-agent | Agent + MCP | SMB→Enterprise | https://github.com/aawais-ai/sales-research-agent | Verify | CRM + recent signals + decision-maker selection + grounded outreach; offline test suite | Extract research/evaluation pattern |
| B04-009 | Professional AI workforce | agent-skills-professional | Skills library | All | https://github.com/aiagenta2z/agent-skills-professional | Verify | 30+ professional roles including HR, marketing, product, sales, engineering, legal, operations, support, recruiting, finance, UX and security | Map roles to workforce OS 67–68 |
| B04-010 | Business skills library | business-skills | Skills library | All | https://github.com/astDeniss/business-skills | Verify | 69 operational skills across sales, marketing, SEO, paid ads, analytics, social, content, video, email, CS, ops, product, hiring and PR | Mine SKILL.md files and quality checklists |
| B04-011 | Digital marketing OS | digital-marketing-pro | Marketing OS + 163 skills | SMB→Enterprise | https://github.com/indranilbanerjee/digital-marketing-pro | Verify | Strategy, SEO, AEO/GEO, paid media, content, CRM, analytics; Agent Skills compatibility | Compare with Nivy Next marketing library |
| B04-012 | GTM skills / RevOps | sumble-skills-public | Skills library | SMB→Enterprise | https://github.com/SumbleData/sumble-skills-public | Verify | Account research, prospecting, list building, scoring, MCP sequencing, signal-based workflows | Extract scoring/prospecting methods |
| B04-013 | Legal/finance/capital skills | CaseMark skills | Professional skill library | Mid-market→Enterprise | https://github.com/CaseMark/skills | Verify | 874 legal skills; 400 finance skills; 400 capital-market skills covering M&A, VC, PE, banking, tax, insurance etc. | Extract only relevant corporate/business skills; license review |
| B04-014 | ERP for AI agents | GERP | ERP + MCP | Enterprise | https://github.com/quantDIY/GERP | MIT | Finance, HCM/payroll, SCM, assets, legal, revenue, learning, master data; Temporal workflows; MCP brain interface | Architecture/reference evaluation |
| B04-015 | AI-native ERP | lambda-erp | ERP + REST + MCP | SMB→Mid-market | https://github.com/lambdadevelopment/lambda-erp | Verify | Accounting, inventory, analytics, document workflows, API/MCP, role-capped keys, tests | Compare with Odoo/ERPNext |
| B04-016 | ERP MCP integration | mcp-erp | MCP integration layer | Mid-market→Enterprise | https://github.com/zavora-ai/mcp-erp | Verify | Unified schema over SAP, NetSuite, Odoo, Zoho Books and Business Central; governed lifecycle writes | Reuse connector/governance design |
| B04-017 | Service-business BOS | evolved | Business OS + MCP | SMB/service businesses | https://github.com/kr8tiv-ai/evolved | MIT | MCP business brain, field app, workbook, owner dashboard; pricing, dispatch, books, safety, supplier/inventory signals | Extract service-business operating pattern |
| B04-018 | Autonomous business OS | autonomous-business-os | Multi-agent BOS | SMB→Mid-market | https://github.com/Cubiczan/autonomous-business-os | Verify | Lead→revenue lifecycle, self-spawning departments, durable/auditable/retryable workflows and approval queues | Compare orchestration/control-plane model |
| B04-019 | Solo-founder autonomous OS | Kompany | Agent OS | Solo→SMB | https://github.com/Fei2-Labs/Kompany | AGPL-3.0 | AI C-suite, directives, budgets, multi-agent debates, cost tracking, REST/MCP/SDK | Already cataloged; re-verify latest architecture |
| B04-020 | India agent-native finance OS | Hisaabo | Finance OS + MCP | India SMB | https://github.com/hisaabo/hisaabo | Verify | Invoices, bank reconciliation, GST, statements and audit trails through shared structured primitives | Already cataloged; evaluate for India finance layer |

## Additional sales/acquisition candidates

| Candidate | Coverage | Source |
|---|---|---|
| Apify Agent Skills | Universal web/social acquisition via curated actors | https://github.com/apify/agent-skills |
| Apollo MCP variants | Prospecting, enrichment, sequences, CRM | https://github.com/apolloio/apollo-mcp-plugin ; https://github.com/Inferensys/apollo-io-mcp |
| B2B Enrichment MCP | Hunter + Apollo enrichment | https://github.com/Aleksey-Panf/b2b-enrichment-mcp |
| Prospector MCP | Business email discovery + verification | https://github.com/josiebot26/prospector-mcp-email-finder |
| OpenLeads | Public-source prospecting, people/email discovery, dedupe | https://github.com/Samyrrrrrr990/openleads |
| Lead-Reach | Web/social multi-source research | https://github.com/getleads-humain/Lead-Reach |
| lead-gen-hacker | n8n + Apify + LinkedIn/Instagram/Maps/YouTube/Meta Ads | https://github.com/sirlifehacker/lead-gen-hacker |
| lead-research-agent | X/LinkedIn/Reddit research + enrichment/scoring | https://github.com/mcvalosborne/lead-research-agent |
| Hermes lead-generation pipeline | Prospecting → scraping → enrichment → contact finding → scoring | https://github.com/vivekshetye/hermes-lead-generation-pipeline |

## What this batch adds to the library

### 1. A deeper Agent Skills layer

The new sources reinforce that Nivy should not treat prompts as the unit of reuse. The preferred reusable unit is:

`SKILL.md → inputs → process → tools → policy → output schema → quality checks → evaluation cases`

### 2. A stronger Business OS comparison set

The repository now has multiple independent reference architectures for:

`CRM + ERP + Finance + HR + Operations + Content + Support + Agent Operator + MCP/A2A`

This is useful for extracting patterns rather than adopting an entire platform.

### 3. A stronger AI-native CRM layer

Relaticle, crmkit, TropaTT and sales-intelligence-mcp provide additional references for:

- agent-readable CRM schemas
- MCP CRUD and analytics
- persistent agent memory
- work queues
- lead scoring
- research and outreach
- permissions and approval gates
- CRM ↔ agent synchronization

### 4. A stronger marketing layer

GTM Skills, digital-marketing-pro, business-skills and sumble-skills-public add reusable skills around:

- ICP and account research
- outbound
- RevOps
- SEO/AEO/GEO
- paid growth
- content operations
- social
- analytics
- experimentation
- customer success

### 5. A stronger enterprise integration layer

GERP, lambda-erp and mcp-erp add reference patterns for:

`ERP domains → unified schema → workflow orchestration → governed MCP → audit`

## Candidate evaluation checklist

For every candidate before adoption:

1. Confirm repository/source identity.
2. Check latest meaningful activity and maintenance.
3. Check exact license and commercial restrictions.
4. Check dependencies and external services.
5. Check data ownership and retention.
6. Check API/MCP authentication and secret handling.
7. Check RBAC and least privilege.
8. Check write-operation approval gates.
9. Check audit logging and rollback.
10. Run representative Nivy test cases.
11. Compare with existing Odoo/n8n/Mautic/Company OS components.
12. Extract reusable patterns even if the whole product is rejected.

## Important decision rule

Do **not** replace the Nivy architecture simply because a repository claims to be a complete Business OS. Treat each candidate as a source of reusable components and architectural patterns. Prefer composition around the existing Company OS unless a candidate demonstrably reduces complexity, risk and maintenance burden.

## Research status

**Discovery status:** Batch captured.  
**Adoption status:** Not approved.  
**Next phase:** source/license verification → functional extraction → sandbox tests → comparison matrix → integration selection.
