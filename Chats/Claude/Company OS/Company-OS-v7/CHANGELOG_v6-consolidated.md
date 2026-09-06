# Company OS v6 — Consolidated Changelog

This package merges **H1–H3**, **M1–M4**, and **L1–L2** from the v6 audit directly into the repo files. **L3 remains open** (needs real GitHub handles from you — nothing to merge yet).

---

## H1 — `dashboard-generate.yml`: "Awaiting Review" status string
**File:** `Company-OS/.github/workflows/dashboard-generate.yml`
Changed `"In Review"` → `"Under Review"` in the status-match line, matching Doc 04's actual Lifecycle Status enum. Metric now computes correctly instead of always reading 0.

## H2 — `Next Review` field
**Files:**
- `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/04-Classification-Naming-Rulebook.md` — added `Next Review: [Date]` to the Required Metadata Header template, and a row to the Recurring Maintenance table.
- `Company-OS/.github/PULL_REQUEST_TEMPLATE.md` — added `Next Review` to the metadata-completeness checklist item.

Existing Draft-status docs (`Brands.md`, `Company-Overview.md`, `Glossary.md`, `Org-Chart.md`, `Document-Type-Mapping.md`, and the new `FAQ.md`/`Ownership-Matrix.md` seeds) intentionally do **not** get a retroactive `Next Review:` line — the field is only required once a document reaches `Approved`.

## H3 — `validate-naming.yml` filename regex
**File:** `Company-OS/.github/workflows/validate-naming.yml`
Split the filename check into two branches: `PROJ-DOC-*` files now match `PROJ-DOC-[ShortCode] — Title.md` (alphanumeric short-code allowed), everything else keeps the strict `[DEPT]-[TYPE]-[NUMBER] — Title.md` pattern. Fixes the false-positive CI failure on the docs' own canonical `PROJ-DOC-Website2026` example.

## M1 — Confidentiality value validation
**File:** `Company-OS/.github/workflows/validate-metadata.yml`
Added a value check after the existing presence check: `Confidentiality:` must now be one of `Public / Internal / Confidential / Restricted`, not just present. Closes the gap between what Doc 10 §1 claimed and what the workflow actually did.

## M2 — STRAT / FORM folder placement
**Files:**
- `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/03-Folder-Structure-Map.md` — added `Strategy/` and `Forms/` to the "Inside Every Department" structure.
- `Company-OS/.github/workflows/validate-naming.yml` — added `TYPE_FOLDER["STRAT"]="Strategy"` and `TYPE_FOLDER["FORM"]="Forms"`.
- All 16 department folders under `Company-OS/01_AREAS/` — added physical `Strategy/.gitkeep` and `Forms/.gitkeep`.

Design decision applied: dedicated folders (not folded into Templates/Records), for parity with every other document type.

## M3 — Shallow checkout
**Files:** `Company-OS/.github/workflows/health-report.yml`, `Company-OS/.github/workflows/dashboard-generate.yml`
Added `with: { fetch-depth: 0 }` to both `actions/checkout@v4` steps, so `git log` staleness calculations see real file history.

## M4 — Ownership Matrix
**Files (new):**
- `Company-OS/.github/workflows/ownership-matrix-generate.yml` — scans all metadata headers on push to `main` and regenerates the matrix, then commits it back.
- `Company-OS/03_RESOURCES/Company_Master_Standards/Ownership-Matrix.md` — seeded with headers, ready for the workflow's first run.

Doc 07 §3's existing claim (auto-updating ownership matrix) is now actually true.

## L1 — Per-department FAQ.md seeds
**Files (new, 16):** `Company-OS/01_AREAS/[DEPT]/Knowledge_Reference/FAQ.md` for all 16 departments (CEO, STR, OPS, FIN, HR, TECH, MKT, LEG, RISK, DATA, SALES, RND, PMO, ADMIN, QA, CS). Each seeded with a full metadata header (Draft status, correct `Code`/`Department`/`Owner` per Doc 01) and an empty Q&A section.

## L2 — Company-Overview.md, Org-Chart.md, Welcome.md
**Files:**
- `Company-OS/03_RESOURCES/Company_Master_Standards/Company-Overview.md` — filled with confirmed facts (Billion Dreams United, founder Abhishek Dayal "Nivy", Lucknow HQ, target markets US/UK/Canada/Australia/UAE); Vision, Mission, History, and other leadership roles flagged `Needs confirm`.
- `Company-OS/03_RESOURCES/Company_Master_Standards/Org-Chart.md` — filled with the one confirmed node (Founder/CEO); reporting lines below that flagged `Needs confirm`.
- `Company-OS/START-HERE/Welcome.md` — `[Company Name]` placeholder replaced with "Billion Dreams United".

## L3 — CODEOWNERS (not merged — still open)
**File:** `Company-OS/CODEOWNERS`
Left untouched. The 19 placeholder handles (`@ceo-office`, `@cfo`, etc.) need real GitHub usernames or team handles — there's no source anywhere in the package to derive them from, and guessing would silently break PR approval routing. Send the department → GitHub-handle mapping and this can be closed out the same way as everything above.

---

## Also updated
- `Company_OS_v6_Audit_and_Implementation_Plan.md` — status note added at the top pointing here, so the audit and the actual repo state stay in sync.
