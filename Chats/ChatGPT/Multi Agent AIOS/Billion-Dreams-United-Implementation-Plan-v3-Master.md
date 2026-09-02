# BILLION DREAMS UNITED — MULTI AGENT AIOS
# MASTER IMPLEMENTATION PLAN v3

**Version:** 3.1  
**Date:** 2026-09-03  
**Status:** Canonical planning layer / supersedes v2 for future implementation sequencing

## 0. Purpose

This document consolidates the previously defined AIOS architecture, revenue-engine plan, registries, reusable skills/prompts, knowledge and memory layers, governance, security, evaluation, observability, infrastructure, open-source reuse strategy, and autonomous improvement loop into one dependency-aware implementation roadmap.

The objective is not to build a collection of disconnected agents. The objective is to build a reusable, governed **Agent Operating System** that can repeatedly create business outcomes and revenue.

## 1. Canonical operating model

```text
Company / CEO
    ↓
Control & Intelligence Layer
    ↓
Governance + Identity + Policy + Approvals
    ↓
Registries
    ├── Agents
    ├── Skills
    ├── Prompts
    ├── Tools / MCP
    ├── Models
    ├── Knowledge Packs
    ├── Memory Policies
    ├── Workflows
    ├── APIs / Credentials
    └── Reusable Assets
    ↓
Agent Capability Resolution
Agent → Approved Skill → Approved Prompt/Knowledge → Approved Tool → Authorized Action
    ↓
Runtime Layer
Hermes + LangGraph + Dify + CrewAI
    ↓
Orchestration / Event Layer
n8n + Event Bus/Outbox + State Machines
    ↓
Systems of Record
Odoo + PostgreSQL + Qdrant + MinIO
    ↓
Revenue + Operations + Finance
    ↓
Evaluation → Observability → Learning → Improvement
```

## 2. Critical principles

1. **Revenue first:** prioritize capabilities that can create, convert, retain, or expand revenue.
2. **Build once, reuse everywhere:** reusable skills, prompts, knowledge packs, tools and workflows are first-class assets.
3. **Governance is runtime-enforced:** declarations in documentation are insufficient; undeclared capabilities fail closed.
4. **Evidence over invention:** externally derived claims require provenance and freshness.
5. **Human approval before protected side effects:** financial, externally binding, irreversible, or policy-restricted actions require approval.
6. **Open-source reuse before reinvention:** discover → audit → fork/import → adapt → govern → integrate.
7. **One authoritative source of truth per domain:** Odoo for CRM/business state; PostgreSQL for operational/event state; Qdrant for approved retrieval; MinIO for durable artifacts.
8. **Every important action is traceable:** run → agent → skill → prompt/knowledge → tool → action → result → event.
9. **Multi-tenant and least privilege by default.**
10. **No false completion:** runtime reports only actions actually executed and verified.
11. **Workspace knowledge is an input, not an uncontrolled runtime source:** existing Company OS, SOP, naming, brand, research and operational artifacts must be classified, mapped, versioned and governed before becoming AIOS knowledge.

# 3. Roadmap

## A — Governance & Company Control Plane

### A.1 Identity and tenancy
- Company/tenant identity
- Actor/user identity
- Roles and RBAC
- Agent identity/version
- Correlation/run/task IDs
- Data classification

### A.2 Policy
- Action policy
- Tool permissions
- Skill permissions
- Destination permissions
- Sensitive-data policy
- Consent/contact policy
- Approval thresholds
- Autonomous-action boundaries

### A.3 Change management
- Versioning
- Compatibility checks
- Rollout/rollback
- Change approvals
- Provenance of configuration changes

**Exit:** governed identity, permissions and change contracts exist.

## B — Canonical Data, Event & State Contracts

- Entity contracts
- Agent input/output schemas
- Event envelope
- Execution contract
- Idempotency keys
- Correlation IDs
- State-transition contract
- CRM lifecycle/state machine
- Outbox/claim/ack semantics
- Error/retry/dead-letter contract
- Audit-event contract

**Exit:** business state and agent events have authoritative contracts.

## C — Registries & Reusable Asset System

### C.1 Existing registries
- Agent Registry
- Skill Registry
- Tool/MCP Registry
- Model Registry
- Workflow Registry
- API Registry
- Credential Registry
- Dependency Registry

### C.2 Upgrade to implementation-grade registries
Add:
- lifecycle status
- owner
- version
- compatibility
- permissions
- dependencies
- provenance
- cost metadata
- evaluation status
- deprecation/retirement

### C.3 Skill system
Each skill has:
- SK ID/version
- purpose
- input/output contract
- allowed agents
- allowed tools
- policy constraints
- prompt references
- knowledge references
- evaluation criteria
- cost/latency metadata

### C.4 Prompt system
Create a versioned Prompt Registry with:
- system prompts
- task prompts
- role prompts
- output-format prompts
- safety/policy prompts
- reusable templates
- model compatibility
- variables
- provenance/source
- changelog
- evaluation evidence

### C.5 Agent ↔ Skill mapping
Canonical resolution:
`Agent → Approved Skill → Approved Prompt/Knowledge → Approved Tool → Authorized Action`

Missing/ambiguous mappings fail closed.

### C.6 Knowledge Packs
Reusable domain knowledge packages:
- company knowledge
- product/service knowledge
- ICP knowledge
- sales playbooks
- brand voice
- pricing/offer rules
- policies/SOPs
- technical documentation
- client-specific knowledge

Every pack requires ownership, version, source, freshness and access policy.

### C.7 Memory system
Separate:
- short-term execution memory
- conversation memory
- customer/account memory
- agent memory
- organizational memory
- procedural memory

Memory must have retention, scope, provenance, privacy and deletion rules.

### C.8 Reusable Asset Library
Catalog:
- open-source agents
- n8n workflows
- prompts
- skills
- tools
- connectors
- templates
- playbooks
- evaluators

Each imported asset must record source, license, audit status, modifications and AIOS compatibility.

**Exit:** AIOS can compose agents from reusable governed capabilities instead of duplicating logic.

## D — Policy, Approval, Safety & Trust

- Human approval service
- Approval tokens
- Escalation rules
- PII/consent controls
- Contact suppression
- Financial thresholds
- External-send controls
- Secrets management
- Prompt-injection/tool-abuse defenses
- Data egress controls
- Audit trail

**Exit:** high-impact actions are protected before side effects.

## E — Infrastructure & Runtime Fabric

Canonical stack:
- Hermes
- LangGraph
- Dify
- CrewAI
- n8n
- Odoo
- PostgreSQL
- Qdrant
- MinIO

Implement:
- runtime adapters
- gateway
- health checks
- service discovery
- secret/config handling
- queues
- retries/timeouts
- artifact storage
- deployment configuration
- backup/recovery

## F — Revenue Agent Factory

Do not treat each agent as an isolated project.

Create a standard agent factory template containing:
- agent.yaml
- prompt references
- skills
- tools
- input schema
- output schema
- policy
- knowledge
- memory policy
- events
- evaluation metadata
- observability metadata
- deployment metadata

Canonical Tier-1 revenue agents remain:
A001, A002, A034, A035, A036, A037, A038, A039, A041, A042, A043, A044, A049, A050, A052, A054, A055, A060, A065.

Build in revenue priority order, while extracting reusable skills/prompts from each implementation.

## G — Revenue Workflows & State Machines

Implement the complete loop:

`Lead → Outreach → Meeting → Proposal → Contract → Payment → Delivery → Renewal → Upsell → Referral → Advocacy`

Priority workflows:
1. Lead intake → enrichment → quality → scoring
2. Scoring → segmentation → outreach strategy → personalization → outreach
3. Reply → triage → qualification
4. Qualification → meeting prep → proposal
5. Proposal → approval → contract
6. Contract → invoice/payment
7. Payment → onboarding
8. Delivery → health monitoring
9. Renewal → upsell/cross-sell
10. Referral → advocacy

All handoffs are event-driven, idempotent and state-aware.

## H — Communications & Intelligence

- Central inbox
- Email
- WhatsApp
- SMS
- LinkedIn where permitted
- Voice/call preparation
- Conversation intelligence
- Meeting intelligence
- Document intelligence/OCR
- Customer interaction timeline

All outbound communication remains policy/approval governed.

## I — Customer Success & Retention

- Onboarding
- Project handoff
- Delivery tracking
- Customer health score
- Risk/churn detection
- Support triage
- Renewal prediction
- Upsell/cross-sell
- Referral detection
- Advocacy automation

## J — Finance & Monetization

- Quote/pricing controls
- Proposal
- Contract state
- Invoice
- Payment links/providers
- Payment confirmation events
- Revenue recognition/state
- Collections
- Commission tracking
- Refund/escalation controls
- Financial reporting

Financial side effects require policy/approval according to threshold.

## K — Marketing & Growth Engine

Use the existing marketing skill catalog and extend it into executable capabilities:
- market/competitor research
- positioning
- messaging
- content strategy
- SEO
- social
- email nurturing
- community
- partnerships
- PR
- attribution
- experimentation

Marketing outputs must connect to measurable pipeline/revenue events.

## L — Control & Intelligence Layer

CEO/management control plane:
- company health
- revenue dashboard
- pipeline
- agent health
- workflow health
- cost/usage
- approvals
- risks
- anomalies
- forecasts
- strategic recommendations
- command center

The control layer observes and governs; it must not silently bypass domain systems or policy.

## M — Evaluation, QA & Observability

Formal testing can be sequenced later during the current build sprint, but the architecture must reserve:
- golden cases
- regression suites
- prompt/skill evaluations
- tool-call evaluations
- policy tests
- workflow tests
- production monitoring
- traces
- cost/latency metrics
- failure taxonomy
- drift detection

Every material change should eventually trigger evaluation evidence.

## N — Learning & Continuous Improvement

Closed loop:

`Outcome → Telemetry → Evaluation → Failure/Opportunity Detection → Skill/Prompt/Workflow Change → Review → Versioned Rollout → Outcome`

Include:
- prompt optimization
- skill optimization
- workflow optimization
- routing optimization
- cost optimization
- model selection
- human feedback
- knowledge freshness

No autonomous change may bypass change-management policy.

## O — Agent-to-Agent & Distributed Collaboration

- In-process delegation where appropriate
- A2A for process/machine/framework boundaries
- shared execution context
- capability discovery
- delegation permissions
- result provenance
- timeout/cancellation
- conflict resolution

## P — Agent Factory, Marketplace & Digital Twin

Later-scale capabilities:
- generate new agents from requirements
- generate skill bundles
- generate workflow scaffolds
- import/audit open-source assets
- internal agent marketplace
- reusable company templates
- company digital twin
- simulation and forecasting

## Q — Scale, Reliability & Multi-Company Operations

- multi-tenant isolation
- regional deployment
- horizontal scaling
- disaster recovery
- backup/restore
- rate limits
- cost budgets
- SLO/SLA
- capacity planning
- governance at scale

# 4. Cross-Workspace Source Inventory

The public `nivyindia/Raw-Repository` contains important Company OS, Notion, research and Claude planning artifacts outside `Chats/ChatGPT/Multi Agent AIOS`. These are not automatically canonical runtime specifications. They are **source material to ingest, classify, reconcile and convert into AIOS registries/knowledge/policies/workflows where relevant**.

### 4.1 Company OS / operating model sources
- `Nivy Next/🟦 Nivy Next — Company OS 2a334207fb4d8186b405f32a6d1876f5.md`
- `Notion - Nivy OS/🟦 Nivy Next — Company OS 72aeb94b1a2a8251a4c9814969454ca4.md`
- `Notion - Nivy OS/🏢 Nivy OS — Company Operating System 806eb94b1a2a825894cb019a2efb2336.md`
- `Notion - Nivy OS/⚡ NIVY OS CLAUDE COMMAND — Master Build & Restruct 358eb94b1a2a81b682cfe2dd2df08ba4.md`
- `Notion - Nivy OS/🏗️ Phase 1 — New Master Structure Design 13aeb94b1a2a8399addf01fe9e912e97.md`
- `Notion - Nivy OS/🗺️ NIVY EMPIRES — Master Reorganization Plan (Claude) ...md`
- `Notion - Nivy OS/📐 Naming Conventions & Versioning Guide — Nivy ...md`

**AIOS use:** company/brand/department structure, metadata standards, naming, ownership, dashboards, document architecture and operating-model knowledge.

### 4.2 SOP / process / documentation sources
- `Notion - Nivy OS/📚 SOPs Quick Reference Index — All Nivy Divisions ...md`
- `Chats/Claude/Documentation-method-for-international-development.md`
- Employee onboarding checklist artifacts under `Notion - Nivy OS/` and `Nivy Research Data/`
- Document-control, naming, versioning and classification artifacts discovered in the workspace

**AIOS use:** Knowledge Packs, procedural memory, workflow templates, SOP-aware agents, onboarding and operational playbooks.

### 4.3 Revenue / growth / one-person-company sources
- `Chats/Claude/Revenue-Priorities-Plan.md`
- `Chats/ChatGPT/One-person-AI-company.md`
- `Chats/ChatGPT/Multi Agent AIOS/Blueprint Update.md`
- `Chats/ChatGPT/Multi Agent AIOS/Billion-Dreams-United-AI-Native-Company-OS-v6.md`
- `Chats/ChatGPT/Multi Agent AIOS/Missing-Layers-Review.md`
- `Chats/ChatGPT/Multi Agent AIOS/Agent List.txt`

**AIOS use:** revenue prioritization, daily/weekly business automation, sales/marketing/finance coverage, missing-layer backlog and ready-made agent/workflow procurement strategy.

### 4.4 AIOS-native architecture sources
- `Chats/ChatGPT/Multi Agent AIOS/ARCHITECTURE_DECISIONS.md`
- `Chats/ChatGPT/Multi Agent AIOS/02-agents/AGENT_SKILL_MAPPING.md`
- `Chats/ChatGPT/Multi Agent AIOS/02-agents/AGENT_TOOL_MAPPING.md`
- `Chats/ChatGPT/Multi Agent AIOS/02-agents/F1-open-source-agent-reference-map.md`
- `Chats/ChatGPT/Multi Agent AIOS/03-skills/registry.yaml`
- `Chats/ChatGPT/Multi Agent AIOS/04-tools/TOOL_REGISTRY.yaml`
- `Chats/ChatGPT/Multi Agent AIOS/06-data/DATA_CATALOG.md`
- `Chats/ChatGPT/Multi Agent AIOS/09-runtime/`
- `Chats/ChatGPT/Multi Agent AIOS/Billion-Dreams-United-Implementation-Plan-v2-Granular-Steps.md`

**AIOS use:** canonical technical contracts, capability registries, data catalog, runtime implementation and historical implementation evidence.

### 4.5 Sources that must be treated as superseded/draft
- `Nivy Next/⚠️ Archive — Draft Company OS (Do Not Use) ...md`
- Any document explicitly marked Draft, Archive, superseded or Do Not Use

These can inform history or conflict resolution but must not silently become canonical runtime truth.

### 4.6 Workspace ingestion rule
For every relevant external workspace file:

`Discover → classify → identify authority → detect conflicts → extract reusable knowledge/process → assign registry/knowledge-pack destination → version → link provenance → approve for runtime use`

Do not bulk-copy the entire workspace into Qdrant or agent context. Only approved, classified and access-controlled knowledge becomes runtime knowledge.

# 5. Small-Phase Execution Plan

The A–Q architecture is the macro roadmap. The following phases are the **actual execution units**. Each phase should be small enough to implement as one focused batch and should leave a concrete repository artifact behind.

## Phase 0 — Baseline & Source Reconciliation

### 0.1 Canonical-plan alignment
- Make v3.1 the canonical implementation plan.
- Update Master Index to point to v3.1.
- Mark v2 as historical evidence.

### 0.2 Workspace inventory
- Inventory AIOS folder.
- Inventory relevant Company OS / Notion / Claude / Research artifacts.
- Identify canonical vs duplicate/draft documents.

### 0.3 Conflict register
- Record conflicting architecture, naming, document-type, ownership, lifecycle and company-structure definitions.
- Decide authoritative source for each domain.

**Deliverable:** source map + conflict map + canonical navigation.

## Phase 1 — Governance Metadata Foundation

### 1.1 Document metadata
- Code
- Title
- Department
- Brand
- Type
- PARA bucket
- Version
- Lifecycle
- Confidentiality
- Owner/RACI
- Dates
- Tags

### 1.2 Naming/versioning
- Normalize AIOS asset naming and versions.
- Connect document versioning with registry versions.

### 1.3 Ownership
- Owner registry
- RACI
- approval authority

**Deliverable:** governance metadata contract.

## Phase 2 — Capability Registry Foundation

### 2.1 Skill Registry
- Upgrade SK001–SK050 from skeleton to implementation-grade.
- Add owner/version/permissions/dependencies/provenance/evaluation/cost/deprecation.

### 2.2 Prompt Registry
- Create prompt IDs, versions, templates, variables, model compatibility and evaluation references.

### 2.3 Knowledge Pack Registry
- Define pack IDs, scope, source, freshness, access policy and owner.

### 2.4 Memory Registry
- Define memory classes, retention, privacy, provenance, scope and deletion.

### 2.5 Reusable Asset Registry
- Register open-source agents, n8n workflows, prompts, skills, tools, connectors, templates, playbooks and evaluators.

**Deliverable:** reusable capability layer.

## Phase 3 — Agent Factory & Capability Binding

### 3.1 Agent Factory template
- agent.yaml
- skills
- prompts
- knowledge
- tools
- policy
- memory
- events
- evaluation
- observability
- deployment

### 3.2 Agent → Skill mapping
- Map all current Tier-1 agents.
- Validate tool authorization.
- Validate prompt/knowledge references.

### 3.3 Open-source integration pipeline
- Discover
- license/audit
- import/fork
- modify
- map to AIOS
- govern

**Deliverable:** repeatable agent creation system.

## Phase 4 — Runtime & Execution Foundation

### 4.1 Gateway
- Agent discovery
- invocation
- policy boundary
- runtime selection

### 4.2 Adapters
- Hermes
- LangGraph
- Dify
- CrewAI

### 4.3 Persistence
- executions
- events
- approvals
- outbox
- run state

### 4.4 Reliability
- timeouts
- retries
- idempotency
- dead-letter/error handling

**Deliverable:** governed executable runtime.

## Phase 5 — CRM & Revenue State Machine

### 5.1 CRM lifecycle
- New
- Scored
- Outreach
- Qualified
- Meeting
- Proposal
- Negotiation
- Won
- Onboarding
- Delivery
- Renewal/Upsell

### 5.2 State/event mapping
- Every state transition gets an event.
- Every event identifies execution/entity/source.

### 5.3 Odoo integration
- CRM upsert
- dedupe
- lifecycle mutation
- provenance fields

**Deliverable:** authoritative revenue state machine.

## Phase 6 — Lead Intelligence Engine

### 6.1 Discovery
A034 Lead Discovery.

### 6.2 Contact
A035 Contact Discovery.

### 6.3 Enrichment
A036 Enrichment.

### 6.4 Quality
A037 Data Quality.

### 6.5 Verification
A038 Verification.

### 6.6 Scoring
A039 Lead Scoring.

### 6.7 Account intelligence
A041 Account Research + A042 Signal Detection.

### 6.8 Segmentation
A040 where required by the revenue workflow.

**Deliverable:** evidence-backed, CRM-ready lead intelligence.

## Phase 7 — Outreach Engine

### 7.1 Strategy
A043 Outreach Strategy.

### 7.2 Personalization
A049 Personalization.

### 7.3 Draft/send
A044 Email Outreach with approval gate.

### 7.4 Follow-up
A050 Follow-Up.

### 7.5 Reply handling
A052 Reply Triage.

**Deliverable:** governed outbound/inbound sales loop.

## Phase 8 — Qualification → Meeting → Proposal

### 8.1 Qualification
A054.

### 8.2 Meeting preparation
A055.

### 8.3 Needs analysis / solution mapping
A057 / A058 where applicable.

### 8.4 Proposal
A060.

### 8.5 Approval / negotiation / contract
- approval token
- contract state
- audit event

**Deliverable:** opportunity conversion engine.

## Phase 9 — Contract → Cash

### 9.1 Contract event
- contract.created
- contract.approved

### 9.2 Invoice
- invoice creation
- invoice state

### 9.3 Payment
- payment link/provider
- payment confirmation
- failure/refund handling

### 9.4 Revenue events
- payment.received
- payment.failed
- refund.requested

**Deliverable:** measurable contract-to-cash path.

## Phase 10 — Cash → Customer Delivery

### 10.1 Payment → onboarding event

### 10.2 Onboarding
A065.

### 10.3 Delivery handoff
- project/task creation
- owner assignment
- customer communication

### 10.4 Customer timeline
- sales context
- commitments
- documents
- delivery state

**Deliverable:** closed sales-to-delivery handoff.

## Phase 11 — Customer Success & Expansion

### 11.1 Health
- health score
- engagement
- delivery risk

### 11.2 Retention
- churn signals
- renewal prediction
- renewal workflow

### 11.3 Expansion
- upsell
- cross-sell
- referral
- advocacy

**Deliverable:** post-sale revenue engine.

## Phase 12 — Communications & Intelligence

### 12.1 Central inbox
### 12.2 Email/WhatsApp/SMS
### 12.3 LinkedIn where permitted
### 12.4 Voice/call preparation
### 12.5 Conversation intelligence
### 12.6 Meeting intelligence
### 12.7 Document/OCR intelligence

**Deliverable:** unified customer communication intelligence.

## Phase 13 — Marketing & Growth

### 13.1 Market/competitor research
### 13.2 Positioning/messaging
### 13.3 Content engine
### 13.4 SEO
### 13.5 Social
### 13.6 Email nurturing
### 13.7 Community/partnerships/PR
### 13.8 Attribution
### 13.9 Growth experiments

Every activity must map to measurable pipeline/revenue outcomes.

**Deliverable:** marketing-to-revenue loop.

## Phase 14 — Finance & Business Operations

### 14.1 Pricing/quotes
### 14.2 Invoices
### 14.3 Collections
### 14.4 Commission
### 14.5 Refunds
### 14.6 Revenue reporting
### 14.7 HR/people operations where relevant
### 14.8 Operational task queues / priority / SLA / notifications

**Deliverable:** finance + operations automation layer.

## Phase 15 — CEO Control & Intelligence

### 15.1 Global dashboard
### 15.2 Brand registry / company registry
### 15.3 Department dashboards
### 15.4 Revenue/pipeline intelligence
### 15.5 Agent/workflow health
### 15.6 Cost/usage
### 15.7 Approvals and risk queue
### 15.8 Forecasts/anomalies/recommendations

**Deliverable:** CEO/management command center.

## Phase 16 — Evaluation, QA & Observability

Testing remains deliberately later in the current build strategy, but implementation hooks are required throughout.

### 16.1 Golden cases
### 16.2 Prompt/skill evaluation
### 16.3 Tool-call evaluation
### 16.4 Workflow tests
### 16.5 Policy tests
### 16.6 Trace/cost/latency
### 16.7 Failure taxonomy
### 16.8 Drift detection

**Deliverable:** measurable quality/reliability layer.

## Phase 17 — Learning & Continuous Improvement

### 17.1 Outcome telemetry
### 17.2 Failure/opportunity detection
### 17.3 Prompt improvement
### 17.4 Skill improvement
### 17.5 Workflow/routing improvement
### 17.6 Knowledge freshness
### 17.7 Model/cost optimization
### 17.8 Governed rollout

**Deliverable:** closed improvement loop.

## Phase 18 — A2A & Multi-Agent Collaboration

### 18.1 Capability discovery
### 18.2 Delegation permissions
### 18.3 Shared execution context
### 18.4 A2A boundaries
### 18.5 Conflict resolution
### 18.6 Cancellation/timeouts

**Deliverable:** controlled multi-agent collaboration.

## Phase 19 — Agent Factory / Marketplace / Digital Twin

### 19.1 Agent generation
### 19.2 Skill bundle generation
### 19.3 Workflow generation
### 19.4 Internal Agent Library
### 19.5 Marketplace
### 19.6 Company templates
### 19.7 Digital Twin
### 19.8 Simulation/forecasting

**Deliverable:** scalable agent-production system.

## Phase 20 — Scale & Multi-Company Operations

### 20.1 Multi-tenancy
### 20.2 RBAC/data isolation
### 20.3 Company-specific policies
### 20.4 Company-specific agents/knowledge
### 20.5 Queues/SLO/SLA
### 20.6 Horizontal scaling
### 20.7 Backup/disaster recovery
### 20.8 Cost budgets/capacity planning

**Deliverable:** production-scale multi-company AIOS.

## Phase 21 — Production Hardening

### 21.1 Security review
### 21.2 Secrets and data egress review
### 21.3 Compliance review
### 21.4 Failure recovery
### 21.5 Backup/restore
### 21.6 End-to-end validation
### 21.7 Production deployment

**Deliverable:** hardened production system.

# 6. Current implementation status

### Already materially implemented
- Agent registry and Tier-1 agent contracts
- Skill registry skeleton
- Agent-skill mapping contract
- Agent-tool mapping contract
- Tool registry
- Data catalog
- Agent execution contract
- Runtime gateway
- Runtime adapters for LangGraph/CrewAI/Hermes/Dify
- Odoo adapter
- PostgreSQL/event persistence foundations
- n8n revenue workflows
- event/outbox routing foundation
- CRM lifecycle definition
- reusable open-source agent/workflow reference mapping
- CI validation foundation

### Partially implemented / next hardening
- Production-grade Skill Registry
- Prompt Registry
- Knowledge Pack Registry
- Memory implementation
- Full Agent→Skill mapping for implemented agents
- CRM state mutation completeness
- Approval workflow for externally protected actions
- Payment/revenue event path
- End-to-end event idempotency
- observability/cost layer
- workspace knowledge ingestion and provenance

# 7. Immediate execution queue

## Sprint 1 — Phase 0–2: Foundation
1. Update Master Index to v3.1.
2. Complete workspace/source inventory.
3. Create conflict register.
4. Upgrade Skill Registry.
5. Create Prompt Registry.
6. Create Knowledge Pack Registry.
7. Create Memory Registry/Policy.
8. Create Reusable Asset Registry.

## Sprint 2 — Phase 3–5: Agent Factory + Runtime + CRM
1. Create Agent Factory template.
2. Map Tier-1 agents to skills/prompts/knowledge/tools.
3. Complete runtime persistence/outbox/error semantics.
4. Complete CRM lifecycle/state mutation.

## Sprint 3 — Phase 6–8: Revenue Acquisition
1. Finish lead intelligence chain.
2. Finish outreach chain.
3. Finish qualification → meeting → proposal.

## Sprint 4 — Phase 9–11: Revenue-to-Customer
1. Contract → invoice → payment.
2. Payment → onboarding.
3. Delivery → health.
4. Renewal/upsell/referral/advocacy.

## Sprint 5 — Phase 12–15: Company Operating Layer
1. Communications intelligence.
2. Marketing/growth.
3. Finance/operations.
4. CEO command center.

## Sprint 6 — Phase 16–18: Intelligence + Collaboration
1. Evaluation/observability.
2. Learning loop.
3. A2A/distributed collaboration.

## Sprint 7 — Phase 19–21: Scale
1. Agent Factory/Marketplace/Digital Twin.
2. Multi-company scale.
3. Production hardening.

# 8. Definition of Done for the AIOS

The AIOS is considered architecturally complete when:

- every agent resolves declared skills;
- every skill resolves approved prompts/knowledge/tools;
- every protected action passes policy/approval;
- every state change produces an auditable event;
- every external side effect is idempotent where required;
- business truth is maintained in authoritative systems;
- every material run is traceable;
- revenue flows from acquisition through retention/expansion;
- reusable assets can be versioned and composed;
- open-source assets can be audited and integrated safely;
- workspace knowledge is classified, governed and provenance-linked;
- evaluation and observability can measure quality, cost and reliability;
- the system can improve through governed versioned changes.

# 9. Relationship to previous plans

v2 remains historical implementation evidence. v3.1 is the **canonical planning sequence for future work**. Existing implemented artifacts are retained; they are not discarded or rebuilt solely because the plan has been upgraded.

The current strategy remains: **build first, revenue first, extract reusable capabilities during implementation, and defer the full testing campaign until the agreed later phase.**
