# AIOS Runtime Adapters

The AIOS gateway is the policy/identity boundary. Runtime adapters are the execution boundary.

## Contract

Every adapter exposes:

`POST /v1/agents/{agent_id}/invoke`

Request:

```json
{
  "agent_id": "A036",
  "execution_id": "uuid",
  "input": {}
}
```

Response must be JSON and preserve the `execution_id`.

## Deployed adapter services

The development compose stack now creates four dedicated adapter services:

- `langgraph-adapter` → LangGraph-compatible target. Uses `/runs/wait` by default and passes an assistant ID plus execution metadata.
- `crewai-adapter` → CrewAI-compatible HTTP target using the AIOS invocation envelope.
- `hermes-adapter` → Hermes-compatible HTTP target using the AIOS invocation envelope.
- `dify-adapter` → Dify workflow target using `/workflows/run` by default and maps AIOS input into Dify `inputs`.
- `odoo-sync` → Odoo CRM synchronization API for governed lead upserts and email lookups.

The adapter services are deliberately thin. They do not invent business logic; they translate the stable AIOS contract into the configured runtime API.

## Configuration

Set `LANGGRAPH_TARGET_URL`, `CREWAI_TARGET_URL`, `HERMES_TARGET_URL` and `DIFY_TARGET_URL` to the actual deployed runtime services. API keys belong in environment/secret management, never in workflow JSON or agent contracts.

The gateway variables (`LANGGRAPH_RUNTIME_URL`, etc.) point to the local adapter services, not directly to the AIOS gateway. This prevents recursive request loops.

## Runtime ownership

- **LangGraph**: primary stateful agent runtime for research, intelligence, scoring, meeting prep, proposal and onboarding agents.
- **CrewAI**: role-based multi-agent execution for strategy/personalization/solution-mapping/qualification tasks.
- **Hermes**: optional general-purpose autonomous runtime.
- **Dify**: optional packaged AI application/workflow runtime.
- **n8n**: business workflow orchestration only.
- **Odoo**: commercial system of record; PostgreSQL owns AIOS execution/event/audit state.
