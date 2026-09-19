# Scale & Country Activation Runbook

**Status:** v1.0 — 2026-09-16

## Purpose

Activate only the controls and complexity required by company size, jurisdiction and industry.

## Scale activation

| Scale | Activate first | Control depth |
|---|---|---|
| Solo/Micro | CRM, communication, invoicing, task automation | Human-in-loop |
| Small | CRM + accounting + calendar + basic HR | Role-based access + audit |
| SMB | Cross-department workflows + dashboards | Formal approvals + exception queue |
| Mid-market | Shared services + data/knowledge layer | Strong identity, observability, controls |
| International | Multi-entity + currencies + tax/privacy/localization | Jurisdiction-aware controls |
| Enterprise | Control plane + SoD + policy-as-code | Formal governance + resilience |
| Multinational | Regional operating models + data residency + failover | Global standards + regional autonomy |

## Country pack schema

Each activated country pack contains:

`country → entity rules → tax/VAT/GST → employment/payroll → privacy/data → contracts → licenses → banking/FX → reporting calendars → localization → retention → responsible owner → source dates`

## Industry pack schema

`industry → regulatory obligations → customer data rules → required licenses → standard contracts → quality controls → reporting → security controls → prohibited/approval actions → evidence requirements`

## Activation rule

Do not create all country packs in advance. Create a pack when a market is commercially active or legally required.

## International baseline

For every active jurisdiction verify:

1. entity/subsidiary obligations
2. tax and indirect tax
3. employment/payroll
4. privacy/data residency
5. banking/FX
6. contract/local law requirements
7. licenses/registrations
8. statutory calendars
9. records/retention
10. cross-border transfer requirements

## Resilience activation

Critical international workflows additionally require:

- backup/restore test
- provider failover plan
- connector outage fallback
- regional degradation mode
- incident escalation
- data recovery objective
- agent quarantine/kill switch

## Rule

The company-scale matrix determines **how much control** is required; country and industry packs determine **which local controls** are required.
