# Master Reuse Implementation Roadmap

**Status:** v1.1 — 2026-09-16

## Objective

Convert the research warehouse into a working AI-native company operating system without rebuilding capabilities that already exist.

**Implementation principle:** reuse first; build only verified gaps.

## Phase 0 — Foundation and governance

**Goal:** make every future reuse decision traceable and controlled.

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

### Reusable infrastructure candidates

- MCP Gateway & Registry
- Preloop
- Airlock
- mcp-approvals
- OpenLIT / Phoenix / Future AGI / mcp-eval

### Exit criteria

Every adopted external asset has a source, access/license status, owner, destination, test result, permissions and approval requirement.

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

### HR

- Recruiting workflow
- Candidate screening
- Interview coordination
- Onboarding
- Performance-review preparation
- People reporting

### Controls

- AI drafts; authorized humans approve accounting entries and formal reports.
- No autonomous tax/audit/legal advice.
- HR access separated by role/data sensitivity.
- Material financial actions logged.

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

---

## Phase 6 — Executive Company OS

**Priority: P2 after revenue/delivery foundations**

### Executive cockpit inputs

- Sales pipeline
- Marketing performance
- Delivery status
- Customer health
- Finance
- People
- Product
- Operations
- Risks
- Strategic projects
- Agent health/cost
- Exceptions

### Outputs

- Daily exception brief
- Weekly company review
- Monthly operating review
- KPI variance analysis
- Decision briefs
- Priority changes
- Blocker escalation
- AI economics/ROI report

### Executive control loop

`Observe → Analyze → Identify Exceptions → Propose Actions → Human Decision → Assign → Execute → Verify → Learn`

---

## Phase 7 — Cross-department agent orchestration

Only after individual workflows are reliable.

### Target architecture

`Human Intent → Control/Router → Specialist Agents/Skills → Knowledge/Memory → MCP/API → Workflow → Approval → Action → Audit → Evaluation → Learning`

Agent-to-agent delegation must be scoped and observable; do not allow unrestricted autonomous delegation.

---

## Phase 8 — Resilience and company-wide optimization

**New cross-company completion layer**

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

1. Build registry schema.
2. Register existing discovered P0/P1 assets.
3. Select 5–10 revenue workflows.
4. Add one governed tool gateway.
5. Add one approval mechanism.
6. Add audit + trace logging.
7. Add evaluation/regression tests.
8. Add cost and exception tracking.
9. Pilot with synthetic + representative data.
10. Promote successful workflows into the canonical Company OS.

## Definition of done for discovery

Major functions, asset types and cross-company infrastructure are now represented. The project should transition from broad discovery to controlled reuse testing and implementation.
