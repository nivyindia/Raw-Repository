# Reusable Prompt Patterns

These are **original synthesis patterns** derived from the research. They are not copied verbatim from the linked libraries.

## Pattern 01 — Existing Solutions Discovery

```text
ROLE: Existing Solutions Discovery Agent

OBJECTIVE:
Find existing software, AI agents, skills, prompt libraries, templates, workflows,
open-source repositories, APIs and commercial products that can perform or support:
[CAPABILITY]

RESEARCH:
Search GitHub, official vendor sites, template marketplaces, documentation,
community repositories and credible business/strategy sources.

FOR EACH RESULT CAPTURE:
- Name
- Category
- What it does
- Department/use case
- Open source / free / freemium / paid
- License or access model if visible
- Maintenance/activity signal
- Integration method
- Required platform/model
- Reusability
- URL
- Evidence/source
- Risks/limitations

RULE:
Do not recommend building custom software until existing options have been exhausted.
```

## Pattern 02 — Company Structure Designer

```text
ROLE: Organization Design Analyst

INPUT:
Company strategy, business model, products/services, target markets, growth stage,
headcount, geography, operating constraints and automation goals.

DESIGN:
1. Business capabilities
2. Departments/functions
3. Sub-functions
4. Roles
5. Responsibilities
6. Decision rights
7. KPIs
8. Core processes
9. Cross-functional workflows
10. AI/automation opportunities
11. Human approval points
12. Governance

OUTPUT:
Current-state hypothesis → target operating model → organization map → role map →
process map → automation map → implementation dependencies.
```

## Pattern 03 — Department Buildout

```text
ROLE: Department Architect

DEPARTMENT: [DEPARTMENT]

Create a reusable department blueprint containing:
- Mission
- Objectives
- Capabilities
- Sub-functions
- Roles
- Responsibilities
- Inputs
- Processes
- Outputs
- KPIs
- Systems/tools
- Required knowledge
- SOPs
- AI skills/agents
- Automation opportunities
- Human review points
- Internal customers
- External customers
- Dependencies
- Risks
- 30/60/90-day implementation sequence

Before creating anything custom, identify existing public skills, prompts, templates,
software and workflows that can be reused.
```

## Pattern 04 — Strategy-to-Execution Cascade

```text
Translate:
Vision → strategic themes → annual objectives → department objectives → team OKRs →
projects → tasks → KPIs → review cadence.

For every node identify owner, dependencies, evidence, metric and review frequency.
Flag contradictions or objectives that cannot be measured.
```

## Pattern 05 — SOP Generator

```text
Interview the process owner to extract one repeatable process.
Then create:
1. SOP title
2. Purpose
3. Scope
4. Owner
5. Trigger
6. Inputs
7. Preconditions
8. Step-by-step procedure
9. Decision rules
10. Exceptions
11. Quality checks
12. Outputs
13. Systems used
14. Metrics
15. Escalation rules
16. Version/change history
17. AI automation opportunities

Validate the SOP with the owner before marking it canonical.
```

## Pattern 06 — AI Agent Candidate Discovery

```text
For each business process, determine whether it is:
A. Human-only
B. AI-assisted
C. AI-agent suitable
D. Deterministic automation suitable
E. Multi-agent workflow suitable

Explain the decision using task characteristics, required judgment, data access,
risk, repeatability, exception rate and human approval requirements.
Then search for existing implementations before proposing custom development.
```

## Pattern 07 — Framework Reconciliation

```text
Given several strategy/organization frameworks:
- Map overlapping concepts
- Identify unique concepts
- Identify contradictions
- Identify required inputs
- Identify expected outputs
- Identify where each framework is strongest
- Produce one neutral consolidated operating model

Do not blindly merge frameworks. Preserve source attribution and mark adaptations.
```

## Pattern 08 — Reuse vs Build Decision

```text
For capability [X], compare:
1. Existing open-source
2. Existing free tool
3. Existing SaaS
4. Existing AI skill/agent
5. Existing prompt/template
6. Existing API/workflow
7. Adaptation/integration
8. Custom build

Score only on explicit criteria such as capability fit, integration effort,
maintenance, license, security, cost and customization. Do not use an overall
"best" score; provide the evidence matrix and decision rationale.
```
