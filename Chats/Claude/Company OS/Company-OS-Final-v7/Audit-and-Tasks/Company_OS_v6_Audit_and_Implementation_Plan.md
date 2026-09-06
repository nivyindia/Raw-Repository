# Company OS v6 — Post-Merge Audit & Implementation Plan

**Scope:** Line-by-line re-audit of `Company-OS-Final-v6.zip` — cross-checked every GitHub Actions workflow's actual logic against what the governance docs (01–10) claim it does, not just whether files exist. This goes deeper than the v5 audit, which mostly checked "does the file exist / is it referenced correctly" — this pass checks "does the code inside the file actually do what the docs say it does."

**Method:** Every claim below was verified by running the actual regex/comparison logic from the workflow file against real values from the governance docs (shown as bash test snippets), not just read side-by-side.

**Status:** 7 confirmed issues. 3 High (silently produce wrong/zero output or reject valid documents) — **all 3 now fixed**, see `H1-H2-H3_Fix_Dashboard-NextReview-NamingRegex.md`. 4 Medium/Low still open. None of these were caught in the v5 audit — they live one layer deeper, in workflow logic vs. doc logic, not doc vs. doc.

---

## 🔴 High Priority — silently wrong output or false CI failures

### H1. `dashboard-generate.yml` — "Awaiting Review" will always show 0
**File:** `Company-OS/.github/workflows/dashboard-generate.yml`, line 31
**Bug:** Checks `[[ "$status" == "In Review" ]]`. But Doc 04's actual Lifecycle Status enum (line 48) is `Draft / Under Review / Approved / Published / Under Revision / Retired` — the real value is **`Under Review`**, not `In Review`.
**Impact:** No document will ever match this string. The dashboard's "Awaiting Review" metric — the exact field this workflow was built to newly compute — is broken from day one, and will silently report 0 forever with no error.
**Note:** This bug is in a file added *this session* (fix 2.5), copied verbatim from the improvements draft without cross-checking the actual status enum in Doc 04.
**Fix:** One-word change: `"In Review"` → `"Under Review"`.

### H2. `Next Review` field is used by 2 workflows but doesn't exist in any document
**Files:** `health-report.yml` (pre-existing) and `dashboard-generate.yml` (added this session) both `grep -m1 "^Next Review:"` to compute the "Outdated" metric.
**Bug:** Doc 04's Required Metadata Header template (the canonical list every document is supposed to follow) has **no `Next Review:` field** — it has `Created Date`, `Last Updated`, `Tags`, `Related Documents`, but nothing about a next-review date.
**Deeper problem:** Doc 07 §4 and Doc 08 both explicitly *claim* "Doc 04 already had a full Review Cycle + 'Next Review' metadata field" — but that field is not actually in Doc 04. This is a doc-to-doc contradiction that both the v4 and v5 audits missed, and it means "Outdated (past Next Review date)" — a headline metric in both the weekly health report and the new dashboard — will always read 0, for every document, forever, with no error or warning.
**Fix (needs a decision, not just a patch):**
- **Option A (recommended):** Add `Next Review: [Date]` to Doc 04's Required Metadata Header template, and to the PR template checklist. This is the smallest change and matches what Doc 07/08 already assume exists.
- **Option B:** Remove the "Outdated" metric from both workflows and reword Doc 07 §9 / Doc 08 to stop claiming the field exists, replacing it with a Lifecycle-Status-age-based check instead (e.g. "Published docs not touched in 180+ days").
- Recommend A — it's a 2-line change vs. rewriting 2 workflows + 2 governance docs, and it's clearly what the original author intended (the field is referenced 6 times across Docs 07, 08, 09, 10 — it was just never actually added to Doc 04's template).

### H3. `validate-naming.yml`'s own filename regex rejects its own governance docs' example filename
**File:** `Company-OS/.github/workflows/validate-naming.yml`
**Bug:** The regex requires the `[NUMBER]` segment to be digits-only: `^[A-Z]+-[A-Z-]+-[0-9]+" — ".+\.md$`. But Doc 03 and Doc 04's own canonical example for a Project Document is:
`PROJ-DOC-Website2026 — Project Plan.md` — where the "number" slot is `Website2026`, an alphanumeric project short-code, not a sequential integer.
**Impact:** Any contributor who follows the governance docs' own documented example for naming a project document will have their PR **fail CI** on a false positive. Confirmed by running the actual regex against the actual example filename from Doc 03/04 (see test output above) — no match.
**Fix:** Either (a) relax the regex's number segment to `[A-Za-z0-9]+` for `PROJ-DOC` codes specifically (project docs use short-codes, not sequential numbers, by design), or (b) if sequential numbers were actually intended for consistency, correct the example in Doc 03/04 instead and note that PROJ-DOC codes need a numeric sequence per project like everything else. Recommend (a) — the alphanumeric short-code is more readable for projects (`Website2026` vs `PROJ-DOC-047`), so fix the regex to match the intended convention rather than the other way round.

---

## 🟡 Medium Priority — real capability/documentation gaps

### M1. `validate-metadata.yml` doesn't actually check Confidentiality's allowed values
**Doc 10 §1 claims:** *"Confidentiality field is one of the 4 allowed values | 🟢 | `validate-metadata.yml` (extend)"* — listed as a working, built check.
**Reality:** The workflow (even after this session's fix) only checks that the `Confidentiality:` field is *present* — it never checks the value is one of `Public / Internal / Confidential / Restricted`. A document with `Confidentiality: banana` would currently pass.
**Fix:** Add a value-validation step after the presence check — extract the value after `Confidentiality:` and assert it's one of the 4 allowed strings, matching what Doc 10 already (over-)promises.

### M2. `validate-naming.yml`'s TYPE_FOLDER map only covers 8 of 12 Doc 02 types
**Bug:** The map checks folder placement for `POL, SOP, WI, TPL, REP, REC, KB, MEET` — but Doc 02 defines 12 types total. `STRAT` and `FORM` (both real types with worked examples — `STR-STRAT-003`, `QA-FORM-002`) have no folder-placement check at all.
**Root cause, one level deeper:** This isn't just a missing entry in the workflow — Doc 03's "Inside Every Department" folder structure itself only defines 8 subfolders (`Policies/, SOPs/, Work_Instructions/, Templates/, Reports/, Records/, Knowledge_Reference/, Meeting_Notes/`). There is genuinely **no defined folder** for a Strategy doc or a Form/Checklist to live in inside a department. So the workflow can't check something Doc 03 never specified.
**Fix:** Add `Strategy/` and `Forms/` (or fold FORM into an existing folder, e.g. Templates or Records, if that's the actual intent) to Doc 03's per-department structure, then extend `validate-naming.yml`'s `TYPE_FOLDER` map to match. `PROJ-DOC` is correctly left unchecked here since it lives in `02_PROJECTS/`, not a department folder — no action needed for that one.

### M3. Shallow git checkout undermines "stuck in Draft >30 days" detection
**Files:** `health-report.yml`, `dashboard-generate.yml`
**Bug:** Both use `git log -1 --format=%ct -- "$file"` to find a file's last-modified date, but neither workflow sets `fetch-depth: 0` on `actions/checkout@v4` — the default is a shallow clone (depth 1, single commit). On a shallow clone, `git log` for a specific file can't see its real history, so the computed "age" is unreliable and will typically undercount how stale a Draft really is.
**Fix:** Add `with: { fetch-depth: 0 }` to the checkout step in both workflows (small cost: slightly longer checkout, well worth it for correct staleness data).

### M4. Doc 07 §3 describes an `Ownership-Matrix.md` file and automation that don't exist
**Claim (Doc 07 §3):** A master file at `03_RESOURCES/Company_Master_Standards/Ownership-Matrix.md`, "Updated automatically whenever a document's metadata header changes (via the GitHub Action described in Doc 05 §4)."
**Reality:** The file doesn't exist anywhere in the repo, and Doc 05 §4 is just a generic GitHub-feature reference table — it never actually describes an ownership-matrix-updating Action. No workflow file implements this either.
**Fix:** Either build it (a small workflow, similar in shape to `dashboard-generate.yml`, that scans all metadata headers and regenerates the matrix) or downgrade Doc 07 §3's wording from "already automated" to "planned, not yet built" so the doc stops overpromising. Recommend building it — it's a near-copy of the dashboard workflow's file-scanning logic, low incremental cost.

---

## 🟢 Low Priority — pre-existing content gaps (not automation bugs, just unfinished)

### L1. Per-department `FAQ.md` files (Doc 07 §7) — 0 of 16 exist
Referenced as standard structure (`01_AREAS/[Dept]/Knowledge_Reference/FAQ.md`) but none have been seeded, even as empty templates. Lower priority since these are meant to grow organically — but a `.gitkeep`-equivalent seed (like what was done for `02_PROJECTS/`) would make the intended structure visible on a fresh clone.

### L2. `Company-Overview.md`, `Org-Chart.md`, `Welcome.md` are still empty placeholder stubs
These sit right next to `Brands.md` (which just got filled in this session) but still read `[Vision, Mission, Leadership, History — fill in.]` etc. Not a bug, but worth flagging since they're the first things a new hire or the AI assistant would open — and this session already established the pattern of "fill what's confirmable, flag what's tentative" for Brands.md. Same treatment could apply here once you're ready to share.

### L3. `CODEOWNERS` still has placeholder GitHub handles
`@ceo-office`, `@cfo`, `@sales-head`, etc. are template placeholders, not real usernames/teams — expected before go-live, just flagging so it's not forgotten in the "still open" list.

---

## Suggested Order of Work

| # | Item | Effort | Why this order | Status |
|---|---|---|---|---|
| 1 | H1 — fix `"In Review"` → `"Under Review"` | 1 min | Trivial, fixes a metric that's completely broken right now | ✅ Done |
| 2 | H3 — fix `validate-naming.yml` regex for PROJ-DOC codes | 10 min | Currently blocks real work — anyone naming a project doc per the docs' own example gets a false CI failure | ✅ Done |
| 3 | H2 — add `Next Review:` field to Doc 04 template (Option A) | 15 min | Unblocks the single most-cited broken metric across 4 governance docs | ✅ Done |
| 4 | M3 — add `fetch-depth: 0` to both checkouts | 5 min | Trivial, makes the staleness numbers from #3 actually trustworthy | ⬜ Open |
| 5 | M1 — add Confidentiality value validation to `validate-metadata.yml` | 15 min | Closes the gap between what Doc 10 claims and what's built | ⬜ Open |
| 6 | M2 — decide STRAT/FORM folder placement, update Doc 03 + workflow | 30 min | Needs a design decision first (new subfolders vs. fold into existing) — flag for your input | ⬜ Open — needs your decision |
| 7 | M4 — build or downsize the Ownership-Matrix promise | 30–60 min | Same pattern as the original dashboard gap; can reuse most of that workflow's logic | ⬜ Open |
| 8 | L1–L3 | Ongoing | Content work, not urgent, do alongside normal usage | ⬜ Open |

See `H1-H2-H3_Fix_Dashboard-NextReview-NamingRegex.md` for the full before/after diffs of the 3 completed fixes.
