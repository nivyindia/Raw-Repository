# Prompt 05 — GitHub Repository and Version Governance

Design and maintain safe GitHub storage.

REPOSITORY MODEL
- main: stable
- develop: integration
- feature/*: feature work
- fix/*: fixes
- audit/*: audit
- improve/*: improvements
- release/*: release preparation

RULES
1. Never develop directly on main for substantial work.
2. Every feature/fix has a focused branch.
3. Keep commits atomic and descriptive.
4. Every release candidate must be traceable to a commit.
5. Tag every released version.
6. Never move an existing release tag.
7. Maintain CHANGELOG.md and VERSION.md.
8. Record migration notes for breaking changes.
9. Preserve evidence/artifacts needed to reproduce a release.
10. Use PR/review gates where available.

VERSIONING
v0.1.0 = smallest viable foundation.
PATCH = correction.
MINOR = compatible capability.
MAJOR = breaking contract/architecture change.

Before release verify:
working tree state, tests, security checks, dependencies, documentation, evidence, migration path, rollback path, version metadata, and tag target.
