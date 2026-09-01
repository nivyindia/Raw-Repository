# BILLION DREAMS UNITED OS — AGENT EXECUTION CONTRACT

**Stage:** C.5  
**Version:** 1.0  
**Status:** Baseline locked

## Purpose

Define the runtime contract an AI agent must satisfy before, during, and after executing a task.

## 1. Execution lifecycle

`Receive → Validate → Authorize → Plan → Execute → Verify → Commit/Report → Audit`

An agent must not skip validation or authorization for governed actions.

## 2. Required execution context

Every run should carry:

- `agent_id`
- `agent_version`
- `run_id`
- `company_id`
- `actor_id` where applicable
- `task_id` where applicable
- `correlation_id`
- `input_schema_version`
- `started_at`
- permission/tool scope

## 3. Input validation

Before execution the agent must:

1. Validate input schema.
2. Confirm required fields.
3. Validate entity references.
4. Check company/tenant scope.
5. Check authorization.
6. Check required approvals.
7. Identify ambiguity or missing information.

Ambiguous high-impact instructions must be escalated rather than guessed.

## 4. Capability resolution

Runtime capability must resolve through:

`Agent → Approved Skill → Approved Tool → Authorized Action`

Undeclared capabilities are denied by default.

## 5. Execution behavior

Agents should:

- Prefer deterministic operations for deterministic tasks.
- Keep side effects bounded and observable.
- Use correlation IDs across downstream calls.
- Apply timeouts and bounded retries.
- Avoid duplicate side effects through idempotency controls.
- Preserve source provenance for externally derived information.

## 6. Human approval

Human approval is required whenever policy marks an action as high-impact, irreversible, financially material, externally binding, or otherwise restricted.

Approval must be obtained **before** the protected side effect occurs.

## 7. Output contract

Agent output should identify:

- `run_id`
- `status: success|partial|failed|escalated`
- structured result
- actions performed
- records changed
- evidence/provenance references where applicable
- errors/warnings
- recommended next action

An agent must never report an action as completed when the underlying operation failed or was not executed.

## 8. Verification

Before reporting success, the agent must verify the expected postcondition where technically possible. For state-changing operations, confirmation should come from the authoritative system of record rather than an unverified local assumption.

## 9. Failure and recovery

On failure:

1. Preserve the last known valid state.
2. Classify the error.
3. Retry only when safe and within policy.
4. Escalate after bounded retry exhaustion.
5. Record an auditable failure event.
6. Never fabricate success.

## 10. Security

- Secrets must be supplied through approved secret-management mechanisms.
- Secrets must never appear in prompts, logs, outputs, repository files, or event payloads.
- Tool permissions are least-privilege.
- Sensitive data is disclosed only to authorized destinations.

## 11. Observability

Production runs must make it possible to trace:

`run_id → agent → skill → tool → action → result → event`

Material failures, approvals, state transitions, and external side effects must be auditable.

## 12. Evaluation

Agents must be evaluated against defined criteria before production activation and after material changes. Evaluation results are evidence, not authorization by themselves.

## 13. Versioning

Agent, skill, tool, input/output, and execution-contract versions must be tracked. Breaking changes require compatibility assessment and controlled rollout.

## Definition of Done

An agent is production-ready only when its identity, skills, tools, permissions, input/output contracts, approval requirements, tests/evaluations, observability, failure handling, and versioning are implemented and evidenced.
