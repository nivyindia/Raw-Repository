# 76 — Company Scale & Maturity Matrix

**Status:** Research/architecture baseline
**Purpose:** Map the reusable company capability library from micro/SMB needs through mid-market and multinational enterprise needs without creating separate operating systems.
**Model:** One capability architecture; progressive activation and control depth.

## 1. Core principle

The library is intended to scale from:

`SOLO / MICRO → SMALL → SMB → GROWING / MID-MARKET → INTERNATIONAL MID-MARKET → LARGE ENTERPRISE → MULTINATIONAL / GLOBAL ENTERPRISE`

A company should activate only the capabilities justified by its current complexity, risk, transaction volume, jurisdictions, employees, customers, products and regulatory obligations.

This avoids the common failure mode of giving a small company enterprise bureaucracy while still providing a migration path toward enterprise-grade controls.

Current operating-model research supports capability-based, adaptive operating models and increasing maturity from asset/process/service/value/invention orientations. Gartner's current midsize-enterprise IT model explicitly describes Levels 1–5 from Asset through Invention. citeturn0search0turn0search8 Deloitte likewise describes operating models as configurations of capabilities that should adapt to business ambition and changing conditions. citeturn0search16turn0search12

## 2. Scale levels

| Level | Working label | Typical operating pattern | Primary objective |
|---|---|---|---|
| L0 | Solo/Micro | Founder-led, few systems | Survive, sell, deliver, collect |
| L1 | Small | Small team, functional ownership emerging | Repeatable operations |
| L2 | SMB | Departments/teams, formal workflows | Scale revenue without chaos |
| L3 | Growing/Mid-market | Managers, specialized functions, multiple systems | Predictability, efficiency, control |
| L4 | International Mid-market | Multiple countries/entities/markets | Cross-border scale and governance |
| L5 | Large Enterprise | Formal functions, shared services, complex portfolios | Enterprise optimization and risk control |
| L6 | Multinational/Global Enterprise | Global entities, jurisdictions, business units | Global orchestration, resilience and strategic advantage |

## 3. Capability activation matrix

Legend: **Core** = normally required; **Scale** = progressively deepens; **Specialized** = activate when business context requires it.

| Capability | L0 | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|---|
| Strategy & business model | Core | Core | Core | Core | Core | Core | Core |
| Executive planning | Core | Core | Core | Core | Core | Core | Core |
| Goal/OKR management | Core | Core | Core | Core | Core | Core | Core |
| Revenue strategy | Core | Core | Core | Core | Core | Core | Core |
| Sales/CRM | Core | Core | Core | Core | Core | Core | Core |
| Marketing/content | Core | Core | Core | Core | Core | Core | Core |
| RevOps | — | Scale | Core | Core | Core | Core | Core |
| Customer success/support | Scale | Core | Core | Core | Core | Core | Core |
| Product management | Specialized | Specialized | Core | Core | Core | Core | Core |
| Engineering/software delivery | Specialized | Specialized | Core | Core | Core | Core | Core |
| IT/helpdesk | Scale | Core | Core | Core | Core | Core | Core |
| ITSM/CMDB | — | — | Scale | Core | Core | Core | Core |
| Enterprise architecture | — | — | — | Scale | Core | Core | Core |
| Data/BI | Scale | Core | Core | Core | Core | Core | Core |
| Data governance/semantic layer | — | — | Scale | Core | Core | Core | Core |
| Accounting/bookkeeping | Core | Core | Core | Core | Core | Core | Core |
| Billing/AR/AP | Core | Core | Core | Core | Core | Core | Core |
| FP&A/management reporting | — | Scale | Core | Core | Core | Core | Core |
| Treasury/banking | — | — | Scale | Core | Core | Core | Core |
| Tax | Core | Core | Core | Core | Core | Core | Core |
| Global tax/transfer pricing | — | — | — | — | Core | Core | Core |
| Finance controls/close | Scale | Core | Core | Core | Core | Core | Core |
| Revenue assurance | — | — | Scale | Core | Core | Core | Core |
| HR/people records | Scale | Core | Core | Core | Core | Core | Core |
| Workforce/task management | Core | Core | Core | Core | Core | Core | Core |
| Performance/KPI/KRA | Scale | Core | Core | Core | Core | Core | Core |
| Workforce planning | — | Scale | Core | Core | Core | Core | Core |
| Global mobility | — | — | — | Specialized | Core | Core | Core |
| Legal/contracts | Scale | Core | Core | Core | Core | Core | Core |
| Compliance | Specialized | Core | Core | Core | Core | Core | Core |
| GRC/risk management | — | Scale | Core | Core | Core | Core | Core |
| Internal controls | — | Scale | Core | Core | Core | Core | Core |
| Internal audit | — | — | Specialized | Core | Core | Core | Core |
| Board/corporate secretary | — | — | Specialized | Specialized | Core | Core | Core |
| Procurement | Scale | Core | Core | Core | Core | Core | Core |
| Supplier management | — | Scale | Core | Core | Core | Core | Core |
| Supply-risk control tower | — | — | — | Specialized | Core | Core | Core |
| Quality/QMS/CAPA | — | Specialized | Scale | Core | Core | Core | Core |
| ESG/sustainability | — | Specialized | Scale | Core | Core | Core | Core |
| Insurance management | — | — | Specialized | Core | Core | Core | Core |
| Corporate development/M&A | — | — | Specialized | Specialized | Core | Core | Core |
| Investor relations | — | — | — | Specialized | Core | Core | Core |
| Entity/subsidiary management | — | — | — | Specialized | Core | Core | Core |
| IP/patent management | Specialized | Specialized | Scale | Core | Core | Core | Core |
| Facilities/workplace | — | Scale | Core | Core | Core | Core | Core |
| Corporate travel/expense | — | Scale | Core | Core | Core | Core | Core |
| Corporate communications | Scale | Core | Core | Core | Core | Core | Core |
| Crisis command | — | — | Specialized | Core | Core | Core | Core |
| Business continuity/DR | — | Scale | Core | Core | Core | Core | Core |
| Security/cyber | Scale | Core | Core | Core | Core | Core | Core |
| Privacy/data protection | Specialized | Core | Core | Core | Core | Core | Core |
| Knowledge management | Core | Core | Core | Core | Core | Core | Core |
| SOP/process management | Core | Core | Core | Core | Core | Core | Core |
| Automation/workflow | Core | Core | Core | Core | Core | Core | Core |
| AI agents/copilots | Scale | Core | Core | Core | Core | Core | Core |
| Agent governance/AgentOps | — | Scale | Core | Core | Core | Core | Core |
| A2A/multi-agent orchestration | — | — | Scale | Core | Core | Core | Core |
| Enterprise portfolio/transformation | — | — | — | Scale | Core | Core | Core |
| Benefits realization | — | — | — | Scale | Core | Core | Core |

## 4. Depth changes by scale

The same capability does not mean the same implementation.

### Example: Finance

- **L0:** invoice, expense, bank reconciliation, tax records.
- **L1:** bookkeeping, AP/AR, payroll coordination, monthly reporting.
- **L2:** close calendar, budgets, cash forecast, management reporting.
- **L3:** FP&A, controls, treasury, working capital, scenario planning.
- **L4:** multi-entity consolidation, FX, intercompany, international tax.
- **L5:** treasury controls, tax control tower, internal audit, revenue assurance, formal financial governance.
- **L6:** global treasury architecture, entity-level controls, transfer pricing governance, global statutory/regulatory orchestration.

### Example: HR/workforce

- **L0:** people records + tasks.
- **L1:** roles, JDs, onboarding, leave, performance basics.
- **L2:** KRAs/KPIs, manager dashboards, learning, workforce planning.
- **L3:** talent architecture, compensation, analytics, succession.
- **L4:** country employment/payroll/mobility packs.
- **L5:** global workforce governance and shared services.
- **L6:** global mobility, workforce risk, regional operating models and enterprise workforce analytics.

### Example: IT

- **L0:** devices, email, access, basic support.
- **L1:** ticketing, asset register, backups, security baseline.
- **L2:** ITSM, knowledge base, workflows, SLA, asset/CMDB foundations.
- **L3:** service portfolio, architecture standards, data/AI governance.
- **L4:** multi-country infrastructure, security/privacy and continuity.
- **L5:** enterprise architecture, application/SaaS portfolio, resilience and IT financial governance.
- **L6:** global technology operating model, architecture governance and strategic technology portfolio.

## 5. Maturity dimensions

Every capability should be evaluated on more than company size:

1. **Process maturity** — ad hoc → documented → standardized → optimized → adaptive.
2. **Automation maturity** — manual → assisted → workflow automation → agentic → autonomous within policy.
3. **Data maturity** — scattered → structured → integrated → governed → intelligence/semantic layer.
4. **Control maturity** — founder approval → role approval → segregation of duties → formal control testing → continuous assurance.
5. **Governance maturity** — informal → management → functional → enterprise → board/global.
6. **Scale maturity** — one team → departments → multiple entities → global business units.
7. **AI maturity** — individual copilot → departmental agents → governed multi-agent workflows → enterprise orchestration.
8. **Resilience maturity** — backup → documented recovery → tested continuity → cross-system resilience → enterprise crisis orchestration.

## 6. Activation rule

Do not activate a capability merely because a larger company has it.

Activate when one or more triggers exist:

- transaction volume makes manual work unreliable;
- headcount creates management complexity;
- multiple teams require coordination;
- multiple products/markets create operational complexity;
- multiple countries/entities create statutory/tax/banking complexity;
- financial/material risk requires stronger controls;
- customers/contracts require formal SLAs or evidence;
- regulators/auditors/boards require formal governance;
- business continuity risk becomes material;
- AI/automation creates a need for governance and traceability.

## 7. Architecture rule

Never create seven independent Company OS products.

Use one composable architecture:

`Company OS`

→ Systems of Record  
→ Workflow/Automation Engine  
→ Knowledge & Memory  
→ Specialist Skills  
→ AI Agents/Copilots  
→ MCP/API/Tool Gateway  
→ Identity & Permissions  
→ Approval/Delegation  
→ Audit/Evidence  
→ Evaluation/Regression  
→ Analytics/KPIs  
→ Cost/Usage  
→ Exceptions/Escalation  
→ Business Continuity

Only the **depth, controls, integrations and number of activated capabilities** should increase with scale.

## 8. Nivy implementation implication

For Nivy, this becomes a **progressive capability activation system**:

`DISCOVER → CLASSIFY SCALE → VERIFY → TEST → SELECT → ADAPT → INTEGRATE → PILOT → PROMOTE`

Every reusable asset should receive:

- minimum scale;
- maximum useful scale;
- capability;
- maturity level;
- license;
- deployment model;
- dependencies;
- data sensitivity;
- human approval requirement;
- audit requirement;
- integration requirements;
- replacement/upgrade path.

## 9. Completeness conclusion

The existing research is now structured to cover both ends of the spectrum:

**small operational details** → **department systems** → **company-wide operating model** → **international complexity** → **enterprise governance** → **multinational orchestration**.

This should be treated as the scale/maturity overlay on top of the existing capability library, not as another standalone operating system.

## Sources

- Gartner, IT Operating Model Assessment for Midsize Enterprises — current five-level model from Asset through Invention. citeturn0search0turn0search2
- Deloitte, Rewiring the enterprise operating model for AI scale — 2026 research on changing operating models, human ownership, governance and AI-generated work. citeturn0search12
- Deloitte, Designing an Operating Model for Changing Market Needs — capability-based, adaptive operating model definition. citeturn0search16
- Deloitte, Architecting an operating model — example showing differentiated SMB/enterprise lines, shared services, business operations and AI/robotics enablement. citeturn0search24
