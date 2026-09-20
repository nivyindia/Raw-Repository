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
