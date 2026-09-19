# End-to-End Business Systems Catalog

**Research date:** 2026-09-16

These are higher-level systems that can inform the Nivy Company OS rather than isolated prompts or automations.

| System | Scope | Access | What it demonstrates | Link |
|---|---|---|---|---|
| Stratisian Operating System | MSME operations | Free | Nine-module operating architecture with protocols, templates and metrics/review rhythm | https://stratisian.com/os |
| Company Operating System — Focus688 | Company management | Open source / MIT stated | Large operating-system reference with chapters, playbooks and AI-native organization concepts | https://github.com/Focus688/company-operating-system |
| Runlane | Agentic business operations | Commercial/free trial | Role agents + skills + SOP-derived runbooks + human review + budgets + audit trail | https://runlane.app/ |
| n8n CRM workflow ecosystem | Automation infrastructure | Mixed / many free | Practical library of hundreds of CRM and AI workflows | https://n8n.io/workflows/categories/crm/ |
| Agent Marketplace | Ready-made AI workers | Commercial/mixed | Agent packaging, integrations, scoped permissions, deployment and human-in-loop patterns | https://agentmarketplace.ai/ |
| Arahi AI Marketplace | Ready-made agent templates | Commercial/mixed | Editable agents across core business departments and integrations | https://arahi.ai/marketplace |
| MarketInc AI | Agent marketplace | Free | Large catalog of task-specific business/marketing agents and chained agent workflows | https://marketinc.io/ |

## End-to-end architecture to extract

The reusable pattern appearing across these systems is:

`Role / outcome → context + knowledge → skill/runbook → tools/connectors → agent/workflow → human approval → system of record → KPI → audit → feedback`

This should be treated as an architecture pattern to test, not as a reason to purchase any particular platform.

## Build-vs-reuse gate

Before implementing a new Nivy component, ask:

1. Does an existing end-to-end system already solve most of this?
2. Can an existing skill or runbook be adapted?
3. Is there an importable automation?
4. Is there an existing open-source component?
5. Is the missing part only integration/configuration?
6. What genuinely remains unique to Nivy?

Only item 6 should normally trigger custom development.
