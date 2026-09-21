# Company OS — Consolidated Final Package (v6)
**Built:** 25 Aug 2026 | **Base version:** v5 (`Company-OS-Final-v5.zip`) + all pending Phase 1/2/4 and audit-issue fix drafts merged in.

> 📌 **For Claude / any AI assistant opening this later:** this single zip is the full, current state of the Company OS system. You do not need any of the older files (`Inital_Company_OS_v1_0`, `Company_OS_v2_0`, `Company_OS_with_github_repositoryv3_0`) — they were checked line-by-line against this version and everything in them is either duplicated here already or fully superseded. Read/improve directly inside this zip's folders; don't ask for the old zips again unless something below explicitly says it's missing.

---

## What's inside

| Folder | What it is | Source |
|---|---|---|
| `Company-OS/` | The actual working repo — 15 departments (`01_AREAS`), governance rulebooks 01–10 (`03_RESOURCES/Company_Master_Standards/GOVERNANCE`), 11 GitHub Actions workflows (incl. new `dashboard-generate.yml`), templates, archive, seeded `02_PROJECTS/` | v5 + this session's fixes |
| `Research-Inbox/` | Staging repo — drop raw notes in `dump/`, auto-classified and PR'd into `Company-OS/` | v5, README already correct |
| `Classifier-Skill/` | Standalone Claude Skill (`departments.json`, `document-types.json`) used for auto-classification | v5 — re-verified against the 12-type/18-department registries, exact match, no changes needed |
| `Research-OS-Skill/` | Separate 12-step research workflow skill, with Perplexity Space + ChatGPT Custom GPT instruction variants, now with a `Document-Type-Mapping.md` companion | v5 + new mapping file |
| `Audit-and-Tasks/` | Full audit report (now with resolved-status updates), the phase-wise task list/tracker (updated progress), the TickTick sync script, and every fix write-up (2.1–2.6, Phase1–4) applied this session | v5 + this session's tracker updates |

## What was checked and left OUT (nothing unique, safe to ignore)
- `Inital_Company_OS_v1_0.zip` — its 4 governance docs are the same content, now living as `01`–`04` inside `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/`.
- `Company_OS_with_github_repositoryv3_0.zip` — its standalone `10-GitHub-Actions-Automation-Map.md` is the same file already present as `GOVERNANCE/10-GitHub-Actions-Automation-Map.md`; the repo inside it is identical to v4's.
- `Company_OS_v2_0.zip`'s repo — identical to v4's `Company-OS/`; only its classifier skill was pulled forward (see table above).

## Change Log (fixes applied in this package, latest first)

**25 Aug 2026 — v5 → v6 merge (this session):**
- **[Fixed] Item 3 (Phase 1) / Issue 2.2** — `Company-OS/.github/workflows/inbox-classify.yml` was a dead scaffold (only `TODO`s, no working PR logic) sitting alongside the real `Research-Inbox/classify-and-pr.yml`. Replaced its content with a `[DEPRECATED]` no-op stub that clearly points to the real workflow, instead of deleting it outright.
- **[Fixed] Item 4 (Phase 1) / Issue 2.3** — `10-GitHub-Actions-Automation-Map.md` Section 5 and the "What's Actually Implemented" table referenced the now-deprecated `inbox-classify.yml` and were missing `inbox-merge-confirmation.yml` entirely. Both sections corrected, plus the Section 10 reporting row and a new Section 3 row for the dashboard workflow.
- **[Fixed] Phase 2, Item 3 / New Finding #5** — `validate-metadata.yml`'s `REQUIRED_FIELDS` array didn't check for `Confidentiality:`, even though it's required in Doc 04's body. One-line patch added.
- **[Fixed] Phase 4, Item 1 / New Finding #4** — `Brands.md` and `01-Department-Code-Registry.md` §C filled in with all 6 Nivy entity codes (ADV, NXT confirmed; ACAD, ALNC, JOBS, CARE tentative — **need your confirmation**, see below).
- **[Verified, no change] Phase 4, Item 2 / Issue 2.6** — Classifier skill JSON (`document-types.json`, `departments.json`) re-checked against the governance registries: exact match, 12/12 types, 18/18 departments, no drift.
- **[Fixed] Phase 4, Item 3** — New `Research-OS-Skill/Document-Type-Mapping.md` maps all 12 Research OS steps to Company-OS Document-Type codes; `SKILL.md` Step 12 updated to reference it.
- **[Fixed] Issue 2.4** — `Company-OS/02_PROJECTS/` was empty and untracked by Git (no `.gitkeep`-equivalent). Added `README.md` + a copyable `_TEMPLATE — Project Name Year/` scaffold (3 sub-folders, `.gitkeep`'d).
- **[Fixed] Issue 2.5** — No dashboard existed anywhere. Added `dashboard-generate.yml` (weekly + manual-trigger workflow computing all 7 Doc 07 §9 metrics, including the 2 nobody computed before — Awaiting Review, Broken Internal Links) and a seed `dashboard.md`.
- `Audit-and-Tasks/Company_OS_Full_Audit.md` and `Company_OS_Task_List.md` updated to reflect all of the above as resolved.

**24 Aug 2026 — v4 → v5:**
- **[Fixed] Issue 2.1** — `Research-Inbox/README.md` used to point at a `cleanup-after-merge.yml` file that doesn't exist, and said cleanup happens *after merge*. Corrected: cleanup actually happens automatically right when the PR is opened (`classify-and-pr.yml`'s last step) — the README now says so, and the dead file reference is removed. Full before/after write-up: `Audit-and-Tasks/2.1_Fix_cleanup-after-merge-reference.md`.

## Still open (needs a human, not a file fix)
- **Phase 1, Item 1** — GitHub Project board itself still needs to be created and configured in the GitHub UI (`02_PROJECTS/` folder is now seeded and ready, but the board is a one-time manual action).
- **Phase 3 (all 4 items)** — TickTick OAuth registration, first token save, first live sync, and daily cron scheduling — none of this can be done from inside the repo; needs your TickTick developer account.
- **Phase 4, Item 1 (partial)** — 4 of 6 Brands.md entries (Nivy Academy, Alliance, Jobs, Care Foundation) are tentative guesses from the name only — reply with corrections and I'll paste the confirmed versions in.
- **Phase 5, Items 2–3** — archiving v1–v4 as superseded, and running one real document through the full Draft→Review→Approved→Published lifecycle as an end-to-end test.
- Full detail + priority order: `Audit-and-Tasks/Company_OS_Full_Audit.md` §2, §5. Phase-wise plan + due dates: `Audit-and-Tasks/Company_OS_Task_List.md` (currently 10/17 tasks done, 59%).

## How to work from this package going forward
1. Any improvement/fix → edit the file directly inside the relevant folder above (e.g. `Company-OS/.github/workflows/...`).
2. Log what changed as a new entry under **Change Log** in this file, so the next session knows what's already done.
3. Tick off the matching line in `Audit-and-Tasks/Company_OS_Task_List.md` and update its progress table.
4. When ready to re-deploy: `Company-OS/` and `Research-Inbox/` are each meant to be their own separate GitHub repo — push them accordingly.
