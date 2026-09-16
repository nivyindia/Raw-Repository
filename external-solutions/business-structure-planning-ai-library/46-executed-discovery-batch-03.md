# Executed Discovery Batch 03 — Remaining Company Operating Gaps

Date: 2026-09-16
Status: DISCOVERED / SOURCE-VERIFIED (where stated)
Purpose: extend the reuse library into operations, security, legal/compliance, data, marketplace and agent-platform gaps.

## Reuse rule
REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

| Area | Reusable solution | Type | What it provides | Access/license note | Official source | Nivy use |
|---|---|---|---|---|---|---|
| Operations / AI Ops | Carbene Forge | AI operations platform | Skills, specialized agents, hooks, automation and work capture around Claude Code | MIT stated by repository | https://github.com/CarbeneAI/Forge | Candidate base for company-wide agent workspace |
| Legal / Compliance | ThomasMoreAI Legal Skills Open | Skill library | 3,500+ legal skills, 39 jurisdictions, 200+ practice plugins, MCP routing | Apache-2.0 stated | https://github.com/ThomasMoreAI/legal-skills-open | Legal/compliance research and review layer; counsel approval required |
| Legal Ops | AgentCounsel | Legal workflow skill library | Contract review, intake, triage, drafting and legal workflow structures | MIT stated | https://github.com/zgbrenner/agentcounsel | Reusable legal SOP/skill patterns |
| Legal AI | AnyLegal OSS | Legal agent harness | Multi-LLM harness, Anthropic-format SKILL.md support, workspace KB | MIT + additional terms; verify before commercial reuse | https://github.com/anylegal-ai/anylegal-oss | Architecture reference / possible legal-agent runtime |
| Cybersecurity | Anthropic Cybersecurity Skills | Security skill library | 754 skills across 26 security domains; mappings to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, AI RMF | Apache-2.0 stated | https://github.com/hliosone/anthropic-cybersecurity-skills | Security analyst skill layer; authorization required for offensive tasks |
| Security operations | SECS | Security agent environment | 35 security skills, guardrails, toolchain and practice lab | License should be checked before adoption | https://github.com/EvilFreelancer/secs | Defensive security / controlled testing patterns |
| Agent governance | PolicyAware | AI control plane | Policy enforcement, PII redaction, MCP governance, routing and audit traces | Verify current license before production | https://github.com/ktirupati/policyaware | Governance layer for Nivy agents |
| Agent evaluation | Future AGI | Evaluation/observability platform | Evals, tracing, simulations, datasets, guardrails and optimization | Apache-2.0 stated in prior discovery; recheck before production | https://github.com/future-agi/future-agi | Agent QA/evaluation |
| Agent observability | OpenLIT | Observability/evaluation | OpenTelemetry traces for LLMs, tools, retrieval, memory, sub-agents and evaluations | Open-source; verify license/version | https://github.com/openlit/openlit | Production monitoring |
| Agent observability | Arize Phoenix | AI observability/evaluation | Tracing, evaluation, datasets, experiments, prompt management and MCP | Open-source; verify current license | https://github.com/Arize-ai/phoenix | Agent quality and debugging |
| Marketplace / agent economy | Agent Marketplace | Agent marketplace reference | Agent delegation, escrow/reputation and proof-of-work architecture | License/crypto architecture require review | https://github.com/Juwebien/agent-marketplace | Architecture reference for future Nivy marketplace |
| Legal discovery | Lawgent | Legal agent | Multi-jurisdiction research, specialist agents and citation verification | Open-source; verify license | https://github.com/WenzhuoXu/lawgent | Legal research architecture reference |
| Legal discovery | Legal AI Skills | Skill/plugin library | 160+ legal skills across contracts, corporate, regulatory, privacy, tax, employment and more | Repository license should be checked | https://github.com/rohasnagpal/legal-ai-skills | India + international legal workflow patterns |

## Gaps deliberately still open

The following require another targeted search rather than being declared complete:
- PMO/project management agent systems
- procurement and supply-chain agents
- BI/data/analytics agent libraries
- localization/internationalization agent systems
- event/webinar/education operating systems
- marketplace seller/operator systems
- industry-specific operating packs
- deeper cloud/ITSM systems

## Adoption safeguards
1. Verify repository license and third-party notices before copying/adapting.
2. Prefer links + metadata over copying upstream content.
3. Separate discovered, tested and production-adopted states.
4. Require human approval for legal, financial, security-sensitive and external-communication actions.
5. Run imported agent workflows in a sandbox before granting production credentials.
6. Record source URL, version/date, license and adaptation notes in the adoption tracker.

## Source evidence
Current web discovery confirms the ThomasMoreAI library describes 3,500+ legal skills across 39 jurisdictions and 200+ plugins under Apache-2.0; AgentCounsel describes portable Markdown legal workflows under MIT; and the cybersecurity skills repository describes 754 skills across 26 domains with five framework mappings. These claims should be rechecked at adoption time because repositories change. citeturn0search0turn0search1turn0search6
