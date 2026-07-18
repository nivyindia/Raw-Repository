# 🧩 SEO Schema Markup Library (JSON-LD — Ready to Implement)

> ⚠️ **Status correction (20 June 2026):** The Master Plan marked these as "✅ written" but no actual files existed anywhere in Notion or Google Drive. This page is the real, first-time-created deliverable. All blocks below are ready to paste into RankMath (per-page Schema Editor) or `functions.php` for sitewide blocks.
> 

> 
> 

> **⚠️ Critical data-accuracy flag:** The "4 regional HQ" addresses in the Master Business Profile System (Section 15) use placeholder emails (`amer.hq@yourcompany.com` etc — note "[yourcompany.com](http://yourcompany.com)", not [thenivy.com](http://thenivy.com)). These read as **template placeholders, not confirmed real offices**. I have used them as drafts below but **DO NOT PUBLISH the LocalBusiness schema until Abhi confirms which of these addresses are real, physical, mail-receivable offices** — publishing false LocalBusiness/NAP data is a Google Business guideline violation and can get a profile suspended.
> 

---

# 1. Organization + WebSite Schema (Sitewide)

*Add via `functions.php` or RankMath Global Schema. Replace `REPLACE_LOGO_URL` and `REPLACE_SOCIAL_URLS` before publishing.*

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.thenivy.com/#organization",
      "name": "Nivy Next",
      "url": "https://www.thenivy.com",
      "logo": "REPLACE_LOGO_URL",
      "email": "contact@thenivy.com",
      "description": "Nivy Next is an AI-first digital services company helping growth-stage businesses across the US, UK, Canada, Australia, and UAE scale through marketing, AI automation, and full-stack digital execution.",
      "sameAs": [
        "REPLACE_LINKEDIN_URL",
        "REPLACE_INSTAGRAM_URL",
        "REPLACE_TWITTER_URL"
      ],
      "contactPoint": [
        { "@type": "ContactPoint", "contactType": "customer service", "email": "contact@thenivy.com", "areaServed": ["US","GB","CA","AU","AE"], "availableLanguage": ["English"] }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.thenivy.com/#website",
      "url": "https://www.thenivy.com",
      "name": "Nivy Next",
      "publisher": { "@id": "https://www.thenivy.com/#organization" },
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://www.thenivy.com/?s={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
  ]
}
```

---

# 2. Homepage WebPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://www.thenivy.com/#webpage",
  "url": "https://www.thenivy.com/",
  "name": "AI Digital Marketing Agency for International Growth | Nivy Next",
  "description": "Nivy Next is an AI-first digital agency helping growth-stage businesses in the US, UK, Canada, Australia & UAE scale through marketing, AI automation, and development.",
  "isPartOf": { "@id": "https://www.thenivy.com/#website" },
  "about": { "@id": "https://www.thenivy.com/#organization" },
  "inLanguage": "en"
}
```

---

# 3. Service Schema — Template + Data Table for All 18 Service Pages

*Apply this template per service page in RankMath, swapping in the row values from the table below.*

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{{SERVICE_NAME}}",
  "name": "{{SERVICE_NAME}} | Nivy Next",
  "description": "{{SERVICE_META_DESCRIPTION}}",
  "provider": { "@id": "https://www.thenivy.com/#organization" },
  "areaServed": ["United States","United Kingdom","Canada","Australia","United Arab Emirates"],
  "url": "https://www.thenivy.com/{{SERVICE_SLUG}}"
}
```

| Slug | Service Name |
| --- | --- |
| /services/seo | SEO |
| /services/ppc | PPC Management |
| /services/social-media-marketing | Social Media Marketing |
| /services/social-media-advertising | Social Media Advertising |
| /services/content-marketing | Content Marketing |
| /services/email-marketing | Email Marketing |
| /services/linkedin-marketing | LinkedIn Marketing |
| /services/video-marketing | Video Marketing |
| /services/local-business-marketing | Local Business Marketing |
| /services/ecommerce-marketing | Ecommerce Marketing |
| /services/cro | Conversion Rate Optimisation |
| /services/marketing-analytics | Marketing Analytics |
| /services/ai-automation | AI Solutions & Automation |
| /services/website-development | Website Development |
| /services/app-development | App Development |
| /services/graphic-design | Graphic Design |
| /services/video-production | Video Production |
| /services/virtual-assistant | Virtual Assistant Services |

---

# 4. Article Schema — Template (for all future blog posts)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{ARTICLE_TITLE}}",
  "description": "{{META_DESCRIPTION}}",
  "image": "{{HERO_IMAGE_URL}}",
  "author": { "@type": "Person", "name": "FOUNDER_NAME", "url": "REPLACE_LINKEDIN_PROFILE_URL" },
  "publisher": { "@id": "https://www.thenivy.com/#organization" },
  "datePublished": "{{ISO_DATE}}",
  "dateModified": "{{ISO_DATE}}",
  "mainEntityOfPage": "{{ARTICLE_URL}}"
}
```

## Prefilled — All 5 Existing Articles

`*FOUNDER_NAME` and image URLs still need replacing — flagged, not guessed.*

```json
[
  {"headline":"How AI Is Transforming B2B Lead Generation in 2026","url":"/blog/how-ai-is-transforming-b2b-lead-generation-2026","author":"FOUNDER_NAME"},
  {"headline":"International Marketing Checklist: US & UK","url":"/blog/international-marketing-checklist-us-uk","author":"FOUNDER_NAME"},
  {"headline":"Full-Funnel vs Channel Marketing","url":"/blog/full-funnel-vs-channel-marketing","author":"FOUNDER_NAME"},
  {"headline":"Why SaaS Companies Need an AI-Native Growth Partner","url":"/blog/why-saas-companies-need-ai-native-growth-partner","author":"FOUNDER_NAME"},
  {"headline":"How We Cut Recruitment Response Time 48hrs to 4 Minutes","url":"/blog/how-we-cut-recruitment-response-time-48hrs-to-4-minutes","author":"FOUNDER_NAME"}
]
```

---

# 5. FAQPage Schema — Template

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{QUESTION_TEXT}}",
      "acceptedAnswer": { "@type": "Answer", "text": "{{ANSWER_TEXT}}" }
    }
  ]
}
```

*Populate `mainEntity` with one object per Q&A once the /faq page content is written (see next deliverable).*

---

# 6. BreadcrumbList — 5 Patterns

```json
[
  {"pattern":"Service sub-page","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.thenivy.com/"},
    {"@type":"ListItem","position":2,"name":"Services","item":"https://www.thenivy.com/services"},
    {"@type":"ListItem","position":3,"name":"Marketing","item":"https://www.thenivy.com/services/marketing"},
    {"@type":"ListItem","position":4,"name":"SEO","item":"https://www.thenivy.com/services/seo"}
  ]},
  {"pattern":"Top-level service","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.thenivy.com/"},
    {"@type":"ListItem","position":2,"name":"Services","item":"https://www.thenivy.com/services"},
    {"@type":"ListItem","position":3,"name":"AI Automation","item":"https://www.thenivy.com/services/ai-automation"}
  ]},
  {"pattern":"Market page","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.thenivy.com/"},
    {"@type":"ListItem","position":2,"name":"Markets","item":"https://www.thenivy.com/markets"},
    {"@type":"ListItem","position":3,"name":"UK","item":"https://www.thenivy.com/markets/uk"}
  ]},
  {"pattern":"Industry page","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.thenivy.com/"},
    {"@type":"ListItem","position":2,"name":"Industries","item":"https://www.thenivy.com/industries"},
    {"@type":"ListItem","position":3,"name":"SaaS","item":"https://www.thenivy.com/industries/saas"}
  ]},
  {"pattern":"Blog article","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.thenivy.com/"},
    {"@type":"ListItem","position":2,"name":"Blog","item":"https://www.thenivy.com/blog"},
    {"@type":"ListItem","position":3,"name":"How AI Is Transforming B2B Lead Generation in 2026","item":"https://www.thenivy.com/blog/how-ai-is-transforming-b2b-lead-generation-2026"}
  ]}
]
```

---

# 7. LocalBusiness Schema — 4 Regions ⚠️ DRAFT — DO NOT PUBLISH

> **Flag:** Source addresses came from the Master Business Profile System's "Global Headquarters" section, but the contact emails there are literally `xxxx.hq@yourcompany.com` — a placeholder domain, not [thenivy.com](http://thenivy.com). These addresses may never have been customised with real Nivy Next office data. **Confirm with Abhi which (if any) of these are real, staffed, mail-receivable addresses before publishing** — Google can suspend Business Profiles for unverifiable NAP data.
> 

```json
[
  {
    "@type": "LocalBusiness",
    "name": "Nivy Next — Americas",
    "address": {"@type":"PostalAddress","streetAddress":"1209 North Orange Street","addressLocality":"Wilmington","addressRegion":"DE","postalCode":"19801","addressCountry":"US"},
    "telephone": "REPLACE_VERIFIED_PHONE",
    "areaServed": ["United States","Canada"]
  },
  {
    "@type": "LocalBusiness",
    "name": "Nivy Next — EMEA",
    "address": {"@type":"PostalAddress","streetAddress":"71-75 Shelton Street, Covent Garden","addressLocality":"London","postalCode":"WC2H 9JQ","addressCountry":"GB"},
    "telephone": "REPLACE_VERIFIED_PHONE",
    "areaServed": ["United Kingdom"]
  },
  {
    "@type": "LocalBusiness",
    "name": "Nivy Next — MEASA",
    "address": {"@type":"PostalAddress","streetAddress":"Meydan Grandstand, 6th Floor, Meydan Road, Nad Al Sheba","addressLocality":"Dubai","addressCountry":"AE"},
    "telephone": "REPLACE_VERIFIED_PHONE",
    "areaServed": ["United Arab Emirates"]
  },
  {
    "@type": "LocalBusiness",
    "name": "Nivy Next — APAC",
    "address": {"@type":"PostalAddress","streetAddress":"10 Anson Road, #10-11 International Plaza","addressLocality":"Singapore","postalCode":"079903","addressCountry":"SG"},
    "telephone": "REPLACE_VERIFIED_PHONE",
    "areaServed": ["Australia","Singapore"]
  }
]
```

---

# 8. Offer Schema — Pricing Page (3 Tiers)

> Pricing is engagement-specific per the Business Profile (no fixed price list) — using `priceSpecification` with "by quote" framing rather than inventing fixed numbers.
> 

```json
{
  "@context": "https://schema.org",
  "@type": "OfferCatalog",
  "name": "Nivy Next Engagement Tiers",
  "itemListElement": [
    { "@type": "Offer", "name": "Starter", "description": "Single service vertical, monthly rolling contract.", "priceSpecification": {"@type":"PriceSpecification","description":"Custom quote — contact for pricing"} },
    { "@type": "Offer", "name": "Growth", "description": "2-3 service verticals, quarterly strategy reviews, 3-month minimum.", "priceSpecification": {"@type":"PriceSpecification","description":"Custom quote — contact for pricing"} },
    { "@type": "Offer", "name": "Partner", "description": "Full-stack access, dedicated team pod, 6-month minimum.", "priceSpecification": {"@type":"PriceSpecification","description":"Custom quote — contact for pricing"} }
  ]
}
```

---

# 9. About + Contact Page Schema

```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Nivy Next",
  "url": "https://www.thenivy.com/about",
  "about": { "@id": "https://www.thenivy.com/#organization" }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact Nivy Next",
  "url": "https://www.thenivy.com/contact",
  "about": { "@id": "https://www.thenivy.com/#organization" }
}
```

---

# 10. Hub Page Schema — /markets and /industries (CollectionPage + ItemList)

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "International Markets | Nivy Next",
  "url": "https://www.thenivy.com/markets",
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      {"@type":"ListItem","position":1,"url":"https://www.thenivy.com/markets/uk"},
      {"@type":"ListItem","position":2,"url":"https://www.thenivy.com/markets/us"},
      {"@type":"ListItem","position":3,"url":"https://www.thenivy.com/markets/australia"},
      {"@type":"ListItem","position":4,"url":"https://www.thenivy.com/markets/canada"},
      {"@type":"ListItem","position":5,"url":"https://www.thenivy.com/markets/uae"}
    ]
  }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Industries We Serve | Nivy Next",
  "url": "https://www.thenivy.com/industries",
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      {"@type":"ListItem","position":1,"url":"https://www.thenivy.com/industries/saas"},
      {"@type":"ListItem","position":2,"url":"https://www.thenivy.com/industries/ecommerce"},
      {"@type":"ListItem","position":3,"url":"https://www.thenivy.com/industries/professional-services"},
      {"@type":"ListItem","position":4,"url":"https://www.thenivy.com/industries/recruitment"},
      {"@type":"ListItem","position":5,"url":"https://www.thenivy.com/industries/health-wellness"}
    ]
  }
}
```

---

> 📅 **Created:** 20 June 2026 — replaces the unverified "✅ written" claim in the Master Plan. **Outstanding before publish:** logo URL, real social URLs, founder name + LinkedIn URL, verified phone numbers, and — critically — confirmation on which regional addresses are real.
>