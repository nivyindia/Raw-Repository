# Agentic Company — Channel & Surface Coverage Expansion Catalog
Research date: 2026-09-19

Purpose: second-wave discovery to close the major channel/surface gaps in the company-wide reuse library. This catalog treats a "channel" broadly: acquisition channel, communication channel, social network, directory/database, marketplace, app ecosystem, public/government source, owned web surface, community, media/PR, telephony, and partner ecosystem.

Governing rule: DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

Important: coverage below is a research map, not a claim that every channel has a production-ready agent. APIs, automation permissions, platform terms, regional availability, licensing and data-use restrictions must be verified before deployment.

## 1. Social-media channel matrix

| ID | Channel/surface | What Nivy should cover | Reusable discovery/resource | Link |
|---|---|---|---|---|
| SM01 | LinkedIn | company page, personal profile, posts, comments, DMs, social selling, lead research, creator/employee advocacy | AI Social Agent; Sales agents already cataloged | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM02 | Instagram | posts, Reels, comments, DMs, creator discovery, publishing, listening | AI Social Agent; Mesh Pilot Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM03 | Facebook | pages, groups, posts, Messenger, Reels, ads | AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM04 | YouTube | long video, Shorts, comments, channel research, publishing | AI Social Agent; Mesh Pilot Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM05 | TikTok | short video, creator discovery, trends, publishing | AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM06 | X/Twitter | posts, replies, DMs, listening, trends | AI Social Agent; Caspian channel layer | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM07 | Threads | publishing, listening, community engagement | AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM08 | Pinterest | visual discovery, boards, publishing | AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM09 | Reddit | communities, listening, research, reputation, contribution | AI Social Agent; social research | https://github.com/SamurAIGPT/open-ai-social-agent |
| SM10 | Discord | communities, support, events, sales/community workflows | Caspian agent communication layer | https://github.com/tryCaspian/caspian-sdk |
| SM11 | Slack | communities, customer/team communication, alerts | Caspian agent communication layer | https://github.com/tryCaspian/caspian-sdk |
| SM12 | Telegram | channel/group/bot communication, sales/support | Caspian; SalesGPT | https://github.com/tryCaspian/caspian-sdk |
| SM13 | Bluesky | social publishing/listening | Caspian | https://github.com/tryCaspian/caspian-sdk |
| SM14 | WhatsApp Business | inbound/outbound sales, support, follow-up, booking | SalesGPT; omnichannel sales systems | https://github.com/NeuroVee/VeeSalesGPT |
| SM15 | WeChat | sales/messaging in relevant markets | SalesGPT channel architecture | https://github.com/NeuroVee/VeeSalesGPT |
| SM16 | Weibo | sales/messaging in relevant markets | SalesGPT channel architecture | https://github.com/NeuroVee/VeeSalesGPT |

## 2. Direct messaging / conversational / telephony

| ID | Surface | Coverage | Reusable resource | Link |
|---|---|---|---|---|
| CH01 | Email | inbound/outbound, sequences, reply classification, follow-up, campaigns | Sales/marketing agents already cataloged | https://github.com/avcap/ai-sdr |
| CH02 | SMS | sales, reminders, support, transactional workflows | Caspian | https://github.com/tryCaspian/caspian-sdk |
| CH03 | RCS | conversational business messaging | Caspian hosted channel list | https://github.com/tryCaspian/caspian-sdk |
| CH04 | Voice/PSTN | inbound receptionist, outbound qualification, routing, booking | AIReceptionist | https://github.com/kirklandsig/AIReceptionist |
| CH05 | SIP | enterprise telephony transport | AIReceptionist / LiveKit architecture | https://github.com/kirklandsig/AIReceptionist |
| CH06 | Multilingual voice | India + international voice workflows | Mesh Pilot AI Voice Agent | https://github.com/Nuraveda-Labs/ai-voice-agent |
| CH07 | Web chat | website qualification, support, sales, booking | omnichannel support/sales systems | https://github.com/Hesper-Labs/owly |
| CH08 | Messenger | Meta conversational sales/support | AI Social Agent / omnichannel agents | https://github.com/SamurAIGPT/open-ai-social-agent |
| CH09 | Viber / LINE | international messaging coverage | Convera channel map for capability inventory | https://www.allaboutbusinessmessaging.com/ |

## 3. Owned web surfaces

| ID | Surface | Required capability |
|---|---|---|
| WEB01 | Main website | pages, SEO, GEO, CRO, lead capture, chat, booking, analytics |
| WEB02 | Landing pages | campaign-specific pages, personalization, A/B testing |
| WEB03 | Blog / knowledge center | SEO/GEO content, research, internal linking, refresh |
| WEB04 | Free tools / calculators | product-led acquisition, lead capture, usage analytics |
| WEB05 | Forms / quizzes / assessments | qualification, segmentation, scoring |
| WEB06 | Customer portal | onboarding, tickets, documents, billing, status |
| WEB07 | Careers portal | jobs, candidate capture, screening |
| WEB08 | Partner portal | referrals, affiliates, co-marketing, deal registration |
| WEB09 | Developer/API portal | product-led growth, integrations, docs |
| WEB10 | Status / trust center | uptime, security, compliance, evidence |

Browser agents are useful as a generic integration layer for sites that lack APIs: OpenOnion Browser Agent and A2A Browser Agent provide natural-language browser control, forms and structured extraction. Use only where platform terms permit automation. https://github.com/openonion/browser-agent ; https://github.com/inference-gateway/browser-agent

## 4. Business directories & local discovery

This must be treated as a separate acquisition/data surface, not just "Google Maps".

| ID | Directory/data surface | Coverage to research/connect |
|---|---|---|
| DIR01 | Google Business Profile / Maps | local business discovery, reviews, categories, local presence |
| DIR02 | Apple Business Connect / Maps | Apple local presence |
| DIR03 | Bing Places | Microsoft local presence |
| DIR04 | Yelp | local discovery/reviews |
| DIR05 | Foursquare | places/business data |
| DIR06 | Yellow Pages and country equivalents | directory discovery |
| DIR07 | TripAdvisor | travel/hospitality/local reviews |
| DIR08 | OpenStreetMap | open geospatial business/place data |
| DIR09 | industry-specific directories | vertical lead sourcing |
| DIR10 | chamber/business-association directories | high-intent local/B2B discovery |
| DIR11 | professional directories | accountants, lawyers, agencies, consultants, healthcare etc. |
| DIR12 | government business registries | company verification and market intelligence |
| DIR13 | startup/company databases | company discovery and funding signals |
| DIR14 | B2B databases | company/contact/enrichment |
| DIR15 | review directories | reputation and buyer-intent research |

Reusable implementation: Google Maps AI Agent can turn Maps searches into structured B2B lead lists and enrichment; LeadPipeline covers Maps → Sheets CRM → outreach. https://github.com/xCodeWraith/GoogleMapAIagent ; https://github.com/AI-Invention/lead-pipeline

## 5. B2B/company/data directories

The discovery layer should not depend on one provider.

| Category | Examples to include in the future connector registry |
|---|---|
| Company databases | Crunchbase, Dealroom, Tracxn, PitchBook, CB Insights |
| B2B/contact data | Apollo, ZoomInfo, RocketReach, Hunter, Prospeo, Clearbit-style enrichment |
| Technology intelligence | BuiltWith, Wappalyzer and technology-detection sources |
| SEO/competitive data | Ahrefs, Semrush, Similarweb, SpyFu |
| Review/software directories | G2, Capterra, GetApp, Software Advice, AlternativeTo |
| Startup/product discovery | Product Hunt, BetaList, Hacker News, startup databases |
| Agency/service directories | Clutch, GoodFirms, DesignRush and vertical equivalents |
| Job/company signals | LinkedIn Jobs, Indeed, Glassdoor, Wellfound and regional job boards |
| Procurement/vendor data | public tender portals, vendor registries, award notices |
| Geographic/open data | OpenStreetMap, government open-data portals |

For GTM integrations, the community GTM MCP catalog explicitly covers CRM, enrichment, SEO, ads, analytics and lifecycle and notes that many high-spend surfaces rely on community-built connectors rather than first-party MCP servers. https://github.com/matteotitta/awesome-gtm-mcp-servers

## 6. App marketplaces / software ecosystems

| Ecosystem | Required automation surface |
|---|---|
| Shopify App Store | ecommerce, orders, customers, marketing, support, fulfillment |
| Salesforce AppExchange | CRM, sales, service, marketing, enterprise workflows |
| HubSpot App Marketplace | CRM, marketing, sales, support, operations |
| Microsoft AppSource | Dynamics, Microsoft 365, Power Platform, enterprise |
| Google Workspace Marketplace | Gmail, Sheets, Drive, Calendar, Meet and add-ons |
| Atlassian Marketplace | Jira, Confluence, service management |
| Slack App Directory | internal/customer workflows |
| Zoom App Marketplace | meetings, events, recordings, follow-up |
| WordPress ecosystem | website, forms, SEO, commerce, content |
| WooCommerce ecosystem | ecommerce operations |
| Odoo Apps | ERP/CRM/finance/HR/operations |
| ERPNext/Frappe ecosystem | ERP/CRM/HR/operations |
| Zapier / Make / n8n ecosystems | integration and workflow building |
| GitHub Marketplace | engineering, CI/CD, security, project workflows |
| AWS / Azure / Google Cloud marketplaces | infrastructure, data, AI and enterprise procurement |

## 7. Freelance / talent / services marketplaces

| Surface | Business use |
|---|---|
| Upwork | client acquisition, jobs, proposals, talent |
| Fiverr | service demand and competitive intelligence |
| Freelancer | jobs and services |
| Toptal | premium talent/market intelligence |
| PeoplePerHour | international services |
| Guru | services and project sourcing |
| Contra | independent professionals |
| Wellfound | startup talent/business discovery |
| LinkedIn Jobs / Indeed / regional boards | hiring + market signals |

Automation must respect each platform's terms and API availability.

## 8. PR / media / creator / community channels

| Channel family | Coverage |
|---|---|
| Press-release distribution | releases, media lists, pickup monitoring |
| Journalist databases | journalist discovery, pitch personalization, response tracking |
| Podcasts | guest discovery, outreach, booking, preparation |
| YouTube creators | creator discovery, sponsorship, collaboration |
| Influencer marketplaces | creator sourcing, negotiation, campaign measurement |
| Affiliate networks | partner recruitment, links, commission tracking |
| Referral programs | customer/partner referrals |
| Communities | Reddit, Discord, Slack, Facebook Groups, forums |
| Q&A | Quora and vertical Q&A communities |
| Newsletters | sponsorships, placements, owned newsletters |
| Events/webinars | Luma, Eventbrite and vertical event platforms |
| Trade shows | exhibitor/sponsor/attendee discovery and follow-up |

Retail-marketing skills also explicitly cover referrals, affiliates, community, influencer, co-marketing, PR and experiential/trade-show workflows. https://github.com/sushpadhye6789/retail-marketing-skills

## 9. Advertising surfaces

Create separate connectors/agents for:
- Google Ads
- Microsoft Advertising
- Meta Ads
- LinkedIn Ads
- TikTok Ads
- YouTube Ads
- Amazon Ads
- Pinterest Ads
- Reddit Ads
- X Ads
- programmatic/display networks
- retargeting platforms
- local advertising networks
- sponsored newsletters/podcasts
- marketplace advertising

The Mesh Pilot marketing stack already exposes an AI Ads Agent covering Meta, Google, TikTok and Amazon Ads as a reusable reference. https://github.com/Meshpilot-AGI/ai-ads-agent

## 10. Search / discovery / AI-answer channels

Cover all of:
- Google Search
- Bing
- Google News
- Google Images
- Google Shopping
- YouTube Search
- Amazon search
- marketplace search
- app-store search
- Reddit search
- social platform search
- AI answer/search systems (ChatGPT, Gemini, Claude, Perplexity and emerging engines)
- GEO / AI visibility
- entity/knowledge graph optimization

The existing UnifAPI and marketing-agent resources in Catalog 13 should be combined with technical SEO crawlers, schema, entity optimization, citation/mention monitoring and content refresh workflows.

## 11. Marketplaces & commerce acquisition

Cover:
- Amazon
- eBay
- Etsy
- Walmart Marketplace
- Alibaba
- IndiaMART
- TradeIndia
- Global Sources
- Faire
- regional B2B marketplaces
- app/software marketplaces
- cloud marketplaces
- service marketplaces
- education/course marketplaces
- booking/travel marketplaces
- property marketplaces
- job/talent marketplaces

Each needs discovery → listing optimization → lead/order capture → communication → CRM → fulfillment → review/retention.

## 12. Government / public-sector / institutional channels

This is a distinct international GTM stream.

| Surface family | Examples / coverage |
|---|---|
| India procurement | GeM, CPPP/eProcure, state tender portals |
| US procurement | SAM.gov and federal agency procurement sources |
| EU procurement | TED / Tenders Electronic Daily and national portals |
| UK procurement | Find a Tender / Contracts Finder |
| International development procurement | World Bank, UN procurement, ADB and other multilaterals |
| Grants | national grant portals, EU funding, US grants, development grants |
| Public company registries | national/state/provincial corporate registries |
| Open data | national, state, city and international open-data portals |
| Licenses/permits | public regulatory registries where legally available |
| Government supplier directories | approved vendor/supplier registries |
| Public meetings/notices | municipal, regulatory and institutional notices |

ProcureX is a reusable example of agentic government-tender analysis for Indian GeM/CPPP/NIC tender PDFs. https://github.com/sarva-20/ProcureX

OpenGov India is another example focused on monitoring CPPP and GeM procurement notices and normalizing tender evidence. https://github.com/xlogix/opengov-india

## 13. Finance / transactional channels

Beyond accounting software, cover:
- bank feeds
- payment gateways
- Stripe/PayPal/Razorpay and regional processors
- invoicing
- subscription billing
- AP/AR
- collections/dunning
- payroll
- tax portals
- expense management
- procurement cards
- FX/remittance
- revenue recognition
- financial reporting
- FP&A
- treasury
- audit evidence

Finance skills already provide reusable agent patterns for billing, AR, reconciliation and revenue operations. https://github.com/loopfour/finance-skills

## 14. HR / people channels

Cover:
- job boards
- applicant tracking systems
- LinkedIn recruiting
- candidate sourcing
- screening
- scheduling
- assessments
- offer generation
- onboarding
- employee helpdesk
- payroll/benefits
- performance/KRAs
- learning/LMS
- internal mobility
- offboarding
- workforce analytics

## 15. Legal / compliance / trust channels

Cover:
- contract intake
- clause extraction/review
- proposal/quotation
- e-signature
- DPA/privacy workflows
- KYC/KYB
- sanctions/PEP screening
- regulatory monitoring
- policy management
- evidence/audit packs
- trademark/IP monitoring
- insurance/certification
- vendor compliance
- customer security questionnaires

High-impact legal and financial actions should retain explicit approval gates.

## 16. Customer lifecycle channels

The lifecycle must be modeled separately from acquisition:
Lead → MQL → SQL → opportunity → proposal → negotiation → won → onboarding → implementation → adoption → support → health → renewal → expansion → cross-sell → upsell → referral → advocacy → win-back.

Include web, email, phone, WhatsApp, SMS, social DMs, in-app messaging, community, customer portal, helpdesk and meetings.

Owly is a reusable omnichannel support reference spanning WhatsApp, email and phone with unified profiles, KB, routing, scheduling and analytics. https://github.com/Hesper-Labs/owly

## 17. Meetings / collaboration / work surfaces

Cover:
- Google Meet
- Zoom
- Microsoft Teams
- Calendars
- meeting transcription
- action-item extraction
- CRM update
- follow-up generation
- proposal/task creation
- Slack/Teams escalation
- project-management systems
- document collaboration

## 18. Browser / universal connector layer

A company OS cannot assume an API exists for every channel. Keep a governed browser-automation capability for approved workflows.

Reusable references:
- OpenOnion Browser Agent — natural-language browser automation, screenshots, forms, scraping and deep research: https://github.com/openonion/browser-agent
- Inference Gateway Browser Agent — A2A browser agent with web navigation, forms, extraction and cited research: https://github.com/inference-gateway/browser-agent
- agent-browser — browser automation CLI with form submission and authenticated session handling: https://github.com/yangcyyang/agent-browser

Do not use browser automation to bypass CAPTCHAs, access controls or platform restrictions.

## 19. Agent-to-agent / integration discovery

| Layer | Reuse |
|---|---|
| MCP | awesome-mcp-servers + GTM-specific MCP catalogs |
| A2A | A2A Registry + A2A Directory |
| Agent communication | Caspian |
| Browser agent | A2A Browser Agent |
| Unified business runtime | ERP-AI / ERPNext / Odoo references |
| Workflow | n8n |
| Agent runtime | LangGraph / Dify / Microsoft Agent Framework |

A2A Registry indexes live hosted A2A agents through agent cards; A2A Directory collects agents, servers and clients. https://github.com/prassanna-ravishankar/a2a-registry ; https://github.com/sing1ee/a2a-directory

## 20. Unified company OS references discovered

| Resource | Why it matters |
|---|---|
| Cyber AI Team | self-hosted company OS pattern: ERPNext system of record + many governed AI workers + owner console + memory + approvals + audit |
| Autonomous Business OS | lead → revenue pipeline plus dynamic department/agent/skill creation and approval-gated loops |
| ERP-AI | agent-native business runtime spanning finance, HR, sales, support, operations, projects, IT, procurement, billing and analytics |
| Sentinel ERP | ERP with HRMS, CRM, finance, inventory/procurement, workflows and AI copilot |

Links:
https://github.com/Hyper-AI-Lab/cyber-ai-team
https://github.com/Cubiczan/autonomous-business-os
https://github.com/erphq
https://github.com/jeevansai-hub/Sentinal-ERP

## 21. Complete channel coverage model for Nivy

The Nivy connector registry should eventually classify every integration into these buckets:

1. Search
2. Social
3. Messaging
4. Email
5. Voice
6. Web
7. Communities
8. Reviews
9. Directories
10. Company databases
11. Contact/enrichment databases
12. Jobs/talent
13. Freelance/service marketplaces
14. Product/software marketplaces
15. Ecommerce marketplaces
16. App stores
17. Cloud marketplaces
18. Events/trade shows
19. PR/media/podcasts
20. Influencers/creators
21. Affiliates/referrals/partners
22. Advertising networks
23. AI-answer engines/GEO
24. Government procurement
25. Government registries/open data
26. Grants/development institutions
27. Finance/payments/banking
28. HR/payroll/LMS
29. Legal/compliance/trust
30. Customer support/helpdesk
31. Meetings/calendar
32. Project/PSA
33. ERP/CRM
34. Knowledge/documents
35. Analytics/BI
36. Developer/API ecosystems
37. Browser/universal automation
38. MCP
39. A2A
40. Identity/RBAC/audit/approval.

## 22. Next research queue — do not mark "complete"

To genuinely approach exhaustive coverage, the next discovery pass should enumerate named services and reusable agents/connectors inside each bucket, country by country where relevant, then record:

- official API/docs
- open-source implementation
- MCP server
- A2A agent
- n8n/Make/Zapier workflow
- browser-agent fallback
- license
- pricing/free tier
- region availability
- ToS/data-use limitations
- maintenance/activity
- Nivy applicability
- exact reuse/adaptation path.

This prevents "all channels" from becoming a static list: the registry should be continuously expanded as new platforms and agents appear.
