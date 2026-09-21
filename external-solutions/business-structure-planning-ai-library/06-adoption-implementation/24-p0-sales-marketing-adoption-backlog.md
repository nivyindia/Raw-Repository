# P0 Sales + Marketing Adoption Backlog

Research date: 2026-09-16

## Objective

REUSE -> ADAPT -> INTEGRATE -> BUILD ONLY WHAT IS MISSING.

This backlog converts discovered assets into testable adoption units.

| Priority | Capability | Candidate source | First action | Integration target | Acceptance evidence |
|---|---|---|---|---|---|
| P0 | ICP builder | Agentic Sales | Extract/adapt skill | Company knowledge | ICP document + validation checklist |
| P0 | Account research | Anthropic Sales / Agentic Sales | Adapt | Web search + CRM | Repeatable account brief |
| P0 | Lead scoring | Agentic Sales / n8n | Test | CRM/Sheets | Score + reason + routing |
| P0 | Lead generation | n8n | Test | Form + enrichment + CRM | Qualified lead record |
| P0 | Personalized outreach | Anthropic Sales / n8n | Adapt | Gmail/CRM | Approved draft + logging |
| P0 | Follow-up sequence | Agentic Sales / n8n | Test | CRM + email | State-based follow-up |
| P0 | Discovery prep | Anthropic Sales / Agentic Sales | Adapt | Calendar + CRM + web | Meeting brief |
| P0 | Call debrief | Anthropic Sales | Adapt | Transcript + CRM | Actions + next step |
| P0 | Pipeline review | Anthropic Sales | Adapt | CRM | Weekly review artifact |
| P0 | Sales forecast | Anthropic Sales / Agentic Sales | Adapt | CRM | Forecast with evidence |
| P0 | Content strategy | Anthropic Marketing / Small Business | Adapt | Sales/CRM + knowledge | 30-day brief |
| P0 | Campaign planning | Anthropic Marketing | Adapt | Calendar + content system | Campaign brief + KPI model |
| P0 | Content production | Anthropic Marketing | Adapt | Brand knowledge | Draft + quality gate |
| P0 | SEO audit | Anthropic Marketing | Test | Website + search data | Audit + prioritized fixes |
| P0 | Email sequences | Anthropic Marketing | Adapt | CRM/email | Sequence + approval gate |
| P0 | Competitive intelligence | Anthropic Sales/Marketing | Adapt | Web + knowledge | Competitor brief |
| P0 | Campaign performance | Anthropic Marketing | Adapt | Analytics | KPI report + actions |

## Adoption gates

### Gate 1 — Source validation
Confirm source exists, current location, license/access and whether the asset is executable.

### Gate 2 — Functional test
Run the original or minimally adapted workflow on synthetic/non-sensitive test data.

### Gate 3 — Nivy adaptation
Add Nivy terminology, ICP, services, brand rules, approval gates and output schemas.

### Gate 4 — Integration
Connect CRM, email, web research, calendar, analytics and automation only after the workflow works standalone.

### Gate 5 — Controlled production
Use small volume, human approval and complete logging.

### Gate 6 — Promotion
Only proven assets move from the Raw Repository into the canonical Company OS / department implementation.

## Do not automate yet

- unrestricted bulk outbound
- autonomous claims about services/pricing
- autonomous contract/legal commitments
- unsupervised publication
- actions that change CRM/account records without auditability
- any workflow requiring credentials or sensitive customer data until security controls exist
