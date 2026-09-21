# Sales Data Acquisition & Multi-Channel Prospecting Catalog

**Status:** v1.0 — 2026-09-16

## Purpose

This closes a specific gap in the sales library: **how leads are actually discovered and collected from many source types and channels**, before enrichment, qualification and outreach.

Core model:

`ICP → Source Selection → Discovery → Extraction → Normalization → Deduplication → Enrichment → Verification → Intent/Signal Detection → Scoring → CRM → Outreach`

This is intentionally broader than a single "lead scraper". Different sources require different acquisition methods, permissions, rate limits, schemas and fallbacks.

## Source / channel coverage

| Source family | Examples | Acquisition method | Reusable assets/candidates | Typical data | Priority |
|---|---|---|---|---|---:|
| Search engines | Google, Bing, DuckDuckGo | Search API / crawler / browser | Crawl4AI MCP, Apify skills | companies, pages, contacts, signals | P0 |
| Company websites | Any public website | HTTP crawl, browser, sitemap, structured extraction | Crawl4AI, Firecrawl-style MCP, Apify | company profile, services, contact pages, tech signals | P0 |
| LinkedIn | People/company/job data | Official/API where available; permitted data providers; browser workflows only where allowed | Apollo MCP, Apify actors, lead-gen workflows | people, roles, companies, jobs | P0 |
| Google Maps / local business | Maps/Places | API/provider/scraper | Apify Google Maps actors, lead-gen workflows | business, phone, website, category, location, reviews | P0 |
| Instagram | Profiles/content | API/provider/scraper where permitted | Apify skills/actors, multi-source n8n workflow | profiles, followers, content, signals | P1 |
| Facebook / Meta | Pages, advertisers | Meta APIs / permitted data providers | Apify skills, Meta Ads Library workflows | pages, advertisers, ads, signals | P1 |
| X/Twitter | Profiles/posts | API/search/provider | Lead Research Agent, Apify skills | people, posts, conversations, signals | P1 |
| Reddit | Communities/posts | API/search/provider | Lead Research Agent, Apify skills | discussions, pain points, intent | P1 |
| YouTube | Channels/videos | API/provider | Apify skills, multi-source lead-gen workflow | creators, channels, videos, topics | P1 |
| GitHub | Organizations/repos/activity | GitHub API/search | GitHub connector + Apify skills | companies, developers, tech stack, activity | P1 |
| Business directories | Yelp, Yellow Pages and regional directories | API/provider/browser/crawler | Apify ecosystem; directory-specific actors | company, category, phone, address, website | P0/P1 |
| Review platforms | G2, Capterra, Trustpilot, Clutch, TripAdvisor etc. | API/provider/crawler | Apify ecosystem / web crawler | vendors, buyers, reviews, pain signals | P1 |
| Job boards | Indeed, LinkedIn Jobs, regional boards | API/provider/crawler | Apify skills/actors | hiring signals, company, role, geography | P1 |
| Company databases | Apollo, Crunchbase-type databases, public registries | API/MCP | Apollo MCP; enrichment MCP | firmographics, funding, contacts, technologies | P0/P1 |
| Email intelligence | Domain/person lookup | API/MCP/DNS/SMTP | B2B Enrichment MCP, Prospector MCP, Hunter-compatible workflows | business emails, confidence, verification | P0 |
| Technology intelligence | BuiltWith/Wappalyzer-type sources | API/browser/provider | Build/use tech-stack enrichment connector | technologies, vendors, CMS, ads, analytics | P1 |
| Advertising intelligence | Meta Ads, Google Ads/search results, other ad libraries | API/provider/crawler | Apify skills/actors | active advertisers, creatives, offers | P1 |
| Government/public registries | Company/entity/license/tender registries | Official API/download/crawler | jurisdiction-specific connectors | legal entities, licenses, tenders | P1 |
| Procurement/tenders | Government/private tender portals | API/crawler/browser | source-specific workflows | active demand, contracts, buyers | P1 |
| Events/conferences | Speaker/sponsor/exhibitor lists | Website/API/crawler | Crawl4AI/Apify | companies, people, buying signals | P1 |
| Associations/chambers | Member directories | API/crawler/browser | source-specific crawlers | companies, sectors, geography | P1 |
| Partner/referral ecosystems | Agencies, consultants, vendors, communities | API/crawler/manual import | CRM/referral workflow | partner candidates, warm paths | P1 |
| News/media | Company/person/topic news | Search/news API/crawler | search + crawler + research agent | events, funding, leadership, triggers | P1 |
| Podcasts/newsletters | Shows, episodes, guests | Search/API/crawler | web research + YouTube/podcast extraction | people, companies, themes | P2 |
| Communities/forums | Industry forums, Slack/Discord where permitted, niche communities | API/search/manual connector | research agent + source-specific tools | pain points, intent, questions | P2 |
| Social listening | Multi-platform mentions | API/provider/search | multi-source research workflows | mentions, sentiment, demand signals | P1 |
| First-party inbound | Website forms, chat, email, ads | Webhook/API | n8n + CRM | high-intent leads | P0 |
| Existing databases | CSV, spreadsheets, CRM exports, purchased lists | File/API import | n8n/data-normalization workflows | contacts/accounts | P0 |

## Verified reusable assets found in this extension

### 1. Apify Agent Skills

`https://github.com/apify/agent-skills`

The current skill catalog includes a universal scraper capable of selecting actors across major social, search, maps, review and other platforms. The documented curated coverage includes Instagram, Facebook, TikTok, YouTube, X, LinkedIn, Google Maps, Reddit, Yelp, GitHub and many more; the broader Apify Store provides a much larger actor ecosystem. **Use as a source/adapter layer, not as permission to bypass site restrictions.**

### 2. Multi-source AI Lead Gen Scraper

`https://github.com/sirlifehacker/lead-gen-hacker`

n8n + Apify + AI workflow covering LinkedIn, Instagram, Google Maps, YouTube and Meta Ads Library, followed by normalization, website/email enrichment and quality filtering.

### 3. Lead Research Agent

`https://github.com/mcvalosborne/lead-research-agent`

Open-source discovery/enrichment/scoring/outreach pipeline covering Twitter/X, LinkedIn and Reddit with enrichment and CRM/email integration patterns.

### 4. Lead-Reach

`https://github.com/getleads-humain/Lead-Reach`

Multi-agent lead discovery/enrichment/research architecture spanning web, LinkedIn, Twitter, GitHub, YouTube and Reddit, with cross-source synthesis.

### 5. Crawl4AI MCP

Examples:
- `https://github.com/jeffmm/crawl4ai-mcp`
- `https://github.com/sadiuysal/crawl4ai-mcp-server`
- `https://github.com/potterdigital/crawl4ai-mcp`

Self-hosted MCP options for search, crawling, browser rendering, multi-page extraction, sitemap crawling and structured content acquisition.

### 6. Apollo official MCP / skills

`https://github.com/apolloio/apollo-mcp-plugin`

Official Apollo MCP and accompanying skills for people/company prospecting, enrichment, sequences and sales analytics.

### 7. B2B Enrichment MCP

`https://github.com/Aleksey-Panf/b2b-enrichment-mcp`

Combines Apollo company intelligence with Hunter email intelligence through one MCP interface.

### 8. Prospector MCP

`https://github.com/josiebot26/prospector-mcp-email-finder`

Self-contained business-email discovery and DNS/SMTP verification without requiring a paid enrichment API.

### 9. OpenLeads

`https://github.com/Samyrrrrrr990/openleads`

Open-source Apollo-style prospecting architecture that federates public sources, discovers people, verifies emails and deduplicates records.

### 10. Hermes lead-generation pipeline

`https://github.com/vivekshetye/hermes-lead-generation-pipeline`

Reusable agent/skill composition for prospecting, scraping, enrichment, contact finding, ICP scoring and outreach.

## Acquisition method matrix

Do not treat all sources as "scraping". Select the least fragile and most compliant method available.

| Method | Best use | Reliability | Cost profile | Preferred order |
|---|---|---|---|---:|
| Official API | Structured source data | High | Free/paid | 1 |
| Official export | Existing authorized data | High | Usually low | 2 |
| Licensed data provider | Large-scale enrichment | High | Paid | 3 |
| MCP/API wrapper | Agent-accessible APIs | High if maintained | Free/paid | 4 |
| Search + crawl | Public web discovery | Medium/high | Low/paid | 5 |
| Browser automation | JS-heavy public workflows | Medium | Low/paid | 6 |
| Source-specific actor | Repeated platform extraction | Medium/high | Variable | 7 |
| Custom scraper | Unique source with no reusable option | Variable | Engineering | 8 |
| Manual research | High-value exception | High for small volume | Human time | 9 |

## Required acquisition agents/skills

1. **Source Router** — selects the best source and acquisition method.
2. **Search Prospecting Agent** — discovers accounts from search engines.
3. **Website Discovery Agent** — finds and classifies company sites.
4. **Directory Prospecting Agent** — extracts businesses from relevant directories.
5. **Social Prospecting Agent** — finds relevant public profiles/signals.
6. **Job-Signal Agent** — detects hiring as buying/technology/growth signals.
7. **Advertising-Signal Agent** — detects active advertisers and offer changes.
8. **Intent-Signal Agent** — detects public buying/problem signals.
9. **Contact Finder Agent** — identifies decision makers.
10. **Email Discovery Agent** — finds candidate business emails.
11. **Email Verification Agent** — verifies deliverability and confidence.
12. **Company Enrichment Agent** — firmographics, services, geography, technology.
13. **Tech-Stack Agent** — identifies relevant technologies.
14. **Funding/Growth Agent** — detects funding, hiring, expansion and growth events.
15. **Review/Pain-Signal Agent** — extracts customer pain and dissatisfaction signals.
16. **Social Conversation Agent** — detects relevant conversations/questions.
17. **Duplicate Resolution Agent** — merges person/account identities.
18. **Source Confidence Agent** — scores provenance and freshness.
19. **ICP Matching Agent** — maps accounts/contacts to ICP.
20. **Lead Scoring Agent** — combines fit + intent + timing + contactability.
21. **Compliance/Policy Agent** — checks source/channel restrictions and outreach eligibility.
22. **CRM Sync Agent** — writes canonical records and provenance.

## Lead record minimum schema

`lead_id | account_id | source | source_url | discovered_at | last_verified_at | person_name | title | company | domain | location | industry | employee_band | revenue_band | technology_signals | hiring_signals | funding_signals | advertising_signals | pain_signals | intent_signals | social_profiles | email | email_confidence | phone | data_provenance | source_confidence | ICP_fit | lead_score | outreach_eligibility | consent/legal_basis | owner | CRM_id`

## Multi-source waterfall

For each account:

`Source A → normalize → dedupe → Source B → enrich → Source C → verify → confidence → stop when sufficient`

Do not query every source for every lead. Use adaptive acquisition based on missing fields and expected value.

Example:

`Google Search → Website → LinkedIn/Apollo → Email Finder → Tech Stack → Hiring → Reviews → Social → Score`

## Quality controls

- Preserve original source URL for every important field.
- Store discovery and verification timestamps.
- Never silently overwrite a stronger source with a weaker source.
- Keep field-level confidence where practical.
- Deduplicate at both person and account level.
- Separate business contact data from personal/sensitive data.
- Respect source terms, robots/access controls, applicable law and provider limits.
- Do not use anti-bot mechanisms to defeat access controls.
- Rate-limit and cache repeated requests.
- Keep an acquisition audit trail.
- Provide suppression/opt-out handling.
- Require human approval before autonomous outbound at initial deployment.

## Nivy priority source stack

### P0 — Start here

`Search → Public company websites → Google Maps/local business → Apollo/company data → Email discovery/verification → CRM`

### P1 — Expand coverage

`LinkedIn → Instagram → Facebook/Meta Ads → YouTube → X → Reddit → GitHub → job boards → review/directories → tech stack → funding/news → tenders/registries`

### P2 — Specialized intelligence

`Associations → events → communities → podcasts/newsletters → advanced social listening → niche directories → country-specific sources`

## Important conclusion

The previous sales library **did cover prospecting, enrichment, scoring and outreach at the workflow level**, but it did **not explicitly inventory the full source-acquisition layer at this depth**.

This file therefore closes that gap by treating lead acquisition as its own reusable infrastructure layer.

It should feed directly into:

`86 Acquisition Catalog → 77 Master Registry → 79 Connector Registry → 82 P0 Workflow Specs → Revenue Engine`

## Discovery policy

This is a reusable source architecture, not a claim that every website on the internet can or should be scraped. When a source has an official API, licensed dataset, export or approved connector, prefer that route. Where access is restricted, the system must fall back to permitted sources rather than attempting to bypass restrictions.
