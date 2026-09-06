# Sales funnel n8n workflows — Phases 1–4

Four importable n8n workflow JSON files, each cumulative (every file contains all prior phases plus the new one):

- **sales-funnel-v1-capture-clean.json** — Phase 1 only (Capture & Clean).
- **sales-funnel-v2-enrich-score.json** — Phases 1+2 (adds Enrich & Score).
- **sales-funnel-v3-crm-sync.json** — Phases 1+2+3 (adds Odoo CRM Sync + Hot-lead alerting).
- **sales-funnel-v4-engage-convert.json** — Phases 1+2+3+4 (adds the full outreach sequence, reply handling, meeting booking, and proposal generation).

Import whichever one matches how far you want to test — v4 is the complete canvas built so far.

## How to import

1. Open your n8n instance → **Workflows** → **Add workflow** → menu (top right) → **Import from File**.
2. Select the JSON file.
3. n8n will show all nodes on the canvas, disconnected from credentials — you need to attach your own (see below).

## What's real vs. what's a placeholder

These are fully-formed, structurally correct n8n workflows — every node, connection, and piece of logic (dedupe query, email-verification call, Apollo enrichment, decision-maker loop, rule-based scoring, Hot/Warm/Cold/Disqualified routing) is wired end-to-end exactly as specified in the phased plan. What I could not do from here is:

- Run it against your actual n8n instance (I don't have access to it).
- Supply your real API keys, database connection, or scraper microservice URL.
- Verify it against live data.

So before it will actually run, you need to do the setup below.

## Required setup before running

| What | Where it's used | Action needed |
|---|---|---|
| `SCRAPER_SERVICE_URL` | "Call Scraper Service" node | Point this at your own Playwright/Crawlee scraping microservice. n8n's Code node cannot run a headless browser itself — this must be a small service you host separately and call over HTTP. |
| Postgres credential (`postgresLeadsDb`) | "Check Duplicate (Postgres)" node | Attach a Postgres credential pointing at a `leads` table with at least `domain` and `email` columns. |
| `REACHER_URL` | "Verify Email (Reacher)" node | Point at your self-hosted Reacher instance (`reacherhq/check-if-email-exists`), or swap for NeverBounce if you'd rather use that. |
| `APOLLO_API_KEY` | "Enrich Company (Apollo)" and "Find Decision Maker" nodes | Your Apollo API key. |
| `SCORING_ENGINE_URL` (optional) | "Score Lead" node | Currently rule-based (see below) — only needed if you want to swap in a self-hosted Ollama call for AI-assisted scoring later. |

Set these as n8n environment variables (Settings → Environment Variables) or as node-level credentials — either works, the nodes reference `$env.VARNAME` by default so environment variables are the quickest path.

## Scoring logic (Phase 2)

The "Score Lead" node currently uses simple rule-based scoring (matches the +2 point logic from the source doc: tier-1 country, employee band, decision-maker found, recent news, enrichment complete) rather than a live LLM call. This runs with zero extra setup. Swap the Code node for an HTTP Request to your Ollama endpoint later if you want AI-assisted scoring instead — the plan already flagged this as an optional upgrade, not a Phase 2 requirement.

## Testing before you rely on it

1. Trigger the webhook manually (Postman/curl) with a sample lead payload to confirm it reaches "Phase 1 Output - Ready for Enrichment."
2. Run "Enrich Company (Apollo)" manually on one real domain to confirm your API key works and field names match your Apollo response shape (Apollo's response schema can drift — check the fields the Code nodes expect against a real response before trusting it).
3. Confirm a test lead lands in the correct Hot/Warm/Cold/Disqualified output.

## Phase 3 setup (CRM sync)

| What | Where it's used | Action needed |
|---|---|---|
| `ODOO_URL`, `ODOO_DB`, `ODOO_UID`, `ODOO_API_KEY` | "Create/Update Odoo Lead" node | Your Odoo Community JSON-RPC endpoint and API user credentials. |
| Two custom fields in Odoo Studio | Same node | Create `x_studio_score_tier` and `x_studio_decision_makers` on `crm.lead` before running, or the write will fail on unknown fields. |
| `MATTERMOST_WEBHOOK_URL` | "Alert Team (Hot Lead)" node | Incoming webhook URL from Mattermost (or swap for a Slack webhook, or replace the HTTP Request node with n8n's native Email node if you'd rather not run either). |

All 4 score tiers (Hot/Warm/Cold/Disqualified) get written to Odoo — only Hot triggers a team alert.

## Phase 4 setup (Engage & Convert)

| What | Where it's used | Action needed |
|---|---|---|
| SMTP credential | "Send Follow-up Email", "Send Cal.com Booking Link", "Send Proposal Email" | Attach an SMTP credential (self-hosted Postal, or Gmail) to each `emailSend` node. |
| `OUTREACH_FROM_EMAIL` | Same nodes | The address outreach emails send from. |
| `AI_DRAFT_URL` (optional) | "Draft Email (AI or Template)" | Your self-hosted Ollama endpoint. If unset, the workflow automatically falls back to the plain-text templates in "Resolve Email Body" — nothing breaks either way. |
| `CALCOM_API_KEY`, `CALCOM_BOOKING_URL` | "Send Cal.com Booking Link" | Your Cal.com instance and booking-page URL. |
| Reply-capture webhook (not included) | "Wait For Reply Or Interval" | This Wait node resumes when a webhook at its resume URL is called with `{"reply_text": "..."}`. You still need a small mail-parsing piece (an IMAP-triggered n8n workflow, or a mail provider's inbound-parse webhook) that watches the outreach inbox and calls this resume URL when a reply arrives — that piece isn't built here since it depends on which mailbox/provider you use. |
| `GOTENBERG_URL` | "Generate Proposal PDF (Gotenberg)" | Your self-hosted Gotenberg instance. |
| Cal.com webhook registration | "Cal.com Booking Webhook" node | Copy this node's production webhook URL into your Cal.com event type's webhook settings. |

**Known simplifications in Phase 4, worth knowing before you rely on it:**
- The reply-capture webhook trigger itself isn't built (see table above) — the Wait node is ready to receive it, but you need to wire up how replies actually reach it for your mail setup.
- "Mark Meeting Scheduled (Odoo)" is a placeholder Set node, not a real Odoo write — reuse the JSON-RPC pattern from "Create/Update Odoo Lead" (Phase 3) with method `write` and the lead ID returned by "Match Lead by Email" to make this a real update.
- The proposal step fires directly after a meeting is booked, for simplicity — in practice you'd likely gate this on "meeting completed," not "meeting scheduled." Add a manual approval step or an Odoo-stage check here if you want that gate.
- Objection handling flags the lead for a human rather than auto-drafting a response, which was a deliberate choice — objection replies are usually worth a person's judgment rather than full automation.

## Next step

Phase 5 (Close & Retain — Won/Lost handling and retention automations) picks up from wherever a lead exits Phase 4: booked a meeting, went to proposal, was marked not-interested, or completed the sequence with no response.
