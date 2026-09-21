# Production Readiness Backlog

**Status:** v1.0 — 2026-09-16

## Purpose

The remaining work is now implementation and verification, not broad discovery.

## P0 — Required before serious autonomous production use

| Work item | Required outcome |
|---|---|
| Master asset registry | Every adopted asset has owner, source, license, destination and status |
| Agent identity | Every production agent has a unique identity |
| Tool registry | Every callable tool/MCP has owner, schema, permissions and lifecycle |
| Least privilege | Agents only receive required capabilities |
| Approval policy | High-impact actions have explicit approval gates |
| Audit trail | Agent/user/tool/action/outcome/evidence is reconstructable |
| Secrets management | No production credentials in prompts/repos |
| Workflow idempotency | Retries cannot create duplicate financial/customer actions |
| Exception queue | Failed/blocked workflows reach a human owner |
| Kill switch/quarantine | Any agent/tool can be disabled rapidly |
| Evaluation suite | Production workflows have repeatable tests |
| Cost ledger | Model/tool/workflow usage and cost are measurable |
| Backup/restore | Critical data/configuration can be restored |
| Production/research separation | Experimental assets cannot silently affect production |

## P0 — First workflows

### Revenue

- Lead intake and normalization
- Account research
- Qualification/scoring
- Outreach drafting
- Follow-up task creation
- Meeting preparation
- Meeting debrief → CRM update
- Pipeline review

### Marketing

- Market/competitor research
- Content brief generation
- Content production workflow
- SEO audit/report
- Campaign reporting

### Delivery

- Won-deal handoff
- Client intake
- Project/task creation
- Status reporting
- Client update drafting

## P1 — Scale the company

- Finance close/reconciliation assistance
- Treasury dashboard
- Workforce onboarding
- KRA/KPI and goal cascade
- Performance evidence collection
- ITSM
- Contract intake/review
- Risk/control register
- Internal audit workflow
- Customer health/QBR
- Procurement/vendor workflow
- Knowledge freshness
- Process mining

## P1 — Enterprise depth

- Corporate secretary/board workflow
- Entity/subsidiary registry
- M&A workflow
- Revenue assurance
- ESG reporting
- Global tax control tower
- SaaS/application portfolio
- QMS/CAPA
- Supply-risk control tower
- Transformation portfolio
- Investor-relations workflow

## P2 — Advanced resilience and optimization

- Multi-provider model routing/failover
- Connector failover
- Regional/data-residency architecture
- Advanced process simulation
- Automated benefits realization
- Crisis command center
- Advanced risk stress testing
- Autonomous cross-agent delegation with bounded permissions

## Test gates

### Gate A — Functional

Does the workflow produce the expected output for normal, edge and invalid inputs?

### Gate B — Control

Are identity, permissions, approval, data boundaries and audit evidence correct?

### Gate C — Operational

Are retries, timeouts, failures, human escalation and rollback correct?

### Gate D — Economic

Is latency, token/tool usage and operating cost acceptable?

### Gate E — Production

Has a controlled pilot succeeded with representative data and an explicit owner?

## Definition of done

A workflow is production-ready only when:

`Functional Pass + Control Pass + Operational Pass + Economic Pass + Owner + Audit + Rollback + Pilot Pass`

## Final discovery rule

If a backlog item cannot be fulfilled by an existing reusable asset after verification/adaptation/composition, only then create a **BUILD GAP**. Every BUILD GAP must document why reuse failed and what minimum new component is required.
