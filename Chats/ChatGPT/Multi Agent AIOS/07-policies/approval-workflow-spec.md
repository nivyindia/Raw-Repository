# AIOS Approval Workflow Specification

**Spec ID:** APPROVAL-WORKFLOW-001  
**Version:** 1.0  
**Status:** Proposed  
**Owner:** Billion Dreams United AIOS Governance

## 1. Purpose

Define the canonical n8n orchestration pattern for AIOS actions that require human approval before execution. This is a workflow specification only; it does not deploy or execute an n8n workflow.

The workflow implements the required sequence:

`event → policy/risk evaluation → approval request → human task/notification → wait → approve/reject → emit event → gated execution`

## 2. Source-of-truth policies

- `07-policies/permission-matrix.yaml`
- `07-policies/ai-risk-policy.yaml`
- `07-policies/communication-policy.yaml`
- `07-policies/suppression-list-data-model.yaml`
- `07-policies/odoo-approval-request-model.yaml`

The Odoo approval request model is the system-of-record for approval state. n8n orchestrates; n8n must not become an independent approval database.

## 3. Canonical flow

```text
┌──────────────────────────────┐
│ 1. GOVERNED EVENT            │
│ approval candidate/action    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 2. NORMALIZE + CORRELATE     │
│ request_id / correlation_id  │
│ idempotency_key              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 3. POLICY + RISK EVALUATION  │
│ Agent→Skill→Tool→Action      │
│ Resolve L0–L4 + policy basis │
└──────────────┬───────────────┘
               │
        ┌──────┴───────┐
        │               │
   approval needed    blocked/no approval
        │               │
        ▼               ▼
┌────────────────┐  ┌──────────────────┐
│ 4. CREATE      │  │ DENY / COMPLETE  │
│ Odoo approval  │  │ audit + event    │
│ request        │  └──────────────────┘
└───────┬────────┘
        │
        ▼
┌──────────────────────────────┐
│ 5. CREATE HUMAN TASK         │
│ Odoo activity / governed     │
│ notification                 │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 6. WAIT                       │
│ webhook/callback or polling  │
│ until decision/expiry         │
└──────────────┬───────────────┘
               │
        ┌──────┴────────┐
        │               │
      approve         reject/expire/cancel
        │               │
        ▼               ▼
┌────────────────┐  ┌──────────────────┐
│ 7A. RECHECK    │  │ 7B. TERMINATE    │
│ policy/scope/  │  │ no execution     │
│ expiry         │  │ emit rejection   │
└───────┬────────┘  └──────────────────┘
        │
        ▼
┌──────────────────────────────┐
│ 8. EMIT approval.granted     │
│ + approval reference         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 9. EXECUTION GATE            │
│ exact action/scope/policy    │
│ + unexpired approval         │
└──────────────┬───────────────┘
               │
        ┌──────┴───────┐
        │               │
       pass            fail
        │               │
        ▼               ▼
┌────────────────┐  ┌──────────────────┐
│ 10. EXECUTE    │  │ BLOCK + ESCALATE │
│ exact action   │  │ audit failure    │
└───────┬────────┘  └──────────────────┘
        │
        ▼
┌──────────────────────────────┐
│ 11. UPDATE ODOO REQUEST      │
│ executed / failed + result   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 12. EMIT FINAL EVENT         │
│ approval.executed/failed     │
└──────────────────────────────┘
```

## 4. n8n logical nodes

| # | Logical node | Responsibility | Failure behavior |
|---|---|---|---|
| 1 | Trigger | Receive governed event or internal workflow call | Reject malformed event |
| 2 | Normalize Request | Build stable IDs and canonical action context | Stop if required fields missing |
| 3 | Policy Evaluation | Resolve policy, authorization and L0–L4 risk | Deny/escalate on uncertainty |
| 4 | IF Approval Required | Route approval-required vs no-approval paths | Default deny |
| 5 | Odoo Create/Update | Persist `approval.request` | Stop if persistence fails |
| 6 | Human Task | Create Odoo activity/approved notification | Stop if task creation fails |
| 7 | Wait/Callback | Suspend until decision, expiry or cancellation | Expire safely |
| 8 | Odoo Decision Read | Read authoritative approval state | Never trust callback alone |
| 9 | Decision Switch | approved/rejected/expired/cancelled | Non-approved states terminate |
| 10 | Recheck Gate | Revalidate policy, scope, identity and expiry | Block + escalate |
| 11 | Execute Action | Call only the pre-authorized action | No fallback outside scope |
| 12 | Odoo Finalize | Persist executed/failed result | Audit failure blocks completion |
| 13 | Event Emit | Emit governed approval/execution event | Do not fabricate success |

## 5. Required input contract

```text
request_id
correlation_id
idempotency_key
requester_type
requester_id
agent_id (when applicable)
action_type
action_reference
target_reference
risk_level
policy_id
policy_version
requested_scope
reason
proposed_payload_reference (when applicable)
expires_at (when applicable)
```

## 6. Approval decision contract

### Approve

Required:

```text
request_id
approver_id
approval_comment
decision_at
```

The approval applies only to the exact `action_reference`, `target_reference`, requested scope, policy version and expiry recorded in the request.

### Reject

Required:

```text
request_id
approver_id
approval_comment
 decision_at
```

A rejected request must never enter the execution path.

### Expire

A request automatically becomes `expired` when its governed expiry time passes. Expiry must be checked immediately before execution.

## 7. Event lifecycle

```text
approval.requested
        ↓
approval.granted ───────────────┐
        │                       │
        ▼                       │
 governed action                │
        │                       │
        ▼                       │
approval.executed               │
                                │
OR                              │
                                │
approval.rejected                │
                                │
OR                              │
                                │
approval.expired / cancelled     │
                                │
        └───────────────→ terminal state
```

Only the authoritative Odoo approval state can establish whether an approval exists.

## 8. Human task routing

Approver selection must be policy-driven and must resolve to an authorized human identity.

```text
risk/action
    ↓
policy-defined approver role
    ↓
authorized Odoo user
    ↓
Odoo activity + governed notification
```

Rules:

- AI cannot select an arbitrary approver to bypass governance.
- Requester should not approve its own material request by default.
- Material actions require separation of duties where policy requires it.
- Missing or ambiguous approver authority blocks the workflow.

## 9. Wait strategy

Preferred pattern:

```text
Create approval request
        ↓
Create human task
        ↓
Wait for signed/authorized decision callback
        ↓
Read Odoo approval.request
        ↓
Validate decision
```

Polling may be used where callbacks are unavailable, but every poll must read authoritative state and respect timeout/expiry. Do not hold credentials or secrets in a long-lived workflow payload.

## 10. Execution gate

Execution is permitted only when all conditions are true:

```text
approval.state == approved
AND policy_version == current_required_version
AND action_reference == requested_action
AND target_reference == requested_target
AND requested_scope == execution_scope
AND approver is authorized
AND approval is not expired
AND idempotency_key is valid
AND correlation_id is valid
AND all communication/consent/suppression gates pass when applicable
```

Any false condition → **block and escalate**.

## 11. Idempotency and duplicate protection

- `request_id` must be unique.
- `idempotency_key` must be unique for the action attempt.
- Replayed `approval.granted` events must not execute the action twice.
- Execution must use a durable idempotency check before side effects.
- Duplicate approval requests for the same action should resolve to the existing request where policy permits.

## 12. Error handling

| Failure | Action |
|---|---|
| Invalid event | Reject + audit |
| Missing policy | Deny + escalate |
| Risk cannot be resolved | Deny + escalate |
| Odoo request creation fails | Stop; do not execute |
| Human task creation fails | Stop; alert governance |
| Approval timeout | Expire + emit event |
| Rejected | Mark rejected + terminate |
| Approval state unavailable | Fail closed |
| Approval scope mismatch | Block + escalate |
| Policy version mismatch | Block + request reapproval |
| Execution failure | Mark failed + audit + alert |
| Audit persistence failure | Block completion |

## 13. Security boundaries

- n8n credentials are stored only in the n8n credential store.
- Approval decisions are not accepted solely from untrusted query parameters.
- External callbacks must be authenticated/signed according to the webhook security standard.
- n8n cannot grant itself additional permissions.
- Human approval cannot override prohibited behavior, consent, suppression, legal, platform or security constraints.
- L4 actions remain prohibited for autonomous AI execution.

## 14. Observability

Every request should be traceable using:

```text
request_id
correlation_id
idempotency_key
audit_reference
policy_id + policy_version
agent_id
workflow_id / workflow_execution_id
approver_id (when applicable)
```

Recommended metrics:

- approval requests created
- average approval latency
- approval/rejection/expiry counts
- execution blocks
- policy mismatches
- duplicate execution prevention
- workflow failures
- audit failures

## 15. Test cases before implementation

1. L0 read-only action bypasses approval path.
2. L1 reversible internal action follows policy-defined autonomous path.
3. L2 action requiring approval creates an Odoo request.
4. L3 action cannot execute before human approval.
5. Rejected approval cannot execute.
6. Expired approval cannot execute.
7. Scope changed after approval forces reapproval.
8. Policy version changed after approval blocks execution.
9. Duplicate callback cannot execute action twice.
10. Odoo approval state unavailable fails closed.
11. Unauthorized approver cannot grant approval.
12. Audit persistence failure prevents successful completion.
13. Suppressed communication remains blocked even after approval.
14. L4 autonomous execution is rejected regardless of approval workflow input.

## 16. Implementation boundary

This document defines orchestration and governance behavior only. It does **not**:

- create the n8n production workflow;
- create Odoo custom Python modules;
- create credentials or secrets;
- authorize a specific human approver;
- define business-specific monetary thresholds;
- override applicable law, platform policy, or security controls.

**Completion criterion:** the specification is complete when the event-to-task-to-wait-to-decision-to-event flow, execution gates, failure paths, audit context and test cases are explicitly defined.