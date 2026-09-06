# Research OS — Setup Implementation Plan
## Claude Skill + ChatGPT Custom GPT + Perplexity Space (kisi bhi topic pe research ke liye)

**Goal:** Teeno platforms (Claude, ChatGPT, Perplexity) pe Research OS ko is tarah set up karna ki future mein **koi bhi topic** do, wahi 12-step (+ v1.1 audit layer) systematic research automatically chale — bina har baar workflow retype kiye.

**Available files** (`Research_OS_Skill.zip` se already extracted):
| File | Platform | Role |
|---|---|---|
| `SKILL.md` | Claude | Full 12-step skill definition |
| `ChatGPT-Custom-GPT-Instructions.md` | ChatGPT | Same 12-step, Custom GPT/Project format |
| `Perplexity-Space-Instructions.md` | Perplexity | Sirf Step 4 (Discovery) + part of Step 5 — search/discovery engine role |

**Division of labor (important to understand before setup):**
```
Claude / ChatGPT (Steps 0–3)   →  Research Brief, Question, Protocol, Search Strategy
        ↓
Perplexity Space (Step 4–5)     →  actual web search, source discovery, primary verification
        ↓
Claude / ChatGPT (Steps 6–12)   →  Evidence Extraction, Analysis, Quality Gate, Recommendations,
                                     Implementation, Final Report, Filing
```
Teeno tools **alag-alag kaam** karte hain — ek dusre ka replacement nahi hain. Isliye teeno setup karne padenge.

---

## Phase 1 — Claude Skill Setup

| # | Task | How |
|---|---|---|
| 1.1 | Claude.ai settings mein Skills feature access confirm karo | Settings → Capabilities/Skills (agar available na ho, "Skills" beta enable karna pad sakta hai) |
| 1.2 | `research-os-skill` folder banao (already zip mein hai) | `SKILL.md` file ke saath — koi extra file nahi chahiye Claude side |
| 1.3 | Skill upload karo | Claude.ai → Settings → Skills → "Upload Skill" / "Create Skill" → `SKILL.md` select karo |
| 1.4 | Skill trigger verify karo | Naya chat kholo, likho "I want to research [koi random topic] for the company" — Claude ko automatically Research OS skill trigger karni chahiye (description mein ye trigger-phrases already defined hain) |
| 1.5 | Skill naam/description confirm karo | `SKILL.md` ke top metadata mein `name: research-os` aur `description` line — ye Claude ko batati hai kab skill use karni hai, isko touch mat karo jab tak trigger sahi kaam kar raha ho |

**Output of Phase 1:** Claude.ai mein "research-os" naam ki skill active, kisi bhi research-type message par auto-trigger karti hai.

---

## Phase 2 — ChatGPT Custom GPT Setup

| # | Task | How |
|---|---|---|
| 2.1 | ChatGPT kholo → "Explore GPTs" → "Create" | Ye naya Custom GPT banayega |
| 2.2 | GPT ka naam do | Suggest: **"Research OS"** |
| 2.3 | "Configure" tab mein jao, "Instructions" field mein pura content paste karo | `ChatGPT-Custom-GPT-Instructions.md` ke andar diya "Instructions to paste" code-block (line 11 se 120 tak) — pura block copy karo, sirf ``` markers ke andar wala part |
| 2.4 | Capabilities enable karo | "Web Browsing" ON karo (Step 4 ke liye zaroori — agar tumhare paas ChatGPT Plus/browsing access hai) |
| 2.5 | Conversation starters add karo (optional but useful) | e.g. "Research [topic] for [department]", "Run Research OS end-to-end on...", "Continue from Step [X]" |
| 2.6 | Save/Publish karo | "Only me" visibility rakho agar internal company use hai |
| 2.7 | Test karo | Naya chat: "I want to research competitor pricing strategy for Sales department" — GPT ko Research Intake Form maangna chahiye |

**Alternative (agar Custom GPT nahi, sirf ChatGPT Project chahiye):**
- ChatGPT → "Projects" → naya project "Research OS" banao → Project Settings → "Custom Instructions" → wahi block paste karo. Har chat is project ke andar automatically follow karega.

**Output of Phase 2:** ChatGPT mein reusable "Research OS" GPT/Project ready, jo Steps 0–3 aur 6–12 handle karega.

---

## Phase 3 — Perplexity Space Setup

| # | Task | How |
|---|---|---|
| 3.1 | Perplexity kholo → "Spaces" → "Create Space" | |
| 3.2 | Space ka naam do | Suggest: **"Research OS"** |
| 3.3 | "Custom Instructions" field mein paste karo | `Perplexity-Space-Instructions.md` ke andar diya "Custom Instructions to paste" code-block (line 16–53) |
| 3.4 | Focus/Model setting (agar available ho) | "Academic" ya "Web" focus try karo — jo primary-source-heavy results de, marketing blogs kam |
| 3.5 | Test karo | Space ke andar ek chhota query daalo (Step 3 se ek category, e.g. "Industry Reports on [topic]") — check karo ki Key Finding/Evidence/Source/Confidence format mein reply aa raha hai |

**Important reminder (already noted in file):** Is Space mein "give me everything about X" jaisa ek giant query mat daalo — Step 3 (Search Strategy, jo Claude/ChatGPT banayega) ke categories one-by-one yahan run karo (Fundamentals → Academic → Industry Reports → ... etc.)

**Output of Phase 3:** Perplexity mein "Research OS" Space ready — discovery/search engine role ke liye.

---

## Phase 4 — End-to-End Test Run (sabhi teen platforms ek saath)

| # | Task | Detail |
|---|---|---|
| 4.1 | Ek test topic choose karo | Kuch low-stakes, real interest wala — e.g. "AI adoption trends in Indian SMEs" |
| 4.2 | Claude Skill mein Steps 0–3 run karo | Research Intake Form bharo, Step 0→1→2→3 ek-ek karke output lo |
| 4.3 | Step 3 ki queries Perplexity Space mein daalo | Category-wise, ek-ek karke; findings copy karo |
| 4.4 | Findings wapas Claude mein paste karo, Steps 5–8 continue karo | Evidence extraction, analysis, quality gate |
| 4.5 | Steps 9–12 complete karo | Company recommendations, implementation, final report, filing |
| 4.6 | Gaps note karo | Kahin bhi wording confusing lagi, ya koi step skip ho gaya, ya Perplexity ka output expected format mein nahi aaya — sab likho |
| 4.7 | Fixes apply karo | Jo bhi gap mila, respective file (`SKILL.md` / ChatGPT instructions / Perplexity instructions) mein directly edit karo |

**Output of Phase 4:** Verified, working 3-platform pipeline — ab kisi bhi naye topic pe seedha use kar sakte ho.

---

## Phase 5 (Optional) — v1.1 Audit Layer Merge

Agar chahte ho ki implementation-heavy research (jahan Step 10 ke baad actual company mein rollout bhi karna hai) automatically audit + revision loop follow kare:

| # | Task |
|---|---|
| 5.1 | Pehle se banayi gayi `Research_OS_v1.1_Implementation_Plan.md` ke Steps 10A–10E ko `SKILL.md` mein Step 10 aur 11 ke beech paste karo |
| 5.2 | Same steps `ChatGPT-Custom-GPT-Instructions.md` ke Instructions block mein bhi add karo (Custom GPT ko re-save/re-configure karna hoga) |
| 5.3 | Perplexity Space ko touch mat karo — 10A–10E sirf Claude/ChatGPT side ka kaam hai (Perplexity sirf discovery karta hai) |

*(Detail wording, dependency table, aur progress format — already `Research_OS_v1.1_Implementation_Plan.md` mein hai, wahi use karo.)*

---

## Dependency Order

```
Phase 1 (Claude Skill)  ─┐
Phase 2 (ChatGPT GPT)    ├─→  Phase 4 (End-to-End Test)  →  Phase 5 (optional v1.1 audit merge)
Phase 3 (Perplexity)    ─┘
```
Phase 1–3 kisi bhi order mein parallel ho sakte hain (independent). Phase 4 tabhi shuru karo jab teeno ready ho. Phase 5 optional hai, sirf agar heavy implementation projects karne hain.

---

*Companion file: `Research_OS_Setup_Progress_Tracker.md` — isi plan ko track karne ke liye.*
