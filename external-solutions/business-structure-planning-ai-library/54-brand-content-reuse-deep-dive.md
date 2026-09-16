# 54 — Brand Content & Creative Reuse Deep Dive

## Purpose

Move from a capability catalog to concrete reusable assets for a Brand Content & Creative Factory.

Research principle:

`DISCOVER → VERIFY → LICENSE/CHECK ACCESS → INSPECT → TEST → ADAPT → INTEGRATE`

## 1. Highest-value reusable sources discovered

| Source | Type | Reuse target | Access/license | Nivy action |
|---|---|---|---|---|
| Hugo He — ppt-master | Open-source agent/tool | Native editable PPTX from documents/topics; supports custom PPTX templates | MIT | P0 test with Nivy PPT template |
| social-media-skills/skills | Agent skill library | Brand profile, voice, strategy, posts, video, design, publishing, analytics | MIT | P0 extract relevant skills |
| scayver/marketing-skills | Marketing skill library | Copywriting, AIDA/PAS/FAB/BAB, social, image, video, sales copy | MIT | P0 mine copy/content skills |
| eigent-ai/agent-skills | Agent skill library | Copywriting, campaigns, ads, landing pages, email | Apache-2.0 | P1 inspect and compare |
| Canva Skills | Official connector skills | Canva editing, bulk create, resize, deck feedback, design workflows | Apache-2.0 | P0 test if Canva connector is available |
| Canva Design Director | Agent skill | Brand governance, presentations, social, layout, accessibility, export | License marked Other; verify before reuse | P1 inspect, do not assume MIT |
| Nebutra/generate-brand-vi | Brand-generation skill | Visual identity, asset inventory, reproducible brand-image DAGs | No license declared in repo metadata | Research only until license clarified |
| AgentsORG/DESIGN | Portable design contract | Machine-readable visual contract for agents | MIT | P0 evaluate as brand/design contract pattern |
| BuilderIO/agent-native | Agent framework + asset-generation skill | Brand-safe reusable visual assets and cross-app asset references | License not declared in repo metadata | Architecture/reference only until license clarified |
| pexoai/pexo-skills | Agent skills | Automated video generation, image/audio/video inputs, multi-shot assembly | MIT | P1 test for video pipeline |
| Adobe Express | Commercial/free tiers | Brand kits, templates, social, presentations, resize, publishing | Commercial/free tiers | P1 tool candidate |
| Microsoft PowerPoint/Copilot | Commercial | Brand-aware presentation creation/editing | Commercial | P1 enterprise PPT candidate |

## 2. Evidence notes

### PPT generation

`ppt-master` is particularly relevant because it produces native editable PowerPoint rather than slide images and explicitly supports using a user's own `.pptx` template. The upstream repository is MIT licensed and actively updated as of 2026-09-16.

Source: https://github.com/hugohe3/ppt-master

### Social/content skills

`social-media-skills/skills` provides 106 agent skills spanning brand profile, voice, audience research, content strategy, writing, image/video, Canva, publishing, engagement and analytics. The repository is MIT licensed. Its workflow explicitly makes brand profile and voice inputs foundational and uses human approval before publishing.

Source: https://github.com/social-media-skills/skills

### Marketing copy

`scayver/marketing-skills` includes copywriting using AIDA, PAS, FAB and Before/After/Bridge plus social, image, video and sales-copywriting capabilities. Repository metadata states MIT.

Source: https://github.com/scayver/marketing-skills

`eigent-ai/agent-skills` has a copywriting skill specifically covering marketing pages, campaigns, launches, ads and email sequences, including AIDA, PAS and BAB. Repository metadata states Apache-2.0.

Source: https://github.com/eigent-ai/agent-skills

### Canva / visual production

The official Canva Skills repository provides ready-to-use skills for the Canva Connector, including design editing and workflows. Repository metadata states Apache-2.0.

Source: https://github.com/canva-sdks/canva-skills

`canva-design-director` adds a design-director workflow covering brand-kit auditing, layout grids, typography, accessibility, presentations, social graphics and export. Its repository metadata marks the license as Other, so license terms must be checked before reuse.

Source: https://github.com/mavericraven/canva-design-director

### Brand-system generation

`generate-brand-vi` is a Codex-oriented skill for creating visual identity rules, image-generation DAGs, approved masters, production assets, manifests and QA. GitHub repository metadata does not declare a license, so it should be treated as a research/reference candidate until licensing is clarified.

Source: https://github.com/Nebutra/generate-brand-vi

### Portable design contract

`AgentsORG/DESIGN` defines a portable `.design` contract containing design tokens/instructions that AI agents can read and obey. Repository metadata states MIT. This is potentially useful as a machine-readable Nivy brand contract pattern.

Source: https://github.com/AgentsORG/DESIGN

### Video

`pexoai/pexo-skills` is an MIT-licensed open-source agent-skill collection for AI video production. It describes model selection, multi-shot sequencing, post-production, subtitles, music and multiple aspect ratios.

Source: https://github.com/pexoai/pexo-skills

## 3. Recommended Nivy skill stack

### Foundation

1. `brand-profile`
2. `voice-builder`
3. `audience-research`
4. `content-pillars`
5. `goals-and-kpis`
6. `design-and-templates`
7. machine-readable `.design`/brand contract

### Copy

1. Framework selector
2. Hook writer
3. Headline writer
4. Value proposition writer
5. Landing-page copy
6. Sales copy
7. Email copy
8. Social copy
9. CTA generator
10. Copy editor / fact checker

### Documents

1. Brief-to-outline
2. Company profile
3. Service catalog
4. Product catalog
5. Proposal
6. Capability statement
7. Case study
8. White paper
9. RFP response
10. Report / executive brief

### Presentation

1. Deck strategist
2. Narrative architect
3. Slide planner
4. PPT generator
5. Chart/data-slide generator
6. Speaker-notes generator
7. Brand/layout checker
8. Presentation QA
9. PPTX export validator

### Creative

1. Creative brief
2. Image prompt router
3. Brand image generator
4. Image editor
5. Infographic/data-viz
6. Carousel designer
7. Thumbnail designer
8. Cover/banner generator
9. DP/profile-image generator
10. Resize/adaptation

### Video

1. Video brief
2. Script
3. Storyboard
4. Shot planner
5. Image/video generation
6. Voice-over
7. Captions
8. Clip extraction
9. Localization/dubbing
10. Thumbnail

### Distribution

1. Platform formatter
2. Approval queue
3. Scheduler/publisher
4. Analytics
5. Content audit
6. Experimentation/A-B testing
7. Repurposing
8. Performance learning

## 4. Brand asset master checklist

### Identity

- Primary logo
- Secondary logo
- Wordmark
- Monogram
- Favicon
- App icon
- Brand pattern
- Icon system
- Color tokens
- Typography tokens
- Photography direction
- Illustration direction
- Motion direction
- Voice and tone

### Social presence

- LinkedIn company logo + banner
- Founder/profile DP + banner
- Facebook profile + cover
- Instagram profile + highlights/covers
- X profile + header
- YouTube profile + channel art + thumbnail system
- TikTok profile
- WhatsApp Business profile
- Telegram channel profile
- OG/social-share image

### Commercial assets

- Company profile
- Capability statement
- Service catalog
- Product catalog
- Brochure
- One-pager
- Sales deck
- Proposal deck
- Case study
- Media kit
- Partner kit
- RFP template
- Quote/estimate template
- SOW template
- Email signature

### Campaign assets

- Campaign key visual
- Ad variants
- Social variants
- Landing-page hero
- Email header
- Webinar/event kit
- Presentation cover
- Video cover
- Thumbnail set
- CTA variants

## 5. Master production architecture

`Brand Contract → Brief → Audience/Objective → Message Strategy → Framework Selector → Copy → Artifact Plan → Template/Layout → Generate → Brand QA → Factual QA → Accessibility/Platform QA → Human Approval → Export → Publish → Measure → Repurpose → Learn`

## 6. Nivy-specific implementation

Use one shared **Brand Content & Creative Factory** across Nivy Global and its sub-brands. The brand layer should be parameterized rather than duplicated.

Example:

`Nivy Global Brand Contract`

→ `Nivy Advisory Brand Contract`

→ `Nivy Next Brand Contract`

→ `Nivy Academy Brand Contract`

→ other approved sub-brand contracts

Each contract should define:

- brand name
- positioning
- audience
- markets
- approved claims
- prohibited claims
- logo assets
- color tokens
- typography
- spacing/grid
- imagery rules
- icon rules
- voice
- vocabulary
- CTA rules
- templates
- platform variants
- approval level

## 7. First test set

Run these before building custom infrastructure:

1. Convert an Nivy company profile into a native PPTX using `ppt-master` and the existing Nivy template.
2. Extract Nivy brand voice into the social-media-skills brand-profile/voice-builder pattern.
3. Generate one LinkedIn post, carousel and Reel script from the same source using the social skills.
4. Generate AIDA/PAS/BAB/FAB variants of one Nivy service message and compare against existing copy.
5. Produce one branded Canva social creative through the official Canva skills/connector if available.
6. Create a machine-readable Nivy design contract based on `.design` concepts.
7. Generate a company-profile one-pager and service catalog from one structured source dataset.
8. Turn one long-form research document into a full repurposing chain.
9. Run brand QA and factual QA before publication.
10. Record outputs, failures, cost, model, tool, license and human edits in the adoption tracker.

## 8. Do not build yet

Do not custom-build:

- PPT generation engine
- Generic social-copy engine
- Generic AIDA/PAS prompt library
- Generic brand-kit database
- Basic image-generation router
- Basic video-generation router
- Basic social content calendar generator

These areas already have reusable components worth testing first.

Build custom components only for gaps such as:

- Nivy-specific orchestration
- Nivy brand-contract schema if existing standards do not fit
- approval and governance rules
- cross-brand asset inheritance
- Odoo/n8n integration
- provenance/version tracking
- organization-specific QA
- unified content-to-revenue attribution

## 9. Verification / adoption states

`Discovered → Source verified → License checked → Security checked → Unchanged test → Nivy test → Brand QA → Human approval → Adapted → Integrated → Production → Measured`

## 10. Key source links

- https://github.com/hugohe3/ppt-master
- https://github.com/social-media-skills/skills
- https://github.com/scayver/marketing-skills
- https://github.com/eigent-ai/agent-skills
- https://github.com/canva-sdks/canva-skills
- https://github.com/mavericraven/canva-design-director
- https://github.com/Nebutra/generate-brand-vi
- https://github.com/AgentsORG/DESIGN
- https://github.com/BuilderIO/agent-native
- https://github.com/pexoai/pexo-skills
- https://support.microsoft.com/en-US/PowerPoint/copilot/keep-your-presentation-on-brand-with-copilot
- https://www.canva.com/business/features/brand/
- https://www.adobe.com/express/create/brand-kit

## Research date

2026-09-16