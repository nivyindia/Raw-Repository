# P1 Adoption Backlog

Research date: 2026-09-16

## Finance + Accounting

| Priority | Capability | Test | Production target |
|---|---|---|---|
| P0 | Reconciliation | Synthetic GL vs bank/subledger | Bookkeeping QA |
| P0 | Month-end close | Mock close packet | Client accounting workflow |
| P0 | Invoice follow-up | Synthetic overdue invoices | AR automation |
| P0 | Cash-flow forecast | Historical/sample data | Advisory dashboard |
| P1 | Journal-entry preparation | Sample transactions | Accountant workbench |
| P1 | Financial statements | Sample trial balance | Reporting package |
| P1 | Variance analysis | Budget vs actual dataset | CFO reporting |
| P2 | Audit/SOX support | Synthetic controls | Audit preparation |

## Operations

| Priority | Capability | Test | Production target |
|---|---|---|---|
| P0 | SOP generation | Existing process notes | Company SOP library |
| P0 | Status reporting | Mock project/task data | Weekly operations brief |
| P0 | Capacity planning | Synthetic workload | Resource allocation |
| P1 | Vendor management | Sample vendor records | Partner operations |
| P1 | Change management | Mock change requests | Controlled rollout |
| P1 | Runbook generation | Incident examples | Delivery/IT runbooks |
| P2 | Compliance tracking | Synthetic obligations | Governance dashboard |

## HR

| Priority | Capability | Test | Production target |
|---|---|---|---|
| P0 | Recruiting workflow | Synthetic candidates | Hiring pipeline |
| P0 | Candidate screening | Blind/sample profiles | Applicant triage |
| P0 | Onboarding | Mock new hire | Employee onboarding |
| P1 | Performance review prep | Synthetic review data | Manager workflow |
| P1 | Policy guidance | Approved policy set | HR assistant |
| P2 | Compensation analysis | Synthetic compensation data | Workforce planning |
| P2 | People reporting | Synthetic HR dataset | Management dashboard |

## Standard adoption sequence

1. Verify current source and license/access.
2. Capture exact inputs, outputs and dependencies.
3. Run unchanged where legally permitted.
4. Test on synthetic or sanitized data.
5. Measure accuracy, completeness and repeatability.
6. Adapt Nivy terminology, policies and output schema.
7. Add human approval checkpoints.
8. Integrate connectors and automation.
9. Run a limited production pilot.
10. Version and regression-test.
11. Promote only proven assets into the canonical Company OS.

## Hard controls

- Never allow an AI workflow to autonomously post accounting entries without required approval.
- Never treat AI output as tax, audit, legal or regulatory advice.
- Protect HR and financial data with least-privilege access.
- Keep source provenance and adaptation history.
- Log material automated actions.
- Separate drafting from approval/execution.
