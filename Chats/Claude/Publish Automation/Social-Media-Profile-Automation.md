> From: https://chatgpt.com/c/6a813b67-cdd0-83ee-b99f-f3fdbb307c1b

# you asked

message time: 2026-08-16 09:54:50

aesa 'koi tool ya software hai jo meri social media profiles apne aap fill kar de, mere pas profile ki text likhi hui hai

---

# chatgpt response

Haan, **aisa possible hai**. Agar aapke paas har platform ke liye profile text already written hai, to tools aapki profiles ko largely automate kar sakte hain.

Lekin ek distinction hai:

| Kaam | Automation |
|---|---|
| Bio/About text prepare karna | ✅ 100% |
| Same information ko platform-specific format mein convert karna | ✅ 100% |
| Profile photo/banner resize karna | ✅ |
| Social profiles par content/post schedule karna | ✅ |
| LinkedIn/Facebook/X/Instagram etc. ko ek dashboard se manage karna | ✅ |
| **Profile settings mein automatically login karke bio/name/category fill karna** | ⚠️ Platform-dependent |
| Password/OTP/2FA automatically handle karna | ❌/unsafe |

### Aapke case mein best setup

Aapke paas agar **Nivy/Nivy Next ki master profile information** ek document/database mein hai, to main ye architecture recommend karunga:

**Master Profile Data → n8n → AI → Platform-specific Profile → Approval → Browser Automation → Profile Updated**

Example:

> Master description  
> ↓  
> n8n  
> ↓  
> AI generates:
> - LinkedIn About
> - Facebook Bio
> - Instagram Bio
> - X Bio
> - YouTube About
> - Pinterest Bio
> - Reddit Profile
> - TikTok Bio
> ↓  
> Character-limit & formatting check  
> ↓  
> Human approval  
> ↓  
> Browser automation fills profile fields

**Important:** Posting/scheduling ke liye APIs available hone par API use karna better hai. Profile editing ke liye jahan API nahi hai, browser automation (Playwright/Selenium/Browser-use type setup) use kiya ja sakta hai, subject to each platform's rules.

Agar aap chaho to main **** bata sakta hoon.

---

# you asked

message time: 2026-08-16 09:57:01

top sare platforms pe, browser tum batao best kon sa hai baki sb kuch khud se batao

---

# chatgpt response

Haan. Aapke use-case ke liye main **single SaaS tool** lene ke bajay **n8n + browser automation + official APIs** ka hybrid setup banaunga. Isse aap 20+ important platforms ko ek master profile se manage kar sakte hain.

### 🏆 Browser: meri recommendation

**Playwright** ko primary browser automation engine rakho.

Reason:
- Open-source
- Chrome/Chromium, Firefox, WebKit support
- Reliable form filling/clicking/uploading
- Screenshots & verification
- n8n ke saath easily integrate ho sakta hai
- Aage AI browser agents ke saath bhi combine kar sakte hain

**Browser-use** ko optional AI layer rakhenge—not as the basic automation engine.

---

## 🌐 Top platforms ka setup

| Platform | Profile automation | Best method |
|---|---|---|
| LinkedIn | ⚠️ Limited API | Playwright |
| Facebook Page | ✅ | Meta API |
| Instagram Business/Creator | ✅/⚠️ | Meta API |
| X | ✅ | X API |
| YouTube | ✅ | YouTube API |
| TikTok | ⚠️ | API + Playwright where permitted |
| Pinterest | ⚠️ | API |
| Reddit | ⚠️ | API |
| Quora | ⚠️ | Playwright |
| Medium | ⚠️ | API/browser |
| GitHub | ✅ | API |
| GitLab | ✅ | API |
| Behance | ⚠️ | Browser |
| Dribbble | ⚠️ | Browser |
| Product Hunt | ⚠️ | Browser/API |
| Crunchbase | ⚠️ | Browser |
| Google Business Profile | ✅ | Google API |
| Threads | ⚠️ | Meta API |
| Telegram | ✅ | Telegram API |
| Discord | ✅ | Discord bot/API |
| WhatsApp Business | ✅ | Meta API |
| Vimeo | ⚠️ | API |
| Twitch | ⚠️ | API |
| Substack | ⚠️ | Browser/API |

**⚠️ का मतलब यह नहीं कि automation impossible है**—बस उस platform पर profile fields के लिए official API access अलग/limited हो सकता है। उदाहरण के लिए LinkedIn का Profile API restricted access वाला है, जबकि YouTube अपने channel branding/description को API से update करने देता है. ([Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api?utm_source=chatgpt.com))

X भी profile-related events को API में expose करता है और profile data में description/bio मौजूद है. ([X Developer Platform](https://docs.x.com/x-api/activity/introduction?utm_source=chatgpt.com)) Instagram का API professional/business/creator accounts के लिए presence management support करता है. ([Postman](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-db99ce99-bf76-475c-8b76-718576c11cae&utm_source=chatgpt.com))

---

# आपके लिए पूरा architecture

मैं इसे इस तरह बनाऊँगा:

```text
                 MASTER COMPANY PROFILE
                         │
                         ▼
                    PostgreSQL
                         │
                         ▼
                       n8n
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
        AI Profile Engine       Asset Engine
          (Ollama)              Logo/Banners
             │                       │
             └───────────┬───────────┘
                         ▼
                PLATFORM ADAPTER
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
   Official API      Playwright       Manual Approval
       │                 │                 │
       └─────────────────┴─────────────────┘
                         ▼
                PROFILE VERIFICATION
                         │
                         ▼
                  Screenshot + Log
```

### Master database में सिर्फ एक बार information डालेंगे

जैसे:

- Company name
- Short description
- Long description
- Founder
- Services
- Industries
- Target countries
- Website
- Email
- Phone
- Address
- Social links
- Keywords
- USP
- Mission
- Vision
- Tagline
- Logo
- Profile photo
- Cover/banner
- CTA
- Founded year

फिर **n8n + Ollama** हर platform के लिए automatically appropriate version बनाएगा।

उदाहरण:

**Master description:**

> Nivy Next is an AI-powered digital marketing and technology company helping businesses grow through performance marketing, automation, web development and AI solutions.

फिर system automatically अलग-अलग character limits और style के हिसाब से versions बनाएगा।

---

## 🔥 सबसे important: सिर्फ text नहीं

मैं आपके लिए system में **Profile Completeness Engine** भी रखूँगा।

हर platform के लिए:

```text
✓ Profile photo
✓ Cover/banner
✓ Username
✓ Display name
✓ Bio
✓ About
✓ Website
✓ Email
✓ Phone
✓ Location
✓ Category
✓ Services
✓ CTA
✓ Keywords
✓ Social links
✓ Verification
```

फिर n8n बोलेगा:

**LinkedIn: 92% complete**  
**Instagram: 100% complete**  
**Facebook: 100% complete**  
**X: 95% complete**  
**YouTube: 100% complete**

और missing चीज automatically identify करेगा।

---

### एक और बहुत useful feature

**Master Change → Everywhere**

आप बाद में master profile में कुछ बदलते हैं:

> "We now provide AI Agent Development."

तो n8n detect करेगा:

```text
Master Profile Changed
        ↓
AI regenerate affected profiles
        ↓
Character-limit validation
        ↓
API / Playwright
        ↓
Update platforms
        ↓
Verify
        ↓
Log
```

इससे आपको **25 websites खोलकर manually profile update नहीं करनी पड़ेगी।**

और जहाँ official APIs उपलब्ध हैं, वहाँ मैं browser automation की जगह API को प्राथमिकता दूँगा—यह ज्यादा stable और platform-compliant approach है.

---

# you asked

message time: 2026-08-16 10:06:33

official api kaha se aygi, short me batao

---

# chatgpt response

Short mein: **har platform ki official Developer website se API milti hai.**

- **Meta (Facebook + Instagram)** → Meta for Developers → App create → API + Access Token. ([Postman](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?utm_source=chatgpt.com))
- **YouTube** → Google Cloud Console → Project → YouTube Data API → OAuth credentials. ([Google for Developers](https://developers.google.com/youtube/registering_an_application?authuser=2&hl=en&utm_source=chatgpt.com))
- **X** → X Developer Portal → App → API credentials.
- **LinkedIn** → LinkedIn Developers → App → required API products/access.
- Baaki platforms mein bhi generally **Developer Portal → Create App → API credentials/OAuth** process hota hai.

**Aapko har platform ka API alag se nikalna padega**, lekin ek baar credentials configure karne ke baad **n8n un sabko centrally manage kar sakta hai**.

---

# you asked

message time: 2026-08-16 10:08:38

to bhai ye kaise banega baki ka, short me batao

---

# chatgpt response

Haan bhai, **baki jahan official API nahi/limited hai**, wahan:

**n8n → Playwright → Login session → Profile fields fill → Save → Screenshot/verification**

Bas ek baar browser mein login + 2FA manually karoge, uske baad Playwright saved session se profile update kar sakta hai.

### Overall:
**API available → n8n + API** ✅  
**API unavailable → n8n + Playwright** ✅  
**AI text generation → Ollama** ✅  
**Central data → PostgreSQL** ✅  
**Sabko control → n8n** ✅

Is tarah ek **Master Social Profile Updater** ban jayega.

---

# you asked

message time: 2026-08-16 10:09:35

kya koi code generate karna padeha, short me batao

---

# chatgpt response

Haan, **thoda code lagega**, lekin bahut zyada nahi.

- **n8n:** mostly visual workflow, coding minimum.
- **API platforms:** API credentials + n8n HTTP/API nodes; usually custom code nahi.
- **Playwright:** profile automation ke liye **small JavaScript/TypeScript scripts** banenge.
- **Ollama:** AI text generation ke liye mostly API call.
- **PostgreSQL:** database queries, basic SQL.

👉 Matlab **ek baar reusable Playwright automation framework bana denge**, phir naye platforms add karna comparatively easy hoga.

---

# you asked

message time: 2026-08-16 10:10:10

kya tum mere liye sabhi platforms ki api khud se dhund kar de sakte ho ya mujhe manually dhundni pdegi, short me batao

---

# chatgpt response

Haan bhai, **main khud research karke sabhi platforms ki official API/developer links aur access requirements ki list de sakta hoon.**  

Aapko manually research nahi karni padegi.  
Bas **API keys / OAuth credentials** jahan required hain, woh aapko respective accounts se generate karne honge.

---

# you asked

message time: 2026-08-16 10:12:55

to agar mujhe claude se sab karwana hai to mai uske kya command, jitme bh socila media platforms ya fir mujhe seo ke liye ke liye jitne bhi platforms ke liye karna hai to sare platforms ki list de do taki mai sabhi pe kar saku,

---

# chatgpt response

Bilkul bhai. Agar goal **Nivy/Nivy Next ko maximum online discoverability + Social SEO + Google SEO + AI/GEO visibility** dena hai, to sirf social media profiles nahi—**social, search engines, business directories, publishing, video, developer, community, review aur SEO platforms** sab cover karne chahiye.

Google ne bhi ab Instagram, TikTok, X aur YouTube ko Search Console mein platform properties ke रूप में support करना शुरू किया है, इसलिए social profiles ka SEO value aur important ho gaya hai. ([Google for Developers](https://developers.google.com/search/blog/2026/07/search-console-social-video-platforms?utm_source=chatgpt.com))

## 1. Social Media — MUST HAVE

| Platform | Priority |
|---|---|
| Facebook Page | 🔴 |
| Instagram | 🔴 |
| LinkedIn Personal | 🔴 |
| LinkedIn Company Page | 🔴 |
| X/Twitter | 🔴 |
| YouTube | 🔴 |
| TikTok | 🔴 |
| Pinterest | 🟠 |
| Reddit | 🔴 |
| Threads | 🟠 |
| Snapchat | 🟡 |
| Telegram | 🟠 |
| Discord | 🟡 |
| Quora | 🔴 |
| Medium | 🔴 |

## 2. Search Engines / Webmaster

| Platform | Priority |
|---|---|
| Google Search Console | 🔴 |
| Google Business Profile | 🔴 |
| Bing Webmaster Tools | 🔴 |
| Yandex Webmaster | 🟠 |
| Naver Search Advisor | 🟡 |
| Baidu Webmaster | 🟡 |
| Google Analytics | 🔴 |
| Google Trends | 🔴 |

Google Search Console indexing, search queries, clicks, impressions, backlinks etc. monitor karta hai. ([Google Support](https://support.google.com/webmasters/answer/9128668?hl=en-IN&utm_source=chatgpt.com)) Bing Webmaster bhi keyword research, backlinks, SEO diagnostics etc. provide karta hai. ([Search - Microsoft Bing](https://www.bing.com/webmasters/about?lang=en&utm_source=chatgpt.com)) Yandex Webmaster mein site verification aur optimization recommendations hain. ([Yandex](https://yandex.com/support/webmaster/en/service/quick-start?utm_source=chatgpt.com))

## 3. Business / Local SEO

Ye **bahut important** hai:

- Google Business Profile
- Bing Places
- Apple Business Connect
- Yelp
- Foursquare
- TripAdvisor
- Yellow Pages
- MapQuest
- HERE
- Waze
- BBB
- Hotfrog
- Manta
- Chamber of Commerce
- Crunchbase
- Clutch
- GoodFirms
- DesignRush
- Sortlist
- UpCity
- G2
- Capterra
- Trustpilot

## 4. Publishing / Content SEO

- Medium
- Substack
- WordPress
- Blogger
- Tumblr
- Ghost
- Hashnode
- DEV Community
- Vocal
- LinkedIn Articles
- Quora
- Reddit

## 5. Video SEO

- YouTube
- TikTok
- Instagram Reels
- Facebook Video
- Vimeo
- Dailymotion
- Twitch
- Rumble

## 6. Developer / Technology Authority

Aapki IT/AI company ke liye particularly important:

- GitHub
- GitLab
- Bitbucket
- Stack Overflow
- Stack Exchange
- DEV
- Hashnode
- CodePen
- Product Hunt
- Hacker News
- Kaggle

## 7. Design / Creative

Nivy Studio / design services ke liye:

- Behance
- Dribbble
- ArtStation
- DeviantArt
- Vimeo
- Pinterest
- Adobe Portfolio

## 8. Startup / Company Profiles

- Crunchbase
- Product Hunt
- AngelList/Wellfound
- F6S
- Gust
- StartupBlink
- Tracxn
- Dealroom

## 9. Reviews / Reputation

- Google Reviews
- Trustpilot
- G2
- Capterra
- Clutch
- GoodFirms
- DesignRush
- UpCity
- Yelp
- Facebook Reviews

---

# 🔥 SEO tools/data layer bhi add karo

Agar Claude se **complete SEO automation system** banwana hai, to ye bhi integrate karwao:

### Free/official

- Google Search Console
- Google Analytics
- Google Business Profile
- Google Trends
- Google Ads Keyword Planner
- Bing Webmaster Tools
- PageSpeed Insights
- Lighthouse

### Professional SEO APIs

- Semrush
- Ahrefs
- Moz
- DataForSEO
- SerpApi
- Similarweb
- Majestic

Semrush ka official API keyword data, backlinks, competitors, domain reports, traffic/market data etc. provide karta hai. ([Semrush Developer](https://developer.semrush.com/api/v4/?utm_source=chatgpt.com))

---

# 🤖 AI/GEO visibility ke liye

Isko bhi system mein include karna chahiye:

- ChatGPT
- Google AI Overviews / AI Mode
- Google Gemini
- Microsoft Copilot
- Perplexity
- Claude
- You.com
- Brave Search
- Bing
- Reddit
- Wikipedia/Wikidata

**Important:** in sab jagah "profile automatically create/update" possible nahi hota. Jahan official API hai, API; jahan nahi hai, permitted browser automation/manual workflow use karna hoga.

---

# 🚀 Claude ko dene wali command

Aap Claude ko **ek giant command** dene ke bajay ye project banwao:

**Master Social + SEO + GEO Distribution Automation System**

Architecture:

```text
MASTER COMPANY DATA
        ↓
PostgreSQL
        ↓
n8n
        ↓
Ollama
        ↓
Platform-specific Content Generator
        ↓
API / Playwright
        ↓
30–50+ Platforms
        ↓
Verification
        ↓
SEO Monitoring
        ↓
Analytics
        ↓
AI/GEO Monitoring
        ↓
Dashboard
```

Aur Claude ko specifically bolo ki:

1. **upar diye gaye sab platforms ko inventory kare**
2. har platform ka **official API/developer documentation** research kare
3. API available hai ya nahi determine kare
4. API access requirements identify kare
5. API nahi hai to **Playwright feasibility** determine kare
6. platform-specific character limits identify kare
7. master company profile se platform-specific profile generate kare
8. profile completeness checker banaye
9. duplicate/incorrect information detect kare
10. NAP consistency checker banaye
11. UTM/link tracking add kare
12. schema/structured-data strategy banaye
13. Google/Bing indexing monitoring kare
14. backlinks/mentions monitor kare
15. brand mentions monitor kare
16. AI search visibility monitor kare
17. n8n workflows generate kare
18. PostgreSQL schema generate kare
19. Ollama prompts generate kare
20. Playwright automation modules generate kare
21. API credentials ke liye `.env` structure banaye
22. **password/API keys code mein hardcode na kare**
23. हर platform के लिए logs + screenshots + failure handling रखे
24. final dashboard बनाये.

### सबसे जरूरी बात

**सिर्फ "social media automation" मत बनवाना।**

Claude को इसे **"Omnichannel Social SEO + Entity SEO + Local SEO + GEO/AI Visibility Automation System"** के रूप में बनवाने को बोलना।

क्योंकि आपका लक्ष्य केवल profile भरना नहीं है—**Nivy/Nivy Next की digital entity को हर relevant search/social/AI surface पर consistently establish करना है.** Third-party SEO tools useful हैं, लेकिन Google खुद कहता है कि उनकी recommendations को Google की official guidance के against verify करना चाहिए. ([Google for Developers](https://developers.google.com/search/docs/fundamentals/third-party-seo?authuser=002&hl=en&utm_source=chatgpt.com))

अगर आप चाहें तो अगला step मैं **Claude को देने के लिए एक ** बना सकता हूँ, जिसमें **ये सभी platforms + APIs + Playwright + n8n + Ollama + PostgreSQL + folder structure + workflows + files** सब शामिल होंगे।

---

# you asked

message time: 2026-08-16 10:13:49

Give me a complete copy-paste master command for Claude including all platforms, APIs, Playwright, n8n, Ollama, PostgreSQL, folder structure, workflows, and files

---

# chatgpt response

Below is a **single master prompt** you can paste into Claude Code. It tells Claude to research the current official APIs itself, build the system incrementally, and generate the complete repository rather than merely giving you an architecture.

**Document Title: **

# MASTER COMMAND FOR CLAUDE CODE

You are the lead architect, senior full-stack engineer, automation engineer, SEO engineer, DevOps engineer, and AI-agent engineer for this project.

Your task is to design and BUILD a production-ready **Omnichannel Social Media + SEO + Local SEO + Entity SEO + GEO/AI Visibility Automation Platform** for my company.

Do NOT merely explain what should be built.

You must:
1. Research current official documentation.
2. Design the architecture.
3. Create the complete folder structure.
4. Generate all required source files.
5. Generate n8n workflow definitions.
6. Generate database schemas.
7. Generate API integration modules.
8. Generate Playwright automation modules where legally/technically appropriate.
9. Generate Ollama prompts and AI processing modules.
10. Generate Docker configuration.
11. Generate environment configuration templates.
12. Generate documentation.
13. Generate tests.
14. Generate monitoring/logging/error handling.
15. Give exact commands required to install and run everything.

IMPORTANT:
- Work incrementally.
- Do not create fake API endpoints.
- Do not invent API capabilities.
- Do not assume an API exists.
- Verify every API against the platform's CURRENT official developer documentation.
- Prefer official APIs over browser automation.
- Use browser automation only where permitted and technically appropriate.
- Never bypass CAPTCHA, MFA, anti-bot systems, rate limits, access controls, or platform security.
- Never attempt to evade platform restrictions.
- Do not automate actions that violate the platform's Terms of Service.
- Where automation is prohibited or unavailable, create a MANUAL ACTION queue instead.
- Never hardcode passwords, API keys, OAuth secrets, cookies, tokens, or private credentials.
- Use environment variables/secrets management.
- Do not create spam, fake reviews, fake accounts, fake engagement, or deceptive activity.
- Respect platform rate limits and robots/automation restrictions where applicable.
- Every destructive or externally visible action should have an approval mode.

==================================================
1. BUSINESS OBJECTIVE
==================================================

Build a centralized system that maintains the company's digital identity and distributes/updates approved company information across relevant online platforms.

The system must manage:

- Company profiles
- Founder profiles
- Brand profiles
- Social media profiles
- Business listings
- SEO properties
- Content publishing
- Video profiles
- Developer profiles
- Review/reputation profiles
- Startup/company directories
- Local SEO
- Entity SEO
- Backlink/mention monitoring
- Search visibility
- AI/GEO visibility
- Profile completeness
- NAP consistency
- Brand consistency
- Content consistency
- Social publishing
- SEO monitoring
- Analytics
- Reporting

The central principle is:

MASTER DATA → AI TRANSFORMATION → VALIDATION → APPROVAL → PLATFORM API/AUTOMATION → VERIFICATION → MONITORING

==================================================
2. TECHNOLOGY STACK
==================================================

Use the following stack unless there is a strong technical reason to change something:

Core orchestration:
- n8n

Database:
- PostgreSQL

AI:
- Ollama
- Support configurable local models
- Keep model names configurable through environment variables

Browser automation:
- Playwright
- TypeScript

Backend:
- Python FastAPI OR Node.js/TypeScript
- Prefer TypeScript if it simplifies Playwright/API integration
- Use a clean modular architecture

Frontend/dashboard:
- Next.js
- TypeScript
- Tailwind CSS

Reverse proxy:
- Caddy OR Nginx

Containerization:
- Docker
- Docker Compose

Storage:
- PostgreSQL
- Local/object storage abstraction for screenshots/assets

Optional:
- Redis for queues/caching if genuinely required

Monitoring:
- structured application logs
- health checks
- execution logs
- workflow logs
- failed-job queue

==================================================
3. PLATFORM INVENTORY
==================================================

Create a central platform registry.

Research and classify the following platforms.

Do NOT assume every platform supports automation.

For each platform determine:

- official website
- official developer portal
- official API documentation
- authentication mechanism
- OAuth requirements
- available profile APIs
- publishing APIs
- analytics APIs
- business/profile APIs
- API pricing if applicable
- API access approval requirements
- rate limits
- automation restrictions
- whether browser automation is permitted
- whether browser automation is technically feasible
- fields that can be updated
- fields that cannot be updated
- manual-only fields
- verification requirements
- current status as of implementation date

Create:
platform_registry
platform_capabilities
platform_credentials
platform_field_mapping
platform_automation_policy

--------------------------------------------------
A. SOCIAL MEDIA
--------------------------------------------------

Primary:

1. Facebook Pages
2. Instagram
3. LinkedIn Personal Profile
4. LinkedIn Company Page
5. X / Twitter
6. YouTube
7. TikTok
8. Pinterest
9. Reddit
10. Threads
11. Snapchat
12. Telegram
13. Discord
14. Quora
15. Medium
16. Tumblr
17. Mastodon
18. Bluesky

For every platform determine whether the official API supports:
- profile data
- bio/about
- avatar
- cover image
- links
- posts
- scheduling
- analytics
- comments
- messages
- followers/following data

Only implement capabilities officially supported.

--------------------------------------------------
B. SEARCH / WEBMASTER / SEARCH VISIBILITY
--------------------------------------------------

1. Google Search Console
2. Google Business Profile
3. Google Analytics
4. Google Trends
5. Google Ads Keyword Planner
6. Google PageSpeed Insights
7. Google Lighthouse
8. Bing Webmaster Tools
9. Bing Places
10. Yandex Webmaster
11. Naver Search Advisor
12. Baidu Webmaster Tools

Build modules for:
- verification
- sitemap monitoring
- indexing monitoring
- search queries
- impressions
- clicks
- CTR
- rankings where available
- crawl errors
- Core Web Vitals where available
- URL inspection where available

--------------------------------------------------
C. BUSINESS / LOCAL SEO DIRECTORIES
--------------------------------------------------

Research current availability and API/access rules for:

1. Google Business Profile
2. Bing Places
3. Apple Business Connect
4. Yelp
5. Foursquare
6. TripAdvisor
7. Yellow Pages
8. MapQuest
9. HERE
10. Waze
11. BBB
12. Hotfrog
13. Manta
14. Chamber of Commerce
15. Crunchbase
16. Clutch
17. GoodFirms
18. DesignRush
19. Sortlist
20. UpCity
21. G2
22. Capterra
23. Trustpilot

IMPORTANT:
Do not automatically create duplicate listings.
Do not submit false business information.
Create manual approval when a directory requires human verification.

--------------------------------------------------
D. CONTENT / PUBLISHING
--------------------------------------------------

1. WordPress
2. Medium
3. Substack
4. Blogger
5. Ghost
6. Tumblr
7. Hashnode
8. DEV Community
9. Vocal
10. LinkedIn publishing
11. Reddit
12. Quora

Implement:
- article generation
- title generation
- meta description
- slug
- tags
- categories
- canonical URL
- internal links
- external references
- featured image
- publishing
- scheduling where officially supported
- draft/approval workflow

--------------------------------------------------
E. VIDEO
--------------------------------------------------

1. YouTube
2. Vimeo
3. TikTok
4. Instagram Reels
5. Facebook Video
6. Dailymotion
7. Twitch
8. Rumble

Manage:
- channel/profile information
- descriptions
- links
- video metadata
- titles
- descriptions
- tags
- thumbnails
- playlists
- publishing
- analytics where APIs support it

--------------------------------------------------
F. DEVELOPER / TECH AUTHORITY
--------------------------------------------------

1. GitHub
2. GitLab
3. Bitbucket
4. Stack Overflow
5. Stack Exchange
6. DEV Community
7. Hashnode
8. CodePen
9. Product Hunt
10. Hacker News
11. Kaggle

Manage only officially permitted fields/actions.

--------------------------------------------------
G. DESIGN / CREATIVE
--------------------------------------------------

1. Behance
2. Dribbble
3. ArtStation
4. DeviantArt
5. Vimeo
6. Pinterest
7. Adobe Portfolio

--------------------------------------------------
H. STARTUP / COMPANY DATABASES
--------------------------------------------------

1. Crunchbase
2. Wellfound
3. F6S
4. Gust
5. StartupBlink
6. Tracxn
7. Dealroom
8. Product Hunt

Do not fabricate company data.

--------------------------------------------------
I. REVIEW / REPUTATION
--------------------------------------------------

1. Google Reviews
2. Trustpilot
3. G2
4. Capterra
5. Clutch
6. GoodFirms
7. DesignRush
8. UpCity
9. Yelp
10. Facebook Reviews

Build:
- review monitoring
- review notification
- response drafting
- approval workflow
- sentiment classification
- recurring issue detection

NEVER generate fake reviews or incentivize deceptive reviews.

==================================================
4. SEO DATA PROVIDERS
==================================================

Research official APIs and build optional adapters for:

1. Semrush
2. Ahrefs
3. Moz
4. DataForSEO
5. SerpApi
6. Similarweb
7. Majestic

Make every paid provider optional.

Use interfaces such as:

KeywordProvider
SERPProvider
BacklinkProvider
CompetitorProvider
TrafficProvider

The system must work with zero paid SEO APIs for basic functionality.

==================================================
5. AI / GEO VISIBILITY
==================================================

Build an AI visibility monitoring framework.

Track brand/company mentions and visibility across:

1. Google Search / AI search surfaces where measurable
2. Bing/Copilot where measurable
3. Perplexity where measurable through permitted means
4. ChatGPT-related discoverability where measurable through permitted means
5. Gemini-related discoverability where measurable through permitted means
6. Claude-related discoverability where measurable through permitted means
7. You.com
8. Brave Search

IMPORTANT:

Do NOT pretend that an AI platform exposes an official "ranking API" if it does not.

For each platform classify:
- official API
- indirect measurement
- manual measurement
- unavailable

Build a GEO monitoring report based on measurable evidence.

==================================================
6. MASTER COMPANY PROFILE
==================================================

Create a master profile database.

Tables/entities should include:

company
brands
people
founders
services
industries
locations
countries
contact_points
social_links
websites
assets
logos
brand_guidelines
descriptions
taglines
mission
vision
usp
keywords
target_audiences
competitors
certifications
awards
press_mentions

Example company fields:

company_name
legal_name
brand_name
short_description
medium_description
long_description
tagline
mission
vision
usp
founded_year
website
email
phone
country
city
address
services
industries
target_markets
social_profiles

==================================================
7. PROFILE TRANSFORMATION ENGINE
==================================================

Build an AI engine that takes MASTER PROFILE DATA and generates platform-specific versions.

Example:

Master Description
        ↓
Ollama
        ↓
LinkedIn version
Facebook version
Instagram version
X version
YouTube version
TikTok version
Pinterest version
Reddit version
Quora version
Medium version
etc.

Every generated profile must pass:

- character limit
- prohibited character check
- URL validation
- brand consistency
- factual consistency
- prohibited claims check
- duplicate detection
- platform-specific formatting
- language validation

Never invent:
- awards
- customers
- revenue
- certifications
- offices
- employees
- partnerships
- reviews
- statistics

==================================================
8. PROFILE COMPLETENESS ENGINE
==================================================

For each platform create a completeness score.

Example:

LinkedIn
Profile image       ✓
Banner              ✓
Name                ✓
Headline            ✓
About               ✓
Website             ✓
Services            ✓
Location            ✓
CTA                 ✓

Score = 94%

Build:
profile_completeness
profile_missing_fields
profile_validation_results

==================================================
9. NAP CONSISTENCY ENGINE
==================================================

For local/business information compare:

Name
Address
Phone
Website
Email
Opening hours
Category

across every platform.

Detect:

- spelling differences
- outdated phone
- outdated address
- wrong URL
- duplicate business listing
- inconsistent company name

Generate:

NAP_CONSISTENCY_REPORT

==================================================
10. SOCIAL CONTENT ENGINE
==================================================

Build content generation workflows for:

- educational posts
- case studies
- company updates
- offers
- founder content
- industry insights
- FAQs
- customer education
- video scripts
- reels
- shorts
- LinkedIn posts
- X posts
- Reddit contributions
- Quora answers
- articles
- newsletters

Do not create spam.

Build content approval states:

DRAFT
AI_REVIEW
HUMAN_REVIEW
APPROVED
SCHEDULED
PUBLISHED
FAILED
ARCHIVED

==================================================
11. CONTENT REPURPOSING
==================================================

Build:

ONE MASTER CONTENT
        ↓
ARTICLE
        ↓
LinkedIn
X
Facebook
Instagram
Threads
Pinterest
Reddit
Quora
YouTube script
Short video script
Newsletter
Google Business post where permitted

Every platform receives a native adaptation rather than identical spam.

==================================================
12. N8N WORKFLOWS
==================================================

Create actual importable n8n workflow JSON files.

Minimum workflows:

01_master_profile_sync.json

02_profile_generation.json

03_profile_validation.json

04_profile_completeness.json

05_platform_api_sync.json

06_playwright_profile_sync.json

07_social_content_generation.json

08_content_approval.json

09_content_distribution.json

10_content_repurposing.json

11_social_analytics.json

12_google_search_console.json

13_google_business_profile.json

14_bing_webmaster.json

15_keyword_research.json

16_serp_monitoring.json

17_backlink_monitoring.json

18_competitor_monitoring.json

19_brand_mention_monitoring.json

20_review_monitoring.json

21_nap_consistency.json

22_ai_visibility_monitoring.json

23_seo_audit.json

24_technical_seo_monitoring.json

25_content_gap_analysis.json

26_internal_link_suggestions.json

27_schema_validation.json

28_monthly_seo_report.json

29_weekly_social_report.json

30_error_retry_queue.json

31_platform_health_check.json

32_asset_distribution.json

33_approval_queue.json

34_manual_action_queue.json

35_daily_master_sync.json

==================================================
13. PLAYWRIGHT AUTOMATION
==================================================

Create a reusable Playwright framework.

Structure:

browser/
  core/
  sessions/
  pages/
  adapters/
  selectors/
  validators/
  screenshots/
  storage/
  tests/

Each platform gets an adapter only when appropriate.

Example interface:

interface PlatformAdapter {
  login(): Promise<void>;
  checkProfile(): Promise<ProfileStatus>;
  updateProfile(data: PlatformProfile): Promise<UpdateResult>;
  uploadAvatar(path: string): Promise<void>;
  uploadBanner(path: string): Promise<void>;
  verify(): Promise<VerificationResult>;
}

Use stable selectors.

Do NOT bypass:
- CAPTCHA
- MFA
- security challenges
- anti-bot systems
- rate limits
- access controls

If a platform blocks automation:
return:

AUTOMATION_NOT_ALLOWED

and create a manual action.

==================================================
14. API ADAPTER ARCHITECTURE
==================================================

Create:

integrations/
  google/
  meta/
  linkedin/
  x/
  youtube/
  pinterest/
  reddit/
  wordpress/
  github/
  gitlab/
  discord/
  telegram/
  seo/
  directories/

Every integration must have:

auth
client
models
mapper
validator
service
tests

Use OAuth where required.

Store credentials only in:
.env
Docker secrets
or another secure secrets mechanism.

==================================================
15. POSTGRESQL DATABASE
==================================================

Create migrations for:

companies
brands
people
services
industries
locations
assets
platforms
platform_capabilities
platform_accounts
platform_profiles
platform_fields
platform_field_values
oauth_credentials
content
content_variants
content_assets
content_publications
content_publication_logs
seo_properties
keywords
keyword_rankings
serps
backlinks
competitors
mentions
reviews
nap_records
profile_scores
profile_validation
ai_visibility
automation_jobs
automation_runs
automation_errors
manual_actions
approval_requests
audit_logs

Add:
- primary keys
- foreign keys
- indexes
- timestamps
- soft-delete where appropriate

==================================================
16. SECURITY
==================================================

Implement:

- encrypted secrets where appropriate
- environment variables
- OAuth token refresh
- RBAC
- audit logs
- CSRF protection
- input validation
- rate limiting
- secure cookies
- session isolation
- least privilege
- no credential logging
- no token logging
- no password storage unless absolutely required
- secret redaction in logs

Roles:

ADMIN
MANAGER
EDITOR
SEO
MARKETING
VIEWER

==================================================
17. APPROVAL SYSTEM
==================================================

Every externally visible action must support:

AUTO
APPROVAL_REQUIRED
MANUAL_ONLY

Example:

Profile bio update:
APPROVAL_REQUIRED

Social post:
APPROVAL_REQUIRED

Google Business update:
APPROVAL_REQUIRED

SEO monitoring:
AUTO

Report generation:
AUTO

Review response:
APPROVAL_REQUIRED

==================================================
18. DASHBOARD
==================================================

Build a Next.js dashboard.

Pages:

/dashboard

/company

/brands

/profiles

/platforms

/profile-completeness

/content

/content/calendar

/approvals

/social

/seo

/keywords

/serps

/backlinks

/competitors

/mentions

/reviews

/local-seo

/nap

/geo

/analytics

/reports

/automation

/jobs

/errors

/manual-actions

/settings

==================================================
19. DASHBOARD KPIs
==================================================

Display:

Total platforms
Connected platforms
Disconnected platforms
Profile completeness
SEO visibility
Keyword rankings
Organic clicks
Organic impressions
CTR
Backlinks
Referring domains
Brand mentions
Review score
NAP consistency
Social followers
Engagement
Published content
Pending approvals
Failed automations
AI/GEO visibility

==================================================
20. FILE/FOLDER STRUCTURE
==================================================

Create this repository:

nivy-omnichannel-seo/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   ├── security.md
│   ├── api-integrations.md
│   ├── platform-matrix.md
│   ├── automation-policy.md
│   ├── seo-strategy.md
│   ├── geo-strategy.md
│   └── troubleshooting.md
│
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
│
├── n8n/
│   ├── workflows/
│   ├── credentials/
│   └── README.md
│
├── apps/
│   ├── api/
│   ├── web/
│   └── worker/
│
├── integrations/
│   ├── google/
│   ├── meta/
│   ├── linkedin/
│   ├── x/
│   ├── youtube/
│   ├── pinterest/
│   ├── reddit/
│   ├── wordpress/
│   ├── github/
│   ├── gitlab/
│   ├── telegram/
│   ├── discord/
│   ├── seo/
│   └── directories/
│
├── browser/
│   ├── core/
│   ├── sessions/
│   ├── pages/
│   ├── adapters/
│   ├── selectors/
│   ├── validators/
│   └── tests/
│
├── ai/
│   ├── prompts/
│   ├── ollama/
│   ├── profile-generator/
│   ├── content-generator/
│   ├── seo-analyzer/
│   └── geo-monitor/
│
├── assets/
│   ├── logos/
│   ├── banners/
│   ├── profile-images/
│   ├── thumbnails/
│   └── generated/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── platform/
│
└── scripts/
    ├── setup.sh
    ├── backup.sh
    ├── health-check.sh
    └── migrate.sh

==================================================
21. PLATFORM MATRIX
==================================================

Create:

docs/platform-matrix.md

with columns:

Platform
Official API
Developer URL
API Documentation
OAuth
Profile Update
Publishing
Analytics
Browser Automation
Automation Allowed?
Manual Required?
Rate Limit
Cost
Access Requirement
Implementation Status
Last Verified Date

IMPORTANT:

You MUST research these values from CURRENT official documentation.

Never fill unknown values with guesses.

Use:

UNKNOWN

instead of guessing.

==================================================
22. API RESEARCH PROCESS
==================================================

Before implementing an integration:

1. Search official developer portal.
2. Open official documentation.
3. Verify authentication.
4. Verify endpoint.
5. Verify permissions.
6. Verify current availability.
7. Verify rate limits.
8. Verify pricing/access requirements.
9. Record source URL.
10. Record verification date.
11. Implement.
12. Add integration test.
13. Mark capability in platform registry.

Do not rely on random blogs when official documentation exists.

==================================================
23. OLLAMA
==================================================

Create an Ollama abstraction.

Environment:

OLLAMA_BASE_URL=
OLLAMA_MODEL=

Create prompts for:

- profile rewriting
- bio generation
- content generation
- platform adaptation
- SEO analysis
- keyword clustering
- search intent classification
- competitor analysis
- content gap analysis
- review sentiment
- review response drafting
- NAP discrepancy analysis
- GEO visibility analysis
- entity consistency
- schema suggestions

All prompts must instruct the model:

"Never invent factual business information."

==================================================
24. SEO ENGINE
==================================================

Implement:

Technical SEO audit
On-page SEO
Keyword clustering
Search intent
Content gap
Competitor analysis
Internal linking
Schema recommendations
Title recommendations
Meta description recommendations
Heading analysis
Image ALT recommendations
Core Web Vitals monitoring
Indexability monitoring
Sitemap monitoring
Robots.txt monitoring
Canonical monitoring

==================================================
25. ENTITY SEO
==================================================

Build an entity consistency engine.

Track:

Company name
Founder
Brand
Services
Industries
Locations
Website
Social profiles
Business directories
Knowledge sources

Detect inconsistent facts.

Generate an:

ENTITY_CONSISTENCY_SCORE

==================================================
26. GEO / AI SEARCH
==================================================

Build a GEO dataset.

For selected queries:

- query
- target country
- language
- search intent
- expected entity
- competitors
- brand mentioned?
- citation/source mentioned?
- sentiment
- answer position if measurable
- evidence URL
- timestamp

Never claim precise AI rankings unless measurable.

==================================================
27. ANALYTICS
==================================================

Create daily snapshots.

Track:

daily
weekly
monthly

Metrics:

social
SEO
local SEO
reviews
backlinks
mentions
content
GEO
traffic

Generate automated reports.

==================================================
28. ERROR HANDLING
==================================================

Every integration must handle:

401
403
404
409
429
500
timeout
network failure
expired OAuth
invalid token
permission denied
platform unavailable

Use:

retry with exponential backoff
dead-letter queue
error classification
manual intervention

Never endlessly retry.

==================================================
29. TESTING
==================================================

Create:

unit tests
integration tests
API mock tests
Playwright tests
database tests
n8n workflow validation
security tests

For external APIs use mocks in CI.

Do not run destructive production actions in tests.

==================================================
30. DEVOPS
==================================================

Create Docker Compose services:

postgres
n8n
ollama
api
worker
web
redis if required
caddy/nginx if required

Add health checks.

Add persistent volumes.

Create backup/restore scripts.

==================================================
31. ENVIRONMENT VARIABLES
==================================================

Create:

.env.example

Include placeholders for:

DATABASE_URL
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB

N8N_ENCRYPTION_KEY

OLLAMA_BASE_URL
OLLAMA_MODEL

GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET

META_APP_ID
META_APP_SECRET

LINKEDIN_CLIENT_ID
LINKEDIN_CLIENT_SECRET

X_CLIENT_ID
X_CLIENT_SECRET

YOUTUBE credentials

PINTEREST credentials

REDDIT credentials

WORDPRESS credentials

GITHUB credentials

GITLAB credentials

SEO provider credentials

Never put real credentials into repository files.

==================================================
32. MANUAL ACTION QUEUE
==================================================

If a platform cannot legally/technically be automated, create:

manual_actions

Fields:

id
platform
action
description
required_data
instructions
status
assigned_to
created_at
completed_at
evidence_url
screenshot

Dashboard must display:

"Manual action required"

instead of pretending automation succeeded.

==================================================
33. AUDIT LOG
==================================================

Log every action:

timestamp
user
platform
action
before_value
after_value
method
status
error
approval_id

Never store passwords or secrets.

==================================================
34. INITIAL COMPANY DATA
==================================================

Create a seed/template file:

config/company-profile.example.yaml

Use placeholders only.

Do NOT invent real company facts.

Example:

company:
  name: ""
  legal_name: ""
  website: ""
  description: ""
  tagline: ""

brands:
  - name: ""
    website: ""

services: []

locations: []

social_profiles: []

==================================================
35. EXECUTION ORDER
==================================================

DO NOT attempt to build everything blindly in one step.

Build in phases.

PHASE 1
Architecture
Platform research
Repository
Database
Docker
Documentation

PHASE 2
Master company profile
PostgreSQL
API backend
Dashboard foundation

PHASE 3
Ollama
Profile transformation engine
Validation engine

PHASE 4
Google ecosystem
Search Console
Analytics
Business Profile
Bing

PHASE 5
Meta
Facebook
Instagram

PHASE 6
LinkedIn
X
YouTube
Pinterest
Reddit

PHASE 7
WordPress
Medium
Substack
Ghost
DEV
Hashnode

PHASE 8
Developer platforms

PHASE 9
Business directories

PHASE 10
Playwright automation where permitted

PHASE 11
SEO engine

PHASE 12
GEO/AI visibility

PHASE 13
Analytics/reporting

PHASE 14
Testing/security

==================================================
36. GIT WORKFLOW
==================================================

Create meaningful commits:

feat: initialize omnichannel architecture
feat: add postgres schema
feat: add master profile engine
feat: add ollama profile generator
feat: add google integrations
feat: add meta integrations
feat: add social integrations
feat: add playwright framework
feat: add seo engine
feat: add geo monitoring
feat: add dashboard
test: add integration tests
docs: add setup documentation

Do not commit secrets.

==================================================
37. FINAL DELIVERABLE
==================================================

At the end provide:

1. Complete folder tree
2. All generated files
3. Installation instructions
4. Docker commands
5. Database migration commands
6. Ollama setup
7. n8n setup
8. OAuth setup instructions
9. API credential checklist
10. Platform capability matrix
11. Platform-by-platform automation status
12. Manual action list
13. Testing instructions
14. Backup instructions
15. Security checklist
16. Production deployment instructions
17. Maintenance instructions

==================================================
38. MOST IMPORTANT RULE
==================================================

DO NOT SAY:

"Here is how you could build it."

BUILD IT.

If a component cannot be implemented because credentials, approval, API access, or platform restrictions are required:

1. Create the integration interface.
2. Create the configuration.
3. Create the documentation.
4. Create mock/test implementation.
5. Create the manual-action fallback.
6. Clearly mark what credential/access is still required from me.

Do not fabricate successful integrations.

==================================================
39. DEFINITION OF DONE
==================================================

The project is considered complete only when:

[ ] Repository exists
[ ] Docker Compose works
[ ] PostgreSQL works
[ ] n8n works
[ ] Ollama works
[ ] API works
[ ] Dashboard works
[ ] Master profile works
[ ] Platform registry works
[ ] API adapters are modular
[ ] Playwright framework works
[ ] Profile generator works
[ ] Profile validator works
[ ] Profile completeness works
[ ] NAP checker works
[ ] SEO engine works
[ ] Content engine works
[ ] Approval engine works
[ ] Manual action queue works
[ ] Analytics works
[ ] Reports work
[ ] Error handling works
[ ] Audit logging works
[ ] Tests exist
[ ] Documentation exists
[ ] No secrets are committed
[ ] No fabricated API endpoints exist
[ ] No prohibited automation is implemented

==================================================
40. START NOW
==================================================

First:

A. Inspect the current repository.

B. Determine what already exists.

C. Create:

docs/platform-matrix.md

D. Research all listed platforms using CURRENT OFFICIAL documentation.

E. Produce a capability matrix.

F. Identify:
- API available
- API unavailable
- API restricted
- browser automation feasible
- browser automation prohibited/unsafe
- manual-only

G. Then create the project architecture.

H. Then implement Phase 1.

I. After each phase:
- run tests
- validate files
- report what was completed
- report what credentials/access I must provide
- continue to the next phase unless blocked

Do not repeatedly ask me for permission for ordinary implementation decisions.

Make sensible engineering decisions yourself.

When credentials or human verification are genuinely required, stop only at that specific point and tell me exactly what I need to provide.

The final system must be modular so that additional platforms can be added later without redesigning the entire architecture.

BEGIN.

**Ek important point:** Claude ko ye command dene ke baad bhi **API keys/OAuth approvals aapko khud generate karne padenge**. Claude research, code, n8n workflows, Playwright framework, database, Docker, prompts, documentation etc. bana sakta hai; aapke private platform credentials ko khud generate nahi kar sakta.

Aur main deliberately prompt mein **"API nahi hai to Playwright se har haal mein karo"** nahi rakh raha hoon—platform restrictions ko bypass karna long-term mein aapke accounts ko risk mein daal sakta hai. Is architecture mein **API → permitted automation → manual queue** fallback hai.

---

# you asked

message time: 2026-08-16 10:15:16

mere pas company ki profile ek jagah pahle se bani hui hai,

---

# chatgpt response

Haan bhai, **toh aur easy ho jayega**. Agar company ki complete profile ek jagah already bani hui hai, to usko **Master Source of Truth** bana do.

Claude ko naya data manually bharwane ke bajay workflow ye hona chahiye:

```text
Existing Company Profile
        ↓
Import / Parse
        ↓
PostgreSQL Master Profile
        ↓
Ollama
        ↓
Platform-specific versions
        ↓
Validation
        ↓
Approval
        ↓
API / Playwright
        ↓
All Platforms
        ↓
Verification + Report
```

### Claude ko kya karna hai

Aap **existing profile ki file/document Claude ko doge**, aur Claude:

1. uska पूरा data extract करेगा
2. fields को normalize करेगा
3. missing information identify करेगा
4. PostgreSQL में Master Profile बनाएगा
5. हर platform के character limits के हिसाब से versions बनाएगा
6. existing profile से factual information ही use करेगा
7. जहाँ information missing है वहाँ **`MISSING`** mark करेगा
8. फिर APIs/Playwright से profiles update करने की तैयारी करेगा.

**Best practice:** आपकी existing profile को `source_of_truth` मानेंगे। AI को company के बारे में कोई नया factual claim खुद से बनाने की अनुमति नहीं होगी।

Agar aap **wo existing company profile file/document Claude ko dene wale hain**, to master command mein ek छोटा section add karna chahiye jo Claude ko kahe: **“पहले इस document को ingest करो, फिर उसी को canonical company profile बनाओ.”**

---

# you asked

message time: 2026-08-16 10:21:22

tumhare hisabse muje kya karna chahiye, kisi document me apni profile ko store kar lena chahiye ya fir ai pe depend karna chahiye, jab mujje profile change karni hogi to kaise karu, document me poori profile bana ke usko approve karke fir postgree me store kar du to wo apne ap le lega

---

# chatgpt response

Bilkul — **aapka idea sahi hai**, aur main AI ko primary source banane ke bajay **approved master document/database ko Source of Truth** rakhunga.

### Best architecture

```text
MASTER PROFILE DOCUMENT
        ↓
Human approval
        ↓
PostgreSQL = Source of Truth
        ↓
n8n detects changes
        ↓
Ollama adapts wording per platform
        ↓
Validation
        ↓
Approval (if required)
        ↓
API / Playwright
        ↓
All platforms updated
```

### Aapko practically kya karna chahiye?

**1. Ek Master Company Profile document banao**

Example:

`/company/master-profile.md`

Isme complete approved information:

- Company name
- Legal name
- Founder
- About
- Short description
- Long description
- Tagline
- Mission
- Vision
- USP
- Services
- Industries
- Target countries
- Locations
- Contact details
- Website
- Social links
- Certifications
- Awards
- Important facts
- Approved keywords
- Brand tone
- Logo/banner references

**2. Jab bhi profile change karni ho:**

Document edit karo → changes review karo → **APPROVED** mark/commit karo.

Example:

```text
Version 1.4

Added:
AI Agent Development

Changed:
Digital Marketing description

Removed:
Old service X
```

**3. n8n automatically detect kare**

```text
Git/file changed
       ↓
n8n
       ↓
Compare old vs new
       ↓
Update PostgreSQL
       ↓
Find affected platforms
       ↓
Ollama generates platform versions
       ↓
Validation
       ↓
Update queue
```

### PostgreSQL ka role

**Document = human-readable master**

**PostgreSQL = machine-readable operational database**

Isliye sirf PostgreSQL में manually editing मत करो।

आपका rule होना चाहिए:

> **Master Document → Approved → PostgreSQL → Automation**

इससे future में अगर आप कहें:

> "Nivy अब AI automation भी provide करती है."

तो आपको 30 platforms अलग-अलग खोलने की जरूरत नहीं होगी।

Master document में एक बार change → system बाकी platforms के लिए changes identify करेगा.

### और एक महत्वपूर्ण चीज

मैं **Git + Markdown/YAML** recommend करूंगा, Google Docs को primary source नहीं।

क्योंकि इससे आपके पास:

- Version history
- Who changed what
- Approval
- Rollback
- Audit trail
- AI-readable format
- n8n integration

सब मिलेगा।

**Final recommendation:**

> **Approved Master Profile in Git → PostgreSQL → n8n → Ollama → APIs/Playwright**

यही आपके लिए सबसे मजबूत architecture होगा।

---

# you asked

message time: 2026-08-16 10:24:30

thk hai mai chahta hu github ka koi url de dunga, usko url ko mai bad me edit kar pau

---

# chatgpt response

Haan bhai, **ye actually aur better approach hai.** Aap ek GitHub repository mein Master Profile rakho aur uska URL Claude/n8n ko de do.

Recommended structure:

```text
GitHub Repository
└── company-profile/
    ├── master-profile.md        ← main profile
    ├── company-facts.yaml       ← structured facts
    ├── services.yaml
    ├── brands.yaml
    ├── social-profiles.yaml
    └── assets/
```

### Aapka workflow

```text
GitHub Master Profile
        ↓
Edit whenever needed
        ↓
Commit / approve
        ↓
n8n detects change
        ↓
PostgreSQL sync
        ↓
Ollama creates platform versions
        ↓
Validation
        ↓
API / Playwright
        ↓
Social + SEO platforms
```

**Important:** sirf GitHub ka public URL dene se n8n automatically changes nahi jaanega. Hum **GitHub webhook → n8n** laga denge. Jaise hi aap approved profile commit karoge, n8n workflow trigger ho jayega.

Aur agar repository **private** rakhni hai, to bhi possible hai—n8n ko GitHub OAuth/token ke through access denge.

Aapke case mein main **GitHub को Master Profile CMS की तरह** use karunga, aur PostgreSQL ko **automation database**.

---

# you asked

message time: 2026-08-16 10:25:18

thik hai to mere liye poora cluadecommand bana do iske lilye

---

# chatgpt response

Bilkul. Aapke case mein main architecture ko **GitHub Master Profile → PostgreSQL → n8n → Ollama → API/Playwright → all platforms** rakhunga.

Neeche wala **single copy-paste master command Claude Code** ko do. Isme Claude ko GitHub repository create karne ke बजाय existing/new repo ko structure karna, master profile ko source of truth banana, automatic sync, versioning, approval aur social/SEO automation sab build karna hai.

**Document Title: **

# MASTER COMMAND
## GitHub Master Company Profile + Omnichannel Social, SEO & GEO Automation System

You are my senior software architect, automation engineer, DevOps engineer, AI engineer, SEO engineer and GitHub/n8n/Playwright specialist.

I want you to BUILD a production-ready system that uses a GitHub repository as the **single human-approved Master Company Profile / Source of Truth**.

Do not merely explain the architecture.

Create the repository structure, files, database schema, n8n workflows, APIs, Playwright framework, Ollama prompts, documentation, tests and deployment configuration.

==================================================
1. CORE PRINCIPLE
==================================================

The most important rule of this project is:

GITHUB MASTER PROFILE
        ↓
HUMAN EDIT
        ↓
HUMAN APPROVAL
        ↓
GIT COMMIT
        ↓
GITHUB WEBHOOK
        ↓
N8N
        ↓
VALIDATE + PARSE
        ↓
POSTGRESQL
        ↓
OLLAMA
        ↓
PLATFORM-SPECIFIC CONTENT
        ↓
VALIDATION
        ↓
APPROVAL IF REQUIRED
        ↓
OFFICIAL API / PERMITTED PLAYWRIGHT
        ↓
PLATFORM UPDATE
        ↓
VERIFICATION
        ↓
AUDIT LOG + REPORT

GitHub is the human-readable canonical source.

PostgreSQL is the machine-readable operational database.

Ollama is the AI transformation layer.

n8n is the orchestration layer.

Official APIs are preferred.

Playwright is only the fallback where automation is permitted and technically appropriate.

==================================================
2. EXISTING COMPANY PROFILE
==================================================

I already have my company profile prepared somewhere.

I may provide you:

- an existing GitHub URL
- an existing Markdown file
- an existing document
- YAML/JSON
- text
- or a combination of these.

FIRST inspect the provided source.

Do not rewrite or invent company information.

Extract the existing information and convert it into the new Master Profile structure.

If information is ambiguous, mark it:

NEEDS_REVIEW

If information is missing:

MISSING

Never invent factual company information.

==================================================
3. GITHUB AS SOURCE OF TRUTH
==================================================

Create/use a GitHub repository such as:

company-master-profile

or:

nivy-company-os

The repository must contain:

company-profile/
├── master-profile.md
├── company-facts.yaml
├── brands.yaml
├── services.yaml
├── industries.yaml
├── locations.yaml
├── people.yaml
├── contact.yaml
├── social-profiles.yaml
├── keywords.yaml
├── competitors.yaml
├── certifications.yaml
├── awards.yaml
├── brand-guidelines.yaml
└── assets/

The most important file is:

master-profile.md

This should be human-readable.

The YAML files should contain structured information required by automation.

==================================================
4. MASTER PROFILE CONTENT
==================================================

Create fields for:

Company name
Legal name
Brand name
Founder
Leadership
Website
Email
Phone
Address
Country
City
Locations
Founded year
Short description
Medium description
Long description
Tagline
Mission
Vision
USP
Services
Industries
Target audiences
Target countries
Target cities
Keywords
Competitors
Certifications
Awards
Achievements
Social links
Business directory links
Contact information
Brand tone
Brand voice
Approved claims
Restricted claims
Important company facts

Also support:

brands
sub-brands
products
services
business units

==================================================
5. SOURCE OF TRUTH RULES
==================================================

Implement these rules:

RULE 1:
GitHub approved profile is the canonical source.

RULE 2:
PostgreSQL must not become an independent source of truth.

RULE 3:
AI-generated information must NEVER overwrite canonical facts automatically.

RULE 4:
Ollama may rewrite/adapt factual information but may not invent facts.

RULE 5:
Platform-specific versions are derivatives of the Master Profile.

RULE 6:
If a platform contains information not present in Master Profile, flag it.

RULE 7:
Human approval is required for important factual changes.

RULE 8:
Every change must be versioned.

==================================================
6. PROFILE VERSIONING
==================================================

Every approved profile change must have:

version
commit SHA
author
date
change summary
changed fields
previous value
new value
approval status

Example:

Version: 1.4.0

Changed:
- Added AI Agent Development service
- Updated company description

Reason:
Business service expansion

Status:
APPROVED

==================================================
7. GITHUB WORKFLOW
==================================================

Create GitHub Actions where useful.

Implement:

Pull Request
↓
Validation
↓
Schema validation
↓
Fact validation
↓
Character validation
↓
Broken-link check
↓
Human approval
↓
Merge
↓
Webhook
↓
n8n

Do not automatically publish unapproved profile changes.

==================================================
8. GITHUB WEBHOOK → N8N
==================================================

Create an n8n webhook endpoint:

POST /webhooks/github/master-profile

The workflow should:

1. Receive GitHub webhook.
2. Verify webhook signature.
3. Determine repository.
4. Determine branch.
5. Determine commit SHA.
6. Determine changed files.
7. Ignore irrelevant files.
8. Fetch changed profile files.
9. Validate them.
10. Parse them.
11. Compare old/new version.
12. Update PostgreSQL.
13. Determine affected platforms.
14. Generate platform-specific changes.
15. Put changes into approval queue.
16. Publish automatically only where configured as AUTO.
17. Log everything.

==================================================
9. POSTGRESQL
==================================================

Create PostgreSQL schema.

Tables:

companies
brands
people
services
industries
locations
contacts
social_profiles
websites
keywords
competitors
certifications
awards
assets
brand_guidelines

master_profile_versions
master_profile_changes

platforms
platform_capabilities
platform_accounts
platform_profiles
platform_profile_fields

generated_profiles
profile_validations
profile_completeness

content
content_variants
content_publications

seo_properties
keywords
keyword_rankings
serps
backlinks
mentions
reviews
nap_records
geo_visibility

automation_jobs
automation_runs
automation_errors
manual_actions

approval_requests
audit_logs

Add:

UUIDs
foreign keys
indexes
timestamps
soft delete where useful

==================================================
10. DATABASE SYNC
==================================================

Create:

GitHub
→ Parse
→ Normalize
→ Validate
→ PostgreSQL

The database must store:

canonical_value
source
source_commit
source_file
version
updated_at

Never silently overwrite data.

==================================================
11. PLATFORM REGISTRY
==================================================

Create a database registry containing every target platform.

For every platform store:

platform_name
category
official_url
developer_url
documentation_url
api_available
oauth_available
profile_api
publishing_api
analytics_api
browser_automation_possible
browser_automation_allowed
manual_only
rate_limit
pricing
access_requirements
last_verified
notes

NEVER invent API information.

Research current official documentation.

==================================================
12. SOCIAL PLATFORMS
==================================================

Research and support where possible:

Facebook Pages
Instagram
LinkedIn Personal
LinkedIn Company Page
X/Twitter
YouTube
TikTok
Pinterest
Reddit
Threads
Snapchat
Telegram
Discord
Quora
Medium
Tumblr
Mastodon
Bluesky

==================================================
13. SEARCH / WEBMASTER
==================================================

Research:

Google Search Console
Google Business Profile
Google Analytics
Google Trends
Google Ads Keyword Planner
Google PageSpeed Insights
Google Lighthouse
Bing Webmaster Tools
Bing Places
Yandex Webmaster
Naver Search Advisor
Baidu Webmaster Tools

==================================================
14. LOCAL / BUSINESS SEO
==================================================

Research:

Google Business Profile
Bing Places
Apple Business Connect
Yelp
Foursquare
Tripadvisor
Yellow Pages
MapQuest
HERE
Waze
BBB
Hotfrog
Manta
Chamber of Commerce
Crunchbase
Clutch
GoodFirms
DesignRush
Sortlist
UpCity
G2
Capterra
Trustpilot

Do not create duplicate or false listings.

==================================================
15. CONTENT PLATFORMS
==================================================

Research:

WordPress
Medium
Substack
Blogger
Ghost
Tumblr
Hashnode
DEV Community
Vocal
LinkedIn Articles
Reddit
Quora

==================================================
16. VIDEO PLATFORMS
==================================================

Research:

YouTube
Vimeo
TikTok
Instagram Reels
Facebook Video
Dailymotion
Twitch
Rumble

==================================================
17. DEVELOPER / TECH PLATFORMS
==================================================

Research:

GitHub
GitLab
Bitbucket
Stack Overflow
Stack Exchange
DEV
Hashnode
CodePen
Product Hunt
Hacker News
Kaggle

==================================================
18. DESIGN PLATFORMS
==================================================

Research:

Behance
Dribbble
ArtStation
DeviantArt
Vimeo
Pinterest
Adobe Portfolio

==================================================
19. STARTUP / COMPANY DATABASES
==================================================

Research:

Crunchbase
Wellfound
F6S
Gust
StartupBlink
Tracxn
Dealroom
Product Hunt

==================================================
20. SEO PROVIDERS
==================================================

Create optional adapters for:

Semrush
Ahrefs
Moz
DataForSEO
SerpApi
Similarweb
Majestic

The core system must work without paid SEO APIs.

==================================================
21. AI / GEO VISIBILITY
==================================================

Create a measurable AI/GEO monitoring layer for:

Google AI search surfaces
Bing/Copilot
Perplexity
ChatGPT-related discoverability
Gemini
Claude
You.com
Brave Search

Do not claim an AI ranking API exists unless officially documented.

Classify each integration:

OFFICIAL_API
INDIRECT_MEASUREMENT
MANUAL
UNAVAILABLE

==================================================
22. OLLAMA
==================================================

Use Ollama for AI transformations.

Environment variables:

OLLAMA_BASE_URL
OLLAMA_MODEL

Create prompts for:

profile adaptation
bio generation
about generation
headline generation
social description
service descriptions
SEO titles
meta descriptions
content generation
content repurposing
keyword clustering
search intent
competitor analysis
content gap
review sentiment
review response drafting
NAP consistency
entity consistency
GEO analysis

Every prompt must include:

"Use only facts supplied by the approved Master Profile.
Never invent company facts."

==================================================
23. PLATFORM PROFILE GENERATOR
==================================================

Build:

Master Profile
↓
Platform Adapter
↓
Platform-specific profile

Examples:

LinkedIn
Instagram
Facebook
X
YouTube
TikTok
Pinterest
Reddit
Quora
Medium
etc.

Each generated version must respect:

character limits
URL limits
formatting
platform-specific fields
platform-specific terminology

==================================================
24. PROFILE COMPLETENESS
==================================================

For every platform calculate:

Profile Completeness Score

Check:

name
username
profile image
banner
bio
about
website
email
phone
location
category
services
CTA
links
keywords
description

Example:

LinkedIn: 92%
Instagram: 100%
X: 85%

Create dashboard.

==================================================
25. PROFILE CHANGE DETECTION
==================================================

When Master Profile changes:

Detect changed fields.

Example:

Old:
Digital Marketing

New:
AI-powered Digital Marketing and Automation

Determine which platforms are affected.

Example:

Website description
LinkedIn About
Facebook About
Instagram Bio
X Bio
YouTube About

Only regenerate affected derivatives.

Do not unnecessarily modify unrelated profiles.

==================================================
26. APPROVAL SYSTEM
==================================================

Every generated change gets:

DRAFT
↓
VALIDATION
↓
APPROVAL_REQUIRED
↓
APPROVED
↓
PUBLISHED

Support:

AUTO
APPROVAL_REQUIRED
MANUAL_ONLY

Default important profile changes to:

APPROVAL_REQUIRED

==================================================
27. OFFICIAL APIs
==================================================

For each platform:

Research current official API documentation.

Use official API wherever possible.

Store credentials using:

environment variables
OAuth
Docker secrets
secure credential storage

Never hardcode credentials.

Create reusable integration interface:

authenticate()
getProfile()
updateProfile()
publish()
getAnalytics()
verify()

Only implement methods supported by the platform.

==================================================
28. PLAYWRIGHT
==================================================

Create a reusable TypeScript Playwright framework.

Structure:

browser/
├── core/
├── sessions/
├── adapters/
├── pages/
├── selectors/
├── validators/
├── screenshots/
├── storage/
└── tests/

Use Playwright only when:

- API is unavailable
- automation is permitted
- account access is legitimate
- no security bypass is required

NEVER bypass:

CAPTCHA
MFA
anti-bot systems
rate limits
access controls
security challenges

If automation is not allowed:

MANUAL_ONLY

==================================================
29. N8N WORKFLOWS
==================================================

Create importable JSON workflows:

github_profile_webhook.json

github_profile_sync.json

profile_change_detector.json

master_profile_parser.json

master_profile_validator.json

postgres_profile_sync.json

platform_profile_generator.json

profile_completeness.json

platform_api_sync.json

playwright_profile_sync.json

approval_queue.json

manual_action_queue.json

social_content_generator.json

content_repurposing.json

content_distribution.json

google_search_console.json

google_business_profile.json

bing_webmaster.json

seo_audit.json

keyword_monitoring.json

serp_monitoring.json

backlink_monitoring.json

competitor_monitoring.json

brand_mentions.json

review_monitoring.json

nap_consistency.json

entity_consistency.json

geo_visibility.json

weekly_report.json

monthly_report.json

error_retry.json

platform_health_check.json

==================================================
30. CONTENT ENGINE
==================================================

Create a master content workflow.

ONE MASTER CONTENT
↓
AI transformation
↓
LinkedIn
X
Facebook
Instagram
Threads
Pinterest
Reddit
Quora
YouTube
Newsletter
Blog

Do not simply copy/paste identical content.

Each platform must receive native formatting.

==================================================
31. SEO ENGINE
==================================================

Build:

technical SEO
on-page SEO
keyword clustering
search intent
competitor research
content gap
internal linking
schema recommendations
meta title
meta description
heading analysis
image ALT
Core Web Vitals
indexing
sitemap
robots.txt
canonical
structured data

==================================================
32. ENTITY SEO
==================================================

Create:

ENTITY_CONSISTENCY_SCORE

Track:

company
brand
founder
services
industry
location
website
social profiles
directories

Detect contradictions.

==================================================
33. NAP CONSISTENCY
==================================================

Compare:

Name
Address
Phone
Website
Email
Hours
Category

across platforms.

Generate:

NAP_CONSISTENCY_REPORT

==================================================
34. MANUAL ACTION QUEUE
==================================================

When automation is unavailable:

create manual task.

Fields:

platform
action
instructions
required_data
status
assigned_to
evidence
created_at
completed_at

The dashboard must clearly show:

MANUAL ACTION REQUIRED

Never pretend a manual action was completed.

==================================================
35. AUDIT LOG
==================================================

Every change must log:

timestamp
source
commit SHA
user
platform
field
old value
new value
method
approval
status
error

Never log secrets.

==================================================
36. DASHBOARD
==================================================

Create Next.js dashboard.

Pages:

/dashboard
/company
/master-profile
/versions
/changes
/platforms
/profiles
/profile-completeness
/approvals
/manual-actions
/content
/content-calendar
/seo
/keywords
/serps
/backlinks
/competitors
/mentions
/reviews
/local-seo
/nap
/entity
/geo
/analytics
/reports
/automation
/errors
/settings

==================================================
37. MASTER PROFILE EDITING
==================================================

The dashboard may display/edit the Master Profile.

However:

The canonical editable files remain in GitHub.

Preferred workflow:

Dashboard edit
↓
Generate Git branch
↓
Create commit/PR
↓
Validation
↓
Human approval
↓
Merge
↓
Webhook
↓
n8n
↓
PostgreSQL

Do not silently change PostgreSQL without updating GitHub.

==================================================
38. GITHUB URL
==================================================

I want to be able to provide one GitHub repository URL later.

Example:

https://github.com/OWNER/REPOSITORY

The system must be configurable through:

GITHUB_REPOSITORY
GITHUB_BRANCH
GITHUB_MASTER_PROFILE_PATH

Example:

GITHUB_REPOSITORY=owner/company-master-profile
GITHUB_BRANCH=main
GITHUB_MASTER_PROFILE_PATH=company-profile/master-profile.md

The repository URL should be changeable through configuration.

Do not hardcode it into source code.

==================================================
39. PRIVATE REPOSITORY SUPPORT
==================================================

Support both:

PUBLIC repository
PRIVATE repository

For private repositories use GitHub OAuth/token/app authentication.

Never store GitHub tokens in source code.

==================================================
40. GITHUB CHANGE DETECTION
==================================================

Support:

GitHub Webhooks

and optionally:

scheduled polling

Fallback:

If webhook fails, scheduled n8n workflow checks the latest commit SHA.

Store:

last_processed_commit_sha

If:

current_commit_sha != last_processed_commit_sha

then process changes.

==================================================
41. PROFILE IMPORT
==================================================

Create an importer that can read:

Markdown
YAML
JSON

Normalize into PostgreSQL.

Example:

master-profile.md
+
company-facts.yaml
+
services.yaml

→ normalized Master Profile.

==================================================
42. VALIDATION
==================================================

Before syncing:

Validate:

required fields
URLs
emails
phone
character limits
duplicate information
invalid claims
missing values
conflicting values
schema
YAML syntax
Markdown structure

Block invalid changes.

==================================================
43. SECURITY
==================================================

Implement:

OAuth
secret management
RBAC
audit logging
input validation
rate limiting
CSRF protection
secure cookies
session isolation
token refresh
secret redaction

Roles:

ADMIN
MANAGER
MARKETING
SEO
EDITOR
VIEWER

==================================================
44. DOCKER
==================================================

Create:

docker-compose.yml

Services:

postgres
n8n
ollama
api
worker
web

Add health checks and persistent volumes.

Use Redis only if required.

==================================================
45. PROJECT STRUCTURE
==================================================

Create:

company-automation/
│
├── README.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
│
├── company-profile/
│   ├── master-profile.md
│   ├── company-facts.yaml
│   ├── brands.yaml
│   ├── services.yaml
│   ├── industries.yaml
│   ├── locations.yaml
│   ├── people.yaml
│   ├── contact.yaml
│   ├── social-profiles.yaml
│   ├── keywords.yaml
│   ├── competitors.yaml
│   ├── certifications.yaml
│   ├── awards.yaml
│   └── assets/
│
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
│
├── n8n/
│   ├── workflows/
│   └── README.md
│
├── apps/
│   ├── api/
│   ├── web/
│   └── worker/
│
├── integrations/
│   ├── github/
│   ├── google/
│   ├── meta/
│   ├── linkedin/
│   ├── x/
│   ├── youtube/
│   ├── pinterest/
│   ├── reddit/
│   ├── wordpress/
│   ├── github/
│   ├── gitlab/
│   ├── telegram/
│   ├── discord/
│   ├── seo/
│   └── directories/
│
├── browser/
│   ├── core/
│   ├── sessions/
│   ├── adapters/
│   ├── pages/
│   ├── selectors/
│   ├── validators/
│   └── tests/
│
├── ai/
│   ├── prompts/
│   ├── ollama/
│   ├── profile-generator/
│   ├── content-generator/
│   ├── seo-analyzer/
│   └── geo-monitor/
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   ├── github-source-of-truth.md
│   ├── platform-matrix.md
│   ├── api-setup.md
│   ├── playwright.md
│   ├── n8n.md
│   ├── ollama.md
│   ├── seo.md
│   ├── geo.md
│   ├── security.md
│   └── troubleshooting.md
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── platform/
│
└── scripts/
    ├── setup.sh
    ├── migrate.sh
    ├── backup.sh
    └── health-check.sh

==================================================
46. ENVIRONMENT VARIABLES
==================================================

Create .env.example.

Include:

GITHUB_REPOSITORY=
GITHUB_BRANCH=main
GITHUB_MASTER_PROFILE_PATH=
GITHUB_WEBHOOK_SECRET=

DATABASE_URL=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

N8N_ENCRYPTION_KEY=

OLLAMA_BASE_URL=
OLLAMA_MODEL=

GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

META_APP_ID=
META_APP_SECRET=

LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=

X_CLIENT_ID=
X_CLIENT_SECRET=

REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=

PINTEREST_CLIENT_ID=
PINTEREST_CLIENT_SECRET=

WORDPRESS_URL=
WORDPRESS_CLIENT_ID=
WORDPRESS_CLIENT_SECRET=

SEM_RUSH_API_KEY=
AHREFS_API_KEY=
MOZ_API_KEY=
DATAFORSEO_LOGIN=
DATAFORSEO_PASSWORD=
SERPAPI_KEY=

Only include credentials that are actually required.

==================================================
47. PLATFORM RESEARCH
==================================================

Create:

docs/platform-matrix.md

For every platform include:

Platform
Category
Official URL
Developer URL
Official API
Documentation
OAuth
Profile update
Publishing
Analytics
Browser automation
Allowed?
Manual required?
Rate limits
Pricing
Access requirements
Implementation status
Last verified

Use CURRENT official documentation.

If unknown:

UNKNOWN

Never guess.

==================================================
48. IMPORTANT API RULE
==================================================

Do not fabricate:

API endpoints
OAuth scopes
permissions
rate limits
pricing
features

If the API requires application approval, document it.

If the API does not allow a required action, do not pretend it does.

==================================================
49. PLAYWRIGHT RULE
==================================================

Playwright must never be used to bypass platform security.

If a platform prevents automation:

stop automation
create manual task
record reason

==================================================
50. REPORTING
==================================================

Generate:

Daily automation report
Weekly social report
Weekly SEO report
Monthly SEO report
Profile completeness report
Platform health report
NAP report
Entity consistency report
GEO visibility report
Failed automation report

==================================================
51. CHANGE IMPACT REPORT
==================================================

When I change the Master Profile, generate:

CHANGE IMPACT REPORT

Example:

Changed:
Services

Affected:

LinkedIn About
Facebook About
Instagram Bio
YouTube About
Website structured data
Google Business Profile
Clutch profile
GoodFirms profile

Not affected:

X username
GitHub username
Founder profile

This is extremely important.

==================================================
52. DRY RUN MODE
==================================================

Before publishing changes, support:

DRY_RUN=true

In dry-run mode:

Do everything except external changes.

Show:

platform
field
old value
new value
reason
source
approval
action

==================================================
53. ROLLBACK
==================================================

If a bad profile update occurs:

GitHub version rollback
↓
n8n detects rollback
↓
PostgreSQL updated
↓
affected platforms identified
↓
reversal changes generated
↓
approval
↓
platform update

==================================================
54. TEST MODE
==================================================

Create:

TEST_MODE=true

No external publishing in test mode.

Use mocked APIs.

==================================================
55. DEFINITION OF DONE
==================================================

The project is complete when:

[ ] GitHub Master Profile exists
[ ] Markdown profile exists
[ ] YAML structured profile exists
[ ] GitHub versioning works
[ ] GitHub webhook works
[ ] n8n receives webhook
[ ] PostgreSQL schema works
[ ] GitHub → PostgreSQL sync works
[ ] Change detection works
[ ] Change impact analysis works
[ ] Ollama profile transformation works
[ ] Platform-specific profile generation works
[ ] Validation works
[ ] Approval workflow works
[ ] API adapters exist where officially supported
[ ] Playwright framework exists
[ ] Manual action queue exists
[ ] Profile completeness works
[ ] NAP consistency works
[ ] Entity consistency works
[ ] SEO engine exists
[ ] GEO monitoring exists
[ ] Dashboard exists
[ ] Audit logs exist
[ ] Error handling exists
[ ] Retry mechanism exists
[ ] Docker setup works
[ ] Tests exist
[ ] Documentation exists
[ ] No secrets committed
[ ] No fabricated APIs
[ ] No prohibited automation
[ ] Dry-run mode works
[ ] Rollback mechanism exists

==================================================
56. IMPLEMENTATION ORDER
==================================================

Do not attempt to blindly implement everything at once.

PHASE 1
Inspect existing repository and existing company profile.

PHASE 2
Create GitHub Master Profile structure.

PHASE 3
Create PostgreSQL schema.

PHASE 4
Create GitHub → n8n → PostgreSQL synchronization.

PHASE 5
Create Ollama profile transformation.

PHASE 6
Create platform registry and research matrix.

PHASE 7
Implement official APIs.

PHASE 8
Implement permitted Playwright adapters.

PHASE 9
Create profile completeness and consistency engine.

PHASE 10
Create social/content automation.

PHASE 11
Create SEO engine.

PHASE 12
Create GEO engine.

PHASE 13
Create dashboard.

PHASE 14
Testing/security/production deployment.

==================================================
57. FIRST ACTION
==================================================

DO NOT start by writing random code.

First inspect the current repository.

Then ask me for the existing GitHub repository URL ONLY if I have not provided one.

If I have already provided a repository URL, inspect it.

Then inspect the existing company profile.

Create:

docs/platform-matrix.md

and:

docs/github-source-of-truth.md

Then show me:

1. Existing repository structure
2. Existing company profile structure
3. Information successfully extracted
4. Missing information
5. Conflicting information
6. Proposed new Master Profile structure
7. Platform capability matrix
8. Implementation plan

After that begin implementation.

==================================================
58. FINAL RULE
==================================================

The system must make future company profile changes extremely simple.

My desired future workflow is:

I edit:

company-profile/master-profile.md

I review it.

I commit it.

Then automatically:

GitHub
→ webhook
→ n8n
→ validation
→ PostgreSQL
→ change detection
→ Ollama
→ platform-specific versions
→ approval
→ APIs/Playwright
→ verification
→ report

I should NOT have to manually edit 30–50 social profiles every time the company's approved description, service list, tagline, contact details, website or other master information changes.

Build the system around this principle.

BEGIN.

---
Powered by [AI Exporter](https://saveai.net)