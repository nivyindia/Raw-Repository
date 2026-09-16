# Cross-Company AI Infrastructure Adoption Map

**Status:** v1.0 — 2026-09-16

## P0 — Build the control foundation

| Capability | Candidate reusable assets | Nivy action | Outcome |
|---|---|---|---|
| AI asset registry | MCP Gateway & Registry | catalog agents/skills/MCP/workflows | discoverability + governance |
| Tool access control | Preloop / Airlock | per-agent allow/ask/deny | least privilege |
| Human approval | Preloop / Airlock / mcp-approvals | approval classes A–E | controlled autonomy |
| Audit | Preloop / Airlock / mcp-approvals | central event trail | reconstruction |
| Source registry | existing research catalog | provenance metadata | evidence |
| Versioning | Git | version agents/skills/prompts | rollback |
| Identity | gateway/IdP patterns | human→agent→tool identity | attribution |

## P1 — Make the company learn

| Capability | Candidate | Nivy action |
|---|---|---|
| Agent observability | OpenLIT / Phoenix | trace model/tool/workflow runs |
| Evaluation | Phoenix / Future AGI / mcp-eval | regression datasets + quality gates |
| Knowledge | SAG + existing Notion/GitHub architecture | canonical company knowledge |
| Process intelligence | ProcessM / commercial process-mining options | mine real workflows before automating |
| Contract operations | CLM agents/skills | obligations and approvals |
| Procurement | vendor/RFP skills | controlled source-to-pay workflows |
| Customer success | CS skills | onboarding/ticket/health/QBR |
| Cost governance | Preloop / model gateway | cost by agent/workflow/customer |

## P2 — Executive intelligence

- Decision registry
- Company-wide exception dashboard
- AI economics/ROI ledger
- Business continuity and provider failover
- Agent marketplace/internal catalog
- Cross-agent delegation/A2A
- Simulation and digital-twin process testing
- Continuous process optimization

## Target composition

`Registry → Identity → Policy → Router → Specialist Agent/Skill → Knowledge → Tool/MCP → Workflow → Approval → Action → Audit → Evaluation → Learning`

## First implementation slice

1. Registry schema
2. Five P0 revenue agents
3. One shared tool gateway
4. One approval mechanism
5. One audit log
6. One evaluation harness
7. One cost ledger
8. One knowledge/evidence registry
9. One exception queue
10. Pilot with synthetic + representative data

## Selection rule

Use the smallest number of reusable components that satisfy required controls. Avoid building duplicate registries, approval systems, observability systems or knowledge stores when an existing component can be adapted safely.
