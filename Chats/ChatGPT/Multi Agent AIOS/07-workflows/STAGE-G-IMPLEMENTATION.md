# Stage G — Tier-1 Workflow Implementation

## Scope
25 core/cross-functional workflows from the v2 build order: 24 core + 5 cross-functional.

## Completed in this pass
- G.x.1 reuse/source decision encoded through canonical workflow specifications.
- G.x.6 workflow.yaml specification created for all 29 workflows.
- Workflow registry created/updated with IDs, names, versions and status.
- Standardized trigger, inputs, outputs, deterministic steps, tools, error policy, approval and emitted events.

## Remaining execution work
- G.x.2 Build actual n8n canvas skeletons.
- G.x.3 Wire live Odoo/PostgreSQL/Qdrant/service credentials.
- G.x.4 Add live retry/dead-letter/error handling nodes.
- G.x.5 Execute test events end-to-end and verify outputs.
- Only after G.x.5 passes should registry status become `100`.

## Important
`spec_ready` is intentional. This repository pass does not claim live n8n execution or production readiness. Credentials/runtime infrastructure and E2E tests must be performed in the deployment environment.

## Build order
WF001, WF002, WF003, WF004, WF005, WF006, WF007, WF008, WF009, WF010, WF011, WF017, WF018, WF019, WF020, WF022, WF023, WF024, WF025, WF029, WF030, WF033, WF034, WF035, WF036, XW001, XW002, XW010, XW014, XW015
