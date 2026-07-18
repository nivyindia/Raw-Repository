# 🗓️ Nivy OS — Master Implementation Plan (All 40 Improvements)

> **What this page is:** A week-by-week, day-by-day implementation plan for all 40 improvements identified across the World-Class OS Comparison (V1.0) and the Extended Benchmark Analysis (V2.0). Every task has an owner type, an estimated time, a specific output, and a done criterion. Nothing is vague. Follow this page in sequence and Nivy OS reaches ~92% world-class maturity.
> 

> **How to use this:** Work top to bottom. Do not skip phases. Each phase builds on the one before it. The "Done When" column is the only thing that matters — a task is not done until its criterion is met, not when it feels finished.
> 

> **Total estimated build time:** ~120–140 hours across 12 weeks. At 10–12 hours/week of dedicated OS build time, this is a 12-week programme. At 20 hours/week, it compresses to 6–7 weeks.
> 

---

# 📊 Implementation At a Glance

| Phase | Name | Weeks | Hours | Maturity Jump | Improvements Covered |
| --- | --- | --- | --- | --- | --- |
| **Phase 1** | Foundation — Databases & Traction Core | 1–2 | 25–30 hrs | 30% → 50% | #1, 2, 3, 21, 22, 32 |
| **Phase 2** | Accountability & Governance | 3–4 | 20–25 hrs | 50% → 62% | #5, 6, 7, 8, 15, 34 |
| **Phase 3** | Revenue & Client Intelligence | 5–6 | 20–25 hrs | 62% → 72% | #4, 9, 10, 28, 29, 30 |
| **Phase 4** | Strategic Intelligence | 7–8 | 15–20 hrs | 72% → 80% | #24, 25, 23, 33, 31 |
| **Phase 5** | People, Training & Culture | 9–10 | 15–20 hrs | 80% → 87% | #11, 12, 13, 14, 26, 27 |
| **Phase 6** | Cross-Brand Intelligence & Meeting Rhythm | 11 | 10–12 hrs | 87% → 90% | #16, 17, 18, 19, 20, 35 |
| **Phase 7** | Automation & Self-Sustaining Systems | 12+ | 15–20 hrs | 90% → 92% | #36–40 + all automation wiring |

---

# 🔵 PHASE 1 — Foundation: Databases & Traction Core

## Weeks 1–2 | ~25–30 hours | Maturity: 30% → 50%

> **Why first:** Nothing else works without solid databases and a live scorecard. These are the concrete slab. Every other phase pours on top of this one.
> 

---

### WEEK 1 — Database Upgrades & Scorecard

#### Day 1–2 | Audit & Upgrade Core Databases

**Owner:** OS Owner (Founder or designated OS Admin)

**Time:** 6–8 hours

| Task | Action | Done When |
| --- | --- | --- |
| **1.1** Audit tasks_database | Confirm Brand, Owner, Deadline, Status, Priority exist. Add: Output Link, QC Status, Time Taken, Blocker, Week, Cycle, Cycle Status fields | All 11 fields present. Every existing task has Brand filled. |
| **1.2** Audit sop_database | Add: Function, Linked Knowledge, Linked Templates, Time Benchmark, Performance Score, Review Cycle, RACI — Responsible, RACI — Accountable, RACI — Informed fields | All 9 new fields added. Brand field confirmed on all entries. |
| **1.3** Audit knowledge_database | Add: Source, Used In SOP (relation), Prerequisites (self-relation), Next Learning (self-relation), Promoted From (URL) fields | All 5 new fields added. |
| **1.4** Audit clients_database | Add: Pipeline Stage, Deal Value, Close Date, Client Health, Last Contact, Next Action, Account Manager, NPS Score (30-day), NPS Score (90-day), NPS Category, Referral Asked, Referrals Given, Testimonial Status, Testimonial Quote fields | All 14 new fields added. Every existing client has Brand and Pipeline Stage filled. |
| **1.5** Audit projects_database | Add: Appetite, Pitch Status, Circuit Breaker Date, Scope Overrun, Client Success Definition fields | All 5 new fields added. |

#### Day 3 | Create 3 Missing Databases

**Owner:** OS Owner

**Time:** 3–4 hours

| Task | Action | Done When |
| --- | --- | --- |
| **1.6** Create KPI DB | Build kpi_database with: KPI Name, Brand, Department, Metric Type, Target, Actual, Period, Linked Projects, Linked Reports, Trend, Alert, Owner. Create filtered views: one per active brand (Next, Advisory, Nexus). | Database exists. 3 brand views created. At least 5 real KPIs entered per active brand. |
| **1.7** Create Experiments DB | Build experiments_database with: Experiment Name, Brand, Department, Hypothesis, Variable Tested, Result, Learning, Next Action, Linked SOP, Linked Knowledge. | Database exists. Template button created inside it for one-click new experiment. |
| **1.8** Create Tools DB | Build tools_database with: Tool Name, Brand (multi-select), Department (multi-select), Function, Linked SOPs, Status, Setup Guide, Cost, Owner. | Database exists. All current tools in use across all brands entered (aim for 15+ entries). |

#### Day 4–5 | Build the Weekly Scorecard (Improvement #1)

**Owner:** OS Owner + Brand Leads

**Time:** 4–5 hours

**Benchmark:** EOS — this is the single highest-impact thing EOS companies implement first.

| Task | Action | Done When |
| --- | --- | --- |
| **1.9** Create scorecard_database | Build with: Metric Name, Brand, Owner, Period, Weekly Target, This Week Actual, Status (Green/Yellow/Red), Trend (Improving/Stable/Declining), Week. | Database exists with filtered view per active brand. |
| **1.10** Populate Scorecard — Nivy Next | Enter 8–12 leading indicators. Examples: Cold emails sent / Reply rate / Qualified leads / Proposals sent / Deals closed / Projects delivered on time / Client satisfaction flag / Team tasks completed. | At least 8 metrics entered with real targets. Owner assigned to each. |
| **1.11** Populate Scorecard — Nivy Advisory | Enter 8–12 leading indicators. Examples: New client enquiries / Filings completed / Compliance reviews done / Overdue client items / Client NPS flag. | At least 8 metrics with real targets. Owner per metric. |
| **1.12** Populate Scorecard — Nivy Nexus | Enter 5–8 leading indicators. Examples: Outreach messages sent / Connections made / Community posts / Buyer-seller introductions / Active deals. | At least 5 metrics with real targets. |
| **1.13** Schedule Scorecard Review | Add "Update Scorecard" as a recurring weekly task in tasks_database for each brand's metric owner. Due: every Monday 9am. | Recurring tasks exist in tasks_database. First update done for the current week. |

---

### WEEK 2 — Issues DB, Cycle System & QC Checklists

#### Day 1–2 | Build the Issues DB with IDS Workflow (Improvement #2)

**Owner:** OS Owner

**Time:** 3–4 hours

**Benchmark:** EOS — issues that aren't logged don't get solved.

| Task | Action | Done When |
| --- | --- | --- |
| **2.1** Create issues_database | Build with: Issue Title, Brand, Department, Type (Short-Term/Long-Term/People), Identified By, Owner, Status (Open/In Discussion/Solved/Dropped), Resolution, Date Identified, Target Resolution Date. | Database exists with filtered view per active brand. |
| **2.2** Enter first batch of issues | From memory or a 20-min team brainstorm: log every known open issue across all active brands. Even 10 entries is a strong start. | At least 10 real issues logged. Every issue has Owner + Target Resolution Date. |
| **2.3** Add IDS section to meeting template | In the L10 Meeting template (built in Phase 2): add a linked view of issues_database showing Open issues sorted by Target Resolution Date. | IDS section exists in meeting template. Issues DB is embedded/linked. |

#### Day 2–3 | Implement 2-Week Cycle System (Improvement #22)

**Owner:** OS Owner + Nivy Next Lead

**Time:** 2–3 hours

**Benchmark:** Linear — the forcing function that creates shipping discipline.

| Task | Action | Done When |
| --- | --- | --- |
| **2.4** Add Cycle fields to tasks_database | Add Cycle (Select) and Cycle Status (Select) fields (already done in Day 1 audit — confirm here). Create an "Inbox" view: all tasks with Cycle = Inbox. Create "Current Cycle" view: Cycle = current cycle name. | Inbox view and Current Cycle view both exist and are named clearly. |
| **2.5** Run first Inbox triage | Open Inbox view. For every task: assign to Current Cycle, move to Backlog, or close. Nothing stays in Inbox. | Inbox view = 0 tasks. Every task is in a Cycle, Backlog, or Cancelled. |
| **2.6** Set Cycle Planning ritual | Add recurring task in tasks_database: "Cycle Planning — [Brand Name]" — due every other Monday. Owner: Brand Lead. The output of this task is: Current Cycle view populated for the next 2 weeks. | Recurring task exists. First cycle planned and current cycle view is populated. |

#### Day 3–5 | Build QC Checklists per Deliverable (Improvement #32)

**Owner:** Department Heads per brand

**Time:** 5–6 hours

**Benchmark:** Amazon/McDonald's — quality is a checklist, not a judgment call.

| Task | Action | Done When |
| --- | --- | --- |
| **2.7** Build QC Checklist — Cold Email Sequence (Nivy Next) | Create a Notion page template with full checklist: Personalization correct / No spam trigger words / CTA single and clear / Unsubscribe mechanism / Brand voice approved / Tracking links work / Sequence timing correct. | Template exists in Nivy Next SOP section. One real email sequence reviewed against it. |
| **2.8** Build QC Checklist — Client Tax Filing (Nivy Advisory) | Create checklist: Figures match source docs / Correct tax year / Correct jurisdiction / Reviewed by CPA / Client signature obtained / Filed within deadline / Filing reference number recorded. | Template exists in Nivy Advisory SOP section. Compliance lead has reviewed and approved it. |
| **2.9** Build QC Checklist — Weekly KPI Report (All brands) | Create universal checklist: All metrics present / Targets vs actuals shown / Trend arrow present / No calculation errors / Sent by deadline / Stored in reports_database. | Template exists in Nivy Global SOPs. Used for first weekly report. |
| **2.10** Build QC Checklist — New SOP (All brands) | Create checklist: 12-part structure complete / Tested by someone who didn't write it / Owner assigned / Brand + Department tagged / Linked to brand Index / Review cycle date set / RACI fields filled. | Template exists. Every SOP created from this point forward uses it before being marked Approved. |
| **2.11** Build QC Checklist — Website / Landing Page (Nivy Next) | Create checklist: Mobile-responsive / CTA above fold / Page speed >85 / No broken links / Meta title + description written / Analytics installed and verified / Legal pages linked. | Template exists. Dev lead has tested it against a live page. |
| **2.12** Build QC Checklist — Project Pitch (All brands) | Create checklist: All 7 sections complete / Appetite defined / Client success definition written / Rabbit holes identified / No-gos stated / Approved by Brand Lead before project starts. | Template exists. First pitch reviewed against it. |

---

# 🟡 PHASE 2 — Accountability & Governance

## Weeks 3–4 | ~20–25 hours | Maturity: 50% → 62%

> **Why second:** Once the scorecard is live and issues are being logged, the system needs accountability structure. Who decides what, who owns which outcome, and how are decisions recorded.
> 

---

### WEEK 3 — V/TO, Rocks, L10 Meeting & Decision Register

#### Day 1–2 | Build Vision/Traction Organizer per Active Brand (Improvement #5)

**Owner:** Founder / CEO

**Time:** 4–5 hours (1.5 hrs per brand)

**Benchmark:** EOS — the first thing every EOS company builds.

| Task | Action | Done When |
| --- | --- | --- |
| **3.1** Build V/TO — Nivy Next | Create one page under Nivy Next Division Home → Section 1 with: Core Values (3–5), Core Focus (purpose + niche), 10-Year Target, 3-Year Picture, 1-Year Plan, Quarterly Rocks (3–5 for Q2 2026), Marketing Strategy (target market, USP, proven process, guarantee). | Page exists. All 7 sections filled. Founder has reviewed and approved it. Shared with Nivy Next team. |
| **3.2** Build V/TO — Nivy Advisory | Same structure. Advisory-specific: include market focus (US/UK/UAE/AUS/Canada), service specialisation, client type. | Page exists. All 7 sections filled. Reviewed and approved. |
| **3.3** Build V/TO — Nivy Nexus | Same structure. Nexus-specific: UAE market focus, community model, buyer-seller positioning. | Page exists. All 7 sections filled. |

#### Day 3 | Build Quarterly Rocks / OKR Tracker (Improvement #6)

**Owner:** OS Owner

**Time:** 2–3 hours

**Benchmark:** EOS + OKR — the quarterly focus layer that sits between vision and weekly tasks.

| Task | Action | Done When |
| --- | --- | --- |
| **3.4** Create rocks_database | Build with: Rock Title, Brand, Quarter (Q1/Q2/Q3/Q4 2026), Owner, Status (On Track/Off Track/Done/Dropped), % Complete, Due Date. Create filtered view per brand per quarter. | Database exists. Q2 2026 Rocks entered for Nivy Next, Advisory, Nexus (3–5 per brand). Each Rock has one Owner. |

#### Day 4–5 | Build Level 10 Meeting Template (Improvement #7)

**Owner:** OS Owner

**Time:** 2–3 hours

**Benchmark:** EOS — the weekly meeting that makes every other system get used.

| Task | Action | Done When |
| --- | --- | --- |
| **3.5** Create L10 Meeting Template | Build as a Notion page template with sections: Segue (5 min) / Scorecard Review (5 min — linked scorecard view) / Rock Review (5 min — linked rocks view) / Customer & People Headlines (5 min) / To-Do Review (5 min) / IDS (60 min — linked issues view) / Conclude & Rate (5 min). Create one copy per active brand. | Template exists. First L10 meeting held for at least one active brand using the template. Meeting rated ≥7/10 by attendees. |
| **3.6** Schedule recurring L10 meetings | Add recurring tasks in tasks_database: "L10 Meeting — [Brand]" — weekly, same day/time, Owner = Brand Lead. First 4 meetings pre-scheduled. | Recurring tasks exist. First meeting completed for each active brand. |

---

### WEEK 4 — RACI on SOPs, Decision Register & Accountability Charts

#### Day 1–2 | Add RACI to All SOPs (Improvement #3)

**Owner:** Department Heads

**Time:** 4–6 hours (depends on number of SOPs)

**Benchmark:** RACI standard — Owner ≠ Accountable. Both must exist.

| Task | Action | Done When |
| --- | --- | --- |
| **4.1** Confirm RACI fields on sop_database | Verify Responsible (Person), Accountable (Person), Informed (Multi-person) fields exist (added in Phase 1 audit). | All 3 RACI fields confirmed present. |
| **4.2** Retroactively fill RACI on all existing SOPs | Open every SOP in sop_database. Fill Responsible + Accountable. For Informed, add anyone who needs to know when this SOP runs. Target: 100% of Active/Approved SOPs have RACI filled. | 0 Approved SOPs with empty Responsible or Accountable fields. |
| **4.3** Update 12-part SOP template | Add a RACI section to the standard SOP template so all future SOPs include it from creation. Section should show: Responsible (who executes), Accountable (who owns outcome + signs off), Consulted (who advises), Informed (who gets notified on completion). | SOP template updated. Next SOP created uses the updated template. |

#### Day 3 | Build Decision Register (Improvement #8)

**Owner:** OS Owner

**Time:** 2 hours

**Benchmark:** EOS — decisions not logged get re-litigated. Logged decisions become institutional memory.

| Task | Action | Done When |
| --- | --- | --- |
| **4.4** Create decision_database | Build with: Decision (Title), Brand, Made By (Person), Date, Context (Text), Outcome (Text), Status (Active/Superseded/Under Review), Linked SOP (Relation). Place in Nivy Global OS section. | Database exists. At least 10 historical key decisions retroactively logged from memory. |

#### Day 4–5 | Build Accountability Charts per Brand (Improvement #15)

**Owner:** Founder / CEO + Brand Leads

**Time:** 3–4 hours

**Benchmark:** EOS — different from an org chart. Defines what success looks like in each seat.

| Task | Action | Done When |
| --- | --- | --- |
| **4.5** Build Accountability Chart — Nivy Next | Create one page per brand: list every active seat. For each seat: Seat Name / Current Person / Core Responsibilities (max 5) / 3 Measurable Outcomes that define success in this seat. Place under Division Home → Section 1. | Page exists for Nivy Next. Every filled seat has 3 measurable outcomes defined. Founder has approved. |
| **4.6** Build Accountability Chart — Nivy Advisory | Same. Advisory seats include: Managing CPA, Tax Compliance Lead, Client Onboarding Coordinator, Bookkeeping Lead. | Page exists. All Advisory seats defined. |
| **4.7** Build Accountability Chart — Nivy Nexus | Same for Nexus active seats. | Page exists. All Nexus seats defined. |
| **4.8** Create OS Changelog DB (Improvement #34) | Build os_changelog_database: Change Title, Date, Changed By, Change Type, What Changed, Why It Changed, Impact, Rollback Plan. First entry: log everything done in Phases 1–2. | Database exists. Phase 1–2 changes logged as first entries. New policy: any OS schema change must be logged here. |

---

# 🟠 PHASE 3 — Revenue & Client Intelligence

## Weeks 5–6 | ~20–25 hours | Maturity: 62% → 72%

> **Why third:** Once you know who's accountable for what and you have a weekly traction rhythm, you need to see the money. Revenue intelligence is what turns an operating system into a business system.
> 

---

### WEEK 5 — CRM Pipeline, Client NPS & VoC Database

#### Day 1–2 | Build CRM Pipeline View (Improvement #4)

**Owner:** Sales Lead per brand

**Time:** 3–4 hours

**Benchmark:** Landmark OS — a Kanban pipeline on clients_database.

| Task | Action | Done When |
| --- | --- | --- |
| **5.1** Confirm Pipeline fields on clients_database | Verify Pipeline Stage, Deal Value, Close Date, Client Health, Last Contact, Next Action, Account Manager fields exist (added in Phase 1). | All 7 fields confirmed. Every client has Pipeline Stage filled. |
| **5.2** Create CRM Kanban view — Nivy Next | Create a Kanban view on clients_database grouped by Pipeline Stage, filtered for Brand = Nivy Next. Columns: Prospect / Qualified / Proposal Sent / Negotiating / Won / Lost / Churned. | Kanban view exists. All Nivy Next prospects and clients correctly staged. |
| **5.3** Create CRM Kanban view — Nivy Advisory | Same for Advisory. Adapt stages to Advisory context: Enquiry / Onboarding / Active / Renewal / Churned. | Kanban view exists for Advisory. |
| **5.4** Create CRM Kanban view — Nivy Nexus | Same for Nexus. | Kanban view exists for Nexus. |

#### Day 3–4 | Build Client NPS & Raving Fan System (Improvement #28)

**Owner:** Account Managers per brand

**Time:** 3–4 hours

**Benchmark:** Tony Robbins — satisfied clients stay. Raving fans refer.

| Task | Action | Done When |
| --- | --- | --- |
| **5.5** Confirm NPS fields on clients_database | Verify NPS Score (30-day), NPS Score (90-day), NPS Category, Referral Asked, Referrals Given, Testimonial Status, Testimonial Quote fields exist. | All 7 NPS fields confirmed. |
| **5.6** Build NPS Collection SOP | Write a 6-part SOP: "How to Collect Client NPS." Steps: (1) At 30 days post-onboarding, send NPS question via email. (2) Log score in clients_database. (3) If 9–10: trigger Referral Ask task. (4) If 0–6: trigger Escalation task. (5) At 90 days, repeat. (6) At renewal, repeat. | SOP exists in sop_database tagged Brand = All / Department = Operations. RACI filled. Approved. |
| **5.7** Run first NPS collection | Identify all active clients across Next, Advisory, Nexus who have been onboarded for 30+ days. Send NPS question to each. Log scores. | At least 80% of eligible clients have an NPS score logged. Tasks created for all Promoters (referral ask) and Detractors (escalation call). |

#### Day 5 | Build Voice of Customer Database (Improvement #29)

**Owner:** OS Owner + Marketing Lead

**Time:** 2–3 hours

**Benchmark:** Tony Robbins — real client language is the most powerful marketing asset.

| Task | Action | Done When |
| --- | --- | --- |
| **5.8** Create voc_database | Build with: Quote (Title — exact client words), Brand, Service, Type (Testimonial/Objection/Complaint/Suggestion/Win), Source, Date, Used In, Client (Relation → clients_database). | Database exists. At least 20 real client quotes/objections entered from memory, WhatsApp, and email archives. |
| **5.9** Link VoC to Marketing & Sales hubs | Add a linked filtered view of voc_database (Type = Testimonial) to each brand's Marketing Hub page. Add a view (Type = Objection) to each brand's Sales Hub page. | Views exist in both hubs per brand. Sales team can access objections. Marketing can access testimonials. |

---

### WEEK 6 — Revenue Forecast, Unit Economics & Cross-Brand Practice Hubs

#### Day 1–2 | Revenue Forecast Tracker (Improvement #10)

**Owner:** Finance Lead / Founder

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **6.1** Create revenue_forecast_database | Build with: Month (Date), Brand (Select), Projected Revenue (Number), Actual Revenue (Number), Variance (Formula: Actual - Projected), Key Driver (Text — what caused variance), Owner (Person). Create view per brand. | Database exists. Last 3 months entered retrospectively for each active brand. Current month projection entered. |

#### Day 3 | Unit Economics Tracker (Improvement #30)

**Owner:** Founder / Finance Lead

**Time:** 2 hours

| Task | Action | Done When |
| --- | --- | --- |
| **6.2** Create unit_economics_database | Build with: Service/Product Name, Brand, Average Deal Value, CAC, LTV, LTV:CAC Ratio (Formula), Gross Margin %, Payback Period (Formula), Last Updated, Health (Green/Yellow/Red). One row per service line per brand. | Database exists. At least 2 service lines per active brand entered with real or estimated numbers. Health status visible immediately. |

#### Day 4–5 | Cross-Brand Practice Hubs (Improvement #9)

**Owner:** Marketing Lead + Sales Lead

**Time:** 3–4 hours

**Benchmark:** Spotify Guilds — cross-team knowledge sharing.

| Task | Action | Done When |
| --- | --- | --- |
| **6.3** Build Marketing Practice Hub | Create a page in Nivy Global with sections: Top Performing Assets (linked view from templates_database filtered by Use Case = Marketing + Performance = High) / This Month's Learnings / Experiments (linked from experiments_database) / Cross-Brand SOP Links / Monthly Practice Meeting Notes. | Page exists with all 5 sections. At least 3 entries in each section. |
| **6.4** Build Sales Practice Hub | Same structure. Sales-specific: Top Scripts, Top Objection Responses (linked from voc_database Type = Objection), Win/Loss Learnings, Experiments, Outreach Templates. | Page exists with all sections. Sales teams from Next, Advisory, Nexus are all aware of it. |
| **6.5** Schedule monthly Practice meetings | Add recurring monthly tasks: "Marketing Practice Meeting — all brands" (30 min) and "Sales Practice Meeting — all brands" (30 min). Owner: respective Practice Lead. Output: one new entry in the Learnings section of each hub. | Recurring tasks exist. First meeting scheduled. |

---

# 🟠 PHASE 4 — Strategic Intelligence

## Weeks 7–8 | ~15–20 hours | Maturity: 72% → 80%

> **Why fourth:** With revenue visibility and traction rhythm in place, Nivy can now look outward — at competitors, markets, and scenarios — and make strategic decisions based on data, not instinct.
> 

---

### WEEK 7 — Competitor Intelligence & Scenario Planning

#### Day 1–3 | Build Competitor Intelligence Database (Improvement #24)

**Owner:** Brand Leads + Marketing Leads

**Time:** 4–5 hours

| Task | Action | Done When |
| --- | --- | --- |
| **7.1** Create competitor_intelligence_database | Build with: Competitor Name, Brand it Competes With, Market, Category (Direct/Indirect/Aspirational), Pricing, Key Differentiators, Our Advantage, Their Weakness, Recent Moves, Last Updated, Update Owner. Create views: by Brand, by Market. | Database exists. At least 5 competitors per active brand entered (minimum 15 total entries). Every entry has Our Advantage filled. |
| **7.2** Link to Division Homes | Add a linked view (filtered by Brand) to each brand's Division Home under a "Competitive Landscape" section. | Each brand's Division Home has a Competitive Landscape section with its relevant filtered view. |
| **7.3** Assign monthly update owners | For each competitor entry: assign an Update Owner. Add recurring monthly task in tasks_database: "Update Competitor Intel — [Competitor Name]" due first Monday of every month. | Every competitor entry has an Update Owner. Recurring tasks exist for all entries. |

#### Day 4–5 | Build Scenario Plans per Active Brand (Improvement #25)

**Owner:** Founder / Brand Leads

**Time:** 4–5 hours (~1.5 hrs per brand)

| Task | Action | Done When |
| --- | --- | --- |
| **7.4** Write Scenario Plan — Nivy Next | Create page under Nivy Next Division Home → Section 1. Complete: Base Case (revenue assumption, team, key risks, key opportunities, top 3 priorities) / Best Case (what must go right, how to accelerate) / Worst Case (what could cause it, contingency actions, tripwire metric). Review quarterly. | Page exists. All 3 scenarios have revenue assumption + action priorities filled. Founder has approved. |
| **7.5** Write Scenario Plan — Nivy Advisory | Same structure. Advisory-specific risks: regulatory changes per market, CPA capacity constraints, client concentration risk. | Page exists. All 3 scenarios complete. |
| **7.6** Write Scenario Plan — Nivy Nexus | Same structure. Nexus-specific risks: UAE market dynamics, platform competition, community engagement. | Page exists. All 3 scenarios complete. |

---

### WEEK 8 — Communication Protocol, Error Log & Idea Bank

#### Day 1–2 | Communication Protocol & Async System (Improvement #23)

**Owner:** OS Owner + All Brand Leads

**Time:** 3–4 hours

| Task | Action | Done When |
| --- | --- | --- |
| **8.1** Write Communication Protocol page | Create "How We Communicate at Nivy" in Nivy Global. Define: what goes in Notion vs. WhatsApp vs. email vs. meeting, response time expectations per channel, async-first principles, and the rule: "if it's not in Notion, it didn't happen" for SOPs and decisions. | Page exists. Reviewed and approved by all Brand Leads. Shared with every team member. |
| **8.2** Create weekly_checkin_database | Build with: Person, Brand, Week (Date), Completed This Week (Text), Working On Next Week (Text), Blockers (Text), Morale (Green/Yellow/Red). Create per-brand filtered views. | Database exists. First weekly check-in completed by all active team members. |
| **8.3** Replace status meetings with check-in | Cancel any recurring status meetings that exist. The weekly check-in DB replaces them. Only L10 meetings remain as regular team touchpoints. | No standing status meetings. L10 is the only recurring team meeting per brand. |

#### Day 3 | Build Structured Error Log (Improvement #33)

**Owner:** OS Owner

**Time:** 1–2 hours

| Task | Action | Done When |
| --- | --- | --- |
| **8.4** Create error_log_database | Build with: Error Title, Brand, Department, Date Occurred, Cost of Error, Root Cause, Root Cause Detail, Fix Applied, Prevention Change, Linked SOP (Relation → sop_database), Resolved (Checkbox). Place in Nivy Global → Operations section. | Database exists. At least 5 historical errors entered from memory. New policy: every error is logged within 24 hours of discovery. |

#### Day 4–5 | Build Idea Bank & Innovation Pipeline (Improvement #31)

**Owner:** OS Owner + all team members

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **8.5** Create idea_bank_database | Build with: Idea Title, Submitted By, Brand, Category, Problem It Solves, Estimated Impact, Estimated Effort, Status (Submitted/Under Review/Promoted/Rejected/Parked), Date Submitted, Review Notes. Create a submission view (Status = Submitted). | Database exists. Every team member has been told to use it. At least 10 ideas entered as first batch. |
| **8.6** Schedule Monthly Innovation Review | Add recurring monthly task: "Innovation Review — all brands" (30 min). Owner: Founder. Output: top 1–2 ideas promoted to Pitch Status in projects_database. All others: Parked or Rejected with note. | Recurring task exists. First Innovation Review scheduled. |

---

# 🟡 PHASE 5 — People, Training & Culture

## Weeks 9–10 | ~15–20 hours | Maturity: 80% → 87%

> **Why fifth:** With traction, accountability, and revenue systems running, people systems can be built correctly — because now there's something for people to be onboarded into and evaluated against.
> 

---

### WEEK 9 — Role Scorecards, Training Tracker & SOP Version History

#### Day 1–2 | Build Role Scorecards (Improvement #26)

**Owner:** Founder + Brand Leads

**Time:** 4–5 hours

**Benchmark:** Netflix Keeper Test — define what excellent looks like before evaluating against it.

| Task | Action | Done When |
| --- | --- | --- |
| **9.1** Create role_scorecards_database | Build a private database (restricted view) with: Role Title, Brand, Seat Mission, Core Outcomes (text — 3–5 measurable results), Competencies Required, Core Values Fit, Performance Thresholds (Excellent/Meets/Below), Keeper Test Question. Link to HR Hub. | Database exists. At least one scorecard per active seat per brand. Founder has reviewed all. |
| **9.2** Write Role Scorecard — Nivy Next Sales Lead | Complete all fields. Core Outcomes must be measurable: e.g. "20 qualified leads/week", "80% proposal-to-call conversion", "2 deals closed/month". | Scorecard complete. Seat occupant has read and agreed to outcomes. |
| **9.3** Write scorecards for all other active seats | Same for every filled seat across Next, Advisory, Nexus. Priority order: Sales → Operations → Marketing → Delivery → Compliance. | Every filled seat has a scorecard. All outcome metrics are numbers, not descriptions. |

#### Day 3 | Add SOP Version History & Change Log (Improvement #12)

**Owner:** OS Owner

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **9.4** Create sop_change_log sub-structure | Add a "Change Log" toggle section at the bottom of every SOP template. Columns: Version / Date / Changed By / What Changed / Why. Update existing core SOPs (top 10 most-used) retroactively with Version 1.0 entry. | Change Log section present in SOP template. All core SOPs have at least a v1.0 entry. New policy: every SOP update requires a change log entry. |

#### Day 4–5 | Build Training Completion Tracker (Improvement #14)

**Owner:** HR Lead / OS Owner

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **9.5** Create training_tracker_database | Build with: Person (Person), Brand, Module Name (Text), Linked Knowledge Entry (Relation → knowledge_database), Completion Status (Not Started/In Progress/Complete), Completion Date, Score (optional). Create per-person and per-brand views. | Database exists. All current team members entered. Completion status filled for any training already done. |

---

### WEEK 10 — Role-Specific Onboarding Tracks & eNPS

#### Day 1–3 | Build Role-Specific Onboarding Tracks (Improvement #11)

**Owner:** HR Lead + Brand Leads

**Time:** 5–6 hours

**Benchmark:** EOS + best practice — one generic track teaches nothing about the actual role.

| Task | Action | Done When |
| --- | --- | --- |
| **10.1** Build Onboarding Track — Nivy Next: Sales/Outreach Role | Create a page with Day 1–7 checklist. Each day: what to read (links to knowledge_database), what to do (linked tasks), what to produce (first output). Day 1: read brand V/TO, Accountability Chart, Communication Protocol. Day 2: read top 5 Sales SOPs. Day 3: shadow a live outreach session. Day 4: first own outreach attempt. Day 5: QC review of Day 4 output. Day 6–7: full execution with support. Completion tracked in training_tracker_database. | Page exists. One new joiner has completed it and rated it. Ambiguities fixed based on their feedback. |
| **10.2** Build Onboarding Track — Nivy Advisory: Compliance/Tax Role | Day 1–7 for compliance officer. Day 1: Nivy Advisory V/TO, compliance SOP library. Day 2: jurisdiction-specific guide. Day 3: shadow a client filing. Days 4–5: complete a test case filing. Day 6: QC review. Day 7: sign-off. | Page exists. Reviewed by Advisory Managing CPA and approved. |
| **10.3** Build Onboarding Track — Universal (all brands) | Day 1 only (before any brand track begins): Nivy Global overview, core values, communication protocol, workspace navigation guide, naming conventions, how to use tasks_database. | Universal Day 1 track exists. All future joiners start here before their brand-specific track. |

#### Day 4–5 | Quarterly Employee Pulse Check Setup (Improvement #27)

**Owner:** HR Lead / Founder

**Time:** 1–2 hours

| Task | Action | Done When |
| --- | --- | --- |
| **10.4** Create pulse_check_database | Build with: Quarter (Select), Brand, Score (0–10 Number), Strength (Text — what to continue), Improvement (Text — what to change). No person field — anonymous. Create a form (Typeform or [Tally.so](http://Tally.so)) linked to this database. | Database exists. Form link shared with all team members. First pulse check responses collected. |
| **10.5** Schedule quarterly pulse check | Add recurring quarterly task: "Send eNPS Pulse Check — all brands" (due first week of each quarter). Owner: HR Lead. Output: results reviewed in quarterly planning session. | Recurring task exists. Results from first pulse check reviewed and key themes noted. |

---

# 🟣 PHASE 6 — Cross-Brand Intelligence & Meeting Rhythm Completion

## Week 11 | ~10–12 hours | Maturity: 87% → 90%

> **Why sixth:** The final structural layer before automation. This phase completes the navigation system, the OS health check, and the Project Pitch workflow — tying all previous phases together into one coherent system.
> 

---

#### Day 1 | Build Project Pitch Template (Improvement #21)

**Owner:** OS Owner

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **11.1** Create Project Pitch Notion template | Build as a Notion page template with 7 sections: (1) The Problem, (2) The Appetite, (3) The Solution Sketch, (4) Rabbit Holes, (5) No-Gos, (6) Success Definition — from client's perspective, (7) Approval block. Apply to projects_database as a page template. | Template exists and is accessible inside projects_database. New projects can be created using this template with one click. |
| **11.2** Backfill Pitches for active projects | For every project currently In Progress: complete a Pitch retrospectively. Fill Appetite, Client Success Definition, Pitch Status = Approved. | All active projects have Pitch Status = Approved. No project is In Progress with Pitch Status = Not Written. |

#### Day 2–3 | Notion Template Buttons for One-Click Page Generation (Improvement #13)

**Owner:** OS Owner

**Time:** 3–4 hours

| Task | Action | Done When |
| --- | --- | --- |
| **11.3** Create template buttons in sop_database | Add Notion template buttons (native feature) that auto-generate a full SOP page pre-filled with: 12-part structure, all property fields defaulted to correct values, RACI section, Change Log toggle at bottom, QC Checklist link placeholder. | Template button exists. Creating a new SOP via button produces a fully structured page in under 5 seconds. |
| **11.4** Create template buttons in knowledge_database | Auto-generate: Knowledge page with standard sections (Overview, Key Concepts, Examples, Related SOPs, Prerequisites, Next Learning). | Template button exists and works. |
| **11.5** Create template buttons in experiments_database | Auto-generate: Experiment page with sections (Hypothesis, Control, Variable, Measurement Method, Results, Learning, Next Action). | Template button exists and works. |

#### Day 4–5 | Quarterly OS Health Check Scorecard (Improvement #35)

**Owner:** OS Owner

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **11.6** Build OS Health Check Template | Create a Notion page template with 4 sections: Data Quality (% fill rates per database), SOPs (overdue reviews, drafts, missing RACI), Navigation (3-click test, dead-ends, broken links), Usage (Scorecard updates, L10 meetings held, Rocks reviewed, ChatGPT processed). Scoring: 1 point per pass. 20-point max. Green: 17+, Yellow: 12–16, Red: <12. | Template exists. First OS Health Check run. Score logged. Actions for anything below Green assigned as tasks in tasks_database. |

---

# ⚙️ PHASE 7 — Automation & Self-Sustaining Systems

## Week 12+ | ~15–20 hours | Maturity: 90% → 92%

> **Why last:** Automation wires the clean, tested system together. Automating a messy system creates automated mess. This phase should only begin when Phases 1–6 are complete and the OS Health Check scores Green.
> 

---

#### Day 1–2 | Notion Native Automations

**Owner:** OS Owner + Technology Lead

**Time:** 3–4 hours

| Automation | Trigger | Action | Done When |
| --- | --- | --- | --- |
| **12.1** Task QC enforcement | Task Status changed to "Done" | If QC Status ≠ "Approved": revert Status to "In QC" and notify Owner | Automation active. Test: try to mark a task Done without QC Approved — it bounces back. |
| **12.2** SOP review reminder | SOP Last Updated date = 30 days before Review Cycle date | Create task for Owner: "Review SOP — [SOP Name]" due = Review Cycle date | Automation active. At least one review task auto-created in the first week. |
| **12.3** KPI Alert notification | KPI Alert checkbox = checked (manually set by metric owner) | Create task for Brand Lead: "KPI Alert — [Metric Name] below threshold" | Automation active. Test: check the Alert box on a KPI — task appears for Brand Lead. |
| **12.4** Issue escalation | Issue Target Resolution Date = today, Status ≠ Solved | Create task for Issue Owner: "Overdue Issue — [Issue Title]" | Automation active. First overdue issue triggers escalation task. |
| **12.5** Client NPS Promoter → Referral Ask | NPS Category set to "Promoter" | Create task for Account Manager: "Referral ask — [Client Name] within 48 hours" | Automation active. Test: set a client to Promoter — referral task appears. |
| **12.6** Client NPS Detractor → Escalation | NPS Category set to "Detractor" | Create task for Department Head: "Escalation call — [Client Name] within 24 hours" | Automation active. Test: set a client to Detractor — escalation task appears. |

#### Day 3–4 | [Make.com](http://Make.com) / Zapier Automations (complex triggers)

**Owner:** Technology Lead

**Time:** 5–6 hours

| Automation | Trigger | Action | Done When |
| --- | --- | --- | --- |
| **12.7** ChatGPT conversation → Processing queue | New entry in ChatGPT conversations DB | Set Promotion Status = "Raw", create task for Research Processor: "Tag and file ChatGPT conversation — [Title]" | Every new ChatGPT conversation auto-creates a processing task. Inbox never accumulates more than 7 days. |
| **12.8** Weekly department head review tasks | Every Monday 8am | Auto-create task for each Brand Lead: "Weekly review — update Scorecard, review Issues, check Rocks" | Automation active. Tasks appear every Monday before 9am. |
| **12.9** Cycle end review trigger | Every 2nd Friday | Create task for Nivy Next Lead: "Cycle end review — check all Cycle tasks, mark Shipped/Carried Over/Killed" | Automation active. Cycle review task appears every 2 weeks. |
| **12.10** Monthly competitor intel update | First Monday of each month | Create tasks for all Update Owners in competitor_intelligence_database | Automation active. Competitor update tasks appear every month without manual creation. |

#### Day 5 | Phase 7 Final QA

**Owner:** OS Owner

**Time:** 2–3 hours

| Task | Action | Done When |
| --- | --- | --- |
| **12.11** Run full OS Health Check | Open the OS Health Check template. Run every check. Score the OS. | Score = 17+ (Green). Any failures assigned as tasks with owner and deadline. |
| **12.12** 3-click test for all content types | Starting from Nivy HQ: can you reach an SOP in 3 clicks? A knowledge page? A client record? A task? A KPI? A competitor? An issue? | All 7 content types reachable in 3 clicks. Any that fail get navigation fixed immediately. |
| **12.13** Dead-end audit | Review any page with no forward links. Every page must have at least one link to another page and one link back to its parent section. | 0 dead-end pages found in active sections of the workspace. |
| **12.14** Log Phase 7 in OS Changelog | Record all automations built and all QA results in os_changelog_database. | Changelog updated. Phase 7 entry exists with all automation names and outcomes. |

---

# ⚪ PHASE 8 — Future State (Q3 2026+)

## Improvements #36–40 | ~15–20 hours when activated

> These improvements are not time-pressured. Activate them when the relevant business capability is being built.
> 

| # | Improvement | Activate When | Est. Time |
| --- | --- | --- | --- |
| 36 | Partner / Franchise Performance Scorecard | First franchise or formal partner agreement signed | 2 hours |
| 37 | Market Expansion Readiness Checklist | Before entering any new geography (e.g. Advisory expanding to new US state or EU) | 2 hours |
| 38 | Legal & Compliance Risk Register | When Nivy Advisory crosses 50 active clients or enters a new jurisdiction | 2–3 hours |
| 39 | Brand Health Tracker (share of voice, NPS by market) | When marketing spend exceeds $5k/month per brand — tracking ROI becomes essential | 2 hours |
| 40 | AI-Assisted Research Pipeline (auto-classify ChatGPT → correct DB) | When ChatGPT conversations DB exceeds 200 unprocessed entries | 8–12 hours |

---

# 🗓️ Full Timeline Summary

| Week | Focus | Key Outputs | Hours |
| --- | --- | --- | --- |
| **Week 1** | Database upgrades + Scorecard | 5 databases upgraded, 3 new DBs created, live scorecard with real metrics | 13–17 hrs |
| **Week 2** | Issues DB + Cycles + QC Checklists | Issues DB live, first Inbox triage done, 5+ QC checklists built | 12–15 hrs |
| **Week 3** | V/TO + Rocks + L10 Meeting | 3 brand V/TOs, Q2 Rocks entered, first L10 meeting held | 10–13 hrs |
| **Week 4** | RACI + Decision Register + Accountability Charts | RACI on all active SOPs, Decision Register with 10+ entries, Charts for 3 brands, OS Changelog live | 10–12 hrs |
| **Week 5** | CRM Pipeline + Client NPS + VoC | 3 Kanban pipelines, NPS collected from all active clients, 20+ VoC entries | 10–12 hrs |
| **Week 6** | Revenue Forecast + Unit Economics + Practice Hubs | Revenue tracker with 3 months retrospective, unit economics per service line, 2 practice hubs live | 9–11 hrs |
| **Week 7** | Competitor Intel + Scenario Plans | 15+ competitors tracked, 3 scenario plans written and approved | 9–11 hrs |
| **Week 8** | Comms Protocol + Error Log + Idea Bank | Communication Protocol adopted by all, error log live with 5+ entries, idea bank with 10+ ideas | 7–9 hrs |
| **Week 9** | Role Scorecards + SOP Versions + Training Tracker | Scorecard per active seat, version history on all core SOPs, training tracker live | 9–11 hrs |
| **Week 10** | Onboarding Tracks + Pulse Check | 2+ role-specific onboarding tracks, universal Day 1 track, first eNPS collected | 7–9 hrs |
| **Week 11** | Project Pitch + Template Buttons + OS Health Check | Pitch template live and used, 3 template buttons built, first OS Health Check run | 8–10 hrs |
| **Week 12** | Automations + Final QA | 6 Notion automations + 4 Make/Zapier automations live, OS scores Green on health check | 10–12 hrs |

**Total: ~118–142 hours across 12 weeks**

---

# ✅ Master Checklist — All 40 Improvements

> Tick these off as each improvement is fully implemented (Done When criterion met — not just started).
> 

| Done? | # | Improvement | Phase | Week |
| --- | --- | --- | --- | --- |
| [ ] | 1 | Weekly Scorecard per Active Brand | 1 | 1 |
| [ ] | 2 | Issues DB with IDS Workflow | 1 | 2 |
| [ ] | 3 | RACI Fields on All SOPs | 2 | 4 |
| [ ] | 4 | CRM Pipeline View | 3 | 5 |
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
| [ ] | 15 | Accountability Chart per Brand | 2 | 4 |
| [ ] | 16 | Client Health Score System | 3 | 5 |
| [ ] | 17 | People Analyzer (EOS) | 5 | 9 |
| [ ] | 18 | "How We Work at Nivy" Playbook | 4 | 8 |
| [ ] | 19 | SOP Testing Protocol | 5 | 9 |
| [ ] | 20 | Quarterly Business Review (QBR) Template | 6 | 11 |
| [ ] | 21 | Project Pitch / Working Backwards Template | 6 | 11 |
| [ ] | 22 | 2-Week Cycle System | 1 | 2 |
| [ ] | 23 | Communication Protocol & Async System | 4 | 8 |
| [ ] | 24 | Competitor Intelligence Database | 4 | 7 |
| [ ] | 25 | Annual Scenario Plans per Brand | 4 | 7 |
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

# 🔥 The One Rule That Governs This Plan

> **A task is not done when it is built. It is done when the Done When criterion is met.**
> 

Building a database takes 30 minutes. Filling it with real data, assigning owners, and using it in the first real workflow — that's the other 3 hours. Every Done When criterion in this plan specifies the first real use, not just the creation.

The difference between a 30%-mature OS and a 92%-mature OS is not the number of pages. It's how many of those pages are used every week.

---

*Master Implementation Plan | Built by Claude | May 2026 | Version 1.0*

*Based on: World-Class OS Comparison V1.0 (Improvements #1–20) + Extended Benchmark Analysis V2.0 (Improvements #21–40)*