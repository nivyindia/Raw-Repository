# Prompt 12 — Prepare and Execute a Release

ROLE
Release engineer.

DO NOT RELEASE until:
- required tasks are VERIFIED
- acceptance gates pass
- tests pass
- security checks pass
- dependencies are pinned/reviewed
- documentation is current
- WORK-STATUS is resumable
- CHANGELOG is updated
- VERSION is correct
- rollback/migration plan exists
- evidence is archived

Release process:
1. freeze release scope
2. create release branch
3. run full verification
4. resolve blockers
5. update version/changelog
6. merge through review
7. tag immutable version
8. record commit SHA
9. publish release evidence
10. return main to stable state

After release:
create post-release audit task and record known limitations.
