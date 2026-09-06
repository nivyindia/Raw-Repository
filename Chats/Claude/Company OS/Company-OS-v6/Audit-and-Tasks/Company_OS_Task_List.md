# Company OS — Phase-Wise Implementation Plan & Progress Tracker

Format note: Har checklist line `ticktick_task_sync.py` directly padh sakti hai —
`due:` aur `priority:` fields optional hain, script auto-parse karegi.

---

## Phase 1 — Foundation Fixes (Week 1)
Goal: Broken/duplicate cheezein clean karo, task-management ka base ready karo.

- [ ] Set up GitHub Project board + move 02_PROJECTS design into live use | due: 2026-08-28 | priority: high (folder scaffold + README now seeded, see 02_PROJECTS/ — Project board itself is still a manual GitHub UI action)
- [x] Fix broken cleanup-after-merge.yml reference in Research-Inbox README | due: 2026-08-29 | priority: high
- [x] Remove/deprecate duplicate inbox-classify.yml scaffold from Company-OS repo | due: 2026-08-29 | priority: high
- [x] Add inbox-merge-confirmation.yml entry to 10-GitHub-Actions-Automation-Map.md | due: 2026-08-30 | priority: medium

**Progress: 3 / 4 done**

---

## Phase 2 — Visibility Layer (Week 2)
Goal: Dashboard aur health-check ko actual visible output mein badlo.

- [x] Build dashboard.md generator script (reads health-report.yml + orphan-detection.yml outputs) | due: 2026-09-05 | priority: high
- [x] Wire dashboard generator into weekly health-report.yml run | due: 2026-09-06 | priority: medium (shipped as its own scheduled workflow, `dashboard-generate.yml`, running after the other Monday jobs — see Doc 10 §3)
- [x] Verify validate-metadata.yml actually enforces Confidentiality field (per Doc 09 plan) | due: 2026-09-06 | priority: medium

**Progress: 3 / 3 done**

---

## Phase 3 — Task Management + TickTick Integration (Week 3)
Goal: Company OS ke tasks (GitHub Issues / audit items) automatically TickTick mein reminders ke saath aa jayein.

- [ ] Register TickTick app (developer.ticktick.com), get Client ID/Secret | due: 2026-09-10 | priority: high
- [ ] Run ticktick_task_sync.py once to complete OAuth login and save token | due: 2026-09-10 | priority: high
- [ ] Point sync script at this Task List file (or GitHub Issues) and do first live publish | due: 2026-09-11 | priority: high
- [ ] Schedule sync script to run daily (cron / GitHub Action) so new tasks auto-publish | due: 2026-09-13 | priority: medium

**Progress: 0 / 4 done**

---

## Phase 4 — Content & Data Completion (Week 4)
Goal: Placeholder/open items fill karo jo abhi tak sirf blueprint hain.

- [x] Fill Brands.md brand/division codes for all Nivy entities (Next, Academy, Alliance, Advisory, Jobs, Care Foundation) | due: 2026-09-18 | priority: medium (Advisory & Next confirmed; Academy/Alliance/Jobs/Care Foundation are tentative — need your confirm/correct, see Brands.md)
- [x] Re-upload and cross-check classifier skill JSON against 12-type registry | due: 2026-09-18 | priority: medium
- [x] Re-upload Research_OS_Skill.zip and map its 12-step naming to Company-OS Document-Type codes | due: 2026-09-19 | priority: low

**Progress: 3 / 3 done**

---

## Phase 5 — Consolidation (Week 5)
Goal: Ek clean, single "v5" final version jisme sab fixes merged hon.

- [x] Merge all Phase 1-4 fixes into a single Company-OS-v5 repo export | due: 2026-09-25 | priority: high
- [ ] Archive v1/v2/v3 as superseded (mark clearly, don't delete) | due: 2026-09-25 | priority: low
- [ ] Final end-to-end test: create 1 sample doc through full lifecycle (Draft -> Review -> Approved -> Published) and confirm all automations fire correctly | due: 2026-09-26 | priority: high

**Progress: 1 / 3 done**

---

## Overall Progress Tracker

| Phase | Tasks | Done | % |
|---|---|---|---|
| 1 — Foundation Fixes | 4 | 3 | 75% |
| 2 — Visibility Layer | 3 | 3 | 100% |
| 3 — TickTick Integration | 4 | 0 | 0% |
| 4 — Content Completion | 3 | 3 | 100% |
| 5 — Consolidation | 3 | 1 | 33% |
| **Total** | **17** | **10** | **59%** |

**Still open, needs a human:** GitHub Project board setup (Phase 1 item 1 — one-time UI action), TickTick OAuth + scheduling (all of Phase 3), archiving old versions (Phase 5 item 2), and end-to-end lifecycle test (Phase 5 item 3). Also: 4 of the 6 Brands.md entries (Academy, Alliance, Jobs, Care Foundation) are tentative guesses from the name only — confirm or correct them.

*Update karte raho — jab task complete ho, `[ ]` ko `[x]` karo, aur "Done" column manually ya script se update karo.*
