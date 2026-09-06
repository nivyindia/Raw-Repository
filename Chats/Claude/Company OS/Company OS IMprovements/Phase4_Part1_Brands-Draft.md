# Fix — Phase 4, Part 1: Fill Brands.md brand/division codes

**Source:** Company_OS_Task_List.md → Phase 4, item 1
**Files affected (replace):** `03_RESOURCES/Company_Master_Standards/Brands.md`, `03_RESOURCES/Company_Master_Standards/GOVERNANCE/01-Department-Code-Registry.md` (Section C)
**Status:** 🟡 Draft ready — 2 of 6 entities confirmed, 4 tentative (need your confirm/correct)

---

## What I had to work with

I checked every file in the zip plus memory for any existing description of these 6 entities. Result:

| Entity | Found where | Confidence |
|---|---|---|
| Nivy Advisory | Known from prior context — cross-border tax, accounting & CPA firm (US/UK/Canada/Australia/UAE/Singapore) | 🟢 Confirmed |
| Nivy Next | Known from prior context — digital services (AI automation, web/app dev, design, video, VA services, digital marketing) | 🟢 Confirmed |
| Nivy Academy | Only the name exists (in Task_List.md item text) — no description anywhere in the repo or prior context | 🟡 Tentative guess |
| Nivy Alliance | Only the name exists — no description anywhere | 🟡 Tentative guess |
| Nivy Jobs | Only the name exists — no description anywhere | 🟡 Tentative guess |
| Nivy Care Foundation | Only the name exists — no description anywhere | 🟡 Tentative guess |

For the 4 tentative ones I've written a short guess purely from the name so the table isn't empty — **please correct these**, don't treat them as fact.

---

## Proposed codes

Following the existing pattern in Doc 01 (`NXT` example already given for Nivy Next):

| Code | Division | Status |
|---|---|---|
| ADV | Nivy Advisory — cross-border tax, accounting & CPA services (US, UK, Canada, Australia, UAE, Singapore) | 🟢 Confirmed |
| NXT | Nivy Next — digital services: AI automation, web/app development, design, video, VA services, digital marketing | 🟢 Confirmed |
| ACAD | Nivy Academy — *(tentative: training/education arm)* | 🟡 Needs confirm |
| ALNC | Nivy Alliance — *(tentative: partner/franchise network)* | 🟡 Needs confirm |
| JOBS | Nivy Jobs — *(tentative: recruitment/job placement services)* | 🟡 Needs confirm |
| CARE | Nivy Care Foundation — *(tentative: CSR/non-profit/social impact arm)* | 🟡 Needs confirm |

---

## Fix 1 — `Brands.md` (full replacement content)

```markdown
# Brands / Divisions

Code: ALL-KB-003
Title: Brands and Divisions
Department: ALL
Type: KB
Version: v1.1
Lifecycle Status: Draft
Confidentiality: Internal
Owner (Accountable): CEO Office

| Code | Brand/Division | Description | Status |
|---|---|---|---|
| ADV | Nivy Advisory | Cross-border tax, accounting & CPA services — US, UK, Canada, Australia, UAE, Singapore | Confirmed |
| NXT | Nivy Next | Digital services division — AI automation, web/app development, design, video, VA services, digital marketing | Confirmed |
| ACAD | Nivy Academy | *(tentative — training/education arm; confirm actual scope)* | Needs confirm |
| ALNC | Nivy Alliance | *(tentative — partner/franchise network; confirm actual scope)* | Needs confirm |
| JOBS | Nivy Jobs | *(tentative — recruitment/job placement services; confirm actual scope)* | Needs confirm |
| CARE | Nivy Care Foundation | *(tentative — CSR/non-profit/social impact arm; confirm actual scope)* | Needs confirm |

See `GOVERNANCE/01-Department-Code-Registry.md` Section C for the canonical code table — this page is the descriptive companion to it.
```

## Fix 2 — `01-Department-Code-Registry.md` Section C (replace this section only)

```markdown
## C. Brand / Division Codes (if applicable to your company)

| Code | Division | Status |
|---|---|---|
| ADV | Nivy Advisory | Confirmed |
| NXT | Nivy Next | Confirmed |
| ACAD | Nivy Academy | Needs confirm |
| ALNC | Nivy Alliance | Needs confirm |
| JOBS | Nivy Jobs | Needs confirm |
| CARE | Nivy Care Foundation | Needs confirm |
```

---

## Replacement Map

| This content | Goes in file | Folder |
|---|---|---|
| "Fix 1" block above | `Brands.md` (replace entire file) | `Company-OS/03_RESOURCES/Company_Master_Standards/` |
| "Fix 2" block above | `01-Department-Code-Registry.md` (replace only Section C, leave A/B/D untouched) | `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/` |
| This draft file itself | `Phase4_Part1_Brands-Draft.md` (reference copy, optional to keep) | `Audit-and-Tasks/` |

---

## Action for you
1. Reply with corrections for the 4 tentative entities (Academy, Alliance, Jobs, Care Foundation) — even one line each is enough.
2. Once confirmed, paste Fix 1 into `Brands.md` and Fix 2 into Doc 01 Section C.
3. Tick Phase 4 item 1 in `Company_OS_Task_List.md` once both files are updated.
