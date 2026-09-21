# Fix — Phase 4, Part 3: Map Research OS's 12-step naming to Company-OS Document-Type codes

**Source:** `Company_OS_Task_List.md` → Phase 4, item 3
**File affected (new):** `Research-OS-Skill/Document-Type-Mapping.md`
**Status:** 🟢 Draft ready — no open questions, ready to paste

---

## Why this was flagged
`Company_OS_Full_Audit.md` §3 item 2: Research_OS_Skill.zip's 12-step framework wasn't in the earlier upload, so nobody had confirmed its step naming actually aligns with the Company-OS Document-Type registry (REP/REC/KB). It's present in this v5 upload now, so here's the mapping.

`Research-OS-Skill/SKILL.md` Step 12 already hardcodes `Type=REP` for the final report — that part was already correct. Nothing else in the 12 steps was mapped anywhere.

## Proposed mapping

| Research OS step(s) | What it produces | Company-OS Type | PARA Bucket | Filed where |
|---|---|---|---|---|
| 0 Research Brief, 1 Research Question, 2 Research Protocol | Project scoping docs | `PROJ-DOC` | Project | `02_PROJECTS/[Research Topic — Year]/` |
| 3 Search Strategy | Working search plan | `PROJ-DOC` (same folder, appended) | Project | same as above |
| 4 Discovery Research, 5 Primary Source Verification, 6 Evidence Extraction | Working evidence log / source library | `REC` | Project | `02_PROJECTS/[Research Topic — Year]/` — kept as a working record, not filed as a department doc |
| 7 Deep Analysis, 8 Quality Gate, 9 Company-Specific Application | Working analysis — folds into Step 11 | *(not filed separately)* | — | — |
| 10 Implementation System → "SOPs Required" section | New standard operating procedures, once approved | `SOP` | Area | `01_AREAS/[receiving Dept]/SOPs/` — must be pulled out and re-filed here, **not** left buried inside the research report |
| 11 Final Research Report | Decision-ready report | `REP` | Project (or Area if it's a recurring research cadence) | `02_PROJECTS/[Research Topic — Year]/` or dept `Reports/` |
| 12 File in Knowledge Base | Confirms/records the above | `REP` *(already correct in SKILL.md)* | — | as above |

**Key point:** the one place a research run produces something other than `REP` is Step 10's "SOPs Required" list — each of those, once actually adopted, needs to be extracted and classified as its own `SOP` document under the receiving department, not left as a subsection of the report.

## Fix — new file `Research-OS-Skill/Document-Type-Mapping.md`

```markdown
# Research OS → Company-OS Document-Type Mapping

Code: ALL-KB-005
Title: Research OS Step-to-Document-Type Mapping
Department: ALL
Type: KB
Version: v1.0
Lifecycle Status: Draft
Confidentiality: Internal
Owner (Accountable): CEO Office

> Companion reference for `Research-OS-Skill/SKILL.md`. Explains which Company-OS Document-Type code (Doc 02) each of the 12 Research OS steps' output maps to, so research output gets filed consistently instead of ad hoc.

| Research OS Step | Output | Type Code | PARA Bucket | Folder |
|---|---|---|---|---|
| 0–2 Brief / Question / Protocol | Project scoping docs | PROJ-DOC | Project | `02_PROJECTS/[Research Topic — Year]/` |
| 3 Search Strategy | Working search plan | PROJ-DOC | Project | `02_PROJECTS/[Research Topic — Year]/` |
| 4–6 Discovery / Verification / Extraction | Evidence log, source library | REC | Project | `02_PROJECTS/[Research Topic — Year]/` |
| 7–9 Analysis / Quality Gate / Application | Working analysis | — (folded into Step 11) | — | — |
| 10 Implementation System — SOPs Required | New SOPs, once approved | SOP | Area | `01_AREAS/[receiving Dept]/SOPs/` |
| 11 Final Research Report | Decision-ready report | REP | Project / Area | `02_PROJECTS/[...]/` or dept `Reports/` |
| 12 File in Knowledge Base | Confirms/records report | REP | — | as above |

See also: `GOVERNANCE/02-Document-Type-Code-Registry.md`, `Research-OS-Skill/SKILL.md`.
```

## Optional companion fix — one line added to `SKILL.md` Step 12
Not required, but ties the two files together for anyone reading the skill cold:

```markdown
### STEP 12 — File it in the Company Knowledge Base
Once the report is done, store it per the company's actual documentation standard (if this Claude account also has the Company OS Classifier skill/governance available, use that — Department, Type=REP, full metadata header). See `Document-Type-Mapping.md` in this folder for how every earlier step's output should be classified, not just the final report. At minimum, capture: Research Title, Department, Research Owner, Research Date, Version, Research Question, Research Scope, Sources, Confidence Level, Key Findings, Recommendations, SOPs Created, KPIs, Next Review Date.
```

---

## Replacement Map

| This content | Goes in file | Folder |
|---|---|---|
| "Fix" block above | New file: `Document-Type-Mapping.md` | `Research-OS-Skill/` |
| "Optional companion fix" block | Replaces existing Step 12 paragraph only, rest of `SKILL.md` untouched | `Research-OS-Skill/` |
| This draft file itself | `Phase4_Part3_ResearchOS-Mapping.md` (reference copy, optional to keep) | `Audit-and-Tasks/` |

## Action for you
1. Paste the new-file block into `Research-OS-Skill/Document-Type-Mapping.md`.
2. Optionally paste the Step 12 replacement into `SKILL.md`.
3. Tick Phase 4 item 3 in `Company_OS_Task_List.md`.
