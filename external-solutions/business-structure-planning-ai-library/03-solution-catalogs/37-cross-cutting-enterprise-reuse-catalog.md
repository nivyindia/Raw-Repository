# Cross-Cutting Enterprise Reuse Catalog

**Research date:** 2026-09-16
**Purpose:** Execute the missing cross-cutting layers identified after the 36-area international-company checklist.

## Reuse rule

`DISCOVER → LICENSE/CHECK ACCESS → INSPECT → TEST UNCHANGED → ADAPT → APPROVE → INTEGRATE → MONITOR`

This file is a discovery catalog, not a production approval list. Verify current license, security, maintenance, dependencies and commercial terms before adoption.

## 1. Enterprise architecture / capability / value-stream modeling

| Asset | Reusable value | Access | Source |
|---|---|---|---|
| Archie EA | Open-source web EA, ArchiMate 3.2, TOGAF-aligned workflow, capability map, application portfolio, value streams, architecture governance | AGPL-3.0; self-hostable; commercial license available | https://github.com/Anioko/archie-ea |
| Turbo EA | Open-source self-hosted EA platform with embedded BPM, configurable metamodel, strategy-to-infrastructure mapping | Open source; verify repository license before production | https://www.turbo-ea.org/ |
| Enterprise Architecture Reference Catalog | 9,697 capabilities, 1,321 processes, 65 value streams; machine-readable JSON APIs | Free/open-source catalog | https://capabilities.turbo-ea.org/ |

**Nivy reuse pattern:** Use capability IDs and value streams as the master index linking departments, processes, systems, agents and KPIs.

## 2. Business Process Management

Reusable process structure:

`Trigger → Customer/Business Outcome → Inputs → Activities → Decisions → Roles → Systems → Controls → Outputs → KPI → Exception → Improvement`

Reusable artifacts to search/adapt:
- BPMN process models
- SIPOC
- RACI
- process inventory
- process owner register
- process maturity assessment
- value-stream maps
- process-mining event logs
- SOP/runbook templates
- exception and escalation matrices

Recommended open standards/tools to investigate:
- BPMN 2.0
- Camunda ecosystem
- OpenTelemetry for execution traces
- OpenLineage for data/process lineage

## 3. End-to-end value streams

Create reusable Nivy value-stream maps for:

1. Lead → Cash
2. Quote → Contract
3. Contract → Onboarding
4. Onboarding → Delivery
5. Delivery → QA → Acceptance
6. Support → Renewal
7. Renewal → Expansion → Referral
8. Procure → Pay
9. Hire → Retire
10. Idea → Product → Launch
11. Incident → Recovery → Postmortem
12. Research → Decision → Implementation

For every value stream store: stages, owner, inputs, outputs, systems, agents, human approvals, KPIs, risks and reusable assets.

## 4. Master data management

Reusable master entities:
- Company
- Contact
- Account
- Lead
- Opportunity
- Customer
- Vendor
- Partner
- Employee
- Product
- Service
- Location
- Contract
- Invoice
- Project
- Document
- Asset

Required metadata: `unique_id, source, owner, status, created_at, updated_at, confidence, sensitivity, lifecycle_state, canonical_source`.

## 5. Identity and access management

Reusable control model:

`Person/Agent → Identity → Role → Permission → Resource → Action → Approval → Audit`

Open-source candidate:
- ZITADEL — SSO, MFA, passkeys, OIDC, SAML, SCIM and multi-tenancy. https://github.com/zitadel/zitadel

Also investigate Keycloak and Authentik as alternatives before architecture commitment.

## 6. AI governance / AgentOps

High-value reusable candidates:

| Asset | Reusable value | Source |
|---|---|---|
| SAFi | Runtime agent/tool governance, policy enforcement, permissions, audit trail and human supervision | https://github.com/jnamaya/SAFi |
| Open Enterprise AgentOps Mesh | Agent registry, evaluation lab, governance gates, evidence vault, policy guardrails, trace ledger, connector sandbox | https://github.com/annapurnaagenticsolutions/open-enterprise-agentops-mesh |
| Alignment Governance Stack | Reference architecture for delegated AI authority, policy, evaluation, receipts and governance memory | https://github.com/mnbower-research/alignment-governance-stack |
| PALO Framework | Operational AI governance lifecycle, agentic authority, policy enforcement and assurance | https://github.com/sev7enITA/PALOframework |
| OGAC | Source-available private enterprise AI control plane combining gateway, evals, guardrails, PII, lineage, knowledge and audit | https://github.com/off-grid-ai/OGAC |

**Nivy minimum agent manifest:**

```yaml
agent_id:
name:
owner:
department:
mission:
inputs: []
outputs: []
allowed_tools: []
data_classes: []
max_autonomy: draft|recommend|execute-with-approval|execute
approval_required_for: []
model_policy:
knowledge_sources: []
evaluation_suite: []
logging:
rollback:
version:
status: experimental|approved|production|retired
```

## 7. Data governance / metadata / lineage

| Asset | Reusable value | Source |
|---|---|---|
| OpenMetadata | Catalog, governance, lineage, quality, ownership, glossary, data contracts, memory, MCP/API access | https://github.com/open-metadata/OpenMetadata |
| OpenLineage | Open standard for run/job/dataset lineage metadata | https://github.com/OpenLineage/OpenLineage |
| DataHub | Open-source data catalog, discovery, lineage and governance reference | https://github.com/datahub-project/datahub |
| Awesome Data Catalogs | Discovery index for catalogs, governance and observability platforms | https://github.com/opendatadiscovery/awesome-data-catalogs |

**Nivy data-asset minimum record:** owner, definition, source, sensitivity, freshness, quality score, lineage, allowed users/agents, retention, downstream dependencies.

## 8. AI/data evaluation and testing

| Asset | Reusable value | Source |
|---|---|---|
| AgentGovBench | 48 governance scenarios covering identity, policy enforcement and observability | MIT; https://github.com/agentic-control-plane/agentgovbench |
| proofagent-harness | Adversarial multi-turn evaluation, artifact evaluation, context assessment, compliance/governance gates and CI integration | Open source; https://github.com/ProofAgent-ai/proofagent-harness |
| Awesome AI Agent Evaluation | Curated discovery list for eval, acceptance gates, observability and red teaming | https://github.com/SeaOtterAI/awesome-ai-agent-evaluation |

**Reusable evaluation pipeline:**

`Golden set → Unit tests → Tool/permission tests → Adversarial tests → Quality scoring → Cost/latency → Human review → Release gate → Regression suite → Production monitoring`

## 9. ITSM / service operations

Reusable lifecycle:

`Request → Triage → Priority → Assignment → Work → Verification → Resolution → Knowledge Capture → Metrics`

Search/reuse categories:
- incident management
- problem management
- change management
- service request management
- SLA management
- asset/configuration management
- service catalog
- postmortems
- on-call/runbooks

Candidate ecosystems: GLPI, Zammad, osTicket, iTop, ERP/CRM service modules. Verify current licenses and feature fit before adoption.

## 10. Business continuity / disaster recovery

Reusable lifecycle:

`Business Impact Analysis → Criticality → RTO/RPO → Dependencies → Backup → Restore Test → Failover → Crisis Communication → Recovery → Postmortem`

Reusable documents:
- BIA template
- business continuity plan
- disaster recovery plan
- backup policy
- restore test procedure
- emergency contact tree
- vendor outage plan
- crisis communications plan
- recovery evidence log

Example reusable open document source: backup/recovery procedure in `jposluns/grc_library`, CC BY-SA 4.0. https://github.com/jposluns/grc_library

## 11. Vendor / software / license management

Reusable lifecycle:

`Discover → Security/Due Diligence → License Check → Cost → Contract → Approval → Procurement → Integration → Review → Renewal/Exit`

Minimum vendor record:
- vendor
- product
- owner
- purpose
- data accessed
- permissions
- license
- cost
- renewal date
- security review
- DPA/contract status
- alternatives
- exit plan

## 12. Financial technology / payments

Search/reuse categories:
- payment gateway
- invoicing
- subscription billing
- collections
- reconciliation
- expense management
- FX
- international payouts
- tax calculation
- payment webhooks
- fraud/risk controls

Architecture pattern:
`Order/Contract → Invoice → Payment Request → Gateway → Webhook → Ledger/ERP → Reconciliation → Customer Receipt`

## 13. Records / document lifecycle

`Create → Classify → Review → Approve → Version → Publish → Use → Retain → Archive → Dispose`

Every document should have: owner, document type, version, status, effective date, review date, source, confidentiality, retention class and superseded-by link.

## 14. Change management / adoption

Reusable change package:
- change impact assessment
- stakeholder map
- communications plan
- training plan
- pilot
- rollout checklist
- adoption KPI
- support plan
- feedback loop
- rollback plan

## 15. Performance management / continuous improvement

Reusable hierarchy:

`Objective → Outcome → KPI → Target → Actual → Variance → Root Cause → Action → Owner → Due Date → Verification`

Methods to search/reuse:
- OKRs
- KPI trees
- balanced scorecards
- SLA dashboards
- process maturity models
- PDCA
- DMAIC
- A3 problem solving
- retrospectives
- postmortems
- benchmarking

## Cross-cutting Nivy architecture

```text
STRATEGY / OUTCOMES
        ↓
CAPABILITIES
        ↓
VALUE STREAMS
        ↓
PROCESSES
        ↓
SYSTEMS / APPLICATIONS
        ↓
AGENTS / SKILLS / WORKFLOWS
        ↓
DATA + KNOWLEDGE + CONNECTORS
        ↓
EVALUATION + GOVERNANCE + HUMAN APPROVAL
        ↓
EXECUTION / SYSTEM OF RECORD
        ↓
KPI / OBSERVABILITY / CONTINUOUS IMPROVEMENT
```

This layer should sit above the 36 business capability areas and provide common governance rather than becoming another disconnected department.
