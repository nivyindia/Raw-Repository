undefined

## 65. Deep-discovery batch — September 2026

Fresh discovery added after a second pass across enterprise-agent, ERP, governance, memory and autonomous-assistant categories.

| Capability | Newly discovered reusable solution | What it adds | Link / evidence |
|---|---|---|---|
| AI ERP + HR + CRM + Finance + Inventory + Procurement | Sentinel ERP | Cross-department ERP, workflow studio, AI copilot, forecasting, anomaly detection | https://github.com/jeevansai-hub/Sentinal-ERP |
| AI-native ERP/accounting | ERPClaw | Natural-language accounting/ERP, purchasing, inventory, payroll, tax, payments, reporting; self-hosted | https://github.com/avansaber/erpclaw |
| ERP/CRM/accounting | IDURAR | CRM, invoices, payments, quotes, accounting, inventory and HR; commercial use stated by project | https://github.com/idurar/idurar-erp-crm |
| AI-native ERP architecture | OpenSpine | Finance/materials/production with planned AI agents and natural-language reporting; currently pre-alpha | https://github.com/beyhanmeyrali/OpenSpine |
| Agent-native accounting | Accounted | Accounting exposed through 150+ MCP tools, scoped API keys/OAuth and audit-oriented bookkeeping | https://github.com/erp-mafia/accounted |
| Agent governance | A2A Governance Gateway | Identity, capability scoping, budgets, HITL approval and tamper-evident audit for A2A calls | https://github.com/ygmrs/a2a-governance-gateway |
| Agent orchestration control plane | GAIA | DAG execution, A2A/MCP routing, policy governance, mTLS/JWT, HITL, trust monitoring and cryptographic audit | https://github.com/vishalsdk14/GAIA |
| Personal/company JARVIS pattern | NovaBot | Telegram interface, memory, email, calendar, web research, browser, social posting, calls, WhatsApp and background tasks | https://github.com/AmplifyCo/novabot |
| Local JARVIS pattern | ORBIT | Voice, Ollama, web research, YouTube, Telegram Desktop, telemetry, memory and HUD | https://github.com/mostafa-kermaninia/Orbit-Local-AI-Agent |
| Persistent memory OS | MemoryOS | Long-term memory, semantic retrieval, RAG, knowledge graphs and workspace organization | https://github.com/akshay-kakade/MEMORY-OS |
| Local-first AI OS | Eidetic OS | Persistent memory, hybrid RAG, knowledge graph, scheduled work and 160+ skills | https://github.com/paulholland511/eidetic-os |
| Governance-first memory | Constitutional Memory for AI Agents | Treats persistent memory as governed authority-bearing state with lifecycle and observability | https://github.com/MihaiCiprianChezan/Constitutional-memory-for-AI-agents |
| AI-agent industry directory | Open Source AI Agents Directory | Curated agents across finance, HR, legal, support, marketing, research, cybersecurity and more | https://github.com/Damitoyinbo/open-source-ai-agents-directory |
| Organizational AI simulation | OpenOfficeRL | Seven role agents operating a simulated company with shared memory and adversarial business scenarios | https://github.com/bvsbharat/OpenOfficeRL |
| AI/no-code business system | NocoBase | Open-source AI + no-code platform for production business systems, workflows and AI agents | https://github.com/nocobase/nocobase |

### 65.1 What these discoveries change for Nivy

The new evidence adds several layers that should be treated as first-class Nivy architecture rather than optional integrations:

1. **Agent Governance Gateway** — every remote agent call should pass identity, scope, budget, risk and approval checks before execution.
2. **AI-native ERP adapter** — Nivy should be able to expose accounting/ERP operations through natural-language tools while retaining deterministic transactional controls.
3. **AI Memory OS** — memory should be persistent, searchable, scoped, inspectable and governed independently of the model.
4. **AI OS / JARVIS shell** — voice/chat should be an interface to the company system, not the company system itself.
5. **Agent control plane** — goal management, DAG/workflow state, health, trust, quotas, HITL and audit belong in a control-plane layer.
6. **AI company simulation/evaluation** — simulated departments can be used to test manager/employee coordination before granting real-world permissions.
7. **Universal agent directory** — maintain a registry of reusable agents by department, capability, protocol, license, maturity and integration method.

### 65.2 Evidence notes

- Sentinel ERP describes unified HRMS, CRM, finance, inventory, procurement, manufacturing and AI automation in one open-source ERP. citeturn0search0
- ERPClaw describes an AI-native self-hosted ERP with accounting, sales, buying, inventory, payments, tax/payroll and regional packs including India, UK, Canada and EU. citeturn0search1
- The A2A Governance Gateway adds identity, budgets, human approval and tamper-evident audit around agent-to-agent calls. citeturn0search2
- The open-source agent directory covers multiple departments including finance, customer service, HR, legal, retail, marketing, research and cybersecurity. citeturn0search3
- IDURAR provides an open-source ERP/CRM/accounting system with invoices, payments, quotes, customers, inventory and HR. citeturn0search4
- MemoryOS provides persistent memory, semantic retrieval, knowledge graphs and RAG as a dedicated memory layer. citeturn0search5
- OpenSpine is an AI-native ERP architecture with finance/materials/production foundations and planned agentic document understanding/natural-language reporting; it is currently pre-alpha. citeturn0search6
- Accounted exposes accounting through MCP tools and emphasizes immutable bookkeeping, scoped credentials and agent operation. citeturn0search7
- Eidetic OS demonstrates persistent memory, hybrid retrieval, knowledge graph, scheduled autonomous work and a large skills catalog. citeturn0search8
- Constitutional Memory proposes treating persistent agent memory as a governed subsystem rather than unmanaged model context. citeturn0search9
- OpenOfficeRL demonstrates simulation of multiple company roles and coordination under changing business scenarios. citeturn0search10
- NocoBase is an additional open-source AI/no-code business-system foundation surfaced in current GitHub topic results. citeturn0search11
- ORBIT demonstrates a local voice agent combining STT, Ollama, web research, YouTube, Telegram Desktop, telemetry and memory. citeturn0search12
- NovaBot demonstrates a broader self-hosted assistant pattern combining email, calendar, web, social, voice calls, WhatsApp and background tasks. citeturn0search13
- GAIA describes an agent orchestration control plane with A2A/MCP routing, policy, HITL, trust monitoring and cryptographic audit. citeturn0search14

### 65.3 Updated Nivy reference architecture

```
User
  ↓
Nivy UI / Voice / Telegram / Web / API
  ↓
Identity + Session + Role
  ↓
Intent + Context + Memory
  ↓
Company Digital Twin / Universal Data Model
  ↓
AI Executive / AI Manager
  ↓
Planner / DAG / Workflow
  ↓
AI Employee + Skill
  ↓
MCP Tool / A2A Agent / API / Browser / Computer
  ↓
Risk + Policy + Budget Gate
  ↓
Human Approval (when required)
  ↓
Transactional System / External Action
  ↓
Verification + Audit + Observability
  ↓
KPI / Outcome / Cost
  ↓
Memory + Knowledge Graph update
  ↓
Proactive monitoring + next action
```

### 65.4 Reuse priority for Nivy

| Layer | First candidates to evaluate | Why |
|---|---|---|
| Company transaction backbone | Odoo / ERPNext / ERPClaw / Sentinel ERP | Avoid building ERP/accounting/HR/CRM primitives |
| Agent control plane | GAIA / LangGraph / Temporal | Durable execution, routing, policy and HITL |
| Governance | A2A Governance Gateway + Keycloak + OpenFGA + OPA | Identity, authorization, risk and approval |
| Memory | MemoryOS / Mem0 / Eidetic OS + Qdrant/Neo4j | Persistent company/agent memory |
| Voice/JARVIS | OpenDex / NovaBot / ORBIT + LiveKit/Pipecat | Voice-first company interface |
| Research | GPT Researcher / STORM / Crawl4AI / SearXNG | Evidence-based intelligence |
| Unified UI | Custom Nivy shell + Refine/shadcn/Appsmith | One user-facing workspace |
| Evaluation | Phoenix / Langfuse / Promptfoo + OpenOfficeRL | Measure agents and simulate organization behavior |

**Rule:** these are candidates for evaluation, not automatic technology choices. Nivy should test the smallest viable combination and retain adapters so individual components can be replaced later.
