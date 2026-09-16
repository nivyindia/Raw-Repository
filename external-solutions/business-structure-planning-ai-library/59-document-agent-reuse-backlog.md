# 59 — Document Agent Reuse Backlog

**Research date:** 2026-09-16

## P0 — reuse/test first

| Capability | First candidates | Test |
|---|---|---|
| Proposal generation | proposal-skills; ai-proposal-claude; n8n proposal workflow | Generate one Nivy Advisory proposal from a real service brief |
| RFP response | Microsoft RFP accelerator; proposal-skills | Process a sample RFP and measure requirement coverage |
| Contract generation | n8n contract workflows + office skills | Populate an approved template without changing protected clauses |
| SOW generation | proposal-skills; ai-proposal-claude | Produce SOW from approved proposal scope |
| Business PDF generation | business-document-generator | Generate branded capability statement/proposal |
| DOCX automation | codex-wps-office-mcp-skills | Create/edit/render a controlled DOCX |
| SOP authoring | strands agent-sop; sop-authoring | Convert one Nivy workflow into an executable SOP |
| Knowledge ingestion | llm-wiki; agent-knowledge | Ingest a selected Raw Repository document and preserve provenance |
| Knowledge querying | llm-wiki / Hermes LLM Wiki | Answer questions with source references |
| Documentation | technical-documentation skill | Create a runbook/onboarding guide/KB article |

## P1

- Policy drafting agent
- Employee handbook agent
- Client onboarding document agent
- Project charter/status/closure agent
- Executive report/QBR agent
- Vendor due-diligence document agent
- Finance document agent
- HR documentation agent
- Incident/postmortem agent
- Document lifecycle/version agent
- Document registry agent
- Review/expiry reminder automation

## P2

- Automated document classification
- Clause-risk detection
- Cross-document contradiction detection
- Corporate-record extraction
- Multi-language document localization
- Document-to-knowledge automatic publishing
- Knowledge-to-document evidence assembly
- Automatic supersession detection

## Reuse decision gates

### Gate 1 — output
Can the existing asset create the required DOCX/PDF/Markdown/HTML output?

### Gate 2 — control
Can we insert human approval before external/legal/financial/HR actions?

### Gate 3 — provenance
Can every material claim be traced to approved company data or source evidence?

### Gate 4 — integration
Can it connect to Nivy's CRM, GitHub/Notion knowledge, n8n and document storage?

### Gate 5 — licensing
Can the skill/workflow/template be legally reused in Nivy's intended commercial environment?

### Gate 6 — maintainability
Can we update the skill/template independently without rebuilding the entire system?

## Immediate target architecture

`Document Request → Router → Knowledge Retrieval → Specialist Skill → Template → Generator → QA → Human Approval → Export → E-sign/Publish → Register → Archive → Review`

## Research conclusion

The search found substantial reusable infrastructure. The next step is **not** to build proposal, contract, SOP or knowledge agents from scratch. First test the identified assets individually, preserve upstream provenance, and adapt only the missing Nivy-specific layer: brand, terminology, approved facts, service catalog, pricing rules, clause library, document metadata, approval policies and integrations.
