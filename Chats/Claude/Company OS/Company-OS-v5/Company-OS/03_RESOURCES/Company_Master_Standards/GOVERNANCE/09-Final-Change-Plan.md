# 09 — Final Change Plan (Exact Additions to Docs 01–07)

> **Purpose:** This is the single source of truth for what will actually be added/edited in the existing 7 documents. Nothing here is applied yet — this is the plan to confirm before I edit Docs 01–07 directly.
> **Confirmed decision:** The **multi-company structure** (Shared-OS + one repository per company/brand) is kept as originally proposed in Doc 05 — this is final, not being changed.

---

## Doc 01 — Department & Code Registry
**No changes.** Already final and confirmed by you earlier. Section C (Brand/Division codes placeholder) still needs your actual brand names whenever you're ready — that's the only open item, and it's an input from you, not a structural change.

---

## Doc 02 — Document Type & Code Registry
**No changes.** Already final.

---

## Doc 03 — Folder Structure Map (PARA-Integrated)
**No changes.** Keeping your original folder names exactly as they are:
`01_AREAS`, `02_PROJECTS`, `03_RESOURCES`, `04_ARCHIVE`, and the department sub-folder pattern (`Policies/SOPs/Work_Instructions/Templates/Reports/Records/Knowledge_Reference/Meeting_Notes`).

**Correction applied:** Doc 06's earlier attempt to rename these to `DEPARTMENTS/POLICIES/SOP-LIBRARY/...` is dropped. Doc 06 will instead be rewritten to add navigation *on top of* these existing names, not replace them.

---

## Doc 04 — Classification & Naming Rulebook
**One addition:**
- Add a new metadata field to the Required Metadata Header: `Confidentiality: Public / Internal / Confidential / Restricted`, placed right after `Lifecycle Status`.
- Add one line to the Governance table: `Confirm Confidentiality tag is set` as part of the existing Quarterly Audit row (not a new row — folded into the audit that already exists there).

Everything else in Doc 04 (RACI, Lifecycle, Versioning, Search requirements) stays exactly as is.

---

## Doc 05 — Repository, Branch & GitHub Workflow
**Kept in full, this is genuinely new content, multi-company structure confirmed:**
- Repository strategy: `Shared-OS` + one `[Company]-OS` per company/brand (Section 1) — **this is the structure you're confirming to keep**
- Branch strategy: `main` / `research/*` / `sop/*` / `process/*` / `feature/*` / `hotfix/*`, publish handled via a `publish:true` metadata tag + GitHub Action (not a permanent branch) — Section 2
- Document lifecycle → branch/repo mapping — Section 3
- GitHub-native feature map (Issues, Projects, PRs, Actions, CODEOWNERS, Rulesets, Labels, Milestones, Discussions, Teams/Permissions, Tags/Releases) — Section 4
- Research-Inbox as a separate repo, with AI-classification-via-PR flow — Section 5
- AI access rules + Golden Rule (AI answer ≠ official; Published document is official) — Section 6
- Governance-as-code (Docs 01–07 themselves live versioned inside `Shared-OS/GOVERNANCE/`) — Section 7

No changes needed — this document stands as written.

---

## Doc 06 — Navigation & Employee Experience Standard
**Being rewritten** to fix the audit finding — same navigation content, but now built on top of Doc 03's existing folder names instead of replacing them:

| Was (wrong) | Becomes (correct) |
|---|---|
| `DEPARTMENTS/[Dept]/README.md` | `01_AREAS/[Dept]/README.md` |
| `POLICIES/`, `SOP-LIBRARY/`, `WORKFLOWS/`, `KNOWLEDGE-BASE/`, `TEMPLATES/`, `DECISIONS/`, `PROJECTS/`, `DASHBOARD/`, `ARCHIVE/` at repo root | These map onto Doc 03's existing structure: company-wide Policies/SOPs live in `03_RESOURCES/Company_Master_Standards/`; department-specific ones stay inside each department's own `Policies/`, `SOPs/` folders (already defined in Doc 03); `02_PROJECTS/` and `04_ARCHIVE/` are unchanged from Doc 03 |
| Department internal folders `SOPs/, Templates/, Checklists/, Workflows/, Reports/, Policies/, Archive/` | Replaced with Doc 03's existing set: `Policies/, SOPs/, Work_Instructions/, Templates/, Reports/, Records/, Knowledge_Reference/, Meeting_Notes/` |

**Everything else in Doc 06 stays exactly as written** (this was all genuinely new, not duplicated anywhere):
- 5 Navigation Layers (Section 3)
- README standard per level, including the Company Home 6-block layout (Section 4)
- Two Navigation Modes + Search, always all three available (Section 5)
- Guided Topic Reading Sequence: Intro→Concepts→Process→SOP→Examples→Checklist→FAQ→Related (Section 6)
- Document Page Standard: Breadcrumb + metadata header + TOC + content + Related Documents/See Also + Previous/Next (Section 7) — this now explicitly references Doc 04's metadata header rather than redefining it
- New Employee Journey, 7 steps (Section 8)
- Glossary requirement, `Knowledge_Reference/Glossary.md` (path updated to match Doc 03's naming) (Section 9)
- Dashboard as navigation hub (Section 10)

---

## Doc 07 — Governance, Health Dashboard & AI Policy
**Being trimmed** per the audit — removing what duplicated Docs 01–04, keeping only what's genuinely new:

**Removed (already covered elsewhere, kept only as a one-line cross-reference):**
- §4 Review Calendar → replaced with: *"See Doc 04, Section on Lifecycle/Governance — Next Review field already covers this."*
- §5 Deprecation System → trimmed to only the new detail: add a `Superseded By: [code]` field to the metadata header (Doc 04) when a document is retired. The rest of the deprecation flow already exists in Doc 04's Lifecycle.
- §7 Templates Library → removed entirely (fully covered by Doc 03's `TEMPLATES` folder concept + Doc 04's 5 ready templates).
- §12's "quarterly" cadence line → removed (already in Doc 04's Governance table); the specific checklist items are kept (see below).

**Kept — genuinely new:**
- §1 Glossary → cross-reference to Doc 06 §9
- §2 Change Log block format (`v1.2 → v1.3 | what changed | approved by | date`) — new
- §3 Document Ownership Matrix as a rolled-up master table (summary view across all documents, distinct from Doc 04's per-document RACI) — new
- §6 Exception/Edge-Case Library section inside SOPs — new
- §8 FAQ-from-real-questions process — new
- §9 Feedback mechanism (`Was this helpful? / Report outdated / Suggest a change` → auto-opens GitHub Issue) — new
- §11 Confidentiality classification — this becomes a cross-reference to Doc 04's new metadata field (added above), not a separate rule
- §12 Documentation Health Dashboard — new, this was your explicit ask. Keeps the specific metrics (Total/Outdated/Awaiting Review/Unowned/Draft/Published/Broken Links) and the automatic-cleanup checklist (orphan files, duplicates, broken links, missing owners, stale research, unpublished-approved docs)
- §13 AI Knowledge Assistant Rules — new, cross-referenced with Doc 05 §6
- §14 Canonical-Source Rule — new, distinct from the "single tool" rule already in Doc 03/04

---

## Net Result After These Edits

- **Docs 01, 02, 05 — untouched**, stand as final
- **Docs 03 — untouched**, your original naming preserved as the one and only folder-naming standard
- **Doc 04 — one field added** (Confidentiality)
- **Doc 06 — same content, corrected to build on Doc 03 instead of replacing it**
- **Doc 07 — shrinks from 14 sections to 9**, all genuinely new, each cross-referencing the existing doc it relates to instead of repeating it

Confirm and I'll apply these edits directly to Docs 03(unchanged)/04/06/07 now.
