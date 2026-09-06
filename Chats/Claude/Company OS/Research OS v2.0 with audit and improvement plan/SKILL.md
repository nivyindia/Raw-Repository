---
name: research-os
description: Use this skill whenever the user wants to conduct business/market research, or mentions starting a research project, research brief, competitor analysis, industry research, or asks to "research X for the company." It runs the user's 12-step Research Operating System v1.1 — Goal → Research Question → Protocol → Search Strategy → Discovery → Primary Sources → Evidence Extraction → Deep Analysis → Quality Gate → Company Recommendations → Implementation/SOP (+ optional Audit & Revision Loop) → Final Report — so they never have to retype the workflow or its prompts.
---

# Research Operating System v1.1 — Claude Skill

This skill runs the user's own 12-step research workflow (plus an optional post-implementation audit layer). The workflow and prompt structure stay the same every time — only the topic, business context, and desired outcome change per project.

## How to start

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

## STEP 0 — Research Brief
Take the user's raw goal and turn it into a structured Research Brief.

## STEP 1 — Research Question
Apply this exact instruction to the Step 0 output:
> Convert this raw goal into a professional research brief and precise research questions. Provide: 1. Business Problem 2. Research Objective 3. Primary Research Question 4. 5–10 Secondary Research Questions 5. Key Variables/Factors to investigate 6. Target Industry/Geography/Company Size if relevant 7. Time Period to consider 8. What to explicitly exclude from scope 9. What business decision this research should support 10. Success criteria for research completion. Do not make assumptions where information is missing — instead create an "Information Needed" section. Make the research question precise enough that another researcher could reproduce systematic web research from it.

## STEP 2 — Research Protocol
Apply to the Step 1 output:
> Create a professional Research Protocol including: Research Objective, Primary/Secondary Questions, Scope, Out of Scope, Geography, Industry, Time Period, Target Population/Companies/Market, Types of Evidence Required, Required Source Types, Inclusion Criteria, Exclusion Criteria, Key Research Themes, Key Search Keywords, Synonyms/Related Terms, Companies/Competitors to investigate, Data points that must be collected, Potential sources of bias, Known limitations, Final deliverables. Detailed enough that another researcher could reproduce the process. Flag ambiguity instead of assuming.

## STEP 3 — Search Strategy
Apply to the Step 2 output:
> Create a comprehensive search strategy divided into: A. Fundamentals B. Academic Research C. Industry Reports D. Market Data E. Best Practices F. Case Studies G. Leading Companies H. Competitor Practices I. Failure Cases J. Contradictory Evidence K. Statistics and Benchmarks L. Tools/Technology M. Regulations/Legal/Compliance N. Geography-specific O. Latest Developments. 5–10 highly specific queries per category, usable directly in a search engine, favoring primary-source terms (research paper, official report, government data, annual report, original survey, case study, dataset, white paper). End with: Must-Find Sources, Nice-to-Have Sources, Sources to Avoid.

## STEP 4 — Discovery Research (use the web_search tool)
For each query group from Step 3, actually run web searches (use the search tool available in this conversation). For each important finding extract: Key Finding, Evidence, Source, Publication Date, Source Type, Why This Source Matters, Confidence (High/Medium/Low), Important Caveat. Prioritize primary/original sources over secondary summaries; do not treat marketing blogs/SEO content as strong evidence; present both sides of contradictory evidence. End each search round with: What did this establish? What remains unknown? What should the next search investigate? Save only the important findings and original source links — not everything returned.

## STEP 5 — Primary Source Verification
Before treating any statistic or claim as evidence, trace it to where it actually originated (paper / company data / annual report / survey / a blog repeating another blog). Build a source library table: Source | Type | Date | URL | Key Finding | Reliability. **Rule: AI-generated summaries are discovery tools; original sources are evidence** — don't skip this verification step even under time pressure.

## STEP 6 — Evidence Extraction
If the user provides documents/papers/reports/PDFs, extract per source: Source Title, Author/Organization, Publication Date, Research Method, Sample/Population, Geography, Main Research Question, Key Findings, Important Statistics, Effect/Impact, Limitations, Potential Bias, What the evidence actually proves, What it does NOT prove, Practical business implication, Exact source/page reference. Build an Evidence Matrix classifying each into Strong/Moderate/Weak-Anecdotal. Never invent missing information — write "Not Reported" instead. Separate the author's opinion from actual findings.

## STEP 7 — Deep Analysis
From the Evidence Matrix, identify: Major Patterns, Repeated Findings, Strongest Evidence, Contradictory Findings, Important Differences and possible reasons, Industry Benchmarks, Leading Company Practices, Commonly Recommended Practices, Practices supported by weak evidence, Common mistakes/failure patterns, Research Gaps, Unanswered Questions, Opportunities, Risks, What's well-supported vs. what's assumption/opinion. Connect every conclusion to its supporting evidence; write "Evidence insufficient to conclude" where that's true. End with "Top 10 Evidence-Based Insights."

## STEP 8 — Quality Gate (adversarial review)
Treat this as a genuinely separate, skeptical pass — actively look for reasons the Step 7 analysis could be wrong, don't just restate it approvingly. Check for: claims with no supporting evidence, sources that don't actually support the claim, correlation presented as causation, weak sample size/methodology, source bias, outdated information, missing contradictory evidence, an available primary source that wasn't used, statistics without context, conclusions stronger than the evidence allows, research gaps, assumptions made along the way. Produce a table: Claim | Supporting Evidence | Problem | Severity (Critical/High/Medium/Low) | Required Correction. Classify every major claim: A. Safe to Use / B. Requires Qualification / C. Should Be Removed / D. Requires Additional Research. Never call something "proven" beyond what the evidence supports.

## STEP 9 — Company-Specific Application
Ask for (if not already given): Company, Industry, Company Size, Current Stage, Current Situation, Business Problem, Business Goal, Budget/Resource Constraints, Existing Systems. Then determine: which findings apply and which don't (and why), what to adopt/modify/avoid, priority order, potential impact of each recommendation, implementation risks. Split into NOW (immediate) / NEXT (30–90 days) / LATER. Connect every recommendation to its supporting evidence; clearly separate evidence-based recommendations from strategic judgment/assumptions.

## STEP 10 — Implementation System
Convert Step 9 into: Top 5 Strategic Priorities; 30-Day Plan (week by week); 60-Day Plan; 90-Day Plan; SOPs Required (each with: Name, Objective, Owner, Trigger, Inputs, Step-by-Step Process, Tools Required, Expected Output, Quality Check, Escalation Process); Roles & Responsibilities; KPIs (KPI, Baseline, Target, Measurement Frequency, Next Review Date, KPI Owner); Risks (Risk, Probability, Impact, Mitigation); Quick Wins. Also set one overall **Rollout Review Checkpoint** (e.g. end of the 90-Day Plan, or a date the user specifies) — this is the point Step 10C will audit against. Never propose an implementation step with no supporting evidence or logical rationale — label assumptions explicitly as "Assumption."

---

## v1.1 AUDIT & REVISION LOOP (Steps 10A–10E) — Optional

*Only run this block if the user said "Tracking Rollout? Yes" in the intake form, or explicitly asks for post-implementation auditing. For a one-off report, skip straight from Step 10 to Step 11.*

### STEP 10A — Pre-Implementation Audit
Before rollout starts, run one more skeptical pass — this time over the Step 10 Implementation System itself, not the underlying research. Check that every SOP, KPI, and 30/60/90-day action still traces back to a specific Step 9 recommendation and its supporting evidence. Flag: implementation items with no evidence trail, KPIs with no realistic baseline or measurement method, SOPs missing an owner or escalation path, resource/budget assumptions never validated against Company Context. Produce a table: Implementation Item | Traced To (Recommendation/Evidence) | Audit Issue | Severity | Fix Required. Nothing should roll out with a "Critical" item still unresolved.

### STEP 10B — Implementation Tracking Log
Once rollout begins, keep a running log the user updates as work actually happens: Date | Action Taken | Planned vs Actual | Owner | Status (On Track/Delayed/Blocked/Done) | Notes. This step doesn't analyze anything — it's just the structured record that makes Step 10D possible later. Default the update cadence to the shortest Measurement Frequency already set in Step 10's KPI table (don't ask a separate, possibly conflicting cadence) — only ask the user if they want a different cadence for the log itself.

### STEP 10C — Outcome Audit (at the review checkpoint)
At the Rollout Review Checkpoint (or each KPI's own Next Review Date, whichever applies — both set in Step 10), compare actual measured KPI values against the Step 10 baseline/target. Build: KPI | Baseline | Target | Actual | Variance | On Track? (Yes/No/Partial). Where a KPI wasn't tracked or data is missing, write "Not Measured" — never estimate a number that wasn't actually collected. Separate misses caused by poor execution (the plan wasn't actually followed) from misses caused by a wrong underlying recommendation (the plan was followed and still didn't work).

### STEP 10D — Gap & Root-Cause Analysis
For every KPI marked "No"/"Partial" in Step 10C and every "Delayed"/"Blocked" item in Step 10B, dig into why: Root Cause (Execution Gap / Resourcing / Wrong Assumption / External Factor / Evidence Was Weak to Begin With), Contributing Factors, and — where relevant — What Step 8's Quality Gate Should Have Caught. Keep this blame-neutral and evidence-based; the goal is calibrating the research process, not assigning fault.

### STEP 10E — Revision & Re-Loop
Turn the Step 10D findings into concrete revisions: which SOPs/recommendations stay as-is, which get modified (and exactly how), which get retired. If the root cause was "Wrong Assumption" or "Evidence Was Weak," route the new evidence back to Step 7/8 for genuine re-analysis rather than patching the recommendation directly. Version the report (v1.0 → v1.1, etc.) and log the change in a short Revision History table: Version | Date | What Changed | Why | Based On.

---

## STEP 11 — Final Research Report
Combine Steps 1, 7, 8, 9, 10 (and, if the audit loop ran, the Step 10E revision summary) into a decision-ready report with this structure: Executive Summary, Business Problem, Research Objective, Research Questions, Research Methodology, Scope & Limitations, Key Findings, Evidence Summary, Industry/Market Analysis, Competitor/Company Benchmark, Contradictions and Debate, Key Insights, Implications for Our Company, Recommendations, Prioritization, Implementation Roadmap, SOPs/Processes Required, KPIs, Risks, Assumptions, Research Gaps, Conclusion, Sources/References. Rules: separate facts from recommendations; connect every factual claim to its source; never invent claims; never present weak evidence as strong; never hide contradictory evidence; give source+date for every important statistic; flag areas with no evidence available. The Executive Summary alone should be enough for a CEO to understand the decision context.

## STEP 12 — File it in the Company Knowledge Base
Once the report is done, store it per the company's actual documentation standard (if this Claude account also has the Company OS Classifier skill/governance available, use that — Department, Type=REP, full metadata header). At minimum, capture: Research Title, Department, Research Owner, Research Date, Version, Research Question, Research Scope, Sources, Confidence Level, Key Findings, Recommendations, SOPs Created, KPIs, Next Review Date.

---

## Operating rules for this skill
- Run one step at a time, show the output, then ask whether to proceed to the next step, unless the user says "run the whole thing end to end."
- Step 4 (Discovery Research) should actually use the web_search tool — don't simulate search results from memory.
- Step 8 (Quality Gate) must be genuinely critical, not a rubber stamp — this is the whole point of the workflow.
- Steps 10A–10E are optional (v1.1) — only run them for implementation-heavy research the user is actually tracking through rollout; skip them for one-off reports.
- Don't skip steps to save time; if the user wants a faster pass, they can set Research Depth to "Quick" in the intake form, which shortens each step's output, not the number of steps.
