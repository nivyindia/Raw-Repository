# Employee & Workforce Operating System — Reuse Catalog

**Status:** v1.0 — 2026-09-16  
**Purpose:** Discover and reuse ready-made employee dashboards, role/KRA/KPI systems, task management, performance workflows, manager dashboards, workforce analytics and AI HR skills before building a custom Nivy workforce layer.

## Core principle

`Company Goals → Department Goals → Team Goals → Role Responsibilities → KRAs → KPIs → Daily/Weekly/Monthly Work → Evidence → Review → Development`

This is broader than an HRMS. The target is a **Workforce Operating System** where every employee has a role-aware work cockpit and every manager/department head has the corresponding management cockpit.

## Ready-made solution candidates

| Asset | Type | Relevant capabilities | Reuse priority | Source |
|---|---|---|---|---|
| WorkHub | Open-source HR/workforce dashboard | Employee/manager/HR dashboards, RBAC, leave, personalization, AI assistance | P0 | https://github.com/Alen983/WorkHub |
| HRKit | Open-source local HR app | Employees, departments, roles, manager hierarchy, org chart, performance, onboarding/offboarding, recruitment, BYOK AI assistant | P0 | https://github.com/AnitChaudhry/HRKit |
| WorkSphere HR Dashboard | Open-source dashboard | Employee/department views, attendance, requests, tasks, progress, analytics and performance metrics | P0 | https://github.com/aimenyusra/hr-management-dashboard |
| SmartHR Nexus | Open-source AI HRMS | Role-based employee/manager/admin dashboards, departments, performance, attendance, AI HR assistant | P0 | https://github.com/adityakr1108/SmartHR-Nexus-AI-Workforce-Platform |
| Orbit HRMS | Open-source HRMS | Employee dashboard, attendance, leave, profiles, RBAC, HR/admin dashboards, AI HR assistant | P1 | https://github.com/rajnarharia/Orbit-HRMS |
| AuraHR | Open-source AI HRMS | 360° performance, skill-gap analysis, career planning, employee/manager analytics and AI | P1 | https://github.com/pkparthk/AuraHR---The-Next-Generation-AI-Powered-HRMS |
| HR Skills | Reusable AI skill library | Performance management, workforce planning, HR analytics, employee experience, learning/development and HR workflows | P0 | https://github.com/tuanductran/hr-skills |
| Employee Performance Analytics HR Skill | AI skill | KPI aggregation, departmental insights, performance reporting, efficiency/workload analysis | P1 | https://github.com/aradotso/data-skills/tree/main/skills/employee-performance-analytics-hr |
| Foreign Worker / HR Agent Platform | Open-source agent system | 50 agents, 123 skills, performance, learning, succession, workforce planning, ESS/MSS, workflow/SOP automation and analytics | P1 | https://github.com/kk666679/Dashboardhr |
| HR Analytics Dashboard | Open-source analytics | Employee performance, attendance, workforce analysis, segmentation and interactive HR metrics | P1 | https://github.com/salmanfarist2006/HR-ANALYTICS-DASHBOARD |
| Employee KRA Dashboard | Ready-made dashboard template | Role-based KRA dashboards, employee data, performance metrics and KRA ratings | P1 | https://blink.new/p/employee-kra-dashboard-r4953uaq |

**Verification note:** These are discovery candidates. License, maintenance, security, actual feature depth and production readiness must be rechecked before adoption.

## Workforce capabilities to reuse

### 1. Organization structure

- Company → department → team → employee hierarchy
- Department head and manager assignment
- Direct reports
- Org chart
- Role and level definitions
- Reporting relationships
- Role-based access control

### 2. Employee cockpit

Each employee should have:

- Profile
- Job title and level
- Manager
- Department
- Job purpose
- Responsibilities
- KRAs
- KPIs
- Daily tasks
- Weekly recurring tasks
- Monthly responsibilities
- Projects
- Work queue
- Deadlines
- Priorities
- SOP links
- Checklists
- Training/learning plan
- Performance history
- Skills matrix
- Goals
- Blockers
- Approvals
- AI assistant

### 3. Manager cockpit

- Team roster
- Today's attendance/status
- Team work queue
- Task completion
- Overdue work
- KRA/KPI progress
- Workload/capacity
- Blockers
- Leave/approval queue
- Performance-review status
- Skill gaps
- Coaching/development actions
- Escalations

### 4. Department-head cockpit

- Department objectives
- Department KPIs/KRAs
- Team performance
- Capacity/utilization
- Projects
- SLA performance
- Cost/budget
- Hiring requirements
- Skill gaps
- Risks/exceptions
- Cross-team dependencies

### 5. Executive cockpit

- Company goals
- Department health
- Revenue/productivity
- Workforce capacity
- Critical exceptions
- Hiring needs
- Performance trends
- Cost per function
- Organizational risks
- AI-agent/workforce automation health

## AI agent / skill layer

| Agent | Core job |
|---|---|
| Role Architect | Define role purpose, authority, responsibilities and level |
| JD Generator | Create/revise job descriptions from approved role definitions |
| Responsibility Mapper | Map company processes/SOPs to role responsibilities |
| KRA Generator | Convert role responsibilities into measurable KRAs |
| KPI Generator | Define measurable indicators and target formulas |
| Goal Cascade Agent | Cascade company goals to departments, teams and roles |
| Task Planner | Convert KRAs/projects into daily and weekly work |
| Daily Work Agent | Generate each employee's prioritized work queue |
| Task Assignment Agent | Assign work based on role, capacity and priority |
| Performance Agent | Monitor KPI/KRA progress and prepare insights |
| Evidence Collector | Link outputs, tasks and records to performance evidence |
| Performance Review Agent | Prepare review summaries for manager/human approval |
| Skill Gap Agent | Identify missing capabilities against role requirements |
| Learning Agent | Build role-specific development plans |
| Manager Copilot | Answer team status, workload, performance and blocker questions |
| Employee Copilot | Explain role, priorities, SOPs, tasks and next actions |
| Department Head Agent | Monitor department goals, capacity, risks and exceptions |
| Workload Agent | Detect overload, under-utilization and capacity conflicts |
| Accountability Agent | Track commitments, deadlines and overdue work |
| SOP Agent | Connect tasks to approved SOPs/checklists |
| Escalation Agent | Escalate blocked, overdue or high-risk work |
| Onboarding Agent | Generate role-specific 30/60/90-day plans |
| Offboarding Agent | Coordinate knowledge transfer and asset-return workflows |
| Recognition Agent | Surface documented achievements for manager review |

## Role/KRA/KPI data model

```text
Company Goal
  ↓
Department Goal
  ↓
Team Goal
  ↓
Role Purpose
  ↓
Responsibility
  ↓
KRA
  ↓
KPI
  ↓
Target
  ↓
Task / Work Item
  ↓
Output / Evidence
  ↓
Review
  ↓
Development / Corrective Action
```

Every KPI should have an owner, formula/definition, target, measurement frequency, data source, reporting period and approval rule.

## Recommended employee dashboard

```text
TODAY
────────────────────────
Priority tasks
Due today
Overdue
Blocked
Approvals

MY PERFORMANCE
────────────────────────
KRA achievement
KPI achievement
Task completion
SLA/quality

MY DEVELOPMENT
────────────────────────
Skill gaps
Learning plan
Current goals

MY AI ASSISTANT
────────────────────────
What should I work on next?
Why is it a priority?
Which SOP applies?
What is blocking me?
```

## Recommended manager dashboard

```text
TEAM HEALTH
────────────────────────
Headcount
Available capacity
Task completion
KRA achievement
KPI achievement
SLA/quality

ATTENTION REQUIRED
────────────────────────
Overdue work
Blocked work
Overloaded employees
Under-utilized capacity
KPI exceptions
Pending approvals
```

## Nivy implementation target

Do **not** immediately build a custom HR dashboard. First test whether one or more existing HR/workforce systems can provide the base data model and UI, then compose AI skills and automation around it.

Target architecture:

`HR/Employee System → Role & Org Model → Goal/KRA/KPI Layer → Task/Work Layer → SOP/Knowledge Layer → AI Employee Copilot → Manager/Department Cockpits → Performance/Evidence → Analytics → Executive OS`

### Reuse strategy

1. Test HRKit for the foundational employee/department/role/org model.
2. Test WorkSphere/SmartHR Nexus/Orbit for dashboard and task UX patterns.
3. Test HR Skills for reusable AI role/performance/workforce capabilities.
4. Test the larger agent platform for advanced performance, learning, succession and workflow patterns.
5. Reuse/adapt rather than fork unless a material requirement is missing.
6. Keep the Nivy role/KRA/KPI schema independent from any one UI so the backend can later connect to Odoo/Notion/other systems.

## Controls

- Employee should see only authorized personal/team information.
- Managers should see only their reporting scope unless explicitly authorized.
- Performance recommendations are decision support, not automatic employment decisions.
- AI-generated KRAs/KPIs require human review before becoming official targets.
- AI performance summaries must cite source evidence.
- Sensitive HR data requires strict permissions, audit logging and retention rules.
- Do not use opaque AI scores as the sole basis for hiring, firing, promotion, compensation or disciplinary action.

## Research status

**Discovery status:** P0/P1 candidates identified.  
**Next status:** source/license verification → functional test → controlled pilot → Nivy adaptation.

## Related library areas

- HR / People
- Operations
- Process Intelligence
- Knowledge Management
- AI Governance / AgentOps
- Executive Company OS
- Task / project management
- Analytics / dashboards
