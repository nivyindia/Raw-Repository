# ⚙️ Phase 7 — Research Processing SOP (How to Tag & Promote)

> 📌 **Phase:** 7 — Raw Research Processing | **Owner:** Claude + Founder | **Status:** 🟢 Active | **Created:** May 18, 2026
> 

---

## 🎯 Purpose

This SOP governs how raw content in the ChatGPT conversations DB and Raw Knowledge Vault gets reviewed, tagged, and promoted into structured pages across the workspace. Nothing is deleted. Everything either gets a home or gets explicitly tagged as Backlog / Not Applicable.

---

## 📋 The Two Raw Research Sources

| Source | Location | What It Contains |
| --- | --- | --- |
| ChatGPT conversations DB | Archive → ChatGPT Chats Manager | Auto-saved ChatGPT conversations via browser extension |
| Raw Knowledge Vault | Nivy OS Master Hub → Raw Knowledge Vault | Manually pasted raw content, drafts, research notes |

---

## 🔄 The Processing Pipeline

```
RAW ENTRY (untagged)
    ↓
REVIEW — Read the content. Identify: Brand, Content Type, Department, Priority
    ↓
TAG — Update Promotion Status → "Under Review"
    ↓
DECIDE:
    ├── Promotable → create structured page → set Promotion Status = "Promoted" → fill Promoted To URL
    ├── Not ready yet → set Promotion Status = "Backlog"
    └── Personal / irrelevant → set Promotion Status = "Not Applicable"
```

---

## 🏷️ Tagging Rules — ChatGPT Conversations DB

For every conversation entry, set these fields:

| Field | Options | Decision Rule |
| --- | --- | --- |
| Brand | Nivy Next / Advisory / Nexus / Jobs / Global / Growth / Artisan / Academy / Alliance / Care / All | Which brand is this conversation primarily about? |
| Content Type | SOP / Strategy / Knowledge / Framework / Research / Business Plan / Template / Idea / Competitor Intel / Personal | What is the primary type of content? |
| Department | Sales / Marketing / Operations / HR / Finance / Tech / Client Delivery / Partnerships / Research & Strategy / All | Which department would use this? |
| Priority | Core / Useful / Future / Ignore | Core = needs action now. Useful = good reference. Future = relevant later. Ignore = no business value. |
| Promotion Status | Raw → Under Review → Promoted / Backlog / Not Applicable | Update as you process each entry. |

---

## 📤 Promotion Rules — What Gets Promoted Where

| Content Type | Promote To |
| --- | --- |
| SOP | sop_database (create a new entry with full SOP page) |
| Knowledge / Research | knowledge_database (create structured knowledge page) |
| Strategy | Brand OS → Strategy section of the relevant brand |
| Business Plan | Brand OS → Section 1 (Vision / Business Plan) |
| Framework | Global Systems Hub → Framework Library |
| Template | templates_database |
| Competitor Intel | knowledge_database (Type = Competitor Intel) |
| Idea | Research Inbox → tag as Idea → leave for scheduled review |
| Personal / Non-Business | Tag as Not Applicable, Archive checkbox = checked |

---

## 📦 Tagging Rules — Raw Knowledge Vault

For every item in the Raw Knowledge Vault, add a tag header at the top:

```
[Brand: Nivy Next] [Type: Research] [Dept: Marketing] [Date: Apr 2026] [Status: Under Review]
```

Then process using the same Decide step above.

---

## ✅ Done Looks Like

- Every ChatGPT conversations DB entry has Brand + Content Type + Department + Priority + Promotion Status filled
- No entry has Promotion Status = blank
- Every Raw Knowledge Vault item has a tag header
- Promoted items have a link in "Promoted To"
- Non-applicable items have Archive = checked
- Zero accumulation without a status