# Master Reuse Implementation Roadmap

**Status:** v1.0 — 2026-09-16

## Objective

Convert the research warehouse into a working AI-native company operating system without rebuilding capabilities that already exist.

**Implementation principle:** reuse first; build only verified gaps.

## Phase 0 — Foundation and governance

**Goal:** make every future reuse decision traceable.

### Deliverables

- Master asset registry
- Standard asset metadata
- Source/license verification field
- Test-status field
- Adaptation/version history
- Human-approval policy
- Permission matrix
- Audit-log convention
- Production vs research separation

### Exit criteria

Every adopted external asset has a source, license/access status, owner, destination, test result and approval requirement.

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
- Opt-out and compliance handling explicit.

### Success evidence

Measure research time, qualified leads, reply rate, meeting rate, CRM completeness, human correction rate and workflow failure rate.

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

### Customer success

- Ticket triage
- Customer-context retrieval
- Escalation packaging
- Resolution summaries
- Knowledge-base article generation

Anthropic's current customer-support plugin follows a similar reusable pattern: ticket triage, response drafting, escalation, customer-context research and conversion of resolved cases into knowledge assets. citeturn0search2turn0search3

### Controls

Customer-facing messages remain reviewable until quality is demonstrated. Sensitive customer data must use least-privilege connectors.

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
- HR access separated by role and data sensitivity.
- Material financial actions logged.

---

## Phase 4 — Governance + Knowledge

**Priority: P1/P2**

### Knowledge layer

- Enterprise search
- Source registry
- SOP library
- Decision records
- Company terminology
- Reusable skills
- Research provenance

### Governance layer

- Contract review
- NDA triage
- Compliance tracking
- Risk identification
- AI governance
- Approval routing

### Architecture

`Question → Enterprise Search → Source Evidence → Skill/Agent → Draft → Human Review → Approved Knowledge/Action`

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

Anthropic's current plugin architecture explicitly separates skills, commands and connectors, and its marketplace includes product-management and data workflows alongside sales, marketing, finance, legal and other functions. citeturn0search0turn0search7

---

## Phase 6 — Executive Company OS

**Priority: P2 after revenue/delivery foundations**

### Executive cockpit

Inputs:

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

Outputs:

- Daily exception brief
- Weekly company review
- Monthly operating review
- KPI variance analysis
- Decision briefs
- Priority changes
- Blocker escalation

### Executive control loop

`Observe → Analyze → Identify Exceptions → Propose Actions → Human Decision → Assign → Execute → Verify → Learn`

---

## Phase 7 — Cross-department agent orchestration

Only after individual workflows are reliable.

### Target architecture

```text
                    ┌──────────────────────┐
                    │   HUMAN / EXECUTIVE  │
                    └──────────┬───────────┘
                               │
                      Approval / Intent
                               │
                    ┌──────────▼───────────┐
                    │   ROUTER / CONTROL   │
                    └──────────┬───────────┘
                               │
       ┌──────────────┬────────┼────────┬──────────────┐
       ▼              ▼        ▼        ▼              ▼
     SALES         MARKET     OPS     FINANCE          HR
       │              │        │        │              │
       └──────────────┴────────┼────────┴──────────────┘
                               │
                    ┌──────────▼───────────┐
                    │ KNOWLEDGE / DATA     │
                    │ CRM / ERP / Notion   │
                    │ GitHub / BI / Email  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ WORKFLOW AUTOMATION  │
                    │       n8n / MCP      │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ APPROVAL + AUDIT     │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ SYSTEMS OF RECORD    │
                    └──────────────────────┘
```

## Reuse-before-build decision gate

For every requested capability:

### Gate 1 — Does an existing asset exist?

Search:

- official vendor/plugin repositories
- GitHub
- MCP/connector ecosystems
- skill libraries
- agent marketplaces
- workflow libraries
- SOP/process libraries
- templates/playbooks
- commercial solutions

### Gate 2 — Can it legally and technically be reused?

Check:

- license/access
- dependencies
- connector compatibility
- security/privacy
- maintenance
- data residency requirements
- permissions
- output quality

### Gate 3 — Can it meet Nivy requirements after adaptation?

Test:

- synthetic inputs
- representative workflow
- edge cases
- human correction rate
- failure modes
- latency/cost
- auditability

### Gate 4 — Integrate or build?

**Reuse** if adequate.

**Adapt** if the core capability works but terminology, schema, policy or connector needs modification.

**Compose** if several existing capabilities can be chained.

**Build** only when a material gap remains.

## Implementation backlog structure

Each production candidate should become a tracked record with:

| Field | Required |
|---|---|
| Capability | Yes |
| Source asset | Yes |
| Source URL | Yes |
| License/access | Yes |
| Nivy workflow | Yes |
| Inputs | Yes |
| Outputs | Yes |
| Connectors | Yes |
| Permissions | Yes |
| Approval gate | Yes |
| Test dataset | Yes |
| Quality metric | Yes |
| Owner | Yes |
| Status | Yes |
| Version | Yes |
| Last tested | Yes |
| Failure notes | When applicable |

## Recommended execution order

**Now:**

1. Build the master registry.
2. Select the first 5–10 P0 revenue workflows.
3. Test the original reusable assets.
4. Adapt only where required.
5. Connect to the CRM and communication layer.
6. Add approval/audit gates.
7. Run a controlled pilot.
8. Measure results.
9. Promote successful workflows into the canonical Company OS.

**After P0 proves reliable:** move to client delivery/operations, then finance/HR, then governance/knowledge, then product/data/technology, and finally cross-department executive orchestration.

## Important architectural principle

Do not create one giant autonomous agent.

Use a **composition model**:

`Router + Specialist Skills/Agents + Workflows + Connectors + Knowledge + Approval + Audit + Systems of Record`

This matches the current reusable-plugin pattern documented by Anthropic, where skills, commands, connectors and sub-agents are modular components that can be customized to company processes. citeturn0search0turn0search1

## Definition of done for this research phase

The research phase is complete when:

- major company functions have reusable-source coverage;
- assets have been classified;
- adoption priorities exist;
- cross-department composition is defined;
- source/provenance requirements are explicit;
- implementation gates are defined;
- the next work is execution/testing rather than more generic planning.

**At this point, the project should transition from broad discovery to controlled reuse testing.**
