# Master Reuse Library Index

**Status:** v1.6 — 2026-09-16

## Purpose

This is the master navigation layer for the Existing Business Structure, Planning & AI Asset Library. It connects external reusable assets to company capabilities, departments, workflows, implementation destinations, controls, and adoption status.

**Core rule:** `DISCOVER → EVALUATE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING`

## Library layers

| Layer | Files | Purpose |
|---|---|---|
| Discovery | 01, 05, 07, 08, 15 | Sources, scope, research coverage and tracking |
| Capability | 02, 09, 18, 19 | What work can be reused |
| Asset extraction | 10–14, 22–23, 25, 28–29 | Agents, skills, prompts, SOPs, templates, workflows and systems |
| Evaluation | 04, 20, 24, 26, 30 | Licensing, quality, controls and adoption |
| Architecture | 27, 31, 60–65 | Connectors, approvals, systems of record and cross-company AI infrastructure |
| Workforce | 67–68 | Employee/manager/department dashboards, roles, responsibilities, KRA/KPI, daily work and workforce AI |
| Completeness audit | 69–71, 74–76 | Ideal-company capability audit, missing-capability backlog, capability model, enterprise audit and scale maturity |
| Targeted gap research | 72–73 | P0/P1 missing-capability research and adoption map |
| Execution registry | 77–80 | Master asset/automation registry, coverage matrix, connector registry and production-readiness backlog |
| Implementation | 81–85 | Foundation plan, P0 workflow specs, control plane, evaluation suite and scale/country activation |
| Master navigation | 32–33, 66 | Unified index, roadmap and cross-company gap analysis |

## Execution layer

- **77** — Master Automation & Implementation Registry
- **78** — Automation Coverage Matrix
- **79** — Integration & Connector Registry
- **80** — Production Readiness Backlog
- **81** — Automation Foundation Implementation Plan
- **82** — P0 Workflow Implementation Specifications
- **83** — Agent Control Plane Implementation Specification
- **84** — Automation Test & Evaluation Suite
- **85** — Scale & Country Activation Runbook

The execution layer explicitly distinguishes:

`Coverage ≠ Automation ≠ Production Automation`

## Standard adoption state

`DISCOVERED → SOURCE-VERIFIED → LICENSE-CHECKED → FUNCTION-TESTED → CONTROL-TESTED → Nivy-ADAPTED → INTEGRATED → PILOT → PRODUCTION → REGRESSION-MONITORED`

## Standard asset record

`asset_id, asset_name, asset_type, department, capability, source_publisher, source_url, license_or_access, maintenance_status, required_inputs, outputs, connectors, permissions, data_sensitivity, human_approval, reuse_mode, nivy_destination, test_status, adaptation_status, production_status, last_verified`

## Cross-company architecture rule

The target is not one giant autonomous agent. It is:

`Registry + Identity + Policy + Router + Specialist Agents/Skills + Knowledge/Memory + MCP/API + Workflows + Approval + Audit + Evaluation + Cost + Exceptions + Systems of Record`

## Discovery stop condition

Do not perform another broad discovery round unless a new capability, jurisdiction, industry requirement, obsolete candidate, materially better reusable asset, or genuine implementation gap appears during testing.
