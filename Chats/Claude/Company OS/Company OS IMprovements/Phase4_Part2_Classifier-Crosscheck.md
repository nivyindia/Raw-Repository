# Fix — Phase 4, Part 2: Re-check classifier skill JSON against 12-type registry

**Source:** `Company_OS_Task_List.md` → Phase 4, item 2
**Files checked (no changes needed):** `Classifier-Skill/reference/document-types.json`, `Classifier-Skill/reference/departments.json`
**Compared against:** `03_RESOURCES/Company_Master_Standards/GOVERNANCE/02-Document-Type-Code-Registry.md`, `GOVERNANCE/01-Department-Code-Registry.md`
**Status:** 🟢 Verified — no mismatch, no file edit required, item can be ticked done

---

## Why this was flagged
`Company_OS_Full_Audit.md` §3 item 1 carried this over as unresolved: the v2/v3 classifier JSON once had 12 types listed while the canonical registry only recognized 8 — an internal contradiction (it even listed `ARCH` as "not a fresh type" and still counted it as one). The registry was fixed to 12 types in v4, but the classifier JSON itself wasn't in that upload to re-verify against.

The JSON is present in this v5 upload, so I compared it directly.

## Document-type check

| Code | Doc 02 (registry) | document-types.json | Match |
|---|---|---|---|
| POL | ✅ | ✅ | ✅ |
| SOP | ✅ | ✅ | ✅ |
| WI | ✅ | ✅ | ✅ |
| TPL | ✅ | ✅ | ✅ |
| REP | ✅ | ✅ | ✅ |
| REC | ✅ | ✅ | ✅ |
| KB | ✅ | ✅ | ✅ |
| PROJ-DOC | ✅ | ✅ | ✅ |
| STRAT | ✅ | ✅ | ✅ |
| FORM | ✅ | ✅ | ✅ |
| MEET | ✅ | ✅ | ✅ |
| ARCH | ✅ (marked "status, not a fresh type") | ✅ (same wording) | ✅ |

Count: 12 / 12 both sides. Same order, same descriptions, no extras, no gaps. The old contradiction is fully resolved in this version — nothing to fix.

## Bonus check — departments.json vs Doc 01
Not explicitly asked for, but same failure mode (JSON drifting from registry), so I checked it too: all 18 codes in `departments.json` (Sections A + B + D of Doc 01: CEO, STR, OPS, FIN, HR, TECH, MKT, LEG, RISK, DATA, SALES, RND, PMO, ADMIN, QA, CS, ALL, PROJ) match exactly.

One thing worth noting, not a bug: `departments.json`'s `brand_division_codes` field still just points to Doc 01 Section C rather than listing brand codes inline. That's correct as-is (Section C is the single source of truth) — but once Part 1's brand codes are confirmed and pasted in, you could optionally mirror them into this JSON field too so the classifier doesn't need to open a second file mid-task. Flagging as optional, not required for this item.

---

## Action for you
1. Nothing to paste — this item needed no file changes.
2. Tick Phase 4 item 2 in `Company_OS_Task_List.md`.
