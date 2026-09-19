# P2 Reuse & Adoption Backlog

**Date:** 2026-09-16
**Rule:** Reuse → Adapt → Integrate → Build only what is missing.

## Priority backlog

| Priority | Work item | Source | First action | Control |
|---|---|---|---|---|
| P0 | Contract/NDA triage | Claude for Legal | Run against synthetic agreements | Lawyer/authorized reviewer |
| P0 | Customer ticket triage | Knowledge Work customer-support | Test routing accuracy | Escalation gate |
| P0 | Customer-context brief | Customer-support | Connect approved CRM/helpdesk data | Least privilege |
| P0 | AI use-case inventory | Claude for Legal | Create Nivy AI register | Compliance owner |
| P1 | Contract renewal watcher | Claude for Legal | Test reminders on sample register | No autonomous termination |
| P1 | Regulatory monitoring | Claude for Legal | Select authoritative feeds | Verify primary sources |
| P1 | Resolution → KB | Customer-support | Test article generation | QA before publish |
| P1 | Product spec workflow | Knowledge Work product-management | Test with one internal product | Product-owner approval |
| P1 | User research synthesis | Product-management | Test on historical/synthetic notes | Source traceability |
| P1 | Executive briefing | Productivity | Test daily/weekly brief | Human review |
| P2 | Data analyst workflow | Data plugin pattern | Define approved datasets/connectors | Reproducibility |
| P2 | Cross-functional launch workflow | Compose existing skills | Pilot one launch | Launch owner |
| P2 | Monthly business review | Compose CRM+marketing+finance+ops+CS | Build report template | Metric validation |

## Standard validation sequence

1. Confirm source and license/access terms.
2. Inspect actual skill/agent/workflow implementation.
3. Record connectors, permissions and data sensitivity.
4. Run unchanged on synthetic or sanitized data where permitted.
5. Measure output quality against explicit acceptance criteria.
6. Adapt terminology, policies, schemas and Nivy approval gates.
7. Integrate with n8n/Odoo/Notion/GitHub/approved systems as appropriate.
8. Add logging, provenance and rollback/approval controls.
9. Pilot in controlled production.
10. Version and regression-test.
11. Build custom code only for proven gaps.

## Do not automate without approval

- Legal conclusions or binding commitments
- Regulatory filings
- Contract acceptance/signature
- Irreversible financial/accounting postings
- Unrestricted external communications
- Sensitive HR decisions
- Material customer commitments
- Autonomous deletion or destructive system changes

## Definition of done

A reuse item is **adopted** only when the source, license, inputs, outputs, permissions, test evidence, human gate, integration location and owner are documented.
