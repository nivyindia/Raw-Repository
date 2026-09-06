# Research OS — Phase B Rollout + File Update Map

## Part 1 — Phase B Status

`Research_OS_Audit_Fix_Implementation_Plan.md` ka **Phase B (Re-Upload/Re-Paste to Live Platforms)** — 4 tasks the, unka status:

| # | Task | Status | Detail |
|---|---|---|---|
| B.1 | Claude Skill replace (agar purani live thi) | ⬜ **Manual — pending** | Ye sirf Claude.ai ke Settings UI mein ho sakta hai, main directly nahi kar sakta. Neeche exact path diya hai. |
| B.2 | ChatGPT Instructions replace (agar purani live thi) | ⬜ **Manual — pending** | Same reason — ChatGPT ke apne UI mein karna hoga. Exact path neeche hai. |
| B.3 | Perplexity untouched confirm | ✅ **Done** | Confirmed — `Perplexity-Space-Instructions.md` byte-for-byte same hai jo pehle thi. Koi action zaroori nahi. |
| B.4 | Version note add | ✅ **Draft ready** | Maine ready-to-paste version note bana diya hai (neeche) — bas copy-paste karna hai jahan platform allow kare. |

**Phase B Status: 🟡 Jitna file-level/prep ho sakta tha, ho chuka hai (B.3 done, B.4 drafted). B.1/B.2 aapko khud platform UI mein karne hain — wo sach mein sirf wahi kar sakta hai jiske paas account access hai.**

---

## Part 2 — Ready-to-Paste Version Note (for B.4)

Jahan bhi platform "description" ya "notes" field allow kare (GPT description, Skill description-append, Space description), ye chhota note paste kar sakte ho:

```
Research OS v1.1 (audit-reviewed) — 12-step workflow + optional post-implementation
audit & revision loop (Steps 10A–10E). Last verified: Aug 25, 2026.
```

*(Ye sirf ek human-readable note hai, taaki future mein pata chale ye kaunsi version hai — koi functional field nahi, isliye zaroori nahi lekin useful hai agar platform jagah de.)*

---

## Part 3 — File Update Map (exact path + kahan)

| # | File Name | Local Path | Kahan Update Karni Hai | Action |
|---|---|---|---|---|
| 1 | `SKILL.md` | `/mnt/user-data/outputs/SKILL.md` | **Claude.ai** → (profile icon) → Settings → Capabilities/Skills → apni "research-os" skill dhundo | Agar purani version pehle se upload hai: usko **remove/delete** karo (ya "Edit"/"Replace" option agar mile), phir "Upload Skill" se ye naya `SKILL.md` upload karo. Pehli baar kar rahe ho to seedha "Upload Skill" → is file ko select karo. |
| 2 | `ChatGPT-Custom-GPT-Instructions.md` | `/mnt/user-data/outputs/ChatGPT-Custom-GPT-Instructions.md` | **ChatGPT** → "Explore GPTs" → apna "Research OS" GPT kholo → "Edit"/"Configure" tab → **"Instructions"** box *(ya: Projects → "Research OS" → Project Settings → "Custom instructions")* | Box ka pura purana text select-all → delete → is file ke andar ` ``` ` code-block ke beech wala **pura content** copy-paste karo (bahar ka heading/note mat le jaana) → "Update"/"Save" dabao. |
| 3 | `Perplexity-Space-Instructions.md` | `/mnt/user-data/outputs/Perplexity-Space-Instructions.md` | **Perplexity** → "Spaces" → "Research OS" Space → "Custom Instructions" | **Kuch mat karo** — ye already sahi hai, touch mat karo (B.3 confirmed). |

---

## Ek baar hone ke baad

Jab B.1 aur B.2 kar lo, `Research_OS_Audit_Fix_Progress_Tracker.md` mein Phase B ke rows (⬜) ko ✅ mark kar dena — ya mujhe bata dena, main update kar dunga.

Uske baad sirf **Phase C (halka spot-check)** bacha rahega — poora Phase 4 test nahi, sirf ye dekhna ki "Next Review Date" / "Rollout Review Checkpoint" / "Tracking Rollout? Yes-No" branching live setup mein bhi sahi kaam karti hai.
