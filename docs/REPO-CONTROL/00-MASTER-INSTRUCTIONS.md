# Master Instructions

## START HERE — READ THIS FILE FIRST

This file is the single entry point for working on this repository.

When a user says **“Read this file and start work”**, do not wait for another detailed command. Follow this sequence:

1. Read this file completely.
2. Read every relevant file in `docs/REPO-CONTROL/`.
3. Follow `01-SOURCE-INDEX.md` to discover the repository's existing plans, instructions, tasks, progress, timelines, blockers, reminders, trackers, READMEs, issues, workflows, and related documents.
4. Treat existing repository evidence as authoritative; never invent status or completion.
5. Identify the highest-priority unfinished actionable work.
6. Execute the work when repository/tool permissions allow it.
7. Verify the result with appropriate tests, checks, or inspection.
8. Record what changed, evidence, status, blockers, and next action in the control files.
9. Update the repository README when the work changes the repository's usable state, structure, setup, or important progress.
10. Preserve old documents. Do not delete or silently replace existing plans; map them in the source index.
11. Commit completed changes with a clear commit message when write access is available.
12. Re-scan the control files and continue to the next unblocked priority when the user's instruction is to continue.

## OPERATING RULES

- **Minimal user command:** “Read `docs/REPO-CONTROL/00-MASTER-INSTRUCTIONS.md` and start work.” is sufficient to begin.
- **No guessing:** repository evidence > current canonical documents > tracked status > conversation memory.
- **No false completion:** an item is complete only when implementation, verification/evidence, status recording, and commit are done where applicable.
- **Preserve history:** do not delete old plans, trackers, research, or instructions unless explicitly instructed.
- **Cross-file discovery:** always scan for related documents before deciding what to do.
- **Self-updating:** keep README and control/tracking files synchronized with meaningful changes.
- **Resume-safe:** leave enough evidence for another ChatGPT session/agent to continue without asking the user to reconstruct context.
- **Human approval:** stop and mark `BLOCKED / NEEDS APPROVAL` when an action requires a decision, credential, payment, destructive change, or unavailable permission.

## CONTROL FILES

- `00-MASTER-INSTRUCTIONS.md` — single entry point and operating contract.
- `01-SOURCE-INDEX.md` — where all relevant instructions/plans/tasks/status/timeline/blockers/reminders live.
- `02-PLAN-TASK-TRACKER.md` — canonical mapping of plans to actionable tasks and their state.
- `03-PROGRESS-TIMELINE.md` — milestones, progress, dates, blockers, reminders, and next checkpoints.
- `04-EXECUTION-VERIFICATION.md` — execution log, tests, evidence, commits, failures, and verification.
- `05-CHANGELOG-RESUME.md` — compact cross-session handoff and latest changes.

## DEFINITION OF DONE

Implementation → verification → evidence → tracker/status update → README update when relevant → commit → resume state.

## IMPORTANT

This is an operational repository control system, not model training. “Learning” means preserving reusable repository knowledge, decisions, procedures, and evidence so future sessions can work consistently.
