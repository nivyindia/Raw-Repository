# 06 — Navigation & Employee Experience Standard (FINAL)

> **Status: FINAL.** This is the decided navigation architecture — built entirely on top of Doc 03's existing folder structure. Nothing in Doc 03 is renamed; this document only adds navigation files/pages pointing into what Doc 03 already defines.
> **Owner:** Workspace Admin

---

## 1. The Full Navigation Formula — One Diagram

```
                            COMPANY OS
                                │
                          START-HERE.md
                                │
                ┌───────────────┼───────────────┐
                ↓               ↓               ↓
            Browse            Role Path        Search
                │               │
                ↓               ↓
             Company         My Role
                ↓               ↓
           Department      Learning Path
                ↓
              Team
                ↓
             Topic
                ↓
            Document
                │
        ┌───────┼──────────────┐
        ↓       ↓               ↓
   Breadcrumb  Table of      Related Docs
              Contents            │
                              See Also
```

**Every major document's navigation contract:**
```
[ Breadcrumb ]

Title
Purpose
Audience

[ Table of Contents ]

Content

[ Next Step / Action ]

[ Related Documents ]

[ See Also ]
```

**Most important final principle:** navigation is never dependent on the raw GitHub folder tree alone. Four layers work together at all times:
```
Browse  +  Role Path  +  Search  +  Contextual Links
```
And sitting above all four:
```
START HERE  +  Index/README  +  Breadcrumb  +  Related Documents
```

---

## 2. Where Navigation Lives Inside Doc 03's Existing Structure

Doc 03 already defines the folder tree. Navigation adds exactly 3 kinds of new file on top of it — nothing in Doc 03 is renamed or moved:

```
🏢 Company HQ
 │
 ├── README.md                          ← NEW — Home / Dashboard / Navigator (Section 5)
 ├── START-HERE.md                       ← NEW — new-employee entry point (Section 9)
 │
 ├── 📁 01_AREAS                          (already in Doc 03 — Departments)
 │    └── [Dept]/
 │         ├── README.md                 ← NEW — Department home (Section 5)
 │         ├── Policies/                  (already in Doc 03)
 │         ├── SOPs/                       (already in Doc 03)
 │         ├── Work_Instructions/           (already in Doc 03)
 │         ├── Templates/                    (already in Doc 03)
 │         ├── Reports/                       (already in Doc 03)
 │         ├── Records/                        (already in Doc 03)
 │         ├── Knowledge_Reference/              (already in Doc 03)
 │         │    └── Glossary.md                ← NEW (Section 10)
 │         │    └── FAQ.md                       ← NEW (Doc 07 §7)
 │         └── Meeting_Notes/                     (already in Doc 03)
 │
 ├── 📁 02_PROJECTS                        (unchanged from Doc 03)
 ├── 📁 03_RESOURCES
 │    └── Company_Master_Standards/          (already in Doc 03 — Docs 01–09 live here)
 │         └── Glossary.md                    ← NEW — company-wide terms (Section 10)
 └── 📁 04_ARCHIVE                            (unchanged from Doc 03)
```

---

## 3. Five Navigation Layers

```
┌──────────────────────────────────────────────────┐
│ Layer 1 — Organization Home                          │
│   START-HERE.md — global entry point                  │
│   (only needed once multiple companies/brands exist)   │
├──────────────────────────────────────────────────┤
│ Layer 2 — Company Home                                │
│   README.md at repo root                               │
├──────────────────────────────────────────────────┤
│ Layer 3 — Department Home                             │
│   01_AREAS/[Dept]/README.md                             │
├──────────────────────────────────────────────────┤
│ Layer 4 — Team Home                                    │
│   01_AREAS/[Dept]/[Team]/README.md                       │
│   (create ONLY if the team has enough independent        │
│    content to justify its own page — don't force it)      │
├──────────────────────────────────────────────────┤
│ Layer 5 — Topic Page                                     │
│   The actual guided document sequence (Section 8)          │
└──────────────────────────────────────────────────┘
```
No employee should ever have to guess "where does the next page live?" — every level has exactly one of these five layers as its home.

---

## 4. Two-Way Navigation Architecture

```
┌─────────────────────────────┐   ┌─────────────────────────────┐
│      Browse by Structure         │   │       Browse by Role             │
│                                     │   │                                     │
│   Company                            │   │   New Employee                       │
│      ↓                                │   │      ↓                                │
│   Department                           │   │   Sales Executive / HR Manager /       │
│      ↓                                  │   │   Marketing Lead / etc.                 │
│   Team                                    │   │      ↓                                   │
│      ↓                                     │   │   My Learning Path                        │
│   Topic (SOP / Policy / Workflow)            │   │                                             │
│                                                │   │                                             │
│   Best for: exploring the org                  │   │   Best for: learning your own job            │
└─────────────────────────────┘   └─────────────────────────────┘
                    │                                      │
                    └──────────── Search connects both paths ────────────┘
```
An employee reaches any piece of knowledge in one of two ways — by exploring the org chart downward, or by following their own role's path — and Search sits underneath both as a third, independent way in.

---

## 5. README Standard — Exact Content Per Level

A README is always a **map**, never content itself. It answers 4 questions only: What is this? What's inside? Where do I start? Who owns it?

### Company README (repo root — Home + Dashboard + Navigator, all in one page)

```
┌───────────────────────────────────────────────────┐
│  [Company] Company OS                                    │
│  Repository Home / README                                  │
├───────────────────────────────────────────────────┤
│  👋 Welcome — Start Here                                    │
│  New employee? Start with Company Overview → Your            │
│  Department → Your Role.              [ → START-HERE.md ]     │
├───────────────────────────────────┬───────────────────┤
│  🏢 Company                          │  🏬 Departments         │
│  • Vision & Mission                   │  • Sales                │
│  • Leadership                          │  • Marketing             │
│  • Brands                               │  • RND                   │
│  • Org Chart                             │  • ... (from Doc 01)      │
│  [ → 03_RESOURCES/Company_Overview ]      │  [ → 01_AREAS/ ]            │
├───────────────────────────────────┴───────────────────┤
│  ⚡ Quick Access                                              │
│  • Company Master Standards (Docs 01–09)                      │
│  • Shared Templates              [ → 03_RESOURCES/ ]           │
├───────────────────────────────────────────────────┤
│  🎯 My Learning Path                                          │
│  Click your role and follow the guided sequence.                │
│                                          [ → Section 9 ]           │
├───────────────────────────────────────────────────┤
│  ❓ Need Help?                                                  │
│  Search • Glossary • Who Owns What • Raise an Issue                │
└───────────────────────────────────────────────────┘
```

### Department README (`01_AREAS/[Dept]/README.md`)

```
┌───────────────────────────────────────────────┐
│  [Department] Department                            │
│  Home › 01_AREAS › [Department]                        │
├───────────────────────────────────────────────┤
│  Department Purpose                                    │
│  What this department does and why it exists,           │
│  2–3 plain-English sentences.                              │
├───────────────────────────────────────────────┤
│  Sub-folders in this Department                            │
│  Policies • SOPs • Work Instructions • Templates •           │
│  Reports • Records • Knowledge Reference • Meeting Notes       │
├───────────────────────────────────────────────┤
│  Owner: [Accountable role, from Doc 01]                          │
├───────────────────────────────────────────────┤
│  Start Learning → [this department's slice of the New              │
│  Employee Journey, Section 9]                                          │
├───────────────────────────────────────────────┤
│  Related Departments (max 3, only if genuinely relevant)             │
└───────────────────────────────────────────────┘
```

Open Sales, open HR, open RND — the layout is identical every time. That consistency, not the content, is what makes the system learnable in one sitting.

---

## 6. Breadcrumb — Mandatory On Every Document

```
Home › 01_AREAS › [Department] › [Team, if applicable] › [Document Title]
```
**Real example:**
```
Home › 01_AREAS › RND — Research & Development › SOPs › RND-SOP-004 — New Product Testing Process
```
This answers, at a glance, the first of the three questions every page must answer (Section 12): *"Where am I right now?"*

---

## 7. Related Documents vs See Also — Kept Deliberately Separate

```
Related Documents             See Also
────────────────              ─────────
Directly relevant              Useful but optional
→ Required Before This          → Background reading
→ Next Step                      → Adjacent topics
→ Related Policy                  → Nice-to-know context
```
A page should never carry more than **~5–8 total outbound links** across both sections combined. If a topic genuinely needs more, that's a signal the content should be split into a proper topic sequence (Section 8) instead of link-dumped onto one page.

---

## 8. Guided Topic Reading Sequence

```
┌────────────┐   ┌──────────┐   ┌─────────┐   ┌─────┐   ┌────────┐   ┌───────────┐   ┌─────┐
│Introduction │──▶│ Concepts  │──▶│ Process  │──▶│ SOP │──▶│Examples │──▶│ Checklist │──▶│ FAQ │
└────────────┘   └──────────┘   └─────────┘   └─────┘   └────────┘   └───────────┘   └─────┘
                         Previous ← • Home • Index • Next →
                    Every document in a topic follows the same reading pattern
```
A user landing on a new topic (e.g. "Cold Email") never opens the SOP cold — they're carried through Introduction → Concepts → Process → SOP → Examples → Checklist → FAQ, each a separate file inside that department's existing folders (`Knowledge_Reference/`, `SOPs/`, per Doc 03) — this sequence requires no new folders, only consistent file ordering and cross-linking.

Skip a step only when it's genuinely not applicable to that specific topic — never skip steps just to save time writing them.

---

## 9. New Employee Journey — Full Sequence

```
┌───┐  START HERE      Welcome + how this whole system works
│ 1 │  ───────────────────────────────────────────────
└───┘

┌───┐  Company          Vision • Brands • Culture
│ 2 │  ───────────────────────────────────────────────
└───┘

┌───┐  Department        Purpose • Sub-folders • Owner
│ 3 │  ───────────────────────────────────────────────
└───┘

┌───┐  Role                Responsibilities • KPIs
│ 4 │  ───────────────────────────────────────────────
└───┘

┌───┐  Training              Guided topic sequence for that role
│ 5 │  ───────────────────────────────────────────────
└───┘

┌───┐  SOP                     Daily-work procedures for that role
│ 6 │  ───────────────────────────────────────────────
└───┘

┌───┐  Assessment                Checklist + sign-off with manager
│ 7 │  ───────────────────────────────────────────────
└───┘
```
This is a **path through content that already exists** — not a new folder. Steps 2–6 simply point, in this exact order, into `03_RESOURCES` and the relevant `01_AREAS/[Dept]/` folders. No employee is ever told "go read the whole Company OS" — they follow this one sequence and nothing more on Day 1.

---

## 10. Glossary

```
Company-wide terms  →  03_RESOURCES/Company_Master_Standards/Glossary.md
Department jargon    →  01_AREAS/[Dept]/Knowledge_Reference/Glossary.md
```
Any document may link an unfamiliar term straight to its glossary entry instead of re-explaining it inline. Reading the company-wide glossary is Step 2 of the New Employee Journey (Section 9).

---

## 11. Standard Document Template — Full Version

```
Breadcrumb:
Home › [Company] › [Department] › [Team] › [Document Title]

────────────────────────────────────────
[ Doc 04's Required Metadata Header — unchanged, reproduced here in full ]
Code · Title · Department · Type · PARA Bucket · Version ·
Lifecycle Status · Confidentiality · Superseded By ·
Owner (Accountable) · Responsible · Consulted · Informed ·
Created Date · Last Updated · Tags · Related Documents
────────────────────────────────────────

Title
Purpose
Who should read this?

[ Table of Contents — required for long documents only ]

------------------------------------------------
Introduction
Concepts
Process
SOP
Examples
Checklist
FAQ
------------------------------------------------

Related Documents        (max ~5–8 combined with See Also)
See Also

← Previous | Department Home | Next →
   (sequential topic series only — omit entirely for standalone reference docs)

[ Change Log — Doc 07 §2 ]
[ Feedback — Doc 07 §8: Was this helpful? / Report outdated / Suggest a change ]
```
This is the one template every document in the company follows, regardless of department, type, or company/brand — five years from now, no document should ever feel "lost."

---

## 12. "You Are Here" — Every Page Answers Three Questions

```
   Where am I?          →  Breadcrumb (Section 6)
   Who is this for?      →  "Who should read this?" line (Section 11)
   What do I do next?     →  Next Step / Previous-Next (Section 11)
```

---

## 13. Search Strategy

```
   Structure known?  →  Browse       (Section 4, left path)
   Role known?        →  Role Path    (Section 4, right path)
   Neither known?       →  Search      (always available, independent of both)
```
No employee is ever forced into folder-browsing as the only way to find something — Search and Role Path exist precisely so structure-browsing is a choice, not a requirement.

---

## 14. Dashboard = Navigation Hub

The Documentation Health Dashboard (full detail in Doc 07 §9) is reachable in exactly one click from the Company README's "Quick Access" block. It is not a new folder in Doc 03's tree — it's a live view generated from the metadata already sitting in every document's header (Doc 04), rendered via GitHub Projects/Actions (Doc 05 §4).

```
Company Dashboard
├── Current Goals
├── Active Projects
├── Pending Approvals
├── Department KPIs
├── Upcoming Reviews
└── Quick Links
```
