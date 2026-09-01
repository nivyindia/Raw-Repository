# Startup OS — Micro Workflow Blueprint

## Purpose
Break the startup into tiny atomic workflows that can be built, tested, versioned, and integrated independently.

---

# Folder Structure

startup-os/
  10-ingestion/
  20-qualification/
  30-outreach/
  40-sales/
  50-onboarding/
  60-delivery/
  70-success/
  orchestration/

---

# 10 — Lead Ingestion (Atomic Workflows)

| ID | Workflow | Trigger | Output |
|---|---|---|---|
| 10.1 | cron-trigger | Cron | run_id |
| 10.2 | source-selector | Manual/Cron | source |
| 10.3 | scrape-google-maps | source | raw_leads |
| 10.4 | scrape-linkedin | source | raw_leads |
| 10.5 | scrape-website | source | raw_leads |
| 10.6 | validate-raw-record | raw_lead | valid/invalid |
| 10.7 | normalize-record | valid_lead | normalized_lead |
| 10.8 | enrich-email-domain | normalized | enriched |
| 10.9 | dedup-email-phone-domain | enriched | existing/new |
| 10.10 | upsert-clients-master | lead | lead_id |
| 10.11 | emit-lead-created | lead_id | event |

---

# 20 — Qualification

| ID | Workflow |
|---|---|
| 20.1 classify-intent |
| 20.2 detect-industry |
| 20.3 detect-company-size |
| 20.4 detect-budget-signal |
| 20.5 detect-authority-signal |
| 20.6 detect-need |
| 20.7 detect-timeline |
| 20.8 calculate-score |
| 20.9 assign-hot-warm-cold |
| 20.10 emit-lead-scored |

---

# 30 — Outreach

| ID | Workflow |
|---|---|
| 30.1 choose-channel |
| 30.2 build-email-personalization |
| 30.3 send-email-step-1 |
| 30.4 wait-2-days |
| 30.5 check-email-reply |
| 30.6 send-email-step-2 |
| 30.7 build-whatsapp-message |
| 30.8 send-whatsapp |
| 30.9 track-whatsapp-reply |
| 30.10 queue-linkedin-task |
| 30.11 send-sms-reminder |
| 30.12 queue-cold-call |
| 30.13 log-call-result |
| 30.14 classify-objection |
| 30.15 suggest-reply |
| 30.16 stop-sequence-on-reply |
| 30.17 mark-no-response |
| 30.18 emit-reply-received |
| 30.19 emit-meeting-interest |
| 30.20 emit-outreach-complete |

---

# 40 — Sales

| ID | Workflow |
|---|---|
| 40.1 create-cal-booking-link |
| 40.2 send-booking-link |
| 40.3 booking-confirmation |
| 40.4 meeting-reminder-24h |
| 40.5 meeting-reminder-1h |
| 40.6 meeting-attendance-update |
| 40.7 generate-discovery-summary |
| 40.8 generate-solution-outline |
| 40.9 fetch-rate-card |
| 40.10 generate-proposal |
| 40.11 approval-check |
| 40.12 send-proposal |
| 40.13 proposal-followup-3d |
| 40.14 proposal-followup-7d |
| 40.15 create-contract |
| 40.16 generate-signed-token |
| 40.17 send-contract |
| 40.18 verify-contract-signature |
| 40.19 mark-contract-signed |
| 40.20 create-invoice |
| 40.21 send-invoice |
| 40.22 verify-payment-webhook |
| 40.23 mark-payment-received |
| 40.24 emit-payment-received |

---

# 50 — Onboarding

| ID | Workflow |
|---|---|
| 50.1 create-odoo-partner |
| 50.2 create-project |
| 50.3 create-onboarding-checklist |
| 50.4 send-welcome-email |
| 50.5 send-whatsapp-welcome |
| 50.6 collect-assets-form |
| 50.7 validate-assets |
| 50.8 kickoff-meeting-schedule |
| 50.9 kickoff-reminder |
| 50.10 onboarding-complete |
| 50.11 emit-onboarding-complete |

---

# 60 — Delivery

| ID | Workflow |
|---|---|
| 60.1 create-delivery-tasks |
| 60.2 assign-freelancer |
| 60.3 start-project |
| 60.4 milestone-reminder |
| 60.5 collect-work |
| 60.6 qa-review |
| 60.7 client-review-request |
| 60.8 delivery-approved |
| 60.9 send-final-files |
| 60.10 close-project |
| 60.11 emit-project-delivered |

---

# 70 — Success / Growth

| ID | Workflow |
|---|---|
| 70.1 send-nps-survey |
| 70.2 capture-nps |
| 70.3 classify-promoter-passive-detractor |
| 70.4 alert-detractor |
| 70.5 request-testimonial |
| 70.6 create-case-study-draft |
| 70.7 generate-referral-link |
| 70.8 send-referral-invite |
| 70.9 track-referral |
| 70.10 upsell-trigger |
| 70.11 renewal-reminder-30d |
| 70.12 renewal-reminder-7d |
| 70.13 renewal-reminder-1d |
| 70.14 churn-risk-alert |
| 70.15 winback-sequence |
| 70.16 mark-advocate |

---

# Integration Map

lead.created
  -> 20.1

lead.scored
  -> 30.1

meeting.booked
  -> 40.4
  -> 40.5

contract.signed
  -> 40.20

payment.received
  -> 50.1

onboarding.completed
  -> 60.1

project.delivered
  -> 70.1

nps.promoter
  -> 70.5
  -> 70.7

---

# Orchestration

## Parent: Lead-to-Meeting

10.1 -> 10.3 -> 10.7 -> 10.8 -> 10.10 -> 20.1 -> 20.8 -> 30.1 -> 30.3 -> 40.1

## Parent: Meeting-to-Payment

40.3 -> 40.7 -> 40.10 -> 40.12 -> 40.15 -> 40.17 -> 40.18 -> 40.20 -> 40.22

## Parent: Payment-to-Retention

40.23 -> 50.1 -> 50.10 -> 60.1 -> 60.10 -> 70.1 -> 70.10 -> 70.11

---

# Build Order

Phase A: 10.x
Phase B: 20.x
Phase C: 30.x
Phase D: 40.x
Phase E: 50.x
Phase F: 60.x
Phase G: 70.x
Phase H: Orchestration

---

# Definition of Done for Each Workflow

- workflow.json created
- README.md created
- input.sample.json created
- output.sample.json created
- tested manually
- tested through parent workflow
- rollback documented

---

# Day-1 Launch Wiring

Enable:
- 10.x
- 20.x
- 30.1-30.9
- 40.1-40.5
- 40.9-40.24
- 50.1-50.10

Manual initially:
- LinkedIn outreach
- Cold calls
- Proposal approval
- QA review

---

# Final Startup Assembly

Traffic
 -> Ingestion
 -> Qualification
 -> Outreach
 -> Meeting
 -> Proposal
 -> Contract
 -> Payment
 -> Onboarding
 -> Delivery
 -> NPS
 -> Referral
 -> Upsell
 -> Renewal

This is the production startup pipeline.
