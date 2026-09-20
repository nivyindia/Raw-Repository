# Prompt 11 — Execute Improvement in Small Phases

Take the highest-priority approved improvement that has satisfied its dependencies.

Cycle:
SELECT → REUSE CHECK → DESIGN → IMPLEMENT → TEST → VERIFY → EVIDENCE → UPDATE STATUS → COMMIT → AUDIT LOCAL IMPACT

Rules:
- one bounded change at a time
- preserve working behavior
- avoid unrelated refactors
- add regression tests for defects
- update architecture/docs when contracts change
- if the change creates a new risk, stop and record it
- never close the audit finding without evidence

After completion, compare actual result with the improvement acceptance criteria and update the audit finding to FIXED / PARTIALLY_FIXED / DEFERRED.
