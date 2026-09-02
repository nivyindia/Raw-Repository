# BILLION DREAMS UNITED — MULTI AGENT AIOS
# MASTER IMPLEMENTATION PLAN v3

**Version:** 3.0  
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

# 4. Current implementation status

### Already materially implemented
- Agent registry and Tier-1 agent contracts
- Skill registry skeleton
- Agent-skill mapping contract
- Agent execution contract
- Runtime gateway
- Runtime adapters for LangGraph/CrewAI/Hermes/Dify
- Odoo adapter
- PostgreSQL/event persistence foundations
- n8n revenue workflows
- event/outbox routing foundation
- CRM lifecycle definition
- reusable open-source agent/workflow reference mapping

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

# 5. Immediate execution queue

## Batch 1 — Foundation completion
1. Upgrade skill registry to implementation-grade.
2. Create Prompt Registry and prompt asset structure.
3. Create Knowledge Pack Registry.
4. Create Memory Policy/Registry.
5. Create reusable Asset Registry.
6. Create Agent Factory template.
7. Map current Tier-1 agents to reusable skills.

## Batch 2 — Revenue completion
1. Complete Odoo CRM state mapping.
2. Complete A044 approval-controlled send path.
3. Complete contract → invoice → payment event path.
4. Complete payment → onboarding event path.
5. Add renewal/upsell/referral state transitions.

## Batch 3 — Agent expansion
Continue the highest-revenue Tier-1 agents and extract reusable capabilities from each rather than duplicating prompts.

## Batch 4 — Intelligence/control
Implement customer health, analytics, cost, anomaly detection and CEO command center.

## Batch 5 — Scale
Agent Factory → A2A → Marketplace → Digital Twin → autonomous optimization → multi-company scale.

# 6. Definition of Done for the AIOS

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
- evaluation and observability can measure quality, cost and reliability;
- the system can improve through governed versioned changes.

# 7. Relationship to v2

v2 remains historical implementation evidence. v3 is the **canonical planning sequence for future work**. Existing implemented artifacts are retained; they are not discarded or rebuilt solely because the plan has been upgraded.

The current strategy remains: **build first, revenue first, extract reusable capabilities during implementation, and defer the full testing campaign until the agreed later phase.**
