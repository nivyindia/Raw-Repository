# Department Deep-Dive Catalog — Reuse Before Build

Research date: 2026-09-16

## Purpose

This catalog converts the general discovery matrix into an execution-oriented search plan. For every department, search the internet for the complete chain:

**end-to-end system → agent team → agent → workflow → skill → prompt → SOP/process → template → framework**

Do not stop at GitHub.

## 1. Marketing

### Reusable capabilities
- Market and competitor research
- ICP/persona research
- Positioning and messaging
- Campaign planning
- Content strategy
- SEO audits and keyword research
- Content production and repurposing
- Social scheduling
- Email sequences
- Paid advertising research/creative
- Landing-page copy
- Marketing analytics/reporting
- Brand governance

### Known reusable sources
- Anthropic Knowledge Work Plugins — marketing: https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing
- Business Skills Library: https://github.com/astDeniss/business-skills
- Claude Office Skills: https://github.com/claude-office-skills/skills

## 2. Sales / RevOps

### Reusable capabilities
- ICP and account research
- Lead enrichment
- Lead scoring/triage
- Prospecting
- Personalization
- Outreach sequences
- Call preparation and summaries
- CRM updates
- Pipeline review
- Forecasting
- Proposal generation
- Deal strategy
- Renewal/expansion signals

### Known reusable sources
- Anthropic Sales Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/sales
- Business Skills Library: https://github.com/astDeniss/business-skills

## 3. Finance / Accounting

### Reusable capabilities
- Cash forecasting
- Invoice processing/chasing
- Expense organization
- Reconciliation
- Journal-entry preparation
- Month-end close
- Financial statements
- Variance analysis
- Margin/unit economics
- Budgeting
- Tax-preparation handoff
- Audit preparation

### Known reusable sources
- Anthropic Finance Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/finance
- Anthropic Small Business Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
- Claude Office Skills: https://github.com/claude-office-skills/skills

**Control:** accounting/tax outputs must have appropriate human/qualified-professional review before external use.

## 4. HR / People

### Reusable capabilities
- Recruiting pipeline
- Candidate screening support
- Interview plans/scorecards
- Offer drafting
- Onboarding
- Policy lookup
- Performance review support
- Compensation analysis
- Headcount planning
- People analytics

### Known reusable source
- Anthropic HR Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/human-resources

## 5. Operations

### Reusable capabilities
- SOP creation
- Process documentation
- Vendor management
- Capacity planning
- Change management
- Risk management
- Runbooks
- Incident/issue handling
- Quality checks
- Operational reporting

### Known reusable sources
- Anthropic Operations Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/operations
- Atlassian Team Playbook: https://www.atlassian.com/team-playbook/plays
- APQC Process Framework: https://www.apqc.org/process-frameworks

## 6. Legal / Compliance

### Reusable capabilities
- Contract review
- NDA triage
- Compliance research
- Risk identification
- Legal briefings
- Template responses
- Policy checking
- AI governance
- Privacy/IP/employment workflow support

### Known reusable source
- Claude for Legal: https://github.com/anthropics/claude-for-legal

**Control:** legal AI is an assistance layer, not a substitute for qualified legal advice.

## 7. Customer Success / Support

### Reusable capabilities
- Ticket classification
- Customer-context retrieval
- Response drafting
- Escalation packaging
- Complaint analysis
- Knowledge-base article generation
- Customer health signals
- Renewal/upsell detection

### Known reusable source
- Anthropic Customer Support Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support

## 8. Product Management

### Reusable capabilities
- Product requirements
- User research synthesis
- Roadmaps
- Competitive tracking
- Product metrics
- Stakeholder updates
- Release planning

### Known reusable source
- Anthropic Product Management Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management

## 9. Data / Analytics

### Reusable capabilities
- SQL generation
- Data exploration
- Statistical analysis
- Dashboard generation
- Data validation
- Narrative reporting

### Known reusable source
- Anthropic Data Plugin: https://github.com/anthropics/knowledge-work-plugins/tree/main/data

## 10. Executive / Company Management

### Reusable capabilities
- Weekly executive briefing
- Goal tracking
- Priority management
- Decision preparation
- Meeting preparation
- Cross-department status aggregation
- Risk and issue review
- Company knowledge retrieval

### Architecture candidates
- Anthropic Productivity Plugin
- Enterprise Search Plugin
- Small Business Plugin
- Existing Company OS projects already catalogued in files 16–17

## Priority search order

1. Revenue engine: Sales + Marketing
2. Delivery engine: Operations + Customer Success
3. Financial control: Finance + Accounting
4. People engine: HR
5. Governance: Legal + Compliance
6. Product/technology: Product + Data + Engineering
7. Executive orchestration

## Adoption principle

Use the smallest reusable unit that safely solves the task. Avoid adopting a giant platform when a skill/workflow plus existing Nivy infrastructure is sufficient.