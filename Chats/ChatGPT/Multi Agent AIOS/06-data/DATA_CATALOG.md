# BILLION DREAMS UNITED OS — DATA CATALOG

**Stage:** B.16  
**Version:** 1.0  
**Status:** Baseline locked

## Purpose

Provide a human- and machine-readable index of the governed data layer so agents, workflows, developers, and operators can discover where authoritative definitions live.

## Canonical artifacts

| Artifact | Purpose | Authority |
|---|---|---|
| `entity-list.yaml` | Canonical 30-entity scope | Entity registry |
| `data-model.yaml` | Entity fields and relationships | Data model |
| `DATA_VALIDATION_RULES.md` | Integrity and validation rules | Validation policy |
| `DATA_GOVERNANCE.md` | Ownership, classification, lifecycle | Governance policy |
| `DATA_CONTRACTS.md` | Cross-system exchange contracts | Contract policy |
| `state-machines/opportunity.yaml` | Opportunity lifecycle | State-machine definition |
| `state-machines/project.yaml` | Project lifecycle | State-machine definition |
| `state-machines/lifecycle-catalog.yaml` | Lifecycle catalog | State-machine registry |
| `STATE_MACHINE_GOVERNANCE.md` | Transition governance | State-machine policy |
| `event-schemas/` | Event payload schemas | Event schema registry |
| `event-schemas/EVENT_REGISTRATION.yaml` | Registered event types | Event registry |

## Domain index

- **Sales:** Lead, Account, Contact, Opportunity, Meeting, Proposal
- **Delivery:** Project, Task
- **Finance:** Invoice, Payment
- **Organization:** Company, Brand, Department
- **Customer:** Client, Ticket
- **Marketing:** Campaign
- **Legal:** Contract
- **AI:** Agent, AgentRun, Skill
- **Automation:** Workflow, WorkflowRun
- **Platform:** Tool, Event
- **Governance:** Evaluation, Approval, Incident
- **Identity/People:** User, Employee
- **Ecosystem:** Partner

## Source-of-truth rules

1. Use the canonical artifacts above before inventing a new entity or field.
2. Implementation databases must conform to the governed model.
3. Derived indexes/caches do not become authoritative merely by containing a copy of the data.
4. Vector stores contain derived representations; source documents remain authoritative.
5. Repository specifications are version-controlled source for architecture/data-contract definitions.

## Discovery metadata

For each production dataset, implementation should additionally expose:

- Dataset/entity name
- Owning domain
- System of record
- Business owner
- Technical owner
- Classification
- Retention category
- Schema version
- Quality status
- Provenance requirements
- Access policy reference

## Agent discovery rule

Agents should consult this catalog before reading or writing governed data. If an entity, field, event, or relationship is absent or ambiguous, the agent must escalate rather than fabricate a schema.

## Change control

Catalog changes must be accompanied by the corresponding schema/policy update and follow `CHANGE_MANAGEMENT.md`. A catalog entry alone does not constitute implementation evidence.

## Definition of Done

The catalog is complete when every governed production dataset is mapped to a canonical entity/contract, system of record, owner, classification, schema version, access policy, and lifecycle policy.
