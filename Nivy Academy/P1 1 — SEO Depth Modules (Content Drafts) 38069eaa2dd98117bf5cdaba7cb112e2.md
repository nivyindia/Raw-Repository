# P1.1 — SEO Depth Modules (Content Drafts)

> **Status:** 🟡 In Progress | **Phase:** 1 — Depth Enhancement | **Parent Task Group:** P1.1 SEO
> 

This page contains detailed module content drafts for each P1.1 task. Once a module's LMS upload, assignment/quiz, and recording are complete, update its status in the [main plan](Course%20improvement%20plan%202%201%2038069eaa2dd980ebac15e1851d74dc99.md) table from 🔴 Pending to 🟡 In Progress to ✅ Done.

---

## P1.1.1 — Core Web Vitals 🟡 In Progress

**Add full module on Core Web Vitals — LCP, CLS, FID/INP — with hands-on PageSpeed and Screaming Frog walkthroughs**

### Learning Objectives

- Understand the three Core Web Vitals metrics and why Google uses them as ranking signals
- Diagnose performance issues on a live website using free tools
- Recommend and implement fixes for common Core Web Vitals failures

### Theory (40 min)

1. What are Core Web Vitals and why they matter for SEO and UX
2. **LCP (Largest Contentful Paint)** — what it measures, thresholds (≤2.5s good / ≤4s needs improvement / >4s poor), common causes (slow server response, render-blocking resources, large images)
3. **CLS (Cumulative Layout Shift)** — visual stability (≤0.1 good), common causes (images without dimensions, late-injected ads/embeds, web font FOIT/FOUT)
4. **INP (Interaction to Next Paint)** — replaced FID in March 2024, measures responsiveness (≤200ms good), common causes (heavy JS execution, long tasks)

### Hands-On Demo (30 min)

1. **PageSpeed Insights walkthrough** — run a live URL, interpret field data vs lab data, prioritise Opportunities and Diagnostics sections
2. **Screaming Frog walkthrough** — crawl a site, pull Core Web Vitals data via PageSpeed Insights API integration, export a site-wide report
3. **Chrome DevTools Lighthouse panel** — run an audit, read the waterfall chart for LCP/CLS culprits

### Student Assignment

Pick any live website (own, client, or assigned). Run PageSpeed Insights + Screaming Frog crawl. Produce a 1-page Core Web Vitals audit report identifying the top 3 issues and recommended fixes.

### Resources to Create

- [ ]  PageSpeed Insights interpretation cheat sheet (PDF)
- [ ]  Screaming Frog Core Web Vitals setup guide (step-by-step with screenshots)
- [ ]  Sample audit report template (Google Doc/Notion)

---

## P1.1.2 — Schema Markup & Structured Data 🔴 Pending

**Add Schema Markup & Structured Data — JSON-LD, Rich Snippets, FAQ schema, Product schema**

### Learning Objectives

- Understand what structured data is and how Google uses it for rich results
- Write valid JSON-LD for common schema types
- Validate and troubleshoot schema implementations

### Theory (30 min)

1. What is structured data and [Schema.org](http://Schema.org) vocabulary
2. JSON-LD vs Microdata vs RDFa — why JSON-LD is preferred
3. Common schema types: Organization, Article, FAQ, Product, Review, BreadcrumbList, LocalBusiness
4. How rich snippets appear in SERPs and their CTR impact

### Hands-On Demo (30 min)

1. Writing JSON-LD by hand for an Article and FAQ page
2. Using Google's Rich Results Test and Schema Markup Validator
3. Implementing schema via Yoast/RankMath (WordPress) and manual `<script>` injection

### Student Assignment

Add FAQ schema and Product schema to a sample page; validate with Rich Results Test; submit screenshots of passing validation.

### Resources to Create

- [ ]  JSON-LD code snippet library (Article, FAQ, Product, LocalBusiness, BreadcrumbList)
- [ ]  Schema validation checklist

---

## P1.1.3 — NLP & Semantic SEO 🔴 Pending

**Add NLP & Semantic SEO — Entity-based SEO, topic clusters, content hubs, TF-IDF**

### Learning Objectives

- Understand how Google's NLP models (BERT/MUM) interpret content
- Build topic clusters and content hubs around pillar pages
- Use TF-IDF analysis to identify content gaps

### Theory (30 min)

1. Entity-based SEO — entities vs keywords, Knowledge Graph
2. Topic clusters — pillar page + cluster content + internal linking model
3. TF-IDF — what it measures and how tools use it for content optimisation

### Hands-On Demo (30 min)

1. Building a topic cluster map for a sample niche
2. Running TF-IDF analysis with a free tool and comparing top-ranking pages
3. Internal linking structure walkthrough

### Student Assignment

Create a topic cluster map (1 pillar + 5 cluster topics) for an assigned niche, with proposed internal linking structure.

### Resources to Create

- [ ]  Topic cluster map template (Notion/Miro)
- [ ]  TF-IDF tool comparison sheet

---

## P1.1.4 — International & Multilingual SEO 🔴 Pending

**Add International & Multilingual SEO — hreflang tags, geo-targeting, international site architecture**

### Learning Objectives

- Implement hreflang correctly for multi-language/region sites
- Choose the right international site architecture (ccTLD vs subdomain vs subdirectory)
- Configure geo-targeting in Google Search Console

### Theory (25 min)

1. hreflang syntax and common mistakes (missing return tags, wrong language codes)
2. Site architecture options and trade-offs
3. Geo-targeting vs language-targeting — clearing up the confusion

### Hands-On Demo (25 min)

1. Writing hreflang tags for a 3-language site
2. Validating hreflang with a free checker tool
3. Search Console international targeting settings walkthrough

### Student Assignment

Draft an hreflang implementation plan for a hypothetical site targeting India (English/Hindi) and UK (English).

### Resources to Create

- [ ]  hreflang syntax cheat sheet
- [ ]  International SEO architecture decision tree

---

## P1.1.5 — AI-Powered SEO 🔴 Pending

**Add AI-Powered SEO — using ChatGPT for keyword clustering, SurferSEO, Frase, NeuronWriter**

### Learning Objectives

- Use AI tools to accelerate keyword research and content briefs
- Understand AI content optimisation scoring (SurferSEO/Frase/NeuronWriter)
- Avoid over-reliance on AI-detectable, low-value content

### Theory (20 min)

1. Where AI helps in SEO workflows: clustering, briefs, gap analysis, meta writing
2. How content scoring tools work (NLP term frequency vs top-ranking pages)
3. Risks: AI content quality, Google's stance on AI-generated content (helpful content guidelines)

### Hands-On Demo (40 min)

1. ChatGPT prompt workflow for keyword clustering from a raw keyword export
2. SurferSEO or NeuronWriter content editor walkthrough — writing to a target score
3. Frase content brief generation demo

### Student Assignment

Take a list of 30 raw keywords, cluster them using an AI prompt template, and produce one content brief using a content optimisation tool.

### Resources to Create

- [ ]  Keyword clustering prompt template
- [ ]  Content brief template

---

## P1.1.6 — E-E-A-T Deep Dive 🔴 Pending

**Add E-E-A-T Deep Dive — Experience, Expertise, Authoritativeness, Trust and how Google evaluates it**

### Learning Objectives

- Explain each component of E-E-A-T and why it was added
- Audit a website/page for E-E-A-T signals
- Implement practical E-E-A-T improvements

### Theory (30 min)

1. Breakdown of Experience, Expertise, Authoritativeness, Trust
2. How E-E-A-T relates to YMYL (Your Money or Your Life) content
3. On-page and off-page signals Google associates with E-E-A-T (author bios, citations, reviews, HTTPS, about/contact pages)

### Hands-On Demo (20 min)

1. E-E-A-T audit walkthrough on a real page
2. Writing an effective author bio with credentials

### Student Assignment

Audit an assigned webpage against an E-E-A-T checklist and propose 5 concrete improvements.

### Resources to Create

- [ ]  E-E-A-T audit checklist
- [ ]  Author bio template

---

## P1.1.7 — Programmatic & Scalable SEO 🔴 Pending

**Add Programmatic & Scalable SEO — auto-generating landing pages, FAQ pages, location pages at scale**

### Learning Objectives

- Understand programmatic SEO concepts and when to use it
- Design a template + data-source model for scalable pages
- Avoid thin-content and duplicate-content pitfalls

### Theory (25 min)

1. What is programmatic SEO and example use cases (location pages, comparison pages, FAQ pages)
2. Template design — variable fields, unique value-adds per page
3. Risks: thin content, index bloat, quality guidelines

### Hands-On Demo (35 min)

1. Building a simple location-page template using a spreadsheet + template merge (Google Sheets + Looker Studio/no-code tool)
2. Reviewing real-world programmatic SEO examples

### Student Assignment

Design a programmatic page template (with at least 5 variable fields) for a hypothetical multi-location business, and generate 3 sample pages.

### Resources to Create

- [ ]  Programmatic SEO template framework
- [ ]  Quality checklist to avoid thin content

---

## P1.1.8 — Video SEO 🔴 Pending

**Add Video SEO — YouTube ranking, transcript optimisation, video schema, embedding strategy**

### Learning Objectives

- Optimise YouTube videos for search and suggested placements
- Add transcripts and video schema to embedded videos
- Build an embedding strategy that boosts both YouTube and website SEO

### Theory (20 min)

1. YouTube ranking factors: title, description, tags, watch time, CTR
2. Transcript optimisation and accessibility benefits
3. VideoObject schema for embedded videos

### Hands-On Demo (30 min)

1. Optimising a sample YouTube video listing (title/description/tags)
2. Adding VideoObject schema to a webpage embed
3. Transcript generation and formatting demo

### Student Assignment

Optimise the metadata for one YouTube video (real or sample) and write VideoObject schema for embedding it on a webpage.

### Resources to Create

- [ ]  YouTube metadata optimisation checklist
- [ ]  VideoObject schema snippet template

---

## P1.1.9 — Expand Technical SEO 🔴 Pending

**Expand Technical SEO — Robots.txt, XML Sitemaps, Crawl Budget, Canonicals, Redirect Chains, Log File Analysis**

### Learning Objectives

- Configure robots.txt and XML sitemaps correctly
- Understand crawl budget and how to optimise it
- Diagnose and fix canonical and redirect issues using log files

### Theory (35 min)

1. robots.txt syntax, common mistakes, and testing
2. XML sitemap best practices (segmentation, priority, lastmod)
3. Crawl budget — what affects it and how to monitor via Search Console
4. Canonical tags — correct usage and common conflicts
5. Redirect chains — why they're harmful and how to map them
6. Log file analysis — what it reveals that Search Console doesn't

### Hands-On Demo (35 min)

1. Auditing robots.txt and sitemap.xml for a live site
2. Screaming Frog redirect chain report walkthrough
3. Basic log file analysis using Screaming Frog Log File Analyser

### Student Assignment

Audit a live site's robots.txt, sitemap, and redirect chains; produce a technical SEO findings report with prioritised fixes.

### Resources to Create

- [ ]  Technical SEO audit template
- [ ]  Log file analysis quick-start guide

---

## P1.1.10 — SEO Reporting 🔴 Pending

**Add SEO Reporting — building live rank-tracking dashboards in Looker Studio + SEMrush**

### Learning Objectives

- Connect SEMrush and Search Console data to Looker Studio
- Build a live SEO performance dashboard
- Present SEO results to non-technical stakeholders

### Theory (15 min)

1. What to report: rankings, traffic, impressions/CTR, backlinks, technical health
2. Audience-appropriate reporting (client vs internal team)

### Hands-On Demo (45 min)

1. Connecting Search Console and GA4 to Looker Studio
2. Connecting SEMrush data via connector/export
3. Building a multi-page dashboard: overview, keyword rankings, technical health

### Student Assignment

Build a 3-page Looker Studio SEO dashboard for an assigned domain using Search Console and SEMrush data.

### Resources to Create

- [ ]  Looker Studio SEO dashboard template (copyable)
- [ ]  Client-facing SEO report template

---

> **Next:** Once these 10 modules are uploaded to LMS with assignments/quizzes/recordings, mark each ✅ Done in the main plan's P1.1 table and update the Phase 1 summary count (0/60 → 10/60).
>