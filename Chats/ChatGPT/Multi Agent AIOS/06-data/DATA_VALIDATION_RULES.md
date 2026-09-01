# BILLION DREAMS UNITED OS — DATA VALIDATION RULES

**Stage:** B.6  
**Version:** 1.0  
**Status:** Baseline locked

## 1. Identity

- Every entity record must have a stable `id`.
- IDs are immutable and must never be silently reused.
- Foreign-key references must point to canonical IDs.
- `company_id` is mandatory for tenant-scoped records.
- `brand_id` is mandatory where the entity belongs to a specific brand scope.

## 2. Audit fields

- `created_at` is immutable after creation.
- `updated_at` changes whenever a mutable record changes.
- Timestamps use ISO-8601 UTC.
- Audit history must be retained for material business-state changes.

## 3. Data types and normalization

- Dates use ISO-8601 date format.
- Datetimes use ISO-8601 UTC.
- Currency values use ISO 4217 currency codes.
- Monetary values must use fixed-precision decimal storage; floating-point storage is prohibited for financial amounts.
- Email addresses should be normalized to lowercase for matching where appropriate.
- Phone numbers should use an international representation where available.
- Status values must come from an entity-specific controlled vocabulary.

## 4. Referential integrity

- A child record cannot reference a nonexistent parent.
- Deletion of referenced records must follow an explicit retention/deletion policy.
- Prefer soft deletion/retirement for records required for audit, finance, compliance, or historical reporting.
- Cross-company references are prohibited unless explicitly supported by an approved relationship.

## 5. Sales data

- A Lead must have a source before entering the qualified sales pipeline.
- An Opportunity must reference an Account.
- Probability must be between 0 and 100 when present.
- Amount must be non-negative when present.
- Expected close dates must be valid dates.
- Duplicate lead/contact detection should use normalized identity signals before creating new records.

## 6. Financial data

- Invoice totals must reconcile: `total_amount = subtotal + tax_amount + other_adjustments` where applicable.
- Invoice numbers must be unique within the applicable company/legal-entity scope.
- Payment amounts must be non-negative.
- Payment currency must be explicit.
- A payment linked to an invoice must not exceed the permitted outstanding balance unless the business process explicitly supports overpayment/credit.
- Financial records must not be silently overwritten; corrections require an auditable adjustment trail.

## 7. AI and automation data

- Every AgentRun must reference a valid Agent.
- Every WorkflowRun must reference a valid Workflow.
- Agent and workflow execution records must capture status and execution timestamps.
- Evaluation records must identify the subject and evaluation criteria version.
- Approval records must identify requester, approver and decision state where applicable.
- External tool credentials are never stored as entity data.

## 8. Event integrity

- Events must have a stable event ID and occurrence timestamp.
- Events should be idempotently processed using an event ID or equivalent deduplication key.
- Event payloads must identify their source and referenced entity.
- Failed processing must be observable and retryable without uncontrolled duplicate side effects.

## 9. Privacy and access

- Sensitive contact data is accessed only by authorized roles/systems.
- Collect only data required for the stated business purpose.
- Data retention must follow applicable legal and company policy.
- Exported datasets must preserve access controls and must not expose secrets.

## 10. Validation gates

Before a high-impact workflow writes or acts on business data:

1. Validate schema.
2. Validate required fields.
3. Validate types and ranges.
4. Validate references.
5. Check duplicates/idempotency.
6. Check authorization.
7. Record provenance/evidence where applicable.
8. Apply human approval when required by `BUILD_RULES.md`.

## 11. Error handling

Validation failures must be classified, logged and returned to the workflow/agent as structured errors. Invalid records must not be silently accepted.

## 12. Governance

Changes to these rules follow `CHANGE_MANAGEMENT.md`. A validation rule is not considered implemented in production merely because this document exists; implementation and test evidence are required before a related component is marked complete.
