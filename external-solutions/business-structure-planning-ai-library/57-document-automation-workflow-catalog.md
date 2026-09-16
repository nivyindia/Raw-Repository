# 57 — Document Automation Workflow Catalog

**Research date:** 2026-09-16

## Reusable workflow patterns found

| Workflow | Existing asset | Trigger | Main automation | Nivy adaptation |
|---|---|---|---|---|
| Proposal factory | n8n proposal template | CRM/Sheet new client | Normalize → AI proposal → Google Doc → PDF → email → e-sign → log → Slack | Odoo/CRM → Nivy proposal template → approval → e-sign |
| Contract factory | n8n contract template | Form/webhook | Validate fields → fill contract → PDF → email | Intake form → approved contract template → legal review → e-sign |
| AI contract lifecycle | n8n AI contract template | Contract request | AI draft → formatted document → e-sign → wait → completion notification | Add clause library + approval gate + contract register |
| RFP response | Microsoft RFP accelerator | RFP email | Retrieve knowledge → analyze requirements → draft proposal → compliance/security → confidence → review | GitHub/Notion knowledge base + Nivy service library + human bid approval |
| Client onboarding | n8n onboarding workflow | Intake form | Normalize client data → create project → contract → email → internal channel → log | Odoo + n8n + document templates + onboarding checklist |
| Employee onboarding | ai-employee-onboarding | New-hire form | Claude plan → welcome emails → sheet log | HRIS/CRM + offer/e-sign + onboarding knowledge |
| SOP execution | AWS sample-sop-mcp | Agent task | Load SOP → execute step → require expected output → advance → audit | Use for internal low-risk procedures with approval gates |
| Knowledge ingestion | llm-wiki / agent-knowledge | New document/source | Extract → classify → create/update pages → link → maintain | Raw Repository → canonical Company OS knowledge layer |
| Documentation generation | technical-documentation skill | Documentation request | Select doc type → generate → audit → maintain | Company docs + technical docs + agent context |
| Office artifact pipeline | codex-wps-office-mcp-skills | Document request | Create/edit → render/export → QA → final artifact | DOCX/XLSX/PPTX generation with visual/export QA |

## Universal document workflow

`INTAKE → CLASSIFY → RETRIEVE SOURCES → SELECT SKILL → SELECT TEMPLATE → GENERATE → VALIDATE → HUMAN APPROVAL → EXPORT → SIGN/PUBLISH → REGISTER → ARCHIVE → REVIEW`

## Reusable automation modules

### 1. Intake
- Webhook/form/email trigger
- CRM event
- Manual command
- RFP attachment ingestion

### 2. Context assembly
- Client profile
- Company facts
- Approved claims
- Pricing
- Service catalog
- Clause library
- Past documents
- Case studies
- Policies

### 3. Generation
- Skill router
- Prompt/framework selection
- Template filling
- DOCX/PDF/PPTX generation

### 4. QA
- Required-section check
- Source/evidence check
- Numerical consistency
- Brand check
- Legal/compliance escalation
- Duplicate/stale clause check
- Rendering/format check

### 5. Approval
- AI draft
- Internal reviewer
- Legal/finance/security reviewer where needed
- Final human approval

### 6. Execution
- Email
- E-signature
- CRM update
- Project creation
- Invoice/PO trigger
- Knowledge-base publication

### 7. Lifecycle
- Version
- Effective date
- Review reminder
- Renewal/expiry reminder
- Supersession
- Archive

## Best Nivy composition

`Odoo/CRM + n8n + GitHub/Notion Knowledge + Agent Skills + DOCX/PDF generation + e-signature + approval queue + document register`.

Do not build this as one giant agent. Keep document generation, retrieval, QA, approval and execution as separable modules.
