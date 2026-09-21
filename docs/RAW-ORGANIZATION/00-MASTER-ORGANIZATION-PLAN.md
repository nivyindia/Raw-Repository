# Raw Repository Organization — Master Implementation Plan

**Repository:** `nivyindia/Raw-Repository`
**Purpose:** Convert the current raw/source warehouse from a cluttered export-oriented structure into a searchable, traceable knowledge warehouse organized primarily by **brand** and secondarily by **knowledge/domain**, while preserving every source artifact and its provenance.
**Status:** PLAN CREATED — execution not yet started
**Date:** 2026-09-16

## 1. Objective

Organize the raw repository without destroying source history. The target system must make it possible to answer:

- Which brand does this material belong to?
- What knowledge/domain does it contain?
- What is the document type or lifecycle state?
- Is it source/raw, reconciled, canonical, duplicate, or reference-only?
- Where did it come from?
- What other files are related to it?
- Has it been promoted to another repository?

## 2. Current-state findings

The repository already contains useful control infrastructure, but the source layer is visibly heterogeneous. The current tree includes Notion-style export folders, UUID/timestamp-heavy filenames, brand-named folders, generic research folders, community exports, and duplicated export content. Examples include `All Communities`, `Nivy Advisory`, `Nivy Next`, `Nivy Global`, `Nivy Jobs`, `Nivy Nexus`, `Nivy Academy`, `Nivy Artisan`, `Nivy Research Data`, `Brand Systems`, and `Notion - Nivy OS`. Search results also show repeated Notion membership/workspace records and repeated brand material across several source locations.

The repository README correctly defines this repository as a source warehouse and says raw material must be preserved and reconciled rather than treated as implementation proof. `WORK-STATUS.md` also directs implementation truth to the canonical AIOS plan. The existing control system requires preservation, cross-file discovery, verification, status recording, and commit evidence.

## 3. Core design decision

Use a **Brand → Knowledge → Document Type → Lifecycle** model for the organized view, while retaining a separate immutable/source layer for provenance.

### Primary dimensions
1. **Brand / business entity** — where the knowledge belongs.
2. **Knowledge domain** — what the material is about.
3. **Artifact type** — strategy, brand, website, marketing, sales, operations, finance, research, prompt, export, reference, etc.
4. **Lifecycle** — raw, classified, reconciled, canonical-candidate, promoted, archive/reference.

Do not use filename alone as truth. Classification must use filename + path + content + links + metadata + duplicate relationships.

## 4. Target repository model

```text
docs/RAW-ORGANIZATION/
  00-MASTER-ORGANIZATION-PLAN.md
  01-SOURCE-ANALYSIS.md
  02-TARGET-STRUCTURE.md
  03-MIGRATION-MAPPING-RULES.md
  04-START-PROMPT.md
  05-CONTINUE-PROMPT.md
  06-EXECUTION-TRACKER.md
  07-RENAME-RULES.md

organized/
  brands/
    nivy-global/
    nivy-advisory/
    nivy-next/
    nivy-nexus/
    nivy-jobs/
    nivy-academy/
    nivy-artisan/
    other-identified-brands/
  knowledge/
    company/
    brand-systems/
    strategy/
    research/
    marketing/
    sales/
    operations/
    technology/
    ai-automation/
    finance-accounting/
    hr-people/
    communities/
    website-digital-presence/
    legal-compliance/
    general-reference/
  cross-brand/
  unclassified/
  archive/

source-archive/
  original-path-preserved/

indexes/
  MASTER-DOCUMENT-INDEX.md
  BRAND-INDEX.md
  KNOWLEDGE-INDEX.md
  MIGRATION-MANIFEST.md
  DUPLICATE-MAP.md
  SOURCE-PROVENANCE-MAP.md
```

The exact brand list is **discovered from source evidence**, not hard-coded from memory. New brands are added only after evidence is found.

## 5. Migration phases

### Phase A — Inventory
- Enumerate every file and directory.
- Capture path, extension, size, hash where possible, and source location.
- Identify exports, generated files, duplicated trees, empty/placeholder artifacts, and control files.

### Phase B — Content classification
For each artifact assign:
- `brand`
- `knowledge_domain`
- `artifact_type`
- `lifecycle_state`
- `source_system`
- `confidence`
- `related_artifacts`
- `promotion_target` if known

### Phase C — Naming normalization
Rename only when the semantic title can be established with adequate confidence. Remove Notion export IDs, random UUID fragments, duplicate emoji prefixes, and noisy suffixes from the **organized copy** while preserving the original path in the migration manifest.

### Phase D — Grouping
Move organized copies into the Brand → Knowledge structure. Cross-brand material goes to `cross-brand`; genuinely unresolved material goes to `unclassified` rather than being guessed.

### Phase E — Deduplication / relationship mapping
Do not delete duplicates during the first pass. Mark exact duplicates, near duplicates, versions, exports, and derivative documents in `DUPLICATE-MAP.md`.

### Phase F — Verification
Check:
- every source file is accounted for;
- every organized file has a provenance record;
- no original source is lost;
- links are updated or explicitly marked;
- no classification was made from filename alone when content contradicted it;
- indexes match the actual tree.

### Phase G — Promotion map
Identify which organized knowledge should eventually move into canonical brand repositories, the Company OS, Systems Library, research repositories, or other destination repositories. Promotion is a separate decision from raw organization.

## 6. Safety rules

1. **No destructive first pass.**
2. Never delete raw source solely because it is duplicated.
3. Never silently overwrite an existing file.
4. Preserve original path and source filename in the migration manifest.
5. Keep ambiguous files in `unclassified/` with a reason.
6. Keep implementation status separate from source volume.
7. Do not treat Notion export metadata as authoritative business meaning.
8. Do not rewrite substantive source content merely to make it look cleaner during classification.
9. Make changes in batches and verify each batch.
10. Commit each verified migration batch with a clear scope.

## 7. Definition of done

The organization project is complete only when:

- inventory coverage is 100% verified;
- all source artifacts have a classification state;
- organized files use stable semantic names;
- brand and knowledge indexes are complete;
- provenance and migration manifests are complete;
- duplicates and versions are mapped;
- unresolved items are explicitly tracked;
- internal links are validated where applicable;
- README/control files reflect the new operating model;
- every migration batch has verification evidence and commits.

## 8. Execution order

**Inventory → classify → propose mapping → approve/lock rules → rename/group → verify → index → promotion map → repeat.**

Do not attempt a repository-wide blind move in one pass.
