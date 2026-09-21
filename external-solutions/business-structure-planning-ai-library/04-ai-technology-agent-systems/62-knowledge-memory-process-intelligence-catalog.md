# Knowledge, Memory & Process Intelligence Catalog

**Status:** v1.0 — 2026-09-16

## Why this layer matters

Agents need reliable context, not just prompts. Nivy needs company memory, source provenance, document lifecycle, process maps, exception detection and continuous learning.

| Capability | Asset/source | Reuse pattern | Nivy target | Priority |
|---|---|---|---|---:|
| Enterprise knowledge | SAG | connected/searchable/traceable knowledge base | Company Knowledge Layer | P1 |
| Enterprise search | existing enterprise-search/plugin patterns | search + open + evidence | Knowledge Router | P0 |
| Agentic retrieval | AgenticRAG research | iterative search/find/open/summarize | Evidence-first research agent | P1 |
| Process mining | ProcessM | event ingestion, conformance, deviation, root cause, KPI | Process Intelligence Layer | P1 |
| SOP mining | existing SOP-to-skill patterns | process → SOP → skill | Process Mining/Skill Factory | P1 |
| Decision memory | Git/Notion structured records | decision + evidence + owner + expiry | Decision Registry | P0 |
| Company terminology | plugin context patterns | canonical terms, aliases, prohibited terms | Terminology Registry | P0 |
| Research provenance | Git + source registry | source, date, claims, verification | Evidence Registry | P0 |
| Knowledge freshness | lifecycle controls | owner, review date, stale flag | Knowledge Maintenance Agent | P1 |
| Memory governance | agent memory patterns | scoped, permissioned memory | Company Memory Policy | P1 |
| Feedback learning | eval datasets | failures → test cases → regression | Continuous Improvement Store | P1 |

## Memory layers

1. **Source memory:** raw external sources and provenance.
2. **Company memory:** approved facts, policies, terminology and operating knowledge.
3. **Workflow memory:** state of ongoing work.
4. **Decision memory:** decisions, rationale, owner and expiry/review date.
5. **Agent memory:** scoped preferences/context needed for a task.
6. **Evaluation memory:** failures, corrections and regression cases.

Never merge these blindly. Each layer needs ownership and permissions.

## Knowledge lifecycle

`Discover → Ingest → Classify → Extract → Verify → Approve → Publish → Index → Use → Feedback → Review → Supersede/Archive`

## Process intelligence lifecycle

`Observe events → reconstruct process → map variants → identify bottlenecks → detect deviations → root-cause analysis → propose redesign → simulate/test → approve → automate → monitor`

Process intelligence platforms combine process mining, modeling and monitoring and are increasingly used to identify where AI-agent deployment can add operational value. citeturn0search8

ProcessM is an open-source example that ingests events, models processes, checks conformance, classifies deviations, performs root-cause analysis and calculates KPIs. citeturn0search10

AgenticRAG research supports the idea of iterative tool-based retrieval rather than relying only on a fixed single-shot retrieval result. citeturn0academia47

## Nivy implementation rule

GitHub remains the provenance/version layer; Notion can serve human-facing knowledge/workspace views; a search/RAG layer serves agents; structured registries hold canonical facts, decisions, skills and asset metadata. Do not use one database as an undifferentiated memory dump.
