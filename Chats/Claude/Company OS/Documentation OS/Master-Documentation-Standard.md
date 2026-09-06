# 📚 Master Documentation Standard — Nivy (Consolidated)

> **Version:** 1.0 | **Last Updated:** August 2026 | **Owner:** Workspace Admin / Ops Head | **Status:** Active
>
> This document merges three source guides from the Nivy workspace into one single, international-level documentation method:
> 1. Document Control Standards & Naming Guide
> 2. Naming Conventions & Versioning Guide
> 3. Metadata & Tagging System
>
> Use this as the single reference before creating, naming, tagging, or versioning **any** document.

---

## 1. Purpose

This standard defines how every document — knowledge base article, SOP, checklist, report, template, or strategy doc — must be **named, versioned, tagged, owned, and reviewed**, so that the system is searchable, traceable, and maintainable by anyone, including someone joining with no prior context.

---

## 2. Required Header Block (Every Document)

Every document must begin with this header (in a callout or quote block):

```
Version: [x.x] | Last Updated: [Date] | Owner: [Role name] | Status: [Live / Draft / Archived]
```

**Status values:**
- **Live / Active** — actively in use, current and accurate
- **Draft / In Progress** — being built or reviewed, not yet in use
- **Archived / Deprecated** — no longer in use, kept for reference

---

## 3. Document & Page Naming Convention

**General page format:** `[Emoji] [Brand] — [Page Name]`

| Content Type | Naming Format | Example |
| --- | --- | --- |
| Knowledge Base | KB-001, KB-002... | KB-001 — What is a Lead |
| Standard Operating Procedure | SOP-[DEPT]-001... | SOP-VA-005 — LinkedIn DM Outreach |
| QC Checklist | QC-001, QC-002... | QC-003 — Follow-Up Checklist |
| Department Page | [Emoji] [Brand] — [Dept Name] | 📊 Nivy Next — Marketing |
| Template | TEMPLATE: [Document Type] | TEMPLATE: Service Agreement |
| Meeting Notes | [YYYY-MM-DD] Meeting — [Topic] | 2026-05-01 Meeting — Quarterly Review |
| Draft | [DRAFT] [Page Name] | [DRAFT] Pricing Strategy 2026 |
| Individual Record | [Person Name] — [Record Type] | Priya Mehta — Onboarding Completion Record |
| Team/System Page | Emoji + descriptive title | 🔄 Handoff System, ⚠️ Error Handling System |

**Database naming:** `lowercase_snake_case`, no spaces (e.g. `projects_database`, `sop_database`). Database **views** use Title Case (e.g. `Active Projects`, `By Brand`).

**Rule:** No page may have an untitled, vague, or duplicate name. Every name must be unique and searchable.

**Naming Don'ts:**
- ❌ "New SOP" — not a valid name
- ❌ "Copy of KB-001" — duplicate, not valid
- ❌ "Temp page" — no temporary pages in the live system
- ❌ "Notes from meeting" — all permanent content must be formatted, named, and versioned
- ❌ ALL CAPS titles — use the standard coded format instead

---

## 4. Versioning System

**Format:** `v[Major].[Minor]`

| Change Type | Version Bump | Example |
| --- | --- | --- |
| New document | Start at v1.0 | First version created |
| Minor update (fix, note, corrected example) | +0.1 | v1.0 → v1.1 |
| Major update (process restructured/rewritten) | +1.0 | v1.1 → v2.0 |

**Rule:** Every edit must update the version number and "Last Updated" date at the top of the page. An edited document without an updated version is treated as unauthorised.

**Where to track versions:** `company_documents_database` → Version property, `sop_database` → Version property, and in the metadata table on the page itself.

---

## 5. Metadata Block (Required on Every Document)

| Field | Description |
| --- | --- |
| 📄 Page Title | Full document name |
| 📝 Description | 1–2 line summary of what the document covers |
| 🏢 Brand | Which brand/entity it belongs to (or "All") |
| 🏪 **Department** | Owning department (Marketing, Finance, Ops, HR, Tech, etc., or "All") |
| 📁 Content Type | Reference / Guide / SOP / Template / Report / Strategy Doc |
| 🏷️ Tags | Freeform keyword tags (see Section 6 for controlled taxonomy) |
| 🔍 Keywords | Search terms someone might use to find this doc |
| 📅 Created Date | Original creation date |
| 🔄 Last Updated | Date of most recent edit |
| 🔢 Version | Current version number (see Section 4) |
| 👤 Owner | Responsible role (not personal name) |
| 🚦 Status | Active / Draft / Archived / Deprecated (see Section 2 & 7) |
| 🔗 Related Pages | Links to connected documents |

---

## 6. Controlled Tagging Taxonomy

Apply consistently to every page/database entry so content is filterable and searchable.

### 📦 Service Tags
`digital-marketing` · `ai-automation` · `web-development` · `app-development` · `graphic-design` · `video-editing` · `virtual-assistant`

### 🏭 Industry Tags
`professional-services` · `ecommerce` · `saas` · `real-estate` · `healthcare` · `education` · `hospitality` · `recruitment`

### 🌍 Platform Tags
`linkedin` · `instagram` · `google` · `meta` · `email` · `youtube` · `webflow` · `wordpress`

### 🏗️ Funnel Stage Tags
`tofu` (awareness) · `mofu` (consideration) · `bofu` (decision/conversion) · `retention` (post-sale)

### 📄 Content Type Tags
`case-study` · `sop` · `template` · `proposal` · `pitch-deck` · `outreach` · `social-post` · `strategy-doc` · `training`

### 📊 Status Tags
🟢 Active · 🟡 In Progress · 🔵 Draft · 🔴 Outdated · ⚪ Archived · ✅ Complete

### ⚡ Priority Levels
P1 (critical, immediate) · P2 (high, this week) · P3 (medium, this month) · P4 (low, backlog)

### 📊 Lead Stage Tags (CRM-style, where applicable)
`lead-cold` · `lead-warm` · `lead-qualified` · `lead-proposal` · `lead-won` · `lead-lost`

**Tagging Discipline Rules:**
1. Every page gets at least one service tag and one status tag.
2. Content assets get a content-type tag + funnel-stage tag.
3. Case studies get an industry tag + service tag.
4. Proposals/outreach get a lead-stage tag.
5. No page should have more than 8 tags — if it does, split it into two pages.

---

## 7. Review Cycle

| Document Type | Review Frequency | Trigger |
| --- | --- | --- |
| Knowledge Base | Every 60 days | Or when a process changes |
| SOPs | Every 30 days | Or immediately after any process change |
| QC Checklists | Every 30 days | Or if a recurring error type is identified |
| SLA Documents | Every 60 days | Or when team size changes significantly |
| Role & Responsibility Matrix | Every 90 days | Or when a new role is created |
| Scorecard Templates | Every quarter | Or when KPI targets change |

**Review Owner:** Department Manager conducts the review; Ops Head/Workspace Admin audits it monthly.

---

## 8. Page Ownership Rules

Every page must have exactly one named owner, assigned **by role**, not by personal name:

| Owner Role | Owns |
| --- | --- |
| Department Manager | All SOPs, QC checklists, onboarding pages, department scorecards |
| Ops Head / Workspace Admin | Role Matrix, Document Control Standards, Naming/Metadata/Tagging Systems, Automation Architecture |
| Individual Contributor | Their own scorecard, their own onboarding record |

If an owner changes role, the new owner inherits the page within their first week.

---

## 9. Why Standards Matter (Plain-English Rationale)

Imagine joining on Day 1 and finding pages titled `"Overview "`, `"ANNEXURE E: APPROVED PRODUCTS/SERVICES & PRICING"`, or `"New page"` — with no idea what they are, whether they're current, or who owns them.

A properly named, tagged, and versioned page tells you immediately:
- **What it is** (from the title)
- **Whether it's current** (from the status tag)
- **Who owns it** (from the owner field)
- **What's inside** (from a 2-sentence description at the top)

**Standard 1 — Status Callout at Top of Every Page:**
```
🟢 Status: Live | Owner: [Name] | Last Updated: [Month Year]
🟡 Status: Draft | Owner: [Name] | Last Updated: [Month Year]
🟠 Status: Needs Review | Owner: [Name] | Please review by: [Date]
🖤 Status: Archived | Kept for historical reference. Do not use for active work.
```

**Standard 2 — Plain-English Description (first line after the status tag):**
Bad: `ANNEXURE E: APPROVED PRODUCTS/SERVICES & PRICING`
Good: `This page lists all approved products and services we offer, with official prices. Use as reference when creating client proposals or quotes.`

**Standard 3 — Additional Naming Formats (extends Section 3):**

| Content Type | Naming Format | Example |
| --- | --- | --- |
| Division/Teamspace home | [Emoji] What is [Division Name]? | 💡 What is Nivy Global? |
| Department overview | [Emoji] [Dept] — Overview | 📣 Marketing — Overview |
| SOP (alt. format) | SOP: [What it covers] | SOP: How to Onboard a New Client |
| Project | PROJECT: [Name] | PROJECT: Website Redesign 2026 |
| Report | REPORT: [Topic] [Period] | REPORT: Sales Performance Q1 2026 |
| Meeting notes (alt.) | MEETING: [Topic] [DD Mon YYYY] | MEETING: Weekly Sync 14 Apr 2026 |
| Roadmap | [Emoji] [Topic] Roadmap | 🗺️ Nivy Next — Roadmap 2026 |
| Guidelines | [Emoji] [Topic] — Guidelines | 🎨 Brand — Guidelines |

---

## 10. Ready-to-Use Page Templates

### Template A — Division / Teamspace Home Page
```
[EMOJI] What is [Division Name]?

> 🟢 Status: Live | Owner: [Name] | Last Updated: [Month Year]

[Division Name] is responsible for [2 sentences explaining what this division does and why it exists].

🎯 Our Mission
[One sentence mission statement]

👥 Our Team
- Lead: [Name]
- Members: [Names or "See Team Directory"]

📁 Key Pages in This Teamspace
- [Link 1] · [Link 2] · [Link 3]

🔗 Related Teamspaces
- [Link to related division/department]

📣 Contact
- Email / Slack / WhatsApp: [details]
```

### Template B — SOP (Standard Operating Procedure)
```
SOP: [What This Covers]

> 🟢 Status: Live | Owner: [Name] | Department: [Dept] | Last Updated: [Month Year]

💡 What is this?
[1-2 sentences: what process, who should follow it?]

👥 Who This Applies To
[Team / Role / All staff]

⏱️ How Long It Takes
[Estimated time]

📝 Step-by-Step Instructions
Step 1: [Title] — [Instruction]
Step 2: [Title] — [Instruction]
Step 3: [Title] — [Instruction]

⚠️ Common Mistakes to Avoid
- [Mistake 1] · [Mistake 2]

❓ FAQs
[Question]: [Answer]

🔗 Related Pages
- [Link]
```

### Template C — Project Page
```
PROJECT: [Project Name]

> 🟡 Status: In Progress | Owner: [Name] | Start Date: [Date] | Target End: [Date]

💡 What is this project?
[2-3 sentences: what's being built, what problem it solves]

🎯 Goal
[Clear, measurable outcome]

📊 Key Milestones
| Milestone | Due Date | Status |
|---|---|---|
| [Task 1] | [Date] | ⏳ Pending |
| [Task 2] | [Date] | ✅ Done |

👥 Team
| Role | Person |
|---|---|
| Lead | [Name] |
| Support | [Name] |

🔗 Related Resources
💬 Notes & Updates
[Latest update — Date]: [What happened]
```

### Template D — Start Here / Onboarding Page
```
👋 Start Here — Welcome to [Division/Team Name]

> 🟢 Status: Live | Owner: [Team Lead Name] | Last Updated: [Month Year]

🏢 What We Do
[3-4 sentences in plain English]

📖 Your First 3 Steps
1. Read [Link to overview page]
2. Introduce yourself to [Name] (contact: [email/WhatsApp])
3. Check your assigned tasks in [Link to project tracker]

📁 Important Pages for You
- 📜 [Rules & Guidelines] · 🛠️ [Tools we use] · 📊 [Dashboards] · 📖 [SOPs]

❓ Got Questions?
- Ask [Name] on [Slack/WhatsApp] · Email: [email]
```

### Template E — Research / Reference Page
```
🔍 [Topic] — Research & Reference

> 🟡 Status: Draft | Owner: [Name] | Last Updated: [Month Year]

💡 What is this?
[1-2 sentences: what was researched, why, who should read it]

🎯 Key Findings
1. [Finding 1] · 2. [Finding 2] · 3. [Finding 3]

📊 Data & Details
[Tables, lists, comparisons]

💡 Recommendations
[What should we do based on this research?]

🔗 Sources
🗓️ Last Reviewed: [Date] by [Name]
```

---

## 11. Standard Department List (for the "Department" Metadata Field)

Use these as the controlled values for the 🏪 Department field in Section 5, unless a document is brand/company-wide ("All"):

**Executive Layer:** Board of Directors · CEO Office · CSO (Strategy) · COO (Operations) · CFO (Finance) · CHRO (HR) · CTO (Technology) · CMO (Marketing) · CLO (Legal & Compliance) · CRO (Risk) · CDO (Data & Innovation)

**Core Functional Departments:** Operations · PMO · Finance & Accounts · Technology / IT / DevOps · Marketing · Sales · Human Resources · Legal & Compliance · Strategy & Business Development · Risk & Governance · Data & Analytics / Innovation Lab · Administration & Facilities · Quality Assurance & Internal Audit · Customer Success / Service Excellence

---

## 12. Onboarding Text (for Every Division's "Start Here" Page)

> **Welcome — Here's How Our Knowledge Base Works**
>
> We use Notion (or the equivalent workspace tool) as our company knowledge base — a shared digital office where every document, plan, SOP, and project lives.
>
> **How it's organised:**
> - **HQ** — Start here. Company overview, org chart, glossary.
> - **Operating System / Core Hub** — The engine room: all databases, SOPs, projects.
> - **Division Teamspaces** — Each division/brand is its own focused area.
>
> **The 3 things you need on Day 1:**
> 1. Read the Glossary so you understand our terms
> 2. Find your division's teamspace and read its Start Here page
> 3. Check your name in the Team Directory
>
> **If you can't find something:** Search the workspace, or ask your team lead.
> **If something looks wrong or outdated:** Leave a comment on that page and tag your team lead.

---

## 13. Ongoing Maintenance Standards

| Task | Frequency | Owner |
| --- | --- | --- |
| Review page statuses (Live/Draft/Archived?) | Monthly | Team leads |
| Check for blank pages needing content | Monthly | Department heads |
| Archive pages no longer in use | Quarterly | Any team member |
| Update Team Directory | When someone joins/leaves | HR |
| Review and update SOPs | Every 6 months | Process owners |
| Add new pages to the master page index | When creating any new page | Creator |

---

## 14. Guiding Principle

**A system that is properly named, tagged, and versioned can be handed to a new team member — anywhere in the world — on Day 1, with zero prior context needed. That is the international standard this document builds toward.**

---

### Source Documents Merged (all duplicates across folders were checked and consolidated)
- 📋 Document Control Standards & Naming Guide (v1.0, Ops Head)
- 📐 Naming Conventions & Versioning Guide — Nivy (v1.0, Workspace Admin)
- 🧹 Metadata & Tagging System (Nivy Next)
- 📐 Phase 4 — Newbie-Friendly Standards & Templates
- FINAL HQ Department List (Perfected + Complete)

*Files checked but excluded as not relevant to internal documentation method: "Naming" (All Communities — brand/community architecture, not document naming), "Additional ISO Standards Overview" (external ISO-certification sales copy, not an internal documentation standard), and several empty/placeholder SOP Template stub files.*
