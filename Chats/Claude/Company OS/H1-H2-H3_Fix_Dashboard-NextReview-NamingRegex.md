# Fix — v6 Audit Items H1, H2, H3 (High Priority)

**Source:** `Audit-and-Tasks/Company_OS_v6_Audit_and_Implementation_Plan.md` → High Priority section
**Status:** ✅ All 3 fixed below (already applied directly in this package — see merge targets for where each piece lives)

---

## H1 — `dashboard-generate.yml`: "Awaiting Review" always showed 0

**File:** `Company-OS/.github/workflows/dashboard-generate.yml`

**Bug:** Line checked `[[ "$status" == "In Review" ]]`, but Doc 04's real Lifecycle Status enum uses `Under Review`, not `In Review`. No document could ever match.

```diff
- [[ "$status" == "In Review" ]] && AWAITING_REVIEW=$((AWAITING_REVIEW+1))
+ [[ "$status" == "Under Review" ]] && AWAITING_REVIEW=$((AWAITING_REVIEW+1))
```

**Merge target:** Replaces this one line inside `Company-OS/.github/workflows/dashboard-generate.yml`. No other changes needed.

---

## H2 — `Next Review` field used by 2 workflows but never defined in Doc 04

**Files affected:**
- `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/04-Classification-Naming-Rulebook.md`
- `Company-OS/.github/PULL_REQUEST_TEMPLATE.md`

**Bug:** `health-report.yml` and `dashboard-generate.yml` both `grep "^Next Review:"` to compute the "Outdated" metric, but Doc 04's Required Metadata Header template never included this field — despite Doc 07 §4 and Doc 08 both claiming it already exists there. "Outdated" always read 0.

**Fix applied — Doc 04, Required Metadata Header (added one line):**
```diff
  Created Date: [Date]
  Last Updated: [Date]
+ Next Review: [Date — required once status reaches Approved; see Governance — Recurring Maintenance below]
  Tags: [comma-separated keywords]
  Related Documents: [links/codes]
```

**Fix applied — Doc 04, Governance — Recurring Maintenance table (added one row):**
```diff
  | Task | Frequency | Owner |
  |---|---|---|
  | Review all `Published` SOPs/Policies for accuracy | Every 3 months (Quarterly Audit) | Each Department Owner |
+ | Set/update `Next Review` date on every document that reaches `Approved` | At the moment of approval, then again at every subsequent review | Owner (Accountable role) |
  | Check for documents with no Owner or stuck in Draft >30 days | Quarterly Audit | Workspace Admin |
```

**Fix applied — `PULL_REQUEST_TEMPLATE.md` checklist (added field name):**
```diff
- - [ ] Metadata header complete (Code, Title, Department, Type, PARA Bucket, Version, Lifecycle Status, Confidentiality, Owner/RACI, Dates, Tags)
+ - [ ] Metadata header complete (Code, Title, Department, Type, PARA Bucket, Version, Lifecycle Status, Confidentiality, Owner/RACI, Dates, Next Review, Tags)
```

**Note — existing documents:** `Brands.md`, `Company-Overview.md`, `Glossary.md`, `Org-Chart.md` and the `Research-OS-Skill/Document-Type-Mapping.md` added earlier this session all pre-date this field and don't have a `Next Review:` line yet. This is expected — they're `Draft` status, and the new rule only requires the field once a document reaches `Approved`. No retroactive edit needed unless/until one of them is approved.

**Merge target:** Two edits inside `GOVERNANCE/04-Classification-Naming-Rulebook.md` (header template + maintenance table), one edit inside `.github/PULL_REQUEST_TEMPLATE.md`.

---

## H3 — `validate-naming.yml` regex rejected its own governance docs' PROJ-DOC example

**File:** `Company-OS/.github/workflows/validate-naming.yml`

**Bug:** The filename regex required the number segment to be digits-only (`[0-9]+`). But Doc 03/04's own canonical example for a Project Document — `PROJ-DOC-Website2026 — Project Plan.md` — uses `Website2026`, an alphanumeric short-code, not a sequential integer. Any PR naming a project doc per the documented convention would fail CI.

**Fix applied — branch the check by code type:**
```diff
- # Filename pattern: CODE — Title.md   where CODE = DEPT-TYPE-NUMBER
- if ! [[ "$base" =~ ^[A-Z]+-[A-Z-]+-[0-9]+" — ".+\.md$ ]]; then
-   echo "::error file=$file::Filename does not match '[DEPT]-[TYPE]-[NUMBER] — Title.md' pattern (see GOVERNANCE/04-Classification-Naming-Rulebook.md)"
-   FAILED=1
- fi
+ # Filename pattern: CODE — Title.md
+ # PROJ-DOC codes use an alphanumeric project short-code instead of a
+ # sequential number (e.g. PROJ-DOC-Website2026 — Project Plan.md, per
+ # Doc 03/04's own canonical example) — checked separately from the
+ # standard [DEPT]-[TYPE]-[NUMBER] pattern used by every other type.
+ if [[ "$base" == PROJ-DOC-* ]]; then
+   if ! [[ "$base" =~ ^PROJ-DOC-[A-Za-z0-9]+" — ".+\.md$ ]]; then
+     echo "::error file=$file::Filename does not match 'PROJ-DOC-[ShortCode] — Title.md' pattern (see GOVERNANCE/04-Classification-Naming-Rulebook.md)"
+     FAILED=1
+   fi
+ elif ! [[ "$base" =~ ^[A-Z]+-[A-Z]+-[0-9]+" — ".+\.md$ ]]; then
+   echo "::error file=$file::Filename does not match '[DEPT]-[TYPE]-[NUMBER] — Title.md' pattern (see GOVERNANCE/04-Classification-Naming-Rulebook.md)"
+   FAILED=1
+ fi
```

**Verified against:**
| Filename | Old regex | New regex |
|---|---|---|
| `PROJ-DOC-Website2026 — Project Plan.md` | ❌ FAIL (false positive) | ✅ PASS |
| `RND-SOP-004 — New Product Testing Process.md` | ✅ PASS | ✅ PASS |
| `STR-STRAT-003 — 2026 Growth Roadmap.md` | ✅ PASS | ✅ PASS |
| `QA-FORM-002 — QC Checklist.md` | ✅ PASS | ✅ PASS |
| `badname.md` | ✅ correctly rejected | ✅ correctly rejected |

**Note:** Tightened `[A-Z-]+` → `[A-Z]+` for the TYPE segment on the non-PROJ-DOC branch, since hyphenated type codes are now handled explicitly by the PROJ-DOC branch — this doesn't change behavior for any other type code (all of POL/SOP/WI/TPL/REP/REC/KB/STRAT/FORM/MEET/ARCH are plain letters, no hyphens).

**Merge target:** Replaces the filename-pattern check block inside `Company-OS/.github/workflows/validate-naming.yml`. The folder-placement check below it (M2 in the plan — still open) is untouched.

---

## Action for you
All three fixes are already applied directly in the extracted package this session — nothing further to paste in for H1–H3. If you're tracking against a separate copy of the repo, apply the 5 diffs above (1 in dashboard-generate.yml, 3 in Doc 04 + PR template combined, 1 in validate-naming.yml).

Tick H1, H2, H3 in `Company_OS_v6_Audit_and_Implementation_Plan.md`'s priority table. M1, M2, M3, M4 and L1–L3 remain open — M2 (STRAT/FORM folder placement) still needs your design decision before it can be drafted.
