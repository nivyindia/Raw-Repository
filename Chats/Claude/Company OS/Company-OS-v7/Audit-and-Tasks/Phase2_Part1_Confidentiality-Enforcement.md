# Fix — Phase 2, Item 3: Verify `validate-metadata.yml` actually enforces the Confidentiality field

**Source:** `Company_OS_Task_List.md` → Phase 2, item 3
**File affected (patch):** `Company-OS/.github/workflows/validate-metadata.yml`
**Related:** `Company_OS_Full_Audit.md` §4 New Finding #5 (this session) / §4 item #3 (now resolved by this check)
**Status:** 🟡 Draft ready — real gap confirmed, one-line patch, ready to paste

---

## Why this was flagged
`Company_OS_Full_Audit.md` §4 item 3 left this open: `validate-metadata.yml` is in the automation map, but whether the `Confidentiality` field was actually added to Doc 04 (vs. just planned in `09-Final-Change-Plan.md`) hadn't been confirmed against the doc body itself.

## What I checked (v5 zip, opened directly)

1. **Doc 04 body — field is actually there, not just planned:**
   - `04-Classification-Naming-Rulebook.md` line 49: `Confidentiality: [Public / Internal / Confidential / Restricted]` — present in the Required Metadata Header.
   - Line 112: a Quarterly Audit governance row already references confirming the Confidentiality tag.
   - So item #3's open question is answered: **the field is confirmed in Doc 04 itself**, not just in the change-plan doc.

2. **But the workflow that's supposed to enforce it doesn't check for it:**
   `validate-metadata.yml`'s required-fields list is:
   ```bash
   REQUIRED_FIELDS=("Code:" "Title:" "Department:" "Type:" "Version:" "Lifecycle Status:" "Owner")
   ```
   `Confidentiality:` is missing from this array. Every other Doc-04-required header field is checked except this one — so a PR can merge a document with no Confidentiality tag and the workflow will still pass it.

**Net effect:** the requirement exists in governance docs, but nothing in CI actually enforces it. That's the real gap — not a documentation-only issue.

## Fix — patch `validate-metadata.yml`

```diff
- REQUIRED_FIELDS=("Code:" "Title:" "Department:" "Type:" "Version:" "Lifecycle Status:" "Owner")
+ REQUIRED_FIELDS=("Code:" "Title:" "Department:" "Type:" "Version:" "Lifecycle Status:" "Confidentiality:" "Owner")
```

That's the only line that needs to change — the rest of the script (file loop, skip-list for README/Glossary/FAQ, error reporting) already works generically off this array, so no other edits are needed.

---

## Replacement Map

| This content | Goes in file | Folder |
|---|---|---|
| Diff above (one line) | `validate-metadata.yml` — replace the `REQUIRED_FIELDS=(...)` line only | `Company-OS/.github/workflows/` |
| This draft file itself | `Phase2_Part1_Confidentiality-Enforcement.md` (reference copy, optional to keep) | `Audit-and-Tasks/` |

## Follow-up note for `Company_OS_Full_Audit.md`
Since this also settles §4 item #3, reword that row from an open question to a resolved-with-a-gap finding, e.g.:
> ✅ Confirmed in Doc 04 body (not just planned) — ❌ but `validate-metadata.yml` didn't check for it until this fix. See New Finding #5.

## Action for you
1. Paste the one-line diff into `validate-metadata.yml`.
2. Tick Phase 2 item 3 in `Company_OS_Task_List.md`.
3. Optionally update §4 item #3's wording in `Company_OS_Full_Audit.md` per the note above.
