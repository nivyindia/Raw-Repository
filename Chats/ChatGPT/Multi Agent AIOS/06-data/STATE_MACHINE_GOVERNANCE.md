# BILLION DREAMS UNITED OS — STATE MACHINE GOVERNANCE

**Stage:** B.11  
**Version:** 1.0  
**Status:** Baseline locked

## Purpose

Define the common governance contract for all AIOS entity state machines.

## 1. Transition contract

Every transition must define:

- Source state
- Target state
- Trigger/event or authorized command
- Actor/agent/workflow responsible
- Preconditions
- Validation checks
- Side effects
- Audit record
- Failure/retry behavior

## 2. Validity rules

1. Unknown states are rejected.
2. Undefined transitions are rejected.
3. Terminal states cannot be exited implicitly.
4. A transition must be atomic from the perspective of business state.
5. Retries must be idempotent where side effects permit.
6. Concurrent transitions must not silently overwrite newer state.
7. State changes must preserve tenant/company scope.

## 3. Authorization

- Human actors require appropriate role permissions.
- Agents and workflows require explicit tool/action permissions.
- High-impact transitions require human approval where mandated by `BUILD_RULES.md`.
- Authorization failures must not mutate state.

## 4. Audit requirements

Every successful transition must record:

`entity_id + previous_state + new_state + actor + timestamp + trigger + reason + correlation_id`

Failed transitions should record the attempted transition and failure reason without falsely recording the target state as achieved.

## 5. Side-effect policy

External side effects such as messages, financial actions, contracts, or irreversible updates should occur only after the state transition's required validation/approval gates succeed.

Where possible:

`Validate → Authorize → Transition → Persist → Emit event → Execute side effect`

Side effects must carry the originating entity ID and correlation ID for traceability.

## 6. Recovery

For recoverable failures:

1. Preserve the last known valid state.
2. Record the failure.
3. Retry according to bounded retry policy.
4. Escalate after retry exhaustion.
5. Never fabricate a successful state transition.

For inconsistent state, create an `Incident` and require controlled remediation.

## 7. Versioning

State-machine definitions are versioned artifacts. Material lifecycle changes require an approved change record and migration/compatibility assessment.

Do not rename or reuse existing state identifiers without a migration decision.

## 8. Testing

Each production state machine requires tests for:

- Valid transitions
- Invalid transitions
- Preconditions
- Authorization failures
- Duplicate/retry behavior
- Concurrent update behavior where relevant
- Terminal-state enforcement
- Audit/event emission
- Recovery/escalation paths

## 9. Registry consistency

State-machine IDs must correspond to canonical entity IDs. Workflow and agent references must be validated against their respective registries before production activation.

## Definition of Done

A state machine is considered production-ready only when its definition, implementation, integration, tests, authorization, auditability, and recovery behavior are all evidenced.
