---
name: company-os-classifier
description: Use this skill whenever a new document, note, research finding, SOP draft, or piece of company knowledge needs to be classified and placed into the Company OS GitHub repository. Triggers on requests like "file this document", "where should this go", "arrange this into the repo", "classify this research", or when the user pastes/uploads raw content and asks it to be organized. This skill outputs the exact Department, Type, Code, Filename, Folder Path, and Metadata Header for the document, following the company's governance rules — it does not invent its own classification logic.
---

# Company OS Classifier Skill

This skill implements the classification logic from the Company OS governance documents (`03_RESOURCES/Company_Master_Standards/GOVERNANCE/` in the repository — Docs 01–09). It exists so that **any new document is arranged the same way, every time, regardless of who or what created it.**

## Step-by-step process — follow in order

### Step 1 — Read the input
Read the raw content provided (pasted text, uploaded file, research note, meeting transcript, etc.) in full before classifying anything.

### Step 2 — PARA Bucket
Ask: does this have a clear end date/deliverable?
- Yes → **Project** (goes to `02_PROJECTS/`)
- No, it's an ongoing department function → **Area** (goes to `01_AREAS/[Dept]/`)
- It's shared reference material (template, glossary entry, brand asset, general knowledge) → **Resource** (goes to `03_RESOURCES/`)
- It's superseded/no longer active → **Archive** (goes to `04_ARCHIVE/`)

### Step 3 — Department
Match against `reference/departments.json` (loaded below). If the content is genuinely cross-department, use `PROJ`. If company-wide, use `ALL`. If you cannot confidently determine the department, do not guess — flag it as "Needs human classification: Department unclear" and stop here.

### Step 4 — Document Type
Match against `reference/document-types.json`. Ask: does it instruct (SOP/WI), record (REP/REC/FORM), inform (KB), plan (STRAT/PROJ-DOC), or template (TPL)? If unclear, flag it rather than guessing.

### Step 5 — Duplicate/Existing-Content Check
Before proposing a new document, state clearly: "I have not searched the existing repository for duplicates — please confirm none exists," unless you have actually been given repository search access in this session, in which case search first and report if a similar/authoritative document already exists.

### Step 6 — Code Assignment
Format: `[DEPT]-[TYPE]-[NUMBER]`. If you don't know the next sequential number for that Department+Type combination, use `[DEPT]-[TYPE]-XXX` and flag: "Number needs confirming against the existing sequence."

### Step 7 — Filename
Format: `[CODE] — [Plain-English Title].md`
Never use: "New SOP", "Copy of X", "Temp", "Notes from meeting", "final", "updated2", ALL CAPS titles.

### Step 8 — Folder Path
Apply the Path Formula:
```
01_AREAS/[Department]/[Sub-folder by Type]/[CODE] — [Title].md
```
Sub-folder mapping (Type → folder):
- POL → Policies/
- SOP → SOPs/
- WI → Work_Instructions/
- TPL → Templates/
- REP → Reports/
- REC → Records/
- KB → Knowledge_Reference/
- MEET → Meeting_Notes/
- PROJ-DOC → goes in `02_PROJECTS/[Project Name — Year]/` instead
- STRAT/FORM → place in the Department's `Knowledge_Reference/` or `Templates/` respectively, unless company-wide (then `03_RESOURCES/`)

### Step 9 — Metadata Header
Always generate this exact block at the top of the output document:
```
Code: [DEPT]-[TYPE]-[NUMBER]
Title: [Plain-English Title]
Department: [Doc 01 code]
Type: [Doc 02 code]
PARA Bucket: [Project / Area / Resource / Archive]
Version: v1.0
Lifecycle Status: Draft
Confidentiality: [Public / Internal / Confidential / Restricted — ask if unclear, default to Internal]
Superseded By: N/A
Owner (Accountable): [Role — ask if unclear]
Responsible (does the work): [Role/Name, or "Unassigned"]
Consulted (input required): [Role(s), or "None"]
Informed (notified on changes): [Role(s), or "All Dept"]
Created Date: [today's date]
Last Updated: [today's date]
Tags: [comma-separated keywords derived from the content]
Related Documents: [links/codes, or "None identified yet"]
```

### Step 10 — Breadcrumb + Navigation Wrapper
Add, per Doc 06:
```
Home › 01_AREAS › [Department] › [Sub-folder] › [Title]
```
And close the document with `Related Documents` / `See Also` sections (max ~5–8 combined links), populated only with genuinely relevant links — never invented ones.

### Step 11 — Output Format
Present the result to the user as:
1. **Proposed classification** (Department, Type, PARA Bucket, Code) — in one short block, for quick confirmation
2. **Proposed file path**
3. **The full formatted document** (metadata header + breadcrumb + normalized content), ready to paste into the repository or hand to a Pull Request
4. **Any flags** raised in Steps 3–6 that need human confirmation before this is finalized

**Never silently finalize a classification the input didn't clearly support.** When genuinely ambiguous, ask one direct clarifying question rather than guessing — a wrong classification is worse than a short delay.

### Step 12 — Do not auto-merge
This skill produces a ready-to-review document and its proposed location. It does not commit directly to `main` or open a Pull Request without the user's explicit go-ahead — per the Company OS governance (`GOVERNANCE/05-Repository-Branch-Workflow.md`, Section 5/8), AI-classified content always goes through human review before becoming official.

## Reference files
- `reference/departments.json` — Department Registry (Doc 01)
- `reference/document-types.json` — Document Type Registry (Doc 02)

Load both before classifying — do not rely on memory of past conversations for these values, as the registries may be updated over time.
