# Unified Company UI / Workspace Resource Catalog

Purpose: reusable open-source/self-hosted building blocks for one Nivy-style company workspace instead of separate UIs for owner, executives, departments, managers, employees, documents, analytics, projects and AI agents.

## Core design target

| Surface | What should appear |
|---|---|
| Owner / CEO | company health, strategy, revenue, cash, goals, departments, people, risks, AI workforce, approvals |
| Executive / Director | assigned business units, KPIs, budgets, initiatives, exceptions, approvals |
| Department Head | department goals, people, workload, KPIs, projects, SOPs, documents, AI agents |
| Manager | team tasks, performance, approvals, meetings, projects, exceptions |
| Employee | personal dashboard, tasks, goals, attendance/leave, documents, learning, requests, AI assistant |
| AI Admin / Operator | agents, skills, workflows, runs, costs, memory, permissions, approvals, audit |
| Company-wide | org chart, directory, documents, knowledge, search, calendar, announcements, dashboards |
| Analytics | revenue, sales, marketing, finance, HR, operations and custom BI dashboards |
| Documents | company → department → team → employee/project/customer/vendor access with RBAC |

These resources are building blocks, not a finished Nivy UI. The target is a unified shell + role-aware navigation + shared identity/RBAC + common search + document/knowledge layer + embedded analytics + business/ERP data + AI control plane.

## Reusable UI / application foundations

| Resource | Type | Useful for Nivy | Link |
|---|---|---|---|
| Refine | React framework | Data-heavy admin panels, CRUD, RBAC/resource navigation, internal tools | https://github.com/refinedev/refine |
| shadcn/ui | UI component system | Accessible, customizable foundation for the Nivy design system | https://ui.shadcn.com/ |
| shadcn Dashboard | Open-source dashboard starter | Sidebar, dashboards, tables, forms, auth, profiles, notes/tickets | https://github.com/shadcndashboard/shadcndashboard |
| Shadcn Admin | Open-source admin template | Analytics, user management, settings, command palette, responsive admin UI | https://github.com/satnaing/shadcn-admin |
| Shadboard | Next.js + shadcn admin template | Another reusable dashboard shell/reference implementation | https://github.com/Qualiora/shadboard |
| Tremor | React dashboard library | KPI cards, charts, tables and analytics surfaces | https://github.com/tremorlabs/tremor |
| Appsmith | Open-source internal-tool builder | Fast custom dashboards, admin panels, operational apps and API/database UI | https://github.com/appsmithorg/appsmith |
| NocoDB | Open-source database UI | Company data tables, views, forms, role-aware operational interfaces | https://github.com/nocodb/nocodb |
| Jetro | Open-source AI canvas | Visual AI workspace, research and live-dashboard surface | https://jetro.ai/ |

## Company / employee portal references

| Resource | Type | Useful for Nivy | Link |
|---|---|---|---|
| Nexus ECM | Open-source company management platform | HR, attendance, leave, projects, finance, inventory, CRM, documents, chat, executive dashboard | https://github.com/fsocietry/nexus-ecm |
| HRMS Portal | Next.js employee/admin portal | Employee self-service + HR admin console; useful reference for role-separated UI | https://github.com/ydvlalit03/hrms-portal |
| StaffPortal | Self-hosted workforce portal | Attendance, leave, timesheets, expenses, IT support, role-based login and AI assistant | https://github.com/sarmakska/staff-portal |
| Plane | Open-source project management | Projects, issues, cycles, roadmaps, docs; can be integrated into the company operating layer | https://github.com/makeplane/plane |

## Company files / documents / knowledge

| Resource | Type | Useful for Nivy | Link |
|---|---|---|---|
| Nextcloud | Self-hosted collaboration/file platform | Central company files, sharing, contacts, calendars and apps | https://github.com/nextcloud/server |
| Paperless-ngx | Open-source DMS | Searchable document archive, OCR, tags and document metadata | https://github.com/paperless-ngx/paperless-ngx |
| Outline | Open-source collaborative knowledge base | Company wiki, SOPs, policies, departmental knowledge and documentation | https://github.com/outline/outline |
| AppFlowy | Open-source workspace | Projects, wikis, databases and team knowledge with local/data-control focus | https://github.com/AppFlowy-IO/AppFlowy |
| AFFiNE | Open-source knowledge/planning workspace | Docs + whiteboard + tables + digital assets; useful for strategy/planning UX | https://github.com/toeverything/AFFiNE |

## Embedded analytics / BI

| Resource | Type | Useful for Nivy | Link |
|---|---|---|---|
| Metabase | Open-source BI | Embed dashboards/questions into Nivy; role-aware analytics and data exploration | https://github.com/metabase/metabase |
| Apache Superset | Open-source BI | Embedded dashboards, filters and large-scale analytics | https://github.com/apache/superset/superset |
| Metabase embedding reference apps | Integration examples | Reference implementation for embedding BI inside a React/web app | https://github.com/metabase/static-embedding-reference-apps |

## AI company / agent-control UI references

| Resource | Type | Useful for Nivy | Link |
|---|---|---|---|
| Bizbox | Open-source AI company orchestration | Goals, AI org chart, budgets, governance, agent coordination, audit and dashboard | https://github.com/zesthq/bizbox |
| Agentic Business Framework (ABF) | Open-source agentic business framework | Business plan → agent team → roles/tools/memory/workflows + web dashboard | https://github.com/alexclowe/abf |
| Appsmith Agents | AI/internal-tools direction | Reference for putting AI agents inside business applications and operational workflows | https://github.com/appsmithorg/appsmith |

## Recommended Nivy UI architecture

Do not build one dashboard per department as isolated software.

Build one shell:

Nivy Workspace
→ Global Search / Command Palette
→ Home
→ My Work
→ Company
→ People
→ Departments
→ Customers / Leads
→ Projects
→ Finance
→ Documents
→ Knowledge / SOPs
→ Analytics
→ AI Workforce
→ Automations
→ Approvals
→ Settings / Governance

Apply RBAC + ABAC + role/context-aware navigation so the same UI changes its visible modules and data for Owner, Director, Department Head, Manager, Employee and AI Operator.

## Reuse-first implementation path

1. UI foundation: Next.js + React + TypeScript + Tailwind + shadcn/ui.
2. Application framework: evaluate Refine for resource/RBAC/data-heavy screens.
3. Company data: connect Odoo/ERPNext/NocoDB/Postgres rather than duplicating records.
4. Files: Nextcloud + Paperless-ngx where needed.
5. Knowledge: Outline/AppFlowy/AFFiNE patterns.
6. BI: embed Metabase/Superset instead of rebuilding chart/query infrastructure.
7. Projects: reuse Plane patterns/integration where appropriate.
8. AI workforce: reuse Bizbox/ABF concepts for agent registry, goals, runs, budgets, memory and audit.
9. Nivy layer: create the unified navigation, identity, permissions, company graph/digital twin and cross-system search.
10. One-login principle: SSO/session should determine what the user can see and do across every module.

## Key gap

No single resource found in this discovery should be treated as the complete Nivy Company OS. The practical reuse strategy is one custom Nivy shell + reusable open-source modules/components + shared identity/RBAC + shared data model + embedded analytics + common search/document layer.
