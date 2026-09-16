# Master Reuse Implementation Roadmap

**Status:** v1.5 — 2026-09-16

## Objective

Convert the research warehouse into a working AI-native company operating system without rebuilding capabilities that already exist.

**Implementation principle:** reuse first; build only verified gaps.

## Phase 0 — Foundation and governance

**Goal:** make every future reuse decision traceable and controlled.

### Deliverables

- Master asset registry — **file 77**
- Automation coverage matrix — **file 78**
- Integration/connector registry — **file 79**
- Production readiness backlog — **file 80**
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

### Reusable infrastructure candidates

- MCP Gateway & Registry
- Preloop
- Airlock
- mcp-approvals
- OpenLIT / Phoenix / Future AGI / mcp-eval

### Exit criteria

Every adopted external asset has a source, access/license status, owner, destination, test result, permissions and approval requirement.

---

## Phase 0.5 — Targeted international-company completeness research

**Completed:** targeted research and comparison are now documented in 69–76.

Source control files:

- **69** — International company completeness audit
- **70** — Missing capability research backlog
- **71** — Ideal company vs Nivy coverage matrix
- **72** — Targeted gap research and reusable candidates
- **73** — Targeted gap adoption map
- **74** — Ideal international company capability model
- **75** — Final enterprise completeness audit
- **76** — Company scale and maturity matrix

### Exit status

**Discovery exit achieved.** No further generic enterprise-function expansion is required. New discovery should be triggered only by a new capability, jurisdiction, industry requirement, obsolete candidate or material implementation gap.

---

## Phase 0.6 — Targeted gap verification and integration

**Priority: P0/P1**

This is the immediate execution phase after completeness research.

### Work packages

1. Verify candidate licenses/access.
2. Verify maintenance/activity and dependencies.
3. Security/privacy review.
4. Create synthetic test datasets.
5. Test representative workflows.
6. Measure human correction rate.
7. Test permissions/approval gates.
8. Test auditability and evidence capture.
9. Normalize schemas.
10. Integrate with the intended system of record.
11. Pilot before production adoption.

### Candidate verification queue

- LQGovernance-OpenBoard
- Tessio
- FreeITSM
- security-atlas
- riskready-community
- sustainability-project
- Rapo
- revenue_leakage_system
- treasury/finance skill candidates
- corporate legal skills
- EIOS/entity architecture

---

## Phase 0.7 — Integration fabric and control plane

**This phase is now explicitly required before broad production scaling.**

### Integration fabric

Implement the governed connection layer:

`CRM ↔ Email ↔ Calendar ↔ Messaging ↔ Accounting ↔ ERP ↔ HR ↔ Helpdesk ↔ Projects ↔ GitHub ↔ Knowledge ↔ Analytics ↔ AI runtime`

Rules:

- one system of record per business object
- stable IDs/correlation IDs
- API/webhook/MCP-first
- idempotent writes
- least privilege
- approval gates for high-impact actions
- audit/evidence capture
- retries/timeouts/dead-letter handling
- manual fallback for critical processes

### AI control plane

Implement:

`Agent Identity → Registry → Tool Registry → Policy → Router → Approval → A2A → Observability → Evaluation → Cost → Exceptions → Kill Switch`

The control layer must be separate from individual agent implementations so agents can be replaced without losing governance.

---

## Phase 0.8 — Production readiness

Before production promotion, every workflow must pass:

`Functional + Control + Operational + Economic + Pilot`

Required controls:

- secrets management
- identity and least privilege
- approval policy
- audit trail
- exception queue
- rollback/manual fallback
- cost limits
- evaluation/regression suite
- backup/restore
- quarantine/kill switch
- owner and escalation path

---

## Phase 1 — Revenue Engine

**Priority: P0**

### Sales

1. ICP builder
2. Account research
3. Lead discovery
4. Lead qualification/scoring
5. Personalized outreach drafting
6. Follow-up sequencing
7. Discovery-call preparation
8. Call debrief and CRM update
9. Pipeline review
10. Forecast preparation

### Marketing

1. Market/competitor research
2. Positioning and messaging
3. Campaign planning
4. Content strategy
5. Content production
6. SEO research/audit
7. Email sequences
8. Campaign reporting

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

### Customer onboarding

`Won Deal → Handoff → Intake → Data Collection → Scope Confirmation → Kickoff → Delivery Plan → Status Updates`

### Operations

- SOP generation
- Runbook generation
- Status reporting
- Capacity planning
- Vendor workflows
- Change management
- Exception management
- Process mining before major automation

### Customer success

- Ticket triage
- Customer-context retrieval
- Escalation packaging
- Resolution summaries
- Knowledge-base article generation
- Health/QBR workflows

---

## Phase 3 — Finance + People

**Priority: P1**

### Finance

- Invoice follow-up
- Cash-flow snapshot
- Reconciliation
- Month-end preparation
- Journal-entry drafting
- Financial-statement preparation
- Variance analysis
- Margin analysis

### Treasury / corporate finance extension

- Bank/account registry
- Cash-position aggregation
- Liquidity forecast
- Payment proposal/approval
- Banking relationship management
- FX exposure monitoring
- Debt/financing calendar
- Working-capital analytics
- Treasury policy checks

### HR / Workforce

- Recruiting workflow
- Candidate screening
- Interview coordination
- Onboarding
- Employee/department/role registry
- Role responsibilities and job-purpose definitions
- KRA/KPI design and target management
- Company → department → team → employee goal cascade
- Daily/weekly/monthly work planning
- Employee work cockpit
- Manager team cockpit
- Department-head cockpit
- Performance evidence and review preparation
- Skills matrix and gap analysis
- Learning/development plans
- Workload/capacity monitoring
- Accountability and exception workflows
- Employee/manager AI copilots
- Workforce analytics

---

## Phase 4 — Governance + Knowledge

**Priority: P0/P1**

### Knowledge layer

- Enterprise search
- Source registry
- Evidence registry
- SOP library
- Decision records
- Company terminology
- Reusable skills
- Research provenance
- Knowledge freshness/review

### Governance layer

- Contract review
- NDA triage
- Compliance tracking
- Risk identification
- AI governance
- Approval routing
- Agent registry
- Tool permissions
- Audit
- Evaluation

### Corporate governance extension

- Entity/subsidiary registry
- Board/committee registry
- Meeting/agenda/minutes workflow
- Resolution/vote records
- Director/officer records
- Corporate calendar
- Statutory filing/deadline tracking
- Investor/stakeholder document workflow

### Internal audit extension

`Risk → Control → Audit Plan → Evidence Request → Evidence → Test → Finding → Remediation → Retest → Assurance Report`

### Memory architecture

Separate:

`Source Memory | Company Memory | Workflow State | Decision Memory | Agent Memory | Evaluation Memory`

---

## Phase 5 — Product + Data + Technology

**Priority: P2**

### Product

- User-research synthesis
- Product requirements/specs
- Roadmap support
- Competitive intelligence
- Feedback analysis
- Innovation portfolio

### Data

- SQL generation
- Data quality validation
- Statistical analysis
- Dashboard preparation
- Metric interpretation

### Engineering / IT

- Issue triage
- Documentation
- Technical research
- Code/task assistance
- Incident/runbook support
- ITSM
- Application portfolio
- SaaS inventory/lifecycle
- Architecture decisions
- Technology standards

### Quality

- QMS
- CAPA
- Nonconformance
- Quality audit
- SLA monitoring

---

## Phase 6 — Executive Company OS

**Priority: P2 after revenue/delivery foundations**

### Executive cockpit inputs

- Sales pipeline
- Marketing performance
- Delivery status
- Customer health
- Finance
- Treasury/liquidity
- People / workforce
- Product
- Operations
- Risks
- Strategic projects
- Agent health/cost
- Exceptions
- Corporate governance/IR signals
- Transformation portfolio
- ESG signals
- Resilience status

### Outputs

- Daily exception brief
- Weekly company review
- Monthly operating review
- KPI variance analysis
- Decision briefs
- Priority changes
- Blocker escalation
- Workforce health report
- AI economics/ROI report
- Transformation portfolio report
- Enterprise risk/resilience brief

### Executive control loop

`Observe → Analyze → Identify Exceptions → Propose Actions → Human Decision → Assign → Execute → Verify → Learn`

---

## Phase 7 — Cross-department agent orchestration

Only after individual workflows are reliable.

`Human Intent → Control/Router → Specialist Agents/Skills → Knowledge/Memory → MCP/API → Workflow → Approval → Action → Audit → Evaluation → Learning`

Agent-to-agent delegation must be scoped and observable; do not allow unrestricted autonomous delegation.

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
- Continuous improvement loops
- Regression suite for all production agents

---

## Reuse-before-build decision gate

### Gate 1 — Does an existing asset exist?

Search official vendor/plugin repositories, GitHub, MCP/connector ecosystems, skill libraries, agent marketplaces, workflow libraries, SOP/process libraries, templates/playbooks and commercial solutions.

### Gate 2 — Can it legally and technically be reused?

Check license/access, dependencies, connector compatibility, security/privacy, maintenance, data residency, permissions and output quality.

### Gate 3 — Can it meet Nivy requirements after adaptation?

Test synthetic inputs, representative workflows, edge cases, human correction rate, failure modes, latency/cost and auditability.

### Gate 4 — Integrate or build?

**Reuse** if adequate. **Adapt** if the core works but schema/policy/connector differs. **Compose** if several assets can be chained. **Build** only for a material gap.

## Immediate execution order

1. Use files 77–80 as the execution control layer.
2. Verify the highest-priority candidate set.
3. Establish the connector/integration inventory.
4. Establish agent/tool identity and permissions.
5. Implement one approval mechanism and unified audit convention.
6. Select 5–10 revenue workflows.
7. Add evaluation/regression tests.
8. Add cost and exception tracking.
9. Pilot with synthetic + representative data.
10. Promote successful workflows into the canonical Company OS.

## Definition of done for discovery

**Achieved:** the ideal international-company capability model has been compared against the reuse library, material P0/P1 gaps have been researched, scale coverage has been mapped, and remaining work is explicitly classified as verification, integration, productionization, jurisdictional adaptation, resilience or genuine build gaps.

From this point, the default operating mode is controlled reuse testing and implementation.
