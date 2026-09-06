# Research OS — Phase A Verification + File Update Map

## Part 1 — Phase A Fix Confirmation

`Research_OS_Audit_Fix_Implementation_Plan.md` ka **Phase A (Verify the Fixes)** ab formally close kiya ja raha hai — sabhi 4 tasks re-checked, line-by-line, teeno files ke against:

| # | Task | Status | Verified Kya |
|---|---|---|---|
| A.1 | `SKILL.md` v1.1 verify | ✅ Fixed & Confirmed | Step 10 mein `Next Review Date` column + `Rollout Review Checkpoint` line hai; Step 10B ab Step 10 ki Measurement Frequency reuse karta hai (alag cadence nahi puchta); Step 10C `Rollout Review Checkpoint` / `Next Review Date` ko hi reference karta hai — koi undefined field nahi. |
| A.2 | ChatGPT Instructions v1.1 verify | ✅ Fixed & Confirmed | Same teeno fields — Next Review Date, Rollout Review Checkpoint, cadence-reuse — Instructions code-block ke andar present hain, SKILL.md ke meaning se match. |
| A.3 | `Research_OS_Final.md` Part B verify | ✅ Fixed & Confirmed | YAML metadata block ab `v1.1` bolta hai; Intake Form mein `Tracking Rollout?` field hai; Operating Rules mein "Steps 10A–10E optional" bullet hai; Step 11 mein Step 10E revision-summary ka mention hai; Part C ab duplicate checklist nahi — sirf snapshot hai jo standalone tracker ko point karta hai. |
| A.4 | Cross-file consistency check | ✅ Fixed & Confirmed | Teeno files (`SKILL.md`, ChatGPT Instructions, `Research_OS_Final.md` Part B) ka Step 10/10A–10E wording ek dusre se meaning mein match karta hai — koi file kisi doosri se drift nahi kar rahi. |

**Phase A Status: ✅ Done — koi open issue nahi bacha.**

---

## Part 2 — File Update Map (kaunsi file kahan update karni hai)

Neeche har deliverable file ka **local path** (jo aapke paas download ho chuki hai) aur **kahan use/update karni hai** (platform + exact location) diya gaya hai.

| # | File Name | Local Path | Kahan Update Karni Hai | Kya Action |
|---|---|---|---|---|
| 1 | `SKILL.md` | `/mnt/user-data/outputs/SKILL.md` | **Claude.ai** → Settings → Capabilities/Skills → "Skills" section | Agar purani `research-os` skill pehle se upload hai → usko **delete/replace** karo, phir "Upload Skill" / "Create Skill" se ye naya `SKILL.md` upload karo. Agar pehli baar upload kar rahe ho, seedha upload karo. |
| 2 | `ChatGPT-Custom-GPT-Instructions.md` | `/mnt/user-data/outputs/ChatGPT-Custom-GPT-Instructions.md` | **ChatGPT** → "Explore GPTs" → apna "Research OS" GPT kholo → "Configure" tab → **"Instructions"** field *(Ya: Projects → "Research OS" project → Project Settings → "Custom instructions")* | Field ka pura purana content select-all-delete karo, phir is file ke andar diye gaye ` ``` ` code-block ka **pura content** copy-paste karo (sirf ` ``` ` markers ke andar wala hissa, bahar ka heading/note mat paste karo) → Save/Update. |
| 3 | `Perplexity-Space-Instructions.md` | `/mnt/user-data/outputs/Perplexity-Space-Instructions.md` | **Perplexity** → "Spaces" → "Research OS" Space → **"Custom Instructions"** field | **Koi change nahi.** Ye file untouched hai — agar pehle se paste ki hui hai, wahi rehne do. Agar pehli baar kar rahe ho, is file ka block paste karo (jaisa original Setup Plan mein tha). |
| 4 | `Research_OS_Final.md` | `/mnt/user-data/outputs/Research_OS_Final.md` | Kisi bhi platform pe **paste nahi karni** — ye sirf aapka apna reference/master doc hai | Apne records ke liye rakho (Google Drive / Notion / local folder), taaki future mein poora system ek jagah dikhe. Platform setup isi se copy nahi hota — wo upar wali files 1–3 se hota hai. |
| 5 | `Research_OS_Audit_Report.md` | `/mnt/user-data/outputs/Research_OS_Audit_Report.md` | Kahin paste nahi karni | Reference/record ke liye — kya-kya galat tha aur kya fix hua, uski history. |
| 6 | `Research_OS_Audit_Fix_Implementation_Plan.md` | `/mnt/user-data/outputs/Research_OS_Audit_Fix_Implementation_Plan.md` | Kahin paste nahi karni | Reference — Phase A/B/C ka roadmap. |
| 7 | `Research_OS_Audit_Fix_Progress_Tracker.md` | `/mnt/user-data/outputs/Research_OS_Audit_Fix_Progress_Tracker.md` | Kahin paste nahi karni | **Aapko khud is file ko edit karna hai** jaise-jaise Phase B/C manual steps complete karte ho (⬜ ko ✅ mein badalna). |
| 8 | `Research_OS_Setup_Progress_Tracker.md` | `/mnt/user-data/outputs/Research_OS_Setup_Progress_Tracker.md` | Kahin paste nahi karni | Original Phase 1–5 setup ka **single source of truth** tracker — isi ko update karte raho jab bhi koi manual task complete ho. |

---

### Quick Summary — sirf 3 files actually kahin "paste/upload" hoti hain:

1. **`SKILL.md`** → Claude.ai Skills settings
2. **`ChatGPT-Custom-GPT-Instructions.md`** (sirf code-block wala hissa) → ChatGPT Custom GPT/Project Instructions field
3. **`Perplexity-Space-Instructions.md`** → Perplexity Space Custom Instructions field

Baaki sab files (`Research_OS_Final.md`, Audit Report, dono Implementation Plans, dono Progress Trackers) sirf **aapke reference ke liye** hain — koi platform inhe accept nahi karta, ye sab is poore system ko samajhne/track karne ke documents hain.
