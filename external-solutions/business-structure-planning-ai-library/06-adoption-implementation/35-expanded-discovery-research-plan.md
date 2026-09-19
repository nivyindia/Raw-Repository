# Expanded Discovery Research Plan

## Objective
Research the internet for reusable assets across the full international-company capability catalog in `34-expanded-international-company-capability-catalog.md`.

The target is not merely a list of SaaS products. The research must find reusable **systems, agents, skills, prompts, automations, connectors, plugins, APIs, SOPs, templates, playbooks and complete workflows**.

## Research layers

### Layer A — Complete systems
Find:
- CRM/RevOps systems
- Marketing automation systems
- Social media management systems
- Content operating systems
- Customer support systems
- Project/operations systems
- HR systems
- Finance systems
- Website/ecommerce systems
- AI operating systems
- Agency operating systems

### Layer B — Specialist applications
Find tools for:
- SEO
- PPC
- social publishing
- social listening
- competitor intelligence
- email marketing
- lead enrichment
- outreach
- website analytics
- CRO
- design
- video
- audio
- image generation
- WordPress
- WooCommerce
- Shopify
- CRM
- customer success
- document automation

### Layer C — AI reusable components
Find:
- agents
- agent teams
- skills
- `SKILL.md` libraries
- Claude plugins
- custom assistants/GPTs
- prompt libraries
- MCP servers
- agent frameworks
- tool-use examples
- evaluation frameworks
- guardrail frameworks

### Layer D — Automation
Find:
- n8n workflows
- Zapier workflows
- Make scenarios
- Pipedream workflows
- GitHub Actions
- webhooks
- API recipes
- browser automation
- RPA
- scheduled jobs
- approval workflows

### Layer E — Production assets
Find:
- SOPs
- checklists
- templates
- scripts
- playbooks
- operating procedures
- campaign calendars
- content calendars
- proposal templates
- offer-letter templates
- onboarding packs
- reporting templates
- QA checklists
- brand guidelines
- design systems

## Platform-specific research

### Social
Research separately for:
- Instagram
- Facebook
- LinkedIn
- X
- YouTube
- TikTok
- Pinterest
- Reddit
- Telegram
- WhatsApp

For each platform find strategy, content creation, scheduling, analytics, engagement, listening, lead capture, automation and repurposing.

### Web
Research separately for:
- WordPress
- WooCommerce
- Shopify
- Webflow
- Framer
- Wix where relevant
- custom React/Next.js
- headless CMS
- static sites

Find design, development, SEO, content, deployment, QA, monitoring, security, maintenance and AI automation assets.

### Creative
Research separately for:
- image generation
- image editing
- graphic design
- presentations
- video generation
- video editing
- avatar/video presenters
- voice generation
- audio editing
- transcription
- subtitles
- dubbing
- thumbnails
- motion graphics

## Research sequence

1. Official/open-source sources first.
2. GitHub repositories and maintained skill libraries.
3. Official vendor marketplaces and integration directories.
4. n8n/Zapier/Make workflow libraries.
5. AI agent/skill marketplaces.
6. Community resources and curated lists.
7. Commercial tools and paid systems.
8. Tutorials only when they contain reusable implementation knowledge.

## Required record
Every asset must be recorded using:

| Field | Required |
|---|---|
| Asset ID | Yes |
| Capability | Yes |
| Department | Yes |
| Platform/channel | If applicable |
| Asset type | Yes |
| Name | Yes |
| Publisher | Yes |
| Official URL | Yes |
| Repository URL | If applicable |
| License/access | Yes |
| Cost model | Yes |
| Open-source | Yes/No |
| Integrations | Yes |
| API/MCP | If applicable |
| AI capability | Yes/No |
| Automation capability | Yes/No |
| Human approval | Yes |
| Data sensitivity | Yes |
| Maintenance signal | Yes |
| Nivy reuse mode | Yes |
| Nivy destination | Yes |
| Test status | Yes |

## Reuse classification

`R0` — Reference only

`R1` — Copy/adapt prompt, template, SOP or methodology

`R2` — Install/use existing skill/plugin/workflow

`R3` — Integrate external application/API

`R4` — Compose multiple existing assets into Nivy workflow

`R5` — Custom-build only missing/differentiating component

## Important discovery rule
Do not conclude "nothing exists" because a full product was not found. Search down the stack:

**System → Application → Agent → Skill → Prompt → Workflow → Connector/API → SOP → Template → Framework**

A missing complete system may still have enough reusable components to avoid custom development.

## Quality filters
Prefer assets with:
- inspectable implementation
- official source
- clear license/access terms
- active maintenance
- meaningful documentation
- reproducible setup
- stable APIs/integrations
- security controls
- human approval where appropriate
- useful testability

Do not adopt solely because an asset is popular.

## Nivy implementation target
The final research should enable a modular company architecture:

`Company Router`
→ `Department Router`
→ `Specialist Agent/Skill`
→ `Workflow`
→ `Connector/API`
→ `Knowledge/Data`
→ `Approval Gate`
→ `Execution`
→ `Audit/Logging`
→ `System of Record`

## Research completion condition
A capability is considered sufficiently researched only when the research team has checked all applicable asset layers and documented either:

1. reusable candidates,
2. why candidates were rejected,
3. or why a custom component is genuinely required.

## Special instruction for creative and publishing workflows
Do not automate unrestricted publishing merely because technically possible. Establish draft → QA → approval → publish stages, brand controls, rights/licensing checks, and platform-specific constraints.
