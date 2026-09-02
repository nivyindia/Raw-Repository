# AIOS Revenue Engine — n8n Integration

This directory contains the business-automation boundary for the Billion Dreams United AIOS.

## Responsibility

n8n owns external business orchestration: webhooks, schedules, CRM updates, email providers, approvals, retries, and downstream integration calls.

The AIOS runtime gateway remains authoritative for agent identity, policy, runtime selection, and agent invocation.

## Revenue path

`lead intake → enrichment → quality → scoring → personalization → outreach → reply triage → qualification → meeting → proposal → onboarding`

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
