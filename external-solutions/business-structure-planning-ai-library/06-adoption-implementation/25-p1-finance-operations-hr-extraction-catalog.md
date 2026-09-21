# P1 Finance + Operations + HR Extraction Catalog

Research date: 2026-09-16

## Objective

Extract reusable skills, commands, connectors and agent patterns before building custom Nivy implementations.

## Finance & Accounting

| Asset | Reusable capability | Source | Nivy use | Control |
|---|---|---|---|---|
| journal-entry-prep | Prepare accrual, prepaid, payroll, fixed-asset and revenue-entry drafts | Anthropic Finance | Accounting delivery | Qualified review before posting |
| reconciliation | Compare GL/subledger/bank/third-party balances and identify breaks | Anthropic Finance | Bookkeeping QA | Human sign-off |
| financial-statements | P&L, balance sheet and cash-flow reporting with comparisons | Anthropic Finance | Client reporting | Accountant review |
| variance-analysis | Explain price/volume/rate/mix and budget variances | Anthropic Finance | CFO reporting | Evidence required |
| close-management | Month-end checklist, sequencing, dependencies and status | Anthropic Finance | Close service | Controller review |
| audit-support | Control testing/workpaper preparation | Anthropic Finance | Audit preparation | Professional review |
| cash-flow-snapshot | 30/60/90-day cash forecast and risk flags | Anthropic Small Business | SMB advisory | Data-quality check |
| margin-analyzer | Unit economics and pricing scenarios | Anthropic Small Business | Advisory | Assumptions documented |
| month-end-prep | Reconcile processors, identify gaps and prepare close packet | Anthropic Small Business | Bookkeeping | Human approval |

Anthropic's Finance plugin explicitly provides journal-entry preparation, reconciliation, financial statements, variance analysis, close management and audit support, with MCP categories for ERP/accounting, data warehouse, spreadsheets, BI, documents, email and chat. See the official source: https://github.com/anthropics/knowledge-work-plugins/tree/main/finance

## Operations

| Asset | Reusable capability | Source family | Nivy use |
|---|---|---|---|
| process-documentation | Convert recurring work into structured SOPs | Anthropic Operations | Delivery OS |
| process-optimization | Identify bottlenecks and improvement opportunities | Anthropic Operations | Continuous improvement |
| vendor-management | Vendor evaluation, records and review workflows | Anthropic Operations | Partner management |
| capacity-planning | Match workload, resources and deadlines | Anthropic Operations | VA/delivery planning |
| change-management | Track operational changes and approvals | Anthropic Operations | Controlled rollout |
| compliance-tracking | Track obligations and evidence | Anthropic Operations | Governance |
| status-reporting | Generate operational status and risk summaries | Anthropic Operations | Weekly management |
| runbook-generation | Create repeatable response/runbook documents | Anthropic Operations | Incident/delivery playbooks |

Operations connectors should remain category-based so the implementation can swap ITSM, project tracker, knowledge base, procurement, office and communication tools without rewriting the workflow.

## Human Resources

| Asset | Reusable capability | Source | Nivy use | Control |
|---|---|---|---|---|
| recruiting | Candidate pipeline and recruiting workflow | Anthropic HR | Hiring engine | Human decision |
| candidate-screening | Structured screening and evidence extraction | Anthropic HR | Applicant triage | Human review |
| onboarding | New-hire workflow and checklist | Anthropic HR | Employee onboarding | Manager approval |
| performance-review | Review preparation and evidence organization | Anthropic HR | People operations | Manager/HR review |
| compensation-analysis | Compensation data analysis | Anthropic HR | Workforce planning | Sensitive-data controls |
| policy-guidance | Retrieve/explain internal policies | Anthropic HR | Employee support | Policy source required |
| people-reporting | HR metrics and reporting | Anthropic HR | Management dashboard | Privacy controls |

HR connector categories include ATS, calendar, chat, email, HRIS, knowledge base and compensation data. The official connector model is tool-agnostic and supports alternatives rather than locking the workflow to one vendor.

## Additional reusable source

Anthropic's Small Business plugin is valuable as a cross-functional orchestration layer because it combines atomic skills, multi-step commands and a natural-language router. It includes cash-flow, invoice-chasing, margin, month-end, lead triage, content strategy and customer workflows.

## Extraction rule

Do not copy large source files into Nivy. Record the source, capability, license/access, inputs, outputs, dependencies, permissions and adaptation notes. Extract only the reusable structure needed for implementation.
