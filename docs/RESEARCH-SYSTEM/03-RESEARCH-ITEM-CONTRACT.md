# Research Item Contract

Every meaningful research item should eventually have enough metadata for another AI or human to understand what it is and where it came from.

## Minimum Metadata

```yaml
id: RR-YYYYMMDD-NNNN
title:
type: agent|skill|workflow|prompt|dashboard|document|repo|integration|other
status: intake|research|curated|validation|transfer-ready|promoted|archived
source:
  url:
  repository:
  path:
  branch:
  captured_at:
provenance:
  original_source:
  discovered_from:
  source_notes:
target:
  destination_repo:
  destination_path:
  destination_type:
assessment:
  reuse: unknown|yes|no
  adaptation: none|minor|major
  duplication: none|possible|confirmed
  validation: pending|passed|failed
  gap: false|true
actions:
  next:
  owner:
  notes:
```

## Required Questions

1. What is this?
2. Where did it come from?
3. Is it already present somewhere in Nivy?
4. Can it be reused as-is?
5. If not, can it be adapted?
6. What dependencies or licenses apply?
7. Where should it ultimately live?
8. What remains missing?
9. What evidence supports the assessment?
