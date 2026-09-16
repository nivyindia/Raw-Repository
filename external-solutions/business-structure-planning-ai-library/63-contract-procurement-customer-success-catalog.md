# Contract, Procurement & Customer Success Catalog

**Status:** v1.0 — 2026-09-16

| Domain | Capability | Reusable asset/source | Nivy workflow | Priority |
|---|---|---|---|---:|
| Legal | Contract intake | CLM/contract-agent patterns | intake → classify → route | P1 |
| Legal | Contract review | legal skills / CLM agents | extract → compare → risk flags → review | P1 |
| Legal | Obligation tracking | CLM patterns | obligation → owner → deadline → alert | P1 |
| Legal | NDA triage | corporate skill libraries | classify → standard/nonstandard → route | P1 |
| Procurement | RFP creation | proposal/RFP skills | brief → RFP → review → issue | P1 |
| Procurement | Vendor discovery | BizOps/vendor skills | requirements → research → shortlist | P1 |
| Procurement | Vendor evaluation | scorecard skills | evidence → scoring → recommendation draft | P1 |
| Procurement | Purchase workflow | ERP operations patterns | request → approval → order → receipt → invoice | P1 |
| Customer Success | Onboarding | customer-success skills | won deal → intake → kickoff → success plan | P0 |
| Customer Success | Ticket triage | customer-support skills | intake → classify → route → resolve/escalate | P0 |
| Customer Success | Escalation | support/CS skills | evidence pack → owner → SLA → resolution | P0 |
| Customer Success | QBR | CS skills | usage/outcomes → risks → QBR draft | P1 |
| Customer Success | Churn risk | CS analytics | signals → risk review → action plan | P1 |
| Customer Success | Knowledge capture | support workflows | resolved case → KB draft → approval → publish | P1 |

## Contract lifecycle

`Request → Intake → Classification → Draft/Template → Redline → Risk Review → Approval → Signature → Obligation Tracking → Renewal/Expiry → Archive`

## Procurement lifecycle

`Need → Specification → Supplier Discovery → RFP/RFQ → Evaluation → Approval → PO/Contract → Delivery → Receipt → Invoice → Reconciliation → Supplier Review`

## Customer-success lifecycle

`Won → Handoff → Onboarding → Adoption → Health Monitoring → Value Review → QBR → Renewal/Expansion → Advocacy`

## Reusable sources already discovered

- Corporate Claude skill collections include contract review, NDA triage, compliance, vendor management, RFP builder, vendor evaluation and customer-success workflows.
- Draft Legal is an open-source agent-first contract lifecycle management system with specialized intake/drafting/negotiation/approval/signature/obligation agents; verify current license and production maturity before reuse.
- WorkWit-AI-Agent is a self-hosted open-source multi-skill agent platform with MCP connectors and governance features; verify license and security before reuse.
- Customer-success skill patterns cover ticket triage, escalation, onboarding, QBR, churn analysis, customer research and knowledge management.

## Adoption rule

Legal and procurement agents should produce evidence-backed drafts and routing decisions, not silently make binding commitments. Customer-facing actions should use approval policies until accuracy and escalation performance are demonstrated.
