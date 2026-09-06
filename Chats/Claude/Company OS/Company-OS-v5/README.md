# Company OS — Consolidated Final Package (v5)
**Built:** 24 Aug 2026 | **Base version:** v4 (`Company_OS_with_Research_OS_v4_0.zip`) — confirmed the most complete/authoritative version, so everything else was merged into it, not the other way round.

> 📌 **For Claude / any AI assistant opening this later:** this single zip is the full, current state of the Company OS system. You do not need any of the older files (`Inital_Company_OS_v1_0`, `Company_OS_v2_0`, `Company_OS_with_github_repositoryv3_0`) — they were checked line-by-line against this version and everything in them is either duplicated here already or fully superseded. Read/improve directly inside this zip's folders; don't ask for the old zips again unless something below explicitly says it's missing.

---

## What's inside

| Folder | What it is | Source |
|---|---|---|
| `Company-OS/` | The actual working repo — 15 departments (`01_AREAS`), governance rulebooks 01–10 (`03_RESOURCES/Company_Master_Standards/GOVERNANCE`), 10 GitHub Actions workflows, templates, archive | v4, unchanged |
| `Research-Inbox/` | Staging repo — drop raw notes in `dump/`, auto-classified and PR'd into `Company-OS/` | v4, **README.md fixed** (see Change Log below) |
| `Classifier-Skill/` | Standalone Claude Skill (`departments.json`, `document-types.json`) used for auto-classification | v2 — confirmed its 12 document types now match `Company-OS/.../02-Document-Type-Code-Registry.md` exactly (this was an open question in the audit; now resolved) |
| `Research-OS-Skill/` | Separate 12-step research workflow skill, with Perplexity Space + ChatGPT Custom GPT instruction variants | Research_OS_Skill.zip, unchanged |
| `Audit-and-Tasks/` | Full audit report, the phase-wise task list/tracker, the TickTick sync script, and the record of the 2.1 fix applied | Audit_v1_0.zip |

## What was checked and left OUT (nothing unique, safe to ignore)
- `Inital_Company_OS_v1_0.zip` — its 4 governance docs are the same content, now living as `01`–`04` inside `Company-OS/03_RESOURCES/Company_Master_Standards/GOVERNANCE/`.
- `Company_OS_with_github_repositoryv3_0.zip` — its standalone `10-GitHub-Actions-Automation-Map.md` is the same file already present as `GOVERNANCE/10-GitHub-Actions-Automation-Map.md`; the repo inside it is identical to v4's.
- `Company_OS_v2_0.zip`'s repo — identical to v4's `Company-OS/`; only its classifier skill was pulled forward (see table above).

## Change Log (fixes already applied in this package)
- **[Fixed] Issue 2.1** — `Research-Inbox/README.md` used to point at a `cleanup-after-merge.yml` file that doesn't exist, and said cleanup happens *after merge*. Corrected: cleanup actually happens automatically right when the PR is opened (`classify-and-pr.yml`'s last step) — the README now says so, and the dead file reference is removed. Full before/after write-up: `Audit-and-Tasks/2.1_Fix_cleanup-after-merge-reference.md`.

## Still open (see `Audit-and-Tasks/Company_OS_Full_Audit.md` §2 and §5 for full detail + priority order)
- 2.2 — duplicate/misplaced `inbox-classify.yml` scaffold still sitting in `Company-OS/.github/workflows/` (real one is in `Research-Inbox/`)
- 2.3 — `inbox-merge-confirmation.yml` still missing its own row in the Automation Map doc
- 2.4 — `02_PROJECTS/` is still empty, GitHub Project board not yet live
- 2.5 — dashboard is design-only, no generator script yet
- Phase-wise plan + due dates for all of the above: `Audit-and-Tasks/Company_OS_Task_List.md`

## How to work from this package going forward
1. Any improvement/fix → edit the file directly inside the relevant folder above (e.g. `Company-OS/.github/workflows/...`).
2. Log what changed as a new entry under **Change Log** in this file, so the next session knows what's already done.
3. Tick off the matching line in `Audit-and-Tasks/Company_OS_Task_List.md` and update its progress table.
4. When ready to re-deploy: `Company-OS/` and `Research-Inbox/` are each meant to be their own separate GitHub repo — push them accordingly.
