# Fix — Phase 1: Foundation Fixes (items 2, 3, 4)

**Source:** `Company_OS_Task_List.md` → Phase 1
**Status:** Item 2 🟢 already fixed (verify only) · Items 3 & 4 🟡 draft ready · Item 1 ⚪ not a file fix (see note at bottom)

Phase 4 (items 1–3) is now fully drafted, so this continues at the next unfinished phase — Phase 1, which the task list still shows as 0/4 despite v5 already having partially fixed it.

---

## Item 2 — `cleanup-after-merge.yml` broken reference — ✅ already fixed, no action needed

The audit (v4) flagged `Research-Inbox/README.md` line ~37 for promising an automatic cleanup via a `cleanup-after-merge.yml` file that doesn't exist anywhere in the repo.

I checked the current README in this v5 upload: that filename isn't referenced anywhere anymore. It now correctly describes `classify-and-pr.yml` deleting the raw file from `dump/` at **PR-open time**, and separately references `inbox-merge-confirmation.yml` (Company-OS) for the post-merge confirmation comment. That's an accurate description of what the actual workflow files do.

**Action:** just tick item 2 done — nothing to paste.

---

## Item 3 — Duplicate scaffold `inbox-classify.yml` — still present, needs removing

Confirmed still there, still self-labeled `⚠️ SCAFFOLD — needs...` at the top, still has two literal `TODO` steps with no working classification or PR-creation logic. Meanwhile `Research-Inbox/.github/workflows/classify-and-pr.yml` is a complete, working implementation of the exact same job (classify → format → open PR → clean up dump/).

Keeping both is confusing (which one is "real" isn't obvious to a new contributor) and the scaffold could get accidentally triggered/relied on since it still sits in `.github/workflows/`.

**Fix:** delete `Company-OS/.github/workflows/inbox-classify.yml` entirely — `classify-and-pr.yml` in Research-Inbox is the one real implementation, there's nothing in the scaffold worth preserving (no working logic, just TODOs).

```
rm Company-OS/.github/workflows/inbox-classify.yml
```

If you'd rather keep a paper trail instead of deleting outright, the alternative is to leave the file but replace its entire content with a one-line deprecation stub pointing at the real workflow — say the word and I'll draft that version instead.

---

## Item 4 — Automation Map: fix Section 5 + add missing `inbox-merge-confirmation.yml` entry

Two problems in `10-GitHub-Actions-Automation-Map.md`, both stemming from the same root cause as Item 3:

1. **Section 5 (Migration)** still cites `inbox-classify.yml` as the workflow that scans, classifies, and opens the migration PR — but that's the non-functional scaffold. The real one is `classify-and-pr.yml`, and it lives in the **Research-Inbox** repo, not Company-OS.
2. **`inbox-merge-confirmation.yml`** isn't mentioned anywhere in the whole document, despite existing and being fully built.

### Replace Section 5 with:

```markdown
## 5. Migration (Research-Inbox → main)

| Task | Type | Workflow file |
|---|---|---|
| Scan Research-Inbox `dump/` for new items | 🟢 (trigger) | `classify-and-pr.yml` (in Research-Inbox repo) |
| Classify item — Department/Type/Code/Metadata, format full document | 🟢 | `classify-and-pr.yml` (calls Claude API inside the Action) |
| Duplicate/conflict detection against existing repo content | 🟡 | needs AI — not yet built into `classify-and-pr.yml` |
| Auto-create the migration Pull Request into Company-OS | 🟢 | `classify-and-pr.yml` |
| Post-migration validation (metadata complete, correct folder) | 🟢 | reuses `validate-metadata.yml` + `validate-naming.yml` on the new PR |
| Confirmation comment posted after PR is merged | 🟢 | `inbox-merge-confirmation.yml` |
```

### Replace the "What's Actually Implemented Right Now" table with:

```markdown
## What's Actually Implemented Right Now

| File | Status |
|---|---|
| `.github/workflows/validate-metadata.yml` | ✅ Built (previous step) |
| `.github/workflows/validate-naming.yml` | ✅ Built below |
| `.github/workflows/check-links.yml` | ✅ Built below |
| `.github/workflows/orphan-detection.yml` | ✅ Built below |
| `.github/workflows/auto-label.yml` | ✅ Built below |
| `.github/workflows/health-report.yml` | ✅ Built below (scheduled weekly) |
| `.github/workflows/stale-check.yml` | ✅ Built below |
| `.github/workflows/inbox-merge-confirmation.yml` | ✅ Built |
| `Research-Inbox/.github/workflows/classify-and-pr.yml` | ✅ Built (lives in the Research-Inbox repo, not this one) |
| `.github/workflows/publish-sync.yml` | ⚠️ Scaffolded — needs your actual Wiki/Notion API details filled in |
```

(The `inbox-classify.yml` row is dropped entirely — see Item 3.)

---

## Item 1 — GitHub Project board setup — not a file fix
This one's a one-time GitHub UI action (create the Project, enable "auto-add"/"auto-move" workflows in Project settings) rather than a repo file to edit — nothing in the zip to draft for it. Leaving it as-is on the task list for you to do directly in GitHub.

---

## Action for you
1. Delete `inbox-classify.yml` (or ask for the deprecation-stub version instead).
2. Paste the two replacement blocks into `10-GitHub-Actions-Automation-Map.md`.
3. Tick Phase 1 items 2, 3, 4. Item 1 stays open until you set up the board.
