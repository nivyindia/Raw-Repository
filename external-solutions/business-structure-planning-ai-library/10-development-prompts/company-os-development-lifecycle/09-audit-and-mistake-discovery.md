# Prompt 09 — Full Audit and Mistake Discovery

ROLE
Independent adversarial auditor. Do not defend the implementation.

OBJECTIVE
Find mistakes, omissions, contradictions, weak assumptions, dead ends, duplicated systems, hidden dependencies, security problems, untested behavior, stale documentation, poor reuse decisions, architectural debt and process failures.

AUDIT EVERY LEVEL
micro action → task → automation → workflow → business process → department → cross-department → manager → executive → control tower → autonomous company.

CHECK
- requirements coverage
- architecture consistency
- dependency order
- data/state correctness
- idempotency/concurrency
- authorization/authority
- failure/recovery
- observability/evidence
- security/privacy
- cost/resource limits
- tests/evaluation
- external integrations
- versioning/migration
- documentation
- reuse opportunities
- pending/deferred work
- production readiness

For each finding:
ID | severity | location | problem | evidence | impact | root cause | dependency | recommended correction | priority.

Do not fix during the audit unless explicitly instructed. Produce an auditable findings report.
