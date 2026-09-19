# Evaluation & Adoption Rules

## 1. Never confuse discovery with adoption

A URL in this library means only that a potentially useful resource was found.
It does not mean it is secure, maintained, licensed for our use, or suitable for production.

## 2. Evaluate every asset

| Criterion | Questions |
|---|---|
| Capability fit | Does it actually perform the required job? |
| Evidence | Is the capability demonstrated in documentation/code/examples? |
| Maintenance | Is it actively maintained or clearly stable? |
| License | Can we legally reuse, modify and redistribute it if needed? |
| Security | Does it require credentials, data access, code execution or external services? |
| Privacy | What company/client data would leave our environment? |
| Dependencies | What models, SaaS products, APIs or runtimes are required? |
| Integration | Can it fit our GitHub/Notion/Odoo/n8n/automation architecture? |
| Cost | Free/open-source/freemium/paid and likely operating cost? |
| Customization | Can company context and policies be injected cleanly? |
| Output quality | Is there a validation/evaluation mechanism? |
| Portability | Can the asset work across models/tools? |

## 3. Adoption states

Use these states in future trackers:

- `DISCOVERED`
- `REVIEW_REQUIRED`
- `LICENSE_CHECK`
- `SECURITY_REVIEW`
- `POC`
- `ADAPTED`
- `INTEGRATED`
- `CANONICAL`
- `REJECTED`
- `ARCHIVED`

## 4. Preferred adoption order

```text
Existing open-source skill / workflow
        ↓
Existing free tool / template
        ↓
Existing commercial tool where justified
        ↓
Adapt / integrate existing components
        ↓
Build missing glue/orchestration
        ↓
Custom development only for genuine gaps
```

## 5. Do not clone entire libraries blindly

Large skill libraries can contain hundreds of capabilities. Import only the relevant
skills after inspection. Keep the original repository URL and version/commit information
when a skill is adopted so that updates can be tracked.

## 6. Preserve provenance

Every adopted asset should record:

```yaml
source_name:
source_url:
source_type:
source_owner:
source_version_or_commit:
license:
access_model:
date_discovered:
date_reviewed:
adoption_state:
internal_adaptation:
destination:
notes:
```

## 7. Company-specific adaptation layer

External assets should not directly become company policy. Put company-specific context
in a separate layer:

```text
External Skill / Framework
        +
Company Context
        +
Brand Rules
        +
Department Rules
        +
Security / Compliance Rules
        +
Tool Integrations
        +
Approval Rules
        ↓
Nivy-adapted capability
```

This keeps the external source reusable and makes future replacement easier.
