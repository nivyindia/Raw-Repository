# Automation Coverage Matrix

**Status:** v1.0 — 2026-09-16

## Purpose

Shows what is already represented in the library versus what still requires execution work. This prevents another generic discovery cycle.

| Layer | Coverage | Remaining work |
|---|---|---|
| Company capabilities | High | Activate by priority |
| SMB processes | High | Connect systems |
| Mid-market processes | High | Add controls/shared services |
| International processes | High | Country packs/localization |
| Enterprise processes | High | Deep control/portfolio implementation |
| Agents | High | Runtime verification |
| Skills | High | Extraction/versioning/testing |
| Prompts | High | Regression testing |
| SOPs/processes | High | Convert priority SOPs to executable workflows |
| Templates/playbooks | High | Parameterize and connect |
| End-to-end systems | High | Select/compose rather than duplicate |
| n8n/workflow automation | High | Build production workflows |
| MCP/connectors | Medium-High | Establish governed connector inventory |
| Systems of record | Medium | Finalize Odoo/Notion/GitHub/HR/helpdesk/accounting roles |
| Identity/permissions | Medium | Implement agent identity and least privilege |
| Approval gates | Medium | Standardize approval policy and runtime enforcement |
| Audit/evidence | Medium | Unified evidence/audit schema |
| Agent registry | Medium | Operational registry + lifecycle automation |
| Observability | Medium | Central traces, metrics, cost and failure monitoring |
| Evaluation | Medium | Automated regression suite |
| Cost control | Medium | Per-agent/workflow/model cost ledger |
| Exception management | Medium | Central exception queue and escalation |
| Security | Medium | Threat model, secrets, sandboxing, supply-chain checks |
| Business continuity | Partial | Backup/failover/degraded-mode tests |
| Cross-agent A2A | Partial | Governed delegation protocol |
| Country packs | Partial | Build only for active markets |
| Industry packs | Partial | Build only for active verticals |
| Production deployment | Partial | Execute Phase 0.6 onward |

## Automation completeness rule

A capability is **covered** when a reusable asset/process exists.

A capability is **automated** when a tested workflow can execute it.

A capability is **production-automated** when identity, permissions, approvals, audit, monitoring, failure handling and regression controls are also operational.

Therefore:

`Coverage ≠ Automation ≠ Production Automation`

## Six genuinely remaining execution buckets

### 1. Integration layer

Connect systems of record through APIs, webhooks, MCP or workflow automation:

`CRM ↔ Email ↔ Calendar ↔ Messaging ↔ Accounting ↔ ERP ↔ HR ↔ Helpdesk ↔ Project/PM ↔ GitHub ↔ Knowledge ↔ Analytics ↔ AI runtime`

### 2. Production automation

Turn library assets into executable:

`Trigger → Agent → Tool → Decision → Approval → Action → Evidence → Audit → KPI`

### 3. Agent control plane

Implement:

`Identity → Registry → Permissions → Policy → Routing → Approval → A2A → Observability → Evaluation → Cost → Exceptions → Kill switch`

This matches current enterprise architecture guidance: control planes are increasingly treated as the common layer for identity, policy, registry, visibility and governance across heterogeneous agents. citeturn0search0turn0search11

### 4. Scale activation

Use the scale matrix in file 76 to avoid overengineering small companies and under-controlling enterprise workflows.

### 5. Jurisdiction/industry activation

Create reusable country/industry packs only where commercially required: tax, privacy, employment, contracts, data residency, licenses, localization, banking/FX and industry controls.

### 6. Resilience

Implement:

- backups
- restore tests
- provider/model failover
- connector failure handling
- degraded-mode procedures
- agent quarantine
- kill switch
- incident response
- human escalation
- cost runaway controls
- security incident handling
- regression testing

## Stop condition for further discovery

Do not perform another broad discovery round unless one of these occurs:

- a new capability appears
- a new jurisdiction/industry is activated
- an adopted asset becomes obsolete
- a materially better asset replaces an existing one
- testing exposes a genuine capability gap
