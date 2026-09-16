# Sales Micro-Workflow Gap & Resource Catalog — International Sales

**Status:** v1.0 — 2026-09-16
**Purpose:** Close the granularity gap between the high-level Sales operating model and the small operational actions that actually make a sales department work every day.

## 1. Finding

The Sales operating model in `89` and resource maps in `90–91` cover the major department capabilities, but several **micro-workflows** need to be explicit. These are easy to miss when research is organized only around departments or funnel stages.

Examples include:
- customer/prospect research before every interaction
- exact requirement discovery and requirement-gap detection
- briefing/questionnaire collection
- meeting scheduling and rescheduling
- timezone handling
- confirmations and reminders
- no-show recovery
- agenda generation
- meeting preparation
- live meeting assistance
- transcript/note processing
- action-item extraction
- follow-up drafting and scheduling
- proposal/PPT creation
- proposal review and approval
- proposal-view notifications
- commercial justification / ROI / business case
- promotion and campaign support for sales
- referral and advocacy promotion
- reactivation of old leads
- next-best-action reminders
- stakeholder/champion enablement
- internal handoff briefs
- customer requirement change tracking

These must be treated as first-class reusable workflows.

## 2. Complete micro-workflow matrix

| ID | Micro-workflow | Required capability | Resource types | Priority |
|---|---|---|---|---|
| MW-001 | Prospect company research | firmographic, website, news, technology, reviews, hiring, funding | research agents, enrichment, search skills | P0 |
| MW-002 | Prospect person research | role, tenure, responsibilities, public professional context | people research, enrichment | P0 |
| MW-003 | Buying committee mapping | economic buyer, champion, users, blockers, procurement | account/stakeholder agents | P0 |
| MW-004 | Pre-call requirement research | infer likely needs from public/internal context | research + discovery agents | P0 |
| MW-005 | Exact requirement gathering | problem, current state, desired state, constraints, priority, success criteria | discovery agent, forms, questionnaires | P0 |
| MW-006 | Requirement completeness check | identify missing/contradictory requirements | requirement analyst, checklist/eval | P0 |
| MW-007 | Requirement confirmation | send structured requirements summary for client confirmation | recap agent + approval | P0 |
| MW-008 | Requirement-to-solution mapping | map each requirement to service/product capability | solution agent | P0 |
| MW-009 | Requirement-to-proposal mapping | ensure every requirement is represented in proposal | proposal compliance matrix | P0 |
| MW-010 | Lead response | instant acknowledgement + routing + next step | workflow/CRM agent | P0 |
| MW-011 | Meeting booking | calendar availability + routing | scheduler/API | P0 |
| MW-012 | Timezone coordination | convert and confirm local times | calendar utility | P0 |
| MW-013 | Meeting confirmation | email/WhatsApp/etc. confirmation | workflow | P0 |
| MW-014 | Pre-meeting questionnaire | collect structured business context | form + CRM workflow | P0 |
| MW-015 | Reminder sequence | 24h/1h/etc. configurable reminders | automation | P0 |
| MW-016 | No-show handling | detect no-show, notify, reschedule | calendar/CRM workflow | P0 |
| MW-017 | Meeting agenda | generate agenda from stage/context | meeting skill | P0 |
| MW-018 | Meeting pre-read | create internal brief | research/meeting agent | P0 |
| MW-019 | Live meeting copilot | questions, objections, context, next actions | conversation AI | P1 |
| MW-020 | Transcript processing | summary, requirements, decisions, risks | transcription + agent | P0 |
| MW-021 | Action extraction | owner + deadline + task | meeting-task agent | P0 |
| MW-022 | CRM update | notes, stage, fields, next step | CRM automation | P0 |
| MW-023 | Follow-up email | personalized recap and next steps | writing skill + CRM | P0 |
| MW-024 | Follow-up scheduling | schedule future touches automatically | workflow | P0 |
| MW-025 | Follow-up escalation | no-response cadence and escalation | sequence engine | P0 |
| MW-026 | Next meeting booking | schedule before ending current meeting | scheduler | P0 |
| MW-027 | Discovery gap alert | flag unanswered critical questions | qualification agent | P0 |
| MW-028 | Pain/impact analysis | quantify business impact/cost of inaction | discovery/ROI agent | P0 |
| MW-029 | Solution brief | summarize proposed approach before full proposal | solution agent | P0 |
| MW-030 | Proposal brief | turn discovery into proposal inputs | proposal agent | P0 |
| MW-031 | Proposal generation | narrative, scope, deliverables, timeline, pricing | proposal agents | P0 |
| MW-032 | PPT/deck generation | presentation + editable PPTX | PPT skills/agents | P0 |
| MW-033 | Executive summary | one-page decision-maker summary | proposal skill | P0 |
| MW-034 | ROI/business case | value model and assumptions | ROI calculator/agent | P0 |
| MW-035 | Requirement compliance matrix | map requirement → response → evidence | RFP/proposal agent | P0 |
| MW-036 | Proposal QA | factual, scope, pricing, consistency, branding | QA agent | P0 |
| MW-037 | Proposal approval | sales/finance/legal approval | workflow + policy engine | P0 |
| MW-038 | Proposal delivery | send with tracking | email/document workflow | P0 |
| MW-039 | Proposal-view alert | notify owner when proposal is viewed | document analytics | P1 |
| MW-040 | Proposal review meeting | automatically propose meeting after delivery | scheduler | P0 |
| MW-041 | Quote generation | product/service/package + pricing | CPQ | P0 |
| MW-042 | Discount approval | policy threshold + manager approval | deal desk | P0 |
| MW-043 | Negotiation preparation | stakeholder, leverage, objections, BATNA/guardrails | negotiation skill | P0 |
| MW-044 | Objection preparation | predict and prepare responses | objection agent | P0 |
| MW-045 | Promotion campaign selection | choose suitable promotion mechanism by segment | campaign/promotion agent | P1 |
| MW-046 | Sales promotion offer design | discount/bundle/trial/bonus/referral/limited offer with margin guardrails | pricing + campaign agent | P1 |
| MW-047 | Promotion asset generation | email/social/landing-page/deck/call script | content agents | P1 |
| MW-048 | Promotion audience selection | ICP/segment/behavior/intent | segmentation agent | P1 |
| MW-049 | Promotion tracking | source, offer, conversion, CAC/margin | attribution/CRM | P1 |
| MW-050 | Cross-sell/upsell trigger | identify unmet/adjacent need | account intelligence | P0 |
| MW-051 | Reactivation | revive old/lost/stalled prospects | reactivation agent | P0 |
| MW-052 | Referral request | identify advocacy moment and request referral | CS/advocacy agent | P0 |
| MW-053 | Testimonial/case-study request | trigger after success milestone | advocacy workflow | P1 |
| MW-054 | Champion enablement | create internal justification/talking points | champion agent | P0 |
| MW-055 | Procurement preparation | required vendor docs, security/commercial questionnaire | deal desk/procurement skill | P0 |
| MW-056 | Internal deal briefing | sales → solution/finance/legal/delivery | handoff workflow | P0 |
| MW-057 | Sales-to-delivery handoff | confirmed scope, requirements, promises, stakeholders | handoff agent | P0 |
| MW-058 | Customer requirement change | version requirements and detect scope impact | change-control workflow | P0 |
| MW-059 | Decision-date tracking | buyer deadline and internal milestones | deal agent | P0 |
| MW-060 | Next-best-action | determine next action from deal state | sales agent | P0 |
| MW-061 | Reminder engine | overdue activity, promised follow-up, proposal expiry | workflow | P0 |
| MW-062 | Stalled-deal detection | inactivity/stage aging/commitment failure | RevOps agent | P0 |
| MW-063 | Competitive update | detect competitor mentions and changes | CI agent | P1 |
| MW-064 | Meeting outcome classification | positive/neutral/negative/no decision | conversation intelligence | P0 |
| MW-065 | Decision log | preserve decisions, rationale and owner | knowledge system | P1 |
| MW-066 | Lost-deal re-entry | define future trigger and re-engagement date | CRM workflow | P0 |
| MW-067 | Customer/prospect communication preference | channel, frequency, language, timezone | CRM/CDP | P1 |
| MW-068 | Sales task prioritization | rank today's work by revenue/risk/urgency | sales copilot | P0 |
| MW-069 | Daily sales briefing | meetings, follow-ups, risks, pipeline, tasks | daily-sales agent | P0 |
| MW-070 | Manager exception briefing | stalled deals, missed SLAs, forecast changes | manager copilot | P0 |

## 3. Newly verified reusable resources

| ID | Resource | Relevant micro-workflows | Source |
|---|---|---|---|
| MR-001 | agentic-sales-skills | prospect research, discovery prep, demo customization, live meeting support, meeting debrief, follow-up, task extraction, proposal, negotiation, champion enablement, forecast, daily standup | https://github.com/Autter-dev/agentic-sales-skills |
| MR-002 | AI Sales Team Claude | prospect research, qualification, decision makers, outreach, follow-up, meeting prep, proposals, objections, competitors | https://github.com/zubair-trabzada/ai-sales-team-claude |
| MR-003 | SalesShortcut | lead research, pain-point analysis, proposal generation, outreach, meeting scheduling, follow-up, lead management | https://github.com/pkprajapati7402/SalesShortcut |
| MR-004 | Agentic Proposal Generator | discovery transcript → customer situation → requirements → solution → implementation → ROI → investment → next steps | https://github.com/griv32/agentic-proposal-generator |
| MR-005 | Proposal PPT Skill | brief audit, proposal thesis, compliance matrix, slide-by-slide planning, editable PPTX, presenter script | https://github.com/ChuluuMGL/proposal-ppt-skill |
| MR-006 | Powerpoint-Generator | requirements interview → information gathering → outline → content → visual design → editable PPTX | https://github.com/CerealAxis/Powerpoint-Generator |
| MR-007 | ProposalCraft | brief analysis, discovery-call prep, proposal drafting, proposal improvement, proposal→email, SOW generation | https://github.com/jabbawocky/proposalcraft |
| MR-008 | Microsoft RFP Generator template | RFP response drafting from approved proposal content/templates and reusable case studies | https://github.com/MicrosoftDocs/m365copilot-docs/blob/main/docs/agent-template-rfp-assistant.md |
| MR-009 | OpenAI sales workflows | account research, stakeholder mapping, discovery, meeting prep, follow-up, proposal/business case, deal management, RFPs | https://openai.com/academy/sales/ |
| MR-010 | Discovery Call Automation pattern | booking → CRM record → questionnaire → confirmation → 24h reminder → research → notes → proposal trigger | https://soloclientstack.com/discovery-call-automation-workflow |
| MR-011 | AgentDock referral-program template | referral promotion design, channels, tracking, communication, incentives, terms, metrics and launch | https://github.com/AgentDock/agentdock/blob/main/content/prompt-library/sales/referral-program-template.mdx |
| MR-012 | Pre-visit Sales Agent | contextual customer/distributor research and recommended opening action before visit | https://github.com/upadhyayanurodh/ai-gcp-pre-visit-sales-agent |

## 4. Sales promotion is broader than discounts

The resource search should explicitly cover:

- introductory offers
- bundles/packages
- trials/pilots/POCs
- limited-time offers
- referral programs
- partner/co-marketing promotions
- event/webinar promotions
- educational lead magnets
- assessment/audit offers
- free consultation/discovery
- case-study/reference-led promotion
- customer success proof
- seasonal/local promotions
- reactivation offers
- cross-sell/upsell campaigns
- loyalty/advocacy programs
- account-based offers
- procurement-specific incentives
- volume/term incentives
- channel incentives
- sales contests/SPIFs

Every promotion must connect to:
`audience → offer → eligibility → economics/margin → channel → message → CTA → tracking → conversion → revenue → retention`

## 5. Exact requirement-gathering model

The discovery system should capture at minimum:

### Current state
- business context
- current process/system
- current provider/tool
- users/stakeholders
- volume
- geography
- constraints

### Problem
- pain point
- frequency
- severity
- business impact
- cost of inaction
- root cause

### Desired state
- desired outcome
- success criteria
- measurable target
- priority
- deadline

### Solution constraints
- budget
- technical constraints
- integrations
- security/privacy
- compliance
- procurement
- implementation capacity

### Buying process
- decision maker
- economic buyer
- champion
- users
- procurement
- legal/security
- evaluation criteria
- competitors
- decision date

### Confirmation
`captured → normalized → conflict checked → missing-field check → customer confirmation → version locked → proposal mapping`

## 6. Meeting operating loop

`Lead/Opportunity → qualify → scheduler → timezone → confirmation → questionnaire → research → agenda → reminders → meeting → transcript → requirements → actions → CRM update → recap → next meeting → follow-up cadence`

Scheduling, confirmations, reminders, routing and post-meeting follow-up are established automation targets; complex proposals and quote approvals should retain human review gates. citeturn0search1turn0search5turn0search6

## 7. Proposal/PPT operating loop

`Discovery → requirements → compliance matrix → solution architecture → value/ROI → scope → timeline → pricing → risks/exclusions → proposal → PPT → QA → approvals → delivery → view tracking → review meeting → negotiation → contract`

The newly found proposal resources demonstrate that this can be decomposed into reusable skills rather than one giant proposal prompt. `proposal-ppt-skill` explicitly covers brief audit, winning thesis, compliance mapping, slide planning and editable PPTX generation; the Agentic Proposal Generator turns discovery transcripts into structured proposals with solution, implementation, ROI and investment sections. citeturn1search0turn1search4

## 8. Prospect/customer research loop

`Account → people → company → website → products/services → customers → reviews → competitors → technology → hiring → funding/news → pain signals → intent → buying committee → hypotheses → discovery questions → CRM evidence`

The research should distinguish **facts**, **inferences/hypotheses**, and **customer-confirmed requirements**. Public research must not be treated as confirmed customer need until validated.

## 9. Daily sales operating system

### Automated morning
- today's meetings
- prospect briefs
- overdue follow-ups
- proposal reminders
- stalled deals
- high-intent signals
- tasks ranked by value/urgency

### Before meeting
- account brief
- people brief
- previous interactions
- likely requirements
- discovery questions
- objections
- desired next step

### After meeting
- summary
- requirements
- decisions
- action items
- owner/deadline
- CRM update
- follow-up draft
- next meeting recommendation

### End of day
- unfinished high-priority work
- missed SLAs
- unanswered prospects
- tomorrow preparation
- forecast changes

## 10. Additional gap categories to keep researching

These are now explicitly added to the discovery backlog:

1. Sales promotion/campaign operating system
2. Prospect intelligence and pre-call research
3. Customer intelligence and account planning
4. Requirement engineering for sales
5. Requirement validation/confirmation
6. Meeting lifecycle automation
7. Presentation/PPT generation
8. Proposal generation and proposal QA
9. Business-case/ROI generation
10. Follow-up/reminder orchestration
11. No-show recovery
12. Proposal engagement tracking
13. Champion enablement
14. Referral/advocacy promotion
15. Reactivation campaigns
16. Sales task prioritization
17. Next-best-action engine
18. Communication/channel preference management
19. Decision and commitment tracking
20. Sales knowledge/decision memory
21. Sales-to-delivery promise/requirement control
22. Requirement-change and scope-impact tracking
23. Micro-automation observability
24. Sales-agent quality evaluation

## 11. Status

These are **newly identified/expanded micro-workflow requirements**, not claims that every one is missing from Nivy's existing repository. Existing catalogs may already partially cover them; this file makes the requirements explicit so the resource search can map them one-by-one and prevent hidden gaps.

`DISCOVER → DEDUPE → VERIFY → LICENSE/COST → TEST → ADAPT → INTEGRATE → BUILD ONLY IF MISSING`
