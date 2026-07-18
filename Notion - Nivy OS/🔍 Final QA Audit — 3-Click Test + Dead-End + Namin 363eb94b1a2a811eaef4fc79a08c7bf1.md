# 🔍 Final QA Audit — 3-Click Test + Dead-End + Naming + Metadata

> 📌 **Phase 9** | **Type:** 3-Click Audit + Dead-End Audit + Naming Audit | **Updated:** May 18, 2026
> 

> Run this audit after Phase 9 is fully live. The workspace passes when every check is ✅.
> 

---

# 🎯 PART 1 — The 3-Click Test

**Rule:** Starting from Nivy HQ (the front door), any major content type must be reachable in ≤3 clicks.

## Test Checklist

| Content Type | Click 1 | Click 2 | Click 3 | ✅ Pass? |
| --- | --- | --- | --- | --- |
| A Nivy Next SOP | Global Dashboard | Nivy Next OS | SOP Index | ❓ |
| A Nivy Advisory SOP | Global Dashboard | Nivy Advisory OS | SOP Index | ❓ |
| A knowledge entry (Nivy Next) | Global Dashboard | Nivy Next OS | Knowledge Index | ❓ |
| A task assigned to a VA | Global Dashboard | Nivy Next OS | Role Dashboard → tasks link | ❓ |
| A KPI for Nivy Next | Global Dashboard | Nivy Next OS | KPI view or Manager Dashboard | ❓ |
| A cross-brand SOP | Global Dashboard | Global Systems | Global Systems Hub | ❓ |
| A ChatGPT conversation | Nivy HQ | Research Lab | ChatGPT conversations DB | ❓ |
| A template | Global Dashboard | Global Systems | Global Templates Library | ❓ |
| Company Roadmap | Nivy HQ | Company Master Index | Company Roadmap link | ❓ |
| A client record | Global Dashboard | Nivy Next OS | clients_database view | ❓ |

**How to run this test:**

1. Open Nivy HQ in a fresh browser tab (no other pages open)
2. For each row above: click through and count clicks
3. If any item takes >3 clicks → flag it in the Dead-End section below
4. Fix: add a shortcut link to the relevant index page

---

# 🕴️ PART 2 — Dead-End Audit

**Rule:** Every page must have at least one forward link and one back-link.

## Pages Most Likely to Be Dead Ends

| Page Type | Check | Fix if Dead End |
| --- | --- | --- |
| Shell brand pages (Academy, Alliance, Care) | Does it link back to Brand OS index? | Add “Return to Brand OS” link |
| Raw Knowledge Vault sections | Do they link to processing SOP? | Add link to Research Processing SOP |
| Archive pages | Do they link to the active replacement? | Add “See live version:” link |
| Old planning docs | Do they link to Master Plan? | Add archive banner with link |
| Individual SOP pages | Do they link back to SOP Index? | Add footer: “← Back to SOP Index” |
| Individual knowledge pages | Do they link to Knowledge Index? | Add footer link |

## Dead Ends Found (Fill During Audit)

| Page | Issue | Fix Applied | Date |
| --- | --- | --- | --- |
| *(fill during audit)* |  |  |  |

---

# 🏷️ PART 3 — Naming Audit

**Rule:** Every page follows the Nivy naming convention. No ALL CAPS, no double emojis, no underscores, no vague names.

## Naming Convention Reminder

| Type | Format | Example |
| --- | --- | --- |
| SOP | `SOP-[BRAND CODE]-[DEPT]-[NUMBER] — [Name]` | `SOP-NN-SALES-001 — Cold Email Outreach` |
| Knowledge Entry | `[Topic] — [Brand]` | `ICP — Nivy Next` |
| Template | `TEMPLATE – [Brand] – [Use Case] – [Name]` | `TEMPLATE – Nivy Next – Cold Email – Initial` |
| DB View | `[Emoji] [Brand] [Filter Description]` | `🟢 Nivy Next — Active Tasks` |
| Division Home | `[Emoji] [Brand] OS — [Descriptor]` | `🚀 Nivy Next OS — Brand Operating System` |

## Naming Violations Checklist

- [ ]  Search workspace for pages with ALL CAPS titles (use search: “NIVY”)
- [ ]  Search for pages with double emojis (e.g. “📦📦”)
- [ ]  Search for pages with underscores in titles
- [ ]  Search for vague page names (e.g. “Untitled”, “New Page”, “Test”, “Draft”)
- [ ]  Verify all SOP pages follow SOP-[CODE] format

---

# 📈 PART 4 — Metadata Completeness Check

**Rule:** Every database entry must have key fields filled. Blank fields = unfindable content.

| Database | Required Fields | Check |
| --- | --- | --- |
| tasks_database | Task Name, Brand, Department, Owner, Status, Priority | ❓ |
| sop_database | SOP Name, Brand, Department, Status, Owner | ❓ |
| knowledge_database | Topic Name, Brand, Department, Status, Type | ❓ |
| clients_database | Client Name, Brand, Status | ❓ |
| KPI DB | KPI Name, Brand, Department, Target, Period, Owner | ❓ |
| ChatGPT conversations DB | Title, Brand, Content Type, Promotion Status | ❓ |

**How to run:** Open each database → filter for blank Brand field → fill in. Repeat for each required field.

---

# ✅ Audit Completion Criteria

The workspace passes the Phase 9 final QA when:

- [ ]  All 10 rows of the 3-click test pass
- [ ]  Zero confirmed dead ends (or all documented and fixed)
- [ ]  Zero naming violations remain
- [ ]  All 6 databases have no blank required fields
- [ ]  All 3 Notion automations tested and live
- [ ]  All 5 [Make.com](http://Make.com) scenarios built and live

**When all boxes are checked → Nivy Empires workspace is complete. 🎉**