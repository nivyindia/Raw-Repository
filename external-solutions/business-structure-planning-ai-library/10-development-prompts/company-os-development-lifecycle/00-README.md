# Company OS Development Lifecycle — Prompt System

Purpose: build the replacement for Nivy Next AIOS from the smallest viable version, then evolve it safely through controlled versions.

Governing loop:
PLAN → DISCOVER/REUSE → ARCHITECT → IMPLEMENT → VERIFY → RECORD → RELEASE → AUDIT → IMPROVE → REPEAT

Principles:
- Reuse before build: DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.
- Never treat documentation/catalog coverage as implementation.
- Every task has an owner, dependency, acceptance criteria, evidence, status, and next action.
- Work in small independently verifiable phases.
- Never silently overwrite a working version.
- Every release is reproducible and traceable to commits, tests, evidence, and source versions.
- Audit is continuous and separate from implementation.
- No major architectural expansion is allowed merely because a gap was discovered; prioritize by dependency and value.

## Prompt sequence
1. 01-bootstrap-and-charter.md
2. 02-discovery-and-reuse.md
3. 03-architecture.md
4. 04-master-plan-and-roadmap.md
5. 05-repository-and-version-governance.md
6. 06-implementation-phase.md
7. 07-verification-and-evidence.md
8. 08-progress-project-task-management.md
9. 09-audit-and-mistake-discovery.md
10. 10-improvement-planning.md
11. 11-small-phase-improvement-execution.md
12. 12-release-and-version.md
13. 13-workflow-and-operating-cycle.md
14. 14-continuous-autonomous-cycle.md

## Canonical repository files
At minimum maintain:
- README.md
- WORK-STATUS.md
- MASTER-PLAN.md
- ARCHITECTURE.md
- ROADMAP.md
- PROGRESS.md
- TASKS.md
- PROJECTS.md
- WORKFLOWS.md
- AUDIT.md
- IMPROVEMENT-PLAN.md
- CHANGELOG.md
- VERSION.md
- EVIDENCE/
- docs/
- prompts/

## Status model
BACKLOG → DISCOVERING → PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED → RELEASED
With side states: BLOCKED, DEFERRED, REJECTED, ARCHIVED.

## Version model
Start with the smallest viable version: v0.1.0.
Use semantic versioning thereafter:
- PATCH: correction/no contract change
- MINOR: backward-compatible capability
- MAJOR: incompatible architecture/contract change

Git strategy:
- main = latest stable
- develop = integration
- feature/* = isolated work
- fix/* = defect correction
- audit/* = audit work
- improve/* = improvement work
- release/* = release preparation
- tags = immutable released versions
- never use tags as mutable pointers

A task is complete only when implementation + verification + evidence + documentation + status update are complete.


## Autonomous Use
Use **15-autonomous-entry-point-sequence-controller.md** as the default entry point when only a destination repository is supplied. It decides which lifecycle prompt to run next from repository state.

### Required execution sequence
**15 → 01 → 02 → 03 → 04 → 05 → 06 ↔ 07 ↔ 08 → 12 → 09 → 10 → 11 → 07 → 09 → 13 → 14 → repeat**

The arrows are dependency-aware, not a requirement to finish every prompt once. The controller may return to an earlier prompt whenever audit, dependency, architecture, verification or release state requires it.

## Universal File-Storage Rule
Every prompt must persist its output in the destination repository's logical canonical folder. Important results must never remain only in chat. Before creating a file, search for an existing canonical destination and update/link it rather than creating duplicates. Implementation, research, audit, evidence, planning and release artifacts must remain separated.

## Additional Controls
- **Decision log:** record important architecture/product decisions and rationale.
- **Risk register:** track security, reliability, cost, dependency, legal/license and operational risks.
- **Dependency register:** record external/internal dependencies and version constraints.
- **Evidence index:** link each verification result to task, commit and version.
- **Change impact analysis:** required before contract/architecture changes.
- **Rollback/migration record:** required for state/schema/contract changes.
- **Definition of Done:** implementation + verification + evidence + documentation + status.
- **Definition of Ready:** objective + dependencies + acceptance criteria + reuse check + verification method.
- **Archive policy:** superseded artifacts are archived, not silently deleted.
- **Resume guarantee:** repository state alone must be sufficient for another agent to continue.
