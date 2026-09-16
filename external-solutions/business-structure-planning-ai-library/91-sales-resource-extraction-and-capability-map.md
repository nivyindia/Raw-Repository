# Sales Resource Extraction & Capability Map — International Sales

**Status:** v1.0 — 2026-09-16
**Purpose:** Convert the complete Sales operating model into an actionable reuse map. This file is the extraction layer between the operating model (`89`) and production selection/testing.

## 1. Research rule

Use **REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**.

Every candidate is classified as:
- **Reuse now** — directly usable with acceptable adaptation.
- **Adapt** — reusable asset requiring Nivy-specific configuration.
- **Integrate** — external system/connector to place behind the Company OS.
- **Reference** — framework/specification rather than executable software.
- **Build gap** — only when no suitable reusable asset exists after targeted discovery.

## 2. High-confidence reusable resource set

| ID | Capability | Resource | Asset | License / access | Recommended use |
|---|---|---|---|---|---|
| X-001 | End-to-end GTM | GTM Skills | Open-source GTM skills, prompts, MCP, workflows | MIT | Reuse/adapt as sales skill foundation |
| X-002 | RevOps | revops-skills | RevOps audit, forecast prep, pipeline hygiene, deal investigation, routing | MIT | Reuse/adapt |
| X-003 | Account planning | GitHub Awesome Copilot enterprise account planning | Agent skill | Open-source repo | Adapt |
| X-004 | Sales enablement | Enablement Skills | Revenue enablement skills/playbooks | Open-source repo | Reuse/adapt |
| X-005 | Account intelligence | Sumble Skills | Account/people scoring, territory planning, research | Open-source skills; external data dependency | Adapt if data economics work |
| X-006 | Sales pipeline | Open CRM | CRM, deals, tasks, pipeline, forecasting | Open-source | Evaluate as component/SOR candidate |
| X-007 | CRM | Horilla CRM | Leads, opportunities, campaigns, dashboards, forecasting | Open-source | Evaluate |
| X-008 | CPQ | SwiftCPQ | Quotes, bundles, discounts, proposal flow | Open-source | Evaluate |
| X-009 | Incentives | Sales Incentive Management Platform | Commission rules/calculation | Open-source | Evaluate/adapt |
| X-010 | Acquisition | Nivy multi-source acquisition catalog | Search/social/directories/enrichment/source waterfall | Internal | Integrate with sales engine |
| X-011 | Pipeline analytics | RevOps MEDDICC Agent | MEDDICC/pipeline/forecast analysis | Open-source | Adapt |
| X-012 | Sales knowledge | Sales Pipeline ContentPack | Leads/opportunities/proposals/quotes/objections/forecast knowledge model | Open-source | Adapt |
| X-013 | Conversation/sales execution | Modjo Sales Agent | 20+ sales skills/router, call follow-up, forecast, competitive intelligence | Open-source repo; Modjo dependency for live workspace | Evaluate |
| X-014 | GTM outbound | La Growth Machine GTM System | Skills + MCP for lists, campaigns, replies | MIT | Evaluate as outbound component |
| X-015 | GTM skills | Sumble public skills | Account scoring, people scoring, territory planning, MCP workflows | Open-source; data service dependency | Adapt |
| X-016 | Pipeline evaluation | Panaversity Agent Factory pipeline skill/evals | Pipeline review/evaluation patterns | Open-source | Reuse evaluation patterns |

## 3. Capability coverage map

| Sales capability | Existing reusable coverage | Primary candidates | Remaining work |
|---|---|---|---|
| Strategy/GTM | Strong | GTM Skills + existing Nivy strategy catalogs | Nivy strategy configuration |
| Sales planning | Partial | Sumble territory planning; sales-planning references | Build Nivy planning template/model |
| Goal cascade | Partial | Existing Nivy workforce/KRA/KPI layer | Sales-specific mapping |
| KRA/KPI | Strong framework; executable depth partial | Existing workforce OS + RevOps skills | Connect sales KPI registry to CRM |
| Organization/roles | Strong | Nivy workforce OS | Map actual org |
| Quota | Partial | RevOps/forecast resources + compensation resources | Nivy quota model |
| Capacity | Partial | Territory/workforce planning skills | Capacity calculator + assumptions |
| Territory | Strong candidate coverage | Sumble territory planning + GTM skills | Country/segment configuration |
| Compensation | Partial | Sales Incentive Management Platform + RevOps skill roadmap | Validate rules, payroll/finance integration |
| Market intelligence | Strong | GTM Skills + acquisition catalog | Source routing |
| Lead acquisition | Strong | Nivy file 86 + Apify/Crawl4AI ecosystem | Production source connectors |
| Lead enrichment | Strong | Apollo MCP, enrichment MCPs, Apify | Provider selection/cost controls |
| Prospecting | Strong | GTM Skills, La Growth Machine, existing Nivy skills | Integrate |
| Qualification | Strong | MEDDICC/other methodology skills | Standardize methodology by segment |
| Discovery | Strong | Agent Skills Collection, GTM Skills, Modjo | Adapt scripts/rubrics |
| Solution engineering | Partial | Sales skills + proposal systems | Technical pre-sales skill pack |
| Opportunity management | Strong | RevOps skills, pipeline skills | Nivy stage gates |
| Account planning | Strong | Enterprise account planning skill, Sumble | Integrate account SOR |
| Proposal | Partial | SwiftCPQ + existing proposal resources | Pricing/SOW templates |
| RFP/RFQ/Bid | Partial | Existing bid/RFP discovery | Dedicated bid agent + compliance matrix |
| Pricing | Partial | SwiftCPQ + deal desk patterns | Nivy pricing policy |
| CPQ | Strong candidate | SwiftCPQ | Test against service packages |
| Deal desk | Partial | RevOps/deal workflows | Approval policy |
| Negotiation | Strong | Agent Skills Collection + GTM Skills + AE skill | Nivy negotiation playbook |
| Closing | Strong | AE skills + CLM/e-sign integrations | Integrate |
| Handoff | Partial | Open CRM + existing workflow catalog | Delivery handoff schema |
| Forecasting | Strong | revops-skills + RevOps MEDDICC Agent + pipeline evals | Connect to SOR and forecast calendar |
| Performance | Strong | RevOps skills + workforce OS | Sales dashboard |
| Coaching | Strong | Modjo Sales Agent + enablement skills | QA rubric |
| Enablement | Strong | Enablement Skills + GTM Skills | Knowledge architecture |
| Channel/partner | Partial | Agent Skills Collection + existing channel resources | PRM workflow |
| Account management | Strong | Account planning + AE skills | Account lifecycle |
| Expansion | Strong candidate | GTM/enablement/account skills | Product/service triggers |
| Renewal | Strong candidate | Enablement + CRM + CS resources | Renewal forecast workflow |
| Advocacy | Partial | Existing CS/advocacy catalog | Reference/referral automation |
| Analytics | Strong | RevOps skills + semantic/BI resources | Nivy semantic model |
| RevOps | Strong | revops-skills + GTM Skills | Integrate with Company OS |
| Governance | Partial | Existing governance/control plane | Sales-specific policy pack |
| QA | Strong candidate | revops-skills + pipeline evals + Modjo | Production evaluation suite |
| International | Partial | Existing country-pack architecture | Country-specific sales packs |
| Quote → contract → order → billing | Partial | CPQ/CLM/O2C resources | Cross-functional integration |

## 4. Immediate extraction priorities

### P0 — extract/adapt first
1. GTM Skills
2. revops-skills
3. Enterprise account planning skill
4. Enablement Skills
5. Existing Nivy multi-source acquisition assets
6. Existing Nivy sales skills
7. RevOps MEDDICC Agent
8. Sales Pipeline ContentPack
9. Modjo Sales Agent patterns
10. Pipeline evaluation/evals from Agent Factory

### P1 — test after P0
11. Sumble skills
12. Horilla CRM
13. Open CRM
14. SwiftCPQ
15. Sales Incentive Management Platform
16. La Growth Machine GTM System

## 5. Production architecture

```text
SOURCE ACQUISITION
  ↓
ENRICHMENT / IDENTITY / DEDUPE
  ↓
CRM / SYSTEM OF RECORD
  ↓
REVOPS DATA + SEMANTIC LAYER
  ↓
SALES SKILLS + SPECIALIST AGENTS
  ↓
WORKFLOW / MCP / API
  ↓
POLICY + APPROVAL + SoD
  ↓
ACTION
  ↓
EVIDENCE + AUDIT
  ↓
KPI / FORECAST / COMMAND CENTER
  ↓
LEARNING / QA / CONTINUOUS IMPROVEMENT
```

Do not create one application for every capability.

## 6. Sales command-center minimum dashboard

### Executive
- revenue vs plan
- bookings/ARR/MRR where applicable
- forecast / commit / best case
- pipeline coverage
- win rate
- sales cycle
- new logo / expansion / renewal
- gross margin contribution

### CRO / VP
- region/country/segment performance
- quota attainment
- pipeline creation
- conversion by stage
- forecast variance/bias
- deal risk
- territory performance
- rep capacity/ramp
- channel contribution

### Manager
- rep performance
- stalled opportunities
- next actions
- activity quality
- forecast changes
- coaching queue
- SLA exceptions

### Rep
- today's priorities
- leads
- meetings
- follow-ups
- opportunity next steps
- risk alerts
- account plans
- quota/pipeline gap

## 7. Sales KRA → KPI → evidence pattern

Every role should use:

`Role → KRA → KPI → Target → Leading Indicator → Activity → Evidence → Review → Corrective Action`

Example:

`AE → New Business Acquisition → New-logo revenue → quarterly target → qualified pipeline coverage → discovery/proposals → CRM evidence → weekly review → coaching/deal action`

No KPI should exist without an owner, target, measurement source, frequency, evidence definition and escalation rule.

## 8. International operating model

```text
GLOBAL SALES STANDARD
        ↓
REGIONAL MODEL
        ↓
COUNTRY PACK
        ↓
SEGMENT / INDUSTRY PACK
        ↓
TERRITORY / ACCOUNT PLAN
        ↓
REP EXECUTION
        ↓
GLOBAL REPORTING
```

Country packs should include:
- currency
- language
- buying behavior
- contract requirements
- tax/VAT/GST considerations where sales process is affected
- privacy/consent rules
- local channels/directories
- payment norms
- procurement requirements
- local holidays/time zones
- local partner/channel model
- industry-specific restrictions

## 9. Research evidence added in this pass

- GTM Skills provides an open-source agentic GTM ecosystem with role-based playbooks, methodologies, workflows, MCP and API components. Source: https://github.com/gtm-skills/gtm
- revops-skills provides MIT-licensed RevOps skills for audit, forecast-call preparation, pipeline hygiene, deal investigation, activity capture and lead routing. Source: https://github.com/elijeangilles/revops-skills
- Sumble's public skills include account research/scoring, people scoring and territory planning and are designed for Claude Code, Codex and Cursor. Source: https://github.com/SumbleData/sumble-skills-public
- La Growth Machine's GTM system provides open-source Claude skills and MCP workflows for prospecting, campaigns and replies. Source: https://github.com/LaGrowthMachine/gtm-system
- Modjo Sales Agent provides a multi-skill sales toolkit with forecast and qualification patterns and explicit approval/anti-fabrication rules. Source: https://github.com/tdeschamps/modjo-sales-agent
- Agent Factory's pipeline skill includes executable evaluation cases for pipeline reviews, providing a reusable pattern for testing sales agents rather than relying only on prompt quality.

## 10. Build-only-if-missing list

Do not build these until the reusable candidates have been tested:

1. Nivy-specific sales planning engine
2. Nivy company → sales → team → role KRA/KPI cascade connector
3. Nivy quota/capacity model
4. Nivy international territory/country activation engine
5. Nivy sales command center if existing BI/CRM cannot satisfy requirements
6. Nivy unified sales-agent router if existing MCP/skills cannot provide safe orchestration
7. Nivy-specific RFP/bid compliance agent
8. Nivy-specific CPQ/deal desk policy layer
9. Nivy sales-to-delivery handoff schema
10. Nivy advocacy/referral automation

These are **candidate gaps**, not confirmed build requirements.

## 11. Status

**Research:** broad coverage established.

**Extraction:** started with high-value reusable assets.

**Testing:** not yet performed against Nivy production data.

**Integration:** not yet performed.

**Production decision:** pending functional, license, security, cost, integration and control tests.

## 12. Relationship to repository

- `89-complete-international-sales-department-operating-model.md` — capability definition.
- `90-sales-resource-discovery-catalog.md` — broad discovery inventory.
- `91-sales-resource-extraction-and-capability-map.md` — extraction/coverage/adoption map.
- `77-master-automation-and-implementation-registry.md` — production registry.
- `86-sales-data-acquisition-and-multi-channel-prospecting-catalog.md` — acquisition layer.
