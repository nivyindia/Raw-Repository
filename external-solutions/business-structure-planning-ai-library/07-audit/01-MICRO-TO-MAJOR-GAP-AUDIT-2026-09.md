# Micro-to-Major Architecture & Library Audit — 2026-09

## Scope

Audit of the current Business Creation → Autonomous Company architecture and reuse-library structure across L0–L10, from atomic actions to autonomous company control.

This is an **audit artifact only**. It does not itself change implementation status.

## Executive finding

The architecture has broad capability coverage, but several foundational runtime primitives are still conceptual or missing. The largest risk is treating a cataloged capability as equivalent to an executable, qualified, operational capability.

### Critical distinction

| State | Meaning |
|---|---|
| Concept Covered | Architecture describes the capability |
| Solution Discovered | Reusable external solution found |
| Solution Qualified | License, provenance, dependency, runtime, security and evidence gates passed |
| Operational | Actually integrated and verified |

## Major findings

### F01 — Universal Object Model
Missing one canonical machine-readable object model for people, organizations, legal entities, departments, teams, customers, suppliers, products, services, contracts, obligations, transactions, tasks, workflows, decisions, evidence, incidents, risks, controls, agents, skills, tools, metrics and experiments.

### F02 — Universal State Model
No single state-machine contract shared by business objects, tasks, workflows, processes, agents, approvals, incidents, contracts, data and assets.

### F03 — Universal Execution Contract
AI Employee, Skill, Signal→Action and Artifact Factory contracts exist, but a common execution contract connecting L0→L10 is still missing.

Required pattern:
Intent → Subject → Context → Preconditions → Authority → Plan → Actions → Observations → Verification → Outcome → Evidence → Cost → Learning.

### F04 — Enterprise Relationship / Graph Model
Entity, process, dependency, event, knowledge, decision, causal, resource and risk graphs are described separately but lack one canonical relationship model.

### F05 — Event Fabric Contract
Need canonical event identity, type, producer, entity/version, timestamp, payload/schema version, correlation/causation IDs, sensitivity, ordering, replay, retention and security semantics.

### F06 — Identity + Authority
Identity is broader than authentication/RBAC. Need identity, delegation, authority, object scope, policy, budget, risk, expiry, approval and revocation semantics.

### F07 — Task/Workflow Runtime
Catalogs describe tasks and workflows, but executable runtime contracts still need state, ownership, idempotency, retry, timeout, cancellation, compensation, replay, evidence, cost and human takeover.

### F08 — Universal Lifecycle
Multiple lifecycle concepts exist, but no single reusable lifecycle engine spans business, person, AI employee, agent, skill, tool, customer, supplier, contract, product, asset, knowledge, data, model, experiment, policy, obligation, decision, incident and company.

### F09 — Universal Evidence
Evidence is referenced throughout the architecture but needs one canonical evidence object covering source, timestamp, actor, action, result, provenance, integrity, retention and audit linkage.

### F10 — Decision Operating System
Decision concepts exist, but Decision ID, authority, evidence set, alternatives, assumptions, constraints, reversibility, approval, expected outcome and actual outcome need a canonical model.

### F11 — KPI Semantic Layer
KPIs are widely cataloged, but metric definitions, dimensions, formulas, source-of-truth, freshness, ownership, lineage and business meaning need one semantic contract.

### F12 — Company State + Digital Twin
Company State and Digital Twin are major architectural goals but are not yet complete schemas with synchronization, historical state, desired state, constraints, resources and simulation semantics.

### F13 — Simulation / Scenario Runtime
Scenario engine is identified, but scenario branching, assumptions, interventions, constraints, cost, risk, capacity and counterfactual evaluation need a common runtime.

### F14 — Causal Intelligence
Correlation, diagnosis and causal reasoning need explicit causal hypotheses, interventions, expected impact and measured impact.

### F15 — Business Builder Runtime
P00–P32 defines business lifecycle scope, but a Business Creation Instance is needed to track phase, gate, artifact, evidence, assumption, dependency, risk, budget, owner and reusable solution.

### F16 — Gate Contract
G0–G29 need executable entry criteria, required inputs/evidence, validation, decision rules, approver, remediation, exit criteria and audit evidence.

### F17 — Solution Registry
Reuse discovery is broad, but one canonical machine-readable Solution Registry is needed for resource, version/commit, license, provenance, dependencies, runtime, security, tests, evidence, cost, adaptation and verification status.

### F18 — Runtime Qualification
Current Wave 7/8 findings identify reproducible test entry points, but those are static findings. Actual isolated execution evidence is still required before promotion.

### F19 — Evaluation Framework
Need common evaluation semantics across atomic actions, tasks, workflows, processes, AI employees, managers, executives, control tower and autonomous company.

### F20 — Unified Observability
Need common trace/correlation semantics linking agent → manager → workflow → tool → API → model → data → decision → outcome.

### F21 — Cost / Budget Authority
FinOps exists conceptually, but universal cost attribution and autonomous spending authority limits need a canonical model.

### F22 — Failure / Recovery Object
Failure lifecycle exists conceptually, but failure, containment, diagnosis, recovery, compensation, CAPA, communication and learning need one object/contract.

### F23 — Self-Healing Safety Boundary
Self-healing requires explicit distinction between reversible, destructive, financial, security, data and customer-facing repairs plus rollback/escalation.

### F24 — Security / Supply Chain
Deeper runtime security is needed for agent sandboxing, browser/code execution, prompt injection, tool/MCP poisoning, data exfiltration, SBOM, signed artifacts and dependency vulnerabilities.

### F25 — Human Governance
Approval exists conceptually but needs a canonical approval request with risk, context, evidence, recommendation, human decision, reason, action and outcome.

### F26 — Multi-company / Group Model
Group, company, legal entity, brand, geography and shared services need canonical hierarchy plus intercompany and data-boundary semantics.

### F27 — Jurisdiction Engine
Country/state/entity/tax/employment/privacy/payment/licensing/data-residency rules need temporal validity and reusable jurisdiction contracts.

### F28 — Business Type Engine
“Any business idea” requires a Business Type Ontology and template engine mapping type → capabilities → departments → processes → legal → technology → workforce → KPIs → risks.

### F29 — Physical Operations Runtime
Physical businesses require machines, sensors, vehicles, warehouses, field workers, GPS, maintenance, inspection and safety interfaces.

### F30 — External Party Gateway
Customers, suppliers, partners, banks, government, investors, insurers and platforms need a common external-party abstraction.

### F31 — Data Deletion / Destruction
Retention, legal hold, archive, deletion, derived-data deletion, embedding/cache deletion and secure destruction need explicit lifecycle semantics.

### F32 — Change / Migration Engine
Schema, workflow, agent, skill, prompt, model, policy, connector and architecture versions need migration, compatibility, canary and rollback semantics.

### F33 — Deployment / Environment Model
Local, development, test, staging, production, DR and simulation environments need canonical boundaries and promotion rules.

### F34 — Backup / DR Contract
Backup verification, restore testing, RTO/RPO, failover/failback and coverage of memory, data, configuration, policies and audit evidence need formalization.

### F35 — Autonomy Authority Model
A0–A8 should be bound to authority, risk, reversibility, budget and approval requirements rather than only capability maturity.

### F36 — Learning Governance
Learning must be separated into knowledge, procedure, skill, prompt, policy, workflow, model and strategy learning, with evaluate → simulate → approve → canary → promote/rollback.

### F37 — Architecture Self-Evolution
Gap detection → solution discovery → qualification → simulation → approval → migration → verification → rollback needs an explicit architecture-evolution engine.

## Micro-level findings

### L0 Atomic
- idempotency
- preconditions/postconditions
- transaction boundary
- concurrency/locking
- timeout/cancellation
- compensation
- retry classification
- side-effect classification
- deterministic verification
- atomic evidence

### L1 Micro Task
- task state machine
- dependency graph
- ownership transfer
- lease
- SLA
- capability/resource requirement
- completion proof
- escalation
- cost
- evidence

### L2 Task Automation
- execution ID
- correlation ID
- trigger dedupe
- retry budget
- execution budget
- tool permission
- pause/resume
- replay
- DLQ
- manual takeover

### L3 Workflow
- workflow definition vs workflow instance
- node/edge state
- context
- compensation
- approval
- replay
- rollback
- version migration

### L4 Process
- process ownership
- capacity
- cost
- risk
- controls
- version migration
- simulation
- continuous improvement

### L5 Department
- department operating contract
- authority
- budget
- AI/human workforce boundary
- department state
- exception ownership
- service catalogue

### L6 Cross-department
- canonical shared objects
- master-data ownership
- obligation synchronization
- resource/capacity synchronization
- cross-department transaction boundaries

### L7 AI Manager
- manager runtime
- workload balancing
- capability matching
- delegation limits
- manager conflict resolution
- succession/replacement

### L8 Executive
- decision object
- evidence set
- alternatives
- scenario simulation
- capital allocation
- executive conflict resolution
- board escalation

### L9 Control Tower
- unified company graph
- state correlation
- causal model
- scenario engine
- resource optimizer
- command/stop/pause/resume/rollback semantics

### L10 Autonomous Company
- universal operating cycle
- bounded autonomy
- authority enforcement
- autonomous budgeting/procurement/hiring
- architecture evolution
- safe learning
- board/human governance
- transformation/exit readiness

## Cross-cutting audit problems

1. Markdown catalogs are strong for human navigation but are not sufficient as the canonical runtime registry.
2. Capability coverage, solution discovery, qualification and operational implementation must remain separate states.
3. Several “engines” are named but do not yet have canonical contracts.
4. Multiple catalogs can describe the same capability at different abstraction levels; cross-level traceability is required.
5. Every reusable asset needs source version, provenance and verification date.
6. Every autonomous action needs authority, policy, risk, budget and evidence.
7. Every state-changing operation needs verification and failure/compensation semantics.
8. Every production change needs versioning, canary and rollback semantics.
9. Every learning loop needs governance before production promotion.
10. The gap tracker itself needs dependency ordering so foundational gaps are solved before higher-level gaps.

## Audit conclusion

The current architecture has strong breadth, but the next work should focus on **foundational primitives and executable contracts**, not simply adding more agents/skills/workflows.

Recommended dependency order:

Universal Objects
→ Relationships
→ States
→ Identity
→ Authority/Policy
→ Events
→ Execution
→ Tasks/Workflows
→ Evidence
→ Decisions/KPIs
→ Company State
→ Digital Twin
→ Simulation/Causal
→ Business Builder Runtime
→ Solution Registry/Qualification Runtime
→ Control Tower
→ Autonomous Company
→ Architecture Self-Evolution.

No item in this audit is considered implemented merely because it is documented.
