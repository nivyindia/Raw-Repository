# Research OS — Phase C Spot-Check + File Update Map

## Part 1 — Phase C Status

`Research_OS_Audit_Fix_Implementation_Plan.md` ka **Phase C (Spot-Check in Practice)** — 3 tasks the:

| # | Task | Status | Detail |
|---|---|---|---|
| C.1 | Step 10 tak chalake KPI table/checkpoint fields dekhna | ⬜ **Manual — pending** | Ye actual live chat mein Claude/ChatGPT ke saath karna hota hai — main sirf test prompt de sakta hoon, chala nahi sakta (ye aapke Claude Skill / GPT ke andar hoga, is conversation mein nahi). |
| C.2 | "Tracking Rollout? Yes" test | ⬜ **Manual — pending** | Same reason. |
| C.3 | "Tracking Rollout? No" test | ⬜ **Manual — pending** | Same reason. |

**Phase C Status: ⬜ Poora phase manual hai — koi file-level kaam nahi bacha, is baar sirf "ready-to-use test material" bana sakta hoon taaki aapko khud kuch likhna na pade, seedha copy-paste karke test kar sako.**

*(Note: pichhle Phase A/B se ye thoda alag hai — A aur B mein kuch file-fixes/prep possible tha jo maine kar diya. Phase C apni nature se hi 100% "live conversation mein test karo" hai, isko file bana ke complete nahi kiya ja sakta — lekin main test-script ready kar sakta hoon.)*

---

## Part 2 — Ready-to-Use Test Prompts

Neeche 3 chhote test cases hain — seedha copy-paste karke apni live Claude Skill ya ChatGPT GPT mein try kar sakte ho.

### Test C.1 — Basic run tak Step 10
```
I want to research pricing strategy for our SaaS product for the Sales department.
Research Depth: Quick. Tracking Rollout?: No.
Run steps 0 through 10 end-to-end and show me the Step 10 output.
```
**Check karo:** Step 10 ke KPI table mein `Measurement Frequency` ke saath ek `Next Review Date` column bhi hai, aur ek alag se `Rollout Review Checkpoint` line/date bhi diya gaya hai.

### Test C.2 — Tracking Rollout = Yes (audit loop trigger)
```
Same as above, but Tracking Rollout?: Yes.
After Step 10, continue into the v1.1 Audit & Revision Loop (Steps 10A–10E) and show me Step 10A and 10C.
```
**Check karo:**
- Step 10A ek proper audit table deta hai (Implementation Item | Traced To | Audit Issue | Severity | Fix Required)
- Step 10C `Rollout Review Checkpoint` ya `Next Review Date` ko explicitly reference karta hai — **nahi** ek undefined "review date set in Step 10" (ye wahi bug tha jo fix kiya gaya tha)

### Test C.3 — Tracking Rollout = No (audit loop skip)
```
Same intake as Test C.1 (Tracking Rollout?: No).
After Step 10, go straight to Step 11 — confirm you're skipping Steps 10A–10E and tell me why.
```
**Check karo:** Assistant khud confirm kare ki 10A–10E skip ho rahe hain kyunki "Tracking Rollout? No" tha, aur seedha Final Report (Step 11) pe jaye.

---

## Part 3 — File Reference Map (kaunsi file kis test se related hai)

| File | Local Path | Is Phase C test se relation |
|---|---|---|
| `SKILL.md` | `/mnt/user-data/outputs/SKILL.md` | Agar Claude Skill mein test kar rahe ho, ye file hi wo logic define karti hai jo Test C.1–C.3 mein check ho raha hai. Koi naya paste nahi — bas confirm karo ye already live upload hai (Phase B.1). |
| `ChatGPT-Custom-GPT-Instructions.md` | `/mnt/user-data/outputs/ChatGPT-Custom-GPT-Instructions.md` | Agar ChatGPT GPT mein test kar rahe ho, same tarah — confirm ye already live paste hai (Phase B.2). |
| `Research_OS_Audit_Fix_Progress_Tracker.md` | `/mnt/user-data/outputs/Research_OS_Audit_Fix_Progress_Tracker.md` | Test results yahan record karo — C.1/C.2/C.3 rows ko ✅/❌ mark karo, aur agar koi test fail ho to "Notes" column mein likh do kya galat mila. |

**Koi naya platform-upload nahi hai is phase mein** — ye purely verification hai ki jo files pehle se upload/paste ho chuki hain (Phase B), wo live conversation mein bhi sahi behave kar rahi hain.

---

## Agar koi test fail ho jaye

Agar Test C.1/C.2/C.3 mein se koi expected behavior nahi deta (e.g. Rollout Review Checkpoint nahi dikh raha, ya 10A–10E trigger nahi ho raha), to mujhe wo exact output paste kar dena — main dekh ke fix kar dunga ki kahin koi naya gap to nahi reh gaya.

**Sab 3 test pass ho jayein → poora Research OS v1.1 (audit-reviewed) production-ready hai, koi manual step bacha nahi.**
