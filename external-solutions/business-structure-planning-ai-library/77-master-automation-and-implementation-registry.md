# Master Automation & Implementation Registry

**Status:** v1.3 — 2026-09-16

This is the execution bridge between the reuse library and the production Company OS.

**Operating rule:** `DISCOVERED → SOURCE-VERIFIED → LICENSE-CHECKED → FUNCTION-TESTED → CONTROL-TESTED → ADAPTED → INTEGRATED → PILOT → PRODUCTION → REGRESSION-MONITORED`

## Standard registry fields

`asset_id | capability | department | scale | asset_type | source | license/access | agent/skill | workflow | connector | system_of_record | inputs | outputs | human_role | approval | permissions | data_sensitivity | test_status | integration_status | pilot_status | production_status | owner | priority | gap | next_action`

## Registry

| ID | Capability | Department | Scale | Asset / path | Type | Source | License/access | Status | Next action |
|---|---|---|---|---|---|---|---|---|---|
| REG-001 | Board governance | Corporate Affairs | International/Enterprise | LQGovernance-OpenBoard | System | LegalQuants/LQGovernance-OpenBoard | MIT | Candidate | Test |
| REG-002 | Meeting decisions | Corporate Affairs | SMB→Enterprise | Decidiq | System | ConductionNL/decidiq | EUPL-1.2 | Candidate | Test |
| REG-003 | Entity information | Knowledge/Corporate | All | EIOS | Information OS | entity-core/eios | Verify | Candidate | Test |
| REG-004 | Treasury skills | Finance/Treasury | SMB→Enterprise | Agent Skills Collection | Skills | itsual/agent-skills-collection | Verify | Candidate | Extract/test |
| REG-005 | ITSM | IT/Operations | SMB→Enterprise | Tessio | System | tessio-ai/tessio | AGPL/community | Candidate | Security/integration test |
| REG-006 | ITSM | IT/Operations | SMB→Enterprise | FreeITSM | System | edmozley/freeitsm | MIT | Candidate | Compare |
| REG-007 | GRC | Risk/Compliance | SMB→Enterprise | security-atlas | System | mgoodric/security-atlas | Apache-2.0 | Candidate | Test |
| REG-008 | GRC + AI agents | Risk/Compliance | Enterprise | riskready-community | System | riskreadyeu/riskready-community | Verify | Candidate | MCP/security test |
| REG-009 | ESG reporting | ESG | International/Enterprise | sustainability-project | System | aliozkanozdurmus/sustainability-project | MIT | Candidate | Data/control test |
| REG-010 | Revenue assurance | Finance/RevOps | Mid-market→Enterprise | Rapo | System | t3eHawk/rapo | Verify | Candidate | Synthetic test |
| REG-011 | Revenue leakage | Finance/RevOps | SMB→Enterprise | revenue_leakage_system | Workflow | Etherlabs-dev/revenue_leakage_system | Verify | Candidate | Synthetic test |
| REG-012 | Corporate legal | Legal | International/Enterprise | legal-skills-open corporate | Skill | ThomasMoreAI/legal-skills-open | Apache-2.0 | Candidate | Jurisdiction review |
| REG-013 | Board intelligence | Corporate Affairs | SMB→Enterprise | board-observer | Agent | vitalii-dynamiq/board-observer | Verify | Candidate | Test |
| REG-014 | Financial OS | Finance | India/SMB | Hisaabo | System | hisaabo/hisaabo | Verify | Candidate | Security/scope test |
| REG-015 | Treasury/agent payments | Treasury | Enterprise | Nirium / Eunomia | Infrastructure | nirium-protocol/nirium-sdk; eunomia-finance/eunomia | Experimental | Research | Sandbox only |
| REG-016 | Business operating system | Cross-company | SMB→Enterprise | BOS-AI | End-to-end system | TheWayWithin/BOS-AI | Verify | Candidate | Architecture extraction |
| REG-017 | Company knowledge graph | Knowledge | All | company-brain | Knowledge system | nemock/company-brain | Verify | Candidate | Provenance test |
| REG-018 | AI-native company OS | Cross-company | SMB→Enterprise | CompanyOS | End-to-end system | rojenwai/CompanyOS | Verify | Candidate | Extract patterns |
| REG-019 | Autonomous business OS | Cross-company | Solo→SMB | Kompany | Agent OS | Fei2-Labs/Kompany | AGPL-3.0 | Candidate | Sandbox |
| REG-020 | Agent skills library | Cross-company | All | AI-Agent-Skills-Library | Skills | mhrsdev/AI-Agent-Skills-Library | Verify | Candidate | Inventory |
| REG-021 | Finance semantic layer | Finance/Data | Mid-market→Enterprise | semantic-layer-finance | Data layer | abchatter/semantic-layer-finance | Verify | Candidate | Schema/security test |
| REG-022 | ERP/ecommerce | Operations/Finance | SMB | genix | ERP | ivanjoz/genix | Verify | Candidate | Comparison |
| REG-023 | CMS/workflows | Marketing/Knowledge | SMB→Enterprise | nivaro | CMS/system | nodeworks/nivaro | Verify | Candidate | Security/function test |
| REG-024 | Sales/marketing | Revenue | All | Existing files 22–24, 49–55 | Skills/workflows | Internal catalog | Mixed | Library | Convert to executable workflows |
| REG-025 | Document automation | Cross-company | All | Existing files 56–59 | Skills/workflows | Internal catalog | Mixed | Library | Connector/test matrix |
| REG-026 | AI infrastructure | Cross-company | All | Existing files 60–66 | Architecture/governance | Internal catalog | Mixed | Library | Implement control plane |
| REG-027 | Workforce OS | HR | All | Existing files 67–68 | Workforce workflows | Internal catalog | Mixed | Library | Integrate HR/task systems |
| REG-028 | Enterprise capability model | Executive | All scales | Files 74–76 | Architecture | Internal catalog | Internal | Library | Activation matrix |
| REG-029 | Multi-source lead acquisition | Revenue | All | File 86 | Acquisition catalog | Internal + verified candidates | Mixed | Cataloged | Instantiate P0 workflows |
| REG-030 | Universal web/social acquisition | Revenue/Research | All | Apify Agent Skills | Skill | apify/agent-skills | Verify | Candidate | Source tests |
| REG-031 | Web crawling/search MCP | Revenue/Research | All | Crawl4AI MCP candidates | MCP | jeffmm/crawl4ai-mcp; sadiuysal/crawl4ai-mcp-server; potterdigital/crawl4ai-mcp | Verify | Candidate | Select/test |
| REG-032 | Multi-platform lead-gen | Revenue | SMB→Enterprise | lead-gen-hacker | Workflow | sirlifehacker/lead-gen-hacker | Verify | Candidate | Sandbox |
| REG-033 | Lead research agent | Revenue | All | lead-research-agent | Agent | mcvalosborne/lead-research-agent | Verify | Candidate | Source/security test |
| REG-034 | Multi-channel lead agent | Revenue | All | Lead-Reach | Agent system | getleads-humain/Lead-Reach | Verify | Candidate | Architecture test |
| REG-035 | B2B enrichment MCP | Revenue/Data | SMB→Enterprise | b2b-enrichment-mcp | MCP | Aleksey-Panf/b2b-enrichment-mcp | MIT | Candidate | Credential test |
| REG-036 | Apollo official MCP | Revenue | SMB→Enterprise | apollo-mcp-plugin | MCP/skills | apolloio/apollo-mcp-plugin | MIT | Candidate | Permission test |
| REG-037 | Email discovery/verification | Revenue/Data | All | Prospector MCP | MCP | josiebot26/prospector-mcp-email-finder | Verify | Candidate | Deliverability test |
| REG-038 | Public-data prospecting | Revenue | SMB→Enterprise | OpenLeads | System | Samyrrrrrr990/openleads | Verify | Candidate | Legal/source test |
| REG-039 | Agentic lead-gen pipeline | Revenue | All | Hermes lead-generation pipeline | Agent/skills | vivekshetye/hermes-lead-generation-pipeline | Verify | Candidate | Skill test |
| REG-040 | Agentic GTM OS | Revenue | SMB→Enterprise | GTM Skills | Skills + MCP + workflows | gtm-skills/gtm | MIT | Candidate | Extract/compare |
| REG-041 | Unified agentic business OS | Cross-company | SMB→Enterprise | FlowWink | Business OS + MCP/A2A | magnusfroste/flowwink | MIT | Candidate | Sandbox |
| REG-042 | Agent-native business OS | Cross-company | SMB/agency | FusionClaw | Business OS + MCP | Fusion-Data-Company/FusionClaw | MIT | Candidate | Compare |
| REG-043 | AI-first CRM | Revenue | SMB→Mid-market | Relaticle | CRM + MCP | Relaticle/relaticle | AGPL-3.0 | Candidate | Compare with Odoo |
| REG-044 | Portable AI CRM skills | Revenue | Solo→SMB | crmkit | CRM + skills + MCP | crmkit/crmkit | MIT | Candidate | Skill extraction |
| REG-045 | AI work/CRM platform | Revenue/Operations | SMB→Enterprise | TropaTT | CRM/work OS + MCP | Anton-Barinov/TropaTT | Verify | Candidate | Security/license test |
| REG-046 | Sales intelligence MCP | Revenue | SMB→Mid-market | sales-intelligence-mcp | MCP | aria-agentworks/sales-intelligence-mcp | MIT | Candidate | API/provenance test |
| REG-047 | Grounded sales research | Revenue | SMB→Enterprise | sales-research-agent | Agent + MCP | aawais-ai/sales-research-agent | Verify | Candidate | Offline evaluation |
| REG-048 | Professional AI workforce | Cross-company | All | agent-skills-professional | Skills | aiagenta2z/agent-skills-professional | Verify | Candidate | Map to workforce OS |
| REG-049 | Business skills library | Cross-company | All | business-skills | Skills | astDeniss/business-skills | Verify | Candidate | Inventory |
| REG-050 | Digital marketing OS | Marketing | SMB→Enterprise | digital-marketing-pro | Marketing OS + skills | indranilbanerjee/digital-marketing-pro | Verify | Candidate | Compare with Nivy Next |
| REG-051 | GTM/RevOps skills | Revenue | SMB→Enterprise | sumble-skills-public | Skills | SumbleData/sumble-skills-public | Verify | Candidate | Extract |
| REG-052 | Legal/finance/capital skills | Legal/Finance/Corp Dev | Mid-market→Enterprise | CaseMark skills | Skills | CaseMark/skills | Verify | Candidate | License/jurisdiction review |
| REG-053 | AI-native ERP architecture | Enterprise | Enterprise | GERP | ERP + MCP + Temporal | quantDIY/GERP | MIT | Candidate | Architecture extraction |
| REG-054 | AI-native ERP | Finance/Operations | SMB→Mid-market | lambda-erp | ERP + API + MCP | lambdadevelopment/lambda-erp | Verify | Candidate | Compare |
| REG-055 | Multi-backend ERP MCP | Finance/Operations | Mid-market→Enterprise | mcp-erp | MCP integration | zavora-ai/mcp-erp | Verify | Candidate | Connector test |
| REG-056 | Service-business OS | Operations | SMB | evolved | Business OS + MCP | kr8tiv-ai/evolved | MIT | Candidate | Extract patterns |
| REG-057 | Autonomous business lifecycle | Cross-company | SMB→Mid-market | autonomous-business-os | Multi-agent BOS | Cubiczan/autonomous-business-os | Verify | Candidate | Orchestration test |
| REG-058 | Full AI outbound sales team | Revenue | SMB→Enterprise | GojiberryAI Sales OS | Sales OS | romangojiberryAI/gojiberryai-sales-os | Verify | Candidate | MCP + sandbox test |
| REG-059 | Agentic sales skills | Revenue | All | agentic-sales-skills | 11 agents + 48 skills | Autter-dev/agentic-sales-skills | Verify | Candidate | Extract/compare |
| REG-060 | B2B sales lifecycle skills | Revenue | All | sales-skills | 21 skills | TheCraigHewitt/sales-skills | Verify | Candidate | Extract/test |
| REG-061 | Extended sales skill library | Revenue | All | Sales-Skills | Skills | louisblythe/Sales-Skills | Verify | Candidate | Inventory/dedupe |
| REG-062 | Sales/GTM MCP + Claude skills | Revenue | SMB→Enterprise | gtm-system | MCP/skills | LaGrowthMachine/gtm-system | MIT | Candidate | Access/permission test |
| REG-063 | Local-first AI sales team | Revenue | Solo→SMB | OpenCloser | Sales platform | issacops/opencloser-v2 | Verify | Candidate | Local sandbox |
| REG-064 | Agent-native CRM | Revenue/RevOps | SMB→Enterprise | Margince | CRM | margince/margince | Verify | Candidate | RBAC/risk-tier test |
| REG-065 | Historical pipeline + MEDDICC | RevOps | Mid-market→Enterprise | revops-meddicc-agent | Analytics/agent | jeff266/revops-meddicc-agent | Verify | Candidate | Synthetic CRM test |
| REG-066 | Sales follow-up/re-engagement | Revenue | SMB→Enterprise | sales-ai-agents | Agents | sneurgaonkar/sales-ai-agents | Verify | Candidate | Adapt/integrate |
| REG-067 | Agency sales department | Revenue | SMB→Enterprise | agency-agents | Agent collection | hmzainjamil/agency-agents | Verify | Candidate | Extract reusable agents |
| REG-068 | AI B2B sales pipeline | Revenue | SMB→Enterprise | ai-sales-agent | Sales platform | yoprobotics/ai-sales-agent | Verify | Candidate | Functional comparison |
| REG-069 | HITL sales pipeline | Revenue | All | Mesh Pilot AI Sales Agent | Sales agent | Meshpilot-AGI/ai-sales-agent | MIT | Candidate | HITL/security test |

## Sales capability coverage

Covered at catalog/system level:
- ICP, positioning and buyer personas
- multi-source acquisition, enrichment and verification
- intent/signals
- outbound email/social sequences
- discovery and qualification
- demos and objection handling
- proposals, pricing and negotiation
- CRM/pipeline and forecasting
- win/loss and sales leadership
- basic handoff

Remaining material depth gaps:
1. Sales Engineering / Technical Pre-Sales
2. RFP/RFQ/Tender automation
3. CPQ and Deal Desk
4. Partner/Channel Sales
5. Territory and Account Planning
6. Renewal/Expansion engine
7. Sales compensation operations
8. Conversation intelligence integration
9. Sales QA/experimentation
10. Sales compliance/governance
11. Revenue handoff automation
12. Production integration/testing

## Sales production chain

`Market Intelligence → ICP → Source Acquisition → Account Discovery → Contact Discovery → Enrichment → Intent/Signals → Qualification → Sequence → Meeting → Discovery → Demo/Technical Validation → Opportunity → Deal Strategy → Proposal/CPQ → Deal Desk → Negotiation → Contract → Closed Won → Handoff → Expansion/Renewal → Win/Loss → Learning`

Cross-cutting:
`CRM + Knowledge + Conversation Intelligence + Agent Control Plane + Identity/Permissions + Approval + Audit + Analytics + Experimentation`

## Mandatory implementation record

No asset reaches production without source/provenance, license/access decision, owner, system of record, data classification, identity/least privilege, approval policy, exception path, audit evidence, functional test, control/security test, cost estimate, rollback/kill switch and regression test.

## Core workflow pattern

`Trigger → Context → Agent/Skill → Tool/MCP → Policy Check → Approval (if required) → Action → Verify → Evidence → System-of-Record Update → KPI → Exception → Learning`

## Research rule

Do not repeat generic discovery just to increase the number of repositories. Research again only for a missing capability, country/jurisdiction, industry specialization, failed candidate, unsuitable license/access model, better maintained replacement, or implementation blocker.
