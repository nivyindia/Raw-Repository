# 58 — Knowledge, SOP & Internal Document Agent Reuse Map

**Research date:** 2026-09-16

## Agent/skill composition

| Agent | Reusable source | Job | Priority |
|---|---|---|---:|
| Document Router | claude-office-skills / Agent Skills pattern | Identify requested document and route to correct skill/template | P0 |
| Proposal Agent | proposal-skills; ai-proposal-claude | Research, structure, scope, pricing, ROI, proof, objections, SOW | P0 |
| RFP Agent | Microsoft RFP accelerator | Parse RFP, map requirements, retrieve evidence, draft response | P0 |
| Contract Agent | office skills + n8n contract workflows | Populate approved contract templates; detect missing fields | P0 |
| Document Generator | business-document-generator | Generate professional PDF business documents from templates | P0 |
| Office Artifact Agent | codex-wps-office-mcp-skills | DOCX/XLSX/PPTX creation/editing/export QA | P0 |
| SOP Author | strands agent-sop + sop-authoring skill | Turn repeatable work into deterministic SOPs | P0 |
| SOP Executor | sample-sop-mcp | Execute SOP step-by-step with outputs and auditability | P1 |
| Knowledge Ingest Agent | llm-wiki / agent-knowledge | Ingest documents into structured knowledge | P0 |
| Knowledge Query Agent | llm-wiki / Hermes LLM Wiki | Retrieve and synthesize internal knowledge | P0 |
| Knowledge Maintainer | llm-wiki | Broken links, stale information, duplicates, contradictions | P1 |
| Documentation Agent | technical-documentation skill | README, ADR, API docs, runbooks, onboarding, KB, changelog | P0 |
| Process Architect | problem-solving-systems-thinking | Map process, actors, decision points, data and risks | P1 |
| BizOps Agent | business-operations-skills | Process docs, vendors, capacity, internal comms, procurement, knowledge ops | P1 |
| PRD Agent | to-prd skill | Convert established context into structured requirements | P1 |

## Nivy internal-document agent team

### Tier 1 — shared agents

1. **Document Router**
2. **Knowledge Retrieval Agent**
3. **Template Selector**
4. **Document Generator**
5. **Document QA Agent**
6. **Approval Coordinator**
7. **Document Registry Agent**
8. **Knowledge Ingestion Agent**
9. **Knowledge Maintenance Agent**
10. **Version/Review Agent**

### Tier 2 — specialist agents

- Proposal Agent
- RFP Agent
- Contract Agent
- SOP Author
- SOP Executor
- Policy Agent
- HR Document Agent
- Finance Document Agent
- Client Onboarding Document Agent
- Project Documentation Agent
- Technical Documentation Agent
- Executive Reporting Agent
- Vendor/Partner Document Agent

## Knowledge architecture

Use reusable patterns from llm-wiki, agent-knowledge and Hermes LLM Wiki rather than designing a new knowledge mechanism from zero. These systems demonstrate ingest/query/maintenance skills and progressive disclosure of large knowledge sources. citeturn1search3turn1search8turn1search13

Recommended flow:

`Source → Ingest → Classify → Metadata → Link → Index → Query → Synthesize → Cite Source → Feedback → Maintain`

## SOP architecture

Use the Agent SOP approach where an SOP is an executable, parameterized workflow rather than merely a passive document. The Strands Agent SOP project explicitly supports converting SOPs into standard Agent Skills and progressive disclosure. citeturn1search0turn1search14

Recommended SOP structure:

`Purpose → Trigger → Preconditions → Inputs → Steps → Decision Rules → Required Outputs → QA → Approval → Exceptions → Escalation → Evidence → Completion → Review`

## Important distinction

- **Policy** = what is allowed/required.
- **Process** = how the organization works end-to-end.
- **SOP** = repeatable operational procedure.
- **Work instruction** = detailed task execution.
- **Skill** = agent instruction package.
- **Workflow** = executable automation/orchestration.
- **Template** = reusable output structure.
- **Record** = evidence that the activity happened.

The AI system should connect all seven instead of generating isolated documents.
