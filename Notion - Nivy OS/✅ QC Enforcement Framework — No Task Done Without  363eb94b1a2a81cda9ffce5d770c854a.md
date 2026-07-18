# ✅ QC Enforcement Framework — No Task Done Without Approval

> 📌 **Phase 9** | **Tool:** Notion | **Status:** ✅ Framework Built | **Updated:** May 18, 2026
> 

> QC enforcement ensures no task output leaves the system without review. This page defines the full QC chain.
> 

---

# 🛡️ THE QC RULE

> **No task can be considered Done until QC Status = Approved.**
> 

This is enforced by:

1. Notion automation (Task Status = Done → QC Status = Pending) — see Native Automations page
2. Manager filter view showing all Pending QC items
3. This policy page: every team member knows the rule

---

# 🔄 The QC Flow

```
VA / Team Member completes task
    ↓
Sets Task Status = Done
    ↓
Notion automation fires → QC Status = Pending
    ↓
Manager sees task in QC Queue (filtered view in tasks_database)
    ↓
Manager reviews Output Link (the deliverable)
    ↓
    ├── Output meets standard → QC Status = Approved → Task is truly done
    └── Output needs improvement → QC Status = Rework → Task Status reverts to In Progress
```

---

# 📊 QC Status Options

| Status | Meaning | Who Sets It |
| --- | --- | --- |
| Pending | Task marked Done, awaiting manager review | Set automatically by Notion automation |
| Approved | Output reviewed and meets standard | Manager |
| Rework | Output needs improvement — task goes back to VA | Manager |

---

# 👁️ The Manager QC Queue

**How to set up the QC Queue view in tasks_database:**

1. Open `tasks_database`
2. Create a new filtered view: name it “✅ QC Queue”
3. Filter 1: QC Status = Pending
4. Filter 2: Brand = [your brand] (for brand-specific managers)
5. Sort: Created date → oldest first (review in order)
6. Display properties: Task Name, Owner, Brand, Department, Output Link, Deadline

**This view is the manager’s Monday opening page.**

---

# 📍 QC Standards by Department

| Department | QC Standard | What Manager Checks |
| --- | --- | --- |
| Sales (Outreach) | Message accuracy, personalisation, correct contact | Did they follow the outreach SOP? Was the contact logged? |
| Client Delivery | On-time, complete, matches brief | Does it match the client brief? Any errors? |
| Marketing (Content) | Brand voice, accuracy, formatting | Is it on-brand? Factually correct? |
| Operations | Process followed, documentation complete | Is the handover documented? Task logged? |
| HR | Compliance with policy, documentation | Is the paperwork complete? Correct? |
| Finance | Accuracy, correct codes/accounts | Numbers correct? Approvals obtained? |

---

# ⚠️ Escalation Policy

| Scenario | Action |
| --- | --- |
| Task in QC Pending for >3 days with no action | Manager gets reminder notification |
| Same task gets Rework 3+ times | Escalate to Founder + create Feedback entry (see Feedback DB) |
| QC Approved but client reports error | Log in Feedback DB as “Escaped Defect” + review QC standard |

---

# 📊 QC KPI (Track Monthly)

| Metric | Target | Where to Track |
| --- | --- | --- |
| First-pass approval rate | >85% | KPI DB (Department: Operations) |
| Average QC turnaround | <24 hours | reports_database (monthly) |
| Rework rate | <15% | KPI DB |
| Escaped defects | 0 | Feedback / Learnings DB |