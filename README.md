# Nivy Research Repository

## 🚀 START / CONTINUE

This repository is the central **Research Intake + Curation + Promotion System** for the Nivy ecosystem.

> **Core rule:** REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING

### Current implementation state

| Area | Status |
|---|---|
| Research system concept | ✅ Implemented |
| Logical repository structure | ✅ Implemented |
| Branch/workflow model | ✅ Implemented |
| Research item metadata contract | ✅ Implemented |
| Promotion rules | ✅ Implemented |
| Research tracker | ✅ Implemented |
| Promotion tracker | ✅ Implemented |
| Gap registry | ✅ Implemented |
| Existing raw-content migration | ⏳ Not started |
| Full inventory/classification | ⏳ Next phase |
| Automated research organizer | ⏳ Later phase |

## 🧭 How This Repository Works

```text
RAW / UNORGANIZED INPUT
        ↓
00-inbox
        ↓
research
        ↓
classify + deduplicate + reconcile
        ↓
curate
        ↓
validate
        ↓
transfer-ready
        ↓
REUSE / ADAPT / INTEGRATE
        ↓
CORRECT DESTINATION REPOSITORY
```

This repository is intentionally **not** the final canonical home for every asset. It preserves research lineage and prepares assets for promotion into the correct destination repository.

## 📁 Control Documents

- `docs/RESEARCH-SYSTEM/00-MASTER-CONCEPT.md`
- `docs/RESEARCH-SYSTEM/01-REPOSITORY-STRUCTURE.md`
- `docs/RESEARCH-SYSTEM/02-BRANCH-WORKFLOW.md`
- `docs/RESEARCH-SYSTEM/03-RESEARCH-ITEM-CONTRACT.md`
- `docs/RESEARCH-SYSTEM/04-PROMOTION-RULES.md`

## 📊 Trackers

- `trackers/research-tracker.md`
- `trackers/promotion-tracker.md`
- `trackers/gap-registry.md`

## ⚠️ Important Migration Rule

The existing repository contains historical/raw material and multiple existing folders. **Do not reorganize or delete that material yet.**

Phase 1 is to establish the control system.

Phase 2 is:

```text
Inventory → classify → deduplicate → map destination → migrate in batches → verify
```

Every migration must preserve provenance and remain traceable.

## Destination Examples

Research may eventually be promoted into repositories such as:

- `nivyindia/Nivy-Next-AIOS`
- Nivy Global / Company OS repositories
- Brand-specific AIOS repositories
- Shared skills, agents, workflows and knowledge repositories

The destination is determined per research item; it is never assumed merely from where the research was captured.
