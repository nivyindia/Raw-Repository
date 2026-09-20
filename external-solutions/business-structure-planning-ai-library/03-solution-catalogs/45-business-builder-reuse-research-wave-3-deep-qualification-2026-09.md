# Business Builder Reuse Research — Wave 3 Deep Qualification & Extraction — 2026-09

## Purpose

Wave 3 converts the highest-value Wave 2 discovery candidates from **repository-level discovery** into **evidence-backed reusable asset records**.

Governing rule:

**DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

> Important: repository inspection is not the same as Nivy runtime qualification. These records remain **Pre-Qualification** until dependency, security, runtime, maintenance, and reproducibility checks are executed.

## Evidence standard

A candidate is only promoted from Discovery when we can identify:
- concrete capability/assets in the repository;
- repository license evidence where available;
- installation/runtime path;
- likely Nivy use;
- adaptation/integration boundary;
- explicit qualification gaps.

---

## Wave 3 priority extraction

| ID | Resource | Evidence observed | License evidence | Reusable assets | Nivy use | Status |
|---|---|---|---|---|---|---|
| W3-001 | [GTM Agents](https://github.com/gtmagents/gtm-agents) | README documents 67 plugins, 92 agents, 52 business skills and 20 workflow orchestrators; includes sales, marketing, growth, CS and RevOps coverage. | Apache-2.0 LICENSE inspected. | Plugins, business skills, agents, orchestration patterns, use-case recipes. | Seed Sales/Marketing/Growth AI workforce and workflow library; extract individual skills rather than importing the whole marketplace blindly. | Pre-Qualification |
| W3-002 | [B2B SDR Agent Template](https://github.com/iPythoning/b2b-sdr-agent-template) | README exposes a 7-layer context architecture: IDENTITY, SOUL, AGENTS, USER, HEARTBEAT, MEMORY, TOOLS; OpenClaw deployment, cron checks, Chroma memory and multi-channel SDR workflow. | README identifies MIT license. | Context files, 10-stage sales workflow, skill structure, cron/health checks, deployment scripts. | Candidate seed for Nivy SDR/RevOps AI employee template and reusable sales-agent contract. | Pre-Qualification |
| W3-003 | [Marketing Skills](https://github.com/mysticaltech/marketingskills) | README lists reusable marketing skills including A/B testing, analytics, competitor alternatives, content strategy, copywriting, email sequence, CRO, launch, pricing, SEO, paid ads, referral, schema, social content. | License must be rechecked at file/package level before vendoring; repository is a fork and credits the upstream project. | Individual SKILL.md / .skill packages; can install selected skills with npx skills or Claude Code. | Strong source for Nivy Marketing Department skill registry; adapt to common Nivy input/output contract. | Pre-Qualification |
| W3-004 | [eCommerce Skills](https://github.com/nexscope-ai/eCommerce-Skills) | README documents 157 free AI-agent skills for Amazon, Shopify, eBay, Etsy, TikTok Shop and Walmart; includes competitor analysis, pricing, profitability, growth, cross-border and PPC skills. | License file/package not yet inspected. | Plain-text skills, marketplace-specific strategy modules, calculators/frameworks. | Business-type-specific extension for ecommerce/D2C/marketplace phase coverage. | Pre-Qualification |
| W3-005 | [Claude Agents Library](https://github.com/aiagentskit/claude-agents-library) | README documents 34 agents across 7 categories, with purpose, responsibilities, skills, communication style, prompts and related-agent links; MCP integration patterns are documented. | MIT badge/license claim in README; LICENSE should still be inspected before reuse. | Agent definitions, role prompts, selection guide, MCP patterns, cost/model selection guidance. | Seed reusable AI employee role cards and agent registry templates. | Pre-Qualification |
| W3-006 | [OpenClaw Master Skills](https://github.com/LeoYeAI/openclaw-master-skills) | README exposes a large curated skills index and OpenClaw installation path; examples include research, browser automation, MCP, prompt engineering, model routing, media, search and agent creation. | License not yet verified. | Skill folders, skill index, discovery/install conventions, browser/search/MCP/model-router skills. | Candidate external skill source for continuous-discovery ingestion; do not bulk-copy without per-skill license/security checks. | Pre-Qualification |
| W3-007 | [AI Brand Architect / NEXORA](https://github.com/Vishwajeetsrk/AI-Brand-Architect) | README describes brand DNA, design tokens, brand wizard, logo/color/type tools, website builder, AgentOS, planner, communication bus, scheduler, reflection, safety governance, shared memory and templates. | MIT license stated in README; LICENSE should be inspected before code reuse. | Brand system concepts, AgentOS modules, planner/bus/scheduler/governance/memory patterns, UI architecture. | Reference architecture for Brand/Corporate Identity plus agent-runtime/control-plane gaps. | Pre-Qualification |
| W3-008 | [Zylo Deck Studio / SocialManager](https://github.com/Aznair25/SocialManager) | README shows deterministic HTML/CSS-to-1080x1350 carousel rendering, LLM copy generation, validation, review contact sheet, CLI + browser UI, local rendering and tests. | License not yet verified. | Content-to-deck pipeline, deterministic renderer, validation rules, human review gate, CLI/API structure. | Reusable Content → Social Creative pipeline; especially useful for P14/P16/P17 and human approval controls. | Pre-Qualification |
| W3-009 | [Claude Code Skills](https://github.com/AlexBramall/claude-code-skills) | README documents 328 skills across 14 domains and ~402 stdlib-only Python CLI tools; includes engineering, product, marketing, research, PM, regulatory, C-level, finance and operations. | MIT stated in README. | SKILL.md packages, reference files, templates/checklists, stdlib-only utility scripts. | High-value cross-department skill source; candidate for Nivy skill registry and departmental skill packs. | Pre-Qualification |
| W3-010 | [CogOS](https://github.com/gvern/cogos-ai) | README describes a personal cognitive OS with FastAPI API, knowledge constellation, ingestion, relationship graph, memory/context, intelligent agent and audio/voice processing. | License not yet verified. | Knowledge graph, ingestion, memory/context, agent and voice architecture ideas. | Reference for enterprise memory/knowledge graph and universal context layers; likely adapt rather than directly adopt. | Pre-Qualification |
| W3-011 | [Openkoda](https://github.com/openkoda/openkoda) | README documents enterprise application foundation, auth/user management, multitenancy, dashboards, data model builder, SQL reporting, automation/event listeners/schedulers, REST API, integrations, RBAC, audit, backup and health monitoring. | MIT license explicitly stated in README. | Enterprise app foundation, dynamic entities, dashboards, workflows/events, REST integrations, RBAC, audit/backup patterns. | Candidate platform component for business application/control-plane surfaces; evaluate against Odoo/NocoBase before choosing. | Pre-Qualification |

---

## Immediate reuse extraction map

### A. Sales / Revenue

**Primary sources**
1. GTM Agents
2. B2B SDR Agent Template
3. Claude Agents Library

**Assets to extract**
- lead research
- lead qualification
- SDR sequence generation
- pipeline inspection
- sales-call preparation
- account management
- customer success
- competitive intelligence
- revenue analytics
- sales-agent context contract
- heartbeat/periodic pipeline checks
- human handoff rules

**Target Nivy locations**
- L1/L2 Sales task automations
- L3 Lead→Meeting / Opportunity→Proposal workflows
- L5 Sales/RevOps department system
- L7 CRO/RevOps AI Manager
- AI Employee Registry → SDR / Researcher / Account Manager

### B. Marketing / Growth

**Primary sources**
1. GTM Agents
2. Marketing Skills
3. Claude Code Skills
4. OpenClaw Master Skills

**Assets to extract**
- copywriting
- content strategy
- SEO audit
- programmatic SEO
- paid ads
- email sequences
- social content
- CRO
- A/B testing
- launch strategy
- pricing strategy
- referral programs
- analytics tracking

**Target Nivy locations**
- Marketing skill registry
- P17 Demand Generation
- P16 Social/Community
- P14 Content/Knowledge
- L7 CMO/Growth AI Manager

### C. Ecommerce / Marketplace

**Primary source**
- eCommerce Skills

**Assets to extract**
- competitor analysis
- marketplace pricing
- profit calculation
- PPC strategy
- product descriptions
- cross-border ecommerce
- brand protection
- marketplace-specific operating skills

**Target Nivy locations**
- G15 Ecommerce/D2C/marketplace business type
- P07 Product/Service
- P17 Marketing
- P18 Sales
- P28 Internationalization

### D. Brand / Digital Presence

**Primary sources**
1. AI Brand Architect / NEXORA
2. Zylo Deck Studio
3. GTM Agents

**Assets to extract**
- brand DNA
- design tokens
- brand guidelines
- creative generation
- deterministic social rendering
- human creative approval
- website/UI generation patterns

**Target Nivy locations**
- P11 Brand
- P15 Website
- P16 Social
- P17 Marketing
- Business Artifact Factory

### E. Enterprise Agent / Skill Infrastructure

**Primary sources**
1. Claude Code Skills
2. OpenClaw Master Skills
3. AI Brand Architect
4. B2B SDR Agent Template

**Assets to extract**
- SKILL.md contract
- agent role contract
- planner
- task scheduler
- communication bus
- memory/context
- safety governance
- health checks
- model/tool routing
- skill discovery/install
- reusable reference files

**Target Nivy locations**
- L7 AI Manager
- L8 AI Executive
- L9 Control Tower
- L10 Autonomous Company
- AI Workforce Registry
- Skill Registry

### F. Knowledge / Memory

**Primary sources**
1. CogOS
2. B2B SDR Agent Template
3. AI Brand Architect

**Assets to extract**
- memory layers
- context construction
- knowledge graph
- ingestion
- relationship mapping
- scoped shared memory
- anti-amnesia patterns

**Target Nivy locations**
- G29 Knowledge Lifecycle
- G41 Universal Intake
- Enterprise Memory
- Universal Company State

---

## Qualification backlog

No Wave 3 candidate is promoted to **Qualified** yet.

### Required next checks

| Check | Required evidence |
|---|---|
| License | LICENSE file + relevant subdirectory license compatibility |
| Dependencies | package manifests / lockfiles / external services |
| Runtime | local Windows/Docker/Linux execution where applicable |
| Secrets | API keys, credentials, external SaaS requirements |
| Security | shell execution, browser permissions, network access, data handling |
| Data | persistence, PII, tenant isolation, export/delete behavior |
| Maintenance | recent commits/releases/issues |
| Tests | existing test suite + reproducible test command |
| Integration | API/MCP/webhook/CLI/file interface |
| Cost | local/cloud/API/SaaS cost |
| Adaptation | exact changes needed for Nivy contracts |
| Provenance | exact source path/file/commit for reused asset |

---

## Highest-priority next extraction

1. **GTM Agents** — enumerate exact plugin/skill/agent files and map them to Nivy Sales/Marketing.
2. **B2B SDR Agent Template** — extract the seven context files and convert them into the generic Nivy AI Employee contract.
3. **Claude Code Skills** — index all 328 skills by Nivy department and avoid duplicate skill creation.
4. **Marketing Skills** — extract individual SKILL.md packages and compare against existing Nivy marketing catalog.
5. **OpenClaw Master Skills** — build a discovery/index ingestion method rather than copying the entire repository.
6. **AI Brand Architect** — compare AgentOS modules against Nivy L7-L10 architecture.
7. **Openkoda** — compare as an application/control-plane candidate against Odoo, NocoBase and the existing Nivy stack.
8. **eCommerce Skills** — map marketplace-specific capabilities into business-type extensions.
9. **Zylo Deck Studio** — extract deterministic creative generation + human approval pattern.
10. **CogOS** — compare memory/knowledge-graph design against the Nivy universal memory model.

## Rule for future waves

Do not create another broad discovery list for these repositories. The next pass should extract **exact files/assets** and produce:
**Capability → Exact File → Source → License → Inputs → Outputs → Dependencies → Runtime → Integration → Security → Maintenance → Cost → Adaptation → Nivy Destination → Evidence → Qualification**.
