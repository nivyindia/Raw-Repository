# Growth Engine — Build Order

**Companion to:** `Growth-Engine-Unified-Automation-Blueprint.md`
**Purpose:** the sequence to actually build the two funnels — infra first, one stage/channel at a time, tested with real data before chaining forward. Don't install every tool in Part III up front and don't bulk-import templates before testing them.

---

## Sales Funnel Build Order

### 1. Stand up hosting first
Get a VPS (or your existing server) with Docker + Portainer/Coolify running. Everything else in this stack — n8n, Odoo, Mautic, databases — runs as containers on top of this, so this is the one true prerequisite before anything else.

### 2. Deploy the core software, not the templates
Install n8n (self-hosted), your CRM (Odoo Community per your funnel doc), PostgreSQL, and Mautic/Listmonk for email. Get each one reachable and logged into on its own — confirm CRM has a lead table, n8n's UI loads — before touching a single workflow template.

### 3. Connect real credentials once
In n8n, set up the credential entries you'll reuse across templates: Gmail/SMTP, Google Sheets/Drive, WhatsApp Business API or Fiwano, Notion, and your CRM's API. Templates fail silently or half-run when credentials are missing — this is the most common blocker, so get this done before importing anything.

### 4. Import and test Stage 1–2 only
Start with the lead-generation/scraping template and the lead-capture-hub template from Part III.6. Import via Workflows → Import from File, rewire it to your actual sheet/CRM, run it once manually with a real test lead, and confirm the data lands where you expect. Do not move forward until this stage works end-to-end with real data.

### 5. Chain forward stage by stage
Only after Stage 1–2 is verified, import Stage 3 (CRM ingestion/enrichment), then Stage 4 (AI qualification), and so on. Each new stage should trigger off the verified output of the one before it, not run in isolation. This is slower but it's the only way to know which stage actually broke when something doesn't work.

### 6. Fill the two flagged gaps as you reach them
When you reach Stage 7 (e-signature), you'll need to separately self-host DocuSeal and its n8n community node since no ready template exists. When you reach Stage 11 (review request send), it's a 2-node build using channels you've already wired in Stage 5 — not a template import.

### 7. Wire the marketing-to-sales handoff last
Only after the 13-stage sales funnel runs solo, connect it to the marketing funnel at the point in Part I.3 — qualified traffic feeding into Stage 2's lead capture hub. Doing this earlier means debugging two unfinished systems at once.

### 8. Add dashboards at the very end
Metabase/Grafana reporting (Stage 13 and the marketing Weekly AI Reports) should be the last thing you build, once there's real data flowing through the funnel to actually report on.

---

## Marketing Funnel Build Order

### 1. Knowledge Base first
Before any AI writes a word of content, your brand voice, offers, SOPs, and FAQs need to live somewhere the AI Brain can read from — Notion, AnythingLLM, or BookStack per Part III.1. Populate this with real content, not placeholders. Everything downstream (content, SEO, strategy) is only as good as what's in here.

### 2. Stand up one AI Brain, not four
Part III.1 lists Ollama, Open WebUI, AnythingLLM, LibreChat, plus Claude/ChatGPT/Gemini as paid options. Pick one to start — if budget allows, a paid model (Claude/ChatGPT) grounded in your Knowledge Base via RAG will outperform a self-hosted model with far less setup pain. Don't stand up all four self-hosted options; that's infra sprawl with no content shipped yet.

### 3. Wire Content, SEO, and Strategy as separate n8n flows
Build the three AI Brain outputs (Content Writing, SEO Optimization, Marketing Strategy) as distinct n8n workflows that pull from the Knowledge Base. Test each in isolation — generate one real blog post, one real keyword list, one real content calendar — before connecting any of them to the Automation Layer.

### 4. Automation Layer: one output channel at a time
The Automation Layer fans out to four places — Website/Blog, Social Scheduling, Email Marketing, CRM Update. Get one working end-to-end first (Website/Blog publishing via WordPress + a webhook is usually the simplest), confirm a real post lands correctly, then add Social Scheduling (Mixpost or Postiz per III.2), then Email (Mautic/Listmonk per III.4), then the CRM Update hook.

### 5. Connect the real channels
Once each automation path works against a test target, point them at your actual accounts: Facebook/Instagram/Pinterest, LinkedIn/X/TikTok, and your real nurture sequences. This is where account credentials and platform API limits become the thing that breaks, so verify one channel before adding the next.

### 6. Analytics last, reports last
Matomo/Plausible/Umami or GA (Part III.5) only becomes useful once real content has been published for a few weeks. Build the Weekly AI Report workflow after there's actual data to report on — this is what feeds back into the Knowledge Base per the flowchart's loop, closing Part I.1.

---

## Note on Overlap

The marketing funnel shares your CRM and n8n instance with the sales funnel (Part I.3 — marketing feeds qualified traffic into Sales Stage 2). If the sales funnel is built first, that infra (n8n, credentials, CRM) is already half-built by the time you get to marketing — you're mainly adding the Knowledge Base and content-generation flows on top, not starting from zero.
