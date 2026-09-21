# Raw Repository Organization — Execution Tracker

**Project status:** PLAN CREATED / EXECUTION PENDING
**Last updated:** 2026-09-16

## Current checkpoint

| Phase | Status | Notes |
|---|---|---|
| Plan | DONE | Master plan and operating model created |
| Initial source analysis | DONE | Structural and semantic patterns sampled from repository |
| Target structure | DONE | Brand-first + knowledge-domain model defined |
| Migration rules | DONE | Classification, rename, duplicate and safety rules defined |
| Full inventory | NOT STARTED | Must be generated from the actual repository tree |
| Classification map | NOT STARTED | Pending full inventory/content scan |
| First migration batch | NOT STARTED | Do only after inventory + classification |
| Verification | NOT STARTED | Batch-level verification required |
| Promotion mapping | NOT STARTED | Separate from raw organization |

## Suggested batch tracker

| Batch | Scope | State | Evidence | Commit |
|---|---|---|---|---|
| B00 | Control/plan files | COMPLETE | Organization plan files created | See git history |
| B01 | Full inventory | PENDING | — | — |
| B02 | High-confidence brand-owned docs | PENDING | — | — |
| B03 | Knowledge-domain docs | PENDING | — | — |
| B04 | Export/duplicate mapping | PENDING | — | — |
| B05 | Ambiguous/unclassified review | PENDING | — | — |
| B06 | Index/link verification | PENDING | — | — |
| B07 | Promotion mapping | PENDING | — | — |

## Required tracker outputs

### Inventory fields
`source_path`, `filename`, `extension`, `size`, `hash`, `source_system`, `suspected_brand`, `suspected_domain`, `artifact_type`, `duplicate_group`, `confidence`, `state`

### Migration fields
`source_path`, `destination_path`, `classification`, `reason`, `confidence`, `batch`, `status`, `verified`, `commit`

## Resume point

Next agent should begin with **B01 — Full inventory**. Do not infer completion of B01 from the existing GitHub tree response; generate and record a complete inventory from the repository itself.
