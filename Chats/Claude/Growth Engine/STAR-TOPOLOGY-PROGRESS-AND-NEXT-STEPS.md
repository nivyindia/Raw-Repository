# N8N Star-Topology Migration — Progress + Handoff

> **Iska use kaise karo:** Ye file naye Claude conversation me `N8N-Star-Topology-Integration-Plan.md` ke saath upload karo (aur `00_Automation.zip` bhi, kyunki source workflow files usi me hain), aur Claude ko bolo "is file ke hisab se aage ka kaam karo." Ye doc batata hai ab tak kya ban chuka hai, kis pattern se bana hai, aur agla step exactly kya hai.

---

## 1. Ab tak kya ban chuka hai (source-of-truth)

Reference: `N8N-Star-Topology-Integration-Plan.md` ke phase numbers (S0, S1, S2, S3, S4, S4b, S4c, S5a/b/c, S6a/b/c/d, S7a/b).

| Step | Module | Status | Note |
|---|---|---|---|
| S0.1–S0.3 | Spine (`funnel_events` table + taxonomy doc) | ✅ Done | `docs/S0-EVENT-TYPE-TAXONOMY.md` |
| S1.1–S1.4 | Hub-Intake workflow | ✅ Done | `phase-0-hub/hub-intake/workflow.json` |
| S2.1–S2.8 | Hub-Dispatcher workflow | ✅ Done + updated twice | see §3 below for exact Switch branches |
| S3.1 | 1.3 Website Lead Capture → `lead.captured` | ✅ Done | |
| S3.2 | 1.4 Inbound Form Qualification → `lead.qualified` | ✅ Done | |
| S3.3 | 1.5 Central CRM Sync — 4 IF nodes + 4 Execute Workflow nodes removed, single Report to Hub | ✅ Done | highest-risk step, already done |
| S3.4 | 1.1, 1.2 — confirmed no change needed | ✅ Done | |
| S3.5 | End-to-end test (Typebot → Hub → 1.4 → Hub → 1.5) | ⬜ **Not done** | needs a live n8n instance, can't be done from files alone |
| **S4.1** | **2.1 Multichannel Outreach → `lead.replied`** | ❌ **NOT DONE** | see §4, Phase A |
| **S4.2** | **2.3 Booking Sync → `lead.booked`** | ❌ **NOT DONE** | see §4, Phase A |
| **S4.3** | **2.4 Proposal Generation → `proposal.sent`** | ❌ **NOT DONE** | see §4, Phase A |
| S4.4 | 2.5 Contract E-Sign → `contract.signed` | ✅ Done | |
| S4.5 | 2.6 Invoice + Payment → `payment.received` | ✅ Done | |
| S4.6 | 2.7 Client Onboarding → `client.onboarded` | ✅ Done | trigger node already existed, only renamed/clarified |
| S4.7 (plan said 2.8) | **Redirected to 2.9**, not 2.8 | ✅ Done (with a deliberate deviation) | 2.8 (weekly report) has no renewal logic at all; 2.9 has all of it. See `2.8-delivery-reporting/README.md`'s "S4.7 note" section for the reasoning. |
| S4.8 | 2.9 Renewal Revenue Ops → `payment.failed` | ✅ Done (folded into the 2.9 work above) | 2.9 now reports THREE events: `renewal.due`, `renewal.overdue`, `payment.failed` |
| S4.9, S4.10 | End-to-end tests | ⬜ **Not done** | needs live n8n |
| S5a/b/c (Phase 4–5: reply-tracking, qualification, outreach/dialer) | 4.3.1, 4.3.2, 4.3.3, 5.1.1, 5.1.2, 4.1.3, 4.2.1, 4.2.2 | 🚫 **Blocked, not started** | **these modules don't exist as n8n workflow.json files anywhere in `00_Automation.zip` or `00_Marketing.zip`.** `00 Marketing`/`00 Sales Funnel` folders are strategy/SOP markdown docs, not built workflows. Confirmed by directory search — see §5. |
| S6a/b/c/d (Phase 6–7: health scoring, churn, NPS, advocacy, deliverability) | 6.1.1 through 7.2 | 🚫 **Blocked, not started** | same reason as S5 — none of these modules exist yet |
| S7a.1 | Grep audit for remaining direct Execute Workflow links | ⬜ Not done yet, but doable right now (no live instance needed) | see §4, Phase B |
| S7a.2, S7a.3 | Merged-file regen, Metabase dashboard | ⬜ Not done | dashboard needs live Metabase; file regen is doable |
| S7b | Full regression test, doc updates, "adding module #15" guide | ⬜ Not done | regression needs live n8n; doc updates are doable |

---

## 2. Established conventions — follow these exactly for consistency

Every "Report to Hub" node added so far uses this exact shape:

```json
{
  "parameters": {
    "workflowId": "REPLACE_WITH_0.0_HUB_INTAKE_WORKFLOW_ID",
    "workflowInputs": {
      "value": {
        "event_type": "<the event type string>",
        "client_id": "={{$json.id}}",
        "odoo_lead_id": "={{$json.odoo_lead_id}}",
        "source_module": "<module number as string, e.g. '2.6'>",
        "payload": "={{ { ...whatever fields the receiving spoke needs... } }}"
      }
    },
    "options": {}
  },
  "id": "report-to-hub-<module>-<short-event-name>",
  "name": "Report to Hub",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1.2,
  "position": [x, y],
  "notes": "explain what changed and why, in Hinglish, matching the module's README tone"
}
```

Rules followed throughout:
- **Always fires in parallel**, off the same Postgres node the old alert/email step branches from — never inserted sequentially in a way that blocks a time-sensitive customer-facing step (this matches the plan's explicit latency-tradeoff warning in §2).
- **If the Postgres `UPDATE ... WHERE ...` query didn't already have `RETURNING *`**, add it — the Report to Hub node needs `client_id`/`odoo_lead_id` from that row. Several pre-existing modules were missing this (was a latent bug even before this migration — e.g. 2.6's old `Execute Workflow - 2.7` node was silently reading a field its own upstream query never returned).
- **Never delete a module's own workflow ID requirement without replacing it** — the point of star topology is that spokes stop needing to know each other's IDs, only Hub-Intake's ID.
- **If a spoke already has an `executeWorkflowTrigger` entry node** (like 2.4 and 2.7 did), don't add a new one — just rename/clarify its `notes` field to say it's now Dispatcher-triggered, not directly called by the old upstream module.
- Every module's `README.md` gets an inline update: the ASCII flow diagram, the "Import Kaise Kare" numbered steps, and a `Known Limitations` bullet noting the Dispatcher branch isn't wired yet (until it actually is).
- Documentation language: Hinglish (Hindi in Latin script + English technical terms), matching the existing README style in the zip.

---

## 3. Hub-Dispatcher — current Switch node branches

`phase-0-hub/hub-dispatcher/workflow.json`, Switch node `Switch - Route by Event Type`, in this exact order (rules array order = connections array order, matters if editing):

1. `lead.qualified` → 2.1 Outreach
2. `lead.booked` → 2.4 Proposal Generation
3. `proposal.ready` → 2.5 Contract E-sign
4. `client.won` → 2.7 Onboarding **(see flag below)**
5. `contract.signed` → 2.6 Invoice + Payment *(added this session)*
6. `payment.received` → 2.7 Onboarding (payment.received) *(added this session, separate Execute Workflow node from #4)*
7. fallback/no-match → `Log Flagged Event` + Discuss alert

**⚠️ Open decision, not yet resolved:** branch #4 (`client.won` → 2.7) and branch #6 (`payment.received` → 2.7) **both** point at Client Onboarding. This was fine when 2.6/2.7 didn't exist yet (S2 was built assuming Won meant instant onboarding), but now that billing (2.6) sits between Won and Onboarded, onboarding should really only fire on `payment.received`. **Recommend removing branch #4 and its Execute Workflow node** before this Dispatcher goes live — full reasoning in `hub-dispatcher/README-S4b-DISPATCHER-UPDATE.md`. Whoever picks this up next should make this call explicitly, not silently.

**Not wired (correctly, for now):** `client.onboarded`, `renewal.due`, `renewal.overdue`, `payment.failed`, `lead.captured`, `lead.replied` (once S4.1 is done), `proposal.sent` (once S4.3 is done) — none of these have a built downstream consumer module yet. They fall to `Log Flagged Event`, which is expected behavior, not a bug, until a consumer exists.

---

## 4. Next phases — do these in order

### Phase A — finish S4 properly (this was skipped, do it first)

|Step|Module|Action|
|-|-|-|
|S4.1|`2.1-multichannel-outreach`|Already has `Execute Workflow Trigger` as entry (no change needed there). Add "Report to Hub" after `Mark Lead as Replied` → `event_type: lead.replied`. Keep the inline nurture-loop logic inline — only report the cross-module-relevant fact that a reply happened.|
|S4.2|`2.3-booking-sync`|Webhook-triggered by Cal.com, stays as-is. Add "Report to Hub" after `Postgres - Mark Booked` → `event_type: lead.booked`. Note: Dispatcher's `lead.booked` branch currently points at 2.4 (see §3, branch #2) — this is already correct, just wasn't being fed by anything until now.|
|S4.3|`2.4-proposal-generation`|Already has `Execute Workflow Trigger` as entry (`From Module 1.5 (status = Booked)`) — rename/clarify notes like was done for 2.7 in S4.6, since caller is now the Dispatcher via `lead.booked`, not 1.5 directly. Add "Report to Hub" after `Postgres - Mark Proposal Sent` → `event_type: proposal.sent`.|
|—|Hub-Dispatcher|Add a `lead.replied` Switch branch if/when a consumer exists (currently none — check S0.3's taxonomy before wiring). Add a `proposal.sent` branch — wait, check: `proposal.ready` already routes to 2.5, is `proposal.sent` a duplicate/different event? Confirm against taxonomy doc before wiring, don't assume.|

Apply the exact same conventions as §2 — RETURNING * check, parallel branch, README updates, taxonomy doc update.

### Phase B — S7a.1 grep audit (doable right now, no live instance needed)

Grep every `workflow.json` in the migrated set for `n8n-nodes-base.executeWorkflow` nodes whose `workflowId` placeholder or notes suggest they point at another **spoke** (not Hub-Intake or Hub-Dispatcher itself). Confirm the only remaining direct links are Hub-Dispatcher → spokes (expected) and nothing spoke → spoke. Document findings in a short report.

### Phase C — decide on Phase 4–7 (S5, S6)

These modules (4.1.3, 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.3, 5.1.1, 5.1.2, 6.1.1 through 7.2) **do not exist as n8n workflows** in either uploaded zip — confirmed via directory search (`find . -iname "*.json"` across both zips only turns up Phase 1 and Phase 2 modules). Two options, pick one before proceeding:

1. **Build these modules first** (separate, larger task — not integration, net-new workflow construction), *then* wire them per S5/S6.
2. **Treat Phase 1–2 as the complete v1 scope** and leave S5/S6 as documented-but-not-built future work — update the taxonomy doc and plan to say so explicitly rather than silently stalling.

### Phase D — testing + final docs (needs a live n8n instance)

S3.5, S4.9, S4.10, S6.13, S7.4 (end-to-end tests) and S7.3 (Metabase dashboard) can't be done from files alone — they need an actual running n8n + Postgres + Metabase stack. Flag these as "ready to test" once Phase A/B are done, rather than trying to simulate them.

---

## 5. Where things live (paths used this session, for re-orientation)

- Source zip: `00_Automation.zip` → extracts to `00 Automation/Growth Engline-n8n-workflow/growth-engine-automation/phase-1/` and `phase-2/` (two near-identical copies exist in the zip — `Growth Engline-n8n-workflow` and `n8n - growth-engine-individual workflows` — always edit from `Growth Engline-n8n-workflow`, it's the canonical/pretty-printed one, per the audit's own note about diverging copies).
- Hub workflows (already migrated in a prior batch) came packaged separately as `S0-S3-hub-and-phase1-migration.zip`, containing `phase-0-hub/hub-intake/`, `phase-0-hub/hub-dispatcher/`, and updated `phase-1/1.1`–`1.5`.
- This session's deliverables were shipped as separate zips per batch: `S4.4-contract-esign-hub-migration.zip`, `S4b-phase2-closeout-hub-migration.zip` (2.6, 2.7, 2.8, 2.9), `S4b-hub-dispatcher-wiring-update.zip`.
- `docs/S0-EVENT-TYPE-TAXONOMY.md` is the single source of truth for which event types exist, who reports them, who consumes them, and whether the Dispatcher branch is wired — **update it every single time** a Report to Hub node or Switch branch is added, or it goes stale immediately (this is literally the failure mode the original audit flagged).

---

## 6. Suggested opening prompt for the next Claude session

```
Attached: N8N-Star-Topology-Integration-Plan.md, 00_Automation.zip, and
STAR-TOPOLOGY-PROGRESS-AND-NEXT-STEPS.md (this file).

Is progress doc ke hisab se Phase A karo: S4.1, S4.2, S4.3 complete karo
(2.1, 2.3, 2.4), same conventions follow karke jo doc me likhe hain.
```
