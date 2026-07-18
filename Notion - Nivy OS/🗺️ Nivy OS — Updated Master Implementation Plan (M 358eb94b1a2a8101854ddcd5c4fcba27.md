# 🗺️ Nivy OS — Updated Master Implementation Plan (May 2026)

> **What this page is:** A fully updated, synthesised implementation plan for the Nivy multi-brand Company OS — integrating the original build plan, the world-class benchmark comparison, the 40-improvement framework, and a realistic sequencing based on where Nivy stands in May 2026. Follow phases in order. Do not skip.
> 

> **Current estimated maturity: ~35%** → After Phases 1–3: ~72% → After all 7 phases: ~92%
> 

---

# 🧠 Starting Point — Honest Assessment

Your workspace has 11 live databases, 8 brand homes, a detailed Nivy Next 10-section OS, and rich raw research. The biggest gaps are not about *content* — they are about **traction and accountability**: the scorecard nobody is reviewing weekly, the issues being solved in WhatsApp, the SOPs being created without RACI, and KPIs that exist in theory but not as a live weekly tool.

**The single most important insight from benchmarking against EOS, OKR, Spotify, and Landmark OS:**

> Nivy has built a world-class knowledge and execution system. What it is missing is a world-class accountability and traction system.
> 

---

# 📊 Phase Overview

| Phase | Focus | Weeks | Hours | Maturity |
| --- | --- | --- | --- | --- |
| **1** | Database Upgrade + Traction Core | 1–2 | 25–30h | 35% → 50% |
| **2** | Accountability & Governance | 3–4 | 20–25h | 50% → 62% |
| **3** | Revenue & Client Intelligence | 5–6 | 20–25h | 62% → 72% |
| **4** | Strategic Intelligence | 7–8 | 15–20h | 72% → 80% |
| **5** | People, Training & Culture | 9–10 | 15–20h | 80% → 87% |
| **6** | Navigation + Cross-Brand Intelligence | 11 | 10–12h | 87% → 90% |
| **7** | Automation & Self-Sustaining Systems | 12+ | 15–20h | 90% → 92% |
| **8** | Future State (Q3 2026+) | — | 15–20h | Triggered |

**Total: ~118–142 hours across 12 weeks**

At 10–12 hrs/week = 12-week programme. At 20 hrs/week = 6–7 weeks.

---

# 🔵 PHASE 1 — Foundation: Database Upgrade + Traction Core

## Weeks 1–2 | ~25–30 hours | Maturity: 35% → 50%

> **Why first:** Nothing else works without solid databases and a live scorecard. These are the concrete slab. Every other phase pours on top of this one.
> 

---

## WEEK 1 — Database Upgrades + Scorecard

### Day 1–2 | Upgrade 5 Core Databases

**Owner:** OS Admin (Founder or designated)

**Time:** 6–8 hours

**tasks_database** — add these missing fields:

- Output Link (URL)
- QC Status (Select: Pending / Approved / Rework)
- Time Taken (Number — hours)
- Blocker (Text)
- Week (Date)
- Cycle (Select)
- Cycle Status (Select: Inbox / Current / Backlog / Cancelled)

**sop_database** — add:

- Function (Select: Lead Gen / Content / Closing / Delivery / Admin / HR / Finance / Tech / Compliance)
- Linked Knowledge (Relation → knowledge_database)
- Linked Templates (Relation → templates_database)
- Time Benchmark (Number — minutes SLA)
- Performance Score (Number 1–10)
- Review Cycle (Select: Weekly / Monthly / Quarterly)
- RACI – Responsible (Person)
- RACI – Accountable (Person)
- RACI – Informed (Multi-person)

**knowledge_database** — add:

- Source (Select: Internal / ChatGPT / External Research / Meeting Notes)
- Used In SOP (Relation → sop_database)
- Prerequisites (Relation → knowledge_database — self)
- Next Learning (Relation → knowledge_database — self)
- Promoted From (URL)

**clients_database** — add:

- Pipeline Stage (Select: Prospect / Qualified / Proposal Sent / Negotiating / Won / Lost / Churned)
- Deal Value (Number)
- Close Date (Date)
- Client Health (Select: 🟢 Healthy / 🟡 At Risk / 🔴 Critical)
- Last Contact (Date)
- Next Action (Text)
- Account Manager (Person)
- NPS Score 30-day (Number)
- NPS Score 90-day (Number)
- NPS Category (Select: Promoter / Passive / Detractor)
- Testimonial Status (Select: Not Asked / Requested / Received)

**projects_database** — add:

- Appetite (Select: Small / Medium / Large)
- Pitch Status (Select: Not Written / Draft / Approved)
- Circuit Breaker Date (Date — when to kill if no progress)
- Client Success Definition (Text)

✅ **Done when:** Every database has a Brand field. Every existing record has Brand filled.

---

### Day 3 | Create 3 Missing Databases

**Owner:** OS Admin

**Time:** 3–4 hours

**Create: kpi_database**

Fields: KPI Name (Title), Brand, Department, Metric Type (Output/Quality/Revenue/Speed/Engagement), Target (Number), Actual (Number), Period (Daily/Weekly/Monthly/Quarterly), Trend (Improving/Stable/Declining), Alert (Checkbox), Owner (Person)

Create filtered views: one per active brand.

**Create: tools_database**

Fields: Tool Name (Title), Brand (Multi-select), Department (Multi-select), Function (Select), Linked SOPs (Relation), Status (Active/Deprecated/Evaluating), Setup Guide (URL), Cost (Free/Paid/Freemium), Owner (Person)

Populate with all tools currently in use (target 15+ entries).

**Create: experiments_database**

Fields: Experiment Name (Title), Brand, Department, Hypothesis (Text), Variable Tested (Text), Result (Win/Loss/Inconclusive/In Progress), Learning (Text), Next Action (Text), Linked SOP (Relation), Linked Knowledge (Relation)

Add a template button for one-click new experiment.

**Also: Add 6 fields to ChatGPT Conversations DB**

- Brand (Select)
- Content Type (Select: SOP / Strategy / Knowledge / Framework / Idea / Research)
- Department (Select)
- Promotion Status (Select: Raw / Under Review / Promoted / Archived)
- Priority (Select: Core / Useful / Future / Ignore)
- Promoted To (URL — link to structured page created)

✅ **Done when:** All 3 databases exist. 15+ tools entered. Template button on experiments DB works.

---

### Day 4–5 | Build the Weekly Scorecard — Improvement #1

**Owner:** OS Admin + Brand Leads

**Time:** 4–5 hours

**Benchmark:** EOS — the single highest-impact thing EOS companies implement first.

**Create: scorecard_database**

Fields: Metric Name (Title), Brand, Owner, Period, Weekly Target (Number), This Week Actual (Number), Status (Select: 🟢 Green / 🟡 Yellow / 🔴 Red), Trend (Improving/Stable/Declining), Week (Date)

**Populate Scorecard — Nivy Next (8–12 metrics):**

- Cold emails sent
- Reply rate (%)
- Qualified leads
- Proposals sent
- Deals closed
- Projects delivered on time
- Client satisfaction flag
- Team tasks completed

**Populate Scorecard — Nivy Advisory (8–12 metrics):**

- New client enquiries
- Filings completed this week
- Compliance reviews done
- Overdue client items
- Client NPS flag

**Populate Scorecard — Nivy Nexus (5–8 metrics):**

- Outreach messages sent
- Connections made
- Community posts published
- Buyer-seller introductions
- Active deals

Add recurring Monday task for each metric owner: "Update Scorecard — [Brand]" due every Monday 9am.

✅ **Done when:** Scorecard is live with real numbers for the current week. Every metric has an owner.

---

## WEEK 2 — Issues DB + 2-Week Cycles + QC Checklists

### Day 1–2 | Build Issues DB with IDS Workflow — Improvement #2

**Owner:** OS Admin

**Time:** 3–4 hours

**Benchmark:** EOS — issues discussed in WhatsApp disappear. Logged issues get solved.

**Create: issues_database**

| Property | Type | Options |
| --- | --- | --- |
| Issue Title | Title |  |
| Brand | Select | All 8 brands |
| Department | Select |  |
| Type | Select | Short-Term / Long-Term / People |
| Identified By | Person |  |
| Owner | Person | Who must resolve it |
| Status | Select | Open / In Discussion / Solved / Dropped |
| Resolution | Text | What was done |
| Date Identified | Date |  |
| Target Resolution | Date |  |

Run a 20-minute team brainstorm. Log every known open issue — target 10+ entries.

Add IDS section to the L10 Meeting template: Identify → Discuss (3 min max) → Solve (assign + date).

✅ **Done when:** 10+ real issues logged. Every issue has Owner + Target Resolution Date.

---

### Day 2–3 | 2-Week Cycle System — Improvement #22

**Owner:** OS Admin + Nivy Next Lead

**Time:** 2–3 hours

**Benchmark:** Linear — the forcing function that creates shipping discipline.

- Confirm Cycle and Cycle Status fields exist on tasks_database
- Create **Inbox view**: all tasks with Cycle = Inbox
- Create **Current Cycle view**: Cycle = current cycle name
- **Triage the Inbox now**: every task goes to Current Cycle, Backlog, or Cancelled. Inbox = 0 tasks.
- Add recurring task: "Cycle Planning — [Brand]" every other Monday. Owner: Brand Lead.

✅ **Done when:** Inbox view = 0 tasks. Current Cycle view is populated for next 2 weeks.

---

### Day 3–5 | QC Checklists per Deliverable Type — Improvement #32

**Owner:** Department Heads

**Time:** 5–6 hours

**Benchmark:** Amazon / McDonald's — quality is a checklist, not a judgment call.

Build Notion page templates with pass/fail criteria for each deliverable:

**1. QC Checklist — Cold Email Sequence (Nivy Next)**

- [ ]  Personalisation correct
- [ ]  No spam trigger words
- [ ]  CTA single and clear
- [ ]  Unsubscribe mechanism present
- [ ]  Brand voice approved
- [ ]  Tracking links working
- [ ]  Sequence timing correct

**2. QC Checklist — Client Tax Filing (Nivy Advisory)**

- [ ]  Figures match source documents
- [ ]  Correct tax year
- [ ]  Correct jurisdiction rules applied
- [ ]  Reviewed by CPA
- [ ]  Client signature obtained
- [ ]  Filed within deadline
- [ ]  Filing reference number recorded

**3. QC Checklist — Weekly KPI Report (All brands)**

- [ ]  All metrics present
- [ ]  Targets vs actuals shown
- [ ]  Trend direction noted
- [ ]  No calculation errors
- [ ]  Sent by deadline
- [ ]  Stored in reports_database

**4. QC Checklist — New SOP (All brands)**

- [ ]  12-part structure complete
- [ ]  Tested by someone who didn't write it
- [ ]  Owner assigned
- [ ]  Brand + Department tagged
- [ ]  Linked to brand Index
- [ ]  Review cycle date set
- [ ]  RACI fields filled

**5. QC Checklist — Project Pitch (All brands)**

- [ ]  All 7 sections complete
- [ ]  Appetite defined
- [ ]  Client success definition written
- [ ]  Rabbit holes identified
- [ ]  No-gos stated
- [ ]  Approved by Brand Lead before project starts

✅ **Done when:** 5 QC checklists exist and each has been used on at least one real output.

---

# 🟡 PHASE 2 — Accountability & Governance

## Weeks 3–4 | ~20–25 hours | Maturity: 50% → 62%

> **Why second:** Once the scorecard is live and issues are being logged, the system needs accountability structure — who decides what, who owns which outcome, how decisions are recorded.
> 

---

## WEEK 3 — V/TO + Quarterly Rocks + Level 10 Meeting

### Day 1–2 | Vision/Traction Organizer per Active Brand — Improvement #5

**Owner:** Founder / CEO

**Time:** 4–5 hours (~1.5 hrs per brand)

**Benchmark:** EOS — the first page every EOS company builds.

Create one V/TO page per active brand under: Division Home → Section 1

Each V/TO contains:

- **Core Values** (3–5)
- **Core Focus** (purpose + niche)
- **10-Year Target**
- **3-Year Picture**
- **1-Year Plan**
- **Quarterly Rocks** (3–5 for Q2 2026)
- **Marketing Strategy** (target market, USP, proven process, guarantee)

Brands to complete: Nivy Next / Nivy Advisory / Nivy Nexus

Advisory note: include market focus (US/UK/UAE/AUS/Canada) and service specialisation.

Nexus note: UAE market, community model, buyer-seller positioning.

✅ **Done when:** 3 V/TOs exist, founder-approved, shared with each brand's team.

---

### Day 3 | Quarterly Rocks / OKR Tracker — Improvement #6

**Owner:** OS Admin

**Time:** 2–3 hours

**Benchmark:** EOS + OKR — quarterly focus layer between vision and weekly tasks.

**Create: rocks_database**

| Property | Type | Notes |
| --- | --- | --- |
| Rock Title | Title | e.g. "Launch Nivy Advisory UK SOP Library" |
| Brand | Select |  |
| Quarter | Select | Q1/Q2/Q3/Q4 2026 |
| Owner | Person | One person per Rock |
| Status | Select | On Track / Off Track / Done / Dropped |
| % Complete | Number | 0–100 |
| Due Date | Date | End of quarter |

Enter Q2 2026 Rocks for Nivy Next, Advisory, Nexus — 3–5 per brand.

Each Rock must have exactly ONE owner.

Review Rocks every L10 meeting (5 minutes). Reset quarterly.

✅ **Done when:** rocks_database exists. Q2 Rocks entered for all 3 active brands.

---

### Day 4–5 | Level 10 Meeting Template — Improvement #7

**Owner:** OS Admin

**Time:** 2–3 hours

**Benchmark:** EOS — the weekly meeting that makes every other system get used.

Create as a Notion page template. Same agenda every week, no exceptions:

```
Level 10 Meeting — [Brand] — [Date]

Segue (5 min)
  → One good thing: personal + professional

Scorecard Review (5 min)
  → Open Scorecard filtered view
  → Flag any 🔴 or 🟡 metrics

Rock Review (5 min)
  → Open Rocks view for Q2 2026
  → On Track / Off Track per Rock

Customer & People Headlines (5 min)
  → Client wins or issues
  → Team wins or issues

To-Do Review (5 min)
  → Last week's to-dos: Done / Not Done
  → Close completed items

IDS — Identify, Discuss, Solve (60 min)
  → Open Issues DB, pull top 3–5 issues
  → IDS each one
  → Assign to-dos: owner + due date

Conclude (5 min)
  → Rate the meeting 1–10
  → Cascading messages (what gets shared with team)
```

Create one copy per active brand. Schedule as recurring weekly task.

✅ **Done when:** First L10 meeting held for at least one brand. Rated ≥7/10 by attendees.

---

## WEEK 4 — RACI + Decision Register + Accountability Charts

### Day 1–2 | RACI on All SOPs — Improvement #3

**Owner:** Department Heads

**Time:** 4–6 hours

**Benchmark:** RACI standard — Owner ≠ Accountable. Both must exist.

- Confirm RACI–Responsible, RACI–Accountable, RACI–Informed fields exist on sop_database
- Fill RACI on every Approved SOP retroactively
- Update 12-part SOP template: add RACI section with four rows (R/A/C/I)

**Rule:** Responsible = who executes. Accountable = who owns outcome + signs off. These are often different people.

✅ **Done when:** 0 Approved SOPs with empty Responsible or Accountable fields.

---

### Day 3 | Decision Register — Improvement #8

**Owner:** OS Admin

**Time:** 2 hours

**Benchmark:** EOS — decisions not logged get re-litigated. Logged decisions become institutional memory.

**Create: decision_database**

| Property | Type | Notes |
| --- | --- | --- |
| Decision | Title | What was decided |
| Brand | Select |  |
| Made By | Person | Who had decision authority |
| Date | Date |  |
| Context | Text | Why this decision was made |
| Outcome | Text | What happened as a result |
| Status | Select | Active / Superseded / Under Review |
| Linked SOP | Relation | If decision resulted in an SOP |

Retroactively log 10+ key business decisions from memory. Place in Nivy Global OS.

✅ **Done when:** decision_database exists. 10+ historical decisions logged.

---

### Day 4–5 | Accountability Charts + OS Changelog — Improvements #15, #34

**Owner:** Founder + Brand Leads

**Time:** 3–4 hours

**Benchmark:** EOS — different from an org chart. Defines what success looks like in each seat.

Create one page per active brand: "Accountability Chart — [Brand]"

Place under: Division Home → Section 1

For each seat:

- Seat Name
- Current Person in Seat
- Core Responsibilities (max 5)
- 3 Measurable Outcomes that define success

The person in the seat must read and agree to the outcomes.

**Also: Create os_changelog_database**

Fields: Change Title, Date, Changed By, Change Type, What Changed, Why, Impact, Rollback Plan

New rule: every schema change to any database must be logged here.

First entries: log everything done in Phase 1.

✅ **Done when:** Accountability Charts exist for Next, Advisory, Nexus. OS Changelog has Phase 1–2 entries.

---

# 🟠 PHASE 3 — Revenue & Client Intelligence

## Weeks 5–6 | ~20–25 hours | Maturity: 62% → 72%

> **Why third:** Once accountability structure is in place, the system needs revenue visibility. This phase turns the OS from a documentation system into a business system.
> 

---

## WEEK 5 — CRM Pipeline + Client NPS + Voice of Customer

### Day 1–2 | CRM Pipeline View — Improvement #4

**Owner:** Sales Lead per brand

**Time:** 3–4 hours

**Benchmark:** Landmark OS — Kanban pipeline on clients_database.

Confirm Pipeline Stage, Deal Value, Close Date, Client Health, Last Contact, Next Action, Account Manager fields exist on clients_database.

**Create Kanban views — one per active brand:**

- Nivy Next columns: Prospect / Qualified / Proposal Sent / Negotiating / Won / Lost / Churned
- Nivy Advisory columns: Enquiry / Onboarding / Active / Renewal / Churned
- Nivy Nexus columns: same as Next

Ensure every client and prospect has Pipeline Stage filled.

✅ **Done when:** 3 Kanban views exist. All clients correctly staged.

---

### Day 3–4 | Client NPS & Raving Fan System — Improvement #28

**Owner:** Account Managers per brand

**Time:** 3–4 hours

**Benchmark:** Tony Robbins — satisfied clients stay. Raving fans refer.

Write a 6-part NPS Collection SOP:

1. At 30 days post-onboarding, send NPS question via email
2. Log score in clients_database
3. If 9–10 (Promoter): trigger Referral Ask task within 48 hours
4. If 0–6 (Detractor): trigger Escalation call task within 24 hours
5. At 90 days: repeat
6. At renewal: repeat

Run first NPS collection: send to all active clients onboarded 30+ days ago.

✅ **Done when:** 80%+ of eligible clients have NPS score. Tasks created for all Promoters and Detractors.

---

### Day 5 | Voice of Customer Database — Improvement #29

**Owner:** OS Admin + Marketing Lead

**Time:** 2–3 hours

**Benchmark:** Real client language is the most powerful marketing asset.

**Create: voc_database**

| Property | Type | Notes |
| --- | --- | --- |
| Quote | Title | Exact client words |
| Brand | Select |  |
| Service | Text |  |
| Type | Select | Testimonial / Objection / Complaint / Suggestion / Win |
| Source | Text | WhatsApp, email, call, etc. |
| Date | Date |  |
| Used In | Text | Where this quote has been used |

Populate with 20+ real client quotes from memory, WhatsApp, and email archives.

Add filtered view (Type = Testimonial) to each brand's Marketing Hub.

Add filtered view (Type = Objection) to each brand's Sales Hub.

✅ **Done when:** 20+ entries. Both filtered views exist in their respective hubs.

---

## WEEK 6 — Revenue Forecast + Unit Economics + Practice Hubs

### Day 1–2 | Revenue Forecast Tracker — Improvement #10

**Owner:** Finance Lead / Founder

**Time:** 2–3 hours

**Create: revenue_forecast_database**

| Property | Type | Notes |
| --- | --- | --- |
| Month | Date |  |
| Brand | Select |  |
| Projected Revenue | Number |  |
| Actual Revenue | Number |  |
| Variance | Formula | Actual - Projected |
| Key Driver | Text | What caused variance |
| Owner | Person |  |

Enter last 3 months retrospectively per active brand. Enter current month projection.

✅ **Done when:** 3 months of historical data + current month projection for each active brand.

---

### Day 3 | Unit Economics Tracker — Improvement #30

**Owner:** Founder / Finance Lead

**Time:** 2 hours

**Create: unit_economics_database**

| Property | Type | Notes |
| --- | --- | --- |
| Service / Product | Title | One row per service line |
| Brand | Select |  |
| Average Deal Value | Number |  |
| CAC | Number | Cost to Acquire Customer |
| LTV | Number | Lifetime Value |
| LTV:CAC Ratio | Formula | LTV / CAC |
| Gross Margin % | Number |  |
| Payback Period | Formula | CAC / (Monthly Revenue per client) |
| Health | Select | 🟢 Healthy / 🟡 Watch / 🔴 Fix |

Enter at least 2 service lines per active brand. Even rough estimates create immediate clarity.

✅ **Done when:** unit_economics_database exists. Every active service line has a row.

---

### Day 4–5 | Cross-Brand Practice Hubs — Improvement #9

**Owner:** Marketing Lead + Sales Lead

**Time:** 3–4 hours

**Benchmark:** Spotify Guilds — cross-team knowledge sharing.

**Build Marketing Practice Hub** (in Nivy Global)

Sections:

- Top Performing Assets (linked view: templates_database, Performance = High, Use Case = Marketing)
- This Month's Learnings
- Experiments (linked from experiments_database)
- Cross-Brand SOP Links
- Monthly Practice Meeting Notes

**Build Sales Practice Hub** (in Nivy Global)

Sections:

- Top Scripts
- Top Objection Responses (linked from voc_database, Type = Objection)
- Win/Loss Learnings
- Experiments
- Outreach Templates

**Schedule monthly Practice Meetings:**

- "Marketing Practice Meeting — all brands" — 30 min, first Monday of month
- "Sales Practice Meeting — all brands" — 30 min, first Monday of month

Output: one new entry in the Learnings section of each hub.

> A win at Nivy Next (e.g. cold email subject with 40% open rate) should reach Nivy Advisory within days — not never.
> 

✅ **Done when:** Both Practice Hubs exist with 3+ entries each. First meetings scheduled.

---

# 🟤 PHASE 4 — Strategic Intelligence

## Weeks 7–8 | ~15–20 hours | Maturity: 72% → 80%

> **Why fourth:** With revenue visibility and traction rhythm running, Nivy can now look outward — at competitors, markets, and scenarios — and make strategic decisions from data, not instinct.
> 

---

### Day 1–3 | Competitor Intelligence Database — Improvement #24

**Owner:** Brand Leads + Marketing Leads

**Time:** 4–5 hours

**Create: competitor_intelligence_database**

| Property | Type | Notes |
| --- | --- | --- |
| Competitor Name | Title |  |
| Brand it Competes With | Select |  |
| Market | Select |  |
| Category | Select | Direct / Indirect / Aspirational |
| Pricing | Text |  |
| Key Differentiators | Text |  |
| Our Advantage | Text | **Must be filled — forces articulation** |
| Their Weakness | Text |  |
| Recent Moves | Text |  |
| Last Updated | Date |  |
| Update Owner | Person |  |

Target: 5 competitors per active brand (15+ entries minimum).

Every entry must have "Our Advantage" filled.

Add filtered view (by Brand) to each Division Home under a "Competitive Landscape" section.

Assign monthly update owners. Add recurring update tasks (first Monday of month).

✅ **Done when:** 15+ entries. All have Our Advantage filled. Recurring update tasks exist.

---

### Day 4–5 | Scenario Plans per Active Brand — Improvement #25

**Owner:** Founder / Brand Leads

**Time:** 4–5 hours (~1.5 hrs per brand)

Create one page per brand under: Division Home → Section 1

Each scenario plan contains:

- **Base Case:** Revenue assumption, team size, key risks, key opportunities, top 3 priorities
- **Best Case:** What must go right, how to accelerate
- **Worst Case:** What could cause it, contingency actions, tripwire metric ("If X happens, we do Y")

Advisory-specific risks: regulatory changes per market, CPA capacity, client concentration.

Nexus-specific risks: UAE market dynamics, platform competition, community engagement.

Review quarterly alongside V/TO.

✅ **Done when:** 3 scenario plans exist. All scenarios have revenue assumption + action priorities. Founder approved.

---

### Week 8 | Communication Protocol + Error Log + Idea Bank — Improvements #23, #33, #31

**Communication Protocol ("How We Communicate at Nivy")** — 3–4 hours

- Create page in Nivy Global
- Define: what goes in Notion vs. WhatsApp vs. email vs. meeting
- Response time expectations per channel
- Async-first principles
- The rule: "If it's not in Notion, it didn't happen" — for SOPs, decisions, and issues
- Create weekly_checkin_database (Person, Brand, Week, Completed This Week, Working On Next, Blockers, Morale)
- Cancel standing status meetings. L10 is the only recurring team touchpoint.

**Error Log** — 1–2 hours

Create error_log_database: Error Title, Brand, Department, Date Occurred, Cost of Error, Root Cause, Fix Applied, Prevention Change, Linked SOP, Resolved (Checkbox)

New rule: every error logged within 24 hours of discovery.

Seed with 5+ historical errors from memory.

**Idea Bank** — 2–3 hours

Create idea_bank_database: Idea Title, Submitted By, Brand, Category, Problem It Solves, Estimated Impact, Estimated Effort, Status (Submitted/Under Review/Promoted/Rejected/Parked)

Schedule monthly Innovation Review (30 min). Founder reviews top ideas. Top 1–2 promoted to Pitch Status in projects_database.

✅ **Done when:** Communication Protocol adopted by all Brand Leads. Error log has 5+ entries. Idea bank has 10+ ideas.

---

# 🟣 PHASE 5 — People, Training & Culture

## Weeks 9–10 | ~15–20 hours | Maturity: 80% → 87%

> **Why fifth:** With traction, accountability, and revenue systems running, people systems can be built correctly — because now there's something meaningful to onboard people into and evaluate them against.
> 

---

### Week 9 | Role Scorecards + SOP Version History + Training Tracker — Improvements #26, #12, #14

**Role Scorecards** — 4–5 hours

Create role_scorecards_database (private/restricted):

- Role Title, Brand, Seat Mission, Core Outcomes (3–5 measurable results), Competencies, Core Values Fit, Performance Thresholds (Excellent/Meets/Below), Keeper Test Question
- Core Outcomes must be numbers: "20 qualified leads/week" not "generate leads"
- One scorecard per active seat per brand
- The seat occupant must read and agree

**SOP Version History** — 2–3 hours

- Add "Change Log" toggle at bottom of every SOP template
- Columns: Version / Date / Changed By / What Changed / Why
- Retroactively add v1.0 entries to the top 10 most-used SOPs
- New rule: every SOP update requires a Change Log entry

**Training Completion Tracker** — 2–3 hours

Create training_tracker_database: Person, Brand, Module Name, Linked Knowledge Entry (Relation), Completion Status (Not Started/In Progress/Complete), Completion Date, Score (optional)

Enter all current team members. Fill completion status for any training already done.

✅ **Done when:** Every active seat has a scorecard with measurable outcomes. Version history on top 10 SOPs. Training tracker populated.

---

### Week 10 | Role-Specific Onboarding Tracks + Employee Pulse Check — Improvements #11, #27

**Onboarding Tracks** — 5–6 hours

Build Universal Day 1 (for all brands, before any brand track):

- Nivy Global overview and values
- Communication Protocol
- Workspace navigation guide
- Naming conventions
- How to use tasks_database

Build role-specific Day 2–7 tracks for at least 2 roles per active brand:

*Nivy Next: Sales/Outreach Role*

- Day 2: Read top 5 Sales SOPs
- Day 3: Shadow a live outreach session
- Day 4: First own outreach attempt
- Day 5: QC review of Day 4 output
- Day 6–7: Full execution with support

*Nivy Advisory: Compliance/Tax Role*

- Day 2: Jurisdiction-specific guide
- Day 3: Shadow a client filing
- Day 4–5: Complete a test case filing
- Day 6: QC review
- Day 7: Sign-off

**One new joiner must complete the track and give feedback. Update based on ambiguities they hit.**

**Quarterly Employee Pulse Check (eNPS)** — 1–2 hours

Create pulse_check_database: Quarter, Brand, Score (0–10), Strength (what to continue), Improvement (what to change)

Build anonymous [Tally.so](http://Tally.so) or Typeform linked to this database.

Schedule quarterly recurring task: "Send eNPS Pulse Check" — first week of each quarter.

✅ **Done when:** Universal Day 1 exists. 2+ role-specific tracks built and tested by a real joiner. First pulse check responses collected.

---

# 🟥 PHASE 6 — Navigation + Cross-Brand Intelligence

## Week 11 | ~10–12 hours | Maturity: 87% → 90%

> **Why sixth:** The final structural layer before automation. This phase completes the discovery system, project workflow, and OS health monitoring.
> 

---

### Day 1 | Project Pitch Template — Improvement #21

**Owner:** OS Admin

**Time:** 2–3 hours

Build as a Notion page template with 7 sections:

1. The Problem
2. The Appetite (Small / Medium / Large — sets scope)
3. The Solution Sketch
4. Rabbit Holes (what could distract or expand scope)
5. No-Gos (what is explicitly out of scope)
6. Client Success Definition — from the client's perspective
7. Approval block

Apply to projects_database as a page template.

Backfill all active projects: every In Progress project gets Pitch Status = Approved.

✅ **Done when:** Template exists. Zero projects In Progress with Pitch Status = Not Written.

---

### Day 2–3 | Notion Template Buttons — Improvement #13

**Owner:** OS Admin

**Time:** 3–4 hours

**Benchmark:** Landmark OS — one-click generation cuts SOP creation time by 70%.

Add Notion template buttons to:

- **sop_database:** Auto-generate full SOP page — 12 sections, all properties defaulted, RACI section, Change Log toggle, QC Checklist link placeholder. Should produce a fully structured page in <5 seconds.
- **knowledge_database:** Auto-generate Knowledge page — Overview, Key Concepts, Examples, Related SOPs, Prerequisites, Next Learning sections.
- **experiments_database:** Auto-generate Experiment page — Hypothesis, Control, Variable, Measurement, Results, Learning, Next Action sections.

✅ **Done when:** 3 template buttons built and tested. Creating via button is faster than manual creation.

---

### Day 4–5 | 3-Click Audit + OS Health Check — Improvement #35

**Owner:** OS Admin

**Time:** 2–3 hours

**3-Click Audit:** Starting from Nivy HQ, verify you can reach each content type in 3 clicks or fewer:

- [ ]  An SOP
- [ ]  A knowledge page
- [ ]  A client record
- [ ]  A task
- [ ]  A KPI
- [ ]  A competitor entry
- [ ]  An open issue

Fix any that fail. Every active page must have at least one forward link and one back-link (no dead ends).

**Build OS Health Check Scorecard Template** — a 20-point quarterly audit:

- Data Quality (fill rates per database)
- SOPs (overdue reviews, drafts, missing RACI)
- Navigation (3-click test, dead ends, broken links)
- Usage (Scorecard updated, L10s held, Rocks reviewed, ChatGPT processed)

Scoring: 🟢 Green = 17+, 🟡 Yellow = 12–16, 🔴 Red = <12

Run first Health Check now. Log score. Assign actions for anything below Green as tasks.

✅ **Done when:** All 7 content types reachable in ≤3 clicks. First Health Check run. Score logged.

---

# ⚙️ PHASE 7 — Automation & Self-Sustaining Systems

## Week 12+ | ~15–20 hours | Maturity: 90% → 92%

> **Critical rule:** Only begin Phase 7 after the OS Health Check scores Green (17+). Automating a messy system creates automated mess.
> 

---

## Notion Native Automations (no external tools needed)

| # | Trigger | Action | Done When |
| --- | --- | --- | --- |
| 12.1 | Task Status → "Done" AND QC Status ≠ "Approved" | Revert to "In QC", notify Owner | Test: task bounces back without QC |
| 12.2 | SOP Last Updated = 30 days before Review Cycle date | Create review task for Owner | First review task auto-created in week 1 |
| 12.3 | KPI Alert checkbox = checked | Create escalation task for Brand Lead | Test: check Alert box → task appears |
| 12.4 | Issue Target Resolution = today, Status ≠ Solved | Create overdue task for Issue Owner | First overdue issue triggers escalation |
| 12.5 | Client NPS Category → "Promoter" | Create referral ask task for Account Manager (48h deadline) | Test: set client to Promoter → task appears |
| 12.6 | Client NPS Category → "Detractor" | Create escalation call task for Dept Head (24h deadline) | Test: set client to Detractor → escalation appears |

---

## [Make.com](http://Make.com) / Zapier Automations (complex cross-tool triggers)

| # | Trigger | Action | Done When |
| --- | --- | --- | --- |
| 12.7 | New entry in ChatGPT conversations DB | Set Promotion Status = "Raw", create processing task | Every new conversation auto-creates a task |
| 12.8 | Every Monday 8am | Create weekly review task for each Brand Lead (Scorecard + Issues + Rocks) | Tasks appear every Monday before 9am |
| 12.9 | Every 2nd Friday | Create cycle-end review task for Nivy Next Lead | Cycle review task appears every 2 weeks |
| 12.10 | First Monday of each month | Create competitor intel update tasks for all Update Owners | Competitor tasks appear monthly without manual creation |

---

## Phase 7 Final QA

- [ ]  Run full OS Health Check — must score 17+ (Green)
- [ ]  3-click test for all 7 content types
- [ ]  Dead-end audit — 0 dead-end pages in active sections
- [ ]  All automations tested with real triggers
- [ ]  Log Phase 7 in os_changelog_database

✅ **Done when:** OS scores Green on health check. All 10 automations active and tested.

---

# ⚪ PHASE 8 — Future State (Q3 2026+ / Trigger-Based)

> These 5 improvements are not time-pressured. Activate when the trigger condition is met.
> 

| # | Improvement | Activate When | Est. Time |
| --- | --- | --- | --- |
| 36 | Partner / Franchise Performance Scorecard | First franchise or formal partner agreement signed | 2 hours |
| 37 | Market Expansion Readiness Checklist | Before entering any new geography | 2 hours |
| 38 | Legal & Compliance Risk Register | Advisory crosses 50 active clients OR enters new jurisdiction | 2–3 hours |
| 39 | Brand Health Tracker (share of voice, NPS by market) | Marketing spend exceeds $5k/month per brand | 2 hours |
| 40 | AI-Assisted Research Pipeline (auto-classify ChatGPT → correct DB) | ChatGPT conversations DB exceeds 200 unprocessed entries | 8–12 hours |

---

# 🚨 5 Decisions to Make Before Phase 6

These will block progress if left unresolved:

1. **Automation tool** — Notion native handles Phases 1–6. Cross-tool triggers (forms → tasks, etc.) need [Make.com](http://Make.com) or Zapier. Decide which before Phase 7 begins.
2. **Notion permissions architecture** — Will clients, VAs, or partners get Notion access? Affects database structure and must be decided before building role dashboards.
3. **KPI review cadence** — Weekly or monthly per brand? Who is the KPI owner per brand? These two questions must be answered before the Scorecard has any value.
4. **ChatGPT processing owner** — Who runs the weekly research promotion process? This is a recurring task in tasks_database. Without a named owner, the ChatGPT DB will continue to accumulate without being processed.
5. **Academy / Alliance / Care Foundation activation timeline** — Does Phase 6 need to include stubs for these, or are they genuinely Q3 2026 or later?

---

# ✅ Master Checklist — All 40 Improvements

> A task is not done when it is **built**. It is done when the **Done When** criterion is met — which always specifies the first real use, not just creation.
> 

| Done? | # | Improvement | Phase | Week |
| --- | --- | --- | --- | --- |
| [ ] | 1 | Weekly Scorecard per Active Brand | 1 | 1 |
| [ ] | 2 | Issues DB with IDS Workflow | 1 | 2 |
| [ ] | 3 | RACI Fields on All SOPs | 2 | 4 |
| [ ] | 4 | CRM Pipeline View (Kanban) | 3 | 5 |
| [ ] | 5 | V/TO per Active Brand | 2 | 3 |
| [ ] | 6 | Quarterly Rocks / OKR Tracker | 2 | 3 |
| [ ] | 7 | Level 10 Meeting Template | 2 | 3 |
| [ ] | 8 | Decision Register | 2 | 4 |
| [ ] | 9 | Cross-Brand Practice Hubs (Marketing + Sales) | 3 | 6 |
| [ ] | 10 | Revenue Forecast Tracker | 3 | 6 |
| [ ] | 11 | Role-Specific Onboarding Tracks | 5 | 10 |
| [ ] | 12 | SOP Version History & Change Log | 5 | 9 |
| [ ] | 13 | Notion Template Buttons (one-click generation) | 6 | 11 |
| [ ] | 14 | Training Completion Tracker | 5 | 9 |
| [ ] | 15 | Accountability Chart per Active Brand | 2 | 4 |
| [ ] | 16 | Client Health Score System | 3 | 5 |
| [ ] | 17 | People Analyzer (EOS — values + GWC) | 5 | 9 |
| [ ] | 18 | "How We Work at Nivy" Cross-Brand Playbook | 4 | 8 |
| [ ] | 19 | SOP Testing Protocol | 5 | 9 |
| [ ] | 20 | Quarterly Business Review (QBR) Template | 6 | 11 |
| [ ] | 21 | Project Pitch / Working Backwards Template | 6 | 11 |
| [ ] | 22 | 2-Week Cycle System | 1 | 2 |
| [ ] | 23 | Communication Protocol & Async System | 4 | 8 |
| [ ] | 24 | Competitor Intelligence Database | 4 | 7 |
| [ ] | 25 | Annual Scenario Plans per Active Brand | 4 | 7 |
| [ ] | 26 | Role Scorecards per Active Seat | 5 | 9 |
| [ ] | 27 | Quarterly Employee Pulse Check (eNPS) | 5 | 10 |
| [ ] | 28 | Client NPS & Raving Fan System | 3 | 5 |
| [ ] | 29 | Voice of Customer (VoC) Database | 3 | 5 |
| [ ] | 30 | Unit Economics Tracker per Brand | 3 | 6 |
| [ ] | 31 | Idea Bank & Innovation Pipeline | 4 | 8 |
| [ ] | 32 | QC Checklists per Deliverable Type | 1 | 2 |
| [ ] | 33 | Structured Error Log | 4 | 8 |
| [ ] | 34 | OS Changelog Database | 2 | 4 |
| [ ] | 35 | Quarterly OS Health Check Scorecard | 6 | 11 |
| [ ] | 36 | Partner / Franchise Performance Scorecard | 8 | Q3+ |
| [ ] | 37 | Market Expansion Readiness Checklist | 8 | Q3+ |
| [ ] | 38 | Legal & Compliance Risk Register | 8 | Q3+ |
| [ ] | 39 | Brand Health Tracker | 8 | Q3+ |
| [ ] | 40 | AI-Assisted Research Pipeline | 8 | Q3+ |

---

# 📅 Full Timeline Summary

| Week | Focus | Key Outputs | Hours |
| --- | --- | --- | --- |
| **Week 1** | Database upgrades + Scorecard | 5 DBs upgraded, 3 new DBs created, live scorecard with real metrics | 13–17 hrs |
| **Week 2** | Issues DB + Cycles + QC Checklists | Issues DB live (10+ entries), Inbox cleared, 5 QC checklists built | 12–15 hrs |
| **Week 3** | V/TO + Rocks + L10 Meeting | 3 brand V/TOs, Q2 Rocks entered, first L10 meeting held | 10–13 hrs |
| **Week 4** | RACI + Decision Register + Accountability Charts | RACI on all active SOPs, 10+ decisions logged, Charts for 3 brands, OS Changelog live | 10–12 hrs |
| **Week 5** | CRM Pipeline + Client NPS + VoC | 3 Kanban pipelines, NPS from all active clients, 20+ VoC entries | 10–12 hrs |
| **Week 6** | Revenue Forecast + Unit Economics + Practice Hubs | Revenue tracker (3 months retro), unit economics per service, 2 practice hubs live | 9–11 hrs |
| **Week 7** | Competitor Intel + Scenario Plans | 15+ competitors tracked, 3 scenario plans written and approved | 9–11 hrs |
| **Week 8** | Comms Protocol + Error Log + Idea Bank | Protocol adopted, error log live (5+ entries), idea bank with 10+ ideas | 7–9 hrs |
| **Week 9** | Role Scorecards + SOP Versions + Training Tracker | Scorecard per active seat, version history on core SOPs, tracker live | 9–11 hrs |
| **Week 10** | Onboarding Tracks + Pulse Check | 2+ role-specific tracks tested by real joiners, first eNPS collected | 7–9 hrs |
| **Week 11** | Project Pitch + Template Buttons + OS Health Check | Pitch template live, 3 template buttons built, first Health Check run | 8–10 hrs |
| **Week 12** | Automations + Final QA | 6 Notion automations + 4 Make/Zapier automations live, OS scores 🟢 Green | 10–12 hrs |

**Total: ~118–142 hours across 12 weeks**

---

# 🔥 The One Rule That Governs This Entire Plan

> **The difference between a 35%-mature OS and a 92%-mature OS is not the number of pages built. It is how many of those pages are used every week.**
> 

Phases 1 and 2 alone — roughly 45–55 hours — take Nivy from 35% to 62% maturity. The Scorecard, Issues DB, RACI on SOPs, CRM Pipeline, and first L10 meeting are what transform the OS from a documentation system into an operating system.

**Start there. This week.**

---

*Built by Claude | Based on full workspace audit + EOS, OKR, Spotify, and Landmark OS benchmarks | May 2026 | Version 3.0 — Consolidated*