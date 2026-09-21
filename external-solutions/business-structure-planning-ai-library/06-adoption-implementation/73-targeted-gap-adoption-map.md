# Targeted Gap Adoption Map

**Status:** v1.0 — 2026-09-16

## Objective

Map each newly identified international-company capability to reuse, compose, adapt or defer decisions.

| Capability | Priority | Existing Nivy coverage | External reuse path | Decision | Next action |
|---|---:|---|---|---|---|
| Board / Corporate Secretary | P0 | Partial | LQGovernance, Decidiq, corporate legal skills | REUSE/ADAPT | Controlled test |
| Treasury / Banking | P0 | Partial | Treasury/working-capital/FX/control skills; finance systems | COMPOSE | Map banking connectors |
| Internal Audit / Controls | P0 | Partial | GRC + audit + control skills | COMPOSE | Build control/evidence test set |
| Corporate Development / M&A | P0 | Partial | Corporate legal + diligence + finance + research skills | COMPOSE | Create M&A workflow pack |
| Enterprise Architecture | P0 | Partial | IT governance + knowledge + project assets | ADAPT | Create application portfolio schema |
| SaaS Asset Management | P0 | Partial | ITSM + procurement + finance + identity | COMPOSE | Create SaaS lifecycle workflow |
| ITSM | P0 | Partial | Tessio / FreeITSM | REUSE | Technical pilot |
| ESG / Carbon | P0 | Partial | sustainability-project + reporting/data layer | REUSE/ADAPT | Evidence/data model test |
| Revenue Assurance | P0 | Partial | Rapo + revenue leakage reference | REUSE/COMPOSE | Contract-to-billing test |
| Transformation Portfolio | P0 | Partial | PMO/project + executive OS | ADAPT | Portfolio schema |
| Entity/Subsidiary Management | P0 | Partial | EIOS + corporate legal skills | COMPOSE | Entity registry schema |
| Investor Relations | P1 | Partial | Board/docs/analytics + IR workflows | COMPOSE | Research/test |
| Insurance | P1 | Gap | Finance/risk/legal components | BUILD-ADAPTER | Policy/claims schema |
| Regulatory Reporting | P1 | Partial | Compliance/document/evidence skills | COMPOSE | Jurisdiction packs |
| Ethics / Whistleblower | P1 | Partial | GRC/incidents/approval | ADAPT | Confidential case workflow |
| Employee Relations | P1 | Partial | Workforce/HR skills | ADAPT | ER case workflow |
| Global Mobility | P1 | Partial | HR/payroll/tax/legal | COMPOSE | Country pack research |
| QMS | P1 | Partial | SOP/process/audit assets | COMPOSE | CAPA/QMS candidate search |
| SLA Management | P1 | Partial | ITSM/customer success | REUSE/ADAPT | SLA engine test |
| Facilities | P1 | Gap | Operations/procurement/assets | COMPOSE | Facilities workflow research |
| Travel/Expense | P1 | Partial | Finance/procurement/workforce | COMPOSE | Travel policy + expense workflow |
| Supply Risk | P1 | Partial | Procurement/risk/intelligence | COMPOSE | Supplier risk control tower |
| Crisis Command | P1 | Partial | ITSM/GRC/incident patterns | ADAPT | Crisis command workflow |
| R&D/Innovation | P1 | Partial | Product/PMO/knowledge | ADAPT | Innovation portfolio schema |
| IP/Patents | P1 | Partial | Legal/document/knowledge | COMPOSE | IP lifecycle research |
| Global Tax Control Tower | P1 | Partial | Finance/tax skills + evidence | COMPOSE | Jurisdiction calendar/control model |

## Reuse gates

1. Verify source and license.
2. Run technical/security review.
3. Test representative workflows.
4. Test permissions and approval behavior.
5. Measure human correction rate.
6. Measure cost/latency.
7. Integrate with system of record.
8. Pilot before production.

## High-value composition patterns

### Corporate governance
`Entity Registry → Board Portal → Agenda/Document Intelligence → AI Proposal → Secretary Approval → Vote/Resolution → Signed Record → Action Tracking → Audit`

### Treasury
`Bank Feeds → Cash Position → Reconciliation → Liquidity Forecast → Risk/Policy Checks → Payment Proposal → Approval → Bank Action → Accounting → Audit`

### Internal audit
`Risk Register → Control Library → Audit Plan → Evidence Request → Evidence Collection → Test → Finding → Corrective Action → Retest → Board Report`

### Revenue assurance
`Contract → Pricing/Entitlements → Usage → Invoice → Payment → Expected-vs-Actual Check → Leakage Finding → Owner → Recovery/Correction → Evidence`

### IT service management
`Employee/Customer Request → AI Triage → Knowledge → Assignment → Workflow → SLA → Resolution → Verification → Knowledge Capture → Analytics`

### Entity management
`Group → Entity → Jurisdiction → Ownership → Officers → Registrations → Tax IDs → Banks → Contracts → Compliance Calendar → Evidence → Renewal/Escalation`

### ESG
`Source Data → Validation → Evidence → Calculation → Claim → Review → Report → Board/Stakeholder Approval → Publication → Audit Trail`

## Priority implementation rule

Do not create 20 new systems. First compose these capabilities from the existing Nivy control plane, knowledge layer, workflow engine, HR/finance/CRM/PMO systems and specialist reusable assets.
