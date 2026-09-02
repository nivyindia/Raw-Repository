# IAM Baseline — Billion Dreams United AIOS

**Version:** 1.1  
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

Canonical item naming: `<ENV>-<SERVICE>-<PURPOSE>`

Examples: `DEV-N8N-SMTP`, `STAGING-ODOO-API`, `PROD-POSTAL-SMTP`.

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

Every automated integration uses a distinct service identity where supported. The following registry is the D.8 baseline:

| Service account | System | Primary scope | Default access | Risk | Environment |
|---|---|---|---|---|---|
| `svc-n8n` | n8n | workflow orchestration/integrations | governed API/tool execution only | L2 | DEV/STAGING/PROD |
| `svc-dify` | Dify | AI workflows/RAG | model + approved vector/tool services | L1/L2 | DEV/STAGING/PROD |
| `svc-odoo-api` | Odoo | business/CRM/ERP API | approved Odoo models/actions only | L2 | DEV/STAGING/PROD |
| `svc-langgraph` | LangGraph | agent orchestration | approved agent tools/state only | L1/L2 | DEV/STAGING/PROD |
| `svc-postgres` | PostgreSQL | application data | service-specific DB/schema only | L1/L2 | DEV/STAGING/PROD |
| `svc-nextcloud` | Nextcloud | document/file access | designated AIOS/client folders | L1/L2 | DEV/STAGING/PROD |
| `svc-postal` | Postal | transactional email | mail delivery operations only | L2 | DEV/STAGING/PROD |
| `svc-qdrant` | Qdrant | vector database | designated collections only | L1/L2 | DEV/STAGING/PROD |
| `svc-minio` | MinIO | object storage | designated buckets/prefixes only | L1/L2 | DEV/STAGING/PROD |
| `svc-metabase` | Metabase | analytics | read-only reporting datasets by default | L0/L1 | STAGING/PROD |
| `svc-mixpost` | Mixpost | social publishing | approved publishing endpoints only | L2/L3 | STAGING/PROD |
| `svc-cal` | Cal.com/Cal.diy | scheduling | approved calendar resources only | L1/L2 | STAGING/PROD |
| `svc-typebot` | Typebot | forms/conversational intake | approved intake endpoints only | L1/L2 | DEV/STAGING/PROD |
| `svc-documenso` | Documenso | document/signature workflows | designated documents only | L2/L3 | STAGING/PROD |
| `svc-mautic` | Mautic | marketing automation | approved campaign/contact operations | L2/L3 | STAGING/PROD |

Service identities are identifiers only; actual credentials must be generated and stored in the appropriate Vaultwarden environment.

## 5. Service Account Scope Rules

### `svc-n8n`
- May invoke approved integrations and workflows.
- May read/write only resources explicitly assigned to a workflow.
- Must not receive unrestricted infrastructure-admin credentials.
- External material actions remain subject to AIOS policy and approval gates.

### `svc-dify`
- May access approved model providers and RAG/vector services.
- Must not receive broad database administration rights.
- Tool access is constrained by agent/workflow policy.

### `svc-odoo-api`
- May access only approved Odoo models, methods, companies, and records.
- Financial, communication, deletion, and material state-changing actions require their applicable governance gates.

### `svc-langgraph`
- Orchestrates agents but does not gain authority beyond the tools assigned to the executing agent.
- Must propagate correlation IDs, policy decisions, and approval references.

### `svc-postgres`
- Use database/schema-specific roles where possible.
- Prefer read-only roles for analytics/research.
- No shared superuser credential in application runtime.

### Supporting service accounts
- `svc-nextcloud`: designated file scopes only.
- `svc-postal`: delivery-only mail permissions; no unrelated infrastructure access.
- `svc-qdrant`: collection-level access where supported.
- `svc-minio`: bucket/prefix-level access where supported.
- `svc-metabase`: read-only by default.
- `svc-mixpost`: publishing scope only; no credential-management access.
- `svc-cal`: designated calendars/resources only.
- `svc-typebot`: approved intake/form resources only.
- `svc-documenso`: designated document/signature resources only.
- `svc-mautic`: governed contact/campaign operations only.

## 6. Least-Privilege Matrix

| Identity | Primary access | Default scope |
|---|---|---|
| `svc-n8n` | workflow integrations | only APIs/tools required by approved workflows |
| `svc-dify` | AI workflow/RAG services | model/vector services only as required |
| `svc-odoo-api` | Odoo API | governed Odoo models/actions only |
| `svc-langgraph` | agent orchestration | assigned tools/state only |
| `svc-postgres` | database | service-specific database/schema only |
| `svc-nextcloud` | files | designated AIOS/client folders only |
| `svc-postal` | mail delivery | SMTP/mail operations only |
| `svc-qdrant` | vector store | designated collections only |
| `svc-minio` | object storage | designated buckets/prefixes only |
| `svc-metabase` | analytics | read-only reporting datasets by default |

No service identity receives unrestricted infrastructure administrator privileges by default.

## 7. Credential Requirements

Each service account MUST have:

- unique credential per environment;
- named owner/system owner;
- documented purpose and scope;
- Vaultwarden secret reference;
- rotation/revocation procedure;
- audit/correlation capability where supported;
- no credential value committed to Git.

Long-lived credentials should be replaced by short-lived/token-exchange mechanisms when the platform supports them.

## 8. Access-Control Rules

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

## 9. Privileged Access

Privileged roles include Vaultwarden administrator, infrastructure administrator, database administrator, Odoo administrator, and AIOS governance/policy administrator.

Requirements: named human identity, MFA, minimum necessary duration/scope, audit trail, no credential sharing, and immediate revocation when role/need ends.

## 10. Secret Lifecycle

`Generate → Store → Grant → Use → Rotate → Revoke → Verify`

New secrets are generated using approved cryptographic tooling and stored in Vaultwarden, not repository files. Suspected compromise triggers immediate revocation/rotation and incident handling.

## 11. Application Runtime Pattern

Preferred: `Application → secret reference → approved secret retrieval mechanism → runtime credential`

Never: `Application → hard-coded credential in source/config repository`

For n8n, credentials should be held in its protected credential store or injected through a governed secret-management mechanism; Vaultwarden remains the authoritative human-controlled secret inventory unless an implementation-specific architecture explicitly documents otherwise.

## 12. AI Agent Access

AI agents inherit no authority merely from being AI agents.

Authorization chain: `Agent → Skill → Tool → Action → Resource`

An agent may access a resource only when policy permits the action, the identity is authorized, scope is within grant, required approvals have passed, and the action is auditable.

Credentials must not be exposed to the model when a tool can perform the operation without revealing the secret value.

## 13. Repository Controls

- `.env` files containing real secrets are prohibited from commits.
- Production credentials are prohibited in examples and fixtures.
- Secret scanning should run in CI where available.
- Configuration templates use placeholders only.
- Rotation does not require source-code changes when the secret reference remains stable.

## 14. Audit Requirements

Record, where technically available: identity, service, environment, resource, permission/action, grant/revoke event, timestamp, approval reference, correlation/request ID, and outcome. Audit records must not leak secret values.

## 15. Access Review

- privileged human access: monthly
- service identities: quarterly
- environment separation: quarterly
- emergency access: after every use
- compromised/revoked identities: immediate review

## 16. Emergency Access

Emergency access is temporary, explicitly justified, logged, and revoked after the incident/task. It must not become a permanent workaround for normal IAM controls.

## 17. Compliance With AIOS Governance

This baseline is subordinate to the permission matrix, AI risk policy, communication policy, suppression-list data model, Odoo approval-request model, and approval workflow specification. Where policies conflict, the stricter control applies until governance explicitly resolves the conflict.
