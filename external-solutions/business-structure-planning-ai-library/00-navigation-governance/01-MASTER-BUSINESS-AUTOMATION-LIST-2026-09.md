# MASTER LIST — Complete Business Automation Universe

**Status:** Canonical master checklist for business automation discovery.

## Purpose

This master list defines the automation coverage that the Business Structure Planning & AI Reuse Library must discover, catalog, qualify and map to reusable solutions.

**DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

## 1. Automation layers

**Micro automation → Workflow automation → Department automation → Company/autonomous automation**

---

## 2. Micro tasks

| Area | Required automation coverage |
|---|---|
| Email | classify → summarize → reply draft → follow-up → attachment extraction → routing |
| Calendar | scheduling → reschedule → reminders → preparation → follow-up → availability/time-zone handling |
| Chat/Messaging | classify → respond → route → summarize → create task → escalate |
| Voice/Phone | transcribe → identify intent → route → summarize → CRM update → callback |
| Documents | rename → classify → extract → OCR → metadata → folder → approval |
| Files | duplicate detection → versioning → archive → permissions → sync → retention |
| Forms | submission → validation → enrichment → CRM/ERP entry → notification |
| Notifications | event → correct person/channel → escalation → acknowledgement |
| Data entry | copy data between CRM/ERP/Sheets/forms automatically |
| Data cleaning | duplicate → normalize → validate → merge → flag |
| Contacts | create/update → enrich → deduplicate → assign owner |
| Tasks | email/message → task → priority → deadline → assignee → reminder |
| Approvals | request → policy check → approver → reminder → escalation → audit |
| Reports | collect → calculate → format → distribute → archive |
| Meeting | transcript → decisions → tasks → owners → deadlines → CRM/project update |
| Search | question → multi-source search → evidence → answer → save knowledge |
| Knowledge | capture → classify → verify → chunk → embed → link → update → retire |
| Translation | detect → translate → terminology QA → publish |
| Templates | data → proposal/invoice/report/email/document automatically |
| Scheduling | recurring jobs → dependencies → blackout windows → retries → timezone handling |
| Identity | provision → authenticate → authorize → rotate → revoke → audit |
| Secrets | create → scope → rotate → expire → revoke → audit |
| Web/browser | navigate → extract → fill → download → verify → record evidence |
| Media | generate → transform → resize → caption → transcribe → publish |
| Localization | language → locale → currency → timezone → regional format → QA |
| Accessibility | detect → remediate → validate → report |
| Backup/archive | snapshot → verify → retain → restore test → expire |
| Cost | meter → allocate → budget check → alert → cap/escalate |

---

## 3. Workflow-level automation

### Sales
Lead → enrich → qualify → score → assign → outreach → follow-up → meeting → CRM → proposal → reminder → close/lost → onboarding

Required micro-components:
- lead enrichment
- email sequencing
- WhatsApp sequencing
- lead deduplication
- meeting preparation
- proposal generation
- proposal comparison
- quote approval
- stale-lead detection
- automatic reactivation
- lost-lead reason analysis
- territory/routing
- account/contact hierarchy
- opportunity hygiene
- forecast update
- commission calculation
- renewal/upsell trigger

### Marketing
Idea → research → content → design → approval → publish → distribute → measure → repurpose

Required micro-components:
- content brief generator
- keyword clustering
- content calendar automation
- content repurposing
- social scheduling
- comment classification
- mention monitoring
- creative QA
- UTM generation
- campaign naming
- campaign QA
- landing-page QA
- attribution reconciliation
- audience segmentation
- consent/preference synchronization
- lead-source reconciliation
- SEO/AEO/GEO monitoring

### HR
Candidate → screening → interview → selection → offer → onboarding → performance → learning → offboarding

Required micro-components:
- CV parsing
- candidate scoring
- interview scheduling
- interview kit generation
- reference-check workflow
- offer generation
- onboarding checklist
- probation reminders
- performance-review reminders
- training assignment
- skill-gap detection
- exit checklist
- knowledge handover
- leave/attendance workflows
- compensation-change workflow
- benefits administration
- employee document expiry
- succession planning
- workforce capacity planning

### Customer lifecycle
Prospect → customer → onboarding → adoption → support → health → renewal → expansion → churn → win-back

Required:
- customer onboarding
- account provisioning
- health scoring
- usage alerts
- renewal reminders
- churn-risk detection
- expansion opportunity creation
- customer feedback collection
- NPS/CSAT workflows
- SLA monitoring
- escalation
- win-back campaigns
- customer offboarding/data export

### Product / engineering delivery
Idea → discovery → requirements → design → development → review → test → release → monitor → feedback

Required:
- feedback ingestion
- duplicate issue detection
- requirement extraction
- story/task generation
- estimation assistance
- dependency detection
- code generation
- code review
- test generation
- CI/CD
- release notes
- deployment approval
- rollback
- feature-flag management
- incident-to-issue creation
- release/customer communication

### Procurement / supply chain
Need → supplier discovery → RFQ → quote → comparison → approval → PO → receipt → invoice → payment → supplier review

Required:
- supplier discovery
- vendor onboarding
- RFQ generation
- bid normalization
- quote comparison
- negotiation support
- purchase approval
- PO generation
- goods receipt
- 3-way matching
- supplier risk
- contract expiry
- reorder point
- inventory replenishment
- shipment tracking

### Finance / revenue
Order/deal → billing → invoice → collection → reconciliation → close → reporting

Required:
- quote/order validation
- invoice generation
- tax calculation
- payment matching
- recurring billing
- failed-payment recovery
- collections sequencing
- credit control
- bank reconciliation
- expense processing
- receipt extraction
- journal preparation
- month-end close
- variance analysis
- cash forecasting
- revenue recognition
- commission/payroll handoff
- audit evidence collection

---

## 4. Department micro-automation matrix

| Department | Required automation families |
|---|---|
| CEO | daily briefing, decision queue, exception alerts, board-pack preparation, decision follow-up |
| Strategy | KPI → variance → hypothesis → action tracking, scenario analysis |
| Finance | invoice → approval → posting → reconciliation → exception, close, cash forecast |
| Accounting | transaction classification → reconciliation → close checklist → audit evidence |
| Sales | lead → enrichment → outreach → follow-up → CRM → forecast |
| Marketing | research → content → publish → campaign → analytics → attribution |
| HR | employee lifecycle + reminders + documents + access + workforce planning |
| Recruitment | sourcing → screening → interview → score → offer → onboarding |
| Operations | task routing → SLA → exception → escalation → capacity |
| Project | planning → assignment → status → risk → closure → lessons learned |
| Product | feedback → classify → roadmap → prioritization → release feedback |
| Engineering | issue → triage → assign → PR → test → deploy → rollback |
| QA | test generation → execution → defect → regression → release quality |
| IT | alert → diagnosis → ticket → remediation → verification → asset lifecycle |
| Security | alert → enrichment → severity → response → evidence → recovery |
| Legal | contract → clause extraction → risk → approval → signature → renewal |
| Procurement | request → quote → comparison → approval → PO → receipt → supplier review |
| Customer Success | onboarding → health → renewal → expansion → churn/win-back |
| Support | ticket → classify → answer → escalate → resolve → knowledge update |
| Knowledge | capture → classify → verify → publish → search → update → retire |
| Admin | forms → approvals → records → reminders → document lifecycle |
| Compliance | obligation → evidence → deadline → filing → audit → remediation |
| Analytics | data → metric → anomaly → root cause → report → distribution |
| Data/AI | ingest → validate → transform → train/evaluate → deploy → monitor → drift response |
| Facilities | request → assign → schedule → execute → inspect → close |
| Field Service | dispatch → route → work order → parts → proof → invoice → follow-up |
| Logistics | order → pick/pack → dispatch → tracking → delivery → exception |
| Inventory | receive → stock → reserve → replenish → count → reconcile → retire |
| Quality | inspection → nonconformance → CAPA → verification → audit |
| Manufacturing/Delivery | plan → allocate → execute → inspect → release → traceability |
| Partnerships | partner discovery → onboarding → deal registration → referral → payout → performance |
| Ecommerce | catalog → pricing → order → payment → fulfillment → return/refund |
| Community | moderation → classify → respond → escalate → sentiment → member lifecycle |
| PR/Media | monitoring → mention classification → response → approval → publication → measurement |
| Learning/Academy | enroll → assess → assign → remind → evaluate → certificate → alumni |
| Governance | policy → control → approval → evidence → review → exception → audit |
| Executive/Board | KPI → variance → narrative → decision → owner → deadline → follow-up |

---

## 5. Cross-system automation

| Integration | Example automation |
|---|---|
| CRM ↔ Email | New lead → CRM → email → reply → CRM activity |
| CRM ↔ Calendar | Qualified lead → meeting → calendar → reminder → meeting result → CRM |
| CRM ↔ Finance | Deal won → customer → invoice → payment → revenue |
| HR ↔ IT | Employee joined → account creation → permissions → equipment → onboarding |
| HR ↔ Payroll | Employee change → compensation → payroll |
| HR ↔ Learning | Skill gap → course assignment → completion → competency update |
| Procurement ↔ Finance | PO → receipt → invoice → 3-way match → payment |
| Procurement ↔ Inventory | approved PO → receipt → stock → reorder calculation |
| Marketing ↔ CRM | Ad lead → enrichment → CRM → qualification → revenue attribution |
| Marketing ↔ Analytics | campaign → spend → conversion → attribution → ROI |
| Support ↔ Product | Repeated complaints → issue cluster → product backlog |
| Engineering ↔ Support | Bug ticket → GitHub issue → fix → release → customer notification |
| Security ↔ HR | Employee offboarding → identity disable → token revoke → asset recovery |
| IT ↔ Procurement | asset need → approval → purchase → inventory → assignment |
| Finance ↔ Management | Financial variance → anomaly → CFO agent → decision |
| Finance ↔ Payroll | approved compensation → payroll → accounting → reporting |
| Finance ↔ Tax/Compliance | transaction data → tax calculation → filing evidence → deadline |
| Legal ↔ Procurement | contract → risk → approval → PO → renewal |
| Legal ↔ Sales | proposal → contract → redline → approval → signature → CRM |
| Customer Success ↔ Support | health decline → support escalation → intervention → health update |
| Product ↔ Analytics | usage → feature adoption → anomaly → product decision |
| Data ↔ AI | source → pipeline → feature/data quality → model/agent → evaluation |
| Everything ↔ Notification | Event → policy → notification → acknowledgement → escalation |
| Everything ↔ Audit | action → evidence → policy check → audit event → retention |

---

## 6. Event-driven automation

Canonical pattern:

**WHEN X HAPPENS → CHECK Y → DO Z → VERIFY → ESCALATE IF FAILED**

Examples:
- Lead enters CRM → enrich → score → assign → start sequence.
- Invoice becomes overdue → calculate aging → check customer risk → send reminder → create collection task → escalate if ignored.
- KPI drops beyond threshold → investigate → identify affected department → create incident → notify owner → recommend action.
- Employee leaves → disable accounts → revoke sessions → recover assets → transfer tasks → archive records → audit.
- API version changes → detect incompatibility → test adapter → switch fallback → notify owner → verify.
- New regulation/control arrives → map obligation → assign owner → collect evidence → deadline alert → filing/audit.

Event sources to catalog:
- user action
- record create/update/delete
- webhook
- API event
- schedule/time
- threshold
- anomaly
- payment
- email/message
- file/document change
- deployment/release
- security event
- approval decision
- SLA timer
- external data change
- IoT/device event
- location/geofence event
- marketplace/order event

---

## 7. Exception automation

Required exception classes:
- timeout
- API failure
- missing data
- duplicate data
- invalid data
- permission denied
- budget exceeded
- SLA breach
- approval timeout
- human does not respond
- agent failure
- tool failure
- payment failure
- integration failure
- conflicting records
- unexpected KPI
- security anomaly
- customer escalation
- rate limit
- authentication/token expiry
- schema/version mismatch
- dependency unavailable
- partial completion
- rollback failure
- data quality failure
- policy violation
- license/usage limit
- model failure/hallucination
- low-confidence result
- missing evidence
- duplicate execution/idempotency conflict

Canonical pattern:

**Detect → Classify → Retry → Alternate Path → Human Escalation → Resolve → Verify → Learn**

---

## 8. Self-maintaining automation

Automation itself must be monitored:

**Workflow running → Health check → Success rate → Latency → Cost → Failures → Drift → Broken API detection → Auto-repair/Fallback → Human escalation**

Also catalog:
- workflow versioning
- dependency monitoring
- connector/API health
- credential expiry
- schema drift
- prompt/skill drift
- model regression
- data drift
- workflow performance regression
- cost anomaly
- duplicate execution
- dead-letter queues
- replay
- rollback
- canary testing
- feature flags
- backup/restore
- disaster recovery
- capacity scaling
- maintenance windows

Target concept:

**AI Workforce + Automation Workforce**

---

## 9. Automation lifecycle / DevOps

The library must cover automation from creation to retirement:

**Discover → Design → Specify → Build/Adapt → Test → Simulate → Approve → Deploy → Observe → Evaluate → Version → Optimize → Rollback → Retire → Archive**

Required artifacts:
- automation specification
- input/output contract
- trigger contract
- dependency manifest
- permissions matrix
- policy/risk classification
- test cases
- test data
- simulation/dry-run
- approval policy
- deployment record
- version history
- changelog
- rollback plan
- runbook
- SLA/SLO
- owner
- cost budget
- audit evidence
- retirement/archive record

---

## 10. Human-in-the-loop and autonomy

Every automation should define its autonomy level:

**Observe → Analyze → Recommend → Draft → Request Approval → Execute → Verify → Auto-execute within policy**

Required controls:
- approval inbox
- delegation
- quorum/multi-approval
- approval timeout
- escalation
- pause/stop/resume
- emergency kill switch
- scoped permissions
- action limits
- spend limits
- rate limits
- data boundaries
- human override
- explainability/evidence
- audit trail

---

## 11. Automation discovery registry

Every discovered automation should be cataloged with:

| Field | Example |
|---|---|
| Automation ID | AUTO-SALES-001 |
| Layer | Micro / Workflow / Process / Department / Cross-company |
| Department | Sales |
| Business capability | Lead management |
| Task | Lead enrichment |
| Trigger | New lead |
| Trigger source | CRM webhook |
| Preconditions | Valid email |
| Inputs | Name, email, company |
| Context | Account + prior activity |
| Decision | Qualification rules/model |
| Actions | Search → enrich → validate |
| Tools | CRM + browser + API |
| Output | Enriched lead |
| Verification | Email/domain validation |
| Human approval | No |
| Autonomy level | Auto-execute |
| Risk | Low |
| Frequency | Real-time |
| Dependencies | CRM/API/browser |
| Error handling | Retry → fallback |
| Idempotency | Required |
| Audit | Yes |
| Evidence | URLs/logs/artifacts |
| KPI | Enrichment accuracy |
| SLA/SLO | < 5 min |
| Cost | Per-run / monthly |
| Security | RBAC/secret scope |
| Existing solutions | Links |
| Open source | Yes/No |
| License | MIT |
| Integration | API/MCP/n8n |
| Test status | Untested/Tested/Qualified |
| Reuse status | Candidate/Qualified/Production-reference |
| Owner | Department/role |
| Version | v1 |
| Nivy implementation | Later |

---

## 12. Complete hierarchy

**ATOMIC ACTION → MICRO TASK → TASK AUTOMATION → WORKFLOW → PROCESS → DEPARTMENT SYSTEM → CROSS-DEPARTMENT WORKFLOW → DEPARTMENT AI MANAGER → COMPANY AI EXECUTIVE → COMPANY CONTROL TOWER → AUTONOMOUS COMPANY**

Every level must support:

**Trigger → Context → Decision → Action → Verification → Exception → Escalation → Audit → Learning**

---

## 13. Automation categories that must never be skipped

Before declaring a capability researched, check all of these:

- agents
- generative AI
- traditional automation
- scripts
- functions/APIs
- webhooks
- MCP/A2A
- skills
- prompts
- workflow templates
- connectors
- integrations
- RPA/browser automation
- forms
- rules engines
- schedulers
- event buses/queues
- databases
- ETL/ELT
- dashboards
- BI
- reports
- document generation
- OCR/extraction
- e-signature
- notifications
- email/SMS/WhatsApp/voice
- search/retrieval
- RAG/knowledge
- memory
- human approval
- policy engines
- identity/RBAC
- secrets
- audit/evidence
- observability
- evaluation
- testing/simulation
- error recovery
- self-healing
- backup/DR
- cost/FinOps
- security
- privacy
- compliance
- localization
- accessibility
- commercial SaaS
- open source
- reusable libraries
- SOPs
- templates
- playbooks
- runbooks
- training/documentation

---

## 14. Current library coverage assessment

| Layer | Target |
|---|---|
| Major systems | Strong |
| Department systems | Strong |
| AI agents | Strong |
| Control towers | Strong |
| Micro automations | Expanded master coverage |
| Cross-system glue | Expanded master coverage |
| Event-driven automation | Expanded master coverage |
| Exception/self-repair | Expanded master coverage |
| Automation lifecycle/monitoring | Expanded master coverage |
| Atomic reusable actions/skills | Expanded master coverage |
| Human-in-the-loop/autonomy | Required |
| Automation DevOps | Required |
| Security/privacy/compliance | Required |
| Cost/FinOps | Required |
| Backup/DR | Required |

This is a **coverage checklist**, not a claim that every item has already been researched or has a reusable implementation.


---

## 17. Additional missing automation coverage — gap expansion

The following categories are added so the master list does not stop at common CRM/ERP/AI workflows.

### 17.1 Atomic / micro-level gaps

| Area | Additional required coverage | Progress |
|---|---|---|
| Inbox operations | spam/phishing classification, mailbox rules, thread merge/split, unsubscribe, bounce handling, sender reputation signals | Not Started |
| Email operations | send-time optimization, out-of-office handling, failed-delivery recovery, attachment conversion, secure-link creation | Not Started |
| Messaging | WhatsApp/SMS/Telegram/Teams/Slack channel preference, opt-in/opt-out, message threading, delivery/read status | Not Started |
| Calls | call recording/consent, voicemail, callback queue, disposition, call-quality checks, phone-number normalization | Not Started |
| Browser/desktop | clipboard, downloads/uploads, printing/scanning, desktop app handoff, session recovery, CAPTCHA/human handoff | Not Started |
| Documents | redaction, PII detection, classification confidence, document comparison, clause/table extraction, watermarking, document expiry | Not Started |
| Records | retention schedule, legal hold, records disposition, immutable archive, chain of custody | Not Started |
| Data quality | completeness, freshness, referential integrity, outlier detection, reconciliation, lineage, quality scoring | Not Started |
| Master data | customer/product/vendor/employee/location master-data synchronization and golden-record management | Not Started |
| Identity | joiner/mover/leaver, SSO lifecycle, MFA enrollment, access review, privileged-access expiry, service-account lifecycle | Not Started |
| Security | secret scanning, phishing triage, vulnerability ticketing, patch reminders, device posture, security evidence collection | Not Started |
| Privacy | consent capture, DSAR intake/fulfillment, deletion/retention checks, purpose limitation, privacy incident routing | Not Started |
| Payments | payment-link creation, payment-status polling, retry/dunning, refunds, chargeback/dispute routing, settlement reconciliation | Not Started |
| Expenses | receipt capture, policy validation, duplicate detection, approval, reimbursement, accounting handoff | Not Started |
| Travel | request → policy check → approval → booking → itinerary → expense → reconciliation | Not Started |
| Assets | asset register, assignment, maintenance, depreciation handoff, return, disposal, certificate/evidence tracking | Not Started |
| Scheduling | resource booking, room/equipment conflicts, waitlists, cancellation/no-show handling, recurring-resource planning | Not Started |
| Search/research | source discovery, source deduplication, citation/evidence capture, freshness checks, contradiction detection, research-to-knowledge publishing | Not Started |
| AI interactions | prompt routing, model selection, context assembly, tool selection, confidence threshold, fallback model, human escalation | Not Started |
| AI memory | memory write/update/delete, stale-memory detection, provenance, user/team/company scope, memory conflict resolution | Not Started |
| AI safety | prompt-injection detection, tool authorization, output validation, policy checks, unsafe-action blocking, evidence requirement | Not Started |
| Observability | trace correlation, run replay, token/cost attribution, latency budget, quality score, incident linkage | Not Started |
| Testing | unit/integration/e2e tests for automations, synthetic events, golden datasets, regression suites, load tests | Not Started |
| Recovery | retry policy, circuit breaker, fallback, dead-letter queue, replay, idempotency key, compensating action | Not Started |
| Localization | legal/entity formats, tax/currency rules, regional calendars, language fallback, timezone/DST edge cases | Not Started |
| Accessibility | keyboard navigation, screen-reader checks, captions, alt text, contrast/accessibility evidence | Not Started |
| Cost | per-agent/per-workflow/per-department cost allocation, quota, budget approval, anomaly detection, chargeback | Not Started |

### 17.2 Missing business workflows / value streams

| Value stream | Required automation coverage | Progress |
|---|---|---|
| Lead-to-cash | demand → lead → opportunity → quote → contract → order → invoice → collection → revenue | Not Started |
| Quote-to-order | qualification → pricing → quote → approval → signature → order | Not Started |
| Order-to-cash | order → fulfillment → invoice → payment → reconciliation → close | Not Started |
| Procure-to-pay | request → sourcing → approval → PO → receipt → invoice → payment | Not Started |
| Hire-to-retire | workforce plan → recruit → hire → onboard → develop → compensate → transfer → exit | Not Started |
| Idea-to-product | idea → research → discovery → requirements → build → QA → launch → adoption → retirement | Not Started |
| Incident-to-resolution | detect → triage → assign → mitigate → resolve → verify → RCA → prevent recurrence | Not Started |
| Request-to-fulfillment | request → policy → approval → assignment → execution → evidence → closure | Not Started |
| Record-to-report | capture → classify → post → reconcile → close → consolidate → report → audit | Not Started |
| Contract-to-renewal | draft → review → approve → sign → obligation → monitor → renew/terminate | Not Started |
| Source-to-contract | supplier discovery → qualification → RFQ → negotiation → contract → supplier performance | Not Started |
| Customer-issue-to-knowledge | issue → resolve → verify → extract lesson → knowledge article → publish → reuse | Not Started |
| Campaign-to-revenue | brief → audience → creative → media → lead → attribution → revenue → optimization | Not Started |
| Content-to-distribution | research → brief → create → QA → approval → publish → syndicate → measure → repurpose | Not Started |
| Employee-access lifecycle | hire/change/exit → identity → permissions → assets → review → revoke → audit | Not Started |
| Data-to-decision | ingest → quality → semantic model → analysis → insight → decision → action → outcome | Not Started |
| Model/agent-to-production | design → dataset → evaluation → approval → deployment → monitoring → rollback → retirement | Not Started |
| Policy-to-control | policy → control → owner → implementation → evidence → test → remediation → attestation | Not Started |
| Risk-to-treatment | identify → assess → prioritize → treatment → owner → monitor → accept/transfer/mitigate | Not Started |
| Problem-to-prevention | detect → RCA → corrective action → verification → preventive control → monitoring | Not Started |
| Asset-to-disposal | acquire → register → assign → maintain → inspect → return → dispose → evidence | Not Started |
| Supplier-to-performance | onboard → contract → order → delivery → quality → scorecard → remediation → renewal | Not Started |
| Revenue-to-forecast | pipeline → bookings → billing → collections → actuals → forecast → variance → action | Not Started |
| Cash-to-treasury | bank/payment feeds → cash position → forecast → liquidity → funding → reconciliation → controls | Not Started |

### 17.3 Missing department / corporate capability areas

| Capability | Required automation families | Progress |
|---|---|---|
| Treasury | cash position, liquidity, bank connectivity, payment controls, funding, FX, reconciliation | Not Started |
| Tax | tax data extraction, jurisdiction mapping, calculation, filing calendar, evidence, reconciliation, notices | Not Started |
| Payroll | payroll inputs, validation, payroll run, exceptions, payslips, statutory filings, accounting reconciliation | Not Started |
| Corporate Development | market scan, target screening, due diligence checklist, valuation inputs, integration tracking | Not Started |
| M&A / Integration | diligence → deal room → approvals → Day-1 readiness → systems/access/data integration → synergy tracking | Not Started |
| Investor Relations | KPI pack, investor Q&A, reporting calendar, disclosure workflow, stakeholder log | Not Started |
| Fundraising | pipeline → investor research → outreach → diligence → data room → term-sheet workflow → close | Not Started |
| Insurance / Risk Financing | policy inventory, renewal, claims intake, evidence, broker communication, coverage tracking | Not Started |
| Corporate Affairs | stakeholder mapping, correspondence, approvals, filings, public-position workflow | Not Started |
| Government / Public Sector | tender discovery, eligibility, bid preparation, compliance evidence, submission, contract tracking | Not Started |
| Grants | opportunity discovery, eligibility, application, budget, reporting, milestone evidence | Not Started |
| International Trade | import/export documentation, HS classification, duties, customs, sanctions checks, shipment compliance | Not Started |
| Revenue Management / Pricing | price rules, discount governance, quote optimization, margin checks, elasticity/experiment tracking | Not Started |
| FP&A | planning, budgeting, rolling forecast, scenario modeling, variance, management reporting | Not Started |
| Corporate Performance | enterprise KPI tree, OKR linkage, initiative tracking, benefits realization, executive reporting | Not Started |
| Enterprise Risk | risk register, controls, KRIs, treatment, risk acceptance, board reporting | Not Started |
| Business Continuity | BIA, dependency mapping, continuity plans, exercises, crisis communication, recovery verification | Not Started |
| Crisis Management | incident command, stakeholder communication, decision log, approvals, recovery, postmortem | Not Started |
| Enterprise Architecture | capability map, application portfolio, dependency graph, standards, architecture review | Not Started |
| Data Governance | ownership, glossary, lineage, quality, classification, access, retention, stewardship | Not Started |
| AI Governance | inventory, risk tiering, evaluations, approvals, model/agent cards, monitoring, incident management | Not Started |
| IP / Knowledge Assets | invention/idea register, licensing, trademarks, copyright evidence, renewal deadlines | Not Started |
| R&D / Innovation | research intake, experiment backlog, hypothesis tracking, experiment results, commercialization handoff | Not Started |
| Corporate Communications | internal announcements, external messaging, approvals, audience targeting, archive | Not Started |
| Workplace / Facilities | office access, maintenance, vendors, rooms, utilities, safety, occupancy, incidents | Not Started |
| Fleet / Mobility | vehicle/asset assignment, maintenance, fuel, route, compliance, incident, disposal | Not Started |
| Sustainability / ESG | data collection, emissions/activity records, targets, evidence, reporting, supplier data | Not Started |
| Franchise / Licensing | partner qualification, territory, agreements, fees/royalties, compliance, performance | Not Started |
| Channel / Partner Sales | partner onboarding, deal registration, lead sharing, MDF, commissions, pipeline attribution | Not Started |
| Affiliate / Referral | partner links/codes, attribution, validation, commissions, fraud checks, payout | Not Started |
| Marketplace Operations | listing, catalog sync, pricing, orders, fees, returns, ratings, reconciliation | Not Started |
| Subscription Operations | signup → entitlement → billing → renewal → failed payment → downgrade/upgrade → cancellation | Not Started |
| Community / Membership | signup → verification → onboarding → engagement → moderation → renewal/churn | Not Started |
| Customer Data Platform | identity resolution, profile stitching, consent, segmentation, activation, suppression | Not Started |
| Search / GEO / AEO | crawler monitoring, indexation, entity consistency, citations/mentions, AI-answer visibility, change detection | Not Started |
| Digital Presence | domain/DNS, website, analytics, forms, chat, social profiles, listings, reviews, app stores | Not Started |
| Procurement Category Management | spend taxonomy, category strategy, supplier concentration, savings pipeline, benchmark tracking | Not Started |
| Legal Operations | matter intake, assignment, deadlines, spend, outside counsel, evidence, reporting | Not Started |
| Quality Management | QMS, SOP control, audits, nonconformance, CAPA, training evidence, change control | Not Started |
| Knowledge Management | taxonomy, ownership, review cycles, stale-content detection, reuse analytics | Not Started |
| Change Management | impact analysis, stakeholder mapping, communications, training, adoption, benefits verification | Not Started |

### 17.4 Major company / autonomous-company level gaps

| Level | Missing capability | Progress |
|---|---|---|
| Company | Universal event bus / event contract across every department | Not Started |
| Company | Universal identity, RBAC, policy and approval plane | Not Started |
| Company | Universal data model / semantic layer / business ontology | Not Started |
| Company | Universal connector/integration registry | Not Started |
| Company | Universal automation registry and dependency graph | Not Started |
| Company | Universal human approval inbox | Not Started |
| Company | Universal audit/evidence ledger | Not Started |
| Company | Universal cost/usage ledger | Not Started |
| Company | Universal exception/recovery service | Not Started |
| Company | Universal notification and escalation service | Not Started |
| Company | Universal document/template/report registry | Not Started |
| Company | Universal KPI/metric/OKR registry | Not Started |
| Company | Cross-company causal graph and root-cause engine | Not Started |
| Company | Digital twin of company, systems, processes, people and resources | Not Started |
| Company | Enterprise scenario/simulation engine | Not Started |
| Company | Enterprise capacity/resource planning engine | Not Started |
| Company | Cross-platform attribution and revenue truth layer | Not Started |
| Company | Autonomous board/executive decision system with evidence and approvals | Not Started |
| Company | AI workforce registry, hierarchy, lifecycle, permissions and performance system | Not Started |
| Company | Automation workforce registry, hierarchy, lifecycle and performance system | Not Started |
| Company | Unified employee/company workspace and command center | Not Started |
| Company | Continuous discovery agent that detects new reusable solutions and gaps | Not Started |
| Company | Automation test/simulation/canary platform | Not Started |
| Company | Company-wide backup, disaster recovery and business continuity control plane | Not Started |
| Company | Company-wide knowledge graph / memory / provenance layer | Not Started |
| Company | Enterprise policy-as-code and bounded-autonomy engine | Not Started |
| Company | Cross-system reconciliation engine | Not Started |
| Company | Company-wide SLA/SLO/OLA management and escalation | Not Started |
| Company | Portfolio/initiative benefits-realization engine | Not Started |
| Company | Enterprise experimentation and optimization engine | Not Started |
| Company | Autonomous self-healing control plane with safe rollback | Not Started |
| Autonomous Company | Goal → planning → execution → measurement → correction → learning loop | Not Started |
| Autonomous Company | Multi-agent manager hierarchy with bounded authority | Not Started |
| Autonomous Company | Cross-department resource allocation and prioritization | Not Started |
| Autonomous Company | Company-wide strategic scenario planning and simulation | Not Started |
| Autonomous Company | Policy-constrained autonomous execution with human override | Not Started |
| Autonomous Company | Continuous self-audit, self-evaluation and evidence generation | Not Started |
| Autonomous Company | Continuous learning + reusable capability discovery loop | Not Started |
| Autonomous Company | Safe shutdown / pause / recovery / disaster mode | Not Started |

---

## 18. Master progress tracker

**Progress is deliberately conservative:** an item is not marked “Done” merely because the category exists in this checklist.  
Status values: **Not Started → Discovery → Cataloged → Qualified → Implemented → Verified**.

| Master layer | Scope | Progress |
|---|---|---|
| L0 | Atomic actions | Discovery |
| L1 | Micro tasks | Discovery |
| L2 | Task automations | Discovery |
| L3 | Workflows | Discovery |
| L4 | Business processes / value streams | Discovery |
| L5 | Department systems | Not Started |
| L6 | Cross-department workflows | Not Started |
| L7 | Department AI managers | Not Started |
| L8 | Company AI executives | Not Started |
| L9 | Company control tower | Not Started |
| L10 | Autonomous company | Not Started |
| Cross-cutting | Agents / skills / prompts / templates | Cataloged |
| Cross-cutting | APIs / connectors / MCP / A2A / webhooks | Cataloged |
| Cross-cutting | Human approval / policy / RBAC | Cataloged |
| Cross-cutting | Observability / evaluation / testing | Cataloged |
| Cross-cutting | Exception handling / self-healing | Cataloged |
| Cross-cutting | Security / privacy / compliance | Cataloged |
| Cross-cutting | Cost / FinOps | Cataloged |
| Cross-cutting | Backup / DR / lifecycle | Cataloged |
| Library | Existing-solution discovery | Discovery |
| Library | Reuse qualification | Discovery |
| Library | Runtime verification | Discovery |
| Nivy | Actual integration / implementation | Not Started |

### Progress rule

A row moves forward only when evidence exists:

- **Not Started** — listed but no focused discovery completed.
- **Discovery** — research is actively identifying reusable solutions.
- **Cataloged** — candidates/resources are recorded with links and metadata.
- **Qualified** — solution has been technically/business qualified for reuse.
- **Implemented** — integrated into the Nivy architecture.
- **Verified** — implementation has passed runtime/evidence checks.

**Important:** “Cataloged” or “Discovery” at the library level does **not** mean every underlying automation is complete.


## 15. Master research batch

**Complete Business Automation Universe — Atomic Tasks → Micro Automations → Workflows → Cross-Department Automations → Event/Exception/Self-Healing Automations**

This master list is the canonical checklist. Detailed reusable candidates, links, qualification evidence and implementation references belong in the solution catalogs and discovery records rather than being duplicated here.

## 16. Governing completion rule

The library is not complete merely because a department system or AI agent exists.

For every business capability, research must descend through:

**Atomic Action → Micro Task → Task Automation → Workflow → Process → Department → Cross-Department → AI Manager → Executive → Control Tower → Autonomous Company**

At each layer search for:

**Agents → Generative AI → Skills → Prompts → MCP/A2A → APIs → Connectors → Workflow Templates → Open Source → Commercial SaaS → Dashboards → Reports → Documents → SOPs → Templates → Monitoring → Exception Handling → Self-Healing**

And additionally verify:

**Security → Privacy → Identity → Permissions → Cost → Reliability → Testing → Observability → Audit → Backup/Recovery → Versioning → Human Approval → Accessibility → Localization → Lifecycle/Retirement**

**Status: MASTER AUTOMATION COVERAGE LIST EXPANDED.**

**Latest build progress:** L0 Atomic Actions, L1 Micro Tasks, L2 Task Automations and L3 Workflows are in **Discovery**. See [Atomic & Micro Automation Reuse Catalog](../03-solution-catalogs/32-atomic-micro-automation-reuse-catalog-2026-09.md), [Task Automation Reuse Catalog](../03-solution-catalogs/33-task-automation-reuse-catalog-2026-09.md) and [Workflow Reuse Catalog](../03-solution-catalogs/34-workflow-reuse-catalog-2026-09.md). The [Library README](./00-README.md) is the master file-level index.
