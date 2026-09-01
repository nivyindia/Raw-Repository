# Company OS — Priority Ranking (Improved)

**Base:** `Company_OS_Full_Audit.md` ke Section 4 (New Findings) + Section 2 (Re-verified Open Issues) se derive kiya gaya. Har item ko **Severity, Effort, Dependency aur Impact** ke basis par re-ranked kiya gaya hai, taaki priority sirf "gut feeling" na ho, balki justify ho.

**Ranking logic:** Pehle wo items jo (a) kisi aur cheez ko **block** kar rahe hain, (b) **data loss / trust-breaking** risk hain, unhe upar rakha gaya. Jo sirf documentation-only ya cosmetic hain, unhe neeche rakha gaya — chahe wo "quick fix" hi kyun na ho.

---

## Priority Table

| Rank | Item | Severity | Effort | Blocks / Depends On | Why this rank |
|---|---|---|---|---|---|
| **P1** | `02_PROJECTS/` folder + GitHub Project board actually set up karo | 🔴 Critical | Medium | **Blocks:** Task management, dashboard "task count", TickTick sync (P6) — sab isi foundation par tike hain | Sabse upar kyunki ye ek **structural blocker** hai — jab tak ye nahi banta, baaki task-automation features (auto-add/auto-move, dashboard task metrics) bhi kaam nahi kar sakte, chahe unke workflows likhe hue kyun na ho |
| **P2** | `cleanup-after-merge.yml` likho (ya README ka wording fix karo) | 🔴 Critical | Low | Independent | README ek **false promise** kar raha hai ("auto-delete hoga") jo reality mein hota nahi. Ye trust/data-hygiene issue hai — `dump/` folder silently accumulate hota rahega. Fix cheap hai (naya workflow ya sirf doc-wording), isliye upar |
| **P3** | Duplicate `inbox-classify.yml` clean karo (remove ya "deprecated" mark karo) | 🟠 High | Low | Independent, lekin P2 ke saath related (dono Research-Inbox automation confusion) | Do overlapping scaffolds confusion create karte hain — koi bhi contributor galat file edit kar sakta hai. Fix trivial hai (delete ya comment add), lekin risk maintenance-level hai isliye P2 se thoda neeche |
| **P4** | Dashboard generator bana do | 🟠 High | Medium–High | **Depends on:** health-report.yml ka data already Issues mein aa raha hai (ye ready hai) | Visibility gap — abhi data scattered hai (GitHub Issues mein) but koi consolidated view nahi. Effort thoda zyada hai (naya script/file banana padega) isliye P1–P3 ke baad |
| **P5** | Automation Map mein missing `inbox-merge-confirmation.yml` entry add karo | 🟡 Medium | Very Low | Independent | Pure documentation gap — functionally kuch broken nahi hai, sirf map incomplete hai. Quick fix hai lekin low-severity isliye P5 |
| **P6** | TickTick / external reminder sync layer add karo | 🟡 Medium | High | **Depends on:** P1 (Project board setup) — bina board ke sync karne ke liye source data hi nahi hoga | Naya capability hai (existing gap nahi), aur P1 pe dependent hai isliye pehle nahi ho sakta chahe priority list mein pehle likha gaya ho |
| **P7** | Brand codes fill karo (Brands.md placeholders) | 🟢 Low | Low | Independent | Data-completeness item, koi automation ya trust issue nahi. Content-fill kaam hai jo kabhi bhi ho sakta hai |
| **P7** | Classifier skill JSON re-check karo (12-type match) | 🟢 Low | Low | **Depends on:** classifier zip re-upload (abhi file hi available nahi) | Blocked by missing input — jab tak zip re-upload nahi hota, ye verify hi nahi ho sakta. Isliye same tier as P7 rakha, action item hai "re-upload karo" |

---

## Kyun purani ranking se different hai

Original audit mein order tha: PROJECTS → cleanup-after-merge → inbox-classify → dashboard → automation-map-entry → TickTick → brands/classifier.

Is improved version mein sequence **same rehti hai top 5 ke liye** (wo already sahi tha), lekin do cheezein add ki gayi hain:
1. Har item ko **reason + dependency** diya gaya hai, taaki "kyun ye pehle" clear ho, sirf list na ho.
2. **P6 (TickTick)** ko explicitly P1 par dependent mark kiya gaya — pehle ye sirf "naya capability" tha, ab clear hai ki ye P1 ke bina start hi nahi ho sakta.
3. **P7 tier** mein do items ek saath rakhe gaye kyunki dono low-severity + low-effort hain, aur classifier item ek external blocker (re-upload) pe depend karta hai.

---

## Merge Mapping — Kisko Kis File Mein Daalna Hai

| Priority Item | Target File (repo mein) | Kya likhna hai |
|---|---|---|
| P1 — `02_PROJECTS/` + Project board | `05-Task-Management-Design.md` (jahan Task Storage design hai) | Ek "Implementation Status" section add karo: "Design complete, board not yet created — action item" |
| P1 — same | `Company-OS/02_PROJECTS/README.md` (nayi file banao, abhi missing hai) | Board link, naming convention, kis tarah task-files yahan aayenge |
| P2 — `cleanup-after-merge.yml` | `Company-OS/.github/workflows/cleanup-after-merge.yml` (nayi file, agar workflow likhna hai) | Actual GitHub Action YAML jo PR merge trigger par source file `dump/` se delete kare |
| P2 — same (agar sirf doc fix) | `Research-Inbox/README.md` (line ~37) | Wording change: "cleanup-after-merge.yml" reference hatao, manual cleanup step likho |
| P3 — duplicate `inbox-classify.yml` | `Company-OS/.github/workflows/inbox-classify.yml` | Ya delete karo, ya top par comment: `# DEPRECATED — superseded by Research-Inbox/classify-and-pr.yml` |
| P3 — cross-reference | `10-GitHub-Actions-Automation-Map.md` | Note add karo ki classify logic ab sirf Research-Inbox repo mein hai, Company-OS mein nahi |
| P4 — Dashboard | Nayi file: `Company-OS/dashboard.md` (ya `.github/workflows/generate-dashboard.yml`) | health-report.yml ka Issues data consolidate karke render karne wala script/file |
| P4 — cross-reference | `07-*.md` (jo Doc 07 §9 dashboard concept describe karta hai) | "Implementation" link add karo jab dashboard file ban jaye |
| P5 — missing workflow entry | `10-GitHub-Actions-Automation-Map.md`, Section 5 (Migration) | Row add karo: "Post-PR-merge confirmation comment → `inbox-merge-confirmation.yml`" |
| P6 — TickTick sync | Nayi file: `Company-OS/.github/workflows/ticktick-sync.yml` | Sync script jo Project board task se TickTick API ko push kare |
| P6 — cross-reference | `10-GitHub-Actions-Automation-Map.md` | Naya section: "External Reminder Integration (TickTick)" |
| P7 — Brand codes | `01_AREAS/.../Brands.md` (Company Master Standards ke andar) | Nivy Next, Nivy Academy, Nivy Alliance etc. ke actual codes fill karo |
| P7 — Classifier JSON | `company-os-classifier-skill.zip` ke andar JSON file (re-upload ke baad milega) | 12-type list match verify karo registry (`02-Document-Type-Code-Registry.md`) ke against |

---

*Is file ko `Company_OS_Full_Audit.md` ke Section 5 ki jagah use karo — waha bas ek line reference chhod do: "Priority Ranking ab `Company_OS_Priority_Ranking.md` mein detailed hai."*
