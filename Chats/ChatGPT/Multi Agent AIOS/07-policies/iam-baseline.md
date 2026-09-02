# IAM Baseline — Billion Dreams United AIOS

**Version:** 1.0  
**Spec ID:** IAM-BASELINE-001  
**Status:** Proposed baseline  
**Scope:** AIOS secrets, service identities, environment separation, and access-control conventions

## 1. Purpose

Define the minimum identity and access-management baseline for Billion Dreams United AIOS. Vaultwarden is the canonical human/service secret-management boundary; applications must receive only the credentials required for their authorized environment and function.

## 2. Vaultwarden Environment Naming

Use three logically isolated environments:

| Environment | Vaultwarden collection/prefix | Purpose | Production secrets allowed |
|---|---|---|---|
| DEV | `AIOS-DEV` | Local development and experimentation | No |
| STAGING | `AIOS-STAGING` | Integration/UAT/pre-production | No, except explicitly non-production test credentials |
| PROD | `AIOS-PROD` | Live business operations | Yes |

Canonical item naming:

`<ENV>-<SERVICE>-<PURPOSE>`

Examples:
- `DEV-N8N-SMTP`
- `STAGING-ODOO-API`
- `PROD-POSTAL-SMTP`
- `PROD-NEXTCLOUD-API`

## 3. Environment Isolation

- DEV credentials MUST NOT authenticate against PROD services.
- STAGING credentials MUST NOT authenticate against PROD services by default.
- PROD credentials MUST never be copied into DEV or STAGING.
- Database credentials are environment-specific.
- API keys, OAuth secrets, webhook signing secrets, SMTP credentials, and encryption keys are environment-specific unless a documented exception is approved.
- Backups containing secrets inherit the classification of the source environment.
- Environment promotion transfers configuration intent, not secret values.

## 4. Identity Classes

### Human identities

- Each operator receives an individual identity.
- Shared human accounts are prohibited except where technically unavoidable and explicitly governed.
- MFA is required for Vaultwarden administration and privileged infrastructure access.
- Access is role-based and reviewed periodically.

### Service identities

Every automated integration uses a distinct service identity where supported:

- `svc-n8n`
- `svc-dify`
- `svc-odoo-api`
- `svc-postgres`
- `svc-nextcloud`
- `svc-postal`
- `svc-qdrant`
- `svc-minio`
- `svc-metabase`
- `svc-mixpost`
- `svc-cal`
- `svc-typebot`
- `svc-documenso`

Service identity names are identifiers only; actual credentials must be generated and stored in the appropriate Vaultwarden environment.

## 5. Least-Privilege Matrix

| Identity | Primary access | Default scope |
|---|---|---|
| `svc-n8n` | workflow integrations | only APIs/tools required by approved workflows |
| `svc-dify` | AI workflow/RAG services | model/vector services only as required |
| `svc-odoo-api` | Odoo API | governed Odoo models/actions only |
| `svc-postgres` | database | service-specific database/schema only |
| `svc-nextcloud` | files | designated AIOS/client folders only |
| `svc-postal` | mail delivery | SMTP/mail operations only |
| `svc-qdrant` | vector store | designated collections only |
| `svc-minio` | object storage | designated buckets/prefixes only |
| `svc-metabase` | analytics | read-only reporting datasets by default |

No service identity receives unrestricted infrastructure administrator privileges by default.

## 6. Access-Control Rules

1. Default deny.
2. Least privilege.
3. Explicit authorization before access.
4. Separate identities by service and environment.
5. Prefer read-only credentials for reporting and research.
6. Write/delete permissions require a documented business need.
7. Production administration requires elevated authorization.
8. Secrets must never be committed to Git.
9. Secrets must never appear in prompts, logs, tickets, analytics, or error traces unless explicitly required and protected.
10. Credentials must be rotatable without changing application source code.
11. Revoked credentials must fail closed.
12. Access grants and removals must be auditable.

## 7. Privileged Access

Privileged roles include:

- Vaultwarden administrator
- infrastructure administrator
- database administrator
- Odoo administrator
- AIOS governance/policy administrator

Privileged access requirements:

- named human identity
- MFA
- minimum necessary duration/scope
- audit trail
- no credential sharing
- immediate revocation when role/need ends

## 8. Secret Lifecycle

`Generate → Store → Grant → Use → Rotate → Revoke → Verify`

Requirements:

- New secrets are generated using approved cryptographic tooling.
- Secrets are stored in Vaultwarden, not repository files.
- Secret references/configuration identifiers may be committed; secret values may not.
- Rotation must be planned for privileged and externally exposed credentials.
- Suspected compromise triggers immediate revocation/rotation and incident handling.

## 9. Application Runtime Pattern

Preferred pattern:

`Application → secret reference → approved secret retrieval mechanism → runtime credential`

Never:

`Application → hard-coded credential in source/config repository`

For n8n, credentials should be held in its protected credential store or injected through a governed secret-management mechanism; Vaultwarden remains the authoritative human-controlled secret inventory unless an implementation-specific architecture explicitly documents otherwise.

## 10. AI Agent Access

AI agents inherit no authority merely from being AI agents.

Authorization chain:

`Agent → Skill → Tool → Action → Resource`

An agent may access a resource only when:

- the action is permitted by policy,
- the agent identity is authorized,
- the requested scope is within granted permissions,
- required approval gates have passed,
- the action is auditable.

Credentials must not be exposed to the model when a tool can perform the operation without revealing the secret value.

## 11. Repository Controls

- `.env` files containing real secrets are prohibited from commits.
- Production credentials are prohibited in examples and fixtures.
- Secret scanning should run in CI where available.
- Configuration templates use placeholders only.
- Rotation does not require source-code changes when the secret reference remains stable.

## 12. Audit Requirements

Record, where technically available:

- identity
- service
- environment
- resource
- permission/action
- grant/revoke event
- timestamp
- approval reference
- correlation/request ID
- outcome

Audit records must not leak secret values.

## 13. Access Review

Minimum review cadence:

- privileged human access: monthly
- service identities: quarterly
- environment separation: quarterly
- emergency access: after every use
- compromised/revoked identities: immediate review

## 14. Emergency Access

Emergency access is temporary, explicitly justified, logged, and revoked after the incident/task. Emergency access must not become a permanent workaround for normal IAM controls.

## 15. Compliance With AIOS Governance

This baseline is subordinate to:

- `07-policies/permission-matrix.yaml`
- `07-policies/ai-risk-policy.yaml`
- `07-policies/communication-policy.yaml`
- `07-policies/suppression-list-data-model.yaml`
- `07-policies/odoo-approval-request-model.yaml`
- `07-policies/approval-workflow-spec.md`

Where policies conflict, the stricter control applies until governance explicitly resolves the conflict.
