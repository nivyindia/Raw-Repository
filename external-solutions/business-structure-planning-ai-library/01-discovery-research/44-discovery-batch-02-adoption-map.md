# Discovery Batch 02 — Adoption Map

## Priority test queue

| Priority | Candidate | First Nivy use | Test method | Gate |
|---|---|---|---|---|
| P0 | Marketing Agent OS | Marketing/SEO/GEO/content/CRO skill base | Sandbox skills against 3 real Nivy briefs | Human approval + output quality + license review |
| P0 | Digital Marketing Pro | End-to-end marketing agent decomposition | Run strategy → SEO → content → CRM → analytics sequence | Human approval + reproducibility + cost |
| P0 | Social Media Skills | Social/content/video/design execution | Test 10 skills across LinkedIn/Instagram/X | Brand voice + factuality + approval |
| P0 | Jarvis | Cross-channel internal operator | Test isolated WhatsApp/Telegram + browser + RAG | Sandbox + RBAC + secret isolation |
| P1 | OpenClaw | Chat-based delegation layer | Evaluate against Nivy daily-ops tasks | Tool permissions + auditability |
| P1 | KairoClaw | Self-hosted messaging gateway | Compare with existing n8n channel architecture | Security + channel reliability |
| P1 | OpenSkill | Internal skill registry/governance | Index Nivy-approved external skills | Security scan + role permissions |
| P1 | OWASP Agentic Skills Top 10 | Skill security baseline | Convert risks into intake checklist | Mandatory before adoption |
| P2 | Awesome AI Agents 2026 | Discovery index | Mine remaining categories | Source/license verification |
| P2 | Claude Skills collection | Additional cross-functional skill mining | Select non-overlapping skills only | License + quality + dependency review |
| P2 | Crewm8 Social Skill Graph | Social skill specialization | Compare against Social Media Skills | Duplication and quality test |

## Integration principle

Do not install every discovered project. The target architecture should select the smallest reusable set that covers the capability map, then compose them through Nivy's orchestration layer (for example n8n/Odoo/GitHub/Notion) with explicit approval gates.

## Required intake record for every candidate

1. Official source URL.
2. Repository commit/tag or version when tested.
3. License and third-party license obligations.
4. Required credentials/secrets.
5. Network/tool permissions.
6. Inputs and outputs.
7. Human approval points.
8. Data/privacy implications.
9. Prompt-injection/tool-abuse risks.
10. Test cases and observed results.
11. Cost and infrastructure requirement.
12. Keep/adapt/reject decision with reason.
