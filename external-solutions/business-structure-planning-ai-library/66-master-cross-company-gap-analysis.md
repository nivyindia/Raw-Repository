# Master Cross-Company Gap Analysis

**Status:** v1.0 — 2026-09-16

## What the library now covers

| Layer | Status |
|---|---|
| Strategy/intelligence | Covered |
| Sales/revenue | Covered |
| Marketing/growth | Covered |
| Social/content/creative | Covered |
| Website/WordPress/ecommerce | Covered |
| SEO/data/analytics | Covered |
| CRM/customer lifecycle | Covered |
| Documents/proposals/business communications | Covered |
| HR/people | Covered |
| Finance/accounting | Covered |
| Operations/PMO | Covered |
| Legal/compliance | Covered |
| IT/cybersecurity | Covered at discovery level |
| AI/automation | Covered |
| Knowledge management | Covered; infrastructure expanded here |
| Partnerships/internationalization | Covered |
| Product/SaaS | Covered |
| Procurement/supply chain | Covered at discovery level; infrastructure expanded here |
| Customer/community/events | Covered |
| Governance/measurement | Covered; AgentOps expanded here |
| Agent registry/identity/approval | **New cross-company layer** |
| Agent observability/evaluation | **New cross-company layer** |
| Process intelligence | **New cross-company layer** |
| Company memory/decision memory | **New cross-company layer** |
| Exception management | **New cross-company layer** |
| AI economics/ROI | Partially covered; needs implementation |
| Business continuity/failover | Gap to implement |
| Cross-agent delegation/A2A | Partially covered; needs controlled implementation |

## Remaining material gaps

### 1. AI asset registry
Need one authoritative inventory for agents, skills, prompts, MCP servers, workflows and policies.

### 2. Control plane
Need centralized policy, identity, tool permissions, approvals, budgets and audit.

### 3. Evaluation/AgentOps
Need repeatable test datasets, trace review, quality thresholds, regression testing and production monitoring.

### 4. Company memory
Need separated source memory, canonical company memory, workflow state, decisions and evaluation memory.

### 5. Process intelligence
Need event-driven process discovery before automating complex workflows.

### 6. Exception management
Need a company-wide queue for failed, blocked, low-confidence and policy-sensitive work.

### 7. AI economics
Need cost and value attribution by model, agent, workflow, customer and channel.

### 8. Continuity
Need provider/model/tool fallback, backup/restore, degraded-mode procedures and recovery tests.

### 9. Cross-agent orchestration
Need controlled delegation rather than unrestricted agent-to-agent autonomy.

## Research completeness conclusion

The major functional discovery categories are now represented. The next work should not be another broad list of departments. It should be **reuse testing, integration, governance and measurement**.

## Final architecture target

```text
                    HUMAN / EXECUTIVE
                           │
                    INTENT + APPROVAL
                           │
                 CONTROL / ROUTER LAYER
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
   SPECIALIST AGENTS     WORKFLOWS          SKILLS
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                  KNOWLEDGE + MEMORY
                           │
                MCP / API / CONNECTORS
                           │
                   SYSTEMS OF RECORD
                           │
              AUDIT + OBSERVABILITY
                           │
                  EVALUATION + COST
                           │
                 EXCEPTION + LEARNING
```

## Transition rule

`DISCOVERY → SOURCE VERIFICATION → LICENSE CHECK → FUNCTION TEST → CONTROL TEST → Nivy ADAPTATION → PILOT → PRODUCTION`

This marks the end of broad cross-company discovery and the beginning of controlled implementation/testing.
