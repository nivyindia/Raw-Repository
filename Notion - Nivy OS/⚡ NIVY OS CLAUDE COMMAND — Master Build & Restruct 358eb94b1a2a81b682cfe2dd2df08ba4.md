# ⚡ NIVY OS CLAUDE COMMAND — Master Build & Restructure Protocol

# ⚡ NIVY OS — CLAUDE COMMAND PROTOCOL

> **What this page is:** A saved, reusable command system you paste to Claude at the start of any OS-building or research-structuring session. Claude reads this page, understands the full Nivy OS context, and executes accordingly. This is your "boot sequence" for every Claude session that touches the Nivy workspace.
> 

---

# 🧠 CONTEXT CLAUDE NEEDS TO KNOW

Before using any command below, paste this context block at the start of your Claude session:

---

## 📋 PASTE THIS CONTEXT BLOCK TO CLAUDE FIRST

```
CONTEXT — NIVY WORKSPACE

You are working inside the Nivy Notion workspace. Here is everything you need to know before executing any task:

## THE BRAND STRUCTURE
Nivy is a multi-brand company. Every brand has its own Division Home and brand-specific OS. The brands are:

1. 🌐 Nivy Global — The MASTER BRAND / parent company. Systems that apply to ALL brands live here.
   - Contains: Departments of Organisation, Nivy HQ, Nivy OS Master Hub, company-wide databases
   - URL: https://www.notion.so/ca9eb94b1a2a8230ad5481ebfb3108b3

2. 💼 Nivy Advisory — Accounting, CPA, tax, compliance, bookkeeping. International B2B.
   - URL: https://www.notion.so/995eb94b1a2a825dbda781b45121bdf6

3. 🚀 Nivy Next — IT, digital marketing, web/app dev, automation. Full-service agency.
   - URL: https://www.notion.so/31beb94b1a2a83bba3970196a25c3793

4. 🔗 Nivy Nexus — Buyer-seller community platform, UAE-focused, outreach-led.
   - URL: https://www.notion.so/9abeb94b1a2a8359b74881c2f7df6ff2

5. 💼 Nivy Jobs — Recruitment and staffing division. All open roles across all brands.
   - URL: https://www.notion.so/e07eb94b1a2a82d1864b017964aa1d57

6. 🎓 Nivy Academy — Training, education, professional development. Coming Soon.
   - URL: https://www.notion.so/b6ceb94b1a2a834f95a301fd9740d443

7. 🤝 Nivy Alliance — Strategic partnership and B2B alliance division. Coming Soon.
   - URL: https://www.notion.so/626eb94b1a2a83fe991c014d31228b8b

8. ❤️ Nivy Care Foundation — CSR and social impact division. Coming Soon.
   - URL: https://www.notion.so/99ceb94b1a2a82d18ec181645219395b

## KEY WORKSPACE RULES
- NEVER delete any page. If something is outdated, mark it [ARCHIVED] or move to 🖤 Archive.
- Cross-brand systems (HR, Finance, QC standards, governance) belong in Nivy Global.
- Brand-specific content (SOPs, services, clients, marketing) belongs in that brand's Division Home.
- Raw research from ChatGPT or external sources lands in 📦 Raw Knowledge Vault first.
- Every page must have: Brand tag, Department tag, Type tag, Status tag, Owner.
- Naming convention: [TYPE] – [Brand] – [Topic] (e.g. "SOP – Nivy Next – Cold Email Outreach")

## THE 10-SECTION COMPANY OS (applies to every brand)
1. Company Master Docs (Vision, Mission, Business Plan, Org Chart)
2. Strategy & Goals (OKRs, yearly goals, review loops)
3. Operations & SOPs (by department: Sales, Marketing, Delivery, HR, Finance, Tech, Admin)
4. Dashboards (Sales, Marketing, Delivery, Finance, HR, Partner)
5. HR & People (Directory, Compensation, L&D, Culture)
6. Finance & Legal (Budgets, Contracts, Compliance)
7. Partner Ecosystem (Sales partners, Franchise, Alliances)
8. R&D & Innovation (Product dev, experiments, AI tools)
9. Communication & Brand Assets (Brand identity, decks, PR)
10. Archives & Knowledge Base (Reports, SOP versions, knowledge library)

## EXISTING DATABASES IN MASTER HUB (Nivy OS)
- departments_database | projects_database | sop_database
- company_documents_database | reports_database | templates_database
- analytics_database | all_pages_index | clients_database
- tasks_database | knowledge_database | ChatGPT conversations DB

## RAW RESEARCH PIPELINE
Raw input (ChatGPT/external) → 📦 Raw Knowledge Vault → Review → Structured page → Correct brand OS section → Tagged + linked

## THE 3-CLICK RULE
Every user must reach any page in ≤ 3 clicks from Nivy HQ. Every page must link back to its parent Index or Division Home.
```

---

# ⚡ THE COMMANDS

Copy-paste any of these commands to Claude after the context block above.

---

## 🔵 COMMAND 1 — BUILD OR UPGRADE A BRAND'S OS

Use when: Starting or rebuilding the OS for a specific Nivy brand.

```
COMMAND: BUILD BRAND OS

Target brand: [BRAND NAME e.g. Nivy Next / Nivy Advisory / Nivy Nexus]

Task:
1. Fetch the Division Home for [BRAND NAME] from Notion.
2. Fetch the Nivy OS Master Hub to understand existing databases.
3. Audit what already exists for this brand: departments, SOPs, knowledge pages, templates.
4. Identify what is MISSING vs what the 10-section Company OS requires.
5. Do NOT delete anything found. If something is duplicate, flag it — don't remove.
6. Build or upgrade the following sections FOR THIS BRAND ONLY:
   - Section 1: Company Master Docs (if not already built)
   - Section 3: Operations & SOPs — list actual departments that exist for this brand
   - Section 4: Dashboards — create filtered views linked to master databases
   - Section 9: Brand Assets — brand-specific comms and templates
7. Identify any content found that should go to Nivy Global instead (cross-brand systems).
8. Flag those cross-brand items and ask me before moving anything.
9. Create a new child page inside the Division Home titled:
   "🏗️ [BRAND NAME] OS — Build Status & Gap Report (May 2026)"
   This page must list: what was found, what was built, what is missing, and next priority actions.
10. Output a summary of everything created and every action taken.

Rules:
- Never delete. Only create, move with permission, or update.
- Every new page must follow naming convention: [TYPE] – [Brand] – [Topic]
- Every new page must have Brand, Department, Type, Status properties if inside a database.
```

---

## 🟢 COMMAND 2 — PROCESS RAW RESEARCH INTO THE OS

Use when: You've pasted or saved new ChatGPT research, notes, or ideas and want Claude to structure and file it.

```
COMMAND: PROCESS RAW RESEARCH

Raw content to process:
[PASTE YOUR RAW CONTENT HERE — ChatGPT output, notes, ideas, voice memo summary, etc.]

Task:
1. Read and fully understand the raw content above.
2. Identify:
   a. Which brand(s) it relates to (Nivy Next / Advisory / Nexus / Global / All)
   b. What type of content it is: SOP / Strategy / Knowledge / Template / Framework / Research / Idea
   c. Which of the 10 OS sections it belongs to
   d. Which department it belongs to (Sales / Marketing / HR / Finance / Tech / Delivery / Admin / Ops)
   e. What priority level: CORE (must implement now) / USEFUL (add this quarter) / FUTURE (backlog)
3. Rename it following convention: [TYPE] – [Brand] – [Topic]
4. Structure the content into the correct Notion page format:
   - If SOP: use the 12-part SOP structure (Overview, Trigger, Prerequisites, Steps, Output Example, QC Checklist, Mistakes, Time Benchmark, Next Step, Related SOPs, Linked Knowledge, Linked Templates)
   - If Knowledge: use (Concept, Simple Explanation, Real Use Cases, Visuals/Examples, Linked SOPs, Related Topics, Prerequisites, Next Learning)
   - If Strategy: use (Objective, Current State, Gap, Recommended Action, Owner, Timeline, KPI)
   - If Template: use (When to Use, Copy Block, Variables, Example Output, Linked SOP)
   - If Framework: use (Purpose, Components, How to Apply, Example, Linked SOPs)
5. Create the structured page in the correct location:
   - Brand-specific content → inside that brand's Division Home → correct section
   - Cross-brand content → inside Nivy Global
   - If unsure → create in 📦 Raw Knowledge Vault with tag [PENDING PLACEMENT]
6. Tag the original raw source as [PROMOTED] in the Raw Knowledge Vault — do NOT delete it.
7. Link the new structured page back to the relevant Index page and Division Home.
8. Output: list of pages created, where they were placed, and any items flagged for my review.

Priority order for implementation:
1. CORE items that belong to active brands (Nivy Next, Nivy Advisory, Nivy Nexus)
2. Cross-brand items for Nivy Global
3. USEFUL items
4. FUTURE items (create stub pages with [BACKLOG] tag)
```

---

## 🟡 COMMAND 3 — WORKSPACE AUDIT & GAP DETECTION

Use when: You want Claude to scan the workspace and find what's missing, broken, or out of place.

```
COMMAND: WORKSPACE AUDIT

Scope: [ALL BRANDS / specific brand name]

Task:
1. Search the Notion workspace for all pages related to [scope].
2. For each brand in scope, check:
   a. Does the Division Home exist and is it complete?
   b. Are all 10 OS sections present (even as stubs)?
   c. Are there orphaned pages (no parent, no tags, no links)?
   d. Are there unnamed or poorly named pages? (ALL CAPS, underscores, vague titles)
   e. Are there duplicate pages covering the same topic?
   f. Are there pages that belong in Nivy Global but are sitting inside a sub-brand?
   g. Are there raw/unstructured pages that should be promoted?
3. Do NOT fix anything yet. Produce a full audit report as a new Notion page with:
   - Section A: What exists and is good
   - Section B: What is missing
   - Section C: Orphaned / broken pages (list with URLs)
   - Section D: Renaming needed (old name → new name)
   - Section E: Pages to move (current location → correct location)
   - Section F: Cross-brand content that should go to Nivy Global
   - Section G: Priority fix list (ranked by impact)
4. Ask for my approval before executing any changes.
5. Create the audit page inside:
   🧠 Nivy OS — Master Hub > 🔍 Workspace Audit & Improvement Log

Rules:
- Flag, don't delete.
- Show me before moving anything.
- Duplicates are kept until I confirm which to archive.
```

---

## 🟠 COMMAND 4 — BUILD A DEPARTMENT HUB

Use when: Adding a new department or rebuilding an existing one inside a brand.

```
COMMAND: BUILD DEPARTMENT HUB

Brand: [e.g. Nivy Next]
Department: [e.g. Marketing / Sales / HR / Finance / Tech / Delivery / Ops / Admin]

Task:
1. Fetch the Division Home for [BRAND].
2. Check if a [DEPARTMENT] section already exists under this brand. If yes, audit it first.
3. Build a Department Hub page with this structure:

   ## [DEPARTMENT] — [BRAND]
   > What this department does, who leads it, what it owns.

   ### 📊 Department KPIs
   [List relevant KPIs for this department and this brand]

   ### 📋 Active SOPs
   [Linked view or list of SOPs tagged Department = [DEPARTMENT] + Brand = [BRAND]]

   ### ✅ Active Tasks
   [Filtered view from tasks_database]

   ### 📚 Knowledge Base
   [Filtered view from knowledge_database]

   ### 📦 Templates
   [Filtered view from templates_database]

   ### 📈 Reports
   [Filtered view from reports_database]

   ### 🔗 Quick Links
   [Links to related departments, handoff docs, tools]

4. If any SOPs, knowledge pages, or templates already exist for this department (scattered across workspace), identify them and suggest linking them here.
5. Create 3 starter SOPs for this department using the 12-part SOP structure. Use realistic content for [BRAND]'s actual services.
6. Output: hub page URL, list of SOPs created, list of existing pages linked.
```

---

## 🔴 COMMAND 5 — MOVE CONTENT TO NIVY GLOBAL

Use when: You've identified systems or content that should be shared across all brands.

```
COMMAND: PROMOTE TO NIVY GLOBAL

Content to promote: [list page titles or paste URLs]
Reason: [why this is cross-brand]

Task:
1. Fetch each page listed.
2. Confirm it is truly cross-brand (applies to 2+ brands, not brand-specific).
3. Identify the correct section in Nivy Global it belongs to:
   - Section 1 (Company Master Docs) for vision, values, governance
   - Section 5 (HR & People) for universal HR policies, org standards
   - Section 6 (Finance & Legal) for group-level finance, compliance
   - Section 7 (Partner Ecosystem) for group-level alliance/franchise rules
   - Knowledge DB for universal knowledge entries
   - Templates DB for universal templates
4. Do NOT move pages yet. List:
   - Page title + current location
   - Proposed new location in Nivy Global
   - Whether a copy stays in the original brand (yes/no recommendation)
5. Ask for my confirmation before executing any moves.
6. After approval: move pages, update their Brand tag to "All", add a backlink in the original brand's section.
```

---

## ⚫ COMMAND 6 — FULL OS PRIORITY BUILD SEQUENCE

Use when: Starting from scratch or doing a major OS upgrade across all brands.

```
COMMAND: FULL OS BUILD — PRIORITY SEQUENCE

Task:
Execute the following in strict priority order. Complete each step fully before moving to the next.
After each step, output what was done and ask for confirmation to proceed.

PRIORITY 1 — NIVY GLOBAL (Master layer first)
1a. Audit Nivy Global Division Home — what exists vs the 10-section OS
1b. Build or complete: Section 1 (Company Master Docs), Section 5 (Universal HR), Section 6 (Finance & Legal)
1c. Ensure all 11 core databases in Nivy OS Master Hub are properly set up with correct properties
1d. Create or confirm: Master Index, Naming Conventions page, Tag Taxonomy page

PRIORITY 2 — ACTIVE BRANDS (Nivy Next, Nivy Advisory, Nivy Nexus)
2a. Run COMMAND 1 (BUILD BRAND OS) for Nivy Next
2b. Run COMMAND 1 for Nivy Advisory
2c. Run COMMAND 1 for Nivy Nexus

PRIORITY 3 — IN-PLANNING BRANDS (Nivy Jobs)
3a. Build stub OS for Nivy Jobs — sections 1, 2, 3 only

PRIORITY 4 — COMING SOON BRANDS (Academy, Alliance, Care Foundation)
4a. Create "Coming Soon" OS stubs — just section 1 (identity docs) and section 2 (goals)

PRIORITY 5 — CROSS-CUTTING SYSTEMS
5a. Process all content in 📦 Raw Knowledge Vault — run COMMAND 2 for each item
5b. Process ChatGPT conversations database — identify promotable research
5c. Build/complete Master Index with all brand sections
5d. Build/complete Navigation system (3-click rule audit)

PRIORITY 6 — AUTOMATION & GOVERNANCE
6a. Map all Notion native automations needed
6b. Document all Make/Zapier workflows needed
6c. Build Document Control page (naming, versioning, review cycles)
6d. Build Tag Taxonomy enforcement guide

After all priorities complete: Run COMMAND 3 (WORKSPACE AUDIT) for final QA.
```

---

# 📐 OS STRUCTURE REFERENCE (Per Brand)

Every brand's Division Home should contain exactly these 10 sections:

| # | Section | What Goes Here | Who Owns It |
| --- | --- | --- | --- |
| 1 | Company Master Docs | Vision, Mission, Business Plan, Org Chart, Governance | Leadership |
| 2 | Strategy & Goals | OKRs, Yearly Goals, Review Loops | CEO / Brand Lead |
| 3 | Operations & SOPs | All department SOPs — Sales, Marketing, Delivery, HR, Finance, Tech, Admin | Dept Heads |
| 4 | Dashboards | KPI views, pipeline views, filtered DB views | All Managers |
| 5 | HR & People | Team directory, compensation, L&D, culture | HR Lead |
| 6 | Finance & Legal | Budgets, contracts, compliance docs | Finance Lead |
| 7 | Partner Ecosystem | Sales partners, alliances, franchise (where applicable) | Sales/Alliance Lead |
| 8 | R&D & Innovation | Experiments, product dev, new ideas, AI tools | Innovation Lead |
| 9 | Communication & Brand Assets | Brand identity, decks, PR, internal comms | Brand/Marketing |
| 10 | Archives & Knowledge Base | Historical reports, SOP versions, knowledge library | Workspace Admin |

---

# 🏷️ WHAT GOES TO NIVY GLOBAL vs BRAND-SPECIFIC

| Content Type | Nivy Global | Brand-Specific |
| --- | --- | --- |
| Company values & mission | ✅ Master version lives here | Each brand may have adapted version |
| HR policies (leave, conduct, appraisal) | ✅ Universal policy | Brand-specific role structures |
| Finance group policies (audit, reimbursement) | ✅ Group standards | Brand P&L and billing |
| Org chart (group level) | ✅ Full group org chart | Brand's internal team structure |
| Tag taxonomy & naming conventions | ✅ Master rules | — |
| SOPs (Sales, Marketing, Delivery) | ❌ Brand-specific | ✅ Each brand has own SOPs |
| Client data | ❌ Brand-specific | ✅ Linked to brand's projects |
| Brand identity (logo, colors, tone) | Reference palette only | ✅ Full brand kit per brand |
| Training modules | ✅ Universal onboarding | Brand-specific role training |
| KPI frameworks | ✅ Framework definition | ✅ Brand tracks own numbers |
| Experiments DB | ✅ Shared | Brand-tagged entries |
| Partner/Alliance framework | ✅ Group framework | Brand-specific partner deals |
| Legal & Compliance (group) | ✅ GDPR, IP, group policy | Brand-specific contracts |
| Knowledge DB | ✅ Shared (tag by brand) | — |

---

# 🔁 RAW RESEARCH PIPELINE (ALWAYS FOLLOW THIS)

```
You paste ChatGPT output / research notes / ideas
         ↓
Run COMMAND 2 → Claude reads and identifies:
  - Brand(s)
  - Content type
  - OS section
  - Department
  - Priority
         ↓
Claude renames it correctly
         ↓
Claude structures it into proper page format (SOP / Knowledge / Strategy / Template / Framework)
         ↓
Claude creates it in correct OS section of correct brand
         ↓
Original raw entry tagged [PROMOTED] in Raw Knowledge Vault (NOT deleted)
         ↓
New page linked to Index + Division Home
         ↓
Claude outputs: what was created, where, what was flagged for your review
```

---

# ✅ 12-PART SOP STRUCTURE (Mandatory for all SOPs)

```
## SOP – [Brand] – [Topic]

**Overview:** What this SOP is and why it exists.
**Trigger / When to Use:** What situation requires this SOP.
**Prerequisites:** Skills, tools, or knowledge needed before starting.
**Steps:** (numbered checkbox list)
**Output Example:** What good output looks like.
**QC Checklist:** Pass/fail criteria for reviewer.
**Common Mistakes:** What to avoid.
**Time Benchmark:** How long this should take (SLA).
**Next Step:** What to do after completing this SOP.
**Related SOPs:** Links to SOPs that connect to this one.
**Linked Knowledge:** Concepts the executor should understand.
**Linked Templates:** Ready-to-use assets for this SOP.
```

---

# 📦 KNOWLEDGE PAGE STRUCTURE

```
## GUIDE – [Brand] – [Topic]

**Concept:** Clear one-line definition.
**Simple Explanation:** Explain it like the person is new.
**Real Use Cases:** How we use this at Nivy (brand-specific examples).
**Visual / Example:** If applicable.
**Linked SOPs:** Where this knowledge gets applied.
**Related Topics:** Other knowledge pages to read.
**Prerequisites:** What to learn before this.
**Next Learning:** What to study after this.
```

---

# 🏷️ MANDATORY TAGS FOR EVERY PAGE

| Tag Type | Required Values |
| --- | --- |
| Brand | Nivy Global / Nivy Advisory / Nivy Next / Nivy Nexus / Nivy Jobs / Nivy Academy / Nivy Alliance / Nivy Care / All |
| Department | Sales / Marketing / Delivery / HR / Finance / Tech / Admin / Ops / All |
| Type | SOP / Guide / Template / Strategy / Framework / Research / Report / Dashboard / Archive |
| Level | Beginner / Intermediate / Advanced |
| Status | Draft / Active / Needs Review / Promoted / Archived / Backlog |
| Priority | Core / Useful / Future |

---

# ⚠️ RULES CLAUDE MUST ALWAYS FOLLOW

1. **Never delete anything.** If something is outdated, mark [ARCHIVED] or move to 🖤 Archive.
2. **Ask before moving pages.** Always show me what you plan to move and wait for confirmation.
3. **Ask before renaming existing pages.** Show old name → new name and wait.
4. **Process in priority order.** Active brands first, coming-soon brands last.
5. **No orphan pages.** Every page you create must link to its Division Home and/or Index.
6. **Flag duplicates, don't resolve them unilaterally.** Show me both versions.
7. **Follow naming convention strictly.** [TYPE] – [Brand] – [Topic]
8. **Cross-brand content goes to Nivy Global.** When in doubt, flag and ask.
9. **Raw research goes to Raw Knowledge Vault first,** then gets promoted.
10. **Output a summary after every session.** List every action taken, every page created, every item needing follow-up.

---

*This command page lives inside: 🏗️ Nivy OS — World-Class Build Plan (Claude's Version)*

*Last updated: May 2026 | Owner: Workspace Admin | Version: 1.0*