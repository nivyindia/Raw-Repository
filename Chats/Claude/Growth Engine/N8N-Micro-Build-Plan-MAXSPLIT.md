# N8N Full-Funnel Automation — MAXIMUM Split Micro-Build-Plan + Progress Tracker
**Base:** `N8N-Micro-Build-Plan.md` (48 sessions) → yahan har session ko uske andar ke individual node/step tak tod diya gaya hai.
**Maqsad:** Ek session (Claude chat) = ek node ya ek chota logical unit. Free-plan tokens me har sub-step easily fit ho jaye.

---

## Kaise Use Karein

1. **Ek chat = ek row is table me** (jaise `3.0.1.1`). Naya chat khologe to sirf:
   - Us row ka "Kya banega" column
   - Parent session ka context ek line me (e.g. "3.0.1 = 2.5 Contract e-sign patch, is sub-step se pehle 3.0.1.1–3.0.1.(n-1) already done hain")
   - Us module ka current relevant node/JSON section
2. Sub-step complete → turant neeche wale tracker me `[x]` mark karo.
3. Jab kisi parent session (e.g. `3.0.1`) ke saare sub-steps `[x]` ho jaayein, parent row bhi ✅ mark ho jaati hai — automatically pura module patch complete.
4. ⚠️ Input-needed tags same rahenge jaise original plan me the — us parent session ke saare sub-steps blocked rahenge jab tak input na mile.

Legend: ⬜ Not started · 🟡 In progress · ✅ Done · ⛔ Blocked (input pending)

---

## Phase 3.0 — Security & Data-Integrity Patches (38 sub-steps / 9 parent sessions)

### 3.0.1 — 2.5 Contract e-sign: accept_token (HMAC) generate + verify
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.1.1 | HMAC `accept_token` generate node (Code node) — jahan proposal-accept link banta hai |
| [ ] | 3.0.1.2 | Token ko accept-link URL me query-param ke roop me append karna |
| [ ] | 3.0.1.3 | "Proposal Accept Webhook" ke baad token-parse node (query-param se nikaalna) |
| [ ] | 3.0.1.4 | HMAC signature verify logic (recompute + compare, expiry check) |
| [ ] | 3.0.1.5 | IF node: valid → "Fetch Lead + Proposal" continue; invalid/expired → reject + alert branch |

### 3.0.2 — 2.6 Invoice/Payment: Payment-gateway signature verify
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.2.1 | Incoming webhook se raw payload + signature header extract karna |
| [ ] | 3.0.2.2 | Expected signature compute karna (HMAC, gateway secret se) |
| [ ] | 3.0.2.3 | IF node: computed vs received signature compare |
| [ ] | 3.0.2.4 | Fail branch → reject (401) + Odoo Discuss alert node |
| [ ] | 3.0.2.5 | Pass branch → existing payment-success flow me continue |

### 3.0.3 — 2.9 Renewal/Dunning: Failed-payment webhook signature verify (same pattern as 3.0.2)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.3.1 | Payload + signature header extract |
| [ ] | 3.0.3.2 | Expected signature compute |
| [ ] | 3.0.3.3 | IF node compare |
| [ ] | 3.0.3.4 | Fail branch → reject + alert |
| [ ] | 3.0.3.5 | Pass branch → dunning flow continue |

### 3.0.4 — 2.6 Invoice/Payment: payment-success → auto-trigger 2.7 Onboarding
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.4.1 | Payment-success node/branch identify karna existing workflow me |
| [ ] | 3.0.4.2 | "Execute Workflow" node add — target: 2.7 Onboarding |
| [ ] | 3.0.4.3 | Required fields map karna (lead_id/client_id, contract details) |
| [ ] | 3.0.4.4 | End-to-end pinned-data test |

### 3.0.5a — 2.4 Proposal: real Odoo `res.partner` lookup/create (pattern-setter)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.5a.1 | Odoo "Search res.partner" node (email/phone match) |
| [ ] | 3.0.5a.2 | IF node: found vs not-found |
| [ ] | 3.0.5a.3 | Not-found branch → Odoo "Create res.partner" node |
| [ ] | 3.0.5a.4 | Merge branches → single unified `partner_id` output |
| [ ] | 3.0.5a.5 | Old generic-contact fallback node remove/replace |
| [ ] | 3.0.5a.6 | Downstream nodes ko naye `partner_id` se rewire karna |

### 3.0.5b — 2.6 Invoice/Payment: same pattern reuse
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.5b.1 | 3.0.5a ka node-pattern copy karna |
| [ ] | 3.0.5b.2 | Invoice-module context ke hisaab se field-mapping adjust |
| [ ] | 3.0.5b.3 | Downstream invoice nodes ko `partner_id` se rewire |

### 3.0.5c — 2.7 Onboarding: same pattern reuse
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.5c.1 | 3.0.5a ka node-pattern copy karna |
| [ ] | 3.0.5c.2 | Onboarding-module context ke hisaab se field-mapping adjust |
| [ ] | 3.0.5c.3 | Downstream onboarding nodes ko `partner_id` se rewire |

### 3.0.6 — 2.5 Contract e-sign: renewal_date calculate + clients_master write
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.6.1 | Code node: `renewal_date = contract_start + contract_term_months` |
| [ ] | 3.0.6.2 | Postgres node: `renewal_date` ko `clients_master` me write |
| [ ] | 3.0.6.3 | `contract_term_months` field missing-case validate/default |

### 3.0.7 — 2.8 Delivery/Reporting: Metabase public link → signed-expiring link
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.0.7.1 | Purana public Metabase link node/reference remove |
| [ ] | 3.0.7.2 | Metabase signed-embedding token generate node (HMAC) |
| [ ] | 3.0.7.3 | Signed link par expiry param set karna |
| [ ] | 3.0.7.4 | Email/notification template ko naye signed link se update |

---

## Phase 3 — Outbound Lead Ingestion (34 sub-steps / 8 parent sessions)

### 3.1.1 — Google Maps scraper wiring
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.1.1.1 | Existing scraper ko callable sub-workflow banana (Execute Workflow Trigger node) |
| [ ] | 3.1.1.2 | Input-parameter node (search query/location) |
| [ ] | 3.1.1.3 | Output-normalize Code node → common schema (name, phone, email, website, source) |
| [ ] | 3.1.1.4 | Error-handling branch (0 results / API fail) |

### 3.1.2 — LinkedIn hiring-posts scraper wiring
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.1.2.1 | Sub-workflow wrap |
| [ ] | 3.1.2.2 | Input-param node |
| [ ] | 3.1.2.3 | Output-normalize Code node |
| [ ] | 3.1.2.4 | Error-handling branch |

### 3.1.3 — Digital Footprints scraper wiring
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.1.3.1 | Sub-workflow wrap |
| [ ] | 3.1.3.2 | Input-param node |
| [ ] | 3.1.3.3 | Output-normalize Code node |
| [ ] | 3.1.3.4 | Error-handling branch |

### 3.1.4 — Lead Generation Agent wiring
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.1.4.1 | Sub-workflow wrap |
| [ ] | 3.1.4.2 | Input-param node |
| [ ] | 3.1.4.3 | Output-normalize Code node |
| [ ] | 3.1.4.4 | Error-handling branch |

### 3.1.5 — Master Orchestrator
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.1.5.1 | Cron/Manual trigger node |
| [ ] | 3.1.5.2 | Execute Workflow node → 3.1.1 (Google Maps) |
| [ ] | 3.1.5.3 | Execute Workflow node → 3.1.2 (LinkedIn) |
| [ ] | 3.1.5.4 | Execute Workflow node → 3.1.3 (Digital Footprints) |
| [ ] | 3.1.5.5 | Execute Workflow node → 3.1.4 (Lead Gen Agent) |
| [ ] | 3.1.5.6 | Merge node — sab 4 outputs combine |

### 3.2.1 — Enrichment port (Airtable → Postgres)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.2.1.1 | Existing Airtable enrichment fields ko Postgres schema me map karna |
| [ ] | 3.2.1.2 | Airtable node ko Postgres node se replace (same operation) |
| [ ] | 3.2.1.3 | Field-by-field parity test |

### 3.2.2 — Dedup/merge gateway + `lead_source_channel` column
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.2.2.1 | Postgres lookup node (email/phone/domain match) |
| [ ] | 3.2.2.2 | Fuzzy-match Code node (name+domain similarity) |
| [ ] | 3.2.2.3 | IF node: duplicate → merge/update path; naya → insert path |
| [ ] | 3.2.2.4 | `lead_source_channel` column add (Postgres migration) |
| [ ] | 3.2.2.5 | `lead_source_channel` value set (originating scraper se) |

### 3.3.1 — Unified Lead Router
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 3.3.1.1 | Routing node — 3.2 ka output read karna |
| [ ] | 3.3.1.2 | Fields ko Module 1.4 Ollama scoring input-schema me map/rename |
| [ ] | 3.3.1.3 | Execute Workflow node → Module 1.4 scoring |
| [ ] | 3.3.1.4 | End-to-end single-lead trace test |

---

## Phase 4 — Missing Channels + Reply Tracking (35 sub-steps / 10 parent sessions)

### 4.1.1 — SMS booking-confirmation ⛔ (SMS gateway choice pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.1.1.1 | SMS gateway credential node configure |
| [ ] | 4.1.1.2 | 2.3 Booking Sync se "booking-confirmed" event par hook trigger |
| [ ] | 4.1.1.3 | SMS-send node (confirmation template) |
| [ ] | 4.1.1.4 | Sent-status Postgres log node |

### 4.1.2 — SMS reminders ⛔ (SMS gateway choice pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.1.2.1 | 24hr-before scheduler/cron check node |
| [ ] | 4.1.2.2 | 1hr-before scheduler/cron check node |
| [ ] | 4.1.2.3 | SMS-send node (reminder template) — dono trigger paths ke liye |
| [ ] | 4.1.2.4 | Reminder-sent status log |

### 4.1.3 — SMS re-engagement ⛔ (SMS gateway choice pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.1.3.1 | Inactive-lead filter trigger condition |
| [ ] | 4.1.3.2 | SMS-send node (re-engagement template) |
| [ ] | 4.1.3.3 | Status log + suppress-repeat flag |

### 4.2.1 — DNC filter + call-list prep ⛔ (dialer tool choice pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.2.1.1 | Postgres query node — `clients_master` se leads pull |
| [ ] | 4.2.1.2 | DNC-list lookup/filter node |
| [ ] | 4.2.1.3 | IF node — DNC matches exclude |
| [ ] | 4.2.1.4 | Call-list format/export node (CSV/Sheet) |

### 4.2.2 — Dialer trigger + outcome webhook ⛔ (dialer tool choice pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.2.2.1 | Dialer API trigger node (call-list push) |
| [ ] | 4.2.2.2 | Webhook node — call-outcome receive |
| [ ] | 4.2.2.3 | Outcome-payload parse Code node |
| [ ] | 4.2.2.4 | Postgres update node — `clients_master` call-outcome fields |

### 4.3.1 — Waha WhatsApp reply tracking
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.3.1.1 | Waha inbound webhook node |
| [ ] | 4.3.1.2 | Message-payload parse Code node |
| [ ] | 4.3.1.3 | Postgres update — `last_reply_channel` / `last_reply_at` |

### 4.3.2 — LinkedIn reply-check polling
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.3.2.1 | Cron polling trigger node |
| [ ] | 4.3.2.2 | LinkedIn inbox-check node/API call (workaround) |
| [ ] | 4.3.2.3 | New-replies parse Code node |
| [ ] | 4.3.2.4 | Postgres update — `last_reply_channel` / `last_reply_at` |

### 4.3.3 — Merge reply channels + nurture filter patch
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.3.3.1 | Merge node — email/WhatsApp/LinkedIn reply signals combine |
| [ ] | 4.3.3.2 | 2.2 Nurture me "already-replied" filter condition add |
| [ ] | 4.3.3.3 | Replied-lead par suppression test |

### 4.4.1 — Objection classification ⛔ (template library confirm pending)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.4.1.1 | Input node — incoming reply text |
| [ ] | 4.4.1.2 | Ollama classification node (price/timing/trust/competitor/not-interested) |
| [ ] | 4.4.1.3 | Postgres write — classified-objection field |

### 4.4.2 — Suggested-reply to Odoo Discuss ⛔ (depends on 4.4.1)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 4.4.2.1 | Template-library lookup node (classification → template match) |
| [ ] | 4.4.2.2 | Template populate Code/Set node (lead-specific fields) |
| [ ] | 4.4.2.3 | Odoo Discuss post node ("suggested reply" — human review gate, auto-send nahi) |

---

## Phase 5 — Qualification Depth + Deal Governance (19 sub-steps / 5 parent sessions)

### 5.1.1 — BANT/MEDDIC extraction
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 5.1.1.1 | Input node — call notes/transcript text |
| [ ] | 5.1.1.2 | Ollama extraction node — BANT fields |
| [ ] | 5.1.1.3 | Ollama extraction node — MEDDIC fields |
| [ ] | 5.1.1.4 | Output structure Code node (JSON schema) |

### 5.1.2 — Extracted fields → Odoo lead
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 5.1.2.1 | Fields ko Odoo lead custom-fields me map |
| [ ] | 5.1.2.2 | Odoo update-lead node |
| [ ] | 5.1.2.3 | Write-success validate + error branch |

### 5.2.1 — `rate_card` table + data load ⛔ (pricing data check pending — `Package_Pricing_AllServiceLines_v1.md` pehle dekho)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 5.2.1.1 | Postgres `CREATE TABLE rate_card` (service-line, tier, price-range, valid-from/to) |
| [ ] | 5.2.1.2 | `Package_Pricing_AllServiceLines_v1.md` ko structured rows me parse (Code node) |
| [ ] | 5.2.1.3 | Bulk-insert data-load node |
| [ ] | 5.2.1.4 | Row-count/spot-check validate |

### 5.3.1 — Proposal pricing guardrail patch (depends on 5.2.1)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 5.3.1.1 | 2.4 Proposal se free-text pricing input node remove |
| [ ] | 5.3.1.2 | `rate_card` lookup node (service-line + tier) |
| [ ] | 5.3.1.3 | Ollama "adjust within X%" assist node |
| [ ] | 5.3.1.4 | IF node — band se bahar price → review-flag |

### 5.4.1 — Deal Desk approval-gate
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 5.4.1.1 | Threshold-check IF node (discount%/deal-size) |
| [ ] | 5.4.1.2 | Odoo Discuss/email approval-request node |
| [ ] | 5.4.1.3 | Wait-for-approval node (webhook/polling) |
| [ ] | 5.4.1.4 | IF node — approved → continue; rejected → notify+stop |

---

## Phase 6 — Post-Sale Growth Loop (40 sub-steps / 13 parent sessions)

### 6.1.1 — Account health-snapshot rollup
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.1.1.1 | Cron trigger node |
| [ ] | 6.1.1.2 | Usage-data pull node |
| [ ] | 6.1.1.3 | Tickets-data pull node |
| [ ] | 6.1.1.4 | Last-contact data pull node |
| [ ] | 6.1.1.5 | Merge + health-score compute Code node |
| [ ] | 6.1.1.6 | Metabase/Odoo write node |

### 6.2.1 — Adoption checklist auto-create
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.2.1.1 | Trigger: onboarding-complete + X-din Wait node |
| [ ] | 6.2.1.2 | Odoo Project task-create node (checklist items) |

### 6.2.2 — Milestone-missed alert
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.2.2.1 | Scheduled check node (milestone due-date vs status) |
| [ ] | 6.2.2.2 | IF node — missed → alert branch |
| [ ] | 6.2.2.3 | Odoo Discuss/email alert node |

### 6.3.1 — Support/ticketing wiring
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.3.1.1 | Slack trigger node (new ticket message) |
| [ ] | 6.3.1.2 | Linear ticket-create node |
| [ ] | 6.3.1.3 | Postgres update — `support_ticket_count` increment |

### 6.4.1 — Upsell/cross-sell trigger
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.4.1.1 | Rule-engine node (usage/tenure/adoption thresholds) |
| [ ] | 6.4.1.2 | Ollama suggestion-generation node |
| [ ] | 6.4.1.3 | Odoo activity-create node |

### 6.5.1 — Churn win-back sequence
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.5.1.1 | Trigger — 2.9 "Churn Risk" tag consume |
| [ ] | 6.5.1.2 | Touch-1 email/WhatsApp send node |
| [ ] | 6.5.1.3 | Wait node + Touch-2 send node |
| [ ] | 6.5.1.4 | Wait node + Touch-3 send node |

### 6.5.2 — No-response escalation
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.5.2.1 | IF node — 3-touch ke baad bhi no-reply |
| [ ] | 6.5.2.2 | Sales-rep escalation notify node |

### 6.6.1 — NPS survey trigger + table
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.6.1.1 | Postgres `CREATE TABLE nps_responses` |
| [ ] | 6.6.1.2 | Trigger node — post-delivery/quarterly schedule |
| [ ] | 6.6.1.3 | Survey-send node (email/form link) |
| [ ] | 6.6.1.4 | Response-webhook capture → `nps_responses` write |

### 6.6.2 — Detractor alert
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.6.2.1 | IF node — NPS score threshold se neeche |
| [ ] | 6.6.2.2 | Immediate alert node (Odoo Discuss/email) |

### 6.7.1 — Case-study auto-request
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.7.1.1 | IF node — High-NPS trigger condition |
| [ ] | 6.7.1.2 | Draft-template populate Code/Set node |
| [ ] | 6.7.1.3 | Email-send node (human-review-gate flag included) |

### 6.8.1 — Referral-link + table
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.8.1.1 | Postgres `CREATE TABLE referrals` |
| [ ] | 6.8.1.2 | Unique-link generate Code node (per client) |
| [ ] | 6.8.1.3 | Link + client_id `referrals` table me write |

### 6.8.2 — Reward-trigger on converted referral
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.8.2.1 | Referral-conversion event-detect trigger node |
| [ ] | 6.8.2.2 | Reward-calculation Code node |
| [ ] | 6.8.2.3 | Reward-issue notify node |

### 6.9.1 — Advocacy loop tag + ask-list
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 6.9.1.1 | Tagging node (advocacy-eligible criteria) |
| [ ] | 6.9.1.2 | Curated ask-list compile node (manual-trigger + tracking table) |

---

## Phase 7 — Cleanup (9 sub-steps / 3 parent sessions)

### 7.1.1 — Deliverability/domain health monitor
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 7.1.1.1 | Daily cron trigger node |
| [ ] | 7.1.1.2 | SPF/DKIM check node (DNS lookup) |
| [ ] | 7.1.1.3 | Bounce-rate check node (ESP data se) |
| [ ] | 7.1.1.4 | IF node — threshold breach → alert |

### 7.2.1 — List auto-refresh
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 7.2.1.1 | Cron trigger node |
| [ ] | 7.2.1.2 | Postgres query node — `clients_master` segment-rules re-filter |
| [ ] | 7.2.1.3 | Segmented list update/replace node |

### 7.3.1 — LinkedIn automation safety review (audit/decision, code nahi)
| Done | Step | Kya Banega |
|---|---|---|
| [ ] | 7.3.1.1 | Current LinkedIn nodes/rate-limits ToS ke against audit |
| [ ] | 7.3.1.2 | Risk-level + recommendation document (decision output) |

---

## Open Inputs Needed (inke bina related sub-steps sab blocked rahenge)
1. SMS gateway — Twilio ya India-specific provider? (blocks sab 4.1.x sub-steps)
2. Dialer/VoiceAgent tool — decide ho chuka hai ya template ka default provider? (blocks sab 4.2.x sub-steps)
3. Objection→response template library — ready hai ya banani hai? (blocks sab 4.4.x sub-steps)
4. Rate-card/pricing data — `Package_Pricing_AllServiceLines_v1.md` pehle check karo, agar kaafi na ho to additional data do (blocks 5.2.1.x → 5.3.1.x)
5. Airtable→Postgres port ke liye koi objection? (blocks 3.2.1.x agar haan)

---

## Totals
| Phase | Parent Sessions | Sub-steps |
|---|---|---|
| 3.0 — Security & Data-Integrity | 9 | 38 |
| 3 — Outbound Lead Ingestion | 8 | 34 |
| 4 — Channels + Reply Tracking | 10 | 35 |
| 5 — Qualification + Deal Governance | 5 | 19 |
| 6 — Post-Sale Growth Loop | 13 | 40 |
| 7 — Cleanup | 3 | 9 |
| **Total** | **48** | **175** |

**0 sub-steps done · sub-steps blocked on input: 4.1.x(11) + 4.2.x(8) + 4.4.x(6) + 5.2.1.x/5.3.1.x(8) = 33 blocked · 142 ready to start**

## Build Order (same as original)
```
Phase 3.0 (38) → Phase 3 (34) → Phase 4 (35) → Phase 5 (19) → Phase 6 (40) → Phase 7 (9, kabhi bhi 3.1 ke baad)
```
