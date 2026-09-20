# Exact Asset Extraction — Wave 4 — 2026-09

Wave 4 moves from repository-level candidates to **exact reusable assets**. These are still **Pre-Qualification** until license, security, runtime and dependency checks are completed.

## Extraction records

| ID | Source | Exact asset | What it provides | Nivy destination | Status |
|---|---|---|---|---|---|
| EA-001 | [GTM Agents](https://github.com/gtmagents/gtm-agents) | `plugins/intent-signal-orchestration/agents/intent-analyst.md` | Intent signal audit → normalization → scoring → insight → distribution; outputs signal dashboard, account dossiers and alerts. | G03/G05; Sales/RevOps AI workforce; intent-signal workflow. | Pre-Qualification |
| EA-002 | [GTM Agents](https://github.com/gtmagents/gtm-agents) | `templates/recipes/generate-leads.md` | Concrete lead-generation recipe with ICP criteria, qualification fields, CRM export and follow-on email/pipeline steps. | P03/P17/P18; Lead Generation Agent. | Pre-Qualification |
| EA-003 | [GTM Agents](https://github.com/gtmagents/gtm-agents) | `plugins/sales-calls/agents/call-strategist.md` | Opportunity context → objectives → stakeholder map → agenda/questions → internal alignment → debrief. | P18; Sales Call Preparation workflow. | Pre-Qualification |
| EA-004 | [B2B SDR Agent Template](https://github.com/iPythoning/b2b-sdr-agent-template) | `skills/delivery-queue/SKILL.md` | Segmented scheduled delivery, queue, cancellation, retries, timezone and quiet-hours configuration. | L2/L3 outbound messaging; scheduling/queue capability. | Pre-Qualification |
| EA-005 | [B2B SDR Agent Template](https://github.com/iPythoning/b2b-sdr-agent-template) | `workspace/AGENTS.md` | Full SDR pipeline: capture → dedupe → BANT → CRM → enrichment → quote approval → negotiation → reporting → nurture → outreach → multi-channel orchestration. | L5 Sales/RevOps; L7 CRO/RevOps Manager; AI SDR Employee. | Pre-Qualification |
| EA-006 | [B2B SDR Agent Template](https://github.com/iPythoning/b2b-sdr-agent-template) | `workspace/SOUL.md` | AI employee operating principles, concise communication, memory protocol, security, approval boundaries and data-handling rules. | Generic Nivy AI Employee contract; G25 AI workforce lifecycle; policy/authority layer. | Pre-Qualification |
| EA-007 | [Claude Code Skills](https://github.com/AlexBramall/claude-code-skills) | `docs/commands/cs-write-a-skill.md` | Repeatable method for authoring standardized skills. | Skill Registry / Skill Factory / G46 solution qualification. | Pre-Qualification |
| EA-008 | [Claude Code Skills](https://github.com/AlexBramall/claude-code-skills) | `engineering/skills/skill-tester/SKILL.md` | Skill testing/evaluation pattern for reusable skills. | Skill Evaluation Harness; G31 AI lifecycle / G46 qualification. | Pre-Qualification |
| EA-009 | [Claude Code Skills](https://github.com/AlexBramall/claude-code-skills) | `docs/skills/c-level-advisor/c-level-agents*.md` | C-level agent briefing/decision/freeze command patterns. | L8 AI Executive layer; decision/authority controls. | Pre-Qualification |
| EA-010 | [SocialManager / Zylo Deck Studio](https://github.com/Aznair25/SocialManager) | `src/generate.py` + `src/zylo/prompts/*` | Topic/source → LLM generation → validated deck spec → deterministic render pipeline; prompt/framework separation. | P14/P16/P17; Content→Creative workflow. | Pre-Qualification |
| EA-011 | [SocialManager / Zylo Deck Studio](https://github.com/Aznair25/SocialManager) | `AGENT.md` | Explicit agent operating rules, brand/design source of truth, human review and no-auto-publish boundary. | Business Artifact Factory; human approval gate; brand governance. | Pre-Qualification |
| EA-012 | [Openkoda](https://github.com/openkoda/openkoda) | `ChatGPTPromptService.java` | Builds LLM prompts dynamically from context services and entity data models, including fields, getters/setters, hints and relations. | Universal context/data-to-agent interface; L8/L9 context assembly. | Pre-Qualification |

## Reuse patterns extracted

### 1. Signal → Action
`Sources → Normalize → Score → Contextualize → Distribute → Workflow`

This should become a generic Nivy event-to-action pattern, not a sales-only implementation.

### 2. AI Employee Contract
From the SDR template:
`Identity → Role → Responsibilities → Memory → Tools → Policies → Approval Authority → Reporting → Escalation`

This can become the base contract for all Nivy AI employees.

### 3. Skill Contract
From Claude Code Skills:
`Trigger/Intent → Instructions → References/Tools → Execution → Test/Evaluation`

Nivy should standardize this rather than importing incompatible skill formats.

### 4. Deterministic Artifact Factory
From SocialManager:
`Input → Generation → Structured Spec → Validation → Deterministic Render → Human Review → Publish`

This pattern applies beyond social carousels to PPT, proposals, reports, landing pages and other business artifacts.

### 5. Dynamic Context Assembly
From Openkoda:
`Entity/Data Model → Eligible Fields/Methods → Hints/Relations → Prompt Context`

This is relevant to the Universal Company State / Universal Data Model work.

## Qualification gates still required

Before copying or executing any asset:
1. exact license file and compatibility;
2. dependency and runtime inspection;
3. security / prompt-injection / secret handling review;
4. PII and data-retention review;
5. external API/SaaS dependency mapping;
6. test/reproducibility check;
7. Windows/Docker compatibility where relevant;
8. Nivy input/output contract adaptation;
9. provenance record with source commit;
10. human-approval boundary for consequential actions.

## Next extraction targets

- GTM Agents: inspect additional sales-prospecting, email-marketing, pipeline-audit and orchestration assets.
- B2B SDR: extract HEARTBEAT, MEMORY, TOOLS and approval/health-check assets.
- Claude Code Skills: enumerate department skill packs and identify duplicate coverage against Nivy catalogs.
- SocialManager: extract validation rules, rendering interfaces and framework catalog.
- Openkoda: inspect event listeners, schedulers, RBAC/audit and automation APIs.

**Rule:** exact asset extraction does not equal permission to copy. License and security qualification precede vendoring or execution.
