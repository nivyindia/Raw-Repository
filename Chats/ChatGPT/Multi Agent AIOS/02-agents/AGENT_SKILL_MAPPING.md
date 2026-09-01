# BILLION DREAMS UNITED OS — AGENT ↔ SKILL MAPPING

**Stage:** C.3  
**Version:** 1.0  
**Status:** Baseline registry contract

## Purpose

Define the canonical mapping contract between registered agents (`02-agents/registry.yaml`) and reusable skills (`03-skills/registry.yaml`).

## Mapping rules

- An agent may use one or more skills.
- A skill may be reused by multiple agents.
- Only skills explicitly mapped to an agent are considered permitted by default.
- Agent execution must respect the agent's tool and permission scope.
- Missing or ambiguous mappings must fail closed and escalate rather than invent capabilities.
- Mapping changes require version control and review under the project change-management process.

## Canonical mapping structure

```yaml
mappings:
  - agent_id: A001
    skill_ids: [SK001, SK002]
    mode: required|optional
    version: "1.0"
```

## Initial capability domains

The registry is organized around these capability families:

- Research & intelligence
- Lead generation & enrichment
- Sales & outreach
- Marketing & content
- Client onboarding & success
- Project & operations management
- Finance & compliance
- Software/IT delivery
- AI/agent operations
- Data & analytics
- Governance, QA & security

## Resolution policy

At runtime, capability resolution should follow:

`Agent → Approved Skill → Approved Tool → Authorized Action`

An agent must not bypass the skill layer to gain an undeclared capability.

## Version compatibility

- Agent definitions must declare the compatible skill version/range when versioning is material.
- Breaking skill changes require compatibility review for every dependent agent.
- Retired skills cannot be newly assigned to agents.

## Validation requirements

Before production activation of a mapping, validate:

1. Agent ID exists.
2. Skill ID exists.
3. Skill is active/approved.
4. Agent is authorized to use the skill.
5. Required tools are available and authorized.
6. Skill input/output contracts are compatible with the agent.
7. Test evidence exists for the integrated capability.

## Initial mapping policy

Because C.1/C.2 registries contain intentionally conservative skeleton entries, mappings should be added only when the corresponding agent and skill definitions are verified. `UNMAPPED` is a valid state and is preferable to an invented mapping.

## Definition of Done

An agent-skill mapping is production-ready only when both registry entries are verified, compatibility is established, permissions are defined, integration tests pass, and the mapping is version-controlled.
