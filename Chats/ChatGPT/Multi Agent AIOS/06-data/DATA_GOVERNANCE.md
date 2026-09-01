# BILLION DREAMS UNITED OS — DATA GOVERNANCE

**Stage:** B.7  
**Version:** 1.0  
**Status:** Baseline locked

## Purpose

Define ownership, quality, provenance, access, retention, and lifecycle controls for the canonical AIOS data layer.

## 1. Governance principles

1. Canonical data has one authoritative system of record.
2. Data ownership is explicit; it is never inferred.
3. Data quality must be measurable and continuously reviewed.
4. External/scraped data must retain provenance and verification state.
5. Sensitive data follows least-privilege access.
6. Historical business records must remain auditable.
7. AI-generated data must not silently become authoritative source data.

## 2. System-of-record policy

- **Business operations / CRM:** Odoo Community + OCA, with Odoo CRM as the canonical CRM.
- **Workflow execution:** n8n execution state/logs for workflow automation.
- **Vector retrieval:** Qdrant for indexed vector representations; source documents remain authoritative elsewhere.
- **Repository governance:** GitHub repository artifacts are authoritative for versioned OS specifications/configuration.

No parallel database may become an unofficial source of truth without an approved architecture decision.

## 3. Data classification

| Class | Examples | Minimum control |
|---|---|---|
| Public | Published company information | Integrity + provenance |
| Internal | Operating plans, non-public workflows | Authenticated access |
| Confidential | Client records, commercial data | Least privilege + audit |
| Restricted | Secrets, credentials, highly sensitive personal data | Dedicated secure secret/access controls; never commit to repository |

## 4. Data ownership

Every production entity should have an explicitly assigned business/system owner before autonomous operation. Until assignment, owner remains `unassigned` and the entity must not be treated as fully governed merely because documentation exists.

## 5. Data quality dimensions

Track, where applicable:

- Completeness
- Accuracy
- Consistency
- Uniqueness
- Timeliness
- Validity
- Referential integrity
- Provenance

Quality failures must generate actionable exceptions rather than being silently ignored.

## 6. Provenance

Externally sourced records should capture, where applicable:

- Source/channel
- Source URL or reference
- Collection timestamp
- Verification status
- Transformation/normalization history
- Responsible workflow or agent

Generated summaries or classifications must remain distinguishable from source facts.

## 7. Access control

- Default to least privilege.
- Separate read, write, export, administrative, and destructive permissions where supported.
- High-impact writes require authorization and, where required by `BUILD_RULES.md`, human approval.
- Bulk exports require an explicit business purpose and appropriate authorization.

## 8. Retention and deletion

Retention periods are entity- and jurisdiction-dependent and must be defined before production use of sensitive data.

- Do not delete records needed for legal, financial, contractual, or audit purposes.
- Prefer retirement/soft deletion where historical traceability is required.
- Destructive deletion must be authorized and auditable.
- Data minimization applies to new collection and derived datasets.

## 9. AI data policy

- Training/retrieval datasets must have known provenance.
- Do not index secrets or restricted credentials into vector stores.
- Access-controlled documents must retain equivalent access controls when retrieved.
- Agent outputs affecting authoritative records require validation before write-back.
- Evaluation data must not be used as production truth without explicit validation.

## 10. Data lifecycle

`Collect → Validate → Normalize → Store → Use → Monitor → Archive/Retire → Delete when authorized`

Every transition should preserve necessary provenance and auditability.

## 11. Data incident handling

Suspected corruption, unauthorized access, material leakage, or systematic quality failure must be recorded as an `Incident`, investigated, contained, and escalated according to severity.

## 12. Governance review

Data governance is reviewed weekly alongside `COMPLETION_MATRIX.md` under `BUILD_RULES.md`. Material changes follow `CHANGE_MANAGEMENT.md`.

## Definition of governed data

A dataset/entity is **governed** only when its system of record, owner, classification, access policy, quality checks, provenance requirements, and retention approach are defined at the level appropriate to its risk.
