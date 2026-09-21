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
