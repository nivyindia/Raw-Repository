# AIOS Revenue Engine — n8n Integration

This directory contains the business-automation boundary for the Billion Dreams United AIOS.

## Responsibility

n8n owns external business orchestration: webhooks, schedules, CRM updates, email providers, approvals, retries, and downstream integration calls.

The AIOS runtime gateway remains authoritative for agent identity, policy, runtime selection, agent invocation, durable events, and outbox delivery state.

## Revenue path

`lead intake → enrichment → quality → scoring → personalization → outreach → reply triage → qualification → meeting → proposal → onboarding`

The revenue path is now event-capable rather than dependent on one long-lived workflow execution:

`workflow → revenue event → PostgreSQL outbox → n8n event router → next workflow`

## Durable event flow

`POST ${AIOS_RUNTIME_URL}/v1/events` persists an event and its outbox message in the same database transaction. The router polls:

`GET ${AIOS_RUNTIME_URL}/v1/outbox/claim?consumer=n8n-revenue-router&event_prefix=revenue.`

After successful downstream dispatch it acknowledges:

`POST ${AIOS_RUNTIME_URL}/v1/outbox/ack`

The outbox uses leases, attempt counts, retry scheduling, and a dead-letter state. Delivery records are idempotent per `(outbox_id, consumer)`.

Current automatic routes:

- `revenue.lead.scored` → Revenue 02 outreach workflow.
- `revenue.lead.qualified` with `qualification_status=qualified` → Revenue 04 opportunity workflow.
- Other revenue events are acknowledged as terminal/approval-required until their dedicated consumer is implemented.

The routing contract is maintained in `event-router.yaml`; the executable n8n workflow is `workflows/aios-event-router.json`.

## Runtime contract

The workflow calls:

`POST ${AIOS_RUNTIME_URL}/v1/agents/{agent_id}/invoke`

with:

```json
{
  "execution_id": "n8n-execution-id",
  "input": {}
}
```

Do not put provider API keys or secrets into workflow JSON. Configure them as n8n credentials or environment-backed secrets.

## Important

The workflow definitions are execution scaffolding. Provider-specific credentials, domains, sender identities, and approval policies must be configured before external sending is enabled.

The PostgreSQL initialization schema in `08-infrastructure/postgres-init/02-create-aios-runtime.sql` is applied automatically only when a new PostgreSQL data volume is initialized. Existing deployments require applying that schema as a migration before enabling the event router.
