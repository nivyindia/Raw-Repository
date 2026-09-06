# 03 — Folder Structure Map (PARA-Integrated)

> **Purpose:** The exact, fixed folder tree. Every document's storage path is derived mechanically from its Department (Doc 01), Type (Doc 02), and PARA category below.
> **Version:** 1.0 | **Owner:** Workspace Admin | **Status:** Approved

---

## Step 0 — PARA Classification (decide this first)

Before assigning a folder, classify the document into one of four PARA buckets:

| Bucket | Definition | Test |
|---|---|---|
| **Project** | Has a clear end date / deliverable | "Will this be 'done' on a specific date?" → Yes |
| **Area** | Ongoing responsibility, never "finishes" | "Is this a standing department function (Finance, R&D, HR)?" → Yes |
| **Resource** | Reference material, not tied to one department's daily work | Templates, glossary, brand assets, general knowledge |
| **Archive** | No longer active in any of the above | Superseded, completed, retired |

---

## Top-Level Structure

```
🏢 Company HQ
 ├── 📁 01_AREAS                      ← Department-owned, ongoing (PARA: Areas)
 │    ├── CEO/
 │    ├── STR — Strategy/
 │    ├── OPS — Operations/
 │    ├── FIN — Finance/
 │    ├── HR — Human Resources/
 │    ├── TECH — Technology/
 │    ├── MKT — Marketing/
 │    ├── SALES — Sales/
 │    ├── RND — Research & Development/
 │    ├── LEG — Legal & Compliance/
 │    ├── RISK — Risk & Governance/
 │    ├── DATA — Data & Innovation/
 │    ├── PMO/
 │    ├── ADMIN/
 │    ├── QA/
 │    └── CS — Customer Success/
 │
 ├── 📁 02_PROJECTS                   ← Time-bound, cross-department (PARA: Projects)
 │    └── [Project Name — Year]/
 │         ├── Charter & Plan
 │         ├── Working Docs
 │         └── Final Deliverables
 │
 ├── 📁 03_RESOURCES                  ← Shared reference, templates, brand (PARA: Resources)
 │    ├── Templates_Master/
 │    ├── Glossary_and_Onboarding/
 │    ├── Brand_Guidelines/
 │    └── Company_Master_Standards/   ← this Standard itself lives here
 │
 └── 📁 04_ARCHIVE                    ← Retired from all of the above (PARA: Archive)
      └── [mirrors the folder it came from, e.g. Archive/RND/, Archive/PROJECTS/...]
```

## Inside Every Department (`01_AREAS/[DEPT]/`)

Each department folder uses the **same** sub-structure — this consistency is what makes the system navigable:

```
[DEPT]/
 ├── Policies/       (POL)
 ├── SOPs/           (SOP)
 ├── Work_Instructions/  (WI)
 ├── Templates/      (TPL — department-specific only; shared ones go in 03_RESOURCES)
 ├── Reports/        (REP)
 ├── Records/        (REC)
 ├── Knowledge_Reference/  (KB)
 └── Meeting_Notes/  (MEET)
```

## Path Formula

```
[PARA-Bucket] / [Department or Project or Resource] / [Sub-folder by Type] / [DEPT-TYPE-NUMBER — Title].ext
```

**Example:** An R&D SOP about product testing →
`01_AREAS / RND — Research & Development / SOPs / RND-SOP-004 — New Product Testing Process.md`

**Example:** A cross-department website redesign plan →
`02_PROJECTS / Website Redesign 2026 / Charter & Plan / PROJ-DOC-Website2026 — Project Plan.md`

---

## Rules

1. A document lives in **exactly one** primary location. Cross-links to other departments are allowed; duplicate copies are not.
2. Anything used by more than one department (templates, brand assets, the Master Standard itself) goes in `03_RESOURCES`, never copy-pasted into each department.
3. Nothing is ever deleted — retired content moves to `04_ARCHIVE`, mirroring its original path.
4. Single Source of Truth: this folder structure exists in **one** tool only (state which tool your company uses — e.g. Notion / SharePoint / Google Drive). No parallel copies in other tools.

---

## Master Index Page (Required — lives in `03_RESOURCES`)

The folder tree alone is not enough for people to *find* things — a single company-wide "table of contents" page is required, kept separate from the department folders themselves:

- **Purpose:** one page anyone can Ctrl+F to find any document by name, tag, brand, or type, without knowing which department folder it's in.
- **Contents:** grouped sections — Workspace Foundation (onboarding, glossary, this Master Standard), Division/Brand Homes, Core Databases (see below), and a link into each department's Areas folder.
- **Ownership rule:** every document that reaches `Published` status (Doc 04) must appear in the Master Index within 24 hours — this is the same rule as the Search & Discoverability Requirement in Doc 04, restated here because it drives the folder-page relationship.

## Core Databases (if the tool supports structured databases, e.g. Notion/Airtable)

Rather than only flat folders, back the structure with a small set of shared databases so documents can be filtered/found by metadata (Doc 01/02 fields) instead of only by path:

| Database | Holds | Key fields (from Doc 04 metadata header) |
|---|---|---|
| `company_documents_database` | Every Policy/SOP/Report/Record etc. — one row per document | Code, Department, Type, PARA Bucket, Lifecycle Status, Owner |
| `templates_database` | All reusable templates (see naming below) | Use Case, Brand/Division, Status |
| `sop_database` | SOPs specifically (subset view, since these are the most frequently referenced type) | Dept, Function, Level, Status |
| `all_pages_index` (Master Pages Index) | Every page/document in the workspace, for the Master Index page above to pull from | Category, Status, Brand |

**Template naming pattern** (fits inside the general Doc 04 naming rule, for the TPL type specifically):
`TEMPLATE — [Brand/All] — [Use Case] — [Specific Name]`
Example: `TEMPLATE — All — Cold Email — Initial Outreach`
