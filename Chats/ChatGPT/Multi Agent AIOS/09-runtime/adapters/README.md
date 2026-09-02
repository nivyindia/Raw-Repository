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

Response should be JSON and must preserve the `execution_id`.

## Runtime ownership

- **LangGraph**: primary stateful agent runtime for research, intelligence, scoring, qualification support, meeting prep, proposal and onboarding agents.
- **CrewAI**: role-based multi-agent execution for strategy/personalization/solution-mapping/qualification tasks where delegation is useful.
- **Hermes**: optional general-purpose autonomous agent runtime for tasks that benefit from tool use, memory, delegation or scheduled execution.
- **Dify**: optional application/workflow runtime for packaged AI applications and reusable prompt/tool workflows.
- **n8n**: business workflow orchestration only. It triggers the AIOS gateway and handles webhooks, schedules, CRM/email integrations, retries and approvals; it is deliberately not configured as an agent runtime.

## Deployment rule

Do not point `LANGGRAPH_RUNTIME_URL`, `CREWAI_RUNTIME_URL`, `HERMES_RUNTIME_URL` or `DIFY_RUNTIME_URL` back at the AIOS gateway. That creates a request loop. Each variable must point at its dedicated adapter or runtime service.

The adapter layer is intentionally provider-neutral: the AIOS contract remains stable while individual engines can be swapped or scaled independently.
