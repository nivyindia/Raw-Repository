# F0.1–F0.3 — Kya Replace Karna Hai (Repo Hygiene)

## F0.1 + F0.2 — Ek hi canonical copy (`growth-engine-automation/`)

Yeh folder — `growth-engine-automation/` (14 modules, phase-1 + phase-2) — **canonical/fixed** version hai. Isse apne zip ke andar dono jagah drop-in replace karo:

- `Growth Engline-n8n-workflow/growth-engine-automation/...` → yahan overwrite karo
- `n8n - growth-engine-individual workflows/growth-engine-automation/...` → yahan bhi overwrite karo (yehi wala tree stale tha — `REPLACE_WITH_..._WORKFLOW_ID` placeholders aur missing 2.6→2.7 node ke saath)

Ab dono jagah same, sahi content hoga — koi confusion nahi rahega ki kaunsi copy sahi hai.

**Note:** `1.1-content-social-factory/workflow.json` is baar ke saath thoda extra improved hai — F0 ke sath F1 (error handler linked) + F2 (HTTP retry) bhi already laga diya hai isme, kyunki wo pehle hi ban chuka tha. Baaki 13 modules abhi sirf F0-level (canonical, correct wiring) hain — unka F1/F2 patch agli baari milega jab tum bologe.

## F0.3 — Phase 3 ke 13 "spec" files ab clearly marked hain

`phase-3-specs-not-yet-built/` folder — 13 files, sabke naam ke end me `-SPEC` laga hai:

```
3.0.3-SPEC.json
3.0.4-SPEC.json
3.0.5-SPEC.json
3.0.6-SPEC.json
3.1.1-SPEC.json
3.1.2-LinkedIn-hiring-posts-scraper-SPEC.json
3.1.3-Digital-Footprints-Sub-workflow-Wrap-SPEC.json
3.1.4-Lead-Generation-Agent-SPEC.json
3.1.5-Master-Orchestrator-SPEC.json
3.2.1-Enrichment-Port-Airtable-Postgres-SPEC.json
3.3.1-Unified-Lead-Router-SPEC.json
4.1.1-Booking-Confirmation-SPEC.json
4.1.2-SMS-Reminders-SPEC.json
```

**Purana naam waali files** (`3.0.3.json`, `Booking Confirmation 4.1.1.json` waghera, jo `n8n - growth-engine-individual workflows/` ke andar flat pade the) — unko **delete kar do ya isi `phase-3-specs-not-yet-built/` folder se replace kar do.** Content same hai, sirf naam badla hai — jaan-boojhkar, taaki koi galti se import na kare aur socche ye asli workflow hai. Yeh files abhi bhi n8n me import nahi hongi (ye build-spec documents hain, importable workflow nahi) — pehle inhe real workflow banana padega (Phase 3+ build).

## Ek nazar me — kya kya badla

| Kya | Pehle | Ab |
|---|---|---|
| 14 Phase 1/2 modules | 2 alag-alag copies, disagree karte the | 1 canonical copy, dono jagah same |
| 1.1 module | Error handling/retry nahi tha | Error handler linked + HTTP retry laga hua |
| 13 Phase-3 spec files | Flat folder me, real workflow jaisa naam | Alag folder, `-SPEC` suffix, clearly not-importable |

Agla step bologe to F1+F2 (error handler + retry) baaki 13 Phase-1/2 modules pe bhi laga dunga — same pattern jo 1.1 pe kiya.
