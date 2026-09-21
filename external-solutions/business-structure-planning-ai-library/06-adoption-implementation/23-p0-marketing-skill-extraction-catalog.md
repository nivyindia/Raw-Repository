# P0 Marketing Skill Extraction Catalog

Research date: 2026-09-16

## Primary reusable sources

| Source | Asset | Reuse action | Notes |
|---|---|---|---|
| Anthropic Marketing Plugin | Campaign/content/brand/competitive/analytics/SEO/email workflows | ADAPT | Includes `/draft-content`, `/campaign-plan`, `/brand-review`, `/competitive-brief`, `/performance-report`, `/seo-audit`, `/email-sequence`. https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing |
| Anthropic Small Business | `content-strategy`, `canva-creator`, campaign workflow | TEST / ADAPT | Demonstrates chaining finance/sales data into content planning and campaign execution with approval gates. https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business |
| Marketing Skills OS | 76 marketing skills + integrations/templates/workflows | TEST / ADAPT | Open-source marketing operating layer for agent-compatible tools. https://github.com/scayver/marketing-skills |
| AI Marketing Skills | Growth experiments, sales pipeline, content ops, outbound, SEO, finance automation | TEST / ADAPT | Complete workflows rather than isolated prompts. https://github.com/ericosiu/ai-marketing-skills |
| n8n lead-generation workflow | Lead discovery + enrichment + cold email | TEST / ADAPT | Business type/location input, data extraction, AI email generation and Gmail delivery. https://n8n.io/workflows/7423-lead-generation-agent/ |
| n8n AI SDR | Automated sales/marketing lifecycle | TEST / ADAPT | Useful bridge between marketing demand generation and sales execution. https://n8n.io/workflows/13529-run-an-ai-sdr-sales-pipeline-with-openai-google-sheets-gmail-and-calendar/ |

## Nivy extraction targets

### Strategy
- market research
- ICP/segment definition
- positioning
- messaging architecture
- offer design
- channel strategy
- campaign planning

### Content
- content strategy
- editorial calendar
- blog/article creation
- landing pages
- social content
- email/newsletters
- case studies
- sales enablement assets

### SEO
- technical audit
- keyword research
- competitor/content-gap analysis
- on-page optimization
- internal linking
- content briefs
- reporting

### Demand generation
- lead magnets
- outbound campaigns
- nurture sequences
- retargeting briefs
- campaign experiments
- conversion optimization

### Brand
- brand voice
- messaging consistency
- asset review
- competitive positioning
- terminology governance

### Analytics
- channel KPIs
- attribution
- campaign performance
- experiment tracking
- weekly/monthly reporting

## End-to-end campaign pattern

Research -> objective -> audience -> offer -> channel plan -> content brief -> asset creation -> approval -> publishing/activation -> measurement -> optimization -> knowledge capture.

The approval gate should remain explicit before external publication or outbound communication.

## Nivy implementation rule

Reuse external methodology and workflow structure, but maintain a single Nivy source of truth for brand voice, ICP, offers, claims, approved channels, legal/compliance constraints and measurement definitions.
