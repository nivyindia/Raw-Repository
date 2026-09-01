# BILLION DREAMS UNITED OS — BUILD RULES

**Version:** 1.1  
**Stage:** A.10  
**Status:** Baseline implementation rules + weekly governance cadence

## 1. Source of Truth

1. Do not create competing sources of truth for the same business entity or operational state.
2. Existing source material must be inspected before creating a new artifact.
3. `id-master-list.yaml` is the canonical ID inventory.
4. `COMPLETION_MATRIX.md` is the canonical implementation tracker.
5. `SYSTEM_MASTER_INDEX.md` is the canonical navigation/index layer.
6. `ARCHITECTURE_DECISIONS.md` contains locked architecture decisions.

## 2. Architecture Rules

1. **Odoo Community + OCA** is the primary business operations backbone.
2. **Odoo CRM** is the canonical CRM; do not create a parallel CRM source of truth.
3. **Qdrant** is the canonical vector database.
4. **n8n** is the primary business workflow engine.
5. **LangGraph** may be used for specialized stateful agent orchestration, not as a second general-purpose business workflow platform.
6. Prefer open-source/self-hostable components where they meet the requirement and are operationally viable.

## 3. Agent Build Rules

Every production agent must have, at minimum:

- Stable agent ID.
- Clear purpose and scope.
- Defined inputs and outputs.
- Explicit tools/integrations.
- Permission boundary.
- Human-escalation condition.
- Error/fallback behavior.
- Evaluation criteria.
- Owner/maintainer.
- Evidence of implementation before being marked complete.

Agents must be narrow enough to test and govern. Avoid creating a single monolithic autonomous agent for unrelated responsibilities.

## 4. Workflow Rules

Every production workflow must define:

- Stable workflow ID.
- Trigger.
- Inputs.
- Processing steps.
- Agent/tool dependencies.
- State/data written.
- Success condition.
- Failure/retry behavior.
- Human approval gates where required.
- Observability/logging.

n8n workflows should be idempotent where practical and must avoid uncontrolled duplicate writes or outreach.

## 5. Revenue-First Rule

Implementation priority follows business impact. The first production loop should concentrate on revenue acquisition:

`Research → ICP → Lead Discovery → Enrichment/Verification → Scoring → Outreach → Follow-up → Reply Triage → Qualification → Meeting Prep → Proposal → Onboarding`

Internal convenience features must not displace critical revenue-engine capabilities without an explicit decision.

## 6. Data Rules

- Minimize duplicated customer/lead data.
- Use stable IDs and explicit relationships.
- Record provenance for externally sourced data.
- Do not treat scraped/unverified data as verified fact.
- Apply validation before high-impact downstream actions.
- Separate raw, normalized and operational data where appropriate.
- Do not place secrets, API keys or credentials in repository source files.

## 7. AI / Knowledge Rules

- Retrieval should use the canonical knowledge architecture and Qdrant where vector retrieval is required.
- Store document metadata and provenance with indexed knowledge.
- Do not allow generated content to silently overwrite authoritative source material.
- Agent outputs that affect business records should be traceable to inputs/evidence.
- Model choice is replaceable; business contracts and evaluation criteria are not.

## 8. Human-in-the-Loop Rules

Human approval is mandatory for actions with material financial, legal, compliance, contractual, reputational or irreversible consequences unless an explicit approved automation policy exists.

Examples include:

- Sending binding contracts.
- Material pricing exceptions.
- Legal/compliance submissions.
- Irreversible financial actions.
- High-risk external communications.

## 9. Security Rules

- Least privilege by default.
- Separate credentials by system and environment.
- Never commit secrets.
- Log security-relevant actions without exposing sensitive credential material.
- Production and development environments must be separable.
- External tools receive only the minimum data required for their task.

## 10. Testing Rules

An artifact is not complete merely because its file exists.

Completion requires appropriate evidence such as:

- Unit/integration test result.
- Workflow execution evidence.
- Agent evaluation result.
- API/integration verification.
- Human acceptance for applicable high-impact functions.

A placeholder, draft, or documentation-only implementation must remain explicitly marked as incomplete.

## 11. Change Rules

- Do not silently change locked architecture.
- Material changes require an ADR/change record.
- Preserve backwards compatibility where practical.
- Update affected registries and completion records when IDs, dependencies or contracts change.
- Never mark an item complete merely to improve the reported completion percentage.

## 12. Naming Rules

Use stable, descriptive names and IDs. IDs must remain immutable once published. If an entity is retired, mark it retired rather than reusing its ID.

## 13. Deployment Rules

Development → test → controlled production promotion is preferred.

Production deployment requires:

1. Configuration validation.
2. Credential validation.
3. Test/evaluation evidence.
4. Rollback or recovery path.
5. Monitoring/logging.
6. Owner assignment.

## 14. Definition of Done

An agent/workflow is **DONE** only when:

`Implemented + Integrated + Tested + Governed + Observable + Owner Assigned + Evidence Recorded`

Documentation alone is not sufficient.

## 15. Priority Rule

When requirements conflict, use this order unless a higher-level ADR overrides it:

1. Safety/security/compliance.
2. Revenue-critical functionality.
3. Data integrity.
4. Reliability/observability.
5. Operational efficiency.
6. Convenience/optimization.

## 16. Weekly Governance Review — A.10

A weekly AIOS review is mandatory for implementation governance.

### Review cadence

- **Frequency:** Weekly.
- **Review artifact:** `COMPLETION_MATRIX.md`.
- **Scope:** Status, owners, evidence, blockers, changes, incidents, and next-stage readiness.
- **Rule:** No completion status is increased without corresponding evidence.

### Weekly review checklist

1. Review every changed/in-progress component.
2. Verify implementation evidence against its status.
3. Identify blocked, stale, failed, or ownerless items.
4. Review registry/architecture changes against change-management rules.
5. Review revenue-critical work before convenience work.
6. Record material decisions as ADR/change records.
7. Update the completion matrix only after evidence review.
8. Define the next week's highest-priority actions.

### Review outputs

Each weekly review must produce:

- Completion percentage snapshot.
- Status changes with evidence.
- Owner/blocker list.
- Material decisions and changes.
- Risks/incidents requiring escalation.
- Next-week priority list.

### Anti-gaming rule

The weekly review exists to measure **real implementation progress**, not documentation volume. Creating files, placeholders, or speculative mappings does not increase completion.

## Related Artifacts

- `id-master-list.yaml`
- `COMPLETION_MATRIX.md`
- `SYSTEM_MASTER_INDEX.md`
- `ARCHITECTURE_DECISIONS.md`
- `CHANGE_MANAGEMENT.md` (A.7)
