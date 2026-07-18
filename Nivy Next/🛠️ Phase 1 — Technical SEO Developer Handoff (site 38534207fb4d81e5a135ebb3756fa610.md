# 🛠️ Phase 1 — Technical SEO Developer Handoff (sitemap, robots.txt, hreflang, OG tags)

> This is the developer handoff package for Phase 1 (Technical SEO Foundation). Everything below is ready to paste/configure — it cannot be "done" by Claude directly since it requires access to the live [thenivy.com](http://thenivy.com) hosting/CMS, which I don't have. Hand this page to whoever has WordPress/server access.
> 

---

# 1.1 — robots.txt

```
User-agent: *
Allow: /
Disallow: /admin
Disallow: /dashboard
Disallow: /wp-admin
Disallow: /*?*utm_
Disallow: /thank-you
Disallow: /book-a-call-confirmation

Sitemap: https://www.thenivy.com/sitemap.xml
```

---

# 1.1 — XML Sitemap Structure

*If using RankMath/Yoast on WordPress, the sitemap generates automatically at `/sitemap_index.xml` — just confirm these URL groups are included and the exclusions below are respected.*

**Include:** all 18 service pages, 7 hub/core pages (Home, Services Hub, Marketing Hub, About, Results, Pricing, Blog), Contact, Book a Call, FAQ, all 5 market pages + hub, all 5 industry pages + hub, all blog articles, Privacy Policy, Terms of Service, Refund & Cancellation Policy.

**Exclude:** `/thank-you`, `/book-a-call` confirmation step, any `/admin` or `/dashboard` routes, any staging subdomain.

---

# 1.3 — hreflang Block (add to `<head>` on every core page)

```html
<link rel="alternate" hreflang="en-gb" href="https://www.thenivy.com/markets/uk" />
<link rel="alternate" hreflang="en-us" href="https://www.thenivy.com/markets/us" />
<link rel="alternate" hreflang="en-ca" href="https://www.thenivy.com/markets/canada" />
<link rel="alternate" hreflang="en-au" href="https://www.thenivy.com/markets/australia" />
<link rel="alternate" hreflang="en-ae" href="https://www.thenivy.com/markets/uae" />
<link rel="alternate" hreflang="x-default" href="https://www.thenivy.com/" />
```

Apply to: Homepage, all 7 service category pages, About, Pricing, Blog index.

---

# 1.6 — Open Graph + Twitter Card Template

```html
<meta property="og:title" content="{{PAGE_META_TITLE}}" />
<meta property="og:description" content="{{PAGE_META_DESCRIPTION}}" />
<meta property="og:image" content="{{1200x630_IMAGE_URL}}" />
<meta property="og:url" content="{{CANONICAL_URL}}" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{{PAGE_META_TITLE}}" />
<meta name="twitter:description" content="{{PAGE_META_DESCRIPTION}}" />
<meta name="twitter:image" content="{{1200x630_IMAGE_URL}}" />
```

**Still needed (design task, not yet done):** one branded default OG image (1200×630) for pages without a unique hero, plus unique OG images for Homepage, About, all 5 blog articles, all 5 market pages.

---

# Pre-Launch Checklist (Developer-Owned — needs live site access)

- [ ]  SSL active, zero mixed-content warnings
- [ ]  www vs non-www standardised with 301 redirect
- [ ]  Custom branded 404 page (links to Home / Services / Contact)
- [ ]  Canonical tags self-referencing on every page
- [ ]  Cloudflare CDN connected (free plan) — critical given India-origin hosting serving UK/US traffic
- [ ]  Images converted to WebP, lazy-loaded below the fold
- [ ]  Calendly/chat widgets loaded on-demand, not on initial paint
- [ ]  Lighthouse run on Homepage, 1 service page, About, Pricing — target >90
- [ ]  GSC + GA4 verified and linked
- [ ]  Sitemap submitted to GSC

> 📅 **Created:** 20 June 2026. Pairs with the 🧩 SEO Schema Markup Library for the full Phase 1 + 2.6 technical package.
>