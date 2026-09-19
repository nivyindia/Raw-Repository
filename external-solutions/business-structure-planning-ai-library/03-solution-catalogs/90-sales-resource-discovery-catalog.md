# Sales Resource Discovery Catalog — Complete International Sales Department

**Status:** v1.0 — 2026-09-16  
**Purpose:** Resource discovery against the complete Sales Department operating model in `89-complete-international-sales-department-operating-model.md`.

## Research basis

The discovery scope is intentionally broader than CRM/pipeline management. Current sales-operations frameworks explicitly include metrics/analytics, territory planning, quota setting, incentive/compensation, enablement, forecasting, sales strategy, capacity planning, account planning, partner channels and performance management. APQC also separates sales strategy/forecasting, sales plans, lead/opportunity management, customer/account management and sales-order management. citeturn0search0turn0search1turn1search0turn1search15

## 1. Complete Sales capability → resource search matrix

| Layer | Capabilities to discover | Resource types to find | Priority |
|---|---|---|---|
| Executive | CRO/Head of Sales operating model | frameworks, dashboards, AI copilot, SOPs | P0 |
| Strategy | sales strategy, GTM, segmentation, ICP, TAM/SAM/SOM | frameworks, templates, skills, agents | P0 |
| Planning | annual/quarterly/monthly sales plans | planners, templates, AI planning agents | P0 |
| Objectives | company → revenue → sales → team → role → individual goal cascade | OKR/KPI/KRA systems, goal software, agents | P0 |
| Organization | sales hierarchy, role architecture, spans/layers, RACI | org-design frameworks, HR skills, templates | P0 |
| Roles | SDR/BDR/AE/SE/AM/KAM/CS/channel/revops/sales ops | JDs, competency models, skills, agents | P0 |
| KRA/KPI | KRAs, KPIs, targets, leading/lagging/activity/outcome metrics | KPI libraries, dashboards, scorecards | P0 |
| Quota | quota methodology, allocation, attainment | quota planning tools, models, templates | P0 |
| Capacity | headcount, ramp, productivity, coverage | capacity models, workforce planning | P0 |
| Territory | geographic, vertical, named-account, segment, country | territory planning tools/models | P0 |
| Compensation | commission, accelerators, SPIFs, clawbacks, disputes | comp systems, calculators, policies | P0 |
| Market | market/competitor/customer intelligence | research agents, skills, data tools | P0 |
| Acquisition | web, directories, social, databases, events, partners | scrapers, APIs, agents, MCPs | P0 |
| Lead management | capture, normalize, enrich, dedupe, verify, score, route | agents, workflows, CRM systems | P0 |
| Prospecting | outbound/inbound/multi-channel/social selling | agents, sequences, skills | P0 |
| Qualification | BANT/MEDDICC/MEDDPICC/CHAMP/SPICED etc. | skills, scorecards, agents | P0 |
| Discovery | discovery calls, pain, requirements, stakeholders | call skills, agents, templates | P0 |
| Solution selling | solution design, technical discovery, demos, POC/trial | SE skills, agents, demo systems | P0 |
| Opportunity | stage gates, exit criteria, deal health, next action | CRM, agents, playbooks | P0 |
| Account planning | strategic/enterprise account plans, MAPs | account-plan skills, templates, agents | P0 |
| Proposal | proposal, SOW, business case, ROI | proposal generators, templates, CPQ | P0 |
| RFP/RFQ/Bid | tender discovery, qualification, response, compliance matrix | bid agents, document systems | P0 |
| Pricing | price books, packaging, discounting | pricing/CPQ systems, skills | P0 |
| CPQ | configure, price, quote, approval | CPQ, quote builders, workflows | P0 |
| Deal desk | discount approvals, commercial/legal/finance review | deal desk workflows, approval engines | P0 |
| Negotiation | commercial/legal negotiation | skills, playbooks, AI assistants | P0 |
| Closing | close plans, signatures, order capture | CLM/e-sign/order workflows | P0 |
| Handoff | sales → delivery/implementation/CS | handoff agents, checklists, integrations | P0 |
| Forecast | pipeline, weighted, commit, best case, risk, historical | forecasting tools, agents, models | P0 |
| Performance | quota attainment, conversion, productivity, cycle, win rate | dashboards, BI, agents | P0 |
| Coaching | rep coaching, call coaching, deal coaching | enablement skills, conversation intelligence | P0 |
| Enablement | onboarding, certification, playbooks, battlecards | skills, knowledge bases, LMS | P0 |
| QA | call/deal/process QA, stage compliance | QA agents, scorecards, audit systems | P1 |
| Channel | reseller, referral, alliance, distributor, partner | PRM, partner skills, workflows | P1 |
| Account management | key accounts, relationship maps, stakeholder coverage | KAM systems, account agents | P0 |
| Expansion | cross-sell, upsell, whitespace, usage triggers | expansion agents, signals | P0 |
| Renewal | renewal forecast, risk, commercial renewal | renewal agents, CS/CRM workflows | P0 |
| Advocacy | NPS/CSAT, references, reviews, testimonials, referrals, champions | advocacy systems, agents, programs | P0 |
| Sales analytics | funnel, cohort, velocity, attribution, win/loss | BI, semantic layers, analytics agents | P0 |
| RevOps | process, systems, data, governance, automation | RevOps OS, agents, MCPs | P0 |
| Sales governance | approvals, SoD, compliance, audit, data quality | policy engines, controls, QA | P0 |
| Continuous improvement | experimentation, win/loss, process mining, benchmarking | research/optimization agents | P1 |
| International | country packs, currencies, languages, local sales practices, privacy | country packs, localization skills | P0 |
| Commercial lifecycle | quote → contract → order → delivery → billing → renewal | quote/CLM/O2C/revenue systems | P0 |

## 2. High-value reusable resources discovered

| ID | Resource | What it contributes | Type | Source |
|---|---|---|---|---|
| SR-001 | Agent Skills Collection — Sales | sales strategy, discovery, demos, objections, proposals, pipeline, enablement, account management, prospecting, qualification, playbooks, MEDDICC, MAPs, pricing, competitive selling, enterprise deals, coaching, CRM hygiene, forecast accuracy, channel sales, renewal/upsell, social selling, compensation | 24 reusable skills | https://github.com/itsual/agent-skills-collection |
| SR-002 | Enablement Skills | 37 revenue-enablement skills plus systems/playbooks for context, planning, onboarding, certification, coaching, account work, messaging, launches, KPI/measurement, CRM, renewals, conversation intelligence | Skills + playbooks | https://github.com/nthnclrk/enablement-skills |
| SR-003 | GitHub Awesome Copilot — Enterprise Account Planning | enterprise account planning, MEDDICC, deal health, mutual action plans | Agent skill | https://github.com/github/awesome-copilot/blob/main/skills/gtm-enterprise-account-planning/SKILL.md |
| SR-004 | Claude-Skills Account Executive | pipeline, discovery, demos, negotiation, closing, account plans, MEDDIC and forecasting | Agent skill | https://github.com/borghei/Claude-Skills/blob/main/sales-success/account-executive/SKILL.md |
| SR-005 | Open CRM | contacts, companies, deals, tasks, configurable pipelines, probability forecasting, activity/velocity, handoff, health, renewal tasks, data quality, audit | Open-source CRM | https://github.com/aeml/open_crm |
| SR-006 | Horilla CRM | leads, opportunities, campaigns, forecasting, dashboards, activity, multilingual/multi-currency and audit trail | Open-source CRM | https://github.com/horilla-opensource/horilla-crm |
| SR-007 | Meow | sales stages, opportunities, automated funnel forecasting, team progress and sales analytics | Open-source sales pipeline | https://github.com/mhwh-dev/crm_meow |
| SR-008 | SwiftCPQ | quote/proposal generation, bundles, discounts, quote analytics, funnel/forecast metrics | Open-source CPQ/proposal | https://github.com/christopher-talke/SwiftCPQ |
| SR-009 | RevOps MEDDICC Agent | historical pipeline analytics, MEDDICC, stage/segment/fiscal-year modeling and forecast analytics | Agent/analytics | https://github.com/jeff266/revops-meddicc-agent |
| SR-010 | Sales Pipeline ContentPack | leads, opportunities, proposals, quotes, objections, forecasts, campaigns, touchpoints, deterministic write boundary | Agentic sales knowledge system | https://github.com/SpillwaveSolutions/sales-pipeline |
| SR-011 | Stafe CRM | deal-risk analytics, competitive intelligence, dynamic pricing, territory performance, commission intelligence, quote builder | CRM / sales intelligence | https://github.com/STAFE-GROUP-AB/Stafe-CRM |
| SR-012 | Sales Incentive Management Platform | quota, roles, product-based commission rules, sales records and commission calculation | Commission system | https://github.com/ibizabroker/sales-incentive-management-platform |
| SR-013 | Existing Nivy multi-source acquisition catalog | search, websites, social, directories, enrichment, verification, intent, tech/funding/hiring signals | Internal catalog | `86-sales-data-acquisition-and-multi-channel-prospecting-catalog.md` |
| SR-014 | Existing Nivy sales skill catalogs | prospecting, qualification, discovery, outreach, closing and sales agents | Internal catalogs | `22-p0-sales-skill-extraction-catalog.md`, `23-p0-marketing-skill-extraction-catalog.md` |
| SR-015 | Existing Nivy sales discovery batches | additional agentic sales systems, CRM, GTM, sales intelligence and outbound assets | Internal catalog | `87-new-agentic-business-systems-and-skills-discovery-batch-04.md` |

## 3. Official process/reference resources to reuse as specifications

| Source | Reusable reference |
|---|---|
| Salesforce Sales Operations | sales metrics/analytics, territory planning, quota, incentives, enablement and cross-functional operations |
| Salesforce Sales Planning | plans, product hierarchy, goals, targets, milestones, quota and territory planning |
| Salesforce Sales Operations / Strategy | sales strategy, pipeline, forecasting, territories, compensation, partner channels |
| Salesforce Sales Performance Management | sales plans, segmentation, territories, quota attainment and compensation |
| APQC Sales PCF / benchmarks | sales strategy, sales forecast, sales plans, lead/opportunity management, account management, sales orders and KPI benchmarking |
| APQC Sales & Order Management | sales-order lifecycle, account data, process efficiency, cycle time and productivity |
| ISO 9001:2026 | process control, competence, documented information, performance evaluation and continual improvement |

These sources should be treated as **reference specifications**, not as proof that a particular vendor is the required implementation. Salesforce explicitly separates pipeline from forecast and includes planning, quota, territory, compensation and partner/channel operations; APQC's sales framework covers strategy/forecasting, plans, leads/opportunities, accounts and orders. citeturn0search1turn0search4turn0search2turn1search15

## 4. KRA/KPI hierarchy to research

The resource search must not stop at revenue quota. Build a measurable hierarchy:

`Company Mission/Vision → Strategic Objectives → Revenue Objectives → Sales Objectives → Regional/Country Targets → Segment/Channel Targets → Team Targets → Role KRAs → Individual Goals → KPIs → Leading Indicators → Daily/Weekly Activities → Evidence → Review → Corrective Action`

### KPI classes

- Revenue: bookings, ARR/MRR, recognized revenue, gross margin contribution
- Pipeline: coverage, velocity, value, aging, stage conversion
- Acquisition: leads, qualified leads, meetings, opportunity creation
- Productivity: activities, meetings, opportunities/FTE, revenue/FTE
- Quality: stage compliance, data completeness, forecast accuracy
- Conversion: contact→meeting, meeting→opportunity, opportunity→win
- Commercial: ASP/ACV, discount, margin, quote-to-close
- Time: response time, sales cycle, stage duration
- Customer: retention, expansion, renewal, NPS/CSAT, advocacy/referrals
- People: ramp time, quota attainment, coaching completion, certification
- Forecast: forecast accuracy, bias, commit accuracy, upside/downside
- Channel: partner pipeline, sourced/influenced revenue, partner activation
- Efficiency: CAC/payback where applicable, sales cost/revenue, automation rate

Salesforce's current sales-performance guidance explicitly distinguishes activity and outcome KPIs and treats quota as a primary KPI within a broader metric framework. citeturn0search15

## 5. Sales hierarchy resource search

The discovery agent must search for resources for each level:

1. Board / CEO commercial governance
2. CRO / Chief Sales Officer
3. VP Sales / Regional VP
4. Sales Director
5. Sales Manager
6. Team Lead
7. Account Executive
8. Enterprise AE
9. SDR / BDR
10. Sales Engineer / Solutions Consultant
11. Account Manager
12. Key Account Manager
13. Channel / Partner Manager
14. Sales Operations
15. Revenue Operations
16. Sales Enablement
17. Sales Analyst
18. Deal Desk
19. Proposal/RFP specialist
20. Sales Compensation / Incentive Operations
21. Customer Success / Renewal interface

For every role find: `job purpose → responsibilities → authority → KRA → KPI → targets → competencies → skills → SOPs → daily/weekly/monthly tasks → dashboard → AI copilot → escalation → career progression`.

## 6. Required discovery output for the next research pass

For every capability/resource, capture:

`resource_id | capability | stage | department | role | scale | geography | asset_type | name | URL | source | license | cost | open_source | API | MCP | agent_skill | automation | integrations | maturity | maintenance | evidence | risks | data_access | deployment | human_approval | reusable_for_nivy | adaptation_required | priority`

## 7. Selection rule

Do not automatically adopt the largest vendor or the most feature-rich product.

Use:

`DISCOVER → VERIFY → LICENSE/COST CHECK → MAINTENANCE CHECK → SECURITY CHECK → FUNCTION TEST → DATA/INTEGRATION TEST → CONTROL TEST → COMPARE → SELECT → ADAPT → PILOT → PRODUCTION`

## 8. Important architecture rule

Do not build a separate application for every sales capability.

Prefer:

`Company OS + CRM/System of Record + RevOps Data Layer + Workflow Engine + Knowledge Base + Agent Skills + Specialist Agents + MCP/API + Approval/Policy Engine + Analytics + Audit`

Salesforce's current sales stack similarly connects sales planning, revenue intelligence, CPQ/revenue lifecycle, performance management and partner relationship management rather than treating each activity as an isolated process. citeturn0search7

## 9. Current research status

**Resource discovery is now broad enough to begin systematic extraction.** The next pass should focus on filling genuine gaps rather than collecting duplicate CRMs.

Highest-priority resource gaps:

1. Complete sales planning/goal/KRA/KPI cascade
2. Quota and capacity planning
3. Sales compensation and commission operations
4. Territory/account planning
5. RFP/RFQ/tender/bid automation
6. CPQ/deal desk/pricing governance
7. Sales engineering/pre-sales
8. Conversation intelligence + coaching
9. Sales enablement/certification
10. Partner/channel sales
11. Renewal/expansion/advocacy
12. Forecasting and forecast governance
13. Sales QA/compliance
14. International country sales packs
15. Sales-to-delivery/order-to-cash handoff
16. Revenue intelligence / sales command center
17. Sales workforce/capacity/ramp planning
18. Sales process mining and continuous improvement

## 10. Relationship to existing repository

This file is the **resource-discovery layer**.

`89-complete-international-sales-department-operating-model.md` = what the Sales Department must do.

`90-sales-resource-discovery-catalog.md` = what already exists to help do it.

`22–88` = previously discovered detailed resources and catalogs.

`77-master-automation-and-implementation-registry.md` = execution/selection registry.

Next step after this catalog: map every capability in file 89 to candidate resources, remove duplicates, verify licenses/access, test candidates, and identify only the genuinely missing build requirements.
