# BILLION DREAMS UNITED OS — DATA CONTRACTS

**Stage:** B.15  
**Version:** 1.0  
**Status:** Baseline locked

## Purpose

Define the contract between AIOS producers, consumers, storage, workflows, and agents so that data exchanged across the system remains predictable, validated, traceable, and versioned.

## 1. Contract layers

Every production integration should identify four layers:

1. **Entity contract** — canonical entity and field definitions in `data-model.yaml`.
2. **Event contract** — event envelope and payload schemas in `event-schemas/`.
3. **API/command contract** — request, response, authorization, and error semantics for synchronous operations.
4. **Workflow contract** — trigger, inputs, outputs, side effects, retry, timeout, and escalation behavior.

## 2. Producer responsibilities

A producer must:

- Emit data conforming to the current registered schema.
- Validate required fields and references before publication.
- Assign stable IDs and correlation metadata.
- Declare the schema/event version.
- Never publish secrets in business payloads.
- Preserve provenance where data originates externally or through AI generation.
- Make retries safe and idempotent where feasible.

## 3. Consumer responsibilities

A consumer must:

- Validate incoming schema/version before processing.
- Reject unknown or incompatible contracts explicitly.
- Be idempotent for retryable events.
- Avoid assuming undocumented field presence or ordering.
- Emit structured failures when processing cannot continue.
- Preserve correlation and causation identifiers.

## 4. Versioning

- Non-breaking additions may use a minor version increment.
- Breaking field/type/semantic changes require a major version.
- Existing versions remain supported for the declared compatibility window.
- Producers and consumers must not silently reinterpret an existing version.
- Contract changes require change-management review and test evidence.

## 5. Synchronous API contract

A command/API operation should define:

```yaml
request:
  schema_version: "1.0"
  correlation_id: "required"
  actor: "required"
  payload: "validated operation-specific payload"
response:
  schema_version: "1.0"
  correlation_id: "same as request"
  status: "success|failure|accepted"
  result: "operation-specific result"
  error: "structured error when applicable"
```

Authentication and authorization are mandatory outside explicitly public endpoints.

## 6. Structured errors

Errors should expose machine-readable fields such as:

- `code`
- `message`
- `category`
- `retryable`
- `field_errors` where applicable
- `correlation_id`
- `details_ref` when additional diagnostics exist

Do not expose secrets or unnecessary sensitive information in errors.

## 7. Workflow contract

Each production workflow must declare:

- Trigger/event
- Required inputs
- Preconditions
- Producer/consumer systems
- Expected outputs
- State transitions
- Side effects
- Timeout
- Retry policy
- Escalation path
- Audit requirements
- Required approval gates

## 8. AI agent contract

Agents interacting with governed data must declare:

- Agent ID/version
- Permitted skills/tools
- Input schema
- Output schema
- Authorization scope
- Human-approval requirements
- Evaluation criteria/version
- Failure/escalation behavior

Agent-generated recommendations are non-authoritative until validated and explicitly committed through the relevant business contract.

## 9. Financial contract requirements

Financial operations must additionally define:

- Currency
- Precision/rounding policy
- Accounting/business date
- Idempotency key
- Reconciliation behavior
- Authorization threshold
- Audit reference

No financial amount should be represented using binary floating-point semantics where exact monetary precision is required.

## 10. Compatibility and rollout

For material contract changes:

`Draft → Validate → Test producers → Test consumers → Compatibility assessment → Approve → Deploy → Monitor → Retire old version`

Rollback must preserve the last known valid contract and must not create ambiguous business state.

## 11. Contract testing

Before production activation, verify:

- Schema validity
- Required fields
- Type/range constraints
- Referential integrity
- Producer output against contract
- Consumer acceptance of supported versions
- Duplicate/retry behavior
- Authorization behavior
- Error behavior
- Audit/correlation propagation

## 12. Source of truth

The canonical entity model, event registry, validation rules, and governance documents in `06-data/` form the baseline data-contract layer. Implementation-specific contracts may extend this layer but must not contradict it without an approved change.

## Definition of Done

A data contract is production-ready only when its schema, owner, version, compatibility policy, producer, consumer, validation, tests, authorization, observability, and change-management path are documented and evidenced.
