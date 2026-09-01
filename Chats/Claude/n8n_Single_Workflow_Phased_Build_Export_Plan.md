# Single n8n workflow — phased build & export plan

## Principle

Build the one combined canvas incrementally, section by section. After each phase, test it with real or dummy leads, then **export that version of the workflow as a versioned JSON file** before starting the next phase. If a later phase breaks something, you revert to the last good export instead of debugging a half-finished 100+ node canvas.

## Naming & versioning

Keep every export, in order, in git:

```
sales-funnel-v1-capture-clean.json
sales-funnel-v2-enrich-score.json
sales-funnel-v3-crm-sync.json
sales-funnel-v4-engage-convert.json
sales-funnel-v5-close-retain.json
sales-funnel-v6-nightly-refresh.json      (companion workflow, see Phase 6)
sales-funnel-vFULL-complete.json          (final merged export)
```

Each version file is the *entire* canvas as it existed at that point — not a diff. n8n's built-in "Download" on a workflow (or the CLI `n8n export:workflow`) produces this JSON directly.

---

## Phase 1 — Capture & clean (Week 1)

**Nodes to add:**
- Webhook trigger (form/API submission)
- Cron trigger (for scraped sources)
- Scraper Code/HTTP node (Google Search + Maps)
- Code node — dedupe/normalize
- HTTP Request — email verification (Reacher/NeverBounce)
- IF node — valid vs invalid branch

**Credentials needed:** email-verification API key; scraper target auth if any.

**Test before exporting:** push 5 dummy leads through the webhook; confirm duplicates are dropped and invalid emails are rejected before reaching the next stage.

**Export:** `sales-funnel-v1-capture-clean.json`

---

## Phase 2 — Enrich & score (Week 2)

**Nodes to add:**
- HTTP Request — company enrichment (Apollo)
- SplitInBatches + HTTP Request — loop over top 3–5 decision-makers
- Merge node — combine company + contact data
- AI/Code node — scoring logic
- Switch node — Hot / Warm / Cold / Disqualified

**Credentials needed:** Apollo API key; Ollama or Groq endpoint for scoring.

**Test:** run the 5 leads from Phase 1 through; confirm enrichment fields populate and each lead lands in the correct score bucket.

**Export:** `sales-funnel-v2-enrich-score.json`

---

## Phase 3 — CRM sync (Week 3)

**Nodes to add:**
- Odoo node — create/update `crm.lead`, writing stage + all enriched fields

**Credentials needed:** Odoo API user/key.

**Test:** confirm each score tier creates an Odoo lead with the right stage and custom fields populated.

**Export:** `sales-funnel-v3-crm-sync.json`

---

## Phase 4 — Engage & convert (Weeks 4–5)

**Nodes to add:**
- AI node — draft personalized first-touch email
- Send-email node
- Wait node (webhook-resume) — holds the lead here across the Day 0/3/7/14 sequence or until a reply arrives
- IF/Switch — reply classification (Interested / Not Interested / Objection / OOO)
- Cal.com webhook node — meeting booked → calendar event + reminder
- Gotenberg node — generate + send proposal PDF

**Credentials needed:** Gmail/SMTP; Cal.com API; Gotenberg endpoint.

**Test:** send yourself a test email, manually call the resume webhook to simulate a reply, confirm classification routes correctly, confirm a test meeting booking creates a calendar event, confirm a proposal PDF generates and sends.

**Export:** `sales-funnel-v4-engage-convert.json`

---

## Phase 5 — Close & retain (Week 6)

**Nodes to add:**
- IF node — Won vs Lost
- Won branch — create customer/project/onboarding tasks + welcome email
- Lost branch — write reason (Price/Competitor/No Budget/Timing/No Response) to a Postgres table
- Retention nodes — onboarding checklist, upsell/renewal reminder

**Test:** simulate one Won lead and one Lost lead; confirm the project/onboarding tasks appear for the Won case and the reason is logged for the Lost case.

**Export:** `sales-funnel-v5-close-retain.json`

---

## Phase 6 — Nightly intelligence refresh (Week 7, companion workflow)

This is the one piece that can't live in the same per-lead execution as everything above — it needs to sweep your whole existing account base on a schedule, not follow a single lead through a multi-day Wait. Build it as a **separate companion workflow** that reuses the Phase 2 enrichment logic via an Execute Workflow node.

**Test:** run manually against a handful of active accounts; confirm a rising score creates an urgent task and notification.

**Export:** `sales-funnel-v6-nightly-refresh.json`

---

## Final phase — merge & full export (Week 8)

- Run the complete canvas end-to-end against a handful of real leads, capture → close.
- Export the final combined workflow: `sales-funnel-vFULL-complete.json`
- Write a short README alongside the exports listing: import order, every credential the workflow needs, and any environment variables (Odoo URL, API base URLs) that must be set before re-importing on a new n8n instance.

---

## Rollback strategy

Every phase's export is kept. If a change in Phase N breaks something, revert to the Phase N-1 JSON, re-import it, and reapply the change more carefully rather than debugging forward in a half-broken canvas.

---

## Status table

| Phase | Deliverable | Export file | Status |
|---|---|---|---|
| 1 | Capture & clean | v1-capture-clean.json | Not started |
| 2 | Enrich & score | v2-enrich-score.json | Not started |
| 3 | CRM sync | v3-crm-sync.json | Not started |
| 4 | Engage & convert | v4-engage-convert.json | Not started |
| 5 | Close & retain | v5-close-retain.json | Not started |
| 6 | Nightly refresh (companion) | v6-nightly-refresh.json | Not started |
| Final | Full merged workflow | vFULL-complete.json | Not started |

Nothing has been built yet — start with Phase 1, since every later phase depends on clean leads reliably reaching the enrichment stage first.
