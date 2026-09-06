# Research Operating System (Research OS) — Final Master Document
### v1.1 (Skill + Optional Audit Layer) + Setup & Deployment Plan — Merged

**Kya hai ye file:** `Research_OS_Skill.zip` (SKILL.md) + `Research_os_implementation_plan.zip` (Setup Plan + Progress Tracker) — dono ko ek jagah merge kiya gaya hai, plus Phase 5 ka v1.1 Audit & Revision Loop (Steps 10A–10E) ab Part B mein add ho chuka hai. Ye single source of truth hai: kaise setup karna hai (Part A) aur actual workflow kaise chalta hai (Part B), plus tracking (Part C).

**Is version mein kya update hua:** Phase 4 (End-to-End Test Run) manual hai isliye skip kiya gaya hai — wo aapko khud teeno platforms pe karna hoga. Phase 5 (v1.1 Audit Layer) ka file-level kaam complete kar diya gaya hai: Steps 10A–10E draft karke `SKILL.md` aur ChatGPT instructions dono mein merge kar diya gaya hai (Perplexity file intentionally untouched, jaisa plan khud kehta hai). Source file `Research_OS_v1.1_Implementation_Plan.md` uploads mein nahi mili, isliye Steps 10A–10E yahan originally draft kiye gaye hain — audit → tracking log → outcome audit → root-cause → revision-loop pattern follow karte hue.

---

# PART A — Setup & Deployment Plan (Phase 1–5)

**Goal:** Teeno platforms (Claude, ChatGPT, Perplexity) pe Research OS ko is tarah set up karna ki future mein **koi bhi topic** do, wahi 12-step (+ optional v1.1 audit layer) systematic research automatically chale — bina har baar workflow retype kiye.

**Source files:**
| File | Platform | Role |
|---|---|---|
| `SKILL.md` (→ Part B, is document mein) | Claude | Full 12-step skill definition |
| `ChatGPT-Custom-GPT-Instructions.md` | ChatGPT | Same 12-step, Custom GPT/Project format |
| `Perplexity-Space-Instructions.md` | Perplexity | Sirf Step 4 (Discovery) + part of Step 5 — search/discovery engine role |

**Division of labor:**
```
Claude / ChatGPT (Steps 0–3)   →  Research Brief, Question, Protocol, Search Strategy
        ↓
Perplexity Space (Step 4–5)     →  actual web search, source discovery, primary verification
        ↓
Claude / ChatGPT (Steps 6–12)   →  Evidence Extraction, Analysis, Quality Gate, Recommendations,
                                     Implementation, Final Report, Filing
```
Teeno tools alag-alag kaam karte hain — ek dusre ka replacement nahi hain. Isliye teeno setup karne padenge.

---

## Phase 1 — Claude Skill Setup

| # | Task | How | Status |
|---|---|---|---|
| 1.1 | Claude.ai settings mein Skills feature access confirm karo | Settings → Capabilities/Skills (agar available na ho, "Skills" beta enable karna pad sakta hai) | ⬜ |
| 1.2 | `research-os-skill` folder banao (already zip mein hai) | `SKILL.md` file ke saath — koi extra file nahi chahiye Claude side | ⬜ |
| 1.3 | Skill upload karo | Claude.ai → Settings → Skills → "Upload Skill" / "Create Skill" → `SKILL.md` select karo | ⬜ |
| 1.4 | Skill trigger verify karo | Naya chat kholo, likho "I want to research [koi random topic] for the company" — Claude ko automatically Research OS skill trigger karni chahiye | ⬜ |
| 1.5 | Skill naam/description confirm karo | `SKILL.md` ke top metadata mein `name: research-os` aur `description` line — isko touch mat karo jab tak trigger sahi kaam kar raha ho | ⬜ |

**Output of Phase 1:** Claude.ai mein "research-os" naam ki skill active, kisi bhi research-type message par auto-trigger karti hai.

---

## Phase 2 — ChatGPT Custom GPT Setup

| # | Task | How | Status |
|---|---|---|---|
| 2.1 | ChatGPT kholo → "Explore GPTs" → "Create" | Naya Custom GPT banayega | ⬜ |
| 2.2 | GPT ka naam do | Suggest: **"Research OS"** | ⬜ |
| 2.3 | "Configure" tab → "Instructions" field mein pura content paste karo | `ChatGPT-Custom-GPT-Instructions.md` ke andar diya "Instructions to paste" code-block — pura block copy karo | ⬜ |
| 2.4 | Capabilities enable karo | "Web Browsing" ON karo (Step 4 ke liye zaroori) | ⬜ |
| 2.5 | Conversation starters add karo (optional) | e.g. "Research [topic] for [department]", "Run Research OS end-to-end on...", "Continue from Step [X]" | ⬜ |
| 2.6 | Save/Publish karo | "Only me" visibility rakho agar internal company use hai | ⬜ |
| 2.7 | Test karo | Naya chat: "I want to research competitor pricing strategy for Sales department" — GPT ko Research Intake Form maangna chahiye | ⬜ |

**Alternative (agar Custom GPT nahi, sirf ChatGPT Project chahiye):**
ChatGPT → "Projects" → naya project "Research OS" banao → Project Settings → "Custom Instructions" → wahi block paste karo. Har chat is project ke andar automatically follow karega.

**Output of Phase 2:** ChatGPT mein reusable "Research OS" GPT/Project ready, jo Steps 0–3 aur 6–12 handle karega.

---

## Phase 3 — Perplexity Space Setup

| # | Task | How | Status |
|---|---|---|---|
| 3.1 | Perplexity kholo → "Spaces" → "Create Space" | | ⬜ |
| 3.2 | Space ka naam do | Suggest: **"Research OS"** | ⬜ |
| 3.3 | "Custom Instructions" field mein paste karo | `Perplexity-Space-Instructions.md` ke andar diya block | ⬜ |
| 3.4 | Focus/Model setting (agar available ho) | "Academic" ya "Web" focus try karo — jo primary-source-heavy results de, marketing blogs kam | ⬜ |
| 3.5 | Test karo | Space ke andar ek chhota query daalo (Step 3 se ek category) — check karo Key Finding/Evidence/Source/Confidence format mein reply aa raha hai | ⬜ |

**Important reminder:** Is Space mein "give me everything about X" jaisa giant query mat daalo — Step 3 (Search Strategy) ke categories one-by-one yahan run karo (Fundamentals → Academic → Industry Reports → ... etc.)

**Output of Phase 3:** Perplexity mein "Research OS" Space ready — discovery/search engine role ke liye.

---

## Phase 4 — End-to-End Test Run (sabhi teen platforms ek saath)

| # | Task | Detail | Status |
|---|---|---|---|
| 4.1 | Ek test topic choose karo | Kuch low-stakes, real interest wala — e.g. "AI adoption trends in Indian SMEs" | ⬜ |
| 4.2 | Claude Skill mein Steps 0–3 run karo | Research Intake Form bharo, Step 0→1→2→3 ek-ek karke output lo | ⬜ |
| 4.3 | Step 3 ki queries Perplexity Space mein daalo | Category-wise, ek-ek karke; findings copy karo | ⬜ |
| 4.4 | Findings wapas Claude mein paste karo, Steps 5–8 continue karo | Evidence extraction, analysis, quality gate | ⬜ |
| 4.5 | Steps 9–12 complete karo | Company recommendations, implementation, final report, filing | ⬜ |
| 4.6 | Gaps note karo | Kahin wording confusing lagi, koi step skip hua, ya Perplexity output expected format mein nahi aaya — sab likho | ⬜ |
| 4.7 | Fixes apply karo | Jo gap mila, respective file (`SKILL.md` / ChatGPT instructions / Perplexity instructions) mein directly edit karo | ⬜ |

**Output of Phase 4:** Verified, working 3-platform pipeline — ab kisi bhi naye topic pe seedha use kar sakte ho.

---

## Phase 5 (Optional) — v1.1 Audit Layer Merge

Agar implementation-heavy research (jahan Step 10 ke baad company mein actual rollout bhi karna hai) automatically audit + revision loop follow kare:

| # | Task | Status |
|---|---|---|
| 5.1 | Steps 10A–10E ko Part B ke Step 10 aur 11 ke beech paste karo | ✅ Done — neeche Part B mein dekho |
| 5.2 | Same steps ChatGPT Custom GPT Instructions block mein bhi add karo (re-save/re-configure) | ✅ File done — GPT mein re-paste karna manual hai |
| 5.3 | Perplexity Space ko touch mat karo — 10A–10E sirf Claude/ChatGPT side ka kaam hai | ✅ Confirmed untouched |

*(Source file `Research_OS_v1.1_Implementation_Plan.md` upload nahi hui thi, isliye Steps 10A–10E is session mein originally draft kiye gaye — audit → tracking log → outcome audit → root-cause analysis → revision loop pattern, jo upar diye gaye Phase 5 goal se match karta hai.)*

---

## Dependency Order

```
Phase 1 (Claude Skill)  ─┐
Phase 2 (ChatGPT GPT)    ├─→  Phase 4 (End-to-End Test)  →  Phase 5 (optional v1.1 audit merge)
Phase 3 (Perplexity)    ─┘
```
Phase 1–3 kisi bhi order mein parallel ho sakte hain (independent). Phase 4 tabhi shuru karo jab teeno ready ho. Phase 5 optional hai, sirf agar heavy implementation projects karne hain.

---

# PART B — The Research OS Workflow (Claude Skill Definition)

```yaml
name: research-os
description: >
  Use this skill whenever the user wants to conduct business/market research,
  or mentions starting a research project, research brief, competitor analysis,
  industry research, or asks to "research X for the company." It runs the
  user's 12-step Research Operating System v1.1 — Goal → Research Question →
  Protocol → Search Strategy → Discovery → Primary Sources → Evidence
  Extraction → Deep Analysis → Quality Gate → Company Recommendations →
  Implementation/SOP (+ optional Audit & Revision Loop) → Final Report — so
  they never have to retype the workflow or its prompts.
```

This skill runs the user's own 12-step research workflow (plus an optional post-implementation audit layer). The workflow and prompt structure stay the same every time — only the topic, business context, and desired outcome change per project.

### How to start

If the user hasn't given the basics yet, ask them to fill this in (or accept it in whatever form they give it):

```
Research Intake Form
Research Topic:        [What do you want to research?]
Department:             [HR / Sales / Marketing / Operations / Finance / Technology / Strategy]
Business Problem:        [What problem are you trying to solve?]
Desired Outcome:          [What decision or outcome should this research produce?]
Company Context:           [Relevant information about the company]
Target Market/Geography:    [If relevant]
Time Horizon:                 [Current / Last 3 Years / Last 5 Years / etc.]
Constraints:                   [Budget / Team / Technology / Legal / Time / etc.]
Expected Deliverable:            [Strategy / SOP / Market Report / Competitor Analysis / Policy / etc.]
Deadline:                          [If relevant]
Research Depth:                     [Quick / Standard / Deep / Academic-Level]
Tracking Rollout?:                   [Yes — will implement and audit results / No — one-off report]
```

Then run the steps below **in order**, one at a time, showing the user each step's output before moving to the next — don't skip ahead or silently merge steps.

---

### STEP 0 — Research Brief
Take the user's raw goal and turn it into a structured Research Brief.

### STEP 1 — Research Question
Apply this exact instruction to the Step 0 output:
> Convert this raw goal into a professional research brief and precise research questions. Provide: 1. Business Problem 2. Research Objective 3. Primary Research Question 4. 5–10 Secondary Research Questions 5. Key Variables/Factors to investigate 6. Target Industry/Geography/Company Size if relevant 7. Time Period to consider 8. What to explicitly exclude from scope 9. What business decision this research should support 10. Success criteria for research completion. Do not make assumptions where information is missing — instead create an "Information Needed" section. Make the research question precise enough that another researcher could reproduce systematic web research from it.

### STEP 2 — Research Protocol
Apply to the Step 1 output:
> Create a professional Research Protocol including: Research Objective, Primary/Secondary Questions, Scope, Out of Scope, Geography, Industry, Time Period, Target Population/Companies/Market, Types of Evidence Required, Required Source Types, Inclusion Criteria, Exclusion Criteria, Key Research Themes, Key Search Keywords, Synonyms/Related Terms, Companies/Competitors to investigate, Data points that must be collected, Potential sources of bias, Known limitations, Final deliverables. Detailed enough that another researcher could reproduce the process. Flag ambiguity instead of assuming.

### STEP 3 — Search Strategy
Apply to the Step 2 output:
> Create a comprehensive search strategy divided into: A. Fundamentals B. Academic Research C. Industry Reports D. Market Data E. Best Practices F. Case Studies G. Leading Companies H. Competitor Practices I. Failure Cases J. Contradictory Evidence K. Statistics and Benchmarks L. Tools/Technology M. Regulations/Legal/Compliance N. Geography-specific O. Latest Developments. 5–10 highly specific queries per category, usable directly in a search engine, favoring primary-source terms (research paper, official report, government data, annual report, original survey, case study, dataset, white paper). End with: Must-Find Sources, Nice-to-Have Sources, Sources to Avoid.

### STEP 4 — Discovery Research (use the web_search tool)
For each query group from Step 3, actually run web searches (use the search tool available in this conversation). For each important finding extract: Key Finding, Evidence, Source, Publication Date, Source Type, Why This Source Matters, Confidence (High/Medium/Low), Important Caveat. Prioritize primary/original sources over secondary summaries; do not treat marketing blogs/SEO content as strong evidence; present both sides of contradictory evidence. End each search round with: What did this establish? What remains unknown? What should the next search investigate? Save only the important findings and original source links — not everything returned.

### STEP 5 — Primary Source Verification
Before treating any statistic or claim as evidence, trace it to where it actually originated (paper / company data / annual report / survey / a blog repeating another blog). Build a source library table: Source | Type | Date | URL | Key Finding | Reliability. **Rule: AI-generated summaries are discovery tools; original sources are evidence** — don't skip this verification step even under time pressure.

### STEP 6 — Evidence Extraction
If the user provides documents/papers/reports/PDFs, extract per source: Source Title, Author/Organization, Publication Date, Research Method, Sample/Population, Geography, Main Research Question, Key Findings, Important Statistics, Effect/Impact, Limitations, Potential Bias, What the evidence actually proves, What it does NOT prove, Practical business implication, Exact source/page reference. Build an Evidence Matrix classifying each into Strong/Moderate/Weak-Anecdotal. Never invent missing information — write "Not Reported" instead. Separate the author's opinion from actual findings.

### STEP 7 — Deep Analysis
From the Evidence Matrix, identify: Major Patterns, Repeated Findings, Strongest Evidence, Contradictory Findings, Important Differences and possible reasons, Industry Benchmarks, Leading Company Practices, Commonly Recommended Practices, Practices supported by weak evidence, Common mistakes/failure patterns, Research Gaps, Unanswered Questions, Opportunities, Risks, What's well-supported vs. what's assumption/opinion. Connect every conclusion to its supporting evidence; write "Evidence insufficient to conclude" where that's true. End with "Top 10 Evidence-Based Insights."

### STEP 8 — Quality Gate (adversarial review)
Treat this as a genuinely separate, skeptical pass — actively look for reasons the Step 7 analysis could be wrong, don't just restate it approvingly. Check for: claims with no supporting evidence, sources that don't actually support the claim, correlation presented as causation, weak sample size/methodology, source bias, outdated information, missing contradictory evidence, an available primary source that wasn't used, statistics without context, conclusions stronger than the evidence allows, research gaps, assumptions made along the way. Produce a table: Claim | Supporting Evidence | Problem | Severity (Critical/High/Medium/Low) | Required Correction. Classify every major claim: A. Safe to Use / B. Requires Qualification / C. Should Be Removed / D. Requires Additional Research. Never call something "proven" beyond what the evidence supports.

### STEP 9 — Company-Specific Application
Ask for (if not already given): Company, Industry, Company Size, Current Stage, Current Situation, Business Problem, Business Goal, Budget/Resource Constraints, Existing Systems. Then determine: which findings apply and which don't (and why), what to adopt/modify/avoid, priority order, potential impact of each recommendation, implementation risks. Split into NOW (immediate) / NEXT (30–90 days) / LATER. Connect every recommendation to its supporting evidence; clearly separate evidence-based recommendations from strategic judgment/assumptions.

### STEP 10 — Implementation System
Convert Step 9 into: Top 5 Strategic Priorities; 30-Day Plan (week by week); 60-Day Plan; 90-Day Plan; SOPs Required (each with: Name, Objective, Owner, Trigger, Inputs, Step-by-Step Process, Tools Required, Expected Output, Quality Check, Escalation Process); Roles & Responsibilities; KPIs (KPI, Baseline, Target, Measurement Frequency, Next Review Date, KPI Owner); Risks (Risk, Probability, Impact, Mitigation); Quick Wins. Also set one overall **Rollout Review Checkpoint** (e.g. end of the 90-Day Plan, or a date the user specifies) — this is the point Step 10C will audit against. Never propose an implementation step with no supporting evidence or logical rationale — label assumptions explicitly as "Assumption."

---

#### v1.1 AUDIT & REVISION LOOP (Steps 10A–10E) — Optional

*Only run this block if the user is tracking an actual company rollout. For a one-off report, skip straight from Step 10 to Step 11.*

**STEP 10A — Pre-Implementation Audit:** Before rollout, run one more skeptical pass over the Step 10 Implementation System itself. Check every SOP/KPI/30-60-90-day action still traces to a specific Step 9 recommendation and its evidence. Flag items with no evidence trail, KPIs with no realistic baseline/measurement method, SOPs missing an owner or escalation path, unvalidated resource/budget assumptions. Table: Implementation Item | Traced To | Audit Issue | Severity | Fix Required. Nothing rolls out with an unresolved Critical item.

**STEP 10B — Implementation Tracking Log:** Once rollout begins, keep a running log the user updates as work happens: Date | Action Taken | Planned vs Actual | Owner | Status (On Track/Delayed/Blocked/Done) | Notes. No analysis here — just the record Step 10D needs later. Default the update cadence to the shortest Measurement Frequency already set in Step 10's KPI table (don't ask a separate, possibly conflicting cadence) — only ask if the user wants it different.

**STEP 10C — Outcome Audit:** At the Rollout Review Checkpoint (or each KPI's own Next Review Date, both set in Step 10), compare actual measured values against the Step 10 baseline/target. Table: KPI | Baseline | Target | Actual | Variance | On Track? (Yes/No/Partial). Missing data = "Not Measured," never an estimate. Separate misses from poor execution vs. a wrong underlying recommendation.

**STEP 10D — Gap & Root-Cause Analysis:** For every KPI marked No/Partial and every Delayed/Blocked log item, determine Root Cause (Execution Gap / Resourcing / Wrong Assumption / External Factor / Evidence Was Weak to Begin With), Contributing Factors, and what Step 8's Quality Gate should have caught, if relevant. Keep this blame-neutral and evidence-based.

**STEP 10E — Revision & Re-Loop:** Turn Step 10D findings into concrete revisions — keep, modify (how), or retire each SOP/recommendation. If root cause was Wrong Assumption or Weak Evidence, route new evidence back to Step 7/8 for genuine re-analysis. Version the report (v1.0 → v1.1) and log it: Version | Date | What Changed | Why | Based On.

---

### STEP 11 — Final Research Report
Combine Steps 1, 7, 8, 9, 10 (and, if the audit loop ran, the Step 10E revision summary) into a decision-ready report with this structure: Executive Summary, Business Problem, Research Objective, Research Questions, Research Methodology, Scope & Limitations, Key Findings, Evidence Summary, Industry/Market Analysis, Competitor/Company Benchmark, Contradictions and Debate, Key Insights, Implications for Our Company, Recommendations, Prioritization, Implementation Roadmap, SOPs/Processes Required, KPIs, Risks, Assumptions, Research Gaps, Conclusion, Sources/References. Rules: separate facts from recommendations; connect every factual claim to its source; never invent claims; never present weak evidence as strong; never hide contradictory evidence; give source+date for every important statistic; flag areas with no evidence available. The Executive Summary alone should be enough for a CEO to understand the decision context.

### STEP 12 — File it in the Company Knowledge Base
Once the report is done, store it per the company's actual documentation standard (if this Claude account also has the Company OS Classifier skill/governance available, use that — Department, Type=REP, full metadata header). At minimum, capture: Research Title, Department, Research Owner, Research Date, Version, Research Question, Research Scope, Sources, Confidence Level, Key Findings, Recommendations, SOPs Created, KPIs, Next Review Date.

---

### Operating rules for this skill
- Run one step at a time, show the output, then ask whether to proceed to the next step, unless the user says "run the whole thing end to end."
- Step 4 (Discovery Research) should actually use the web_search tool — don't simulate search results from memory.
- Step 8 (Quality Gate) must be genuinely critical, not a rubber stamp — this is the whole point of the workflow.
- Steps 10A–10E are optional (v1.1) — only run them for implementation-heavy research the user is actually tracking through rollout; skip them for one-off reports.
- Don't skip steps to save time; if the user wants a faster pass, they can set Research Depth to "Quick" in the intake form, which shortens each step's output, not the number of steps.

---

# PART C — Progress Tracker

**Important — single source of truth:** Is section ko is master doc ke andar manually track mat karo (do jagah status maintain karne se drift ho jata hai — jaisa is version se pehle hua tha, jahan ye section purani reh gayi thi jabki standalone tracker update ho chuka tha). Task-by-task status ke liye sirf **`Research_OS_Setup_Progress_Tracker.md`** dekho aur wahi update karo — ye file sirf ek quick pointer/snapshot hai.

## Quick Snapshot (see standalone tracker for detail)

| Phase | Status |
|---|---|
| Phase 1 — Claude Skill Setup | 🟡 File ready (`SKILL.md` v1.1); upload/trigger-test manual |
| Phase 2 — ChatGPT Custom GPT Setup | 🟡 File ready (Instructions v1.1); GPT create/publish manual |
| Phase 3 — Perplexity Space Setup | 🟡 File ready (unchanged); Space create manual |
| Phase 4 — End-to-End Test Run | ⬜ Not started — fully manual, intentionally skipped for now |
| Phase 5 — v1.1 Audit Layer Merge | ✅ File work done (all three files internally consistent, incl. audit-pass fixes) |

**Jab manual steps (Phase 1/2/3 ke platform-side tasks + Phase 4) complete ho jayein → Research OS production-ready hai, kisi bhi naye topic pe seedha use karo.**

---

*Merged from: `Research_OS_Skill.zip` (SKILL.md v1.1) + `Research_os_implementation_plan.zip` (Implementation Plan + Progress Tracker). ChatGPT-Custom-GPT-Instructions.md (v1.1) aur Perplexity-Space-Instructions.md (unchanged) alag platform-specific files hain, isliye separately use karo — unka content is master file mein duplicate nahi kiya gaya.*
