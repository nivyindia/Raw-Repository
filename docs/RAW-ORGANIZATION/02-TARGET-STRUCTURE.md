# Target Structure

## Design principle

**Brand first, knowledge second, document type third, lifecycle fourth.**

Do not create hundreds of folders from every source label. Keep the hierarchy shallow and use indexes/metadata for fine-grained retrieval.

## Proposed structure

```text
organized/
├── brands/
│   ├── nivy-global/
│   │   ├── company/
│   │   ├── strategy/
│   │   ├── brand-system/
│   │   ├── operations/
│   │   ├── marketing/
│   │   ├── sales/
│   │   └── research/
│   ├── nivy-advisory/
│   │   ├── brand-system/
│   │   ├── strategy/
│   │   ├── services/
│   │   ├── marketing/
│   │   ├── sales/
│   │   ├── website/
│   │   ├── operations/
│   │   └── research/
│   ├── nivy-next/
│   ├── nivy-nexus/
│   ├── nivy-jobs/
│   ├── nivy-academy/
│   ├── nivy-artisan/
│   └── <new-evidence-based-brand>/
├── knowledge/
│   ├── company/
│   ├── brand-systems/
│   ├── strategy/
│   ├── research/
│   ├── marketing/
│   ├── sales/
│   ├── operations/
│   ├── technology/
│   ├── ai-automation/
│   ├── finance-accounting/
│   ├── hr-people/
│   ├── communities/
│   ├── website-digital-presence/
│   ├── legal-compliance/
│   └── general-reference/
├── cross-brand/
├── unclassified/
└── archive/
```

## Why both `brands/` and `knowledge/`?

A document may belong clearly to a brand but also contain reusable company knowledge. The indexes should connect the two without forcing one physical copy into multiple locations.

- `brands/` = brand-centric working view.
- `knowledge/` = reusable domain-centric view.
- `cross-brand/` = material intentionally spanning multiple brands.
- `unclassified/` = temporary holding area with explicit reason.
- `archive/` = obsolete/legacy source that must remain accessible.
- `source-archive/` = provenance-preserving original representation when a source migration strategy requires it.

## Metadata strategy

Use front matter for organized Markdown documents where practical:

```yaml
---
title: "Semantic Document Title"
brand: "Nivy Advisory"
knowledge_domain: "Marketing"
artifact_type: "Online Presence Plan"
lifecycle: "organized-source"
source_path: "Notion - Nivy OS/..."
source_system: "Notion export"
confidence: "high"
duplicate_group: ""
version_group: ""
promotion_target: ""
last_classified: "2026-09-16"
---
```

Metadata must never replace the migration manifest. The manifest remains the authoritative mapping from old path to new path.

## Indexes

### MASTER-DOCUMENT-INDEX
One row per organized artifact, linking brand, domain, type, lifecycle and provenance.

### BRAND-INDEX
One entry per discovered brand/entity, with evidence-backed description and links to its organized knowledge.

### KNOWLEDGE-INDEX
One entry per knowledge domain with links to relevant brands and cross-brand material.

### MIGRATION-MANIFEST
Old path → new path + classification + confidence + batch + verification.

### DUPLICATE-MAP
Exact duplicate, near duplicate, export duplicate, version, derivative, or unrelated similarity.

### SOURCE-PROVENANCE-MAP
Source system/export/batch/date and any known parent-child relationship.

## Naming standard

Preferred:

`<Semantic Title>.md`

For recurring controlled documents:

`<Domain> - <Specific Subject>.md`

Examples:

- `Nivy Advisory - Company Profile.md`
- `Nivy Advisory - Website Structure.md`
- `Nivy Advisory - Brand Color Palette.md`
- `Online Presence - 30 Day Plan.md`
- `Email Marketing - Sequences.md`

Avoid:

- Notion UUID suffixes
- export IDs
- meaningless numeric suffixes
- duplicate emoji-only prefixes
- `Untitled`, `New`, `Page`, `Copy`, unless that is the actual source title and it remains unresolved
