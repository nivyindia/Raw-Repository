# N8N Full-Funnel Automation — Micro Build Plan (Free-Plan Friendly)
**Base:** `N8N-Full-Funnel-Automation-Build-Plan.md`
**Maqsad:** Har Phase/Module ko itna chota session bana dena ki Claude free plan (limited tokens/session) me bhi ek session = ek complete deliverable (chota workflow.json patch ya chota naya node-set + README update) ban sake.

---

## Kaise Use Karein (Free Plan Ke Liye)

1. **Ek session = ek row is table me.** Naya Claude chat khologe to sirf us **ek row** ka context do — poora build plan paste mat karo, sirf:
   - Us row ka "Kya banega" column
   - Jis existing module (`X.Y`) ko patch/touch karna hai uska current `workflow.json` (agar chota hai) ya sirf uska relevant node-section
   - `PROGRESS-TRACKER.md` me se sirf uss ek line ka status
2. Session complete hone par turant `PROGRESS-TRACKER.md` me us row ko `✅ Done` mark karo (naya chat khulte hi Claude ko batao "ye already done hai, is par mat kaam karo").
3. **S = Small session** (1 node-group ya 1 patch, ~1 chat me aasani se ban jayega). **M = Medium session** (2-3 nodes + testing logic, agar free-plan tokens tight ho to isko bhi 2 halves me todo — table me note likha hai kaha todna hai).
4. Jahan **⚠️ Input needed** likha hai, wahan session shuru karne se pehle wo input do — nahi to session ka half token wahi discussion me chala jayega.

---

## Phase 3.0 — Security & Data-Integrity Patches (existing 8 modules ke patches, naya module nahi)

| Session ID | Module Patch Hoga | Kya Banega (1 session ka scope) | Size |
|---|---|---|---|
| 3.0.1 | 2.5 Contract e-sign | `accept_token` (signed HMAC) generate node + verify node accept-link par | S |
| 3.0.2 | 2.6 Invoice/Payment | Payment-gateway signature verify node (fail → reject+alert) | S |
| 3.0.3 | 2.9 Renewal/Dunning | Failed-payment webhook signature verify node (same pattern as 3.0.2) | S |
| 3.0.4 | 2.6 Invoice/Payment | "Execute Workflow" node: payment-success → auto-trigger 2.7 Onboarding | S |
| 3.0.5a | 2.4 Proposal | Real Odoo `res.partner` lookup/create node (generic-contact fallback hatana) | S |
| 3.0.5b | 2.6 Invoice/Payment | Same `res.partner` lookup/create node (reuse 3.0.5a ka pattern) | S |
| 3.0.5c | 2.7 Onboarding | Same `res.partner` lookup/create node (reuse 3.0.5a ka pattern) | S |
| 3.0.6 | 2.5 Contract e-sign | Contract-sign → `renewal_date = contract_start + contract_term_months` calculate + `clients_master` write | S |
| 3.0.7 | 2.8 Delivery/Reporting | Metabase public-link ko authenticated/signed-expiring link se replace | S |

*(3.0.5 ko teen chote sessions me tod diya hai kyunki same pattern 3 alag modules me repeat hota hai — pehla session (3.0.5a) pattern set karega, baaki do sirf reuse honge.)*

---

## Phase 3 — Outbound Lead Ingestion (Gap 1)

| Session ID | Naya/Patch | Kya Banega | Size |
|---|---|---|---|
| 3.1.1 | Naya | Google Maps scraper ko sub-workflow ke roop me wire karna + output ko common schema me normalize | M |
| 3.1.2 | Naya | LinkedIn hiring-posts scraper ko sub-workflow wire + normalize | M |
| 3.1.3 | Naya | Digital Footprints scraper ko sub-workflow wire + normalize | M |
| 3.1.4 | Naya | Lead Generation Agent ko sub-workflow wire + normalize | M |
| 3.1.5 | Naya | Master Orchestrator: cron/manual trigger → 3.1.1→3.1.4 ko sequence me call + merge | S |
| 3.2.1 | Naya | Enrichment logic port (Airtable pattern → Postgres `clients_master`) | M |
| 3.2.2 | Naya | Fuzzy-match dedup/merge gateway (email/phone/domain) + naya column `lead_source_channel` add | M |
| 3.3.1 | Patch | Unified Lead Router: 3.2 output → Module 1.4 ke Ollama scoring path me feed | S |

---

## Phase 4 — Missing Channels + Reply Tracking (Gap 2 + 3)

| Session ID | Naya/Patch | Kya Banega | Size |
|---|---|---|---|
| 4.1.1 | Naya | SMS gateway setup + booking-confirmation trigger (2.3 Booking Sync se hook) | S |
| 4.1.2 | Naya | SMS reminder triggers (24hr aur 1hr before) | S |
| 4.1.3 | Naya | SMS re-engagement trigger | S |
| 4.2.1 | Naya | DNC-list filter + call-list prep from `clients_master` | S |
| 4.2.2 | Naya | Dialer trigger + call-outcome webhook + `clients_master` update | M |
| 4.3.1 | Naya | Waha WhatsApp inbound webhook → `last_reply_channel`/`last_reply_at` update | S |
| 4.3.2 | Naya | LinkedIn reply-check (polling, API-restricted workaround) | M |
| 4.3.3 | Patch | 2.1 email reply-tracking ko merge + 2.2 Nurture me "already-replied" filter | S |
| 4.4.1 | Naya | Reply-text classification (Ollama: price/timing/trust/competitor/not-interested) | S |
| 4.4.2 | Naya | Matching response-template suggest → Odoo Discuss me "suggested reply" (auto-send nahi) | S |

**⚠️ Input needed before 4.4.x:** Objection→response template library ready hai ya banani hai? (Note: `Nivy-Next-Sales_and_marketing_Research` folder me `Cold_Email_Sequence_v1.md` aur `LinkedIn_Outreach_Sequence_v1.md` already hain — inme se kuch objection-handling angles reuse ho sakte hain, poora nahi.)

**⚠️ Input needed before 4.1.x:** SMS gateway decide — Twilio ya India-specific provider?
**⚠️ Input needed before 4.2.x:** Dialer/VoiceAgent tool decide hai ya standalone template ka provider hi use karna hai?

---

## Phase 5 — Qualification Depth + Deal Governance (Gap 4 + 7 + pricing part of Gap 6)

| Session ID | Naya/Patch | Kya Banega | Size |
|---|---|---|---|
| 5.1.1 | Naya | BANT/MEDDIC extraction from notes/transcript (Ollama) | M |
| 5.1.2 | Naya | Extracted fields ko Odoo lead par structured fields me likhna | S |
| 5.2.1 | Naya | `rate_card` Postgres table (service-line, tier, price-range, valid-from/to) + data load | S |
| 5.3.1 | Patch | 2.4 Proposal Generation: free-text pricing hatakar rate-card lookup + "adjust within X%" AI-assist | M |
| 5.4.1 | Naya | Deal Desk approval-gate: threshold-cross → Odoo Discuss/email approval-request | M |

**⚠️ Input needed before 5.2.1:** Actual pricing/rate-card data. **Note:** `Nivy-Next-Sales_and_marketing_Research/research/04-Positioning-Offers/Package_Pricing_AllServiceLines_v1.md` aur `Competitor_and_Market_Pricing_Benchmark_v1.md` already uploaded folder me maujood hain — 5.2.1 shuru karne se pehle ye dono check kar lena, shayad rate-card ka base data yahin se mil jaye.

---

## Phase 6 — Post-Sale Growth Loop (Gap 5)

| Session ID | Naya/Patch | Kya Banega | Size |
|---|---|---|---|
| 6.1.1 | Naya | Account health-snapshot rollup (usage/tickets/last-contact) cron → Metabase/Odoo | M |
| 6.2.1 | Naya | Onboarding-complete + X din → adoption checklist auto-create Odoo Project me | S |
| 6.2.2 | Naya | Milestone-missed alert | S |
| 6.3.1 | Naya | Slack+Linear ticket wiring → `clients_master.support_ticket_count` update | M |
| 6.4.1 | Naya | Upsell/cross-sell rule engine (usage/tenure/adoption) + Ollama suggestion → Odoo activity | M |
| 6.5.1 | Naya | Churn win-back sequence (3-touch email/WhatsApp), 2.9 "Churn Risk" tag consume | M |
| 6.5.2 | Naya | No-response → sales rep escalation | S |
| 6.6.1 | Naya | NPS/Feedback survey trigger (post-delivery/quarterly) + `nps_responses` table | S |
| 6.6.2 | Naya | Detractor turant-alert | S |
| 6.7.1 | Naya | High-NPS → case-study auto-request email + draft template populate (human review gate) | S |
| 6.8.1 | Naya | Referral-link generation per client + `referrals` table | S |
| 6.8.2 | Naya | Reward-trigger on converted referral | S |
| 6.9.1 | Naya | Advocacy tag + curated ask-list (mostly manual-trigger + tracking) | S |

---

## Phase 7 — Cleanup Items

| Session ID | Naya/Patch | Kya Banega | Size |
|---|---|---|---|
| 7.1.1 | Naya | Postal domain health (SPF/DKIM/bounce-rate) daily check + alert | S |
| 7.2.1 | Naya | Segmented list auto-refresh from `clients_master` filters | S |
| 7.3.1 | Review | LinkedIn full-automation safety review (ToS risk) — audit/decision session, code shayad nahi | S |

---

## Total Session Count
- Phase 3.0: 9 sessions
- Phase 3: 8 sessions
- Phase 4: 10 sessions
- Phase 5: 5 sessions
- Phase 6: 13 sessions
- Phase 7: 3 sessions
- **Total: 48 chote sessions** (har ek free-plan me easily fit hone ke hisaab se size kiya gaya hai)

## Build Order (same rationale jo original plan me tha)
```
Phase 3.0 (9 sessions) → Phase 3 (8) → Phase 4 (10) → Phase 5 (5) → Phase 6 (13) → Phase 7 (3, kabhi bhi 3.1 ke baad)
```
