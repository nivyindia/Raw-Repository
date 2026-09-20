# Prompt 06 — Execute One Small Implementation Phase

ROLE
You are the implementation agent.

INPUT
One approved task/phase from TASKS.md/PROJECTS.md.

DO
1. Read WORK-STATUS.md first.
2. Read the governing plan and architecture.
3. Inspect dependencies and reuse candidates.
4. Claim exactly one bounded unit of work.
5. Implement only that unit.
6. Add/update tests.
7. Run the required verification.
8. Capture evidence.
9. Update TASKS.md, PROGRESS.md, WORK-STATUS.md and CHANGELOG if applicable.
10. Commit the completed unit.
11. Do not silently expand scope.

COMPLETION REQUIREMENTS
Implementation + test + evidence + documentation + status update.

If blocked:
record exact blocker, evidence, attempted solutions and next smallest unblock action.


## Output Storage
Implementation artifacts must be placed beside the component they belong to. Tests belong in the repository's test location; configuration in configuration locations; documentation in docs; evidence in evidence/artifact locations. Never put generated implementation files into the prompt/planning folders unless they are themselves prompt assets.
