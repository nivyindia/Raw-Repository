# Agent Registry, Identity, Approval & Exception Catalog

**Status:** v1.0 — 2026-09-16

## Master control objects

| Object | Minimum fields | Purpose |
|---|---|---|
| Agent | id, name, owner, version, status, purpose | identify every agent |
| Skill | id, version, source, license, inputs, outputs | reusable capability |
| Tool/MCP | id, endpoint, scopes, risk class | controlled action surface |
| Workflow | id, trigger, steps, owner, SLA | deterministic orchestration |
| Policy | id, rule, scope, approver, expiry | enforce behavior |
| Approval | request, actor, action, risk, approver, decision, reason | human control |
| Exception | type, severity, owner, SLA, status, evidence | operational recovery |
| Audit event | timestamp, actor, tool, action, result, trace | reconstruction |
| Cost event | model, agent, user, tokens, cost, workflow | AI economics |
| Decision | question, evidence, decision, owner, review date | institutional memory |

## Agent lifecycle

`Proposed → Registered → Security Reviewed → Tested → Approved → Pilot → Production → Suspended/Quarantined → Retired`

## Identity model

Every action should resolve to both:

`Human principal → Agent principal → Tool principal`

This enables user attribution, least privilege, separation of duties and incident reconstruction.

## Exception taxonomy

1. Authentication failure
2. Authorization denial
3. Missing approval
4. Tool unavailable
5. Connector timeout
6. Invalid input
7. Schema mismatch
8. Knowledge/source conflict
9. Low-confidence result
10. Policy violation
11. Sensitive-data exposure risk
12. Budget exceeded
13. Rate limit
14. Duplicate action
15. External-party response failure
16. Human approval timeout
17. Data-quality failure
18. Workflow state inconsistency
19. Model/provider outage
20. Suspected agent misuse

## Exception loop

`Detect → Classify → Freeze risky action → Gather evidence → Notify owner → Human decision → Recover/Rollback → Record → Create regression test → Resume`

## Agent registry requirements

- Unique stable ID
- Human owner
- Business owner
- Version
- Source/provenance
- License/access
- Allowed environments
- Allowed models
- Allowed tools
- Data classes
- Approval class
- Budget
- SLA
- Evaluation status
- Last security review
- Last successful run
- Known failure modes
- Rollback/quarantine procedure

The open-source MCP Gateway & Registry explicitly treats MCP servers, agents and skills as governed AI assets with centralized discovery, access control and audit. citeturn0search6turn0search11

## Nivy implementation target

Create one machine-readable registry in the Raw/Company OS architecture, then expose filtered views for developers, operators, executives and agents. The registry is metadata/control—not the knowledge base itself.
