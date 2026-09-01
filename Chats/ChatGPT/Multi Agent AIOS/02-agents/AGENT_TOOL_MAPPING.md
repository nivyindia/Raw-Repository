# BILLION DREAMS UNITED OS — AGENT ↔ TOOL MAPPING

**Stage:** C.4  
**Version:** 1.0  
**Status:** Baseline registry contract

## Purpose

Define how registered agents obtain tool capabilities through explicit, authorized mappings.

## Capability chain

`Agent → Skill → Tool → Authorized Action`

Agents must not directly acquire undeclared tools or bypass the skill/permission layer.

## Mapping contract

```yaml
mappings:
  - agent_id: A001
    skill_id: SK001
    tool_ids: [TOOL001]
    permissions: [read]
    version: "1.0"
```

## Permission classes

- `read` — retrieve permitted information.
- `write` — create or update permitted records.
- `execute` — run an approved operation/workflow.
- `export` — export governed data; requires explicit authorization.
- `admin` — configuration/administrative capability; restricted to approved agents/operators.

## Security rules

1. Least privilege is the default.
2. Tool access must be explicitly mapped.
3. Sensitive/destructive actions require elevated authorization and applicable human approval.
4. Credentials/secrets are never embedded in agent definitions or mapping files.
5. Disabled, retired, or unapproved tools cannot be assigned to production agents.
6. Cross-company data access requires an explicitly approved scope.

## Runtime validation

Before tool invocation, the execution layer must verify:

1. Agent exists and is active.
2. Skill exists and is approved.
3. Tool exists and is approved.
4. Agent-skill mapping exists.
5. Agent-tool mapping exists.
6. Requested permission is within the mapping.
7. Data/company scope is authorized.
8. Required approval gate is satisfied.
9. Invocation is logged with correlation ID.

If any check fails, the action must fail closed and return a structured authorization error.

## Tool classes

Typical tool classes include:

- CRM/business systems
- Communication channels
- Search/research
- Browser/scraping
- Databases
- File/document storage
- Code/repository systems
- Analytics/BI
- Finance/accounting
- Project management
- AI/LLM inference

The concrete tool registry remains the authoritative source for tool IDs, versions, endpoints, and lifecycle status.

## Audit

Every privileged tool invocation should record:

`agent_id + skill_id + tool_id + action + permission + company_id + actor + timestamp + correlation_id + outcome`

Failures must not be represented as successful tool execution.

## Versioning

Breaking changes to a tool or permission contract require compatibility review of dependent agents and skills. Retired tools require migration or explicit decommissioning of dependent mappings.

## Definition of Done

An agent-tool mapping is production-ready only when the agent, skill, and tool are verified; permissions and scope are explicit; authorization/approval behavior is tested; and invocation auditability is implemented.
