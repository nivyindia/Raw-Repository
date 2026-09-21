# Migration & Classification Rules

## Classification precedence

When evidence conflicts, use this order:

1. Explicit substantive content inside the document
2. Explicit brand/domain references in headings and links
3. Parent/related document context
4. Source folder context
5. Filename semantics
6. Export metadata / IDs

Filename alone is never sufficient for a high-confidence classification.

## Brand assignment

Assign exactly one primary brand when the document is clearly brand-specific. Add related brands in metadata/indexes rather than duplicating the file.

Use `cross-brand` when:
- the document intentionally governs multiple brands;
- no single brand owns the knowledge;
- the document is a shared company-level system.

Use `unclassified` when the evidence is insufficient.

## Knowledge assignment

Assign one primary knowledge domain. Secondary domains belong in metadata/indexes rather than nested folder duplication.

## Artifact types

Controlled vocabulary should start with:

- profile
- strategy
- plan
- roadmap
- research
- analysis
- brand-system
- website
- marketing
- sales
- operations
- SOP
- finance
- legal
- HR
- technology
- automation
- prompt
- template
- checklist
- meeting/notes
- export
- reference
- index
- control

Add new types only when repeated source evidence justifies them.

## Lifecycle states

- `raw` — untouched source representation.
- `classified` — metadata/classification known.
- `organized-source` — semantic location/name assigned while remaining source material.
- `reconciled` — relationships/duplicates/versions evaluated.
- `canonical-candidate` — suitable for promotion review.
- `promoted` — copied/reconciled into a canonical destination repository.
- `archive` — retained for historical reference.

## Duplicate handling

### Exact duplicate
Same content/hash. Keep one canonical organized representation and map every source occurrence in `DUPLICATE-MAP.md`.

### Export duplicate
Same underlying Notion/other export represented in multiple folders. Preserve the source locations in provenance.

### Version
Different substantive versions. Keep all versions until a canonical version is explicitly established.

### Derivative
A summary, rewritten version, plan derived from another artifact, etc. Link parent/child relationship.

## Rename policy

Rename when:
- semantic title is clear;
- destination is clear;
- provenance can be recorded;
- collision is resolved.

Do not rename yet when:
- content is ambiguous;
- two documents have materially different meanings;
- the title cannot be inferred safely;
- the item may be a technical export artifact whose relationship is not understood.

## Link policy

Before changing a path, scan for inbound references. After migration, validate links and record broken/unresolved links rather than inventing destinations.

## Batch policy

Recommended batch sequence:

1. controls/indexes
2. obvious brand-owned documents
3. obvious knowledge-domain documents
4. duplicated exports
5. ambiguous items
6. archive/reference cleanup
7. cross-repository promotion mapping

Every batch gets a manifest range, verification note and commit.
