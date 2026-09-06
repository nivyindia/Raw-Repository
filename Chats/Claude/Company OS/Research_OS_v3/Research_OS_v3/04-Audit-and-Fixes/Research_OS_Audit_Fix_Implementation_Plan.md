# Research OS — Audit Fix Implementation Plan

**Goal:** `Research_OS_Audit_Report.md` mein mile 7 issues ko verify karna aur teeno platforms (Claude, ChatGPT, Perplexity) mein consistent tareeke se roll out karna, taaki jo file-level fixes ho chuke hain wo actual production setup mein bhi reflect ho.

**Important:** File-level fixes already ho chuke hain (`SKILL.md`, `ChatGPT-Custom-GPT-Instructions.md`, `Research_OS_Final.md` — sab v1.1, audit-consistent). Ye plan sirf **verification** aur **manual roll-out** ke liye hai — koi naya content generate nahi karna, sirf update karna jahan pehle se kuch upload/paste ho chuka hai.

---

## Phase A — Verify the Fixes (kar sakta hoon, ya aap khud bhi kar sakte ho)

| # | Task | How |
|---|---|---|
| A.1 | `SKILL.md` v1.1 ko poora padho | Confirm: Step 10 mein "Next Review Date" + "Rollout Review Checkpoint" hai, 10B mein cadence-reuse hai, 10C sahi checkpoint reference karta hai |
| A.2 | `ChatGPT-Custom-GPT-Instructions.md` v1.1 ko poora padho | Same 3 cheezein confirm karo, wording SKILL.md se match honi chahiye (verbatim nahi, but meaning same) |
| A.3 | `Research_OS_Final.md` Part B ko poora padho | Confirm: YAML block v1.1, intake form mein Tracking Rollout field, operating rules mein 10A–10E bullet, Step 11 mein 10E-summary mention, Part C ab sirf snapshot hai (duplicate checklist nahi) |
| A.4 | Teeno files ek dusre ke saath cross-check karo | Step 10/10B/10C ka wording teeno jagah same *meaning* deta hai (exact words match hone zaroori nahi, platform-specific phrasing theek hai) |

**Output:** Confidence ki jo audit report mein "fixed" likha hai, wo actually files mein hai — koi claim-vs-reality gap nahi.

---

## Phase B — Re-Upload/Re-Paste to Live Platforms (agar pehle se koi setup ho chuka hai)

*Ye sirf tab zaroori hai agar aapne pehle se koi purani version (v1.0, ya bina-fix wali v1.1) kisi platform pe upload/paste kar di thi. Agar abhi tak kuch bhi live upload nahi hua, toh seedha original Implementation Plan ke Phase 1–3 follow karo — ye Phase B skip ho jayega.*

| # | Task | How |
|---|---|---|
| B.1 | Claude.ai mein purani skill hai to remove/replace karo | Settings → Skills → purani `research-os` skill delete/replace karo → naya `SKILL.md` (is audit ke baad wala) upload karo |
| B.2 | ChatGPT Custom GPT/Project ke Instructions ko replace karo | Configure tab → Instructions field ka pura content select-all-delete → naya `ChatGPT-Custom-GPT-Instructions.md` ka code-block paste karo → Save |
| B.3 | Perplexity Space ko touch mat karo | Koi change nahi — Perplexity file untouched hai, audit se related nahi |
| B.4 | Version note karo | Dono platforms pe (agar description field allow kare) "v1.1 (audit-reviewed)" jaisa kuch likh do, taaki future mein pata chale ye kaunsi version hai |

**Output:** Live setup ab fixed v1.1 use kar raha hai, purani buggy version kahin bhi active nahi.

---

## Phase C — Spot-Check the Fix in Practice (halka test, poora Phase 4 nahi)

*Ye poora end-to-end test nahi hai (wo abhi bhi manual + skipped hai) — sirf itna check karna hai ki naye Step 10/10A–10E fields sahi se kaam karte hain.*

| # | Task | Detail |
|---|---|---|
| C.1 | Kisi bhi chhoti research request se Step 10 tak chalao | Check karo ki KPI table mein "Next Review Date" column aur "Rollout Review Checkpoint" line dikh rahi hai |
| C.2 | "Tracking Rollout? Yes" bolke dekho | Check karo ki Steps 10A–10E trigger hoti hain aur 10C sahi checkpoint reference karta hai (na ki koi undefined "review date") |
| C.3 | "Tracking Rollout? No" bolke dekho | Check karo ki Step 10 ke baad seedha Step 11 chalta hai, 10A–10E skip ho jaate hain |

**Output:** Confirm ki fix sirf "kaagaz pe sahi" nahi hai, balki actual conversation mein bhi expected tareeke se behave karta hai.

---

## Dependency Order

```
Phase A (Verify)  →  Phase B (Re-upload, if needed)  →  Phase C (Spot-check)
```
Phase A hamesha pehle. Phase B sirf agar pehle se kuch live hai. Phase C dono ke baad, chhota sanity check.

---

*Companion file: `Research_OS_Audit_Fix_Progress_Tracker.md` — isi plan ko track karne ke liye.*
