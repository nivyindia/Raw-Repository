# Reuse Adoption Backlog

Research date: 2026-09-16

## Objective

Turn discovery into a practical backlog. Each item should be tested before custom development is considered.

| Priority | Work item | Reusable source | Nivy action | Acceptance test |
|---|---|---|---|---|
| P0 | Sales research + call prep | Anthropic Sales Plugin | Adapt skills to Nivy ICP/CRM | Produces research brief + call plan from a target account |
| P0 | Lead triage | Sales / Business Skills | Adapt | Produces explainable lead-priority output from defined ICP |
| P0 | Outreach drafting | Sales Plugin | Adapt | Generates personalized sequence using approved messaging |
| P0 | Campaign planning | Marketing Plugin | Adapt | Produces campaign brief, calendar and KPIs |
| P0 | SEO audit | Marketing Plugin | Adapt | Produces repeatable technical/content/competitor audit |
| P0 | Content engine | Marketing + Business Skills | Adapt | Brief → content → brand review → approval |
| P0 | CRM/pipeline review | Sales Plugin | Integrate | Weekly pipeline report with risks and actions |
| P1 | Client onboarding | Operations + Customer Support patterns | Adapt | Intake → project setup → task creation → welcome pack |
| P1 | SOP generator | Operations Plugin + SOP frameworks | Adapt | Process notes → validated SOP with owner/inputs/outputs/QC |
| P1 | Customer support triage | Customer Support Plugin | Adapt | Classifies, retrieves context and drafts response |
| P1 | Invoice follow-up | Small Business Plugin | Adapt | Identifies overdue invoices and drafts approval-gated reminders |
| P1 | Monthly finance close | Finance / Small Business Plugin | Evaluate with accounting controls | Reconciliation + exception list + close packet |
| P1 | HR onboarding | HR Plugin | Adapt | Role/start date → onboarding plan/checklist |
| P2 | Contract triage | Claude for Legal | Study/adapt with legal review | Flags clauses and produces review checklist |
| P2 | Executive briefing | Productivity + Enterprise Search | Adapt | Aggregates approved company data into weekly briefing |
| P2 | Data analyst | Data Plugin | Integrate | Question → SQL → validation → chart/report |
| P2 | Product research | Product Plugin | Adapt | Research → synthesis → requirements/decision memo |

## Standard test sequence

1. Run source asset unchanged where licensing and environment permit.
2. Record inputs, outputs, connectors and permissions.
3. Test on synthetic/sanitized data.
4. Measure quality against a predefined acceptance test.
5. Adapt terminology, company policy and output schemas.
6. Add human approval where the action is consequential.
7. Integrate with Nivy systems.
8. Version the adapted asset.
9. Add regression tests.
10. Only build custom components for remaining gaps.

## Build trigger

Custom development is justified when:

- no suitable reusable asset exists;
- the reusable asset cannot meet a required control or integration;
- licensing prevents required use;
- reliability is insufficient after adaptation;
- or the capability is a strategically differentiating Nivy component.

## Evidence requirement

Every adopted asset must retain its source URL, original publisher, license/access status, adaptation date and Nivy version.