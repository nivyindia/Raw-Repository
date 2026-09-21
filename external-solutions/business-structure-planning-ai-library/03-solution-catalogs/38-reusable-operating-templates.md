# Reusable Operating Templates

**Purpose:** Ready-to-adapt structures derived from the completed company capability and cross-cutting discovery work. These are original Nivy-neutral templates, not copied third-party text.

## 1. Capability record

```yaml
capability_id:
name:
business_outcome:
owner:
value_streams: []
processes: []
systems: []
agents: []
skills: []
data_inputs: []
outputs: []
kpis: []
risks: []
controls: []
status: discovery|tested|approved|production|retired
```

## 2. Reusable solution record

```yaml
solution_id:
name:
type: system|platform|agent-team|agent|plugin|skill|command|prompt|mcp|api|workflow|rpa|sop|framework|template|checklist|dataset|dashboard
source:
source_url:
publisher:
license:
access: open-source|free|freemium|paid|commercial|unknown
maintenance_status:
last_verified:
departments: []
capabilities: []
inputs: []
outputs: []
connectors: []
permissions: []
data_sensitivity:
human_approval:
security_notes:
quality_notes:
reuse_mode: direct|adapt|reference-only|do-not-use
nivy_destination:
test_status:
```

## 3. Agent intake checklist

- [ ] Business outcome defined
- [ ] Owner assigned
- [ ] Allowed data defined
- [ ] Allowed tools defined
- [ ] Least-privilege permissions configured
- [ ] Human approval points defined
- [ ] Failure/rollback behavior defined
- [ ] Evaluation dataset available
- [ ] Security/adversarial tests run
- [ ] Audit logging enabled
- [ ] Cost/latency limits defined
- [ ] Version recorded
- [ ] Production approval recorded

## 4. Process/SOP template

```text
TITLE:
PURPOSE:
TRIGGER:
OWNER:
SCOPE:
INPUTS:
PRECONDITIONS:
ROLES:
SYSTEMS:
STEPS:
DECISION POINTS:
EXCEPTIONS:
ESCALATION:
QUALITY CHECKS:
OUTPUTS:
KPIs:
EVIDENCE/LOGS:
REVIEW FREQUENCY:
RELATED PROCESSES:
VERSION:
```

## 5. Workflow template

`Trigger → Validate → Enrich → Decide → Execute → Verify → Record → Notify → Escalate if needed`

Every automation should define idempotency, retries, timeout, failure destination and human fallback.

## 6. AI skill template

```markdown
# Skill

## Purpose

## Trigger

## Required inputs

## Preconditions

## Procedure
1.
2.
3.

## Output schema

## Quality checks

## Failure conditions

## Human approval

## Tools/connectors

## Data sensitivity

## Examples

## Evaluation cases

## Version
```

## 7. Prompt template

```text
ROLE
You are [specialist].

OBJECTIVE
Produce [business outcome].

CONTEXT
[company/process/customer context]

INPUTS
[data required]

RULES
- Follow approved policy.
- Do not invent missing facts.
- Cite or identify source data where applicable.
- Escalate when authority is insufficient.

PROCESS
1. Validate inputs.
2. Analyze.
3. Produce structured output.
4. Run quality checks.
5. Identify uncertainty.

OUTPUT FORMAT
[exact schema]

APPROVAL
[when human review is required]
```

## 8. Agent evaluation card

| Dimension | Test |
|---|---|
| Task success | Does it complete the intended task? |
| Factuality | Are claims grounded in approved sources? |
| Instruction following | Does it follow required procedure? |
| Tool safety | Are tool calls permitted and necessary? |
| Data protection | Does it avoid unauthorized disclosure? |
| Robustness | Does it survive ambiguous/adversarial input? |
| Consistency | Does it regress across versions? |
| Cost | Is spend within budget? |
| Latency | Is response time acceptable? |
| Human handoff | Does it escalate correctly? |
| Auditability | Can actions be reconstructed? |

## 9. Vendor evaluation scorecard

Use factual fields rather than a single subjective score:

- Functional coverage
- Integration availability
- API quality
- Security controls
- Data residency
- License/contract
- Total cost
- Exit/migration path
- Maintenance history
- Community/vendor support
- Compliance documentation
- Permission model
- Observability

## 10. Data asset card

```yaml
asset_id:
name:
type:
owner:
source:
definition:
sensitivity:
quality_checks: []
freshness:
lineage:
retention:
allowed_users: []
allowed_agents: []
contract:
lifecycle:
```

## 11. Change request

```text
CHANGE:
REASON:
SYSTEM/PROCESS:
CURRENT STATE:
TARGET STATE:
IMPACTED TEAMS:
DATA IMPACT:
SECURITY IMPACT:
CUSTOMER IMPACT:
TRAINING REQUIRED:
TEST PLAN:
ROLLBACK PLAN:
APPROVERS:
ROLLOUT DATE:
ADOPTION KPI:
POST-CHANGE REVIEW:
```

## 12. Incident/postmortem

```text
INCIDENT:
DATE/TIME:
IMPACT:
DETECTION:
TIMELINE:
ROOT CAUSE:
CONTRIBUTING FACTORS:
CONTAINMENT:
RECOVERY:
CUSTOMER COMMUNICATION:
WHAT WORKED:
WHAT FAILED:
CORRECTIVE ACTIONS:
OWNER:
DUE DATE:
VERIFICATION:
```

## 13. Business continuity record

```text
BUSINESS SERVICE:
OWNER:
CRITICALITY:
MAXIMUM TOLERABLE DOWNTIME:
RTO:
RPO:
DEPENDENCIES:
BACKUP:
RESTORE METHOD:
ALTERNATE SERVICE:
KEY CONTACTS:
COMMUNICATION CHANNEL:
TEST FREQUENCY:
LAST TEST:
RESULT:
GAPS:
```

## 14. Document lifecycle record

`Draft → Review → Approval → Published → Periodic Review → Superseded → Archived → Disposed`

Required controls: version, owner, approver, effective date, review date, source/provenance, access classification.

## 15. Customer lifecycle workflow

`Traffic → Lead → Qualification → Discovery → Proposal → Contract → Payment → Onboarding → Delivery → QA → Support → Renewal → Expansion → Referral`

For each stage define:
- trigger
- owner/agent
- required data
- automation
- human approval
- KPI
- exit condition
- exception path

## 16. Research-to-reuse workflow

`Question → Scope → Search → Source Capture → License Check → Capability Extraction → Test → Compare → Adapt → Approve → Catalog → Integrate → Monitor`

## 17. Research source ledger

| Date | Query | Capability | Source | URL | Asset type | License/access | Evidence | Decision | Owner | Next action |
|---|---|---|---|---|---|---|---|---|---|---|

## 18. Continuous-improvement loop

`KPI variance → Diagnose → Root cause → Improvement hypothesis → Experiment → Measure → Standardize → Update SOP/skill/agent → Regression test`

## 19. Nivy production gate

A reusable asset may move from research to production only when:

1. Source and provenance are recorded.
2. License/access permits intended use.
3. Security and data permissions are understood.
4. Synthetic/sanitized testing is complete.
5. Quality meets the required threshold.
6. Human approval boundaries are documented.
7. Failure and rollback behavior exists.
8. Version and adaptation history are recorded.
9. Monitoring is available.
10. An owner accepts operational responsibility.

## 20. Build-only-the-gap rule

Build custom software/agents only when at least one is true:

- No suitable reusable asset exists.
- Existing asset cannot meet a required control or integration.
- License prevents the intended deployment.
- Testing shows inadequate reliability after reasonable adaptation.
- Required differentiation is strategically specific to Nivy.
- Operational cost of adapting an existing asset is demonstrably higher than building the missing component.
