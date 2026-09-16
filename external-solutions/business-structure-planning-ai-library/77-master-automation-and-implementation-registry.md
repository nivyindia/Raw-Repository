# Master Automation & Implementation Registry

**Status:** v1.1 — 2026-09-16

## Purpose

This is the execution bridge between the reuse library and the production Company OS.

It answers, for every reusable capability:

`What exists → where it comes from → what it does → how it connects → who/what runs it → what approval is needed → how it is tested → whether Nivy has integrated it → whether it is production-ready.`

**Operating rule:** `DISCOVERED → SOURCE-VERIFIED → LICENSE-CHECKED → FUNCTION-TESTED → CONTROL-TESTED → ADAPTED → INTEGRATED → PILOT → PRODUCTION → REGRESSION-MONITORED`

## Standard registry fields

`asset_id | capability | department | scale | asset_type | source | license/access | agent/skill | workflow | connector | system_of_record | inputs | outputs | human_role | approval | permissions | data_sensitivity | test_status | integration_status | pilot_status | production_status | owner | priority | gap | next_action`

## Seed registry

| ID | Capability | Department | Scale | Asset / path | Type | Source | License/access | Intended workflow | Status | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| REG-001 | Board governance | Corporate Affairs | International/Enterprise | LQGovernance-OpenBoard | System | GitHub: LegalQuants/LQGovernance-OpenBoard | MIT | Agenda → meeting → quorum → vote → minutes → action/evidence | Candidate | License/security/function test |
| REG-002 | Meeting decisions | Corporate Affairs | SMB→Enterprise | Decidiq | System | GitHub: ConductionNL/decidiq | EUPL-1.2 | Agenda → motion → vote → decision → tracking | Candidate | Test + schema mapping |
| REG-003 | Entity information | Knowledge/Corporate | All | EIOS | Information OS | GitHub: entity-core/eios | Verify | Entity → record → provenance → retrieval | Candidate | License/maintenance test |
| REG-004 | Treasury skills | Finance/Treasury | SMB→Enterprise | Agent Skills Collection | Skills | GitHub: itsual/agent-skills-collection | Verify | Cash/banking/FX/debt/control task → skill → evidence | Candidate | Extract + test skills |
| REG-005 | ITSM | IT/Operations | SMB→Enterprise | Tessio | System | GitHub: tessio-ai/tessio | AGPL/community | Intake → triage → route → SLA → resolve → KB | Candidate | Security + integration test |
| REG-006 | ITSM | IT/Operations | SMB→Enterprise | FreeITSM | System | GitHub: edmozley/freeitsm | MIT | Ticket → asset/CMDB → workflow → resolution | Candidate | Compare with Tessio |
| REG-007 | GRC | Risk/Compliance | SMB→Enterprise | security-atlas | System | GitHub: mgoodric/security-atlas | Apache-2.0 | Risk → control → evidence → audit → board report | Candidate | Security/function test |
| REG-008 | GRC + AI agents | Risk/Compliance | Enterprise | riskready-community | System | GitHub: riskreadyeu/riskready-community | Verify | Risk/control/policy/incident/audit → governed agent action | Candidate | MCP/security/approval test |
| REG-009 | ESG reporting | ESG | International/Enterprise | sustainability-project | System | GitHub: aliozkanozdurmus/sustainability-project | MIT | Data → claims → citations → report → board dashboard | Candidate | Data/control test |
| REG-010 | Revenue assurance | Finance/RevOps | Mid-market→Enterprise | Rapo | System | GitHub: t3eHawk/rapo | Verify | Billing/revenue data → controls → leakage signals | Candidate | Synthetic revenue test |
| REG-011 | Revenue leakage | Finance/RevOps | SMB→Enterprise | revenue_leakage_system | Workflow/system | GitHub: Etherlabs-dev/revenue_leakage_system | Verify | Contract → entitlement → actual billing → mismatch | Candidate | Test against synthetic contracts |
| REG-012 | Corporate legal | Legal | International/Enterprise | legal-skills-open corporate skill | Skill | GitHub: ThomasMoreAI/legal-skills-open | Apache-2.0 | Entity/governance/M&A/securities task → legal skill → human review | Candidate | Jurisdiction/test review |
| REG-013 | Board meeting intelligence | Corporate Affairs | SMB→Enterprise | board-observer | Agent | GitHub: vitalii-dynamiq/board-observer | Verify | Agenda → transcript → decisions/actions → summary | Candidate | Verify repo/license |
| REG-014 | Financial OS | Finance | India/SMB | Hisaabo | System | GitHub: hisaabo/hisaabo | Verify | Invoice/bank/reconciliation/GST/audit trail | Candidate | Scope and security test |
| REG-015 | Treasury/agent payments | Treasury | Enterprise | Nirium / Eunomia | Infrastructure | GitHub: nirium-protocol/nirium-sdk; eunomia-finance/eunomia | Experimental/verify | Policy → payment proposal → approval → execution → evidence | Research | Sandbox-only evaluation |
| REG-016 | Business operating system | Cross-company | SMB→Enterprise | BOS-AI | End-to-end system | GitHub: TheWayWithin/BOS-AI | Verify | Strategy → agents → routines → MCP → business work | Candidate | Architecture extraction |
| REG-017 | Company knowledge graph | Knowledge | All | company-brain | Knowledge system | GitHub: nemock/company-brain | Verify | Source → graph → planning/doc generation | Candidate | Test provenance/retrieval |
| REG-018 | AI-native company OS | Cross-company | SMB→Enterprise | CompanyOS | End-to-end system | GitHub: rojenwai/CompanyOS | Verify | Departments → orchestration → memory → governance | Candidate | Extract reusable patterns |
| REG-019 | Autonomous business OS | Cross-company | Solo→SMB | Kompany | Agent OS | GitHub: Fei2-Labs/Kompany | AGPL-3.0 | Directive → C-suite agents → budget/work | Candidate | Sandbox evaluation |
| REG-020 | Agent skills library | Cross-company | All | AI-Agent-Skills-Library | Skills | GitHub: mhrsdev/AI-Agent-Skills-Library | Verify | Role/task → reusable skill | Candidate | Inventory + license test |
| REG-021 | Finance semantic layer | Finance/Data | Mid-market→Enterprise | semantic-layer-finance | Data layer | GitHub: abchatter/semantic-layer-finance | Verify | Agent question → governed financial semantic query | Candidate | Schema/security test |
| REG-022 | ERP/ecommerce | Operations/Finance | SMB | genix | ERP | GitHub: ivanjoz/genix | Verify | Order → inventory → sales → cash | Candidate | Functional comparison |
| REG-023 | CMS/workflows | Marketing/Knowledge | SMB→Enterprise | nivaro | CMS/system | GitHub: nodeworks/nivaro | Verify | Content/data → workflow → approval → publish | Candidate | Security/function test |
| REG-024 | Sales/marketing | Revenue | All | Existing files 22–24, 49–55 | Skills/workflows | Internal catalog | Mixed | Research → CRM → outreach → response → pipeline | Library | Convert to executable workflows |
| REG-025 | Document automation | Cross-company | All | Existing files 56–59 | Skills/workflows | Internal catalog | Mixed | Intake → extract → classify → generate → review → store | Library | Connector + test matrix |
| REG-026 | AI infrastructure | Cross-company | All | Existing files 60–66 | Architecture/governance | Internal catalog | Mixed | Agent → registry → identity → tool → policy → audit | Library | Implement control plane |
| REG-027 | Workforce OS | HR | All | Existing files 67–68 | Workforce workflows | Internal catalog | Mixed | Role → KRA/KPI → goals → tasks → evidence → review | Library | Integrate HR/task systems |
| REG-028 | Enterprise capability model | Executive | All scales | Files 74–76 | Architecture | Internal catalog | Internal | Capability → maturity → scale → implementation | Library | Use as activation matrix |
| REG-029 | Multi-source lead acquisition | Revenue | All | File 86 | Acquisition catalog | Internal catalog + verified public candidates | Mixed | ICP → source router → discovery → extraction → normalize → dedupe → enrichment → verification → CRM | Cataloged | Instantiate P0 acquisition workflows |
| REG-030 | Universal web/social acquisition | Revenue/Research | All | Apify Agent Skills / apify-ultimate-scraper | Skill | GitHub: apify/agent-skills | Verify | Source selection → actor → extraction → structured output | Candidate | License/access + source-specific tests |
| REG-031 | Web crawling/search MCP | Revenue/Research | All | Crawl4AI MCP candidates | MCP | GitHub: jeffmm/crawl4ai-mcp; sadiuysal/crawl4ai-mcp-server; potterdigital/crawl4ai-mcp | Verify | Search/crawl → extraction → structured lead/company data | Candidate | Select one + test |
| REG-032 | Multi-platform lead-gen | Revenue | SMB→Enterprise | lead-gen-hacker | Workflow | GitHub: sirlifehacker/lead-gen-hacker | Verify | LinkedIn/Instagram/Maps/YouTube/Meta Ads → normalize → enrich → qualify | Candidate | Reproduce in sandbox |
| REG-033 | Lead research agent | Revenue | All | lead-research-agent | Agent/system | GitHub: mcvalosborne/lead-research-agent | Verify | Twitter/LinkedIn/Reddit → enrich → score → outreach | Candidate | Source/security test |
| REG-034 | Multi-channel lead agent | Revenue | All | Lead-Reach | Agent system | GitHub: getleads-humain/Lead-Reach | Verify | Web/LinkedIn/Twitter/GitHub/YouTube/Reddit → enrichment → research | Candidate | Architecture/test |
| REG-035 | B2B enrichment MCP | Revenue/Data | SMB→Enterprise | b2b-enrichment-mcp | MCP | GitHub: Aleksey-Panf/b2b-enrichment-mcp | MIT | Domain/person → Hunter + Apollo enrichment → verification | Candidate | Credential/sandbox test |
| REG-036 | Apollo official MCP | Revenue | SMB→Enterprise | apollo-mcp-plugin | MCP/skills | GitHub: apolloio/apollo-mcp-plugin | MIT | ICP → people/company search → enrichment → sequence | Candidate | Account/permission test |
| REG-037 | Free email verification | Revenue/Data | All | Prospector MCP | MCP | GitHub: josiebot26/prospector-mcp-email-finder | Verify | Name/domain → discovery → DNS/SMTP verification | Candidate | Safety + deliverability test |
| REG-038 | Public-data prospecting | Revenue | SMB→Enterprise | OpenLeads | System | GitHub: Samyrrrrrr990/openleads | Verify | Query → federated public sources → people → email → dedupe | Candidate | Legal/source/function test |
| REG-039 | Agentic lead-gen pipeline | Revenue | All | Hermes lead-generation pipeline | Agent/skills | GitHub: vivekshetye/hermes-lead-generation-pipeline | Verify | Prospect → scrape → enrich → contact-find → score → outreach | Candidate | Skill extraction/test |

## Sales acquisition coverage

The acquisition layer is now explicitly tracked as a separate capability from downstream sales automation.

`SOURCE DISCOVERY → ACQUISITION → NORMALIZATION → IDENTITY RESOLUTION → ENRICHMENT → VERIFICATION → SIGNALS → ICP/SCORING → CRM → OUTREACH`

### Source families now represented

- Search engines
- Company websites
- LinkedIn
- Google Maps/local businesses
- Instagram
- Facebook/Meta Ads
- X/Twitter
- Reddit
- YouTube
- GitHub
- Business directories
- Review platforms
- Job boards
- Company databases
- Email intelligence
- Technology intelligence
- Advertising intelligence
- Government/public registries
- Tenders/procurement
- Events/conferences
- Associations/chambers
- Partner/referral ecosystems
- News/media
- Communities/forums
- Social listening
- First-party inbound
- Existing databases/files

## Status definitions

- **Candidate:** discovered and mapped; not yet accepted for production.
- **Verified:** source, license/access, maintenance and basic function checked.
- **Tested:** representative functional tests passed.
- **Controlled:** permissions, approvals, audit/evidence and failure handling tested.
- **Adapted:** schemas, prompts, policies or UX adapted to Nivy.
- **Integrated:** connected to intended systems of record/workflows.
- **Pilot:** live/representative limited deployment with monitoring.
- **Production:** approved for operational use.
- **Regression-monitored:** production behavior continuously evaluated.

## Mandatory implementation record

No asset can be promoted to production without:

1. source and provenance
2. license/access decision
3. owner
4. system of record
5. data classification
6. credential/identity method
7. least-privilege permissions
8. human-approval policy
9. failure/exception path
10. audit/evidence capture
11. functional test
12. control/security test
13. cost estimate
14. rollback/kill-switch path
15. regression test

## Core workflow pattern

`Trigger → Context → Agent/Skill → Tool/MCP → Policy Check → Approval (if required) → Action → Verify → Evidence → System-of-Record Update → KPI → Exception → Learning`

## Scale activation

| Scale | Default automation posture |
|---|---|
| Solo/Micro | Simple workflows, low-cost tools, human-in-loop |
| Small | CRM/finance/HR integrations, reusable agents, scheduled automation |
| SMB | Cross-department workflows, role-based access, dashboards, audit trail |
| Mid-market | Shared services, workflow orchestration, formal controls, observability |
| International | Multi-entity, currency/tax/privacy/localization, jurisdiction packs |
| Enterprise | Control plane, SoD, policy-as-code, portfolio governance, resilience |
| Multinational | Regional autonomy under global standards, data residency, cross-border controls, failover |

## Completion rule

The library is not considered implementation-complete merely because an asset was discovered. Completion means the asset has passed the required adoption state for its risk class and scale.
