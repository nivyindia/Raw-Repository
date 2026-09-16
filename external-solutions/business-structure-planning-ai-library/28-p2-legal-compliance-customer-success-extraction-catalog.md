# P2 Legal, Compliance & Customer Success — Reusable Solution Extraction Catalog

**Status:** Research catalog / reuse-first
**Date:** 2026-09-16
**Purpose:** Identify existing reusable agents, skills, workflows, connectors and operating patterns before building Nivy-specific components.

## 1. Legal & Compliance

### Primary reusable source: Anthropic Claude for Legal
Official source: https://github.com/anthropics/claude-for-legal

The repository provides reference plugins, skills, managed-agent cookbooks and MCP connectors for commercial, privacy, corporate, employment, litigation, regulatory, AI governance and IP workflows. It includes scheduled/event-driven patterns such as renewal watching, regulatory monitoring, diligence grids and launch monitoring. Outputs are explicitly designed for attorney review. 

| Capability | Reuse candidate | Nivy use | Control |
|---|---|---|---|
| Contract review | Vendor agreement reviewer | Vendor/client MSA/NDA first-pass review | Lawyer/authorized reviewer |
| NDA triage | NDA triager | Route routine vs complex NDAs | Human escalation |
| Contract history | Amendment tracing | Maintain agreement change history | Source-document verification |
| Renewal monitoring | Renewal watcher | Contract renewal/cancel-by reminders | No autonomous termination |
| Privacy | DSAR/privacy workflows | Privacy request intake and drafting | Jurisdiction/legal review |
| Regulatory monitoring | Regulation feed monitor | Track relevant markets and AI rules | Verify against primary sources |
| AI governance | AI inventory / use-case triage / impact assessment | Maintain Nivy AI system register | Legal/compliance approval |
| Corporate legal | Corporate workflow skills | Entity/governance document support | Counsel review |
| Employment legal | Employment workflow skills | Employment document triage | Counsel/HR approval |
| IP | IP workflow skills | IP intake and research support | Counsel review |

### Connector pattern
Useful connector classes include document management, CLM, e-signature, research databases, collaboration, and project tracking. The official connector documentation emphasizes read-heavy access, provenance in results, and explicit confirmation for write actions. https://github.com/anthropics/claude-for-legal/blob/main/CONNECTORS.md

### Security/reuse rule
Do not treat legal skills as legal advice. Keep source provenance, jurisdiction, retrieval date, confidence/verification status, approval owner, and irreversible-action gates. Community skills should pass publisher/license/connector/security checks before installation.

## 2. Customer Success / Support

### Primary reusable source: Anthropic Knowledge Work Plugins — customer-support
Official source: https://github.com/anthropics/knowledge-work-plugins

The customer-support plugin is described as supporting ticket triage, response drafting, escalation packaging, customer-context research, and conversion of resolved issues into knowledge-base articles. Connectors listed by the official repository include Slack, Intercom, HubSpot, Guru, Jira, Notion and Microsoft 365. 

| Capability | Reuse candidate | Nivy use | Human gate |
|---|---|---|---|
| Ticket triage | Support classifier/router | Route client requests by priority/type | Escalation for critical cases |
| Customer context | Account/context researcher | Assemble CRM + prior interaction context | Data-access controls |
| Response drafting | Support response writer | Draft email/chat responses | Approval for sensitive/high-value cases |
| Escalation | Escalation package | Give delivery team structured issue brief | Manager ownership |
| Knowledge capture | Resolution-to-KB | Convert solved issues into reusable SOP/FAQ | QA before publication |
| Issue tracking | Ticket/project handoff | Link support cases to delivery work | Controlled write access |

## 3. Adoption schema

For each candidate capture: `source`, `source_url`, `capability`, `inputs`, `outputs`, `connectors`, `permissions`, `data_sensitivity`, `license`, `human_approval`, `test_status`, `nivy_destination`, `adaptation_notes`.

## 4. Reuse decision

**Reuse unchanged** when it fits and license/permissions allow.

**Adapt** when the workflow is sound but terminology, approval gates, integrations, jurisdiction or output schema differs.

**Compose** multiple skills when the source provides atomic capabilities but Nivy needs an end-to-end workflow.

**Build only missing pieces** when no adequate reusable asset exists or integration/control/reliability requirements cannot be met.

## 5. High-priority P2 candidates

1. Contract/NDA intake and triage
2. Contract renewal watcher
3. AI governance inventory and use-case triage
4. Regulatory monitoring
5. Customer ticket triage
6. Customer-context briefing
7. Escalation package generation
8. Resolution-to-knowledge-base workflow

## Sources
- Anthropic, Claude for Legal: https://github.com/anthropics/claude-for-legal
- Anthropic, Claude for Legal connectors: https://github.com/anthropics/claude-for-legal/blob/main/CONNECTORS.md
- Anthropic, Knowledge Work Plugins: https://github.com/anthropics/knowledge-work-plugins
