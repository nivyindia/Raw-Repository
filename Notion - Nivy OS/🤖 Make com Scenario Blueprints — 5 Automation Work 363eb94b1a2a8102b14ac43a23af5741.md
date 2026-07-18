# 🤖 Make.com Scenario Blueprints — 5 Automation Workflows

> 📌 **Phase 9** | **Tool:** [Make.com](http://Make.com) | **Status:** 📋 Spec Ready — Build in [Make.com](http://Make.com) | **Updated:** May 18, 2026
> 

> ℹ️ **Getting Started with [Make.com](http://Make.com)**
> 

> 1. Create account at [make.com](http://make.com) (free plan supports 1,000 operations/month — enough to start)
> 

> 2. Connect Notion integration: Settings → Connections → Add → Notion → Authorise
> 

> 3. Connect Gmail / Google Workspace for email notifications
> 

> 4. Build each scenario below as a separate [Make.com](http://Make.com) “Scenario”
> 

---

# 🤖 SCENARIO 1 — Form Submission → Task Created in Notion

**Priority:** High — build first

**What it does:** When a prospect submits the website contact form, automatically create a task in `tasks_database` pre-filled with brand, department, and source.

**Trigger module:** Webhooks → Custom Webhook (or your form tool: Typeform / Google Forms / [Cal.com](http://Cal.com))

**Action modules:**

1. Notion → Create a Database Item in `tasks_database`
    - Task Name: `New Lead: [Form Name Field] — [Company]`
    - Brand: Nivy Next (or route by form field)
    - Department: Sales
    - Status: To Do
    - Priority: High
    - Owner: Assign to sales VA (fixed field)
    - Blocker: leave blank

**Blueprint logic:**

```
Webhook receives form data
    ↓
Filter: is this a real enquiry? (name + email both present)
    ↓
Notion: Create task in tasks_database
    ↓
Gmail: Send confirmation email to prospect
    ↓
Gmail: Send internal notification to sales team
```

**Test:** Submit your own contact form → verify task appears in tasks_database within 60 seconds.

---

# 🤖 SCENARIO 2 — New ChatGPT Chat → Added to Research Inbox

**Priority:** Medium

**What it does:** When a new conversation is saved to the ChatGPT conversations DB (via the browser extension), automatically create a linked entry in the Research Inbox with Promotion Status = Raw.

**Trigger module:** Notion → Watch Database Items → `ChatGPT conversations DB`

- Filter: only trigger for new items (Created at = today)

**Action modules:**

1. Notion → Create a Page in `Research Inbox` database (if one exists)
    - Title: `[AUTO] [Chat Title] — [Date]`
    - Source: ChatGPT conversations DB
    - Status: Raw
    - Processing Needed: Review + Tag
    - Link: URL to the ChatGPT conversation page

**Alternative if no Research Inbox DB:** Skip creation — just update the ChatGPT conversation entry:

- Promotion Status → Raw (if blank)
- This ensures every new entry starts tagged, never accumulates without status.

---

# 🤖 SCENARIO 3 — Weekly Department Review Task Creator

**Priority:** Medium

**What it does:** Every Monday at 9 AM IST, automatically creates a review task for each department head, ensuring weekly operational rhythm without manual reminders.

**Trigger module:** Schedule → Every week → Monday 9:00 AM IST (UTC+5:30)

**Action modules (repeat for each dept head):**

1. Notion → Create Database Item in `tasks_database`
    - Task Name: `🔄 Weekly Review — [Department] — [Week Date]`
    - Brand: Nivy Next (or set per dept)
    - Department: [the relevant department]
    - Status: To Do
    - Priority: High
    - Owner: [dept head person]
    - Deadline: Friday of that week

**Departments to create for:**

- Sales (Owner: Sales Manager)
- Marketing (Owner: Marketing Lead)
- Client Delivery (Owner: Delivery Manager)
- Operations (Owner: COO / Ops Lead)

**Test:** Temporarily change trigger to “every 5 minutes” → verify tasks appear → change back to weekly.

---

# 🤖 SCENARIO 4 — KPI Below Threshold → Email / Slack Alert

**Priority:** Medium (activate after KPI DB has live data)

**What it does:** When a KPI entry’s Alert checkbox is checked (meaning Actual < Target), send an email alert to the relevant manager.

**Trigger module:** Notion → Watch Database Items → `KPI DB`

- Filter: Alert = Checked (true)

**Action modules:**

1. Gmail → Send Email
    - To: [manager email for that brand]
    - Subject: `🚨 KPI Alert — [KPI Name] — Nivy Empires`
    - Body:
        
        ```
        KPI: [KPI Name]
        Brand: [Brand]
        Department: [Department]
        Target: [Target]
        Actual: [Actual]
        Period: [Period]
        
        Action required: Review this KPI and update your action plan.
        Link: [Notion page URL]
        ```
        
2. Optional: Slack → Post Message to #alerts channel (if Slack is in use)

**Escalation rule:** If same KPI fires for 2 consecutive weeks → CC the Founder in the email.

---

# 🤖 SCENARIO 5 — Lead Follow-Up Queue (Outreach Log → Follow-Up Task)

**Priority:** Medium

**What it does:** Scans the Outreach Log DB every morning. If a lead’s last contact was 3 days ago and Status = “No Response”, automatically creates a follow-up task for the VA.

**Trigger module:** Schedule → Every day → 8:30 AM IST

**Action modules:**

1. Notion → Search Objects in `Outreach Log DB`
    - Filter: Status = No Response AND Last Contact Date ≤ Today minus 3 days
2. Iterator → loop through each matching lead
3. Notion → Create Database Item in `tasks_database`
    - Task Name: `🔄 Follow-up: [Lead Name] — [Company]`
    - Brand: Nivy Next
    - Department: Sales
    - Status: To Do
    - Priority: Medium
    - Owner: Assigned VA
    - Deadline: Today

**Deduplication:** Before creating, check if a follow-up task for this lead already exists today. If yes → skip.

---

# 📊 Scenario Priority & Build Order

| # | Scenario | Build Order | Est. Ops/Month |
| --- | --- | --- | --- |
| 1 | Form → Task | 🔴 First | ~50 |
| 2 | ChatGPT → Research Inbox | 🟠 Second | ~100 |
| 3 | Weekly Review Creator | 🟠 Third | ~16 |
| 4 | KPI Alert → Email | 🟡 Fourth | ~20 |
| 5 | Lead Follow-up Queue | 🟡 Fifth | ~200 |

**Total estimated:** ~386 ops/month — well within [Make.com](http://Make.com)’s free 1,000 ops/month tier.

**Once all 5 are live:** Mark each as ✅ Live in the Phase 9 Master Hub table.