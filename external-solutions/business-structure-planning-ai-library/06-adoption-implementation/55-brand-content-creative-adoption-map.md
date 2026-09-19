# 55 — Brand Content & Creative Adoption Map

## Purpose

Convert the brand/content discovery work into a practical reuse-first implementation map for the Nivy Content & Creative Factory.

## 1. P0 candidates

| Capability | Existing reusable solution | Reuse mode | Nivy action |
|---|---|---|---|
| AI design/artifact factory | AICAE/Open Design | Open source, Apache-2.0; bundled skills retain upstream licenses | Evaluate locally; use as a common design/artifact layer |
| PPT generation | Presenton Skills | Open-source agent skill; PPTX/PDF/PNG | Test as presentation adapter |
| PPT agent | PPTAgent | Open source; research/production candidate | Benchmark against Presenton |
| Multi-agent PPT QA | ppt-agent-skills | Skill package; license verify before production | Test visual QA/state-machine approach |
| Brand design systems | Open Design DESIGN.md pattern | Portable Markdown design systems | Create Nivy DESIGN.md contract |
| Social content | social-media-skills | Open source | Reuse platform-specific skills |
| Marketing content | marketing-skills | Open source | Reuse strategy/copy/growth skills |
| Automation | n8n | Open source/self-hosted | Orchestrate briefs, generation, approval, publishing |

## 2. P1 candidates

- Video generation/editing skills
- Image-generation and image-editing skills
- Document/catalog generation
- SEO/GEO/AEO content production
- Newsletter/email production
- Repurposing pipelines
- Localization/multilingual adaptation
- Social scheduling/publishing adapters
- Analytics/performance-learning workflows

## 3. Brand Contract

Every artifact should load a machine-readable brand contract before generation:

`brand_id`
`brand_family`
`logo_rules`
`color_tokens`
`font_tokens`
`spacing_tokens`
`imagery_rules`
`icon_rules`
`layout_rules`
`voice`
`approved_claims`
`prohibited_claims`
`terminology`
`CTA_rules`
`market_rules`
`platform_rules`
`approval_level`

The contract should be versioned in GitHub and inherited by sub-brands with explicit overrides.

## 4. Universal artifact pipeline

`Brief → Audience → Objective → Source facts → Message framework → Copy → Brand contract → Template/skill → Generate → Render → Visual QA → Factual QA → Compliance QA → Human approval → Export → Publish → Archive → Repurpose → Measure`

## 5. Artifact matrix

| Input | Primary outputs | Secondary outputs |
|---|---|---|
| Research | Report, executive brief | LinkedIn, carousel, infographic, newsletter |
| Service brief | Service catalog, sales deck | Landing page, social posts, proposal sections |
| Case study | Case-study PDF/deck | Social proof, website section, sales email |
| Webinar | Deck + recording | Clips, article, newsletter, FAQ, social |
| Product launch | Launch deck + creative | Ads, social, email, website, press material |
| Job opening | JD/career creative | LinkedIn, social, community post |
| Customer FAQ | Help document | Chatbot knowledge, social FAQ, support macros |

## 6. Required QA gates

### Visual
- Correct logo and clear space
- Correct colors and typography
- Consistent spacing/layout
- Appropriate image licensing/provenance
- Correct aspect ratio
- No clipping/overlap

### Content
- Source facts verified
- Claims supported
- Correct audience and market
- Clear CTA
- No accidental contradictions
- No unsupported statistics

### Commercial/risk
- Pricing verified
- Offer terms verified
- Regulatory/sensitive claims reviewed
- External publication requires approval where configured

## 7. Nivy architecture

`Brand Repository → Content Brief DB → Strategy/Framework Router → Agent Skills → Artifact Generator → Render/QA → Approval Queue → n8n → Channel APIs → Analytics → Learning Store`

### Shared agents

1. Brand Guardian
2. Content Strategist
3. Framework Router
4. Copywriter
5. Presentation Generator
6. Document Generator
7. Social Producer
8. Visual Producer
9. Video Producer
10. Repurposing Agent
11. Localization Agent
12. QA Agent
13. Publishing Agent
14. Analytics/Learning Agent

## 8. Decision rule

Reuse an existing asset when it meets the required output, license/access conditions, security requirements and integration constraints. Adapt it when only the brand/process layer differs. Build custom code only where the missing requirement is material and no suitable reusable component exists.

## 9. Research sources

- Open Design: https://github.com/AICAE/opendesign
- Presenton Skills: https://presenton.ai/skills/presenton
- PPTAgent: https://github.com/icip-cas/PPTAgent
- PPT Agent Skills: https://github.com/sunbigfly/ppt-agent-skills
- Social Media Skills: https://github.com/social-media-skills/skills
- Marketing Skills: https://github.com/scayver/marketing-skills
- n8n Skills: https://github.com/n8n-io/skills

## Status

Discovery sources verified on 2026-09-16. License/access must be rechecked before production adoption; bundled/upstream components may carry separate licenses.