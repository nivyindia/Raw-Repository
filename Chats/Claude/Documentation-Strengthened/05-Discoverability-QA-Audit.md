# 05 — Discoverability & QA Audit

> **Purpose:** Docs 01–04 define how documents are named, typed, and filed. This document defines how you *verify* the system is actually working — i.e. that a real person can find any document in seconds, not just that it was filed "correctly" on paper.
> **Version:** 1.0 | **Owner:** Workspace Admin | **Status:** Approved
> **Run this:** as part of the Quarterly Audit (see Doc 04, Governance — Recurring Maintenance), and once immediately after this whole Standard (Docs 01–05) goes live.

---

## Part 1 — The 3-Click Test

**Rule:** Starting from the company home / Master Index page (Doc 03), any major content type must be reachable in **≤3 clicks**.

Build a checklist covering each major content type your company has, for example:

| Content Type | Click 1 | Click 2 | Click 3 | Pass? |
|---|---|---|---|---|
| A department SOP | Master Index | Department Area | SOP Index | ☐ |
| A knowledge/reference entry | Master Index | Resources | Knowledge Index | ☐ |
| A project deliverable | Master Index | Projects | [Project] Index | ☐ |
| A cross-department policy | Master Index | Resources | Company Master Standards | ☐ |
| A template | Master Index | Resources | Templates Library | ☐ |
| An archived/retired document | Master Index | Archive | [mirrors original path] | ☐ |

**How to run it:** open the Master Index in a fresh tab with nothing else open, click through each row, count clicks. Anything over 3 clicks gets a shortcut link added and is re-tested.

## Part 2 — Dead-End Audit

**Rule:** Every document must have at least one forward link (to something related) and one back-link (to its parent index/folder).

Check these first — they're the most likely dead ends:
- Brand/division "shell" pages that don't link back to their division home
- Individual SOPs/documents that don't link back to their department's SOP/document index
- Archived documents that don't link forward to the current live replacement
- Old planning/working docs that don't link to the current master plan or project index

Log findings as you go:

| Document | Issue | Fix Applied | Date |
|---|---|---|---|
| *(fill during audit)* | | | |

## Part 3 — Naming Audit

**Rule:** Every document follows the Doc 04 naming rule exactly. No ALL CAPS titles, no double emojis, no underscores, no vague names ("New SOP", "Copy of X", "Temp", "Notes").

Checklist:
- [ ] Search for ALL CAPS titles
- [ ] Search for double/decorative emoji clutter in titles
- [ ] Search for underscores or inconsistent separators in titles
- [ ] Spot-check 10 random documents against the `[CODE] — [Plain-English Title]` format (Doc 04, Step 5)

## Part 4 — Metadata Completeness Audit

For a sample of documents (or all, if the count is manageable):
- [ ] Metadata header (Doc 04) present and fully filled — no blank Owner/Department/Type fields
- [ ] Lifecycle Status matches reality (a document marked `Published` is actually the current live version)
- [ ] Version number matches the Version Control history (Doc 04, Versioning)
- [ ] Listed in the relevant database(s) (Doc 03, Core Databases) — a document that exists as a file but isn't in `company_documents_database`/`all_pages_index` fails this check

---

## Outcome

The workspace/repository "passes" a Quarterly Audit cycle when every row across Parts 1–4 is checked. Findings that can't be fixed immediately are logged with an owner and a fix-by date — they carry over to the next Quarterly Audit if unresolved, per Doc 04's Governance section.
