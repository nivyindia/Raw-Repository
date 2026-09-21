# P0 Workflow Implementation Specifications

**Status:** v1.0 — 2026-09-16

## Purpose

Turn the first high-value library capabilities into executable workflow specifications.

| ID | Workflow | Trigger | Core steps | Human gate | Primary SoR | Output |
|---|---|---|---|---|---|---|
| WF-01 | Lead intake | Form/import/webhook | normalize → dedupe → enrich → CRM | No for data normalization | CRM | clean lead |
| WF-02 | Account research | qualified lead | research → ICP fit → evidence → summary | Yes before outreach | CRM + knowledge | research brief |
| WF-03 | Outreach | approved prospect | personalize → policy check → approve → send → log | Yes | CRM/email | sent message + trace |
| WF-04 | Meeting prep | calendar event | retrieve account → open opportunities → agenda → risks | Optional | CRM/knowledge | prep brief |
| WF-05 | Meeting debrief | meeting ends | transcript/notes → decisions → actions → CRM update | Yes for material CRM changes | CRM | structured debrief |
| WF-06 | Follow-up | action due | retrieve context → draft → approval → send/create task | Yes for external message | CRM/task | follow-up |
| WF-07 | Won-deal handoff | deal won | validate scope → create project → intake checklist → owner assignment | Yes | CRM/project | delivery workspace |
| WF-08 | Client intake | onboarding submitted | validate data → classify → missing-items queue → project update | Yes for sensitive data | CRM/project/knowledge | complete intake |
| WF-09 | Status reporting | scheduled | collect tasks/issues → summarize → exceptions → draft client update | Yes before external send | project/CRM | status report |
| WF-10 | Executive exception brief | schedule/event | collect KPIs → detect variance → rank exceptions → prepare decision brief | Yes | analytics/knowledge | executive brief |

## Common contract

Every workflow implements:

`Trigger → Context → Validate → Agent/Skill → Tool → Policy → Approval → Action → Verify → Evidence → SoR update → KPI → Exception`

## WF-01 Lead intake

**Idempotency key:** source + external lead ID/email + event timestamp bucket.

**Failure:** quarantine malformed records; never silently discard.

**Security:** only minimum contact/business data required for qualification.

## WF-02 Account research

**Evidence requirement:** every material claim includes source/provenance.

**No-go:** invented company facts, financials, pricing or decision-maker information.

## WF-03 Outreach

**Autonomy:** Recommend/Approve initially.

**Controls:** opt-out suppression, frequency limits, approved claims, approved sender identity, audit of final message.

## WF-05 Meeting debrief

**Required outputs:** decisions, commitments, owners, dates, risks, CRM fields changed.

**Control:** transcript/notes remain access-controlled and retention-bound.

## WF-07 Won-deal handoff

**Gate:** contract/scope status must be confirmed before delivery work is activated.

**Fallback:** manual handoff checklist.

## WF-10 Executive exception brief

**Rule:** the agent proposes; the executive decides. No automatic strategic change from a brief.

## Promotion criteria

A workflow moves from specification to pilot only after Gate A functional testing and Gate B control testing. Production requires Gates C–E from file 80.
