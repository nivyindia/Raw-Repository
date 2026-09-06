# Deployment guide — Sales Funnel n8n workflows (Phases 1–6)

This walks through getting `sales-funnel-vFULL-complete.json` and
`sales-funnel-v6-nightly-refresh.json` running on a real n8n instance, in order.
Do the steps in order — later steps assume earlier ones are done.

---

## 0. Prerequisites

Have these running and reachable from your n8n instance before you start:

| Service | Used for |
|---|---|
| n8n (self-hosted, v1.6x+) | Runs the workflows |
| Postgres | Dedupe check, lost-deal log, onboarding tasks, renewal reminders, score history |
| Odoo Community (or equivalent CRM with JSON-RPC) | `crm.lead` records, stage/lost tracking, activities |
| A scraper microservice you host (Playwright/Crawlee) | Phase 1 lead sourcing — n8n's Code node can't run a headless browser itself |
| Reacher (self-hosted) or NeverBounce | Email verification |
| Apollo.io account + API key | Company/contact enrichment |
| SMTP credential (self-hosted Postal, or Gmail) | All outbound email nodes |
| Cal.com instance | Meeting booking |
| Gotenberg (self-hosted) | Proposal PDF generation |
| Mattermost or Slack incoming webhook | Team alerts |
| Optional: Ollama endpoint | AI-assisted scoring / email drafting (both have non-AI fallbacks) |

If any of these aren't ready yet, you can still import and inspect the workflow — just
don't activate it until the relevant piece is in place, since the whole thing is one
connected canvas.

---

## 1. Create the database schema

Run `schema.sql` once against the Postgres database you'll point n8n's `postgresLeadsDb`
credential at:

```bash
psql "$DATABASE_URL" -f schema.sql
```

This creates `leads`, `lost_deals`, `onboarding_tasks`, `renewal_reminders`, and
`account_score_history`.

---

## 2. Set up Odoo custom fields

In Odoo Studio, on the `crm.lead` model, create two custom fields before importing
anything (Phase 3 writes to them):

- `x_studio_score_tier` (text)
- `x_studio_decision_makers` (text/JSON)

Confirm your Odoo instance exposes `action_set_won_rainbowman` via XML-RPC for marking
leads Won (Phase 5). If it doesn't on your version, swap the `Convert Lead to Customer
(Odoo)` node's method for a plain `write` call setting the Won `stage_id` instead.

---

## 3. Import the main workflow

1. n8n → **Workflows** → **Add workflow** → **Import from File** → select
   `sales-funnel-vFULL-complete.json`.
2. Leave it inactive for now — you still need to attach credentials.

---

## 4. Attach credentials

Every node using a credential (Postgres, SMTP) will show a red warning until you attach
one. Click each flagged node and select/create:

| Credential name (suggested) | Node(s) | Points at |
|---|---|---|
| `postgresLeadsDb` | Check Duplicate, Log Lost Deal, Insert Onboarding Tasks, Insert Renewal Reminder | Your Postgres instance from step 1 |
| SMTP credential | Send Follow-up Email, Send Cal.com Booking Link, Send Proposal Email, Send Welcome Email | Your mail sender |

---

## 5. Set environment variables

n8n → **Settings** → **Environment Variables**. All nodes reference `$env.VARNAME`, so
this is the fastest path (node-level credentials work too if you prefer).

| Variable | Used by | Notes |
|---|---|---|
| `SCRAPER_SERVICE_URL` | Call Scraper Service | Your Playwright/Crawlee microservice |
| `REACHER_URL` | Verify Email | Self-hosted Reacher, or swap node for NeverBounce |
| `APOLLO_API_KEY` | Enrich Company, Find Decision Maker | Apollo API key |
| `SCORING_ENGINE_URL` | Score Lead (optional) | Only needed if you swap in AI-assisted scoring |
| `ODOO_URL`, `ODOO_DB`, `ODOO_UID`, `ODOO_API_KEY` | All Odoo nodes (Phases 3, 5, 6) | Your Odoo JSON-RPC endpoint + API user |
| `MATTERMOST_WEBHOOK_URL` | All team-alert nodes | Mattermost/Slack incoming webhook |
| `OUTREACH_FROM_EMAIL` | All emailSend nodes | Sending address |
| `AI_DRAFT_URL` | Draft Email (optional) | Falls back to plain-text templates if unset |
| `CALCOM_API_KEY`, `CALCOM_BOOKING_URL` | Send Cal.com Booking Link | Your Cal.com instance |
| `GOTENBERG_URL` | Generate Proposal PDF | Self-hosted Gotenberg |
| `CONTRACT_LENGTH_MONTHS` | Schedule Renewal Reminder (Phase 5) | Defaults to 12 if unset |
| `SCORE_RISE_THRESHOLD` | Is Score Rising? (Phase 6) | Defaults to 10 if unset |

---

## 6. Register the two external webhooks

1. **Cal.com Booking Webhook** — open that node in n8n, copy its production webhook URL,
   paste it into your Cal.com event type's webhook settings.
2. **Deal Outcome webhook** (`Wait For Deal Outcome`, Phase 5) — this node's resume
   webhook needs something to call it with `{"outcome": "Won"}` or
   `{"outcome": "Lost", "lost_reason": "Price"}`. Wire an Odoo automated action on
   `crm.lead` stage change to call it, or build a small internal form — this piece is
   intentionally left open since it depends on how your reps work.
3. **Reply-capture webhook** (`Wait For Reply Or Interval`, Phase 4, carried over) —
   same as before: needs an IMAP-triggered workflow or your mail provider's
   inbound-parse webhook to call it when a reply lands.

---

## 7. Test end-to-end before activating

Work through each phase's original test from the build plan, in order, using the same
handful of dummy leads all the way through:

1. **Capture & Clean** — push 5 dummy leads through the webhook; confirm duplicates
   drop and invalid emails reject.
2. **Enrich & Score** — confirm enrichment fields populate and each lead lands in the
   right score bucket.
3. **CRM Sync** — confirm each tier creates an Odoo lead with the right stage/fields.
4. **Engage & Convert** — send yourself a test email, manually call the reply-resume
   webhook, confirm classification routes correctly, confirm a test Cal.com booking
   fires the webhook and creates a calendar event, confirm a proposal PDF generates.
5. **Close & Retain** — call the deal-outcome webhook once with `Won` and once with
   `Lost`; confirm the Won case creates onboarding tasks + welcome email + renewal row,
   and the Lost case logs a reason to `lost_deals` and marks the Odoo lead inactive.
6. **Nightly Refresh** (separate workflow) — run it manually against a handful of real
   accounts; confirm a rising score creates an Odoo activity and a team alert, and that
   `account_score_history` gets a new row either way.

---

## 8. Extract the Phase 2 sub-workflow for Phase 6

Phase 6's `Execute Workflow - Re-Enrich & Score` node needs a standalone workflow to
call. To create it:

1. Open `sales-funnel-vFULL-complete.json` in the n8n editor.
2. Select the node chain from `Enrich Company (Apollo)` through `Score Lead`
   (the Phase 2 enrichment + scoring logic).
3. Copy those nodes into a brand-new workflow, save it (e.g. name it
   `Enrichment & Scoring - Sub-workflow`), and note its workflow ID from the URL.
4. Open `sales-funnel-v6-nightly-refresh.json`, click `Execute Workflow - Re-Enrich &
   Score`, and replace the placeholder `REPLACE_WITH_ENRICHMENT_SUBWORKFLOW_ID` with the
   real ID (or just pick it from n8n's workflow list in that node's dropdown).

This is a one-time manual step — it can't be done from a JSON import alone since it
requires creating a new workflow inside your instance.

---

## 9. Go live

1. Activate `sales-funnel-vFULL-complete.json`.
2. Import and activate `sales-funnel-v6-nightly-refresh.json` as its own workflow.
3. Point your real lead-capture form/landing page at the production webhook URL.
4. Watch the first few real executions closely (n8n's **Executions** tab) before
   trusting it unattended.

---

## Rollback strategy

Every phase's export (`v1` through `v5`) stays in the repo. If a future change breaks
something, revert to the last-good numbered JSON, re-import it, and reapply the change
more carefully rather than debugging forward in a half-broken canvas — the same strategy
used to build this in the first place.

---

## Known simplifications, carried over and new

- The scraper microservice, reply-capture webhook wiring, and deal-outcome webhook
  wiring are all left as integration points rather than fully built, since each depends
  on infrastructure/process choices specific to your setup.
- `Mark Meeting Scheduled (Odoo)` (Phase 4) is still a placeholder Set node — reuse the
  JSON-RPC `write` pattern from `Create/Update Odoo Lead` to make it a real update.
- Objection handling (Phase 4) flags a human rather than auto-drafting a response —
  deliberate, not a gap.
- Phase 5's onboarding checklist is a fixed 5-item list — edit `Build Onboarding
  Checklist` to match your actual process.
- Phase 5's renewal reminder only computes and stores a date — actually sending the
  reminder as the date approaches needs a small scheduled query (an easy addition to
  Phase 6's nightly sweep, or its own small workflow) that isn't built here since it
  depends on your preferred lead time.
- Phase 6's `Execute Workflow` node needs the one-time manual sub-workflow extraction
  in step 8 above before it will run.
