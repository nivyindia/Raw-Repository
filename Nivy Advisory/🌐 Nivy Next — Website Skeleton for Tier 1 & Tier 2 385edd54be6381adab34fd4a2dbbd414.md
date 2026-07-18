# 🌐 Nivy Next — Website Skeleton for Tier 1 & Tier 2 International Clients

> **Document Type:** Website Architecture Blueprint | **Version:** 1.0 | **Created:** 20 June 2026
> 

> **Purpose:** A complete page-by-page website skeleton for [thenivy.com](http://thenivy.com) — built specifically to convert Tier 1 (US, UK, Canada, Australia, Germany, Netherlands, Singapore, Ireland, NZ) and Tier 2 (UAE, India enterprise, South Africa, Malaysia, Brazil, Poland, Portugal) international clients. Every section is written with the psychological trust requirements of those buyers in mind.
> 

---

# How to Read This Document

This is not a content document — it is a **structural blueprint**. Each page entry defines:

- The page's **single conversion goal**
- The **section-by-section layout** with copy direction
- The **trust signals** that Tier 1/2 buyers require at each point
- The **CTA logic** and where it leads
- **SEO intent** the page captures

Every section marked `[BLOCK]` is a reusable component. The same block appears across multiple pages — build it once in your CMS, drop it anywhere.

---

# 🗺️ Full Site Map

```
thenivy.com
│
├── / (Homepage)
│
├── /about
├── /results
├── /pricing
├── /blog
├── /contact
├── /book-a-call
│
├── /services (Hub)
│   ├── /services/marketing (Hub)
│   │   ├── /services/seo
│   │   ├── /services/ppc
│   │   ├── /services/social-media-marketing
│   │   ├── /services/social-media-advertising
│   │   ├── /services/content-marketing
│   │   ├── /services/email-marketing
│   │   ├── /services/linkedin-marketing
│   │   ├── /services/video-marketing
│   │   ├── /services/local-business-marketing
│   │   ├── /services/ecommerce-marketing
│   │   ├── /services/cro
│   │   └── /services/marketing-analytics
│   ├── /services/ai-automation
│   ├── /services/website-development
│   ├── /services/app-development
│   ├── /services/graphic-design
│   ├── /services/video-production
│   └── /services/virtual-assistant
│
├── /markets (Hub)
│   ├── /markets/uk
│   ├── /markets/us
│   ├── /markets/australia
│   ├── /markets/canada
│   ├── /markets/uae
│   ├── /markets/germany
│   ├── /markets/singapore
│   └── /markets/south-africa
│
├── /industries (Hub)
│   ├── /industries/saas
│   ├── /industries/ecommerce
│   ├── /industries/professional-services
│   ├── /industries/recruitment
│   ├── /industries/health-wellness
│   ├── /industries/fintech
│   ├── /industries/real-estate
│   └── /industries/education
│
└── /legal
    ├── /privacy-policy
    ├── /terms-of-service
    ├── /cookie-policy
    └── /gdpr
```

**Total pages at full build: 53**

---

# NAV & FOOTER SYSTEM

## Primary Navigation

```
[Logo]  Services ▾  Industries ▾  Markets ▾  Results  Pricing  About  [Book a Call — CTA Button]
```

**Services mega-menu:**

```
Marketing                    Technology              Creative & Ops
SEO                          AI Automation           Graphic Design
PPC Advertising              Website Development     Video Production
Social Media Marketing       App Development         Virtual Assistant
Social Media Advertising     ─────────────────
Content Marketing            [→ See All 18 Services]
Email Marketing
LinkedIn Marketing
Video Marketing
Local Business Marketing
Ecommerce Marketing
Conversion Rate Optimisation
Marketing Analytics
```

**Trust bar under nav (sticky on scroll):**

`Trusted by growth-stage businesses in 🇺🇸 🇬🇧 🇨🇦 🇦🇺 🇦🇪 · Response within 24hrs · Clients live in 5–7 days`

## Footer (4 columns)

**Col 1 — Nivy Next**

Logo + one-line positioning: "AI-powered growth for ambitious international businesses."

Contact: [contact@thenivy.com](mailto:contact@thenivy.com) | +91 86705 43601

Social icons: LinkedIn · Instagram · X

**Col 2 — Services**

SEO · PPC · Social Media · Content · Email · LinkedIn · Video Marketing · Local · Ecommerce · CRO · Analytics · AI Automation · Web Dev · App Dev · Design · Video Production · VA Services

**Col 3 — Company**

About · Results · Pricing · Blog · Book a Call · Contact · Careers

**Col 4 — Markets**

🇺🇸 US · 🇬🇧 UK · 🇨🇦 Canada · 🇦🇺 Australia · 🇦🇪 UAE · 🇩🇪 Germany · 🇸🇬 Singapore · 🇿🇦 South Africa

**Footer bottom bar:**

`© 2026 Nivy Next. All rights reserved. | Privacy Policy | Terms of Service | Cookie Policy | GDPR`

`Nivy Next is a trading name of Nivy Digital Private Limited, registered in India (CIN: [TBC]).`

---

# PAGE 1 — HOMEPAGE (/)

**Goal:** Convert cold international traffic → discovery call within 30 seconds of landing.

**SEO intent:** Brand + "AI digital agency" + "digital marketing agency [country]"

---

## S1 · HERO

**Layout:** Full-width, dark/strong background. Left: copy. Right: visual (device mockup or abstract motion graphic).

**H1:** `Scale Faster. Grow Smarter. One AI-Powered Team.`

**Sub:** `Full-stack digital services for growth-stage businesses in the US, UK, Canada, Australia, and UAE — marketing, automation, web, apps, design, and VA operations under one roof.`

**CTA pair:**

- `[Book a Free Strategy Call]` — primary, links → /book-a-call
- `[See Our Results →]` — secondary, links → /results

**Trust line beneath CTAs:**

`No long-term lock-in on Starter plans · Response within 24 hrs · Clients live in 5–7 business days`

---

## S2 · TRUST BAR [BLOCK: trust-bar]

**Layout:** Horizontal scrolling strip, grey background.

`Google Partner | Meta Blueprint | HubSpot Partner | Semrush Agency | OpenAI API | AWS Activate | Make Certified`

**Second row:** Market flags with label:

`Actively serving clients in 🇺🇸 US · 🇬🇧 UK · 🇨🇦 Canada · 🇦🇺 Australia · 🇦🇪 UAE · 🇩🇪 Germany · 🇸🇬 Singapore`

---

## S3 · PAIN PANEL ("Sound familiar?")

**Layout:** 3 cards, icon + headline + 1-line description.

**Card 1:** `Too many vendors, zero accountability` — You're managing 4–6 agencies. Nobody owns the result.

**Card 2:** `Ad spend burning with nothing to show` — Campaigns running, CPA rising, pipeline flat.

**Card 3:** `Your competitors are using AI. You're not.` — Automation and AI are compressing timelines — for whoever deploys them first.

---

## S4 · THE SOLUTION

**Layout:** Centre-aligned intro + hub-and-spoke diagram.

**Headline:** `One Team. 18 Capabilities. One Result.`

**Body:** `Nivy Next is not an agency. We're a growth partner — one integrated team that connects your marketing, technology, creative, and operations into a single system built around your business goal.`

**Hub diagram:** Centre node = "Nivy Next" → 4 spokes: Marketing (12 services) · Technology (3) · Creative (2) · Operations (1)

---

## S5 · SERVICES GRID

**Layout:** 4-column category grid. Each category has icon, name, and service pills below.

**Marketing (12):** SEO · PPC · Social Media Marketing · Social Media Advertising · Content Marketing · Email Marketing · LinkedIn Marketing · Video Marketing · Local Marketing · Ecommerce Marketing · CRO · Marketing Analytics

**Technology (3):** AI Automation · Website Development · App Development

**Creative (2):** Graphic Design · Video Production

**Operations (1):** Virtual Assistant Services

**Below grid:** `[→ Explore All 18 Services]` → /services

---

## S6 · RESULTS STATS [BLOCK: stats-strip]

**Layout:** 4 large stat cards in a row.

| Stat | Label |
| --- | --- |
| 3.2x | Average lead quality improvement within 90 days |
| 41% | Average reduction in cost per acquisition |
| 80% | Reduction in manual ops via AI automation |
| <5 min | AI lead response time vs. 24–48 hrs manual |

---

## S7 · PROCESS TIMELINE [BLOCK: process]

**Layout:** Horizontal 6-step numbered timeline.

1. **Discovery** — 30-min call. Understand your goals, market, and gaps.
2. **Strategy** — Tailored proposal with scope, timelines, and investment.
3. **Onboarding** — Account setup, tool access, team intro. Fast and frictionless.
4. **Execution** — Your dedicated team gets to work. Weekly updates.
5. **Reporting** — Clear performance data. No black boxes.
6. **Scale** — Results compound. We expand as your business grows.

**Below:** `Most clients are live within 5–7 business days of sign-off.`

---

## S8 · CASE STUDY PREVIEWS [BLOCK: case-study-cards]

**Layout:** 3 cards. Each: Market flag + industry + key result metric (large, bold) + 1-line summary + "Read Full Case Study →"

**Card 1:** 🇬🇧 UK · B2B SaaS · **CPA reduced 70%** — PPC restructure + SEO foundation built in 90 days

**Card 2:** 🇺🇸 US · Recruitment · **Response time: 48hrs → 4min** — AI automation replacing manual qualification

**Card 3:** 🇦🇺 AU · E-Commerce · **Email: 0% → 31% of revenue** — Klaviyo flows built and live in 3 weeks

`[→ See All Case Studies]` → /results

---

## S9 · TESTIMONIALS [BLOCK: testimonials]

**Layout:** Carousel. Each card: quote → role → company type → market flag → star rating.

> *"Nivy Next didn't just run our campaigns — they changed how we think about growth. The results in Q1 exceeded everything we'd achieved in the prior year."*
> 

> — Head of Marketing, B2B SaaS | 🇬🇧 United Kingdom ⭐⭐⭐⭐⭐
> 

> *"The AI automation system saved us 30+ hours per week. Our team focuses entirely on closing now — not chasing."*
> 

> — Founder, Recruitment Firm | 🇺🇸 United States ⭐⭐⭐⭐⭐
> 

> *"Incredibly professional, fast, and strategic. They feel like an extension of our internal team."*
> 

> — CEO, E-Commerce Brand | 🇦🇺 Australia ⭐⭐⭐⭐⭐
> 

---

## S10 · WHO WE WORK WITH (ICP)

**Layout:** 2 columns. Left: description. Right: qualification pills.

**Headline:** `Built for Growth-Stage Businesses Who Are Done With Average Results`

**Qualification pills:**

`$500K–$10M ARR` · `5–100 employees` · `Founder / CMO / Head of Growth` · `US, UK, CA, AU, UAE, DE, SG` · `Ready to invest in outcomes, not just activity`

**Industries:** SaaS & Tech · E-Commerce · Professional Services · Recruitment · Health & Wellness · Fintech · Real Estate · Education

---

## S11 · MARKETS [BLOCK: markets]

**Layout:** Flag + country + 1-line market note, in a row.

🇺🇸 **United States** — CCPA-aware · EST-aligned · AI-automation focus

🇬🇧 **United Kingdom** — GDPR-native · GMT-aligned · B2B SaaS & professional services

🇨🇦 **Canada** — CASL-compliant · EST/PST · Cross-border expansion

🇦🇺 **Australia** — Privacy Act · AEST-aligned · E-commerce & DTC

🇦🇪 **UAE** — PDPL-compliant · GST-aligned · Professional services & enterprise

🇩🇪 **Germany** — GDPR · Precision-led buyers · Engineering & SaaS

🇸🇬 **Singapore** — PDPA · APAC hub · High-growth tech

`[→ Find your market →]` → /markets

---

## S12 · FINAL CTA BANNER

**Layout:** Full-width dark section, centred.

**Headline:** `Ready to Build a Growth System That Actually Works?`

**Sub:** `Start with a free 30-minute strategy call. No pitch deck. No hard sell. Just an honest conversation about your goals.`

`[Book Your Free Strategy Call →]` → /book-a-call

`Trusted by growth-stage businesses in 🇺🇸 🇬🇧 🇨🇦 🇦🇺 🇦🇪 · Clients typically live within 5–7 business days`

---

# PAGE 2 — SERVICES HUB (/services)

**Goal:** Route every visitor to the right service in under 10 seconds.

**SEO intent:** "digital marketing agency" · "AI agency" · "full service digital agency"

## S1 · HERO

**H1:** `Everything Your Business Needs to Grow — Under One Roof`

**Sub:** `18 services. 4 categories. One accountable team. Built for growth-stage businesses scaling internationally.`

**CTA:** `[Explore Services ↓]` · `[Not Sure? Book a Call →]`

## S2 · 4-CATEGORY GRID

Large cards with icon, category name, service count, 1-line positioning, and "View Services →" link.

**🎯 Marketing (12 services)** — Full-funnel demand generation across search, social, content, and email. → /services/marketing

**🤖 Technology (3 services)** — AI automation, web development, and app builds on modern stacks. → /services/ai-automation

**🎨 Creative (2 services)** — Brand identity, design systems, and video production. → /services/graphic-design

**🙋 Operations (1 service)** — Trained virtual assistants working your timezone. → /services/virtual-assistant

## S3 · MARKETING SERVICES DETAIL

12-service grid. Each: icon + name + outcome-first 1-liner + link.

## S4 · TECHNOLOGY SERVICES DETAIL

3 service cards with fuller descriptions.

## S5 · CREATIVE & OPERATIONS

3 service cards.

## S6 · NOT SURE WHICH SERVICE?

**H2:** `Not sure where to start?`

**Body:** Most businesses need a combination of services. In a 30-minute call, we'll map the right services to your specific goals — no guesswork, no overselling.

`[Book a Free Strategy Call →]` → /book-a-call

## S7 · [BLOCK: stats-strip]

## S8 · [BLOCK: trust-bar]

---

# PAGE 3 — UNIVERSAL SERVICE PAGE TEMPLATE

**Applies to:** All 18 service pages. Same 18-section structure. Swap content per service.

**Goal:** Educate → build trust → capture the right lead.

## S1 · HERO

- Outcome-first H1 (not the service name)
- 2-sentence positioning
- Primary CTA (service-specific audit/consultation)
- Secondary CTA ("View [Service] Packages")
- Trust line: "Trusted by businesses in 🇺🇸 🇬🇧 🇨🇦 🇦🇺 🇦🇪"

## S2 · [BLOCK: trust-bar] — platform/tool logos for this service

## S3 · PROBLEMS WE SOLVE

- 6–8 specific pain points, bullet list, plain language
- Written in second-person ("You're...", "Your...")

## S4 · IS THIS RIGHT FOR YOU?

- **Strong fit if:** 4–5 qualifying statements
- **Not the right fit if:** 2–3 disqualifying statements (builds trust through honesty)

## S5 · SERVICES INCLUDED

Table: Service name | What's covered

## S6 · BUSINESS IMPACT STATS

4–6 industry stats proving the channel/service drives ROI. Always cited.

## S7 · WHY NIVY NEXT

4 differentiators specific to this service — not generic agency claims.

## S8 · OUR PROCESS

Numbered steps, 6 maximum. From engagement start to live/results.

## S9 · POPULAR USE CASES

3–4 mini case studies: [Industry | Market]: Problem → Approach → Result.

## S10 · DELIVERABLES CHECKLIST

Bulleted list of tangible outputs. Sets expectations, reduces objections.

## S11 · INDUSTRIES SERVED

Icon pills: SaaS · E-Commerce · Professional Services · Recruitment · Health · Finance · Education · Real Estate

## S12 · CASE STUDY PREVIEW [BLOCK: case-study-cards]

2 expanded case study cards for this specific service.

## S13 · TESTIMONIAL [BLOCK: testimonials]

1 testimonial, specific to this service. Role + company type + market flag + stars.

## S14 · TECHNOLOGY STACK

Table: Category | Tools (e.g. Research & Analysis | SEMrush, Ahrefs, Moz)

## S15 · PRICING

3-column table: 🔹 Starter | 🔷 Growth | 💠 Scale

Rows: Best For · Key deliverables · Volume · Reporting · Starting From

## S16 · FAQ

5–6 questions. Always include:

- "How quickly will I see results?"
- "Do I own the accounts/assets?"
- 3 service-specific questions

## S17 · RELATED SERVICES

3 cross-links with 1-line rationale for each pairing.

## S18 · FINAL CTA

- Strong problem-aware headline ("Your competitors are being found right now…")
- Primary CTA
- Secondary CTA

---

# PAGE 4 — RESULTS / CASE STUDIES (/results)

**Goal:** Eliminate the last objection before booking. Proof at scale.

**SEO intent:** "digital agency case studies" · "[service] results"

## S1 · HERO

**H1:** `Real Results. Real Businesses. No Made-Up Numbers.`

**[BLOCK: stats-strip]** — 4 aggregate stat cards above the fold.

## S2 · FILTER BAR

`Filter by: Service ▾ | Market ▾ | Industry ▾` — interactive, no page reload.

## S3 · FEATURED CASE STUDY (HERO CARD)

Full-width card: Market flag + industry + service + challenge (1 sentence) + key result metric (very large) + "Read Full Case Study →"

## S4 · CASE STUDY GRID

3-column grid. Each card:

- Market flag + industry + company size
- Service tag pills
- Challenge (1 sentence)
- **Key result (large, bold)**
- "Read Full Case Study →" link

**Minimum for launch:** 5 case studies (one per primary market: US, UK, AU, UAE, CA)

## S5 · [BLOCK: testimonials] — 3-carousel

## S6 · AGGREGATE PROOF

`X clients served · $Xm in client revenue influenced · X markets · 18 services`

## S7 · CTA

`[Book a Free Strategy Call →]` + `[Explore Our Services →]`

---

## CASE STUDY DETAIL PAGE TEMPLATE (/results/[slug])

**S1 · Snapshot Card** — Market + Industry + Company size + Services used + Timeline + Key metric

**S2 · Client Background** — Industry context, company stage, market

**S3 · The Challenge** — Specific problem in their language, not ours

**S4 · Our Approach** — Strategy rationale, why these services, why this order

**S5 · The Solution** — What we built/deployed, step by step

**S6 · Results** — Metrics with timeframes. Charts or stat cards where possible.

**S7 · Client Quote** — Attributed. Role + company type + market flag.

**S8 · Related Case Studies** — 3 cards from same industry or service

**S9 · CTA** — "See what we could do for your business →"

---

# PAGE 5 — ABOUT (/about)

**Goal:** Address the trust gap for international buyers. Who is this company?

**SEO intent:** "about nivy next" · "AI digital agency india" · "offshore digital agency reliable"

## S1 · HERO

**H1:** `We Exist Because Growing Businesses Deserve Better Than a Vendor List.`

**Sub:** One team. 18 capabilities. Five international markets. Built from the ground up to be an AI-native growth partner — not another agency you have to manage.

## S2 · THE SHORT VERSION

3 stat cards: Founded | Markets Served | Services Delivered

## S3 · COMPANY TIMELINE

Visual horizontal timeline: 2022 → 2023 → 2024 → 2025 → 2026.

Each node: year + one-sentence milestone.

## S4 · THE INDIA QUESTION (critical for Tier 1 trust)

**H2:** `Why do US, UK, and Australian businesses choose a team based in Lucknow, India?`

Address directly and confidently. 3 points:

1. World-class talent at 40–60% of local agency cost
2. Timezone-matched operations: EST · GMT · AEST business hours
3. AI-native infrastructure: faster, more consistent, more measurable than most local agencies

## S5 · MISSION / VISION / VALUES

Icons + name + 1-sentence description for each of the 6 values.

## S6 · TEAM

Photo grid: real photos mandatory. Name + role + 1-sentence specialist description.

**Minimum:** Founder + 2 heads of department.

## S7 · CERTIFICATIONS STRIP [BLOCK]

`Google Ads Certified | Meta Blueprint | HubSpot Partner | Semrush Agency | OpenAI API | AWS Activate | Make Certified`

## S8 · WHERE WE OPERATE [BLOCK: markets]

Flag + country + hours + compliance note.

## S9 · PRACTICAL CREDIBILITY BLOCK

- Response SLA: 24 business hours
- Onboarding: 5–7 business days
- Payment: Stripe · Wire · PayPal
- GDPR compliance: stated explicitly
- Governing law: England & Wales

## S10 · CTA

`[Book a Discovery Call →]` + `[View Our Results →]`

---

# PAGE 6 — PRICING (/pricing)

**Goal:** Eliminate price uncertainty. Pre-qualify budget. Reduce wasted discovery calls.

**SEO intent:** "digital marketing agency pricing" · "ai automation pricing"

## S1 · HERO

**H1:** `Transparent Pricing for Every Stage of Growth.`

**Sub:** No hidden fees. No lock-in surprises. Clear investment tied to clear outcomes. All prices in USD — GBP, AUD, CAD available on request.

## S2 · HOW IT WORKS

3 tier description cards: 🔹 Starter (month-to-month) · 🔷 Growth (3-month min) · 💠 Scale (3-month min, often 6)

Plus: ad spend note, account ownership note.

## S3 · MARKETING SERVICES TAB

Tabbed by sub-category. Each service = 3-column pricing table.

18 services total across 4 tabs: Marketing · Technology · Creative · Operations.

## S4 · GROWTH SYSTEMS BUNDLES

5 pre-packaged combinations. Table: Bundle name | Monthly fee | What's included | Replaces.

## S5 · ENTERPRISE & AI

No published figures. Range display. "Book a call" as the CTA.

## S6 · INTERNATIONAL RULES

USD pricing · GBP/AUD/CAD on request · Stripe/Wire/PayPal · 3-month min on Growth/Scale · Monthly in advance · No setup fees.

## S7 · PRICING FAQ

7 questions. Must include: ad spend question, refund question, currency question, contract length question.

## S8 · CTA

`[Not sure which plan? Book a free call →]` + `[See Our Results →]`

---

# PAGE 7 — BLOG / INSIGHTS (/blog)

**Goal:** Drive organic traffic. Build authority with international buyers.

**SEO intent:** AI marketing · international growth · B2B lead generation · digital strategy

## S1 · HERO

**H1:** `Insights for Growth-Stage Businesses Scaling Internationally.`

**Sub:** Strategic guides, AI explainers, and market-specific growth playbooks — for founders, CMOs, and operators.

## S2 · FILTER BAR

`Categories: AI & Automation · Digital Marketing · Growth Strategy · Market Insights · Case Studies`

`Markets: 🇺🇸 US · 🇬🇧 UK · 🇨🇦 CA · 🇦🇺 AU · 🇦🇪 UAE · All`

## S3 · FEATURED ARTICLE (HERO CARD)

Large card: image + category pill + market pill + title + 2-sentence excerpt + read time + author + CTA.

## S4 · ARTICLE GRID

3-column card layout. Each card: image · category tag · market tag · title · 1-line excerpt · read time · "Read More →"

## S5 · EMAIL CAPTURE

`[Subscribe for weekly growth insights →]` — name + email + market preference + GDPR checkbox.

---

## ARTICLE PAGE TEMPLATE (/blog/[slug])

**Structure:**

- Meta title (55–65 chars) + meta description (150–160 chars)
- Hero: Article title + author + date + category + read time
- Introduction: problem framing (hook within first 3 sentences)
- Body: H2/H3 structure, 1,500+ words, internal links to relevant service pages
- Conclusion + clear CTA linking to relevant service
- Author bio block
- Related articles (3 cards)
- Email capture widget

**5 Launch Articles:**

1. How AI Is Transforming B2B Lead Generation in 2026 — keyword: `ai lead generation b2b`
2. International Marketing Checklist: US & UK Market Readiness — keyword: `digital marketing international expansion`
3. Full-Funnel vs Channel Marketing: Which Is Right for You? — keyword: `full funnel marketing strategy`
4. Why SaaS Companies Need an AI-Native Growth Partner — keyword: `ai marketing agency saas`
5. How We Cut Recruitment Response Time From 48 Hours to 4 Minutes — keyword: `ai automation recruitment`

---

# PAGE 8 — CONTACT (/contact)

**Goal:** Reduce friction for anyone not ready for a direct call.

**SEO intent:** "contact nivy next" · "hire digital agency"

## S1 · HERO

**H1:** `Let's Talk About Your Growth.`

**Sub:** No sales pitch. No pressure. Tell us about your business and we'll tell you honestly whether we're the right fit.

## S2 · SPLIT LAYOUT

**Left (60%):** Contact form

- First Name · Last Name · Company · Country (dropdown) · Service Interest (18 options + "Not Sure") · Monthly Budget (6 ranges) · How did you hear? · Message · GDPR checkbox (required)
- Submit → "We'll respond within 24 business hours"

**Right (40%):** Contact details + trust signals

- Primary: [contact@thenivy.com](mailto:contact@thenivy.com) · +91 86705 43601
- Response SLA badge
- "What happens next" 3-step mini-process
- 1 testimonial [BLOCK]

## S3 · REGIONAL CARDS

4 cards: 🇺🇸 AMER · 🇬🇧 EMEA · 🇦🇪 MEASA · 🇦🇺 APAC

Each: regional email + hours + timezone.

## S4 · OFFICE HOURS TABLE

| Region | Timezone | Hours |
| --- | --- | --- |
| Americas | EST (UTC-5) | Mon–Fri, 9am–6pm |
| UK & Europe | GMT (UTC+0) | Mon–Fri, 9am–6pm |
| Middle East | GST (UTC+4) | Mon–Fri, 9am–6pm |
| Australia | AEST (UTC+10) | Mon–Fri, 9am–6pm |

## S5 · FAQ (CONTACT-SPECIFIC)

- How quickly will you respond?
- Can I just send an email instead?
- What happens after I submit the form?
- Do you work with companies outside your listed markets?

---

# PAGE 9 — BOOK A CALL (/book-a-call)

**Goal:** Remove all friction from the booking process. Maximum conversion.

**SEO intent:** "book strategy call digital agency" · "free marketing consultation"

## S1 · HERO

**H1:** `Book Your Free 30-Minute Strategy Call.`

**Sub:** No pitch decks. No hard sell. Just an honest conversation about your business, your goals, and whether we're the right team to help.

## S2 · SPLIT LAYOUT

**Left:** Calendly embed (connected to [contact@thenivy.com](mailto:contact@thenivy.com) · all timezone options shown)

**Right:**

- **What to expect on the call** (4 bullet points):
    1. We'll ask about your business, current challenges, and growth goals
    2. You'll get honest feedback on what's working and what isn't
    3. We'll recommend the right service combination for your stage
    4. If it's a fit, we'll outline next steps — no pressure either way
- **Trust signals:** Response within 24hrs · Most clients live 5–7 days post sign-off · Trusted in 🇺🇸 🇬🇧 🇨🇦 🇦🇺 🇦🇪
- **1 testimonial** specifically about the discovery call experience

## S3 · [BLOCK: stats-strip]

## S4 · [BLOCK: trust-bar]

---

# PAGE 10 — MARKETS HUB + INDIVIDUAL MARKET PAGES

## Hub page (/markets)

**H1:** `We Work Your Timezone, Your Compliance Standards, Your Market.`

Grid of 8 market cards. Each: flag + country + 1-line positioning + key compliance note + link.

---

## Individual Market Page Template (/markets/[country])

**Goal:** Capture country-specific search traffic. Build local credibility.

**SEO intent:** "digital marketing agency [country]" · "AI agency [city]"

**S1 · HERO**

`Nivy Next in [Country] — AI-Powered Growth for [Country] Businesses`

Sub: market-specific sub-positioning (different for each country)

`[Book a Strategy Call — [TZ] business hours]`

**S2 · WHY [COUNTRY] BUSINESSES CHOOSE US**

4 bullet points — market-specific advantages. Must include:

- Timezone alignment
- Compliance knowledge (GDPR / CCPA / CASL / Privacy Act / PDPL as applicable)
- Relevant case study reference
- Cost vs local agency comparison

**S3 · COMPLIANCE CALLOUT BOX**

Specific legislation for this market + how Nivy Next handles it.

| Country | Compliance |
| --- | --- |
| 🇬🇧 UK | UK GDPR + PECR |
| 🇺🇸 US | CCPA (California) + CAN-SPAM |
| 🇨🇦 Canada | CASL + PIPEDA |
| 🇦🇺 Australia | Privacy Act 1988 + Spam Act 2003 |
| 🇦🇪 UAE | UAE PDPL |
| 🇩🇪 Germany | GDPR + BDSG |
| 🇸🇬 Singapore | PDPA |
| 🇿🇦 South Africa | POPIA |

**S4 · CASE STUDY (MARKET-SPECIFIC)**

1 case study from this market (or nearest proxy until real one exists).

**S5 · SERVICES MOST USED IN [COUNTRY]**

3–5 service pills most relevant to this market's typical buyer profile.

**S6 · [BLOCK: testimonials]** — filtered to this market if possible.

**S7 · CTA**

`[Book a Free Strategy Call — [TZ] Business Hours]`

Contact: relevant regional email.

---

# PAGE 11 — INDUSTRIES HUB + INDIVIDUAL INDUSTRY PAGES

## Hub page (/industries)

**H1:** `We Know Your Industry. Not Just Your Channel.`

Grid of 8 industry cards. Each: icon + industry name + service stack summary + link.

---

## Individual Industry Page Template (/industries/[industry])

**Goal:** Convert industry-specific search traffic. Show vertical depth.

**SEO intent:** "digital marketing agency for [industry]" · "AI automation [industry]"

**S1 · HERO**

`[Industry] Growth — Built by People Who Know Your Sector`

Sub: 1-sentence that names the specific challenge this industry faces.

**S2 · INDUSTRY-SPECIFIC PAIN POINTS**

4 pain points written from inside the industry's world. Not generic.

**S3 · RECOMMENDED SERVICE STACK**

For this industry, which 3–5 services work best together and why.

**S4 · INDUSTRY CASE STUDY**

1 full case study from this industry. Format: [BLOCK: case-study-detail]

**S5 · [BLOCK: testimonials]** — filtered to this industry.

**S6 · INDUSTRY FAQ**

4–5 questions buyers in this specific industry always ask. Not generic FAQ.

**S7 · RELATED INDUSTRIES**

3 cards: "Businesses in [adjacent industry] also work with us for..."

**S8 · CTA**

---

# REUSABLE CONTENT BLOCKS LIBRARY

Build these once in your CMS. Reference by block name anywhere in the site.

| Block Name | Contents | Used On |
| --- | --- | --- |
| `[BLOCK: trust-bar]` | Tool/platform logos + market flags + certifications | Homepage, all service pages, about |
| `[BLOCK: stats-strip]` | 4 aggregate stat cards | Homepage, results, book-a-call |
| `[BLOCK: process]` | 6-step delivery timeline | Homepage, about, service pages |
| `[BLOCK: case-study-cards]` | 3 filterable case study preview cards | Homepage, service pages, results |
| `[BLOCK: testimonials]` | 3-card rotating carousel | Homepage, about, contact, service pages |
| `[BLOCK: markets]` | 8 flag cards with market-specific notes | Homepage, about, footer |
| `[BLOCK: certifications]` | Certification badge strip | About, service pages |
| `[BLOCK: cta-banner]` | Full-width conversion CTA section | Every page bottom |
| `[BLOCK: pricing-table]` | 3-tier pricing table template | All service pages, pricing page |
| `[BLOCK: faq]` | Expandable accordion | All service pages, contact, pricing |

---

# TIER 1 / TIER 2 TRUST REQUIREMENTS BY PAGE

Every page must pass all applicable checks before publish:

## Tier 1 (US, UK, Canada, Australia, Germany, Netherlands, Singapore, Ireland, NZ)

- [ ]  GDPR/CCPA/CASL/Privacy Act compliance language present where forms appear
- [ ]  Governing law stated (England & Wales)
- [ ]  No placeholder emails or phone numbers
- [ ]  Response SLA stated and realistic
- [ ]  Pricing in USD with GBP/AUD available on request
- [ ]  Testimonials include role, company type, and country flag
- [ ]  Case studies have real numbers and a stated timeframe
- [ ]  No vague outcome claims ("improve your results") — every claim is specific
- [ ]  Team has real names and faces (faceless agencies don't win Tier 1 enterprise)
- [ ]  Payment via Stripe or wire transfer (PayPal acceptable as secondary)
- [ ]  SSL certificate + cookie consent banner active
- [ ]  Page speed: Lighthouse score >90 on mobile

## Tier 2 (UAE, India enterprise, South Africa, Malaysia, Brazil, Poland, Portugal)

- [ ]  UAE/PDPL note present on market page and contact form
- [ ]  GST timezone stated for UAE-specific pages
- [ ]  Pricing context: "40–60% of local agency cost" message present on About and market pages
- [ ]  WhatsApp contact option present (Tier 2 buyers often prefer it)
- [ ]  Currency context: USD pricing is expected and acceptable — confirm on pricing page
- [ ]  Case studies include at least 1 from the UAE or relevant Tier 2 market
- [ ]  Arabic/regional language option flagged for UAE if budget allows (not mandatory for launch)

---

# SEO ARCHITECTURE SUMMARY

## Page-Level Keyword Targets

| Page | Primary Keyword | Secondary Keywords |
| --- | --- | --- |
| / | ai digital agency | full service digital agency, digital marketing agency |
| /services | digital marketing services | online marketing services, marketing agency services |
| /services/seo | seo agency | seo services, seo company, search engine optimisation |
| /services/ppc | ppc agency | google ads agency, paid search management |
| /services/social-media-marketing | social media marketing agency | smm agency, social media management |
| /services/social-media-advertising | paid social media agency | meta ads agency, facebook ads agency |
| /services/content-marketing | content marketing agency | content writing services, blog writing agency |
| /services/email-marketing | email marketing agency | email automation, klaviyo agency |
| /services/linkedin-marketing | linkedin marketing agency | linkedin lead generation, b2b linkedin agency |
| /services/video-marketing | video marketing agency | youtube marketing, video strategy |
| /services/ecommerce-marketing | ecommerce marketing agency | shopify marketing, dtc marketing |
| /services/cro | conversion rate optimisation agency | cro services, landing page optimisation |
| /services/ai-automation | ai automation agency | business process automation, ai marketing |
| /services/website-development | website development agency | web design agency, next.js development |
| /services/app-development | app development agency | mobile app development, flutter agency |
| /markets/uk | digital marketing agency uk | marketing agency london, uk seo agency |
| /markets/us | digital marketing agency usa | us marketing agency, american digital agency |
| /markets/australia | digital marketing agency australia | australian seo agency, sydney digital agency |
| /markets/uae | digital marketing agency dubai | uae marketing agency, dubai digital agency |
| /industries/saas | digital marketing agency for saas | saas growth agency, b2b saas marketing |
| /industries/ecommerce | ecommerce marketing agency | shopify agency, dtc growth agency |

## Technical SEO Requirements

- Sitemap: auto-generated, submitted to Google Search Console
- Robots.txt: configured correctly
- hreflang: not required at launch (single English site), add when second-language versions built
- Schema markup: Organization + WebSite on homepage; Article on blog posts; FAQPage on service pages
- Core Web Vitals: LCP <2.5s · FID <100ms · CLS <0.1 — all green before launch
- Internal linking: every service page links to 2–3 related services + 1 case study
- Canonical tags: all pages self-canonical
- 301 redirects: map if migrating from old site structure

---

# LEGAL PAGES (/legal/*)

## /privacy-policy

- GDPR-structured (UK/EU standard — covers all Tier 1 markets)
- All data processors named: Calendly, GA4, HubSpot, Stripe, Cloudflare
- UK/EU data subject rights: Access · Rectification · Erasure · Portability · Object · Restrict
- Cookie section: categories + opt-out instructions
- Last updated date: set on publish

## /terms-of-service

- Governing law: England & Wales
- Payment terms, IP ownership, confidentiality, limitation of liability, termination (30-day notice)
- Payment methods stated: Stripe, Wire, PayPal
- Solicitor review recommended before launch

## /cookie-policy

- Cookie categories: Strictly Necessary · Analytics · Marketing · Preferences
- Third-party cookies listed: Google Analytics, Meta Pixel, Hotjar, HubSpot
- Opt-out mechanism linked (cookie consent banner)

## /gdpr

- GDPR rights explained in plain English
- Data request form or mailto: link
- DPO contact (or Founder as contact) stated
- Retention periods stated per data category

---

# LAUNCH READINESS CHECKLIST

## Technical

- [ ]  Domain and SSL configured
- [ ]  Cookie consent banner live and functional (accept/decline/preferences)
- [ ]  All forms connected to CRM or inbox
- [ ]  GA4 tracking verified
- [ ]  Meta Pixel installed (if running paid social)
- [ ]  Calendly embed live and tested on mobile
- [ ]  All 404s resolved
- [ ]  Sitemap submitted
- [ ]  Core Web Vitals all green
- [ ]  Page speed: Lighthouse >90 mobile

## Content

- [ ]  Zero placeholder text, emails, or phone numbers
- [ ]  All team photos real (not stock)
- [ ]  All testimonials attributed (role + company type + market)
- [ ]  All case study numbers verified
- [ ]  Privacy Policy last-updated date set
- [ ]  Governing law confirmed and solicitor-reviewed
- [ ]  Pricing tiers confirmed by Founder
- [ ]  GDPR consent checkbox on every form

## Conversion

- [ ]  Calendly tested across US/UK/AU timezones
- [ ]  Auto-reply emails active for all forms
- [ ]  WhatsApp Business number active
- [ ]  Mobile layout tested on iOS and Android
- [ ]  Primary CTA visible above fold on all key pages
- [ ]  Trust bar visible on homepage and service pages