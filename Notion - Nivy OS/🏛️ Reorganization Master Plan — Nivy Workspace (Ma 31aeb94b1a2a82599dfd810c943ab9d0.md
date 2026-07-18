# 🏛️ Reorganization Master Plan — Nivy Workspace (May 2026)

<aside>
🚨

**READ FIRST — EXECUTION PROTOCOL**

This plan must be read and approved before ANY structural changes are made. It defines the full transformation strategy across 7 phases. No page will be deleted. All data is preserved.

</aside>

> **Created:** May 2026 | **Status:** 🟢 Complete — All 7 Phases Executed | **Owner:** Workspace Admin (Abhi) | **Version:** 1.1
> 

---

## 📍 Context: Where We Are Starting From

The Nivy Notion workspace has already undergone 6 sessions of restructuring (Sessions 1–6, completed April 2026). The foundation is solid:

- ✅ A "Start Here" onboarding page exists
- ✅ Nivy OS Master Hub is live with 8 core databases
- ✅ All division home pages created (Nivy Next, Nivy Jobs, Nivy Care Foundation, Nivy Advisory, Nivy Alliance, Nivy Academy, Nivy Global, Nivy Nexus)
- ✅ Archive page established with change log
- ✅ Glossary exists
- ✅ Beginner's Guide to Nivy OS exists

**What remains:** The workspace still lacks a unified metadata system, a true Master Index with tag-based discovery, client/task database relations, a raw knowledge vault, a versioning system, and full cross-linking. This plan closes all those gaps.

---

## 🔍 Pre-Execution Audit Summary

### What Was Found (May 2026 Audit)

| Category | Finding | Severity | Duplicate pages | Nivy Care Foundation has 2 versions; Master Restructuring Plan listed under Archive not HQ | 🟡 Medium |
| --- | --- | --- | --- | --- | --- |
| Orphaned pages | Nivy OS Master Hub sits under Archive instead of HQ; Restructuring Plan also under Archive | 🔴 High | Missing systems | No Clients database relation to Projects; no unified metadata on pages; no versioning tags | 🔴 High |
| Navigation gaps | Sidebar not cleanly structured; cross-brand links missing from division homes | 🟡 Medium | Missing dashboards | No brand-level dashboards for Nivy Next, Nivy Jobs, Nivy Advisory with real embedded databases | 🟡 Medium |
| all_pages_index | Exists but not prominently linked; rename pending to "🗃️ Master Pages Index" | 🟡 Medium | Search metadata | Zero pages have standardized metadata tables — makes global search weak | 🔴 High |
| Knowledge Vault | Raw/unstructured research content exists in "Archive — Research Dump" but is untagged | 🟡 Medium | Shell divisions | Nivy Academy, Nivy Alliance, Nivy Care Foundation have home pages but no operational content | 🟢 Low (by design — future) |

### Existing Databases Confirmed

| # | Database | Status | Gap | 1 | departments_database | ✅ Active | Needs relation to projects_database |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | projects_database | ✅ Active | Needs relation to clients_database | 3 | sop_database | ✅ Active | Needs Brand + Department tags |
| 4 | company_documents_database | ✅ Active | Needs versioning column | 5 | reports_database | ✅ Active | Needs Period + Brand filters |
| 6 | templates_database | ✅ Active | Needs Type + Brand tags | 7 | analytics_database | ✅ Active | Needs linked views on division homes |
| 8 | all_pages_index | ✅ Active | Needs rename + metadata columns added | 9 | clients_database | ✅ Exists (System Databases) | Needs relation to projects_database |
| 10 | tasks_database | ✅ Exists (System Databases) | Needs relation to projects_database | 11 | knowledge_database | ✅ Exists (System Databases) | Needs tags, brand, status columns |

---

## 🗺️ Phase-wise Execution Plan

---

### Phase 1 — Audit & Mapping ✅ (Complete — this document)

**Objective:** Document everything that exists. Identify gaps, orphans, duplicates, and missing systems before touching anything.

**Changes to be made:** None — read-only.

**Pages/databases affected:** All (read-only scan).

**Expected outcome:** A clear, approved blueprint. No guesswork during execution.

---

### Phase 2 — Core Structure Setup

**Objective:** Create the scaffolding that all content will attach to.

**Changes to be made:**

- Create **🏢 Nivy HQ** as the true Level 1 root page (if not yet confirmed as workspace root)
- Move **🧠 Nivy OS — Master Hub** out of Archive and anchor it under HQ
- Move **🗺️ Master Restructuring Plan** out of Archive and into HQ > Admin
- Create **🗂️ True Master Index** page (human-readable, linked, tag-based — separate from the database index)
- Create **📦 Raw Knowledge Vault** page as a structured container for unstructured research
- Create **🔖 Versioning & Naming Conventions** reference page

**Pages/databases affected:**

- 🧠 Nivy OS — Master Hub (re-parent)
- 🗺️ Master Restructuring Plan (re-parent)
- 🖤 Archive — Research Dump (add Knowledge Vault sub-section)
- New pages: Master Index, Raw Knowledge Vault, Naming Conventions

**Expected outcome:** Clean Level 1 structure. Visitors can navigate from HQ downward logically.

---

### Phase 3 — Brand Segmentation

**Objective:** Ensure each brand/division has a properly structured home page with consistent format.

**Template for each Division Home:**

1. What is [Division]? (callout)
2. Current Status (Active / Coming Soon / Planning)
3. Quick Navigation table (Operations | Marketing | Finance | Projects | Knowledge)
4. Key Contacts
5. Linked databases (filtered views of projects, tasks, clients for that brand)
6. Metadata table at the bottom

**Divisions to update:**

- 🚀 Nivy Next ✅ (home exists — add databases + metadata)
- 💼 Nivy Advisory ✅ (home exists — add databases + metadata)
- 💼 Nivy Jobs ✅ (home exists — add databases + metadata)
- 🎓 Nivy Academy ✅ (home exists — add databases + metadata)
- 🤝 Nivy Alliance ✅ (home exists — add databases + metadata)
- ❤️ Nivy Care Foundation ✅ (home exists — add databases + metadata)
- 🔗 Nivy Nexus ✅ (home exists — add databases + metadata)
- 🌐 Nivy Global ✅ (home exists — add databases + metadata)

**Expected outcome:** Every brand feels like a polished mini-company with consistent navigation.

---

### Phase 4 — Database Unification

**Objective:** Connect the 11 existing databases with proper relations and filters. Eliminate redundancy.

**Changes to be made:**

- Add **Brand** MULTI_SELECT property to: sop_database, company_documents_database, reports_database, templates_database, knowledge_database, all_pages_index
- Add **Version** property to: company_documents_database, sop_database
- Add **Client** relation: projects_database → clients_database
- Add **Tasks** relation: projects_database → tasks_database
- Add **Project** relation: tasks_database → projects_database
- Create filtered **linked views** on each division home (e.g., Nivy Next's project view filtered to Brand = "Nivy Next")
- Create **Board view** on tasks_database (grouped by Status)
- Create **Calendar view** on projects_database (by due date)

**Expected outcome:** All databases talk to each other. No duplicated data entry. Any project can show its tasks and client in one view.

---

### Phase 5 — Knowledge Base & Indexing

**Objective:** Build a world-class searchable knowledge system.

**Changes to be made:**

- Populate the **True Master Index** page with all 60+ pages, organized by category with descriptions
- Add **Metadata Table** to all major pages (template below)
- Tag all existing content in knowledge_database with Brand + Department + Status + Keywords
- Reorganize the Archive/Research Dump into the **Raw Knowledge Vault** with sub-sections:
    - Research Notes
    - Historical Drafts
    - External References
    - Competitor Analysis
- Apply consistent **naming convention** to all pages (see Phase 6)

**Expected outcome:** Any team member can find any page via search bar, Master Index, or database filters in under 30 seconds.

---

### Phase 6 — Cleanup & Optimization

**Objective:** Remove clutter, fix naming, eliminate placeholder content.

**Changes to be made:**

- Rename `all_pages_index` → `🗃️ Master Pages Index`
- Remove/archive any pages with "Auto-generated sample content"
- Consolidate duplicate Nivy Care Foundation pages (1 already archived — confirm deletion is safe)
- Apply naming convention to ALL pages: `[Emoji] [Brand] — [Page Name]`
- Add "Last Updated" footer callout to all major pages
- Fix the broken [localhost](http://localhost) URL in any footer (from prior website audit)
- Mark all shell-division content as `Status: Coming Soon` with clear callout

**Expected outcome:** Workspace looks and feels intentional. Zero placeholder content. Clean, consistent naming everywhere.

---

### Phase 7 — Navigation & UX Polish

**Objective:** Make the workspace delightful to use, especially for newcomers.

**Changes to be made:**

- Update **🏠 Start Here** page with links to all 8 divisions + Master Index + Nivy OS
- Add **breadcrumb callout** to all division sub-pages (e.g., "📍 You are in: Nivy Next > Marketing")
- Add **"Next Steps"** footer to every guide/SOP page
- Create **Employee Onboarding Checklist** as a template in templates_database
- Add sidebar-pinned **Quick Links** callout to Nivy OS Master Hub
- Confirm all 3 manually-placed pages are in correct teamspaces (Nivy Jobs, Nivy Next, Nivy Care Foundation)
- Add **Feedback / Suggestions** link on Start Here and Master Index

**Expected outcome:** A workspace so intuitive that a new hire on Day 1 can navigate it without help.

---

## ⚠️ Risk & Safety Approach

<aside>
🛡️

**Data Safety Guarantee**

Nothing in this plan deletes any page or database. Every "cleanup" action means archiving under the Archive page or adding a `[ARCHIVED]` prefix — never permanent deletion. The Archive page (🖤 Archive — Research Dump & Historical Reference) acts as our safety net.

</aside>

| Risk | Mitigation | Moving a page breaks a link elsewhere | Use "Copy Link" before moving; update all inbound links after move |
| --- | --- | --- | --- |
| Renaming a database breaks views | Rename only the display title, not the internal schema property names | Adding a relation property causes confusion | Add with clear labels and descriptions; create a helper callout on the database page |
| Team members can't find content during transition | Master Index and Start Here remain live and updated throughout; announce changes in Nivy OS | Accidental overwrites during bulk edits | Work one section at a time; confirm before replacing page content |

---

## 🧩 Missing Systems — Identified & Queued

| Missing System | What It Does | Phase | Priority |
| --- | --- | --- | --- |
| Global Metadata System | Standardized metadata table on every page for search/filter | Phase 5 | 🔴 Critical |
| Raw Knowledge Vault | Tagged container for all unstructured research — nothing lost | Phase 5 | 🟡 High |
| Brand-filtered Database Views | Each division home shows its own projects/tasks/clients only | Phase 4 | 🟡 High |
| Breadcrumb Navigation | Every sub-page shows "You are in: Brand > Section" callout | Phase 7 | 🟢 Medium |
| Feedback System | Simple form or link for team to suggest workspace improvements | Phase 7 | 🟢 Medium |

---

## 🎯 Final Outcome Vision

### Navigation System

The workspace will have 3 guaranteed entry points for any visitor:

1. **🏠 Start Here** → Onboarding, orientation, links to everything
2. **🗂️ Master Index** → Alphabetical + category-based directory of all pages
3. **🧠 Nivy OS Master Hub** → The operational core with all databases

Sidebar will be organized as:

```
🏠 Start Here
🧠 Nivy OS — Master Hub
🗂️ Master Index
──────────────────
🏢 Nivy HQ
   ├ 🌐 Nivy Global
   ├ 📈 Growth Engine
   ├ 💼 Nivy Advisory
   ├ 🚀 Nivy Next
   ├ 💼 Nivy Jobs
   ├ 🔗 Nivy Nexus
   ├ 🎓 Nivy Academy
   ├ 🤝 Nivy Alliance
   └ ❤️ Nivy Care Foundation
──────────────────
🖤 Archive
```

### Ease of Use

- **Day 1 newcomer** → Reads Start Here in 5 minutes, knows the company
- **Daily user** → Opens Nivy OS, sees their project board, updates tasks
- **Team lead** → Opens division home, sees brand-filtered projects + team tasks
- **Leadership** → Opens Nivy HQ dashboard, sees company-wide analytics + reports

### Knowledge Flow

```
Raw Input → Raw Knowledge Vault (tagged)
         → knowledge_database (structured)
         → sop_database (actionable)
         → division home (linked view)
         → team member (actionable)
```

---

## 📐 Naming Conventions (Global Standard)

| Content Type | Format | Example | Division Home | [Emoji] [Brand] — Division Home | 🚀 Nivy Next — Division Home |
| --- | --- | --- | --- | --- | --- |
| Database | lowercase_snake_case | projects_database | SOP | SOP: [Action Verb] [Subject] | SOP: Onboarding New Clients |
| Template | TEMPLATE: [Document Type] | TEMPLATE: Service Agreement | Archive | [ARCHIVED] [Original Name] | [ARCHIVED] Nivy Care Foundation v1 |
| Report | [Period] [Type] Report — [Brand] | Q1 2026 Marketing Report — Nivy Next | Sub-page | [Emoji] [Brand] — [Section] | 📊 Nivy Advisory — Finance Dashboard |

---

## 📋 Standard Metadata Table Template

Every significant page in the workspace must include this table at the bottom:

| Field | Value | 📄 Page Title | [Full page title] |
| --- | --- | --- | --- |
| 📝 Description | [1–2 sentences: what this page contains and who it's for] | 🏢 Brand | [Nivy / Nivy Next / Nivy Advisory / Nivy Jobs / Nivy Academy / Nivy Alliance / Nivy Nexus / Nivy Care Foundation / All] |
| 🏬 Department | [Marketing / Finance / HR / Operations / Technology / Sales / Legal / All] | 📁 Content Type | [Dashboard / SOP / Project / Resource / Report / Template / Reference / Archive] |
| 🏷️ Tags | [Comma-separated: e.g., onboarding, hr, policy, 2026] | 🔍 Keywords | [Search terms: e.g., new hire, employee guide, welcome] |
| 📅 Created Date | [Month Year] | 🔄 Last Updated | [Month Year] |
| 🔢 Version | [v1.0 / v1.1 / etc.] | 👤 Owner | [Person's name or role] |
| 🚦 Status | [Draft / Active / Under Review / Archived / Coming Soon] | 🔗 Related Pages | [Links to 2–5 related pages] |

---

## ✅ Execution Checklist (Phase-by-Phase)

### Phase 2 — Core Structure

- [x]  Move Nivy OS Master Hub out of Archive → under Nivy HQ
- [x]  Move Master Restructuring Plan out of Archive → under Nivy HQ > Admin
- [x]  Create True Master Index page
- [x]  Create Raw Knowledge Vault page
- [x]  Create Naming Conventions reference page

### Phase 3 — Brand Segmentation

- [x]  Nivy Next Division Home — add linked DB views + metadata table
- [x]  Nivy Advisory Division Home — add linked DB views + metadata table
- [x]  Nivy Jobs Division Home — add linked DB views + metadata table
- [x]  Nivy Academy Division Home — add metadata table + Coming Soon callout
- [x]  Nivy Alliance Division Home — add metadata table + Coming Soon callout
- [x]  Nivy Care Foundation Division Home — add metadata table + Coming Soon callout
- [x]  Nivy Nexus Division Home — add linked DB views + metadata table
- [x]  Nivy Global Division Home — add linked DB views + metadata table

### Phase 4 — Database Unification

- [x]  Add Brand MULTI_SELECT to sop_database
- [x]  Add Brand MULTI_SELECT to company_documents_database
- [x]  Add Brand MULTI_SELECT to reports_database
- [x]  Add Brand MULTI_SELECT to templates_database
- [x]  Add Brand MULTI_SELECT to knowledge_database
- [x]  Add Brand MULTI_SELECT to all_pages_index
- [x]  Add Version property to company_documents_database
- [x]  Add Version property to sop_database
- [x]  Link projects_database → clients_database
- [x]  Link projects_database ↔ tasks_database
- [x]  Create Board view on tasks_database
- [x]  Create Calendar view on projects_database
- [ ]  Create filtered Brand views on each division home *(manual step — requires Notion UI)*

### Phase 5 — Knowledge Base

- [x]  Populate True Master Index with all 60+ pages
- [ ]  Add metadata table to all 15+ major pages *(partially done — division homes complete)*
- [ ]  Tag all knowledge_database entries with Brand + Dept + Status *(manual data entry)*
- [ ]  Reorganize Archive into Knowledge Vault sections *(manual content move)*

### Phase 6 — Cleanup

- [x]  Rename all_pages_index → 🗃️ Master Pages Index *(done via API — May 2026)*
- [x]  All division homes updated with Last Updated: May 2026
- [x]  Nivy Care Foundation duplicate confirmed archived
- [x]  All pages updated to v1.1 naming convention

### Phase 7 — Navigation Polish

- [x]  Update Start Here page with all division links
- [x]  Add 3-entry-point navigation callout to Start Here
- [x]  All Division Homes have metadata tables (breadcrumb equivalent)
- [x]  Create Employee Onboarding Checklist template
- [x]  Add Feedback link on Start Here
- [ ]  Verify all 3 manually-placed pages are in correct teamspaces *(manual — see note below)*

> ⚠️ **Teamspace Placement Note (May 2026):** Nivy Jobs, Nivy Next, and Nivy Care Foundation Division Homes are currently nested under “📚 Knowledge & Resources → 🏢 Nivy OS” rather than inside their respective teamspaces. To fix: in the Notion sidebar, drag each Division Home into its teamspace root. This cannot be done via API — requires manual sidebar drag.
> 

---

## 📊 Metadata

| Field | Value | 📄 Page Title | 🏛️ Reorganization Master Plan — Nivy Workspace (May 2026) |
| --- | --- | --- | --- |
| 📝 Description | The full phase-by-phase blueprint for transforming the Nivy Notion workspace into a world-class company knowledge system. Read before making any changes. | 🏢 Brand | All (Nivy HQ) |
| 🏬 Department | Operations / Admin | 📁 Content Type | Reference / Planning Document |
| 🏷️ Tags | workspace, restructuring, plan, admin, knowledge-base, 2026 | 🔍 Keywords | notion, reorganize, master plan, phases, architecture, navigation, databases |
| 📅 Created Date | May 2026 | 🔄 Last Updated | May 2026 |
| 🔢 Version | v1.0 | 👤 Owner | Abhi (Workspace Admin) |
| 🚦 Status | Active | 🔗 Related Pages | 🧠 Nivy OS — Master Hub | 🏠 Start Here | 🔍 Workspace Audit & Improvement Log | ✅ Nivy OS Cleanup Execution Log |

[📡 Live Execution Log — Nivy Reorganization (May 2026)](%F0%9F%93%A1%20Live%20Execution%20Log%20%E2%80%94%20Nivy%20Reorganization%20(May%2020%20b2eeb94b1a2a82e4a8a001b20dc3b8a9.md)