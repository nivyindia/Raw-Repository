# AIOS Event Schema Registry

**Stage:** B.13  
**Version:** 1.0  
**Status:** Registry contract

## Purpose

Define the canonical contract for event schemas created under Stage B.12 and future event additions.

## Required event envelope

Every event must contain:

- `event_id` — globally unique, immutable identifier.
- `event_type` — canonical event name, e.g. `lead.created`.
- `event_version` — semantic/schema version.
- `occurred_at` — ISO-8601 UTC timestamp describing when the business event occurred.
- `source` — producing system/workflow/agent.
- `company_id` — tenant/company scope.
- `entity_type` — canonical entity type.
- `entity_id` — canonical entity identifier.
- `correlation_id` — identifier connecting related executions/actions.
- `causation_id` — immediate event/command that caused this event, when known.
- `payload` — event-specific validated data.
- `metadata` — non-business transport/processing metadata.

## Compatibility

- Consumers must validate `event_type` and `event_version` before processing.
- Backward-compatible payload additions may increment a minor schema version.
- Breaking field/type/semantic changes require a new major version and migration plan.
- Producers must not silently change the meaning of an existing version.

## Delivery and processing

- Event consumers must be idempotent.
- Duplicate events must not create uncontrolled duplicate business side effects.
- Processing failures must be observable and retryable.
- Events should be immutable once published.
- Ordering must not be assumed unless explicitly guaranteed by the event transport contract.

## Security

- Do not place passwords, API keys, access tokens, or other secrets in event payloads.
- Apply access controls appropriate to the underlying entity data.
- Sensitive personal information should be minimized and referenced rather than unnecessarily replicated.

## Initial canonical event set

The B.12 priority events are:

1. `lead.created`
2. `lead.enriched`
3. `lead.qualified`
4. `outreach.sent`
5. `reply.received`
6. `meeting.booked`
7. `proposal.sent`
8. `contract.signed`
9. `payment.received`
10. `client.onboarded`

## Registration rule

New event types require a unique name, owning domain, producer, payload schema, consumer impact assessment, version, and test evidence before production registration.

## Definition of Done

An event schema is production-ready only when the schema is versioned, validated, tested, registered, observable, and integrated with its producer/consumer workflows.
