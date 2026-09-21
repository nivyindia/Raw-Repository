# Branch Workflow

Branches are workflow/state controls, not substitutes for folders.

## Recommended Branches

| Branch | Purpose |
|---|---|
| `main` | Stable canonical control system |
| `intake` | New raw research ingestion |
| `research/*` | Active research and analysis work |
| `curation/*` | Curated/reconciled research |
| `validation/*` | Validation of transfer-ready assets |
| `promotion/*` | Preparing changes for destination repositories |
| `archive/*` | Historical snapshots when needed |

## Default Flow

```text
main
  ↓
intake
  ↓
research/<topic>
  ↓
curation/<topic>
  ↓
validation/<topic>
  ↓
promotion/<destination>-<topic>
  ↓
PR / review
  ↓
main
```

## Rules

1. Do not create a branch merely to store a folder.
2. Use a branch when work is actively changing or being reviewed.
3. Do not delete raw source material after promotion.
4. A promoted asset must retain a provenance pointer back to its source record.
5. A destination repository owns its final implementation; Research-Repository owns the research lineage.
6. Merge/review state must not be confused with research quality. Quality is recorded in validation metadata.
