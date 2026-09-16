# 56 — Document & Business Skill Source Catalog

**Research date:** 2026-09-16

## Purpose

Find existing AI agents, Agent Skills, SOP skills, document generators, workflows and MCP/tooling that can be reused to create Nivy's official and internal company documents.

Core rule: `DISCOVER → VERIFY → LICENSE/CHECK ACCESS → TEST → REUSE → ADAPT → INTEGRATE`.

## High-value sources

| Source | Type | Reusable capability | Access/license status | Nivy use |
|---|---|---|---|---|
| claude-office-skills/skills | Claude Skills | Contracts, NDA, proposals, HR docs, offer letters, invoices, reports, office workflows | GitHub; verify individual skill licenses | P0 document skill library |
| peterbamuhigire/proposal-skills | Agent Skills / proposal engine | Proposals, tenders, EOI, methodology, workplan, M&E, risk, pricing, proposal QA; 109 active SKILL.md entrypoints reported | Open source repo; verify license before production | P0 proposal/RFP engine |
| zubair-trabzada/ai-proposal-claude | Claude Code proposal system | Prospect research, pricing, ROI, scope, objections, case studies, follow-up, SOW, PDF proposal; 14 skills / 5 agents | GitHub; verify license | P0 sales proposal reuse candidate |
| microsoft/agent-for-rfp-response-solution-accelerator | RFP agent reference | RFP intake, knowledge retrieval, proposal drafting, compliance/security, confidence, human review | Microsoft accelerator; licensing/dependencies must be checked | P0 RFP architecture reference |
| n8n proposal workflow | n8n workflow | CRM/Sheets → AI proposal → Google Doc → PDF → email → e-signature → logging → Slack | Free workflow template; dependent services may be paid | P0 automation candidate |
| n8n contract workflow | n8n workflow | Form → contract template → PDF → email | Free workflow template; dependencies may be paid | P0 contract automation |
| n8n AI contract lifecycle | n8n workflow | Contract request → AI generation → HTML → e-signature → completion tracking | Free workflow template; verify provider terms | P0 contract lifecycle |
| business-document-generator | Agent Skill | Proposal/business plan/budget generation from templates; PDF + Python generation | GitHub skill; verify license | P0 generic document generator |
| strands-agents/agent-sop | Agent SOP framework | Portable SOPs, progress/resumability, SOP-to-SKILL conversion, authoring skill | Open source; verify current license | P0 SOP factory |
| aws-samples/sample-sop-mcp | MCP/reference architecture | Agent executes auditable SOP steps one at a time with human intervention | AWS sample; verify license | P1 SOP execution/control |
| TheBushidoCollective/han sop-authoring | Agent Skill | Writing deterministic, actionable SOPs for agents | GitHub; verify license | P0 SOP authoring |
| JPeetz/agent-skills technical-documentation | Agent Skill | README, ADR, API docs, runbooks, onboarding, changelog, knowledge base, docs audit, agent context | Repo license should be checked | P0 internal documentation |
| arronKler/llm-wiki | Agent-native knowledge system | Ingest, query, maintain, configure; linked Markdown KB; static export | GitHub; verify license | P0 knowledge base |
| jackwener/llm-wiki | Agent-native persistent KB | Ingest/query/lint/research skills, CLAUDE.md + AGENTS.md bootstrap, compounding knowledge | GitHub; verify license | P0 knowledge operations |
| keshrath/agent-knowledge | Knowledge-ingest Skill | Bootstrap/update knowledge base from source material | GitHub; verify license | P1 ingestion |
| Hermes LLM Wiki skill | Bundled Agent Skill | Build/query interlinked Markdown knowledge base | MIT per current docs | P1 portable KB option |
| alirezarezvani/claude-skills business-operations | Agent Skill router | Process mapping, vendor management, capacity, internal comms, knowledge ops, procurement | MIT stated | P1 internal operations |
| Xiangdong-415/codex-wps-office-mcp-skills | Codex skills + MCP workflow | DOCX, XLSX, PPTX, export QA, WPS/Word MCP workflows | MIT stated | P0 office artifact layer |
| matt-riley/agent-skills to-prd | Agent Skill | PRD synthesis, user stories, implementation/testing decisions, issue handoff | GPLv3 stated | P1 product/requirements docs |
| bybaochaule/problem-solving-systems-thinking | Agent Skill | Process decomposition, workflow mapping, decision trees, SOP/agent-flow design | Verify license | P1 process design |

## Document families to map onto these reusable assets

1. Proposal
2. SOW
3. MSA / service agreement
4. NDA
5. RFP/RFQ/tender response
6. Capability statement
7. Service catalog
8. Pricing/rate card
9. Client onboarding pack
10. Project charter
11. PRD/specification
12. SOP
13. Work instruction
14. Runbook
15. Policy
16. Employee handbook
17. Internal communication
18. Meeting agenda/minutes/decision record
19. Executive report/QBR
20. Knowledge-base article
21. Training guide
22. Incident/postmortem
23. Risk/compliance record
24. Vendor/partner documentation
25. HR documentation
26. Finance documentation
27. Technical documentation

## Reuse architecture

`Brief/Form → Document Router → Skill → Knowledge/RAG → Template → Generate → Factual/Legal/Brand QA → Human Approval → DOCX/PDF → E-sign/Publish → CRM/Knowledge Archive → Version/Review Reminder`

## Critical controls

- Never treat an AI-generated legal contract, tax document, HR decision, compliance statement or regulated document as final without appropriate human review.
- Keep source evidence and approved clauses separate from generated prose.
- Track template version and approval status.
- Preserve editable source files as well as final PDFs.
- Add document IDs, owners, effective/review dates and supersession metadata.
- Check licenses before copying skills or templates into proprietary production systems.
