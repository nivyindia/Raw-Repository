# Executed Discovery Batch 02 — Creative, Growth, Operations, Security, Data & Channels

**Status:** Discovered / source-verified where stated  
**Date:** 2026-09-16  
**Objective:** Find existing reusable systems, agents, skills and operating components before building custom Nivy systems.

## Reuse rule
REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

> This is a source catalog, not an endorsement. Verify current licensing, maintenance, security, API availability and production suitability before adoption.

| Area | Existing solution | Type | What can be reused | Access / license | Official source | Nivy fit |
|---|---|---|---|---|---|---|
| Creative/social | Social Media Skills | 106-agent-skill library | Strategy, writing, video, design, publishing, analytics; integrations for Canva, video, voice/music and editing | Open source; verify individual tool licenses | https://github.com/social-media-skills/skills | High |
| Marketing | Marketing Agent OS | Portable agent-skill OS | 236 skills across SEO, GEO/AEO, content, CRO, paid, lifecycle, social, analytics, sales and RevOps | Apache-2.0 wrapper; retain upstream licenses | https://github.com/iamwaqargulzar/Marketing-Agent-OS | Very high |
| Marketing | Digital Marketing Pro | Multi-agent marketing OS | 24 specialist agents plus 163 Agent Skills; strategy, SEO, AEO/GEO, paid media, CRM, analytics, localization | Open-source repository; verify current license | https://github.com/indranilbanerjee/digital-marketing-pro | Very high |
| Agent skills | skills.ws | Skill registry/catalog | Searchable skills for marketing, growth, design, analytics, operations, finance and agent building | Free/open-source catalog; verify each skill | https://www.skills.ws/ | High |
| Design/ops | Claude Skills collection | Broad skill library | 245 skills, 653 Python tools, 32 agent/persona definitions and compliance frameworks | Verify repository license and each dependency | https://github.com/Ck1sap/borghei-Claude-Skills | High |
| Social/community | Crewm8 Social Media Manager Skill Graph | Skill graph | 37 agent-agnostic social skills across X, LinkedIn, Instagram and TikTok | MIT stated by repository | https://github.com/gokulsvision/Crewm8-Social-Media-Manager-Skill-Graph | High |
| Messaging/desktop | Jarvis AI Desktop Agent | Self-hosted agent platform | Multi-agent execution, browser automation, RAG, office files, email, calendar, WhatsApp, Telegram, skills and sandbox/security | Apache-2.0; third-party licenses remain separate | https://github.com/dev-core-busy/jarvis | High |
| Messaging | OpenClaw | Chat-first personal/ops agent | WhatsApp, Telegram, Discord, Slack, Signal, iMessage; browsing, files, email, calendar and skills | MIT stated by surfaced source; verify upstream before deployment | https://github.com/openclaw/openclaw | High |
| Messaging | KairoClaw | Self-hosted AI ops platform | Multi-channel AI across Telegram, WhatsApp and web, memory, tools, RBAC and admin dashboard | MIT stated by project | https://www.kairoclaw.com/ | High |
| AI agent discovery | Awesome AI Agents 2026 | Curated registry | Categories for creative agents, data, cybersecurity, localization, CRM, research, voice and automation | Catalog; inspect individual project licenses | https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026 | High |
| Agent governance | OWASP Agentic Skills Top 10 | Security framework | Security risks and mitigations for agent skills across major skill ecosystems | Public OWASP project | https://owasp.github.io/www-project-agentic-skills-top-10/ | Critical |
| Skill governance | OpenSkill | Skill registry/security layer | Search 8,000+ skills, private registries, security audits and role-based access | Free individuals; open-source CLI; verify service terms | https://www.openskill.sh/ | High |
| Marketing | Marketing Agent OS + Social Skills combination | Composable stack | Reuse broad marketing skills plus specialized social/media execution instead of rebuilding | Mixed upstream licenses | Sources above | Very high |

## Batch-02 coverage gaps still requiring deeper discovery

- Dedicated open-source video production/editing pipelines and audio/podcast production systems.
- PPC-specific agent/workflow libraries for Google/Meta/LinkedIn ads with safe approval gates.
- PMO/project-management agent packs and reusable delivery SOP libraries.
- ITSM, cloud operations, DevSecOps and security-operation agent packs.
- Legal/compliance/privacy operations with verified licenses and jurisdiction coverage.
- BI/data-engineering/data-quality agent skills beyond general analytics libraries.
- Localization/internationalization systems for multilingual content, websites and market entry.
- Procurement/supply-chain and vendor-management agent systems.
- Events/webinars/education operating packs.
- Marketplace/platform operations and industry-specific operating packs.

## Evidence notes

- The Social Media Skills repository explicitly lists image generation/editing, video generation, voice/music, editing/clipping and Canva-related skills. citeturn0search5
- Marketing Agent OS reports 236 installable skills covering SEO, GEO/AEO, content, CRO, paid media, lifecycle, social, analytics, sales and RevOps, with an Apache-2.0 wrapper and retained third-party attribution. citeturn0search8
- Digital Marketing Pro describes 24 specialist agents and a larger Agent Skills layer spanning marketing execution and governance. citeturn0search12turn0search13
- Jarvis combines multi-agent execution, browser automation, knowledge retrieval, office automation, messaging channels and sandbox/security controls. citeturn0search0
- OWASP's Agentic Skills Top 10 is directly relevant to screening third-party skills before allowing them into a company agent environment. citeturn0search9

## Adoption status vocabulary

- **Discovered:** found and recorded.
- **Source-verified:** official project/source checked.
- **License-checked:** license terms checked sufficiently for cataloging; still recheck before production.
- **Test candidate:** selected for sandbox evaluation.
- **Adapted:** integrated into Nivy-specific workflows.
- **Production:** passed security/evaluation/approval requirements and is actively used.
