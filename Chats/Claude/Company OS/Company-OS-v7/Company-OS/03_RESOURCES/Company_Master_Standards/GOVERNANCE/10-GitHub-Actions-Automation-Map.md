# 10 — GitHub Actions Automation Map (FINAL)

> **Purpose:** Every task that can realistically be automated in this Company OS, categorized by what actually implements it — a pure GitHub Action, a GitHub native setting, or an AI-assisted Action. This is the master list; the actual `.yml` workflow files implementing the 🟢 items are in `.github/workflows/` in the repository.
> **Owner:** Workspace Admin / CTO

---

## 1. Documentation Validation

| Task | Type | Workflow file |
|---|---|---|
| Required metadata fields present (Code, Title, Department, Type, Version, Lifecycle Status, Owner) | 🟢 | `validate-metadata.yml` (already built) |
| Filename matches `[DEPT]-[TYPE]-[NUMBER] — Title.md` pattern | 🟢 | `validate-naming.yml` |
| Document sits in the folder matching its declared Type (e.g. a `Type: SOP` file must be inside a `SOPs/` folder) | 🟢 | `validate-naming.yml` |
| Markdown syntax validation | 🟢 | `validate-naming.yml` (markdownlint step) |
| Confidentiality field is one of the 4 allowed values | 🟢 | `validate-metadata.yml` (extend) |

## 2. Navigation

| Task | Type | Workflow file |
|---|---|---|
| Broken internal links (`.md` links pointing to files that don't exist) | 🟢 | `check-links.yml` |
| Missing breadcrumb line at top of document | 🟢 | `validate-naming.yml` (extend) |
| Orphan document detection (not linked from any README/index) | 🟢 | `orphan-detection.yml` |
| Missing/invalid Table of Contents on long documents | 🟡 | needs AI to judge "is this long enough to need a TOC" |

## 3. Documentation Health

| Task | Type | Workflow file |
|---|---|---|
| Review-date tracking (flag documents past `Next Review`) | 🟢 | `health-report.yml` (scheduled weekly) |
| Missing Owner detection | 🟢 | `health-report.yml` |
| Stale document detection (no edits in 90+ days, still Draft) | 🟢 | `health-report.yml` |
| Duplicate-candidate detection (same/similar filename) | 🟢 | `health-report.yml` (filename-similarity check) |
| Duplicate-**meaning** detection (different filename, same content) | 🟡 | needs AI — filename matching alone won't catch this |
| Health report auto-generated and posted as a GitHub Issue | 🟢 | `health-report.yml` |
| Central `dashboard.md` consolidating all health metrics into one view | 🟢 | `dashboard-generate.yml` |

## 4. GitHub Governance

| Task | Type | How |
|---|---|---|
| Block direct pushes to `main` | 🔵 | Branch protection rule (repo Settings, not an Action) |
| Require CODEOWNER approval before merge | 🔵 | Branch protection + `/CODEOWNERS` file (already built) |
| Require at least 1 review on every PR | 🔵 | Branch protection rule |
| Label validation (PR must carry a Department + Type label) | 🟢 | `auto-label.yml` |
| Auto-apply Department label based on changed file path | 🟢 | `auto-label.yml` |

## 5. Migration (Research-Inbox → main)

| Task | Type | Workflow file |
|---|---|---|
| Scan Research-Inbox `dump/` for new items | 🟢 (trigger) | `classify-and-pr.yml` (in Research-Inbox repo) |
| Classify item — Department/Type/Code/Metadata, format full document | 🟢 | `classify-and-pr.yml` (calls Claude API inside the Action) |
| Duplicate/conflict detection against existing repo content | 🟡 | needs AI — not yet built into `classify-and-pr.yml` |
| Auto-create the migration Pull Request into Company-OS | 🟢 | `classify-and-pr.yml` |
| Post-migration validation (metadata complete, correct folder) | 🟢 | reuses `validate-metadata.yml` + `validate-naming.yml` on the new PR |
| Confirmation comment posted after PR is merged | 🟢 | `inbox-merge-confirmation.yml` (in Company-OS repo) |

## 6. Publishing

| Task | Type | Workflow file |
|---|---|---|
| Detect `publish: true` tag on merge to `main` | 🟢 | `publish-sync.yml` |
| Validate document is `Approved`/`Published` status before syncing out | 🟢 | `publish-sync.yml` |
| Sync tagged document to external Wiki/Notion | 🟢 (once target API/webhook is configured) | `publish-sync.yml` |

## 7. Task Management

| Task | Type | How |
|---|---|---|
| Issue → Project board auto-add | 🔵 | GitHub Projects "auto-add" workflow (built-in, configured in Project settings) |
| Project column auto-move on PR merge | 🔵 | GitHub Projects built-in workflow |
| Review reminder comments on old open PRs | 🟢 | `stale-check.yml` |
| Stale task/Issue detection & auto-comment | 🟢 | `stale-check.yml` (uses `actions/stale`) |

## 8. Documentation Lifecycle

| Task | Type | Workflow file |
|---|---|---|
| Review-due notification (Issue opened X days before `Next Review`) | 🟢 | `health-report.yml` |
| Deprecation reminder when a `Superseded By` field is set but old doc still `Published` | 🟢 | `health-report.yml` (extend) |
| Archive workflow trigger (move to `04_ARCHIVE` on status change) | 🟡 | file *move* + link updates need AI judgment, not just a script |

## 9. AI Integration Pattern (used by every 🟡 item above)

```
GitHub Event (push to Research-Inbox / scheduled run)
        ↓
   GitHub Action triggers
        ↓
   Calls Claude API (with the Company OS Classifier Skill's logic — Doc 04)
        ↓
   AI returns: classification + proposed file + flags
        ↓
   Action posts this as a PR / Issue comment
        ↓
   Human Approval (merge or reject)
```
**Rule, unchanged from Doc 05 §7:** AI never merges directly. Every AI-assisted Action step ends at a Pull Request or a comment — a human always makes the final call.

## 10. Reporting

| Task | Type | Workflow file |
|---|---|---|
| Weekly documentation health report (Issue with full stats) | 🟢 | `health-report.yml` |
| Broken-link report | 🟢 | `check-links.yml` |
| Review-due report | 🟢 | `health-report.yml` |
| Migration report (what moved from Inbox, when) | 🟢 | `classify-and-pr.yml` (PR body, in Research-Inbox repo) |

---

## Mental Model — Roles Stay Separate

```
GitHub Actions      = automation engine (the 🟢 items — deterministic checks & reports)
Claude/AI            = reasoning engine (the 🟡 items — classification, judgment calls)
GitHub Repository      = source of truth
GitHub Projects          = task management (built-in, no custom Action usually needed)
Dashboard                  = visibility (reads what Actions + metadata already produced)
```

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
| `.github/workflows/dashboard-generate.yml` | ✅ Built (consolidates health metrics into `dashboard.md`, scheduled weekly) |
| `.github/workflows/inbox-merge-confirmation.yml` | ✅ Built (posts cleanup-confirmation comment on PR merge) |
| `Research-Inbox/.github/workflows/classify-and-pr.yml` | ✅ Built (real migration engine — scans, classifies, opens PR) |
| `.github/workflows/inbox-classify.yml` | ⛔ Deprecated — superseded by `classify-and-pr.yml` above, see Audit item 2.2 |
| `.github/workflows/publish-sync.yml` | ⚠️ Scaffolded — needs your actual Wiki/Notion API details filled in |
