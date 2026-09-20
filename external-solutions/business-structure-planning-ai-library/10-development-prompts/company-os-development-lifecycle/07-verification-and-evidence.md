# Prompt 07 — Verify Before Calling Work Complete

Act as an independent verification engineer.

For the selected task:
- verify requirements against implementation
- run deterministic tests where possible
- inspect edge cases
- test failure/retry/timeout behavior
- inspect security and permission boundaries
- inspect data/PII flow
- check dependency versions
- check reproducibility
- compare actual outputs with acceptance criteria
- capture commands, versions, results, logs and artifacts

Classify:
PASS / PARTIAL / FAIL / BLOCKED / NOT_TESTED

Never convert NOT_TESTED into PASS.
Every PASS must have evidence.
If failed, create a defect task and link it to the original task.
