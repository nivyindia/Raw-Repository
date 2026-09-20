# Exact Asset Qualification — Wave 5 — 2026-09

Wave 5 qualifies the 12 exact assets extracted in Wave 4. It separates license/content qualification from runtime qualification; an asset is not marked fully Qualified unless the evidence supports reuse in its intended form.

## Qualification statuses
- Qualified — Documentation Pattern: license identified and the reusable pattern can be adapted without requiring source runtime execution.
- License-Compatible — Runtime Pending: permissive license identified, but executable/runtime/dependency/security verification remains.
- Blocked — License/Provenance: license or provenance is insufficient for safe reuse.
- Adapt Only: source-specific behavior/policy must be rewritten rather than copied.

## Matrix
| ID | Exact asset | License | Runtime/dependency | Security/data | Decision | Nivy action |
|---|---|---|---|---|---|---|
| EA-001 | GTM intent-analyst.md | Apache-2.0 | Markdown agent asset; no local runtime required for the pattern | External signal/enrichment may involve APIs/PII | Qualified — Documentation Pattern | Adapt as generic Signal→Action agent contract |
| EA-002 | GTM generate-leads.md | Apache-2.0 | Uses sales-prospecting/plugin behavior; runtime not verified | Lead/contact PII and outbound compliance need policy gates | License-Compatible — Runtime Pending | Adapt recipe; do not copy source-specific commands unchanged |
| EA-003 | GTM call-strategist.md | Apache-2.0 | Markdown agent asset | Opportunity/customer data may contain confidential information | Qualified — Documentation Pattern | Adapt into Sales Call Preparation skill |
| EA-004 | SDR delivery-queue/SKILL.md | MIT | Queue/worker behavior is executable/integration dependent | Messaging, timezone, retry and outbound-rate controls need policy | License-Compatible — Runtime Pending | Reimplement/adapt queue contract; test separately |
| EA-005 | SDR workspace/AGENTS.md | MIT | Full SDR pipeline references CRM/enrichment/outreach components; not fully verified | BANT/outreach/sanctions rules are source-specific | Adapt Only / Runtime Pending | Extract architecture; rewrite Nivy policies and contracts |
| EA-006 | SDR workspace/SOUL.md | MIT | Agent operating document | Source-specific identity/security rules must not become Nivy policy automatically | Qualified — Documentation Pattern / Adapt Only | Use as AI Employee contract input; rewrite Nivy policy |
| EA-007 | Claude Code Skills cs-write-a-skill.md | MIT | Documentation workflow | Low direct data risk; generated skills still need security review | Qualified — Documentation Pattern | Canonical Nivy Skill Factory template |
| EA-008 | Claude Code Skills skill-tester/SKILL.md | MIT | Repository has pytest configuration; execution not performed | Test code/fixtures must be sandboxed | License-Compatible — Runtime Pending | Adapt into Skill Evaluation Harness |
| EA-009 | Claude Code Skills C-level advisor docs | MIT | Markdown command/agent pattern | Executive context is sensitive; authority remains Nivy-controlled | Qualified — Documentation Pattern / Adapt Only | Extract decision/briefing/freeze patterns only |
| EA-010 | SocialManager generate.py + prompts | No root LICENSE found in inspected contents | Python dependencies include Playwright, OpenAI, FastAPI, Uvicorn, multipart | LLM/browser execution and generated artifacts need sandboxing | Blocked — License/Provenance | Do not vendor/copy code; independently reproduce architecture until license is established |
| EA-011 | SocialManager AGENT.md | No root LICENSE found in inspected contents | Documentation asset | Brand/publish controls are source-specific | Blocked — License/Provenance | Research reference only; author Nivy contract independently |
| EA-012 | Openkoda ChatGPTPromptService.java | MIT | Java/Spring application; root POM identifies Spring Boot 3.0.5; runtime not executed | Dynamic model introspection needs strict data allowlisting | License-Compatible — Runtime Pending | Reproduce dynamic-context pattern; inspect dependency tree before code reuse |

## Repository-level evidence
| Source | License | Last repository push observed | Key evidence |
|---|---|---:|---|
| GTM Agents | Apache-2.0 | 2026-04-03 | LICENSE, SECURITY.md, tests/docs/configuration present |
| B2B SDR Agent Template | MIT | 2026-08-20 | LICENSE, extensive CHANGELOG.md, agent/workspace assets |
| Claude Code Skills | MIT | 2026-05-22 | LICENSE, pytest configuration, conventions/installation docs |
| SocialManager | License file not found at root | 2026-08-13 | Python requirements and tests present; license must be resolved before copying |
| Openkoda | MIT | 2025-02-19 | LICENSE, Maven POM, Docker/examples/application modules |

## Important findings
1. No asset is promoted to Implemented.
2. Documentation/prompt assets can be qualified for pattern adaptation without executing external code.
3. Executable assets remain Runtime Pending until dependencies, tests, secrets, network calls and Windows/Docker behavior are verified.
4. SocialManager assets are explicitly blocked for copying because a repository-level license was not found in the inspected root contents.
5. Source-specific policies are not Nivy policy; translate them into Nivy-owned policy/authority contracts.
6. Provenance must pin a source commit before vendoring. This wave records branch-level evidence; the next runtime/vendor step must record exact commit SHAs.

## Qualification pipeline
License → Provenance → Dependency → Runtime → Security → Data/PII → Tests → Windows/Docker → Contract Adaptation → Human Approval → Qualified → Adapt/Integrate

## Next wave
1. Pin exact source commit SHAs for every promoted asset.
2. Inspect manifests/lockfiles and transitive dependencies for EA-004, EA-008 and EA-012.
3. Run isolated runtime tests for executable assets.
4. Create canonical Nivy contracts for AI Employee, Skill, Signal→Action, Artifact Factory and Dynamic Context Assembly.
5. Update G46 qualification records and individual gap links only after evidence is reproducible.