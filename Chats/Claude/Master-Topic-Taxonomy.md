# Master Content Taxonomy — BDU Knowledge Base
**Rule: every file — including every ChatGPT chat and every future research drop — gets a real Brand/Topic/Subtopic home. Nothing sits loose, and nothing sits in a generic "misc" dump.**

---

## What changed in this version, and why

Buried inside `Notion - Nivy OS` there's already a well-designed system for exactly the problem you just asked about — *"where do I put newly researched data?"* It looks like a past session (Claude, per the page footers) built a **4-Zone Research Lab** with a real intake → review → publish pipeline, plus a Sandbox Archive rule of "never delete, always tag." It was even later simplified — one page notes Zones 1, 2, and 4 were unified so **Nivy HQ became the single front door** to everything.

That's a better pattern than what I gave you before, so I'm adopting it instead of inventing a parallel system. Two real upgrades this brings:

1. **A dedicated Research Lab / Inbox** — a defined landing spot for anything you research, with clear rules for what happens to it next, instead of you having to decide the "final" folder on day one.
2. **A Sandbox Archive** instead of a `_Needs-Review` afterthought — content that doesn't fit anywhere yet is tagged and kept, never deleted, and revisited on a schedule.

---

## How this answers your actual question

**Where do I put something I just researched?**
→ `ZONE-0-Research-Lab/01-Inbox/`. That's it. You don't classify it, you don't decide the brand, you don't pick a subtopic — you just drop it in with (ideally) a one-line note of what it is. Everything else below is what happens to it *after*, in batches, not something you have to figure out in the moment.

From there it moves through a short, repeatable pipeline:

```
01-Inbox                → raw, untagged, just landed
     ↓
02-Draft-Zone           → structured into a standard format (SOP / Knowledge / Strategy /
                           Framework / Market-Research — templates below), destination proposed
     ↓
03-Review-Queue         → you approve or reject
     ↓ (approved)                              ↓ (rejected)
04-Migration-Queue      →  moved to its         05-Sandbox-Archive → tagged, kept forever,
   permanent Zone 2/3      permanent home            revisited quarterly
   folder in batches
```

This means your "research → organize" workflow becomes: **research → drop in Inbox → forget about it until the next batch pass.** The batch pass is a small, repeatable task (matches the phase-tracker style from before), not a re-think of the whole structure each time.

---

## Full Structure

```
ZONE-0-Research-Lab/                       ← YOUR DAILY DROP-OFF POINT FOR NEW RESEARCH
├── 01-Inbox/                              (raw research, chat exports, notes — untagged, unfiltered)
├── 02-Draft-Zone/                         (Claude structures raw content into standard formats)
├── 03-Review-Queue/                       (Draft → Reviewing → Approved / Rejected)
├── 04-Migration-Queue/                    (Approved, batched, waiting to move to permanent home)
└── 05-Sandbox-Archive/                    (never deleted — tagged: Personal-Ideation, Old-Plan,
                                             Raw-Export, Not-Applicable, Backlog)

ZONE-1-Nivy-HQ/                            ← SINGLE FRONT DOOR / COMMAND CENTRE
├── Global-Dashboard.md                    (build status, links to every brand + database)
├── Master-Index.md                        (every SOP/doc: DeptCode-TopicCode, Type, Version,
                                             Tags, Status, Reference, Last Updated — see below)
└── Naming-Conventions.md

ZONE-2-Global-Systems/                     ← ANYTHING USED BY 2+ BRANDS LIVES HERE, NOWHERE ELSE
├── Departments/
│   ├── CEO-Executive-Office/
│   ├── CFO-Finance/
│   ├── CMO-Marketing/
│   ├── CTO-Technology/
│   ├── HR/
│   ├── Operations/
│   ├── Project-Management/
│   └── Sales/
├── Systems-and-Blueprints/
│   ├── Nivy-OS-Core/                      (Level 1-4 system docs, Authority System, Brand Identity)
│   ├── GAOS/
│   ├── Growth-Engine/                     (Marketing Funnel M01-M22, Sales Funnel stages)
│   └── Automation-and-Tools/              (n8n, CRM, scripts)
├── Training-and-People-Development/
│   ├── BDE-Launchpad-Program/
│   ├── BDE-90-Day-Program/
│   └── Onboarding-and-Orientation/
├── Legal-Compliance-and-Policy/
│   ├── NDAs-and-Agreements/
│   ├── Company-Policies/
│   ├── ISO-and-Global-Compliance/
│   └── Service-Guarantees-and-Disclaimers/
├── Templates-Library/                     (Global Templates — proposals, SOPs, outreach, delivery)
├── Universal-Research-Library/            (market research by geography — UK, UAE, USA, India, AUS, Canada)
├── Reports-and-Dashboards/
├── Weekly-and-Time-Trackers/
└── Assets/

ZONE-3-Brand-OS/                           ← ONE OS PER BRAND, BRAND-SPECIFIC CONTENT ONLY
├── Nivy-Advisory/
│   ├── Strategy-and-Planning/  Brand-and-Website/  Marketing-and-Content/
│   ├── Sales-and-Pricing/  SOPs-and-Processes/  Clients-and-Leads/
│   ├── Templates/  Reports-and-Trackers/  Assets/
├── Nivy-Academy/
│   ├── Strategy-and-Planning/  Curriculum-and-Courses/  Marketing-and-Content/
│   ├── Sales-and-Enrollment/  SOPs-and-Processes/  Benchmarking/
│   ├── Templates/  Reports-and-Trackers/  Assets/
├── Nivy-Next/
│   ├── Strategy-and-Planning/  Brand-Bible/  Website-and-SEO/  Marketing-and-Content/
│   ├── Sales-and-Pricing/  SOPs-and-Processes/  Templates/  Reports-and-Trackers/  Assets/
├── Nivy-Nexus/
│   ├── Strategy-and-Business-Ideas/  Community-and-Members/  Marketing-and-Content/
│   ├── Sales-and-Deal-Management/  Lead-and-KPI-Trackers/  SOPs-and-Processes/
│   ├── Templates/  Assets/
├── Nivy-Jobs/
│   ├── Strategy-and-Planning/  Freelancer-and-Partner-Programs/  Sales-Process/
│   ├── SOPs-and-Processes/  Templates/  Reports-and-Trackers/  Assets/
├── Nivy-Alliance/
│   ├── Partner-Program-Structure/  Onboarding-and-Welcome/  Agreements-and-Templates/
│   ├── Reports-and-Trackers/  Assets/
├── Nivy-Care-Foundation/
│   ├── Strategy-and-Programs/  Community-and-Outreach/  Templates/  Assets/
├── Nivy-Artisan/
│   ├── Strategy-and-Planning/  Marketing-and-Content/  SOPs-and-Processes/  Assets/
├── Urban-Vibes/
│   ├── Strategy-and-Planning/  Marketing-and-Content/  SOPs-and-Processes/  Templates/  Assets/
└── All-Communities/
    ├── Community-Structure-and-Guidelines/  Member-and-Engagement-Tracking/
    ├── Content-and-Templates/  Assets/

_System/
├── INDEX.md                     (master map — every folder, one-line description, file count)
├── Naming-Conventions.md
├── Duplicate-and-Merge-Log.md
└── Classification-Log.md
```

**Note on "Urban Vibes":** the original Sandbox Archive doc actually tags Urban Vibes and a "Matrimonial Research" thread as `[PERSONAL IDEATION] — not a Nivy brand`. If that's still accurate, Urban Vibes content should route to `ZONE-0-Research-Lab/05-Sandbox-Archive/Personal-Ideation/` instead of getting a full Brand OS folder — flag this for a decision before Phase 2.7 runs (see tracker).

---

## The Master Index metadata pattern (optional, but worth adopting going forward)

A different doc in the same export (`Brand Systems/Structure of Workspace`) proposes tagging every page with a small metadata block. Retrofitting this onto 7,700+ existing files isn't worth the effort, but it's cheap to apply to **everything new** going through the Research Lab pipeline from now on:

```
Title:     [Emoji] DeptCode-TopicCode-ShortTopicName | Brand | Type | vX
Metadata:  Brand | Department | Topic | Subtopic | Type (SOP/Playbook/Strategy/Knowledge) |
           Version | Tags | Status (Draft/Approved/Deprecated) | Source | Last Updated
```

This is what makes `ZONE-1-Nivy-HQ/Master-Index.md` searchable later without opening every file.

---

## Where the messiest raw sources land (updated paths)

| Raw source | Destination |
|---|---|
| `Notion - Nivy OS` (3,237 flat files) | Split across `ZONE-2-Global-Systems/` and every `ZONE-3-Brand-OS/<brand>/` by subject |
| `chat gpt data export` | Read, matched by subject, filed inline into the same Zone 2/3 topic folders — treated as **Migration Queue material**, not a separate archive |
| Anything genuinely unclear even after reading | `ZONE-0-Research-Lab/05-Sandbox-Archive/`, tagged `[NOT APPLICABLE]`, `[BACKLOG]`, `[OLD PLAN]`, `[RAW EXPORT]`, or `[PERSONAL IDEATION]` — never silently dropped |
| `Nivy Research Data/Nivy Company Hub` | `ZONE-2-Global-Systems/Departments/` (near 1:1 mapping already) |
| `Nivy Research Data/BDE Complete Training` + GAOS launchpad | `ZONE-2-Global-Systems/Training-and-People-Development/` |
| `Brand Systems`, `Notion - Global Systems Workpace` | `ZONE-2-Global-Systems/Systems-and-Blueprints/` + `Legal-Compliance-and-Policy/` |
| Duplicate export pairs (Nexus, All Communities, Jobs) | Merged into one canonical copy before classification starts |
| Weekly logs (`W1 Jun 21-27`, etc.) | `ZONE-2-Global-Systems/Weekly-and-Time-Trackers/` unless clearly brand-specific |
| Loose images/fonts | `Assets/` inside whichever Zone 2/3 topic they belong to |

---

## How to use this tracker with Claude Free

Each phase is scoped small on purpose — one phase = one fresh Claude Free conversation = one sitting. To resume work:

1. Start a new chat.
2. Upload `Raw-Repository.zip` (or the in-progress working copy) **and** this file.
3. Say: *"Read the progress tracker in this file, find the first phase marked `Not Started`, and execute only that phase."*
4. When done, ask Claude to **update this file's tracker table** and give you the resulting file(s).
5. Save the updated tracker over this file, repeat for the next phase.

**Legend:** ⬜ Not Started · 🟨 In Progress · ✅ Done

---

## Progress Tracker

### Stage 0 — Setup

| # | Phase | Scope | Status | Depends On | Output / Notes |
|---|---|---|---|---|---|
| 0.1 | Extract raw zip + build full empty skeleton (Zone 0, 1, 2, 3 + `_System`) | Folder structure only | ⬜ Not Started | — | Working copy created |
| 0.2 | Decide: is Urban Vibes a real brand or Sandbox `[PERSONAL IDEATION]`? Confirm before 2.7 runs | 1 decision | ⬜ Not Started | — | Affects whether Urban Vibes gets a Brand OS folder |

### Stage 1 — Deduplication

| # | Phase | Scope | Status | Depends On | Output / Notes |
|---|---|---|---|---|---|
| 1.1 | Merge `Nivy Nexus` ↔ `Notion - Nivy Nexus` | 566 files | ⬜ Not Started | 0.1 | Log in Duplicate-and-Merge-Log.md |
| 1.2 | Merge `All Communities` ↔ `Notion - All Communities` | 61+31 | ⬜ Not Started | 0.1 | Log in Duplicate-and-Merge-Log.md |
| 1.3 | Merge `Nivy Jobs` ↔ `Notion - Nivy Jobs`; delete 18 leftover raw `Export-*.zip`; remove stray root export folder | 48+45+18+1 | ⬜ Not Started | 0.1 | Log in Duplicate-and-Merge-Log.md |

### Stage 2 — Brand-by-brand clean + classify → `ZONE-3-Brand-OS/`

| # | Phase | Source Folder | Est. Files | Status | Depends On | Output |
|---|---|---|---|---|---|---|
| 2.1 | Clean + classify | `Nivy Advisory` | 198 | ⬜ Not Started | 0.1 | → `ZONE-3-Brand-OS/Nivy-Advisory/` |
| 2.2 | Clean + classify | `Nivy Academy` | 374 | ⬜ Not Started | 0.1 | → `ZONE-3-Brand-OS/Nivy-Academy/` |
| 2.3 | Clean + classify | `Nivy Next` | 854 | ⬜ Not Started | 0.1 | → `ZONE-3-Brand-OS/Nivy-Next/` (large — split into 2 sub-batches if needed) |
| 2.4 | Clean + classify | `Nivy Nexus` (merged) | 566 | ⬜ Not Started | 1.1 | → `ZONE-3-Brand-OS/Nivy-Nexus/` |
| 2.5 | Clean + classify | `Nivy Jobs` (merged) | 51 | ⬜ Not Started | 1.3 | → `ZONE-3-Brand-OS/Nivy-Jobs/` |
| 2.6 | Clean + classify | `Nivy Artisan` | 23 | ⬜ Not Started | 0.1 | → `ZONE-3-Brand-OS/Nivy-Artisan/` |
| 2.7 | Clean + classify | `Urban Vibes` | 45 | ⬜ Not Started | 0.2 | → Brand OS **or** Sandbox Archive, per 0.2 decision |
| 2.8 | Clean + classify | `Nivy Global` | 77 | ⬜ Not Started | 0.1 | Route by actual subject — Zone 2 or a brand |
| 2.9 | Clean + classify | `GAOS` (real content only; log & exclude onboarding boilerplate) | ~15/63 | ⬜ Not Started | 0.1 | → `ZONE-2-Global-Systems/Systems-and-Blueprints/GAOS/` |
| 2.10 | Clean + classify | `All Communities` (merged) | 61 | ⬜ Not Started | 1.2 | → `ZONE-3-Brand-OS/All-Communities/` |
| 2.11 | Clean + classify | `Brand Systems` + `Notion - Global Systems Workpace` | 83+190 | ⬜ Not Started | 0.1 | → `ZONE-2-Global-Systems/Systems-and-Blueprints/` + `Legal-Compliance-and-Policy/` |

### Stage 3 — Company Hub & Training migration → `ZONE-2-Global-Systems/`

| # | Phase | Scope | Est. Files | Status | Depends On | Output |
|---|---|---|---|---|---|---|
| 3.1 | Migrate `Nivy Company Hub (Workspace)` departments | ~120 | ⬜ Not Started | 0.1 | → `Departments/` |
| 3.2 | Migrate `BDE Complete Training` (launchpad + 90-day program) | ~250 | ⬜ Not Started | 0.1 | → `Training-and-People-Development/` |

### Stage 4 — Classify `Notion - Nivy OS` (3,237 files, 11 batches of ~300)

| # | Phase | Scope | Status | Depends On | Output |
|---|---|---|---|---|---|
| 4.1–4.11 | Batches 1–11 | ~300 files each | ⬜ Not Started (×11) | 0.1 | Route into Zone 2 or the matching Brand OS folder; log every file in Classification-Log.md |

### Stage 5 — ChatGPT export → Migration Queue (11 batches, matches existing `conversations-0XX.json` split)

| # | Phase | Scope | Status | Depends On | Output |
|---|---|---|---|---|---|
| 5.1–5.11 | `conversations-000.json` … `conversations-010.json` | one file each | ⬜ Not Started (×11) | 0.1 | Match `.dat` attachments; file each convo into matching Zone 2/3 topic |

### Stage 6 — Cleanup & finishing

| # | Phase | Scope | Status | Depends On | Output |
|---|---|---|---|---|---|
| 6.1 | Normalize assets — loose images/fonts into the right `Assets/` folders | ⬜ Not Started | Stages 2–5 | |
| 6.2 | File the orphans — root stray `.md` + `New Research` (2 files) | ⬜ Not Started | 0.1 | |
| 6.3 | Reconcile file counts vs. the original 7,732-file baseline | ⬜ Not Started | Stages 1–6.2 | |
| 6.4 | Build `ZONE-1-Nivy-HQ/Global-Dashboard.md` + `Master-Index.md` + one `README.md` per Zone/brand | ⬜ Not Started | 6.3 | |
| 6.5 | Final zip for delivery / GitHub push | ⬜ Not Started | 6.4 | |

**Total phases: 47.** Progress so far: **0 / 47 complete.**

---

## Next step

Confirm the Zone-based structure and the Urban Vibes call (0.2), then start with **Phase 0.1**. Everything you research from today onward has one instruction: **drop it in `ZONE-0-Research-Lab/01-Inbox/`** — the batch phases handle the rest.
