# 07 — Governance, Health Dashboard & AI Policy (FINAL)

> **Status: FINAL.** Only the governance mechanisms genuinely missing from Docs 01–04 — trimmed per the Doc 08 audit. Anything that already existed elsewhere is cross-referenced here, not repeated.
> **Version:** 1.1 (trimmed from 14 sections to 9 — see Doc 08 audit) | **Owner:** Workspace Admin / Ops Head

---

## 1. Glossary
Already fully specified in Doc 06, Section 9. No separate rule here — this entry exists only so this document's table of contents stays complete. Read Doc 06 §9 for the actual rule.

---

## 2. Change Log (new)
Every document that reaches `Approved` or later (per Doc 04's Lifecycle) carries a Change Log block at its bottom, one line per version bump:
```
v1.2 → v1.3 | Changed pricing approval process | Approved by [Role] | 2026-08-24
v1.1 → v1.2 | Added exception for international clients | Approved by [Role] | 2026-06-10
```
This sits below the "Related Documents / See Also" block from Doc 06 §7, as the last thing on the page. It is not a replacement for Doc 04's Version/Last Updated metadata fields — it's the human-readable history those fields point to.

---

## 3. Document Ownership Matrix (new — a rollup, not a new rule)
Doc 04 already requires every individual document to name its Owner/Responsible/Consulted/Informed roles in its own metadata header. This section adds one thing on top: a single master table, kept at `03_RESOURCES/Company_Master_Standards/Ownership-Matrix.md`, listing every active document's Code, Title, Department, and Owner in one place — a summary view for quickly answering "who owns X" without opening every individual document. Updated automatically whenever a document's metadata header changes (via the GitHub Action described in Doc 05 §4).

---

## 4. Review Calendar
Already fully specified in Doc 04's Governance table via the `Next Review` metadata field and the Quarterly Audit row. No new rule — Doc 07 originally repeated this and it has been removed. See Doc 04, Governance — Recurring Maintenance.

---

## 5. Deprecation — one new field only
Doc 04's Lifecycle already covers `Under Revision → Retired`, and Doc 03's `04_ARCHIVE` already covers where retired documents go. The one genuinely new addition (already applied to Doc 04's metadata header) is:
```
Superseded By: [Code of the replacement document, or "N/A"]
```
Set this field the moment a document is Retired, so anyone who lands on the old version is pointed straight to its replacement. No separate deprecation process beyond this — the rest already exists in Doc 04.

---

## 6. Exception / Edge-Case Library (new)
Every SOP (Doc 02 type `SOP`) gets an optional section, placed after the main step-by-step process:
```
Common Exceptions / What to Do If...
- If [situation not covered by the standard steps] → [what to do instead]
```
This exists to stop people from silently improvising undocumented workarounds when a real-world case doesn't fit the standard flow — those workarounds get captured here instead, and reviewed into the main SOP if they become common enough.

---

## 7. FAQ from Real Questions (new)
Each department's `01_AREAS/[Dept]/Knowledge_Reference/FAQ.md` collects questions that keep coming up — whether asked to the AI assistant (Doc 05 §6) or in team chat. The Department Owner periodically reviews recurring questions and converts the useful ones into permanent FAQ entries. This is a living document, updated as questions come in, not a one-time write-up.

---

## 8. Feedback Mechanism (new)
Every document at `Published` status (Doc 04 Lifecycle) ends with:
```
Was this helpful?  |  Report outdated information  |  Suggest a change
```
Clicking any of these auto-opens a GitHub Issue (Doc 05 §4), pre-tagged with that document's Department and Code, so feedback routes straight to the right owner without extra steps.

---

## 9. Documentation Health Dashboard (new)

Lives at `03_RESOURCES/Company_Master_Standards/` as a config/index, rendered as a live view (GitHub Projects, or a small script reading every document's metadata header). This is what tells you, at a glance, how healthy the whole system is:

```
Total Documents:        1,284
Outdated (past Next Review date):  37
Awaiting Review:        14
Unowned (no Owner set):  8
Draft (stuck >30 days):  42
Published:               1,183
Broken Internal Links:   3
```

**Automatic cleanup checks** (run via GitHub Actions, per Doc 05 §4 — this detail is genuinely new, distinct from the Quarterly Audit cadence already set in Doc 04):
- Orphan files — not linked from any README/index
- Duplicate documents — same title/topic filed in two places
- Broken internal links
- Outdated SOPs — past their `Next Review` date
- Missing Owner or missing required metadata fields
- Stale research — sitting in a `research/*` branch (Doc 05 §2) with no activity for 60+ days
- Approved-but-never-published documents

These checks run on the same Quarterly Audit cycle Doc 04 already established — this section only adds *what specifically gets checked*, not a new cadence.

---

## 10. AI Knowledge Assistant Rules (new)

**What employees can ask the AI to do:**
```
✅ Find company documents          ✅ Explain SOPs in plain language
✅ Summarize policies               ✅ Find related documents
✅ Build a learning path            ✅ Compare approved documents
```

**Boundaries:**
```
⚠️ Always verify against the source document before treating it as final
⚠️ Don't ask AI to bypass your GitHub permissions
⚠️ Don't paste confidential (per the new Confidentiality field, Doc 04) info into unapproved tools
⚠️ AI-generated text is not automatically official policy
```

**The one rule to teach every employee:**
> *"AI helps you understand the Company OS. The Company OS decides what is official."*

Every AI answer must include its source — e.g. `Source: 01_AREAS/Sales/SOPs/SALES-SOP-002 — v2.1` — so nothing is trusted blindly. The underlying technical access rules (what the AI can/cannot touch) are already defined in Doc 05, Section 6 — this section is the employee-facing version of that same rule.

---

## 11. Canonical-Source Rule (new — distinct from "Single Source of Truth Tool")
Doc 03/04 already establish that all documents live in **one tool only** (no parallel copies in Notion + GitHub + Docs, etc.). This is a related but separate rule, at the *fact* level rather than the *tool* level: **one fact or policy has exactly one authoritative copy**, wherever it lives. Every other mention of that fact anywhere else in the system is a link/reference to that one copy — never a restated duplicate. This is what stops two departments from independently writing slightly different versions of "the same" policy that quietly drift apart over time.

---

## Guiding Principle (three layers working together)

```
Folder navigation (Doc 03/06)   → for humans
Metadata & search (Doc 04)       → for AI
Links — Related/See Also/Glossary (Doc 06) → for learning
```
None of the three should be relied on alone — this is what keeps a large, growing document set feeling small and findable to the person actually using it.
