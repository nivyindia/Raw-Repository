# AIOS Runtime Installation

## Start the current development stack

From this directory:

```bash
cp .env.example .env
cd ../08-infrastructure
docker compose up -d --build
```

The gateway is exposed at `http://localhost:8080`.

## Inspect registered agents

```bash
curl http://localhost:8080/v1/agents
```

## Invoke a non-approval-gated agent

```bash
curl -X POST http://localhost:8080/v1/agents/A039/invoke \
  -H 'Content-Type: application/json' \
  -d '{"input":{"lead_id":"example-lead"}}'
```

The gateway will route to the runtime configured for A039. If that runtime is not configured yet, the response is explicitly `runtime_not_configured`.

## Approval-gated actions

A044, A060 and A065 require an approval token at the runtime boundary. The gateway will not attempt execution without it.

## Next runtime adapters

Set these environment variables when the corresponding services are deployed:

- `LANGGRAPH_RUNTIME_URL`
- `CREWAI_RUNTIME_URL`
- `HERMES_RUNTIME_URL`
- `DIFY_RUNTIME_URL`

This keeps the business agent contracts stable while the execution backends are brought online incrementally.
