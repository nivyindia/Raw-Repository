# Employee & Workforce Operating System — Adoption Map

**Status:** v1.0 — 2026-09-16

## P0 adoption backlog

| ID | Capability | Reuse candidate | Test | Nivy destination |
|---|---|---|---|---|
| WF-01 | Employee/department/role master | HRKit | Functional + schema test | People Engine / Workforce Registry |
| WF-02 | Employee + manager dashboards | SmartHR Nexus / WorkSphere | UX + RBAC test | Employee/Manager Cockpits |
| WF-03 | Tasks and work queues | WorkSphere + existing task system | Workflow test | Work Management Layer |
| WF-04 | Role/KRA/KPI skills | HR Skills + KRA dashboard patterns | Skill-output test | Performance Layer |
| WF-05 | Goal cascade | Custom composition using reusable HR skills | Scenario test | Goal Management |
| WF-06 | Employee AI assistant | HRKit / SmartHR Nexus patterns | Knowledge + permissions test | Employee Copilot |
| WF-07 | Manager AI assistant | HR skills + workforce analytics | Scope + evidence test | Manager Copilot |
| WF-08 | Performance analytics | Employee Performance Analytics skill + HR analytics dashboards | Metric/evidence test | People Analytics |

## P1 adoption backlog

| ID | Capability | Candidate | Destination |
|---|---|---|---|
| WF-09 | Skill-gap analysis | AuraHR / HR Skills | Learning & Development |
| WF-10 | Career planning | AuraHR | Talent Development |
| WF-11 | Succession planning | Larger HR agent platforms | Talent / Leadership |
| WF-12 | Workload/capacity analysis | HR analytics + operations layer | Workforce Planning |
| WF-13 | Onboarding 30/60/90 | HRKit + onboarding skills | Employee Lifecycle |
| WF-14 | Performance-review preparation | HR Skills + performance systems | Performance Management |
| WF-15 | Department health dashboard | HR analytics patterns | Department Cockpit |
| WF-16 | Executive workforce dashboard | HR analytics + Executive OS | Executive Cockpit |

## Standard operating loop

`Role Definition → Goal Assignment → KRA/KPI Definition → Work Planning → Daily Execution → Evidence → Review → Coaching → Learning → Goal Refresh`

## Integration points

- HR/employee master
- Odoo or selected system of record
- Task/project system
- SOP/knowledge repository
- Attendance/time tracking
- CRM/delivery systems where work output originates
- GitHub for technical work evidence where appropriate
- Notion/company knowledge where appropriate
- n8n for notifications, scheduled reviews and workflow orchestration
- AI control plane for permissions, approvals and audit

## Definition of done

The workforce layer is ready for production only when:

1. Every employee has an approved role definition.
2. Every role has approved responsibilities and KRAs.
3. KPIs have definitions, targets, owners and data sources.
4. Daily/weekly recurring work is linked to roles and SOPs.
5. Employees have role-scoped work dashboards.
6. Managers have team-scoped dashboards.
7. Department heads have department-scoped dashboards.
8. Evidence is traceable to actual work outputs.
9. AI recommendations are explainable and reviewable.
10. HR-sensitive data has RBAC, audit and retention controls.
11. Performance workflows have human approval.
12. Metrics can flow into the Executive Company OS.
