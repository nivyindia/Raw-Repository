# AIOS Runtime Layer

The runtime layer turns the governed agent contracts under `agents/` into executable requests.

## Runtime roles

- **AIOS Gateway**: single API boundary for agent invocation and health.
- **Policy boundary**: rejects unknown agents and external-send requests unless explicitly routed through an approved integration.
- **Runtime router**: selects n8n for business automation, LangGraph for stateful agent orchestration, CrewAI for multi-role crews, Hermes for autonomous workers, and Dify for AI/RAG applications.
- **n8n** remains the primary business workflow engine.
- Odoo/PostgreSQL remain business/system-of-record services; Qdrant is the canonical vector store.

## Current implementation

The gateway is deliberately adapter-based. An agent contract does not become coupled to one framework. Each registered agent has a runtime target in `runtime/registry.yaml` and can be moved between runtimes without changing its business contract.

The first revenue path is:

`A034 → A035 → A036 → A037 → A038 → A039 → A041 → A042 → A043 → A049 → A044 → A050 → A052 → A054 → A055 → A057 → A058 → A060 → A065`

The gateway exposes:

- `GET /health`
- `GET /v1/agents`
- `GET /v1/agents/{agent_id}`
- `POST /v1/agents/{agent_id}/invoke`

If a downstream runtime URL is not configured, the gateway returns a clear `runtime_not_configured` response instead of pretending an execution happened.
