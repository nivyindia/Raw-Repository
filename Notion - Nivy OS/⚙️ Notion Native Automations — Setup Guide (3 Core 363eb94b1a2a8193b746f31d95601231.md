# ⚙️ Notion Native Automations — Setup Guide (3 Core Triggers)

> 📌 **Phase 9** | **Tool:** Notion Native Automations | **Status:** 📋 Spec Ready — Needs Manual Setup | **Updated:** May 18, 2026
> 

> ℹ️ **How Notion Automations Work**
> 

> Go to any database → click the ⚡ lightning bolt icon at top right → “Add automation” → set Trigger → set Action. These run automatically inside Notion with no external tool.
> 

---

# ⚡ AUTOMATION 1 — Task Done → QC Status = Pending

**Purpose:** Ensure no task is considered complete without passing QC. Forces quality control on every output.

**Database:** `tasks_database`

**Setup steps:**

1. Open `tasks_database` → click ⚡ → Add automation
2. **Trigger:** Property changed → **Status** changes to ‘Done’
3. **Action:** Edit property → **QC Status** → set to ‘Pending’
4. Name it: *“Task Done → Queue for QC”*
5. Enable and test with a dummy task

**Expected behaviour:**

- VA marks task Done → QC Status automatically flips to Pending
- Manager sees Pending in their QC filter view
- Manager reviews output, sets QC Status to Approved or Rework
- Only Approved tasks count as truly complete

**Why this matters:** Without this, “Done” means nothing. With it, Done = reviewed and approved.

---

# ⚡ AUTOMATION 2 — SOP Needs Review → Notify Owner

**Purpose:** Ensure SOPs don’t go stale. Triggers when a manager flags an SOP for review.

**Database:** `sop_database`

**Setup steps:**

1. Open `sop_database` → click ⚡ → Add automation
2. **Trigger:** Property changed → **Status** changes to ‘Needs Review’
3. **Action:** Send notification to → **Owner** property (the person assigned to that SOP)
4. **Notification message:** *“Action needed: [SOP Name] has been flagged for review. Please update within 7 days.”*
5. Name it: *“SOP Review Alert”*

**Expected behaviour:**

- Any team member (or scheduled review cycle) sets SOP Status to Needs Review
- Owner gets a Notion notification immediately
- Owner reviews, updates content, sets Status back to Approved
- Last Updated date updates automatically (Notion auto-tracks this)

---

# ⚡ AUTOMATION 3 — KPI Alert Checked → Notify Manager

**Purpose:** Instant alert when a KPI drops below its target threshold.

**Database:** `KPI DB`

**Setup steps:**

1. Open `KPI DB` → click ⚡ → Add automation
2. **Trigger:** Property changed → **Alert** checkbox changes to checked (true)
3. **Action:** Send notification to → **Owner** property
4. **Notification message:** *“KPI Alert: [KPI Name] is below threshold. Actual: [Actual]. Target: [Target]. Review needed.”*
5. Name it: *“KPI Below Threshold Alert”*

**How the Alert field gets checked:**

- During weekly KPI update, if Actual < Target → check the Alert checkbox manually
- Or: once [Make.com](http://Make.com) is live, it can check this field automatically based on formula comparison

**Escalation rule:** If Alert stays checked for 2 consecutive weeks → escalate to Founder dashboard.

---

# 🧪 Testing All 3 Automations

| Automation | Test Method | Pass Condition |
| --- | --- | --- |
| Task Done → QC Pending | Create test task → set Status = Done | QC Status flips to Pending within 10 seconds |
| SOP Needs Review | Set any SOP Status = Needs Review | Owner receives Notion notification |
| KPI Alert | Check Alert box on any KPI entry | Owner receives Notion notification |

**Once all 3 pass → mark Automation 1-3 as ✅ Live in the Phase 9 Master Hub.**