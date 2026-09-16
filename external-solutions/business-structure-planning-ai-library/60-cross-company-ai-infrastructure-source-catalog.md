# Cross-Company AI Infrastructure Source Catalog

**Status:** v1.0 — 2026-09-16

## Purpose
Discover reusable infrastructure that makes agents, skills, workflows, knowledge, approvals, identity, audit, and systems of record operate as one governed company layer.

## Discovery chain
`End-to-end control plane → agent team → agent → skill → prompt → MCP/connector → API → workflow → SOP/process → template → governance/control`

## Source catalog

| Asset | Type | Capability | Access | License/access | Nivy reuse | Priority | Verification |
|---|---|---|---|---|---|---:|---|
| Preloop | Agent control plane | MCP firewall, model gateway, budgets, approvals, observability, audit | OSS + hosted/commercial | Apache-2.0 OSS | Control-plane candidate | P0 | Web verified 2026-09-16 |
| Airlock | MCP gateway | Per-agent allow/ask/deny, HITL, audit | OSS | MIT | Lightweight tool/approval gateway | P0 | Web verified |
| MCP Gateway & Registry | AI asset registry/gateway | MCP, agents, skills, workflows, OAuth, gateway, audit | OSS | Apache-2.0 | Master AI asset registry candidate | P0 | Web verified |
| mcp-approvals | HITL MCP server | Approval gate + hash-chained audit | OSS | MIT | Simple approval primitive | P0 | Web verified |
| OpenLIT | Agent observability/evaluation | Traces, tools, memory, evals, OpenTelemetry | OSS | Recheck before production | AgentOps layer | P0 | Existing research |
| Arize Phoenix | AI observability/evaluation | Tracing, evals, datasets, experiments | OSS | Recheck before production | Evaluation/trace layer | P1 | Existing research |
| Future AGI | Agent evaluation | Evals, tracing, simulations, datasets, guardrails | OSS | Apache-2.0 stated | Evaluation layer | P1 | Existing research |
| mcp-eval | MCP/agent evaluation | Real-environment tests, traces, assertions | OSS | Recheck | MCP regression testing | P1 | Existing research |
| PolicyAware | Governance/control plane | Policy enforcement, PII redaction, MCP governance, audit | OSS | Apache-2.0 stated | Policy layer | P1 | Existing research |
| SAFi | Agent governance | Policies, supervision, allow-list, approval/block, audit | OSS | Recheck | Governance candidate | P1 | Existing research |
| ProcessM | Process intelligence | Process mining, conformance, deviation/root cause, KPIs | OSS | Recheck | Process discovery/mining | P1 | Web verified |
| SAG | Knowledge base | Searchable, connected, traceable knowledge and lifecycle | OSS | Recheck | Company knowledge candidate | P1 | Web verified |
| Anthropic Knowledge Work Plugins | Plugin/skill system | Skills, commands, connectors, sub-agents by function | OSS | Recheck repo scope/license | Reusable function library | P0 | Existing research |
| n8n Skills | Automation skill library | Workflow lifecycle, AI agents, errors, expressions, reuse | OSS | Recheck | Automation implementation | P0 | Existing research |
| Agent Platform | Multi-agent platform | RAG, memory, A2A, MCP, governance, evals, approvals | OSS | Recheck | Architecture reference | P1 | Existing research |

## Standard asset record
`name, URL, publisher, asset_type, capability, inputs, outputs, integrations, authentication, permissions, data_sensitivity, approval_requirements, license_access, deployment, maintenance, maturity, cost, reuse_mode, Nivy_destination, test_status, last_verified`.

## Architecture finding
Current control-plane patterns converge on tool governance, model routing/budgets, human approvals, runtime observability and durable audit evidence. Preloop documents these primitives together. citeturn0search2turn0search9

AI asset registries are becoming a distinct layer: the AWS open-source MCP Gateway & Registry describes centralized discovery and governance for MCP servers, agents, skills and workflows. citeturn0search6turn0search11

## Nivy rule
Do not select one broad platform merely because it is broad. Map required controls/interfaces first, test the smallest viable combination, and preserve component-level replaceability.
