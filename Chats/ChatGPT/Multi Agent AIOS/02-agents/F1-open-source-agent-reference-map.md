# Stage F — Open-Source Agent Reference Map

Purpose: use proven open-source agent patterns as implementation references while keeping Billion Dreams United OS as the governing architecture.

## Reference projects reviewed

| Reference | Useful patterns | AIOS adaptation |
|---|---|---|
| LeadReach AI | multi-channel discovery, enrichment, qualification, intent scoring, personalization | map capabilities into A034/A036/A039/A043/A044; keep our policy/approval layer authoritative |
| AI Sales Agent / Mesh Pilot | discovery → enrichment → drafting → HITL → send → reply learning | strengthen A044 with mandatory approval, suppression, audit and outcome feedback |
| Enverif | durable agent runs, persistent lead state, campaigns, schedules, delegation | adapt durable state and handoffs to Odoo/PostgreSQL + n8n/LangGraph |
| OpenOutreach | discovery + qualification + enrichment + send guards | use verdict/explanation and send-guard patterns; do not bypass AIOS communication policy |
| sales-ai-agents | multi-source enrichment, previous-thread context, follow-up, executive summaries | adapt account context, conversation memory and follow-up intelligence |

## Architecture rule

Existing open-source projects are references, not replacements for AIOS contracts. All adapted agents must conform to:

`Agent → Skill → Tool → Action`

and the AIOS permission matrix, AI risk policy, communication policy, suppression model, approval model, IAM baseline, audit requirements, and event contracts.

## Priority upgrades

1. A034 Lead Discovery — multi-source parallel discovery + provenance + deduplication.
2. A036 Lead Enrichment — multi-source cross-checking + freshness/confidence.
3. A039 Lead Scoring — ICP fit + intent + reachability + strategic value + data quality.
4. A043 Outreach Strategy — research/signal-driven channel and sequence strategy.
5. A044 Email Outreach — personalization + approval queue + suppression + delivery/outcome feedback.
6. A050 Follow-Up — stale-opportunity detection + conversation context + policy-gated drafts.

## Licensing rule

Only use source code when its license permits the intended use. Otherwise use publicly documented architecture/behavior as inspiration and implement independently. Never import credentials, private data, proprietary prompts, or restricted code.

## Sources

- LeadReach AI: https://github.com/getleads-humain/Lead-Reach
- AI Sales Agent: https://github.com/Nuraveda-Labs/ai-sales-agent
- Enverif: https://github.com/ShubhamTuts/enverif
- OpenOutreach: https://github.com/eracle/OpenOutreach
- sales-ai-agents: https://github.com/sneurgaonkar/sales-ai-agents
- LangGraph: https://github.com/langchain-ai/langgraph
