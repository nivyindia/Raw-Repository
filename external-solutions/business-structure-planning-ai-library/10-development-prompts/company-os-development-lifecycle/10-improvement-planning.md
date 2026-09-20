# Prompt 10 — Turn Audit Findings into an Improvement Plan

Read the latest audit and current repository state.

For every finding:
1. validate whether it is real
2. remove duplicates
3. determine root cause
4. determine dependency order
5. identify reusable solutions
6. define the smallest safe correction
7. define acceptance criteria
8. define verification evidence
9. estimate scope/risk
10. assign phase/project/task IDs

Prioritize:
critical correctness/security → foundational dependency → high operational impact → reliability → maintainability → optimization → convenience.

Create/update IMPROVEMENT-PLAN.md and TASKS.md.

Do not implement yet. The output is a small-phase executable improvement backlog.


## Output Storage
Store improvement plans in the canonical improvement/planning folder and convert approved findings into linked executable tasks in TASKS.md or the task system. Do not create an isolated improvement list that is not connected to execution tracking.
