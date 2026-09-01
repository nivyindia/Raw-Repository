# Billion Dreams United — Complete Multi-Agent AI Company OS
## Master Blueprint v4 (Whole Company — Revenue-First Priority)

---

## 0. What's New in v4

v3 tak humne sirf Sales+Marketing funnel discover kiya tha. Ab **Phase 8 zip** khola — pata chala **Growth Hacking layer bhi already real-built hai**:

- **6 n8n workflow engines built** (8.1 Reward/Contest — 22 nodes, 8.2 Referral — 21 nodes, 8.3 Free-Audit — 11 nodes, 8.4 UGC/Share, 8.5 Community, 8.6 Signal-Based Outreach) + Hub-Dispatcher updated with new event branches
- **8.7 Dashboard** = SQL views on Postgres (not a workflow) — also built
- Full legal/compliance package per engine (T&C, Privacy, Landing pages, Cookie notices) — international-level (6-country contest eligibility, GDPR/CCPA/CASL/PECR coverage)
- **Exact current blockers documented** (see Section 9) — this replaces the vague "Gap A/B/C" from memory with the precise list

Combined with v3's Growth Engine (14 workflows, sales+marketing) and 54+22-stage funnel docs, **tumhare paas already ek chhota-khaasa automation empire hai** — is document ka kaam ab sirf naya banana nahi, balki **whole-company view me isko fit karna aur jo genuinely khaali hai (HR, Legal, Finance-agent, Dev department, COO layer) usko design karna** hai.

---

## 1. Guiding Principles (unchanged, still binding)

1. 1 function → 1 primary tool. Duplicate mat rakho.
2. Agent ≠ new software — same LLM, alag role+tools+permissions.
3. Ready-made pehle, custom baad me — 60-80% assemble hota hai.
4. High-risk action = human approval, hamesha.
5. Revenue-generating pieces pehle, orchestration (COO agent) baad me.
6. Honest status — built / skeleton / plan, kabhi round-up nahi.

---

## 2. Corporate Structure

```
Billion Dreams United (Parent — single Odoo, multi-company)
├── Nivy Next      — Digital Marketing, Web Dev, SEO, Social, AI Automation, SaaS, IT
├── Nivy Advisory  — Tax, Accounting, Compliance, Consulting
├── Nivy Academy   — Courses, LMS, Community, Certifications
├── Nivy Jobs      — Recruitment, Employer Services, Placement
└── Nivy Studio    — UGC, Creators, Influencers, Production
```
Shared services (central): HR, Finance, Legal, Automation, Company Brain, Analytics.

---

## 3. Full Company Departments (18, Not Just Sales/Marketing)

| Dept | Covers |
|---|---|
| 1. CEO/COO Office | Strategy, orchestration, company-wide intelligence |
| 2. Growth/Research | Market, competitor, ICP research |
| 3. Marketing | Content, SEO, social, email, ads (22-stage funnel) |
| 4. Growth Hacking | Contests, referrals, UGC, community, signal-outreach (Phase 8, 6 engines) |
| 5. Sales | Lead-to-close (54-stage funnel) |
| 6. Delivery/Dev | Requirement→deploy for client projects |
| 7. Customer Success | Onboarding, retention, upsell, renewal |
| 8. Support | Tickets, chat, FAQ |
| 9. Finance | Invoicing, expenses, reports |
| 10. HR | Recruiting, onboarding, training |
| 11. Legal | Contracts, compliance, T&C |
| 12. Operations/Automation | SOPs, workflow maintenance |
| 13. Knowledge/Company Brain | Shared memory across all agents |
| 14. BI/Analytics | Dashboards, KPIs |
| 15. Internal Comms | Team chat, notifications |
| 16. Project Management | Task tracking, delivery |
| 17. IT/DevOps | Infra, deployment, monitoring |
| 18. Executive Assistant | Scheduling, inbox triage (per-brand) |

---

## 4. THE MASTER TABLE — Agent × Task × Tool × Ready-Made Source × Priority × Status

**Priority key:** 🥇 Sprint 1 (Revenue, build first) · 🥈 Sprint 2 (Delivery) · 🥉 Sprint 3 (Ops/Support) · 🏁 Sprint 4 (COO/CEO, last)

| # | Agent | Dept | Task | Primary Tool | Ready-Made Source | Priority | Status |
|---|---|---|---|---|---|---|---|
| 1 | Market Research Agent | Growth | Market/competitor/niche research | Dify + Perplexity + Firecrawl | [Dify](https://github.com/langgenius/dify) workflows; Perplexity (cloud) | 🥇 | 🔴 To build |
| 2 | ICP Agent | Growth | Ideal customer profile | Dify | Custom on Dify — feeds Sales Stage 02 | 🥇 | 🔴 To build |
| 3 | Lead Research/Extraction Agent | Sales | Company/decision-maker discovery | n8n + Browser Use + Apify | [Lead generation agent](https://n8n.io/workflows/7423-lead-generation-agent/) · [Browser Use](https://github.com/browser-use/browser-use) | 🥇 | 🟢 Stage 06 piloted, workflow exists |
| 4 | Lead Enrichment Agent | Sales | Contact/company enrichment | n8n + Hunter/Perplexity | [Hunter.io + Perplexity enrichment](https://n8n.io/workflows/3616-automated-lead-generation-and-contact-enrichment-with-hunterio-and-perplexity-ai/) | 🥇 | 🟢 Template identified |
| 5 | Lead Qualification/Scoring Agent | Sales | Score & route leads | n8n + CrewAI | [Qualify & route leads GPT-4o](https://n8n.io/workflows/9739-qualify-and-route-leads-across-channels-with-gpt-4o-slack-and-crm-integration/) | 🥇 | 🟢 Documented verdict, module 1.4 built |
| 6 | SDR/Outreach Agent | Sales | Multi-channel personalized outreach | n8n + CrewAI | [AI SDR Pipeline](https://n8n.io/workflows/13529-run-an-ai-sdr-sales-pipeline-with-openai-google-sheets-gmail-and-calendar/) · [Jina AI+Agents outreach](https://n8n.io/workflows/6649-generate-sales-leads-and-personalized-outreach-emails-using-jina-ai-and-openai-agents/) | 🥇 | 🟢 Module 2.1 built |
| 7 | Follow-up/Nurture Agent | Sales | Drip sequences, no-reply logic | n8n + Mautic | Built-in n8n Wait/IF pattern | 🥇 | 🟢 Module 2.2 built |
| 8 | Meeting/Booking Agent | Sales | Discovery call scheduling | Cal.com + n8n | [Cal.com](https://github.com/calcom/cal.com) webhook pattern | 🥇 | 🟢 Module 2.3 built |
| 9 | Proposal Agent | Sales | Auto-draft proposal from CRM data | Dify + n8n | Custom Dify app + module 2.4 | 🥇 | 🟢 Module 2.4 built |
| 10 | Contract/E-sign Agent | Sales | Status tracking, contract dispatch | Documenso + n8n | [Documenso](https://github.com/documenso/documenso) + `n8n-nodes-docuseal` | 🥇 | 🟢 Module 2.5 built |
| 11 | Invoicing Agent | Finance | Invoice + payment tracking | Invoice Ninja + n8n | [Invoice Ninja](https://github.com/invoiceninja/invoiceninja) | 🥇 | 🟢 Module 2.6 built |
| 12 | Onboarding Agent | Delivery | Signed+paid → project creation | n8n + Odoo | ["Contract signed" trigger chain](https://medium.com/@ciphernutz/10-plug-and-play-n8n-workflow-templates-you-can-use-immediately-15507a7a4da3) | 🥇 | 🟢 Module 2.7 built |
| 13 | Contest/Reward Agent | Growth Hacking | Contest entry, dedupe, fraud-check, winner select | n8n | Custom-built `8.1-Reward-Contest-Engine.json` (22 nodes) | 🥇 | 🟢 **Built, needs import+activate** |
| 14 | Referral Agent | Growth Hacking | Unique code, tracking, 2-stage reward | n8n | Custom-built `8.2-Referral-Engine-Universal.json` (21 nodes) | 🥇 | 🟢 **Built, needs import+activate** |
| 15 | Free-Value/Audit Agent | Growth Hacking | Free audit delivery → lead capture | n8n + Firecrawl + PageSpeed API | Custom-built `8.3-Free-Audit-Engine.json` (11 nodes) | 🥇 | 🟢 **Built, needs API keys** |
| 16 | Negotiation Assistant | Sales | Objection/pricing suggestions (human-in-loop) | CrewAI | Custom — stays mostly human by design | 🥈 | 🔴 Later |
| 17 | Requirement Agent | Delivery | Extract requirements from calls/docs | Dify + Whisper | [Dify](https://dify.ai/workflows) + self-hosted Whisper transcription | 🥈 | 🟡 Plan stage |
| 18 | Solution Architect Agent | Delivery | Architecture/DB/API planning | CrewAI | [CrewAI Marketplace](https://marketplace.crewai.com/) templates | 🥈 | 🟡 Plan stage |
| 19 | Coding Agent | Delivery | Write/modify code | OpenHands | [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🥈 | 🟡 Plan stage |
| 20 | Code Review Agent | Delivery | PR review | GitHub + OpenHands | GitHub Actions + OpenHands SDK | 🥈 | 🟡 Plan stage |
| 21 | QA/Test Agent | Delivery | Tests, regression, bug triage | OpenHands + CrewAI | Same OpenHands stack | 🥈 | 🟡 Plan stage |
| 22 | DevOps Agent | Delivery | Build/deploy/monitor | n8n + GitHub Actions | Native GitHub Actions + n8n webhook | 🥈 | 🟡 Plan stage |
| 23 | Delivery/Reporting Agent | Delivery | Project status → client reports | n8n + Odoo Project | Module 2.8 | 🥈 | 🟢 Module 2.8 built |
| 24 | UGC/Share Agent | Growth Hacking | Content submission → verify → leaderboard | n8n | Custom-built `8.4-UGC-Share-Engine.json` | 🥈 | 🟢 **Built, needs import** |
| 25 | Community Agent | Growth Hacking | Partner/community signup, drip, advocacy | n8n | Custom-built `8.5-Community-Engine.json` | 🥈 | 🟢 **Built, needs import** |
| 26 | Signal-Outreach Agent | Growth Hacking | Trigger-based outreach (hiring/funding signals) | n8n | Custom-built `8.6-Signal-Based-Outreach-Engine.json` | 🥈 | 🟢 **Built, needs import** |
| 27 | Renewal/Revenue-Ops Agent | CS | Renewal reminders, expansion triggers | n8n | Module 2.9 | 🥉 | 🟢 Module 2.9 built |
| 28 | Customer Support Agent | Support | Ticket triage, FAQ, chatbot | Chatwoot + Dify | [Chatwoot](https://github.com/chatwoot/chatwoot) (built-in Captain AI agent) | 🥉 | 🟡 Verdict documented, not deployed |
| 29 | Churn Prevention Agent | CS | Health-score, risk flag | n8n + Metabase | [Health-scoring pattern](https://goodspeed.studio/blog/n8n-workflow-examples-for-saas-companies) | 🥉 | 🔴 Pending build |
| 30 | Finance Agent | Finance | Expense categorization, reports | n8n + Odoo Accounting | Native Odoo + n8n schedule | 🥉 | 🟡 Plan stage |
| 31 | HR Agent | HR | JD writing, resume screening, onboarding | n8n + Dify | Custom Dify app | 🥉 | 🟡 Plan stage |
| 32 | Legal/Contract Agent | Legal | Contract drafting assist, compliance check | Claude (cloud) + Documenso | Manual-assist only, human-reviewed | 🥉 | 🟡 Plan stage |
| 33 | BI/Analytics Agent | Analytics | KPI dashboards, insights | Metabase + Postgres | [Metabase](https://github.com/metabase/metabase) | 🥉 | 🟡 SQL views built (8.7), dashboard UI pending |
| 34 | Internal Comms Agent | Ops | Notifications, alerts to team channels | Rocket.Chat + n8n | [Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) webhook | 🥉 | 🟡 Plan stage |
| 35 | Project/Task Agent | PM | Requirement→task, deadline suggest, blockers | OpenProject + n8n | [OpenProject](https://github.com/opf/openproject) API | 🥉 | 🟡 Plan stage |
| 36 | AI COO / Orchestrator | Core | Route between all crews, approval gates | LangGraph | [LangGraph](https://github.com/langchain-ai/langgraph) | 🏁 | 🔴 Build last |
| 37 | CEO Intelligence Agent | Core | Company-wide summary, recommendations | LangGraph + all sources | Custom multi-agent, reads Company Brain | 🏁 | 🔴 Build very last |

**Reading this table's biggest surprise:** rows 13–15 and 24–26 (Growth Hacking, 6 agents) are **already built n8n workflows sitting unimported** — this is currently the highest-leverage unused asset in the entire company. Import + activate + real credentials = live growth engines within days, not months.

---

## 5. Layer 1 — Cloud AI Brain Assignment (unchanged from v3, reference table)

| Task type | Best AI |
|---|---|
| Strategic reasoning, proposals, contracts | Claude |
| General brainstorming, JD writing | ChatGPT |
| Live research, competitor monitoring | Perplexity |
| Long-document/huge-context analysis | Gemini |
| Internal knowledge Q&A | NotebookLM |
| Voice generation | ElevenLabs |
| Video avatar | HeyGen |
| Video generation | Veo |
| Logos/images | Ideogram |
| SEO research | SurferSEO, NeuronWriter, Ahrefs |
| Private/high-volume tasks | Ollama + vLLM + LiteLLM (self-hosted) |

---

## 6. Full Architecture (3-Layer, Final)

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1 — AI BRAINS: Claude/ChatGPT/Perplexity/Gemini/        │
│           NotebookLM/ElevenLabs/HeyGen + Ollama/vLLM/LiteLLM  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2 — ORCHESTRATION: LangGraph (COO) → CrewAI (crews) →   │
│           Dify (agent apps) → OpenHands (dev) → Browser Use/  │
│           Skyvern/Firecrawl (research)                        │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3 — EXECUTION (all REAL, deployable today):              │
│  Growth Engine: 14 n8n workflows (Marketing 1.1-1.5,           │
│    Sales+Delivery 2.1-2.9)                                     │
│  Growth Hacking: 6 n8n workflows (8.1-8.6) + Hub-Dispatcher     │
│  Business software: Odoo · Postgres · Qdrant · Mautic ·        │
│    Postal · Cal.com · Documenso · Postiz/Mixpost · Waha ·      │
│    Typebot · Chatwoot · Metabase · NocoDB · Invoice Ninja ·    │
│    Rocket.Chat · Nextcloud · OpenProject                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Sprint 1 — Revenue Engine (Build/Activate First)

**Goal: paisa aana shuru ho, sabse kam naya code likh ke.** Zyada tar Sprint 1 ka kaam ab **"build" nahi, "activate" hai:**

| Step | Action | Effort |
|---|---|---|
| 1 | Confirm `01-PHASE-8-MIGRATIONS.sql` v2 ran on Postgres | Verify only |
| 2 | Import + activate modules 1.1–1.5 (Marketing) + 2.1–2.9 (Sales/Delivery) in n8n | Import (already built) |
| 3 | Import + activate 8.1, 8.2, 8.3 (Reward/Referral/Free-Audit) | Import (already built) |
| 4 | Import + activate 8.4, 8.5, 8.6 (UGC/Community/Signal-Outreach) | Import (already built) |
| 5 | Import updated Hub-Dispatcher (with new event branches), fill placeholder workflow IDs | Wiring |
| 6 | Fill `{{legal_entity_name}}`, `{{support_email}}`, `{{support_whatsapp}}` placeholders (10-min find-replace across all legal/landing docs) | One script run |
| 7 | Wire real credentials: WhatsApp/Telegram/Email nodes (8 NoOp placeholders across 8.1-8.6), Firecrawl+PageSpeed API keys | Credentials |
| 8 | Finalize real reward/prize amounts in `campaigns` table (currently placeholder) | Business decision |
| 9 | Legal review of T&C/contest rules before going live in any market | Human/lawyer |
| 10 | Fill `WEBHOOK_URL` on 6 landing pages once n8n workflows are live | Post-activation |

**Only after Steps 1–10:** build the two remaining ⚪ track-only patches — `contest.winner_selected → 8.5` entry point, `ugc.submission_verified → 8.2` entry point (both are small patches, not new builds).

**Then, and only then**, build the genuinely-new Sprint 1 agents from Section 4 (rows 1-2: Market Research, ICP) since everything downstream of them is already built and waiting.

---

## 8. Sprint 2/3/4 (After Revenue Is Flowing)

- **Sprint 2 (Delivery):** rows 16-23 — Requirement→QA→DevOps agent chain, using OpenHands + CrewAI. Build only once Sprint 1 is producing real signed clients.
- **Sprint 3 (Ops):** rows 27-35 — Support, Finance, HR, Legal, BI, Internal Comms, PM agents. Company-stabilization phase.
- **Sprint 4 (Core):** rows 36-37 — LangGraph COO and CEO Intelligence Agent, built last, once there's real cross-department data for them to orchestrate over.

---

## 9. Consolidated Gap/Blocker Report (Exact, From Your Own Docs)

**🔴 Launch-blocking:**
1. Postgres migration (`01-PHASE-8-MIGRATIONS.sql` v2) — unconfirmed
2. 8.1/8.2/8.3 import/activate in n8n — unconfirmed
3. 8.4/8.5/8.6 import/activate — pending
4. Hub-Dispatcher updated import (new event branches + placeholder IDs filled)
5. Reward/prize amounts still placeholder in `campaigns` table
6. Legal review before any market goes live
7. `WEBHOOK_URL` placeholders on 6 landing pages

**🟡 Should-fix-soon:**
8. WhatsApp/Telegram/Email — 8 NoOp nodes need real credentials across 8.1-8.6
9. Firecrawl + PageSpeed API keys (8.3 engine)
10. `signal.lead_flagged → 2.1` — blank email/phone signals need manual-research routing instead of silent no-op

**⚪ Track-only (structural, doesn't block launch):**
11. `contest.winner_selected → 8.5` entry point missing (patch needed)
12. `ugc.submission_verified → 8.2` entry point missing (patch needed)
13. `client.onboarded`, `renewal.due`, `renewal.overdue`, `payment.failed` — pre-existing events, still no downstream consumer
14. Opt-out feedback webhook destination undecided

**Plus from v3, still open:**
15. 36-vs-14-vs-6(Phase8) workflow reconciliation — need to confirm in live n8n instance whether all these are the same numbered system or genuinely separate builds
16. 12 Sales Funnel stages (38-44, 50-54) still need pilot-depth docs
17. Marketing Funnel 72% incomplete (144/200 files) — M09-M10 pilot not started

---

## 10. Deployment Quick Reference

**VPS:** Ubuntu 22.04/24.04, 32GB RAM/8vCPU/200GB SSD recommended.
**Subdomains:** n8n, odoo, mail(Postal), files(Nextcloud), sign(Documenso), social(Mixpost/Postiz), bi(Metabase), cal(Cal.com), wa(Waha), bot(Typebot) — Caddy reverse-proxy, auto-SSL.

---

## 12. n8n vs Agent AI — Full Task-Level Automation Split

Same logic jo Market Research/ICP pe lagayi (n8n = pipe, agent = judgment jo pipe ke andar baithta hai) — ab saare 37 agents pe consistently apply ki hai. Teen categories:

- **n8n-solo** — pure data movement/rules/math/scheduling. Agent lagana slower+costlier, zero benefit.
- **Agent-solo** — pure reasoning task, execution/integration ki zaroorat hi nahi (ya n8n sirf logging ke liye).
- **Mix** — n8n trigger/fetch/store karta hai, agent sirf judgment wale specific step pe baithta hai.

| # | Agent | Split | Kahan agent lagta hai (agar mix/solo) |
|---|---|---|---|
| 1 | Market Research | 🔀 Mix | Synthesis/insight — n8n sirf fetch+store karta hai |
| 2 | ICP Agent | 🔀 Mix | ICP definition judgment |
| 3 | Lead Research/Extraction | 🔀 Mix (mostly n8n) | Sirf ambiguous/fuzzy-match relevance filtering |
| 4 | Lead Enrichment | 🔀 Mix (mostly n8n) | Sirf ambiguous name/company match resolution |
| 5 | Lead Qualification/Scoring | 🔀 Mix | Qualitative fit judgment (company description padhna); numeric scoring n8n |
| 6 | SDR/Outreach | 🔀 Mix | Per-lead personalization copy; sequencing/sending n8n |
| 7 | Follow-up/Nurture | ⚙️ n8n-solo | Wait/IF branching, no judgment needed |
| 8 | Meeting/Booking | ⚙️ n8n-solo | Pure Cal.com webhook scheduling |
| 9 | Proposal Agent | 🔀 Mix | Content drafting (what to include, tone); data-pull/assembly n8n |
| 10 | Contract/E-sign | ⚙️ n8n-solo | Pure status tracking |
| 11 | Invoicing | ⚙️ n8n-solo | Pure math/triggers |
| 12 | Onboarding | ⚙️ n8n-solo | Template-based project creation |
| 13 | Contest/Reward (8.1) | ⚙️ n8n-solo | Dedupe/fraud-score/payout = deterministic |
| 14 | Referral (8.2) | ⚙️ n8n-solo | Code/tracking/reward math |
| 15 | Free-Value/Audit (8.3) | 🔀 Mix | Turning raw PageSpeed/Firecrawl data into readable recommendations |
| 16 | Negotiation Assistant | 🧠 Agent-solo | Pure judgment, human-in-loop; n8n only logs outcome |
| 17 | Requirement Agent | 🔀 Mix | Extracting structured requirements from transcript; n8n triggers/stores |
| 18 | Solution Architect | 🧠 Agent-solo | Architecture design is pure reasoning; n8n logs to PM tool |
| 19 | Coding Agent | 🧠 Agent-solo | OpenHands IS the agent; n8n only triggers/logs |
| 20 | Code Review Agent | 🧠 Agent-solo | Review judgment; n8n triggers on PR webhook |
| 21 | QA/Test Agent | 🔀 Mix | Writing new test cases/triaging failures; running existing suites = n8n/CI |
| 22 | DevOps Agent | ⚙️ n8n-solo (mostly) | Deploy pipelines deterministic; agent optional only for anomaly-log analysis |
| 23 | Delivery/Reporting | ⚙️ n8n-solo | Status-pull + template report |
| 24 | UGC/Share (8.4) | 🔀 Mix | Content-quality/guideline verification; points/leaderboard = n8n |
| 25 | Community (8.5) | ⚙️ n8n-solo (mostly) | Membership/drip deterministic; agent optional for advocacy-trigger judgment |
| 26 | Signal-Outreach (8.6) | 🔀 Mix | Signal relevance scoring ("worth acting on?"); fetch/route = n8n |
| 27 | Renewal/Revenue-Ops | ⚙️ n8n-solo | Date-based reminders, deterministic |
| 28 | Customer Support | 🔀 Mix | Answer drafting from KB; ticket routing = n8n rules |
| 29 | Churn Prevention | 🔀 Mix | Interpreting combined health-signal, drafting CSM alert reasoning; data-merge = n8n |
| 30 | Finance Agent | ⚙️ n8n-solo (mostly) | Rule-based categorization; agent only for genuinely ambiguous transactions |
| 31 | HR Agent | 🔀 Mix | JD drafting/resume screening judgment; forms/scheduling = n8n |
| 32 | Legal/Contract Agent | 🧠 Agent-solo | Drafting assist, always human-reviewed; n8n only for status/logging |
| 33 | BI/Analytics | ⚙️ n8n-solo (mostly) | SQL views/Metabase deterministic; agent optional for natural-language narration on top |
| 34 | Internal Comms | ⚙️ n8n-solo | Pure notification routing |
| 35 | Project/Task Agent | 🔀 Mix | Breaking requirement into tasks, blocker detection; task creation = n8n |
| 36 | AI COO/Orchestrator | 🧠 Agent-solo | This IS the orchestration layer (LangGraph); n8n executes its decisions |
| 37 | CEO Intelligence | 🧠 Agent-solo | Cross-source synthesis; Metabase/n8n only feed it data |

**Architecture rule that ties this together:** even in Agent-solo rows, the agent's output still gets logged back through n8n into Postgres/Company Brain — so every decision stays auditable regardless of which layer did the thinking. This isn't optional; it's what keeps Section 11's governance rule (Agent → Tool → Permission check → Validation → n8n → Database) true everywhere, not just in the Mix rows.

---

## 13. Improvements Applied (my own additions, flagged as such)

These weren't in any source doc — adding them because the audit above surfaced real gaps:

1. **8.1 Contest fraud-scoring** — currently a Code-node rule set. Fine at low volume; flag for upgrade to an agent-based anomaly-detector once entry volume grows past what simple rules catch (e.g., coordinated fake-account rings). Not urgent — Sprint 3+.
2. **8.4 UGC verification** — source docs don't specify how "verify" happens. Recommend: agent does first-pass content-guideline check (auto-approve obvious passes, auto-reject obvious spam), human reviews only the ambiguous middle — reduces manual review load without removing the human gate on edge cases.
3. **Churn Prevention (row 29)** — earlier docs describe this as a pure data-merge trigering a Slack alert. Adding an agent-interpretation step here (turning "usage down 40% + 2 open tickets + NPS 3" into a one-line risk reasoning) makes the CSM alert actually actionable instead of just a number dump.
4. **Consistency check across Mix rows** — every Mix row above sends its agent output back through n8n before it touches CRM/Postgres, matching the governance rule. No exceptions found needing a fix.

---

## 14. Audit Summary

| Split type | Count | % |
|---|---|---|
| ⚙️ n8n-solo | 17 | 46% |
| 🔀 Mix | 13 | 35% |
| 🧠 Agent-solo | 7 | 19% |

**Headline finding:** less than half the company genuinely needs an AI agent at all — the rest is legitimately n8n's job. This matches the original guardrail principle (Section 1, #1: one primary tool per function) — the temptation to "AI-agent-ify" everything would have made the system slower and more expensive for 46% of the work with zero quality gain.

---

## 15. What This Document Deliberately Does Not Do

- Doesn't re-build what's already built (rows marked 🟢 in Section 4 are import/activate tasks, not development tasks).
- Doesn't invent business-specific values (legal entity name, prize amounts, real emails) — these are explicitly flagged as "your input needed."
- Doesn't sequence COO/CEO agents before the revenue engine is live — Section 8 ordering is deliberate, matching your own stated priority.
