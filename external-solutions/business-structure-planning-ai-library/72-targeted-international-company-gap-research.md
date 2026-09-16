# Targeted International Company Gap Research

**Status:** v1.0 — 2026-09-16

## Purpose

Close the remaining material capability gaps identified by comparing the existing Nivy reuse library with the operating model of a mature international company.

The goal is **reuse → verify → adapt → integrate**, not to build every capability from scratch.

## Evidence basis

Current operating-model research emphasizes connected end-to-end processes, shared data, governance, controls, people/capabilities and technology rather than isolated departmental automation. Deloitte's 2026 corporate-functions research highlights finance, HR, IT, procurement, risk/compliance, analytics, vendor management and cross-functional transformation as core operating concerns. KPMG's target operating model framework explicitly connects processes, people, service delivery, technology, performance insights/data and governance. McKinsey describes treasury, legal, risk and investor relations as functions commonly centralized at enterprise level. citeturn0search2turn0search7turn0search3

## Newly verified reusable candidates

| Gap | Reusable candidate | What it provides | Reuse status |
|---|---|---|---|
| Corporate Secretary / Board | LQGovernance-OpenBoard | Board documents, meetings, voting, minutes, signatures, tasks, access control, AI proposals with human approval | Candidate; MIT; security review required |
| Corporate governance decisions | Decidiq | Meetings, agendas, motions, amendments, voting, minutes, decision tracking | Candidate; EUPL-1.2; verify fit |
| Corporate/entity information | EIOS | Entity-centered information architecture, governance, provenance, retrieval and portability | Architecture candidate; verify maturity/license |
| Treasury / financial controls | Agent-skills-collection | Treasury operations, working capital, debt, banking relationships, FX, financial controls, audit readiness, internal audit | Skill-source candidate; license/freshness review |
| Treasury/agent payments | Eunomia / Nirium | Policy-bounded agent treasury/payment concepts | Experimental; not a default Nivy finance system |
| Revenue assurance | Rapo | Revenue assurance controls and revenue-leak detection | Candidate; domain-specific, adapt rules |
| Revenue leakage | revenue_leakage_system | Contract-vs-actual billing comparison, deterministic evidence and findings | Candidate; MIT/source review |
| ITSM | Tessio | Tickets, AI triage, routing, knowledge, dashboards, workflows, SLAs, asset inventory, portal | Strong candidate; community AGPL |
| ITSM | FreeITSM | 23 modules including tickets, assets, knowledge, changes, problems, CMDB, LMS and AI | Candidate; MIT |
| GRC / internal audit | security-atlas | Risk, compliance, audit, third-party risk, policy, evidence, board reporting | Architecture candidate; Apache-2.0 |
| AI-enabled GRC | riskready-community | Risk, controls, policies, incidents, audits, evidence, ITSM, organisation governance; MCP servers and human approval | Candidate; security/license review required |
| Enterprise risk/control model | open-investment-model risk/control domain | Risk, compliance, financial crime, AI governance, cyber, resilience, internal control, internal audit, legal/contract management | Reference architecture; verify license |
| ESG / sustainability | sustainability-project | Audit-ready ESG reporting, deterministic multi-agent workflows, claim citations, TSRS/CSRD alignment, board dashboards | Candidate; MIT |
| Corporate legal | legal-skills-open corporate skill | Entity formation, governance, finance, M&A, securities, VC, dissolution and corporate formalities | Strong skill candidate; Apache-2.0; US jurisdiction |
| Board meeting intelligence | board-observer | Board meeting prep, transcription, insights, action/decision detection, summaries | Candidate; verify external dependencies |

## P0 gap conclusions

### 1. Corporate Secretary / Board Management
**Status: reusable path found.**

Use board-governance software plus legal/corporate skills. Do not build board voting/minutes logic unless required after testing. LQGovernance explicitly implements human approval for AI-proposed governance actions and maintains audit trails. citeturn2search0

### 2. Treasury & Banking
**Status: reusable skill layer found; production banking integration remains implementation work.**

Cover liquidity, cash positioning, bank reconciliation, payment controls, FX, debt, banking relationships, working capital and treasury policy. The current skill collection exposes dedicated treasury and control skills. citeturn1search4

### 3. Internal Audit / Controls Testing
**Status: reusable GRC/control paths found.**

Use a control library + evidence collection + audit planning + corrective-action workflow. The three-lines model is a useful control boundary: operations own first-line controls, risk/compliance provide oversight, and internal audit provides independent assurance. citeturn0search1turn1search8

### 4. Corporate Development / M&A
**Status: capability identified; reusable legal/corporate and diligence skills exist, but an integrated M&A agent system should be assembled from research, diligence, valuation, legal and integration components rather than built as one monolith.**

### 5. Enterprise Architecture / Application Portfolio
**Status: still a targeted integration gap.**

Need application inventory, ownership, lifecycle, dependency map, architecture decisions, technology standards, technical debt and SaaS rationalization. Existing IT/AgentOps infrastructure can supply governance, but a dedicated application-portfolio layer should still be tested.

### 6. Software/SaaS Asset Management
**Status: partial.**

Need SaaS inventory, owner, spend, renewal, access, usage, risk, data classification, license and offboarding workflows. This should connect to identity, procurement, finance and ITSM rather than become another isolated database.

### 7. ITSM / Enterprise Service Desk
**Status: reusable path found.**

Tessio provides self-hosted AI ITSM with ticket triage/routing, knowledge, dashboards, workflows, SLAs and asset inventory; FreeITSM provides a broader free/self-hosted module set. citeturn1search1turn1search13

### 8. ESG / Sustainability + Carbon
**Status: reusable path found.**

Use an ESG data/evidence/reporting layer and connect it to finance, procurement, HR, facilities and supply-chain data. The sustainability-project candidate provides audit-ready multi-agent reporting and board dashboards. citeturn1search9

### 9. Revenue Assurance
**Status: reusable path found.**

Add contract-to-billing reconciliation, pricing/discount entitlement checks, usage/overage validation, invoice completeness and leakage detection. Rapo and the revenue-leakage reference implementation provide concrete starting points. citeturn2search2turn2search5

### 10. Corporate Transformation Portfolio
**Status: partial.**

Existing PMO/project systems cover projects, but the enterprise layer needs a portfolio view: strategic objective → initiative → owner → investment → benefits → milestones → risks → dependencies → realization. Treat this as an executive/PMO extension, not a new standalone platform unless testing proves necessary.

### 11. Global Entity/Subsidiary Management
**Status: architecture gap with reusable corporate-law skills.**

Need entity register, jurisdiction, directors/officers, ownership, tax IDs, registrations, licenses, bank accounts, contracts, statutory deadlines, intercompany relationships and beneficial ownership. The corporate legal skill covers formation/governance concepts, while entity-centered information architecture can provide the information model. citeturn2search6turn2search1

## P1 conclusions

| Capability | Result |
|---|---|
| Investor Relations | Reusable corporate/board/document/analytics components; dedicated IR workflow still needed |
| Insurance Management | Gap remains; connect policies, renewals, claims, coverage, risk register and finance |
| Regulatory Reporting | Partial; use compliance evidence + document automation + jurisdiction-specific skills |
| Ethics / Whistleblower | GRC/incident architecture reusable; confidential case workflow required |
| Employee Relations | HR/workforce foundation exists; add grievance/case/confidentiality workflow |
| Global Mobility / Immigration | Dedicated capability still needed; integrate HR, payroll, tax and legal |
| Quality Management / QMS | Gap remains; add QMS, CAPA, nonconformance, audit and document-control workflows |
| SLA Management | ITSM/customer-success candidates provide reusable SLA patterns |
| Facilities / Workplace | Gap remains; integrate assets, vendors, maintenance, access, incidents and workplace requests |
| Corporate Travel / Expense | Finance/procurement/workforce components exist; dedicated travel workflow remains |
| Supply Risk | Procurement + risk + external intelligence components exist; supplier-risk control tower remains |
| Crisis Command Center | Incident/ITSM/GRC patterns exist; enterprise crisis coordination remains |
| R&D / Innovation Portfolio | Product/PMO foundation exists; portfolio/experiment governance remains |
| IP / Patent Portfolio | Legal/document/knowledge components exist; dedicated IP lifecycle remains |
| Global Tax Control Tower | Finance/tax skills exist; multi-jurisdiction calendar/evidence/control tower remains |

## P2 conclusions

These should not block implementation. Keep them as deferred capability packs unless Nivy's operating model or a client engagement makes them material:

- Physical security
- Fleet and physical asset management
- Legal hold / advanced records lifecycle
- Public/government affairs
- Responsible sourcing and supplier sustainability
- Enterprise risk stress testing
- Advanced stakeholder engagement

## Cross-company architecture finding

The new research reinforces that these capabilities should not become isolated applications. Mature operating models connect processes, people, technology, performance/data and governance. citeturn0search7turn0search0

Target composition:

`Corporate Registry + Workforce + Finance/Treasury + Revenue + Procurement + ITSM + GRC + Legal + Knowledge + PMO + Specialist Skills + MCP/API + Approval + Audit + Analytics`

## Discovery decision

The targeted P0 list now has a credible reuse path for most items. The remaining work is primarily **functional testing, integration and jurisdiction-specific adaptation**, not broad discovery.

This file does not claim that every international-company capability is universally required. Relevance depends on company size, ownership, jurisdictions, industry, regulatory status and transaction complexity.
