# Automation Foundation Implementation Plan

**Status:** v1.0 — 2026-09-16

## Objective

Move the library from documented reuse into controlled execution without prematurely building a giant platform.

## Architecture

`Systems of Record → n8n/integration layer → governed tool/MCP layer → specialist agents/skills → knowledge/memory`

Cross-cutting: `identity → permissions → policy → approval → audit → observability → cost → exceptions`

## Implementation waves

### Wave 0 — Foundation

1. Freeze the master registry schema.
2. Assign owner/status to every P0 asset.
3. Define canonical IDs and correlation IDs.
4. Define system-of-record ownership by business object.
5. Define agent autonomy levels: Recommend → Approve → Guided Execute → Bounded Autonomous.
6. Define approval classes: none, low-risk, financial, external communication, destructive/security-sensitive.
7. Define audit event schema.
8. Define exception and retry contract.
9. Define secrets rule: credentials never stored in Git, prompts or documents.

### Wave 1 — Revenue spine

Implement first:

`Lead intake → normalize → enrich/research → CRM → qualify → outreach draft → human approval → send → response capture → calendar → meeting prep → debrief → CRM update → follow-up`

### Wave 2 — Delivery spine

`Won deal → handoff → intake → project/task creation → SOP/context retrieval → delivery work → QA → client update → invoice trigger → customer-success handoff`

### Wave 3 — Finance/workforce

`CRM/order → invoice → accounting → reconciliation → cash snapshot`

`Candidate → employee → role → goals/KRA/KPI → tasks → evidence → review → learning`

### Wave 4 — Governance/IT

`Contract/risk/control → evidence → review → approval → audit`

`Ticket → classify → route → SLA → resolve → knowledge`

### Wave 5 — Executive control loop

`Metrics/events → exceptions → executive brief → decision → assignment → verification → learning`

## Non-negotiable design rules

- One system of record per master object.
- Read and write permissions are separate.
- External communication starts human-approved.
- Financial movement starts human-approved.
- Agents receive minimum required tools.
- Every production action has a traceable actor and outcome.
- Retries must be idempotent.
- Every critical workflow has a human fallback.
- Production and experimental assets are separated.
- No autonomous agent gets broader permissions merely because another agent requested them.

## Definition of completion

Foundation is complete when a P0 workflow can pass functional, control, operational and economic tests and can be disabled or rolled back safely.
