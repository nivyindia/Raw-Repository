# BILLION DREAMS UNITED OS
# MASTER IMPLEMENTATION PLAN — v2 (GRANULAR STEP BREAKDOWN)
## Har Stage ko chhote, single-deliverable steps mein split kiya gaya hai

**Base document:** Billion-Dreams-United-Improvement_Implementation-Plan-v1.md
**Date:** 2026-09-01
**Rule carried forward:** Ek step tabhi "done" mana jayega jab uska **actual file/artifact** exist kare. Sirf discussion/decision = done nahi.

Har Stage (A–K) ab chhote **numbered steps** mein tod diya gaya hai — har step:
- ek hi clear deliverable produce karta hai
- ek din (ya usse kam) mein complete ho sakta hai
- next step is par depend karta hai (sequence fixed hai, skip mat karo)

---

# STAGE A — GOVERNANCE FOUNDATION (5 files → ab 11 steps)

| Step | Action | Deliverable | Depends on |
|---|---|---|---|
| A.1 | Repo skeleton banao (`00-governance/` se `21-incidents/` tak sab empty folders + `.gitkeep`) | Folder structure committed | — |
| A.2 | Har existing ID (87 agents + 48 WF + 26 MW + 15 XW = 176 items) ko ek CSV/YAML list mein nikaalo, sirf ID+name | `id-master-list.yaml` | A.1 |
| A.3 | `COMPLETION_MATRIX.md` banao — har ID ko status=0 assign karo | `COMPLETION_MATRIX.md` (176 rows) | A.2 |
| A.4 | `SYSTEM_MASTER_INDEX.md` banao — har existing MD file (v6, directory, funnel list) ka one-line summary + link | `SYSTEM_MASTER_INDEX.md` | A.1 |
| A.5 | `ARCHITECTURE_DECISIONS.md` shuru karo — sirf 5 already-decided ADRs likho (Odoo not OpenProject, Odoo not 2nd CRM, one vector DB, one workflow engine, revenue-first order) | `ARCHITECTURE_DECISIONS.md` (5 ADRs) | A.1 |
| A.6 | `BUILD_RULES.md` banao — locked build order (A→K) ko literally copy-paste karke rule-doc banao | `BUILD_RULES.md` | — |
| A.7 | `CHANGE_MANAGEMENT.md` banao — sirf 1 rule likho: "koi bhi registry entry change → PR + owner sign-off + version bump" | `CHANGE_MANAGEMENT.md` | A.1 |
| A.8 | COMPLETION_MATRIX mein un items ko status=100 mark karo jo sach mein locked hain (company structure, tech stack, funnel, dept template — ~10 items) | Updated matrix | A.3 |
| A.9 | Ek `OWNER` column add karo matrix mein — abhi sab "unassigned" | Updated matrix | A.3 |
| A.10 | Weekly review cadence decide karo (kab/kaun matrix update karega) — 3 lines in BUILD_RULES.md | Updated BUILD_RULES.md | A.6 |
| A.11 | Stage A completion check: matrix se `SUM(status)/176` compute karke ek number nikaalo — ye tumhara "real %" hai | Computed number saved in COMPLETION_MATRIX.md header | A.3–A.10 |

**Stage A output:** 5 governance files → ab 11 discrete, checkable actions. Ek din mein A.1–A.7 ho sakte hain agar focused ho.

---

# STAGE B — DATA + EVENT CONTRACTS (→ ab 14 steps)

## B.1–B.6: Canonical Data Model
| Step | Action | Deliverable |
|---|---|---|
| B.1 | 30 entities ki list finalize karo (already listed in v1 plan) | `06-data/entity-list.yaml` |
| B.2 | Sabse critical 6 entities (Lead, Account, Opportunity, Contact, Project, Invoice) ka field-level schema likho | `06-data/data-model.yaml` (v0.1 — 6 entities) |
| B.3 | Agle 10 entities (Company, Brand, Client, Campaign, Meeting, Proposal, Contract, Payment, Task, Ticket) add karo | `data-model.yaml` (v0.2 — 16 entities) |
| B.4 | Baaki 14 AI/ops entities (Agent, AgentRun, Skill, Tool, Workflow, WorkflowRun, Event, Evaluation, Approval, Incident, Department, User, Employee, Partner) add karo | `data-model.yaml` (v1.0 — 30 entities) |
| B.5 | Har entity mein 5 common fields standardize karo (id, company_id, brand_id, created_at, updated_at) | Updated data-model.yaml |
| B.6 | Data model ko ek diagram (ER-style, text-based) mein visualize karo — sirf relationships | `06-data/data-model-diagram.md` |

## B.7–B.10: State Machines
| Step | Action | Deliverable |
|---|---|---|
| B.7 | Lead state machine likho (states + transitions + trigger + workflow + agent per transition) | `06-data/state-machines/lead.yaml` |
| B.8 | Opportunity state machine likho | `06-data/state-machines/opportunity.yaml` |
| B.9 | Project state machine likho | `06-data/state-machines/project.yaml` |
| B.10 | Ticket state machine likho | `06-data/state-machines/ticket.yaml` |

## B.11–B.14: Event Schema
| Step | Action | Deliverable |
|---|---|---|
| B.11 | Base event envelope schema lock karo | `06-data/event-schemas/base_event.yaml` |
| B.12 | Top 10 highest-priority events (lead.created, lead.enriched, lead.qualified, outreach.sent, reply.received, meeting.booked, proposal.sent, contract.signed, payment.received, client.onboarded) ka payload schema likho | 10 files in `06-data/event-schemas/` |
| B.13 | Baaki ~15 events (project/ticket/renewal related) add karo | 15 more files |
| B.14 | Event → Workflow → Agent mapping table banao (kaun sa event kaunsa WF trigger karta hai) | `06-data/event-workflow-map.md` |

---

# STAGE C — REGISTRIES (→ ab 16 steps)

## C.1–C.4: Registry Skeletons
| Step | Action | Deliverable |
|---|---|---|
| C.1 | `02-agents/registry.yaml` skeleton — 87 rows, sirf id+name+status | File created |
| C.2 | `03-skills/registry.yaml` skeleton — jitni skills v1 plan mein identified hain (~50) | File created |
| C.3 | `04-tools/registry.yaml` skeleton — 15 priority tools ki list | File created |
| C.4 | `05-workflows/registry.yaml` skeleton — 48+26+15 = 89 rows | File created |

## C.5–C.9: Tool Registry (build FIRST — everything else depends on it)
| Step | Action | Deliverable |
|---|---|---|
| C.5 | `odoo.search_lead`, `odoo.create_lead`, `odoo.update_lead` — input/output schema likho | 3 tool entries filled |
| C.6 | `odoo.create_opportunity`, `postgres.query_readonly`, `postgres.write_event` — schema likho | 3 more entries |
| C.7 | `firecrawl.extract`, `browser_use.research` — schema likho | 2 more entries |
| C.8 | `mautic.send_email`, `postal.send_transactional`, `cal.create_booking` — schema likho | 3 more entries |
| C.9 | `qdrant.search`, `qdrant.upsert` — schema likho, tool registry ko v1.0 mark karo (15/15 done) | Tool registry 100% for Tier-1 |

## C.10–C.16: Agent Contract Standard (apply to first 5 agents only, as pilot)
| Step | Action | Deliverable |
|---|---|---|
| C.10 | `agents/lead-intelligence/lead-discovery/agent.yaml` (A034) likho | 1 agent.yaml |
| C.11 | A034 ka `prompt.md` draft likho | 1 prompt.md |
| C.12 | A036 (Enrichment) ka agent.yaml + prompt.md | 2 files |
| C.13 | A038 (Verification) ka agent.yaml + prompt.md | 2 files |
| C.14 | A039 (Lead Scoring) ka agent.yaml + prompt.md | 2 files |
| C.15 | A044 (Email Outreach) ka agent.yaml + prompt.md | 2 files |
| C.16 | Pilot 5 agents ka `tools.yaml` + `input.schema.json` + `output.schema.json` fill karo — ab COMPLETION_MATRIX mein inko status=25 mark karo | 5 agents × 3 files = 15 files |

---

# STAGE D — POLICY + APPROVAL ENGINE (→ ab 9 steps)

| Step | Action | Deliverable |
|---|---|---|
| D.1 | Risk matrix table (L0–L4) ko `07-policies/permission-matrix.yaml` mein YAML format mein convert karo | 1 file |
| D.2 | `07-policies/ai-risk-policy.yaml` — har risk level ke liye "AI allowed / approval required" rule likho | 1 file |
| D.3 | `07-policies/communication-policy.yaml` — sirf consent_status → channel_permission chain likho (abhi logic, code nahi) | 1 file |
| D.4 | Suppression list ka data model define karo (already B.2–B.4 mein cover ho sakta hai — cross-link karo) | Cross-reference note |
| D.5 | Odoo mein `approval.request` custom model design karo (fields: action_type, requested_by, risk_level, status, approved_by) — sirf spec, build nahi | `07-policies/approval-request-model-spec.md` |
| D.6 | Approval flow ka n8n workflow diagram banao (event → task create → wait → approve/reject → emit event) — text-based flowchart | `07-policies/approval-workflow-spec.md` |
| D.7 | Vaultwarden environments plan karo (dev/staging/prod vaults) — sirf naming convention decide karo | `07-policies/iam-baseline.md` |
| D.8 | Service accounts ki list banao (n8n, Dify, Odoo-API, LangGraph) — har ek ke scope note karo | Same file update |
| D.9 | Founder + backup admin 2FA/SSO checklist banao | Checklist added |

---

# STAGE E — INFRASTRUCTURE (→ ab 10 steps)

| Step | Action | Deliverable |
|---|---|---|
| E.1 | Ek VPS/laptop pe Docker install + verify | Working Docker |
| E.2 | `docker-compose.yml` (dev) mein Odoo + PostgreSQL likho, `up` karke test karo | Working Odoo+PG |
| E.3 | Same compose mein n8n add karo, health check | Working n8n |
| E.4 | Dify add karo (docker-compose separate repo se) | Working Dify |
| E.5 | Ollama + LiteLLM add karo, ek chhota local model pull + test | Working local inference |
| E.6 | Qdrant + MinIO add karo | Working vector DB + storage |
| E.7 | Mautic + Postal add karo (email infra) | Working email stack |
| E.8 | Cal.com/Cal.diy add karo | Working booking |
| E.9 | GitHub repo connect karo (Actions ke liye) — basic `lint+test` workflow file likho | `.github/workflows/ci.yml` |
| E.10 | PostgreSQL + Odoo ka daily automated backup script likho AUR **ek baar actually restore karke test karo** scratch env mein | Backup script + restore-test log |

*(Staging/Production environments Stage E ke baad, jab Tier-1 agents 60%+ pahunch jayein, tab clone karna — abhi dev sufficient hai)*

---

# STAGE F — TIER-1 REVENUE AGENTS (19 agents) (→ per-agent 7-step micro-cycle)

Har agent ke liye same 7-step cycle chalega (isse "60% complete" ka matlab exact pata chalega):

| Micro-step | Action |
|---|---|
| F.x.1 | `agent.yaml` + `prompt.md` finalize (status → 25) |
| F.x.2 | Tools wire karo, ek test input se manually run karo (status → 40) |
| F.x.3 | n8n/LangGraph trigger se connect karo, ek real event pe chalao (status → 60) |
| F.x.4 | 10 golden test cases banao aur pass karwao (status → 75) |
| F.x.5 | Staging mein 1 week chalao, errors log karo (status → 85) |
| F.x.6 | Production mein daalo, human review har output pe (status → 95) |
| F.x.7 | Policy ke andar autonomous karo, monitoring live (status → 100) |

**Build order (per v1 plan, ab explicit sequence):**
1. F.1 = A001 (Market Research) — F.1.1 → F.1.7
2. F.2 = A002 (ICP)
3. F.3 = A034 (Lead Discovery)
4. F.4 = A035 (Contact Discovery)
5. F.5 = A036 (Enrichment)
6. F.6 = A037 (Data Quality)
7. F.7 = A038 (Verification)
8. F.8 = A039 (Lead Scoring)
9. F.9 = A041 (Account Research)
10. F.10 = A042 (Signal Detection)
11. F.11 = A043 (Outreach Strategy)
12. F.12 = A044 (Email Outreach)
13. F.13 = A049 (Personalization)
14. F.14 = A050 (Follow-Up)
15. F.15 = A052 (Reply Triage)
16. F.16 = A054 (Qualification)
17. F.17 = A055 (Meeting Prep)
18. F.18 = A060 (Proposal)
19. F.19 = A065 (Onboarding)

**Phase target:** F.1–F.19 sab ko step 4 (75%) tak le jao. Top 5 (F.3, F.5, F.8, F.12, F.14) ko step 7 (100%) tak push karo — ye core loop hai.

---

# STAGE G — TIER-1 WORKFLOWS (→ per-workflow 6-step micro-cycle)

| Micro-step | Action |
|---|---|
| G.x.1 | Reuse-source decide karo (RW-S03 / RW-S04 / RW-S08 / build fresh) |
| G.x.2 | n8n canvas mein skeleton banao (trigger + nodes, no logic) |
| G.x.3 | Odoo/Postgres/Qdrant connections wire karo (paid API nodes hatao) |
| G.x.4 | Error handling + retry + dead-letter add karo |
| G.x.5 | Test event se end-to-end run karo, output verify karo |
| G.x.6 | `workflow.yaml` spec file likho (trigger/inputs/outputs/events_emitted) — registry mein status=100 mark karo |

**Build order (24 core + 5 cross-functional):**
WF001 → WF002 → WF003 → WF004 → WF005 → WF006 → WF007 → WF008 → WF009 → WF010 → WF011 → WF017 → WF018 → WF019 → WF020 → WF022 → WF023 → WF024 → WF025 → WF029 → WF030 → WF033 → WF034 → WF035 → WF036
then: XW001, XW002, XW010, XW014, XW015

---

# STAGE H — EVALUATION + TESTING (→ ab 8 steps, parallel se Stage F ke saath)

| Step | Action | Deliverable |
|---|---|---|
| H.1 | Golden dataset template banao (input/expected-output JSON format) | `08-evaluation/template.jsonl` |
| H.2 | Top 5 core agents (F.3, F.5, F.8, F.12, F.14) ke liye 20-20 real/realistic cases likho | 5 datasets |
| H.3 | Baaki 14 Tier-1 agents ke liye 10-10 cases likho (lighter, since not core loop) | 14 datasets |
| H.4 | Rule-based checker likho (schema validity, required fields) — chhota script | `08-evaluation/rule-check.py` |
| H.5 | Promptfoo setup karo, LiteLLM se connect karo | Working promptfoo config |
| H.6 | Release-gate script/checklist likho (score >= threshold → staging) | `08-evaluation/release-gate.md` |
| H.7 | Weekly 10% human-spot-check process document karo | `08-evaluation/human-review-process.md` |
| H.8 | Har Tier-1 agent ka pehla evaluation run karke score record karo | `08-evaluation/results/<agent_id>.json` |

---

# STAGE I — OBSERVABILITY + INCIDENT MANAGEMENT (→ ab 7 steps)

| Step | Action | Deliverable |
|---|---|---|
| I.1 | PostgreSQL mein `agent_runs` table banao (run_id, agent_id, cost, duration, status etc.) | Table created |
| I.2 | Har Tier-1 agent ko is table mein log karne wala wrapper likho (n8n node ya function) | Logging wrapper |
| I.3 | Metabase dashboard #1 — AI Ops (success rate, cost, latency) banao | Dashboard 1 |
| I.4 | Metabase dashboard #2 — Sales funnel (leads→meetings→proposals→closed) banao | Dashboard 2 |
| I.5 | Metabase dashboard #3 — Incident dashboard (failed runs, escalations) banao | Dashboard 3 |
| I.6 | Kill-switch n8n workflow banao (ek flag toggle → sab outbound agents disable) | 1 n8n workflow |
| I.7 | Kill-switch ko ek baar actually test karo (trigger karke confirm karo sab ruk gaya) | Test log |

---

# STAGE J — FIRST LIVE REVENUE LOOP (→ ab 5 steps, sequential)

| Step | Action |
|---|---|
| J.1 | End-to-end connect karo: Market Research → Lead Discovery → Enrichment → Verification → Scoring → Account Research → Personalization → Outreach (chain test, human-approved sends) |
| J.2 | Outreach → Reply Triage → Qualification → Meeting Booking → Meeting Prep tak chain add karo |
| J.3 | 10-15 real leads daalo, poore funnel se run karo, har step pe manually verify karo |
| J.4 | 2 weeks real operation chalao — L2 policy (human-approved) ke saath — daily errors/breaks fix karo |
| J.5 | Results ke basis pe agents ko 75%→95% push karo (jo prove ho chuke), L2 approval relax karo un par |

---

# STAGE K — SCALE (→ ab 4 major sub-tracks)

| Track | Action |
|---|---|
| K.1 | A007–A020 batch (content/SEO/social) — Stage F ka wahi 7-step micro-cycle repeat karo har agent ke liye |
| K.2 | A067–A079 batch (retention agents) — same cycle |
| K.3 | Hermes interface build karo — daily brief template pehle likho (`65. CEO Daily Command Center` format se), phir Odoo/Postgres se actual data pull karke populate karo |
| K.4 | 2+ months stable Tier-1 operation ke baad hi AI COO layer shuru karo (Level 4→5 autonomy — v6 blueprint Section 46) |

---

# SUMMARY — TOTAL GRANULAR STEP COUNT

| Stage | Original items | Granular steps |
|---|---:|---:|
| A — Governance | 5 files | **11 steps** |
| B — Data/Event | 3 files | **14 steps** |
| C — Registries | 4 files | **16 steps** |
| D — Policy | 3 items | **9 steps** |
| E — Infrastructure | 1 bundle | **10 steps** |
| F — Tier-1 Agents | 19 agents | **19 × 7 = 133 micro-steps** |
| G — Tier-1 Workflows | 29 workflows | **29 × 6 = 174 micro-steps** |
| H — Evaluation | ongoing | **8 steps** |
| I — Observability | ongoing | **7 steps** |
| J — Revenue Loop | 1 milestone | **5 steps** |
| K — Scale | ongoing | **4 tracks** |

**Total explicit, checkable action items: ~390** (vs. the ~14 stage-level bullets in v1).

---

# HOW TO USE THIS FILE

1. Har step ko COMPLETION_MATRIX.md mein ek row ke against tick karo jab complete ho.
2. Kabhi bhi ek step skip mat karo — dependency chain fixed hai (A se pehle B nahi, C se pehle A ka tool registry nahi).
3. Roz/haftey ek target set karo: e.g. "is week A.1–A.11 + B.1–B.6 complete karna hai."
4. Jab kisi bhi Stage ke saare steps 100% ho jayein, tab hi agla Stage full-speed shuru karo (parallel thoda chal sakta hai — jaise H aur I, F ke saath parallel).

Agla practical step: is file ko `00-governance/` folder mein daal do aur A.1 se shuru karo — pehla actual deliverable sirf folder structure banana hai, jo 10 minute ka kaam hai.
