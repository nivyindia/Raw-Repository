# AgentOps, Governance, Identity & Approval Skill Catalog

**Status:** v1.0 — 2026-09-16

## Scope

Cross-company controls required before many agents can safely touch production systems.

| Capability | Reusable assets | Required control | Nivy implementation target | Priority |
|---|---|---|---|---:|
| Agent registry | MCP Gateway & Registry | inventory, owner, version, status | AI Asset Registry | P0 |
| Tool firewall | Preloop / Airlock | allow/deny/ask by agent/tool | Tool Control Plane | P0 |
| Human approval | mcp-approvals / Preloop / Airlock | approval before consequential action | Approval Queue | P0 |
| Policy-as-code | PolicyAware / Preloop / SAFi | declarative rules | Governance Policy Pack | P0 |
| Identity | Gateway + IdP patterns | agent identity, user attribution, least privilege | Identity & Access layer | P0 |
| Secrets | gateway/connector vault patterns | no secrets in prompts/repositories | Secret management | P0 |
| Audit | Preloop / Airlock / mcp-approvals | immutable/reconstructable event trail | Agent Audit Log | P0 |
| Runtime observability | OpenLIT / Phoenix | model/tool/session traces | AgentOps dashboard | P1 |
| Evaluation | Phoenix / Future AGI / mcp-eval | quality, safety, regression tests | Eval harness | P1 |
| Cost governance | Preloop | budgets and attribution | AI cost ledger | P1 |
| Incident response | governance/observability tools | kill switch, quarantine, replay | Agent Incident Runbook | P1 |
| Version control | Git + registry | skill/prompt/agent versioning | Git-native lifecycle | P0 |
| Approval separation | mcp-approvals | requester cannot approve own action | Segregation of duties | P0 |
| Expiry/fail closed | mcp-approvals | timeout cannot become implicit approval | Safety policy | P0 |

## Mandatory policy categories

1. Agent identity and owner
2. Allowed models
3. Allowed tools/connectors
4. Data classification
5. Maximum action scope
6. Approval threshold
7. Financial threshold
8. External communication threshold
9. Destructive-action threshold
10. PII/sensitive-data handling
11. Rate limits
12. Cost budget
13. Timeouts
14. Audit retention
15. Incident escalation
16. Kill/quarantine procedure
17. Human override
18. Version/rollback

## Approval classes

| Class | Examples | Default |
|---|---|---|
| A | read/search/summarize | auto |
| B | internal draft/create | auto or sampled QA |
| C | CRM update, internal workflow change | policy-based |
| D | external message, publish, hiring recommendation, invoice action | human approval |
| E | payment, legal commitment, destructive production action | explicit authorized human approval |

## Key reusable evidence

Preloop documents an integrated open-source control plane combining MCP firewall, model gateway, budgets, human approvals, runtime observability and audit trails. citeturn0search2turn0search3

Airlock provides per-agent allow/ask/deny rules, human approval and audit logging around MCP/CLI/API access. citeturn0search0

The mcp-approvals project implements a human decision gate with append-only hash-chained audit records, separation of duties and fail-closed timeouts. citeturn0search4

## Nivy design rule

Treat governance as infrastructure, not a document. Every production agent should have an identity, owner, allowed tools, data scope, budget, approval policy, audit trail and rollback/quarantine procedure.
