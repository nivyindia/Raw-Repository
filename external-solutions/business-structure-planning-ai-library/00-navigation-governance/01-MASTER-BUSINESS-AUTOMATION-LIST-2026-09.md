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
