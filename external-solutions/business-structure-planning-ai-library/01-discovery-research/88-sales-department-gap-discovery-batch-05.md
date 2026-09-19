# Sales Department Gap Discovery — Batch 05

**Date:** 2026-09-16
**Purpose:** Identify sales capabilities not yet explicitly represented in the reuse library and map reusable open-source/AI assets.

## Assessment

The sales department is already broadly covered across acquisition, prospecting, enrichment, outreach, discovery, proposals, negotiation, pipeline and forecasting. The remaining gaps are mostly **depth and specialist sales operations**, not basic sales functions.

## Newly identified reusable candidates

| ID | Capability | Candidate | Type | Source | Why relevant | Status |
|---|---|---|---|---|---|---|
| S-040 | Full AI outbound sales department | GojiberryAI Sales OS | Sales OS | https://github.com/romangojiberryAI/gojiberryai-sales-os | Head of Sales, signal hunter, ICP analyst, account research, enrichment, intent scoring, LinkedIn copy, outreach and reply agents | Candidate |
| S-041 | End-to-end agentic sales skills | agentic-sales-skills | Skills/agents | https://github.com/Autter-dev/agentic-sales-skills | 11 agents and 48 skills covering preparation, prospecting, meetings, demos, proposals, close, forecasting, rep performance and CS handoff | Candidate |
| S-042 | Full B2B sales lifecycle skills | sales-skills | Skills | https://github.com/TheCraigHewitt/sales-skills | 21 persistent skills spanning ICP, persona, prospecting, discovery, demo, objections, proposal, negotiation, pipeline, forecast and comp | Candidate |
| S-043 | Large sales skill library | Sales-Skills | Skills | https://github.com/louisblythe/Sales-Skills | Broad core/process/AI SDR skill inventory including referrals, events, onboarding, expansion and territory planning | Candidate |
| S-044 | Agentic GTM operating system | GTM Skills | GTM OS/MCP | https://github.com/gtm-skills/gtm | Prompts, workflows, MCP, role playbooks, industry packs, methodologies and signal-based targeting | Candidate |
| S-045 | Sales/GTM MCP + Claude skills | gtm-system | MCP/skills | https://github.com/LaGrowthMachine/gtm-system | Sales Navigator search, multichannel campaigns, audience/inbox operations and reply handling | Candidate |
| S-046 | Local-first AI sales team | OpenCloser | Sales platform | https://github.com/issacops/opencloser-v2 | Strategist, lead researcher, AI caller, sales coach, post-call manager, CRM and analytics | Candidate |
| S-047 | Agent-native CRM | Margince | CRM | https://github.com/margince/margince | MCP/REST agent surface, audited tools, risk tiers, human approval for sensitive CRM actions | Candidate |
| S-048 | RevOps pipeline history + MEDDICC | revops-meddicc-agent | RevOps/analytics | https://github.com/jeff266/revops-meddicc-agent | Reconstructs point-in-time pipeline, scores deals from call transcripts and supports Slack questions | Candidate |
| S-049 | Sales follow-up/re-engagement agents | sales-ai-agents | Agents | https://github.com/sneurgaonkar/sales-ai-agents | Stale-deal follow-up, lead re-engagement, personalized outreach and executive pipeline summaries | Candidate |
| S-050 | Agency sales department agents | agency-agents | Multi-agent skills | https://github.com/hmzainjamil/agency-agents | Outbound strategist, discovery coach, deal strategist, sales engineer, proposal strategist, pipeline analyst, account strategist and sales coach | Candidate |
| S-051 | AI B2B sales pipeline | ai-sales-agent | Sales agent | https://github.com/yoprobotics/ai-sales-agent | Qualification, personalized messaging, CRM pipeline, reminders and sales analytics | Candidate |
| S-052 | HITL sales pipeline | Mesh Pilot AI Sales Agent | Sales agent | https://github.com/Meshpilot-AGI/ai-sales-agent | Discovery, enrichment, email drafting, approval gate, send, reply/bounce/unsubscribe learning loop | Candidate |

## Remaining sales capability gaps

### 1. Sales engineering / technical pre-sales
- Technical discovery
- Solution architecture
- POC qualification
- Demo environment planning
- Technical objection handling
- Security questionnaire/RFP technical response
- Architecture-to-proposal handoff

### 2. RFP / RFQ / tender sales automation
- Tender discovery
- Bid/no-bid decision
- Compliance matrix
- Requirement extraction
- Win-theme generation
- Response assembly
- Pricing input coordination
- Submission checklist
- Post-bid analysis

### 3. CPQ / quote governance
- Product/service configuration
- Pricing rules
- Discount authority
- Margin floor
- Quote generation
- Approval routing
- Version control
- Quote expiry and follow-up

### 4. Deal desk
- Commercial approvals
- Non-standard terms
- Discount review
- Margin review
- Contract redlines coordination
- Legal/finance/security approvals
- Exception tracking

### 5. Territory and account planning
- Territory design
- Named-account planning
- White-space analysis
- Stakeholder maps
- Buying committee maps
- Multi-threading
- Land-and-expand planning

### 6. Partner/channel sales
- Partner discovery
- Partner qualification
- Referral registration
- Channel pipeline
- Partner enablement
- Co-selling
- Partner attribution
- Partner commissions

### 7. Expansion / renewal / account growth
- Renewal risk
- Upsell/cross-sell signals
- Expansion opportunity detection
- QBR preparation
- Executive business reviews
- Customer advocacy/referral triggers

### 8. Sales compensation operations
- Quota allocation
- Territory/quota modeling
- Commission calculation
- SPIFF management
- Compensation disputes
- Commission audit

### 9. Sales capacity and workforce planning
- Rep capacity
- Pipeline coverage requirements
- Hiring timing
- Ramp forecasting
- SDR/AE/SE ratios
- Territory capacity

### 10. Sales data quality / revenue intelligence
- CRM hygiene
- Contact/account deduplication
- Stage consistency
- Activity normalization
- Historical snapshots
- Forecast variance
- Data lineage

### 11. Conversation intelligence depth
- Call transcription
- Buying signal detection
- MEDDICC/SPICED extraction
- Competitor mentions
- Objection taxonomy
- Next-step extraction
- Coaching feedback
- Deal-risk updates

### 12. Sales enablement / knowledge
- Battlecards
- Persona playbooks
- Product knowledge
- Industry packs
- Case-study retrieval
- ROI calculators
- Competitive updates
- Rep certification

### 13. Sales QA / experimentation
- Outreach A/B tests
- Sequence experiments
- Call-quality audits
- Qualification consistency
- Proposal quality checks
- Win/loss feedback loops

### 14. Revenue handoff
- Sales → onboarding
- Sales → implementation
- Sales → customer success
- Commercial commitments → delivery system
- Scope/assumption verification
- Customer success acceptance

### 15. Sales governance and compliance
- Consent/communication rules
- Suppression lists
- DNC handling
- Regional outbound requirements
- Data provenance
- Audit trails
- Approval thresholds
- Agent permissions

## Sales department target architecture

`Market Intelligence → ICP → Source Acquisition → Account Discovery → Contact Discovery → Enrichment → Intent/Signals → Qualification → Sequence → Meeting → Discovery → Demo/Technical Validation → Opportunity → Deal Strategy → Proposal/CPQ → Deal Desk → Negotiation → Contract → Closed Won → Handoff → Expansion/Renewal → Win/Loss → Learning`

Cross-cutting:

`CRM + Knowledge + Conversation Intelligence + Agent Control Plane + Identity/Permissions + Approval + Audit + Analytics + Experimentation`

## What is genuinely still missing

The sales **basic function set is not materially missing**. The main unbuilt depth is:

1. Sales Engineering / Technical Pre-Sales
2. RFP/RFQ/Tender automation
3. CPQ + Deal Desk
4. Partner/Channel Sales
5. Territory + Account Planning
6. Renewal/Expansion engine
7. Compensation operations
8. Conversation intelligence integration
9. Sales QA/experimentation
10. Sales compliance/governance
11. Revenue handoff automation
12. Production integration/testing of all existing candidates

## Priority

P0 implementation depth:
- Sales Engineering
- RFP/RFQ
- CPQ/Deal Desk
- Conversation Intelligence
- CRM data quality
- Revenue handoff

P1:
- Partner/channel
- Account planning
- Expansion/renewal
- Sales compensation
- Capacity planning

P2:
- Advanced experimentation
- Advanced enablement certification
- Specialized territory optimization

## Research conclusion

Do not restart generic sales discovery. The remaining research should be triggered only for one of the capability gaps above, a specific country/industry, or when an existing candidate fails functional/control testing.

The next practical stage is to convert the catalog into a production sales system and test candidates against Nivy's actual CRM, acquisition sources, services, approval rules and international-market requirements.
