# Canonical AI Employee Contract

Status: Draft for Nivy adaptation from Wave 4/5 research.

## Contract
Identity → Mission → Responsibilities → Context → Memory → Skills → Tools → Policies → Authority → Approvals → Execution → Verification → KPI/Reporting → Escalation → Learning → Lifecycle

## Required fields
- employee_id
- role
- department
- manager_id
- mission
- responsibilities
- inputs
- outputs
- skills
- tools
- allowed_data
- prohibited_actions
- authority_level
- approval_rules
- escalation_rules
- KPI/SLA
- memory_scope
- audit_requirements
- lifecycle_state
- version

## Safety
- Least privilege by default.
- No source-repository policy becomes Nivy policy automatically.
- External side effects require an explicit authority rule.
- Sensitive data must be scoped and logged.
- Every consequential action must be attributable to employee, manager, tool and policy version.
- Human approval is mandatory where policy requires it.

## Lifecycle
Create → Qualify → Assign → Activate → Observe → Evaluate → Upgrade/Restrict → Suspend → Retire → Archive.
