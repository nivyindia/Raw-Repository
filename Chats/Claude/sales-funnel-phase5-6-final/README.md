# Sales funnel n8n workflows — Phases 1–6 (complete)

Importable n8n workflow JSON files. The first five are cumulative (each file contains
every prior phase plus the new one); Phase 6 is a **separate companion workflow** by
design (see the phased plan — it sweeps your whole account base on a schedule instead
of following one lead through a multi-day Wait, so it can't live in the same
per-execution canvas).

| File | Contents |
|---|---|
| `sales-funnel-v1-capture-clean.json` | Phase 1 only — Capture & Clean |
| `sales-funnel-v2-enrich-score.json` | Phases 1+2 — adds Enrich & Score |
| `sales-funnel-v3-crm-sync.json` | Phases 1+2+3 — adds Odoo CRM Sync + Hot-lead alerting |
| `sales-funnel-v4-engage-convert.json` | Phases 1+2+3+4 — adds outreach sequence, reply handling, meeting booking, proposal generation |
| `sales-funnel-v5-close-retain.json` | Phases 1+2+3+4+5 — adds Won/Lost handling, onboarding, retention |
| `sales-funnel-v6-nightly-refresh.json` | **Standalone companion workflow** — nightly account re-scoring sweep |
| `sales-funnel-vFULL-complete.json` | Same canvas as v5, final name/versionId — the one to actually deploy |
| `schema.sql` | Postgres tables required across all phases |
| `DEPLOYMENT.md` | Step-by-step deployment guide |

Import whichever `.json` matches how far you want to test — `vFULL-complete.json` is
the complete per-lead canvas, and `v6-nightly-refresh.json` is imported separately.

## How to import

1. Open your n8n instance → **Workflows** → **Add workflow** → menu (top right) → **Import from File**.
2. Select the JSON file.
3. n8n will show all nodes on the canvas, disconnected from credentials — attach your own (see `DEPLOYMENT.md`).
4. Import `sales-funnel-v6-nightly-refresh.json` as a **second, separate** workflow — do not merge it into the main canvas.

## What's real vs. what's a placeholder

These are fully-formed, structurally correct n8n workflows — every node, connection, and
piece of logic described in the phased plan is wired end-to-end. What I couldn't do from
here:

- Run any of it against your actual n8n/Odoo/Postgres instances (no access to them).
- Supply your real API keys, database connections, or the scraper microservice.
- Verify field-name assumptions against live API responses (Apollo's schema in
  particular can drift).
- Extract Phase 2's enrichment nodes into the reusable sub-workflow Phase 6 calls —
  that's a one-time manual step, see `DEPLOYMENT.md`.

So before any of this will actually run, work through `DEPLOYMENT.md`.

## Phase 5 — Close & Retain

Picks up from three exit points already present in Phase 4:

- **Send Proposal Email** → `Wait For Deal Outcome` (resume webhook) → `Is Deal Won?`
  - **Won** → convert the Odoo lead, build a 5-item onboarding checklist, insert it into
    Postgres, send a welcome email, compute a renewal date, log it, and alert the team.
  - **Lost** (manual outcome) → reason tagged from whatever the rep supplies.
- **Mark Not Interested / Unsubscribed** → auto-tagged `Not Interested` → Lost branch.
- **Sequence Complete - No Response** → auto-tagged `No Response` → Lost branch.

All Lost paths converge on `Normalize Lost Reason`, which maps free text onto the plan's
five standard buckets (Price / Competitor / No Budget / Timing / No Response), logs the
row to `lost_deals`, marks the Odoo lead inactive, and notifies the team.

**Known simplification:** the actual Won/Lost signal has to come from somewhere — the
`Wait For Deal Outcome` node exposes a resume webhook for this, but you still need to
decide what calls it (an Odoo automated action on stage change, or a simple internal
form). That piece isn't built here since it depends on how your reps work.

## Phase 6 — Nightly Intelligence Refresh (companion workflow)

Runs on its own schedule (2 AM daily by default) against every existing customer
account, one at a time:

1. Pull active accounts from Odoo.
2. Re-run enrichment + scoring via an `Execute Workflow` call into a sub-workflow you
   extract from Phase 2 (see `DEPLOYMENT.md` — this is a one-time setup step, not
   something an import can do automatically).
3. Compare the new score to the last-logged score in `account_score_history`.
4. If the score rose by at least `SCORE_RISE_THRESHOLD` points (default 10), create an
   urgent Odoo activity for the account owner and post a team alert.
5. Log the result either way, then move to the next account.

## Final merged export

`sales-funnel-vFULL-complete.json` is the same 81-node canvas as `v5`, exported with a
final name and version ID once the full end-to-end path (capture → close → retain) was
confirmed structurally sound. It's the file to actually deploy; the numbered `v1`–`v5`
files stay in the repo purely as rollback checkpoints per the plan's versioning strategy.

## Next step

Nothing further is planned in the phased build — Phases 1 through 6 (plus the final
merge) are all now present. From here it's setup and testing (`DEPLOYMENT.md`), not
more building.
