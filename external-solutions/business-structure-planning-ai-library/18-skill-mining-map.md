# Skill Mining Map — Reusable Department AI Assets

Research date: 2026-09-16

## Objective

Do not recreate department agents from scratch. Mine existing skill/command/plugin repositories and extract reusable atomic capabilities.

## Primary source: Anthropic Knowledge Work Plugins

Official repository: https://github.com/anthropics/knowledge-work-plugins

The repository packages specialist work as skills, connectors, slash commands and sub-agents. It currently exposes plugins for productivity, sales, customer support, product management, marketing, legal, finance, data, enterprise search, bio-research, small business and plugin management.

### Department extraction map

| Department | Existing asset family | Reuse target for Nivy |
|---|---|---|
| Executive / Productivity | productivity | Daily planning, task management, meetings, commitments |
| Sales / RevOps | sales | Prospect research, call prep, outreach, pipeline, forecasting, deal review |
| Marketing | marketing | Content, campaigns, brand voice, competitive research, SEO, reporting |
| Customer Success | customer-support | Ticket triage, response drafting, escalation, customer research, KB creation |
| Product | product-management | PRDs, roadmaps, user research, competitive tracking, stakeholder updates |
| Finance / Accounting | finance | Journal entries, reconciliation, statements, variance analysis, close, audit prep |
| Data / Analytics | data | SQL, exploration, statistics, dashboards, validation |
| Legal / Compliance | legal | Contract review, NDA triage, compliance, risk, legal research |
| HR / People | human-resources | Recruiting, onboarding, reviews, policy lookup, compensation, people analytics |
| Small-business orchestration | small-business | Cross-functional cash, sales, marketing, customer and operations workflows |
| Knowledge | enterprise-search | Cross-system knowledge retrieval |

## Secondary skill library

### Claude-Skills

https://github.com/borghei/Claude-Skills

Reference describes 368 skills across 20 domains, with each skill packaged with SKILL.md documentation, scripts, references and assets.

**Mining rule:** copy the concept and structure only where the license permits; otherwise retain the source link and create an adapted Nivy implementation.

### Business Skills Library

https://github.com/astDeniss/business-skills

Advertises 69 operational skills spanning sales, marketing, SEO, paid ads, analytics, social, content, video, email, customer success, operations, product, hiring and PR.

### Claude Office Skills

https://github.com/claude-office-skills/skills

Useful atomic examples include lead research, lead qualification, content writing, brand guidelines, invoice organization, proposal writing, email classification, meeting notes, weekly reporting and data analysis.

## Nivy extraction schema

Every mined skill should become a record with:

- `skill_id`
- `source`
- `source_url`
- `department`
- `capability`
- `task`
- `trigger`
- `required_inputs`
- `process_steps`
- `output`
- `quality_checks`
- `human_approval`
- `connectors`
- `permissions`
- `data_sensitivity`
- `license`
- `reuse_mode`: direct / adapt / study
- `nivy_destination`
- `test_status`

## Important rule

A skill is an atomic reusable capability, not a complete autonomous department. Combine skills with routing, knowledge, connectors, policies, approvals, logging and KPIs to create an agent/workflow.