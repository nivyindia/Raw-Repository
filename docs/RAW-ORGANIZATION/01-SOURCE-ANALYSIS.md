# Raw Repository — Initial Source Analysis

**Date:** 2026-09-16
**Scope:** Initial structural/content scan used to design the organization implementation plan.

## Observed source patterns

The repository contains multiple generations and formats of source material:

| Pattern | Evidence / examples | Organization implication |
|---|---|---|
| Brand folders | `Nivy Advisory`, `Nivy Next`, `Nivy Global`, `Nivy Jobs`, `Nivy Nexus`, `Nivy Academy`, `Nivy Artisan` | Strong candidate for brand-first grouping |
| Generic knowledge folders | `Brand Systems`, `Nivy Research Data`, `All Communities` | Must be classified by content, then attached to brand or cross-brand knowledge |
| Notion export container | `Notion - Nivy OS` | Treat as source-system/provenance, not final taxonomy |
| Export subtrees | `All Communities/Export-*` and similar | Detect duplicates and retain provenance |
| UUID/Notion-ID filenames | e.g. `Nivy c0a...md`, long numeric suffixes | Normalize names only after content classification |
| Repeated workspace records | Similar `Nivy` membership files appear under several folders | Likely export duplicates; map, don't delete initially |
| Brand-specific operating material | Nivy Advisory OS, brand content, website structure, online presence plans | Group by brand + knowledge domain |
| Repository controls | `docs/REPO-CONTROL/*`, `WORK-STATUS.md`, README | Keep operational controls outside migrated source content |

## Evidence from search

- The repository README defines the repository as a source warehouse for historical documents, research, plans, drafts, exports and references, and explicitly requires preservation and reconciliation. fileciteturn3file0L2-L2
- `WORK-STATUS.md` says raw material is not implementation proof and points implementation truth to the canonical AIOS plan. fileciteturn6file0L2-L2
- The master instructions require preservation of old documents, cross-file discovery, verification, synchronized control files, and commit evidence. fileciteturn7file0L2-L2
- The source index currently uses broad searches for plans, instructions, tasks, progress, blockers, tests and tracking rather than a semantic brand/knowledge index. fileciteturn8file0L2-L2
- Search found Nivy Advisory content spread across a dedicated brand folder, `Notion - Nivy OS`, and `Nivy Research Data`, including brand profile, website structure, color palette, content, online-presence planning, email sequences and an operating system. fileciteturn9file1L17-L24 fileciteturn9file3L56-L64 fileciteturn9file6L126-L133 fileciteturn9file9L169-L176
- Search also found the same general Nivy workspace record pattern under multiple brand/export folders, confirming that export metadata and duplicated structural artifacts should not be mistaken for separate business knowledge. fileciteturn5file0L2-L9 fileciteturn5file2L28-L35 fileciteturn5file5L67-L74

## Initial classification model

Every source item should receive these fields before migration:

```yaml
source_path:
source_filename:
source_system:
brand:
knowledge_domain:
artifact_type:
lifecycle_state:
confidence:
duplicate_group:
version_group:
related_files:
promotion_target:
notes:
```

## Initial knowledge domains

These are working categories, not final truth:

- Company / corporate
- Brand systems
- Strategy / business model
- Research / market intelligence
- Marketing / content
- Sales / lead generation
- Website / digital presence
- Operations / SOPs
- Finance / accounting / tax
- Technology / software
- AI / automation / agents
- HR / people / hiring
- Communities / partnerships
- Education / academy
- Legal / compliance
- Projects
- General reference

## Initial brand candidates

The first pass should investigate, at minimum, the brands/entities surfaced by the repository itself: Nivy Global, Nivy Advisory, Nivy Next, Nivy Nexus, Nivy Jobs, Nivy Academy, Nivy Artisan, plus any additional entities discovered from content. `Other`, `Personal`, and `Unknown` must not be used as lazy buckets; they require an explicit classification reason.

## Important conclusion

The raw repository should **not** simply be renamed into brand folders. It needs a two-layer model: preserved source/provenance plus an organized semantic view. This prevents the same export from being repeatedly reclassified and prevents loss of historical context.
