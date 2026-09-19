# Master Reuse Implementation Roadmap

**Status:** v1.6 — 2026-09-16

## Objective

Convert the research warehouse into a working AI-native company operating system without rebuilding capabilities that already exist.

**Implementation principle:** reuse first; build only verified gaps.

## Phase 0 — Foundation and governance

**Goal:** make every future reuse decision traceable and controlled.

### Execution files

- **77** — Master Automation & Implementation Registry
- **78** — Automation Coverage Matrix
- **79** — Integration & Connector Registry
- **80** — Production Readiness Backlog
- **81** — Automation Foundation Implementation Plan
- **82** — P0 Workflow Implementation Specifications
- **83** — Agent Control Plane Implementation Specification
- **84** — Automation Test & Evaluation Suite
- **85** — Scale & Country Activation Runbook

### Deliverables

- Master asset registry
- Agent/skill/MCP/workflow registry
- Source/license verification
- Permission matrix
- Identity mapping: human → agent → tool
- Human-approval policy
- Policy-as-code candidates
- Audit-log convention
- Agent observability/evaluation
- AI cost ledger
- Exception queue
- Production vs research separation

### Exit criteria

Every adopted external asset has a source, access/license status, owner, destination, test result, permissions and approval requirement.

---

## Phase 0.5 — Targeted international-company completeness research

**Completed:** targeted research and comparison are documented in 69–76.

**Discovery exit achieved.** No further generic enterprise-function expansion is required unless testing exposes a genuine gap.

---

## Phase 0.6 — Candidate verification and integration

**Priority: P0/P1**

1. Verify license/access.
2. Verify maintenance/activity and dependencies.
3. Security/privacy review.
4. Create synthetic test datasets.
5. Test representative workflows.
6. Measure human correction rate.
7. Test permissions/approval gates.
8. Test auditability/evidence capture.
9. Normalize schemas.
10. Integrate with the intended system of record.
11. Pilot before production.

Candidate queue: LQGovernance-OpenBoard, Tessio, FreeITSM, security-atlas, riskready-community, sustainability-project, Rapo, revenue_leakage_system, treasury/finance skills, corporate legal skills, EIOS/entity architecture.

---

## Phase 0.7 — Integration fabric and control plane

Implement:

`CRM ↔ Email ↔ Calendar ↔ Messaging ↔ Accounting ↔ ERP ↔ HR ↔ Helpdesk ↔ Projects ↔ GitHub ↔ Knowledge ↔ Analytics ↔ AI runtime`

and:

`Agent Identity → Registry → Tool Registry → Policy → Router → Approval → A2A → Observability → Evaluation → Cost → Exceptions → Kill Switch`

Design rules: one system of record per object, stable IDs/correlation IDs, API/webhook/MCP-first, idempotent writes, least privilege, approval for high-impact actions, audit/evidence capture, retry/timeout/dead-letter handling, and manual fallback.

---

## Phase 0.8 — Production readiness

Every workflow must pass:

`Functional + Control + Operational + Economic + Pilot`

Required: secrets management, identity, least privilege, approvals, audit, exception handling, rollback/manual fallback, cost limits, regression tests, backup/restore, quarantine/kill switch, owner and escalation path.

---

## Phase 1 — Revenue Engine

**Priority: P0**

### P0 workflows

1. Lead intake and normalization
2. Account research
3. Qualification/scoring
4. Outreach drafting
5. Follow-up task creation
6. Meeting preparation
7. Meeting debrief → CRM update
8. Pipeline review
9. Won-deal handoff
10. Client intake/status reporting

### Marketing

- Market/competitor research
- Positioning/messaging
- Campaign planning
- Content production
- SEO audit
- Email sequences
- Campaign reporting

### Architecture

`Research → Qualification → CRM → Outreach Draft → Human Approval → Send → Response Capture → Follow-up → Meeting → Debrief → Pipeline`

### Controls

- No unrestricted bulk outbound at first.
- No invented service/pricing claims.
- Human approval for external messaging during pilot.
- CRM writes logged.
- Opt-out/compliance handling explicit.

---

## Phase 2 — Client Delivery + Operations

**Priority: P1**

`Won Deal → Handoff → Intake → Data Collection → Scope Confirmation → Kickoff → Delivery Plan → Status Updates`

Capabilities: SOP/runbook generation, status reporting, capacity planning, vendors, change management, exception management, ticket triage, customer context, escalation, knowledge capture and QBR/health workflows.

---

## Phase 3 — Finance + People

**Priority: P1**

Finance: invoice follow-up, cash-flow snapshot, reconciliation, month-end preparation, journal-entry drafting, statements, variance and margin analysis.

Treasury: bank/account registry, cash position, liquidity forecast, payment proposal/approval, banking relationships, FX exposure, debt calendar, working capital and treasury policy checks.

HR/workforce: recruiting, onboarding, employee/role registry, responsibilities, KRA/KPI, goal cascade, daily work, manager/department cockpits, performance evidence, skills, learning, workload, accountability and workforce analytics.

---

## Phase 4 — Governance + Knowledge

**Priority: P0/P1**

Knowledge: enterprise search, source/evidence registry, SOPs, decisions, terminology, reusable skills, provenance and freshness.

Governance: contracts, compliance, risk, AI governance, approvals, agent/tool registry, audit and evaluation.

Corporate governance: entity/subsidiary registry, board/committee workflows, resolutions/votes, officers, calendars, statutory deadlines and stakeholder documents.

Internal audit:

`Risk → Control → Audit Plan → Evidence Request → Evidence → Test → Finding → Remediation → Retest → Assurance Report`

Memory layers: `Source | Company | Workflow State | Decision | Agent | Evaluation`.

---

## Phase 5 — Product + Data + Technology

**Priority: P2**

Product: research, requirements, roadmap, feedback, innovation portfolio.

Data: SQL, quality validation, analysis, dashboards, metric interpretation.

Engineering/IT: issue triage, documentation, technical research, code/task assistance, incident/runbooks, ITSM, application portfolio, SaaS lifecycle, architecture and standards.

Quality: QMS, CAPA, nonconformance, audits, SLA monitoring.

---

## Phase 6 — Executive Company OS

**Priority: P2 after revenue/delivery foundations**

Inputs: sales, marketing, delivery, customer, finance, treasury, people, product, operations, risk, strategic projects, agent health/cost, exceptions, governance/IR, transformation, ESG and resilience.

Control loop:

`Observe → Analyze → Identify Exceptions → Propose Actions → Human Decision → Assign → Execute → Verify → Learn`

---

## Phase 7 — Cross-department agent orchestration

Only after individual workflows are reliable:

`Human Intent → Control/Router → Specialist Agents/Skills → Knowledge/Memory → MCP/API → Workflow → Approval → Action → Audit → Evaluation → Learning`

Agent-to-agent delegation must be scoped and observable.

---

## Phase 8 — Resilience and company-wide optimization

- Model/provider failover
- Connector failover
- Backup/restore tests
- Degraded-mode runbooks
- Business continuity
- Agent quarantine/kill switch
- Cost optimization
- Capacity planning
- Process simulation
- Continuous improvement
- Regression suite for all production agents

---

## Reuse-before-build decision gate

### Gate 1 — Existing asset?
Search official vendor/plugin repositories, GitHub, MCP/connector ecosystems, skill libraries, agent marketplaces, workflow libraries, SOP/process libraries, templates/playbooks and commercial solutions.

### Gate 2 — Legally and technically reusable?
Check license/access, dependencies, connector compatibility, security/privacy, maintenance, data residency, permissions and output quality.

### Gate 3 — Adequate after adaptation?
Test synthetic inputs, representative workflows, edge cases, correction rate, failure modes, latency/cost and auditability.

### Gate 4 — Integrate or build?
**Reuse** if adequate. **Adapt** if schema/policy/connector differs. **Compose** if multiple assets can be chained. **Build** only for a material gap.

## Immediate execution order

1. Run the foundation plan in **81**.
2. Implement and test the first P0 workflows in **82**.
3. Establish the control-plane minimum in **83**.
4. Apply the evaluation suite in **84**.
5. Activate scale/country controls using **85**.
6. Promote only workflows that pass production gates.

## Definition of done for discovery

**Achieved:** the ideal international-company capability model has been compared against the reuse library, material P0/P1 gaps have been researched, scale coverage has been mapped, and remaining work is classified as verification, integration, productionization, jurisdictional adaptation, resilience or genuine build gaps.

**Default mode:** `VERIFY → TEST → SELECT → ADAPT → INTEGRATE → PILOT → PRODUCTION`.
