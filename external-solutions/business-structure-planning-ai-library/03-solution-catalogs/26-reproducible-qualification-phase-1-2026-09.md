# Reproducible Qualification — Phase 1 Evidence — September 2026

**Scope:** Source-level qualification of the first Nivy reuse candidates.
**Status:** Phase 1 = repository identity + README/license/interface evidence. No production adoption decision is made from source inspection alone.

**Decision rule:** REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

## 1. Evidence matrix

| Candidate | Canonical repository verified | License evidence | Interface / integration evidence | Current capability evidence | Phase-1 gate result |
|---|---|---|---|---|---|
| ERPClaw | avansaber/erpclaw | GPL-3.0 (LICENSE.txt) | OpenClaw primary; experimental Hermes; CLI/action router; WebClaw/ERPClaw Web; PostgreSQL/SQLite | README reports v4.15.0, 46 modules, 3,235 actions; accounting, sales, buying, inventory, payments, tax, payroll, reporting | PASS — source inspection |
| NocoBase | nocobase/nocobase | License must be verified from the exact deployment/version before adoption | MCP, HTTP APIs, CLI, plugins; integrations with OpenClaw/Hermes/Dify/Coze/n8n and messaging/email surfaces are documented in README | Open-source AI + no-code business-system platform; AI employees, workflows, data models, permissions and audit logs documented | PASS — capability evidence / license follow-up required |
| Microsoft Agent Governance Toolkit | microsoft/agent-governance-toolkit | MIT (LICENSE) | Python/TypeScript/.NET/Rust/Go; MCP; A2A; framework adapters; CLI | Policy engine, identity/trust, audit, runtime controls, MCP security gateway, SRE/compliance packages; README reports 992 conformance tests | PASS — source inspection |
| MemOS | MemTensor/MemOS | Apache-2.0 (LICENSE) | API; local plugin; OpenClaw/Hermes/DeepSeek Harness; hybrid FTS5 + vector retrieval | Persistent memory, local-first SQLite, multi-agent collaboration, skill evolution, plugin integrations | PASS — source inspection |

## 2. What was actually verified

### ERPClaw
- Repository: avansaber/erpclaw
- README explicitly states GPL-3.0.
- README describes self-hosted deployment with SQLite by default and PostgreSQL support.
- README exposes a single action-router style foundation and OpenClaw/Hermes runtime paths.
- Financial safety claims are implemented as architectural requirements in the README: immutable GL entries, transaction boundaries and validation.
- The README reports current build facts as v4.15.0, 46 modules and 3,235 actions.
- Not yet verified: clean-room installation on Nivy test host, API contract tests, backup/restore, security audit, Nivy adapter.

### NocoBase
- Repository: nocobase/nocobase
- README describes an open-source AI + no-code platform for business systems.
- README documents data models, workflows, permissions, audit logs and plugin architecture.
- README documents AI employees and external-agent interfaces including MCP, HTTP APIs and CLI.
- Not yet verified: exact license file for the current checkout, clean installation, database export/import, API contract, Nivy embedding and production resource requirements.

### Microsoft Agent Governance Toolkit
- Repository: microsoft/agent-governance-toolkit
- LICENSE is MIT.
- README documents policy enforcement, identity/trust, audit, MCP security, runtime controls and framework adapters.
- README provides install paths for Python, TypeScript, .NET, Rust and Go.
- README documents OpenAI Agents SDK, CrewAI, LangGraph/LangChain, Dify and other integrations.
- Not yet verified: Nivy-specific policy model, performance overhead, deployment topology and which modules are required for the V1 revenue engine.

### MemOS
- Repository: MemTensor/MemOS
- LICENSE is Apache-2.0.
- README documents local-first memory with SQLite, hybrid FTS5 + vector retrieval and multi-agent collaboration.
- README documents local integrations for OpenClaw/Hermes/DeepSeek Harness and a cloud plugin.
- Not yet verified: Nivy entity/permission model, temporal facts, retention controls, migration/export and performance under company-scale workloads.

## 3. Gate status

| Gate | Phase-1 result |
|---|---|
| G1 Identity | PASS for all four repositories |
| G2 License | PASS ERPClaw, AGT, MemOS; FOLLOW-UP NocoBase |
| G3 Activity | FOLLOW-UP — verify recent commits/releases separately |
| G4 Deployment | FOLLOW-UP — install test required |
| G5 Interface | PASS at documentation level |
| G6 Data | PARTIAL — architecture visible; migration/export tests pending |
| G7 Security | PARTIAL — documented controls exist; adversarial test pending |
| G8 Governance | PASS at design level for AGT; PARTIAL for others |
| G9 Reliability | FOLLOW-UP — CI/tests/recovery need execution evidence |
| G10 Integration | PARTIAL — documented interfaces exist; Nivy adapter test pending |
| G11 Replaceability | DESIGN REQUIREMENT — adapter boundary still needs implementation |
| G12 Evidence | PASS for source inspection; install/runtime evidence pending |

## 4. V1 interpretation

Do not make any of these the irreversible Nivy core yet.

Current architecture candidates:
- ERPClaw: transaction/ERP candidate behind an adapter.
- NocoBase: rapid internal business-system/admin UI candidate; also useful for data-model/workflow prototyping.
- Microsoft Agent Governance Toolkit: governance/control-plane implementation reference and possible reusable middleware.
- MemOS: memory subsystem candidate behind a memory adapter.

Nivy should retain ownership of:
1. unified UI/workspace;
2. identity/RBAC;
3. company digital twin + universal data/event contracts;
4. agent/skill/tool registries;
5. policy/risk/approval contracts;
6. memory abstraction;
7. integration adapters;
8. audit/observability contracts.

## 5. Next execution

The next phase is runtime qualification, in this order:

1. ERPClaw — install + create company + customer + invoice + payment + report.
2. NocoBase — install + create data model + workflow + role + AI employee + audit event.
3. Agent Governance Toolkit — run policy allow/deny + identity + audit + MCP interception.
4. MemOS — install local memory + write/read/search + multi-session persistence.
5. Build a minimal Nivy adapter for each surviving candidate.
6. Record runtime evidence and make only per-gate PASS/FAIL decisions.

No overall candidate ranking is used.
