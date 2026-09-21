# Deep Qualification — Agent Company Reuse Candidates — September 2026

**Purpose:** Convert discovery into implementation-ready candidates by checking license, maturity, deployment, interfaces, governance, and Nivy fit.

**Decision rule:** **REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.**

## 1. Qualification matrix

| Candidate | Layer | License / commercial note | Deployment | Interface | Maturity signal | Nivy role | Decision |
|---|---|---|---|---|---|---|---|
| Sentinel ERP | ERP / CRM / HR / Finance | MIT reported by project | Self-hosted | Web / APIs / workflows | Broad full-suite scope; verify current release before production | Transaction-system candidate | **Evaluate** |
| ERPClaw | AI ERP / accounting | GPLv3 | Self-hosted | Natural language / APIs | 46 modules and 3,235 actions reported in current project docs | ERP + AI tool adapter candidate | **Evaluate deeply** |
| IDURAR | ERP / CRM / accounting | AGPL-3.0 | Self-hosted | Web / API | Established open-source ERP/CRM scope | Lightweight ERP/CRM fallback | **Evaluate** |
| OpenSpine | AI-native ERP | Verify current license before use | Self-hosted project | Planned AI/NL reporting | Pre-alpha | Architecture/R&D reference | **Do not depend on V1** |
| Accounted | Agent-native accounting | AGPL-3.0-or-later with extension exception | Self-hosted | 150+ MCP tools / OAuth | Specialized accounting | MCP accounting adapter/reference | **Evaluate** |
| NocoBase | No-code / business systems | Verify edition/license per deployment | Self-hosted | APIs / workflows / plugins | Mature business-app platform | Rapid internal admin/UI builder | **Evaluate** |
| GAIA | Agent control plane | Verify repository license/current status | Self-hosted | A2A / MCP | Governance-heavy architecture | Agent orchestration/control-plane reference | **Prototype** |
| A2A Governance Gateway | Agent governance | Verify repository license/current status | Self-hosted | A2A | Explicit identity/budget/HITL/audit design | Policy gateway reference | **Prototype** |
| Microsoft Agent Governance Toolkit | Agent governance/security | Verify component licenses before redistribution | Self-hosted/source reference | MCP / A2A / governance APIs | Active specification/toolkit work | Governance design + implementation reference | **Reuse patterns** |
| MemoryOS / MemOS | Persistent memory | Check exact repository/version license | Self-hosted | API / agent integrations | Dedicated memory-OS architecture | Company + agent memory layer | **Prototype** |
| MemoryOS AI Agents | Persistent memory | MIT | Self-hosted | LangGraph-compatible | Drop-in STM/LTM architecture | Simple memory adapter candidate | **Prototype** |
| Memento | Bitemporal graph memory | Verify current repo license | Self-hosted | MCP | Strong temporal-memory concept; benchmark claims need independent validation | Auditable temporal memory candidate | **Evaluate** |
| Ariadne | Multi-source memory/RAG | Verify current repo license | Self-hosted | MCP / agent integration | Broad ingestion + graph + RAG scope | Knowledge ingestion/reference layer | **Evaluate** |
| NovaBot | JARVIS / omnichannel assistant | Verify current repo license | Self-hosted | Telegram / email / calendar / web / browser / voice / WhatsApp | Broad integration surface | Nivy interface/assistant reference | **Prototype selectively** |
| ORBIT | Local voice assistant | Verify current repo license | Local/self-hosted | Voice / Ollama / web / Telegram | Local-first assistant pattern | Voice shell reference | **Prototype selectively** |
| Eidetic OS | Personal AI OS / memory | Verify current repo license | Local/self-hosted | Skills / scheduled tasks / RAG / graph | 160+ skills reported by project | Personal/company assistant reference | **Evaluate patterns** |
| OpenOfficeRL | Company simulation | Verify current repo license | Research/local | Multi-agent simulation | Explicit simulated-company environment | Agent-manager evaluation harness | **Prototype for testing** |
| Open Source AI Agents Directory | Agent discovery | Directory; each project has own license | Web/GitHub | Repository links | Useful breadth, not implementation evidence | Discovery index | **Use as discovery input** |

> **Important:** “Evaluate” does not mean production-ready. License, activity, security, dependency health, API stability, data model, deployment and actual feature behavior must be verified against the current repository before adoption.

## 2. New governance evidence

Microsoft's Agent Governance Toolkit specification describes an MCP security gateway with tool-call interception, authentication, rate limiting, approval callbacks, audit logging and metrics. Sensitive tools can be blocked unless approval is granted, and every interception is recorded. citeturn0search3turn0search11

**Nivy implication:** governance must sit **before** execution, not after it:

```
Agent identity
  → capability/tool scope
  → data scope
  → policy/risk check
  → budget/rate limit
  → human approval if required
  → tool execution
  → verification
  → immutable/auditable event
```

## 3. New memory evidence

Recent projects demonstrate several distinct memory models:

- **Graph + Redis:** a dedicated memory layer can separate short-term session/checkpoint state from long-term Neo4j/Memgraph knowledge. citeturn0search1
- **MCP memory:** Memory Palace exposes persistent semantic memory and knowledge-graph recall through MCP. citeturn0search2
- **Bitemporal memory:** Memento tracks when a fact was true separately from when it was learned, which is useful for changing company facts. citeturn0search5
- **Hybrid source ingestion:** Ariadne combines documents, conversations and code with RAG, graph memory and agent/MCP integration. citeturn0search7
- **Model-independent memory OS:** MemOS describes a unified memory API with graph-based, multimodal and isolated knowledge bases. citeturn0search16

**Nivy implication:** do not make “memory” equal to a vector database. The target should support:

**Working context → Session memory → Long-term facts → Entity/relationship graph → Documents/knowledge → Decisions → Tool/action history → Temporal/version history → Permissions/retention → Retrieval policy.**

## 4. Minimum qualification gates

Before a candidate enters the Nivy implementation stack, verify:

| Gate | Required evidence |
|---|---|
| G1 Identity | Exact repository/project and canonical upstream |
| G2 License | SPDX/license file + commercial-use implications |
| G3 Activity | Recent commits/releases/issues; distinguish active from archived |
| G4 Deployment | Docker/compose/Kubernetes/native installation and resource requirements |
| G5 Interface | REST/API, MCP, A2A, webhooks, CLI or SDK |
| G6 Data | Database, schema, export/import and migration path |
| G7 Security | Authentication, authorization, secrets, sandboxing and network model |
| G8 Governance | Approval, budgets, policy gates, audit trail |
| G9 Reliability | Tests, CI, backups, recovery and failure behavior |
| G10 Integration | Odoo/ERPNext/ERPClaw, n8n, Nivy UI, identity and event bus compatibility |
| G11 Replaceability | Adapter boundary exists so the candidate can be removed later |
| G12 Evidence | Reproduction/test result recorded in the library |

## 5. V1 qualification order for Nivy

Do not attempt to integrate the whole universe simultaneously.

### Track A — Revenue engine
1. CRM/lead source
2. Lead research
3. qualification
4. outreach drafting
5. human approval
6. sending
7. follow-up
8. meeting
9. proposal
10. won/lost
11. revenue/KPI

### Track B — Company backbone
1. identity/RBAC
2. company/customer/lead/opportunity data
3. documents/knowledge
4. tasks/workflows
5. finance/accounting boundary
6. audit events

### Track C — Agent control
1. agent registry
2. skill registry
3. tool registry
4. permission registry
5. policy/risk engine
6. approval queue
7. execution/audit log
8. agent health/cost metrics

### Track D — Memory
1. working context
2. session memory
3. durable facts
4. entity graph
5. document RAG
6. temporal/versioned facts
7. permission-aware retrieval

### Track E — Interface
1. Nivy web shell
2. role-based workspace
3. global search
4. AI chat
5. notifications
6. approval center
7. optional voice/Telegram

## 6. New high-value discovery candidates

These are worth adding to the candidate pool even though they are not automatically selected:

| Candidate | Why it matters | Link |
|---|---|---|
| Microsoft Agent Governance Toolkit | Concrete MCP/A2A governance, approval, audit and compliance specifications | https://github.com/microsoft/agent-governance-toolkit |
| Memory Palace | MCP-native persistent semantic memory + graph | https://github.com/jeffpierce/memory-palace |
| Memento | Bitemporal knowledge graph memory | https://github.com/shane-farkas/memento-memory |
| Ariadne | Multi-source ingestion + RAG + knowledge graph + persistent memory + MCP | https://github.com/Chaobs/ariadne-memory |
| MemOS | Memory operating system with graph-based memory and KB isolation | https://github.com/MemTensor/MemOS |
| Agent-Memory | Local-first persistent memory with SQLite/HNSW and three memory layers | https://github.com/ivanzwb/agent-memory |
| Ori Mnemos | Git/Markdown local-first persistent memory with knowledge graph and retrieval learning | https://github.com/aayoawoyemi/Ori-Mnemos |

## 7. Immediate next execution task

The next step is **not another giant discovery list**.

For the highest-impact candidates, run a reproducible qualification test:

```
DISCOVER
→ CLONE/INSPECT
→ LICENSE CHECK
→ BUILD/INSTALL
→ SMOKE TEST
→ API/MCP TEST
→ SECURITY/GOVERNANCE TEST
→ DATA MODEL CHECK
→ NIVY ADAPTER TEST
→ SCORE ONLY AS PASS/FAIL PER GATE
→ RECORD EVIDENCE
→ REUSE / ADAPT / REJECT
```

Use **pass/fail evidence per gate**, not an overall ranking score.

### Priority test set

1. ERPClaw
2. Sentinel ERP
3. NocoBase
4. Microsoft Agent Governance Toolkit
5. GAIA
6. MemOS / MemoryOS
7. Memento
8. NovaBot
9. OpenOfficeRL

## 8. Nivy architectural conclusion

The research now supports treating Nivy as an **orchestration and control layer over reusable systems**, rather than rebuilding every business function.

```
NIVY
├── Unified UI
├── Identity / RBAC
├── Company Digital Twin
├── Universal Data + Event Model
├── Agent Registry
├── Skill Registry
├── Tool / MCP Registry
├── Agent Control Plane
├── Policy / Risk / Budget Gate
├── Approval Center
├── Workflow / Durable Execution
├── Memory + Knowledge
├── Transaction System Adapter
├── Integration / Connector Layer
├── Audit + Observability
└── Proactive Intelligence
       │
       ├── ERP / CRM
       ├── Finance
       ├── HR
       ├── Sales
       ├── Marketing
       ├── Support
       ├── Projects
       ├── Legal
       ├── Procurement
       └── Other specialist systems
```

**Principle:** Nivy owns the cross-system identity, context, orchestration, governance, memory, UX and integration contracts. Specialist systems remain replaceable modules behind adapters.
