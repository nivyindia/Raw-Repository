# 04 — Classification & Naming Rulebook

> **This is the master logic file.** It references Doc 01 (Departments), Doc 02 (Types), and Doc 03 (Folders). Feed all four documents together into a Claude Skill or Custom GPT — this file tells the AI *how* to use the other three to classify, name, and place any new document.
> **Version:** 1.0 | **Owner:** Workspace Admin | **Status:** Approved

---

## Step-by-Step Classification Logic

When given any new document, follow these steps in order:

**Step 1 — PARA Bucket** (see Doc 03, Step 0)
→ Is it a Project, an Area (department), a Resource, or already Archive?

**Step 2 — Department**
→ If Area or Project, which department code applies (Doc 01)? If it's cross-department, use `PROJ`. If company-wide, use `ALL`.

**Step 3 — Document Type**
→ Which type code applies (Doc 02)? Ask: does it instruct (SOP/WI), record (REP/REC/FORM), inform (KB), plan (STRAT/PROJ-DOC), or template (TPL)?

**Step 4 — Code Assignment**
→ Format: `[DEPT]-[TYPE]-[NUMBER]` (number = next sequential number for that dept+type combo; start at 001).
→ Example: `RND-SOP-004`

**Step 5 — Name**
→ Format: `[CODE] — [Plain-English Title]`
→ Example: `RND-SOP-004 — New Product Testing Process`
→ Naming Don'ts: no "New SOP", "Copy of X", "Temp", "Notes from meeting", no ALL CAPS titles.

**Step 6 — Folder Path**
→ Apply the Path Formula from Doc 03 using the Department + Type from Steps 2–3.

**Step 7 — Metadata Header** (required at the top of every document — see template below)

**Step 8 — Lifecycle Status** (see table below) — every new document starts at `Draft`.

---

## Required Metadata Header (every document)

```
Code: [DEPT]-[TYPE]-[NUMBER]
Title: [Plain-English Title]
Department: [Doc 01 code]
Type: [Doc 02 code]
PARA Bucket: [Project / Area / Resource / Archive]
Version: v[Major].[Minor]
Lifecycle Status: [Draft / Under Review / Approved / Published / Under Revision / Retired]
Confidentiality: [Public / Internal / Confidential / Restricted]
Superseded By: [Code of replacement document, or "N/A"]
Owner (Accountable): [Role]
Responsible (does the work): [Role/Name]
Consulted (input required): [Role(s), or "None"]
Informed (notified on changes): [Role(s), or "All Dept"]
Created Date: [Date]
Last Updated: [Date]
Next Review: [Date — required once status reaches Approved; see Governance — Recurring Maintenance below]
Tags: [comma-separated keywords]
Related Documents: [links/codes]
```

---

## Lifecycle Workflow

```
Draft → Under Review → Approved → Published → (later) Under Revision → Retired
```

| Status | Meaning | Who Moves It Forward |
|---|---|---|
| Draft | Being written, not yet usable | Responsible person |
| Under Review | Sent to Owner/Consulted parties for feedback | Owner (Accountable role from Doc 01) |
| Approved | Signed off, not yet distributed | Owner |
| Published | Live and in active use | Owner publishes; Informed parties notified |
| Under Revision | An approved doc is being edited — old version stays Published until new one is Approved | Responsible person |
| Retired | No longer in use | Owner moves it to `04_ARCHIVE` (Doc 03), keeps history |

**Rule:** A document cannot skip from Draft straight to Published. A document without a named Owner cannot leave Draft.

---

## Versioning

| Change | Version Bump |
|---|---|
| First publish | v1.0 |
| Minor edit (typo, small clarification) | +0.1 |
| Major edit (process changed/restructured) | +1.0 |

Every edit updates both the Version and Last Updated fields — an edit without a version bump is treated as unauthorised.

---

## Search & Discoverability Requirements

Every document must be:
1. Tagged (Tags field above) with at least: one department tag, one type tag, one status.
2. Listed in the central index/dashboard (the searchable "Start Here" hub — separate deliverable) within 24 hours of reaching `Published`.
3. Named so that Ctrl+F/search on its Code or Title finds it in under 10 seconds.

---

## Governance — Recurring Maintenance

| Task | Frequency | Owner |
|---|---|---|
| Review all `Published` SOPs/Policies for accuracy | Every 3 months (Quarterly Audit) | Each Department Owner |
| Set/update `Next Review` date on every document that reaches `Approved` | At the moment of approval, then again at every subsequent review | Owner (Accountable role) |
| Check for documents with no Owner or stuck in Draft >30 days | Quarterly Audit | Workspace Admin |
| Check for duplicate/orphaned files outside this structure | Quarterly Audit | Workspace Admin |
| Confirm Department & Type registries (Doc 01, 02) are still accurate | Every 6 months | Ops Head |
| Full structure health report to leadership | Quarterly | Workspace Admin |
| Confirm every `Published`/`Approved` document has its Confidentiality field set | Quarterly Audit (same cycle as above) | Workspace Admin |

**Single Source of Truth Rule:** All company documents live in one designated tool only. Any document found outside it during an audit is migrated in or flagged for deletion within the same audit cycle.

---

## Quick Reference — One-Line Summary

*Every document = one PARA bucket + one department + one type + one code + one metadata header + one lifecycle status, stored at exactly one predictable path, reviewed every quarter.*
