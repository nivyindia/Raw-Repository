# 📊 Analytics & Tracking Setup Plan — GA4, GTM, GSC, Clarity

**Status:** ✅ Drafted (Claude improvement pass, June 2026) — ready for dev/marketing handoff

**Covers:** Phase D1–D4 (Analytics & Tag Setup, Google Search Console, Core Web Vitals, CRO Baseline Targets)

**Hard rule:** Install all tracking *before* launch, not after. Retroactive tracking means losing your entire launch-window data — the highest-traffic, highest-curiosity period the site will ever have.

---

# D1. Analytics & Tag Setup

## Stack

- **Google Analytics 4 (GA4)** — core analytics, installed via Google Tag Manager (not hardcoded) so tags can be managed without a dev redeploy
- **Google Tag Manager (GTM)** — container for GA4 + Meta Pixel + LinkedIn Insight Tag
- **Meta Pixel** — for paid social retargeting, if/when paid campaigns run
- **LinkedIn Insight Tag** — B2B audience is a meaningful share of ICP (founders, CFOs); LinkedIn ad retargeting and conversion tracking matters more here than for a typical consumer site
- **Microsoft Clarity** — free heatmaps/session recordings (see D4)

## Conversion Events to Map in GTM/GA4

| Event Name | Trigger | Why It Matters |
| --- | --- | --- |
| `form_submit` | Contact form or quick-contact form submitted | Primary lower-intent conversion |
| `calendly_booking` | Booking widget completes a scheduled call | Primary high-intent conversion |
| `pdf_download` | Tax deadline calendar or gated guide downloaded | Lead magnet conversion — segment by country/guide |
| `phone_click` | Click-to-call link tapped (mobile primarily) | High-intent micro-conversion |
| `email_click` | mailto: link clicked | Lower-intent micro-conversion |
| `pricing_tier_click` | "Get Started" clicked on a specific pricing tier | Tells you which tier visitors self-select before talking to a human |
| `country_page_view` | Any country page viewed | Feeds the geo-audience segmentation below |

## GA4 Audiences to Build

- **By geography:** segment by which country page(s) a visitor viewed — tells you which markets are generating organic interest vs. which need more SEO/content investment
- **By page path / service interest:** segment by which service page(s) a visitor viewed (CPA & Tax vs. Bookkeeping vs. Advisory vs. Compliance)
- **Cross-reference both:** a visitor who views the UAE page *and* the Compliance & Entity Setup page is a much hotter lead than either signal alone — worth a custom audience for retargeting

---

# D2. Google Search Console

## Pre-Launch Checklist

- [ ]  Verify domain ownership in GSC (DNS or HTML tag method — DNS preferred, survives site rebuilds)
- [ ]  Submit XML sitemap on launch day (auto-generated; confirm it includes all Phase 1 pages and excludes legal/utility pages from priority crawl)
- [ ]  Set country targeting per subdirectory under GSC International Targeting settings, matching the URL structure already confirmed in the SEO sub-page (`/countries/united-states/`, etc.)

## Ongoing Monitoring (from Day 1)

- **Crawl errors** — weekly check for the first month, monthly after
- **Index coverage** — confirm all Phase 1 pages are indexed within 2–3 weeks of launch; flag anything stuck in "Discovered — not indexed"
- **Core Web Vitals report** — GSC surfaces field data (real user data) distinct from the Lighthouse lab data in D3 below; both matter

---

# D3. Core Web Vitals Checklist (for Dev)

| Metric | Target | Common Fix |
| --- | --- | --- |
| LCP (Largest Contentful Paint) | < 2.5s | Compress and correctly lazy-load hero images; avoid render-blocking fonts |
| CLS (Cumulative Layout Shift) | < 0.1 | Reserve image/ad space with explicit width/height; avoid late-loading fonts that shift layout |
| INP (Interaction to Next Paint) | < 200ms | Avoid heavy JS execution on page load; defer non-critical scripts (chat widgets, pixels) |

**Process:** Run a Lighthouse audit on every Phase 1 page before go-live — not just Home. Country pages and the Pricing page (table-heavy, form-heavy) are the most likely to fail CWV thresholds and are exactly the pages where a slow load costs a qualified lead.

---

# D4. CRO Baseline Targets

## Targets to Set Before Launch (so "good" and "bad" mean something from week one)

| Funnel Step | Target Conversion Rate |
| --- | --- |
| Home → Book a Call | 2–3% |
| Country page → any CTA | 1.5–2% |
| Blog → Email capture (lead magnet) | 3–5% |

**Why set these now instead of after launch:** without a baseline, the team has no way to tell whether month-one performance is healthy or concerning — every number looks fine in isolation. These targets are directional industry benchmarks for professional-services lead gen, not guarantees; revisit after the first full month of real data.

## Tooling

- **Microsoft Clarity** installed on launch day — free heatmaps and session recordings, no budget justification needed to turn it on
- **Monthly CRO review** covering: top 5 pages by traffic, average scroll depth per page type, CTA click-through rate by page

## First Monthly Review Should Answer

1. Which country pages are getting traffic but not converting? (Signals a messaging or trust gap, not a traffic gap.)
2. Where does scroll depth drop off sharply? (Signals a section that isn't earning attention — candidate for re-ordering or cutting.)
3. Is the lead magnet (tax deadline calendar) actually pulling its weight as a secondary CTA, or is everyone ignoring it in favor of the primary?

---

> **Cross-reference:** Conversion event names above should match the CTA inventory in 🎯 CTA Hierarchy & Mobile-First Design Brief. Hand both pages to dev together — tracking and CTA placement are designed as one system, not two separate workstreams.
>