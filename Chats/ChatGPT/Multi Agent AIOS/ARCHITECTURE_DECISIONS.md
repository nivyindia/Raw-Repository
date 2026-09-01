# BILLION DREAMS UNITED OS — ARCHITECTURE DECISIONS

**Version:** 1.0  
**Stage:** A.5  
**Status:** Locked baseline decisions only

> This document records only decisions already established in the master implementation plan. It is not a place to introduce new architecture choices.

## ADR-001 — Odoo, not OpenProject, as the Primary Business Operations Platform

**Decision:** Use **Odoo Community Edition + appropriate OCA modules** as the primary business operations/ERP platform. OpenProject is not the primary project-management system.

**Rationale:** Odoo provides the broader operational backbone required across CRM, sales, invoicing, accounting/finance, projects, tasks and related business processes. Avoid creating a parallel system of record where Odoo can serve the function.

**Consequence:** Business records and operational workflows should integrate with Odoo rather than establishing OpenProject as a competing operational core.

## ADR-002 — Odoo, not a Second CRM

**Decision:** Do not maintain a second CRM as a parallel source of truth. Odoo CRM is the canonical CRM layer.

**Rationale:** A second CRM would create duplicated customer/lead records, synchronization complexity and ownership ambiguity.

**Consequence:** External tools may support specific acquisition/communication functions, but canonical Lead, Account, Opportunity and related business records remain in Odoo.

## ADR-003 — One Vector Database

**Decision:** Standardize on **one vector database** for the AIOS rather than deploying multiple competing vector stores.

**Baseline:** Qdrant is the selected vector database in the implementation stack.

**Rationale:** A single vector layer reduces operational complexity, duplicated indexes, inconsistent retrieval and unnecessary infrastructure cost.

**Consequence:** AI agents and knowledge workflows should use the canonical Qdrant layer unless a future ADR explicitly changes this decision.

## ADR-004 — One Workflow Engine

**Decision:** Standardize on **one primary workflow/orchestration engine** for business automation.

**Baseline:** n8n is the primary workflow engine. LangGraph may be used where agent-state orchestration is specifically required, but it is not a second general business workflow platform.

**Rationale:** Centralizing business workflow automation prevents fragmented orchestration and makes triggers, retries, events, credentials and monitoring easier to govern.

**Consequence:** Business automation should default to n8n; specialized agent orchestration must have a clear boundary and integration contract.

## ADR-005 — Revenue-First Build Order

**Decision:** Build and productionize the revenue-generating acquisition/sales loop before lower-priority internal or scale capabilities.

**Rationale:** The immediate objective is to create a functioning revenue engine. The implementation plan therefore prioritizes Market Research → ICP → Lead Discovery → Enrichment/Verification → Scoring → Outreach → Follow-up → Reply Triage → Qualification → Meeting Prep → Proposal → Onboarding.

**Consequence:** Tier-1 revenue agents and their supporting workflows receive implementation priority before broad autonomous expansion.

## Decision Governance

- These five ADRs are the locked baseline for Stage A.
- A conflicting proposal must not silently override an ADR.
- Any change requires the change-management process once `CHANGE_MANAGEMENT.md` is active.
- New architecture decisions belong in a future numbered ADR; historical decisions must remain traceable.

## Related Governance Artifacts

- `Billion-Dreams-United-Implementation-Plan-v2-Granular-Steps.md`
- `id-master-list.yaml`
- `COMPLETION_MATRIX.md`
- `SYSTEM_MASTER_INDEX.md`
- `BUILD_RULES.md` (A.6)
- `CHANGE_MANAGEMENT.md` (A.7)
