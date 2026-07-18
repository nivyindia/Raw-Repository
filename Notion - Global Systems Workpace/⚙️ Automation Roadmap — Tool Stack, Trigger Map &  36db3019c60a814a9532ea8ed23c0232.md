# ⚙️ Automation Roadmap — Tool Stack, Trigger Map & Upgrade Path

> **Purpose:** Define the full tool stack for each phase, map automation priorities, and give the founder a clear upgrade path from free tools to a fully automated ecosystem — without over-investing in tools before revenue justifies it.
> 

> **Owner:** Founder / Tech Lead
> 

> **Status:** Phase 1 Active
> 

> **Last Updated:** May 2026
> 

---

# 🧭 AUTOMATION PHILOSOPHY

**Rule 1:** Never automate a process you haven't done manually first. Manual → Document → Automate.

**Rule 2:** Free tools until Phase 3. No paid tool should be added before revenue covers it 3x.

**Rule 3:** Automate in this order: reporting first, then onboarding, then CRM, then outreach. Revenue-facing processes get automated last (after they're proven manually).

**Rule 4:** Every automation must have a manual fallback. If Zapier breaks, the team still knows what to do without it.

---

# 🛠️ TOOL STACK BY PHASE

## 🔴 Phase 1 — Free / Near-Free Stack (Weeks 1–6)

> Total monthly cost target: ₹0 — ₹500
> 

| Tool | Purpose | Category | Cost |
| --- | --- | --- | --- |
| Notion | Workspace, SOPs, CRM (basic), learner tracking | Core OS | Free |
| Google Forms | Applications, daily reports, assignment submission, freelancer reports | Data collection | Free |
| Google Sheets | Performance tracking, lead management, scorecard, KPI dashboard | Tracking | Free |
| Google Drive | File storage, templates, shared documents | Storage | Free |
| WhatsApp | Learner communication groups, daily reminders, freelancer check-ins | Communication | Free |
| Gmail | Outreach templates, institute correspondence, notifications | Email | Free |
| Loom | Training video recordings (Modules 1–8) | Content | Free (limited) |
| Google Slides | Orientation deck, institute pitch deck | Presentations | Free |
| [Apollo.io](http://Apollo.io) (free tier) | Lead prospecting — 50 credits/month | Lead research | Free |
| LinkedIn (free) | Lead research, connection outreach | Outreach | Free |
| Calendly (free tier) | Freelancer appointment scheduling | Scheduling | Free |

**Phase 1 Automation Actions (Manual triggers, no code needed):**

- WhatsApp group message at 7:30 PM daily: "Daily report reminder — submit by 8 PM!"
- Google Forms auto-email confirmation on submission (built-in Forms feature)
- Google Sheets conditional formatting: red = missed report, green = submitted
- Gmail canned responses for rejection, orientation invite, and onboarding messages

---

## 🟠 Phase 2 — Low-Cost Additions (Weeks 7–14)

> Total monthly cost target: ₹500 — ₹2,000
> 

| Tool | Purpose | Replaces / Adds To | Cost |
| --- | --- | --- | --- |
| ClickUp (free) or Trello | Task management for operators | Notion task lists | Free |
| [Apollo.io](http://Apollo.io) (paid basic) | Expanded lead prospecting | Apollo free tier | ~₹1,200/mo |
| Typeform (free) | Better application + orientation forms | Google Forms | Free |
| Zoom (free) | Orientation sessions, freelancer calls | WhatsApp calls | Free |
| Notion CRM (upgraded) | Full pipeline + learner tracking in one place | Google Sheets CRM | Free |
| WhatsApp Business | Broadcast lists, quick replies, auto-response | WhatsApp personal | Free |
| [Bit.ly](http://Bit.ly) | Link tracking for outreach messages | — | Free |

**Phase 2 Automation Actions:**

- WhatsApp Business broadcast list for daily report reminders (no group noise)
- Google Sheets formula: auto-calculates weekly learner scorecard totals
- Google Forms → Google Sheets auto-population (native integration)
- Gmail filters: auto-label institute emails, freelancer reports, learner applications
- Calendly booking link in all freelancer outreach follow-ups

---

## 🟡 Phase 3 — Revenue-Funded Upgrades (Weeks 15–26)

> Total monthly cost target: ₹2,000 — ₹8,000
> 

| Tool | Purpose | Replaces | Cost |
| --- | --- | --- | --- |
| HubSpot (free CRM) | Full pipeline management, deal tracking, contact history | Notion/Sheets CRM | Free |
| Zapier (Starter) | Connect Forms → CRM → WhatsApp notifications | Manual copy-paste | ~₹1,500/mo |
| Slack (free) | Team communication — replaces WhatsApp for operators | WhatsApp groups | Free |
| Teachable or Notion LMS | Structured training portal, module unlocking | Notion pages | Free–₹1,500/mo |
| Loom (paid) | Unlimited training video storage + team sharing | Loom free | ~₹800/mo |
| Google Data Studio | Visual KPI dashboard for founder | Google Sheets charts | Free |
| Lemlist or Mailchimp | Email sequence automation for outreach | Gmail manual | ~₹1,200/mo |

**Phase 3 Automation Actions (Zapier flows):**

| Trigger | Action | Tool |
| --- | --- | --- |
| New Google Form submission (daily report) | Add row to Sheets + send Slack notification to Team Lead | Zapier |
| New learner application submitted | Send welcome email automatically | Zapier + Gmail |
| Lead status changes to "Meeting Booked" in CRM | Send Calendly confirmation to freelancer | Zapier + HubSpot |
| Freelancer weekly report submitted | Notify Founder on Slack | Zapier |
| CRM entry not updated in 5 days | Send reminder to assigned operator | Zapier + Slack |

---

## 🟢 Phase 4 — Scale Infrastructure (Month 7–12+)

> Total monthly cost target: ₹10,000 — ₹25,000 (funded by revenue)
> 

| Tool | Purpose | Replaces |
| --- | --- | --- |
| Custom Notion Dashboard or Retool | Real-time founder KPI visibility | Manual spreadsheet review |
| Make (Integromat) | Advanced multi-step automation flows | Zapier Starter |
| AI outreach tools (e.g. Expandi, Dripify) | Semi-automated LinkedIn outreach sequences | Manual DMs |
| Automated lead distribution system | Route leads to correct operator/freelancer automatically | Manual assignment |
| Dedicated LMS (Teachable Pro or Thinkific) | Full learner portal with auto-progression | Notion + Loom |
| CRM upgrade (HubSpot Starter paid) | Advanced pipeline analytics, reporting | HubSpot free |
| Analytics dashboard (Looker Studio) | Full ecosystem performance visualization | Google Sheets |

---

# ⏰ AUTOMATION PRIORITY ORDER

Build in this exact sequence. Don’t jump ahead.

| Priority | What to Automate | Why First | Phase |
| --- | --- | --- | --- |
| 1 | Daily report collection reminder | Reduces Team Lead nagging, builds habit | Phase 1 |
| 2 | Application form auto-confirmation email | First impression quality, saves founder time | Phase 1 |
| 3 | Scorecard calculation (Google Sheets formula) | Removes manual math, reduces error | Phase 2 |
| 4 | Learner onboarding email sequence | Welcome → Orientation → Day 1 task (3 emails) | Phase 2 |
| 5 | CRM status update reminders (missed updates) | Keeps pipeline data clean | Phase 3 |
| 6 | Freelancer weekly report notification to Founder | Founder doesn’t have to chase | Phase 3 |
| 7 | Institute monthly report generation | Template-based, saves 2 hours/month | Phase 3 |
| 8 | Lead routing to operators | Removes manual assignment bottleneck | Phase 4 |
| 9 | Outreach sequence automation | Scale without adding headcount | Phase 4 |
| 10 | Full KPI dashboard auto-refresh | Founder sees live numbers, not weekly summaries | Phase 4 |

---

# 📧 AUTOMATION DESIGN: ONBOARDING EMAIL SEQUENCE

Build this in Phase 2 using Gmail + Zapier (or manually in Phase 1 with canned responses).

**Trigger:** Orientation Acknowledgment Form submitted.

| Email # | Send Timing | Subject | Content Summary |
| --- | --- | --- | --- |
| Email 1 | Immediately | Welcome to the ecosystem — here’s what happens next | Confirm receipt, share Module 1 link, set Day 1 expectation |
| Email 2 | Day 1 (morning) | Your first task is waiting | Remind of Day 1 task, link to daily report form, share WhatsApp group link |
| Email 3 | Day 3 | How are you doing? | Check-in, remind of daily report streak, share Module 2 link if Module 1 done |
| Email 4 | Day 7 | End of Week 1 — here’s what great looks like | Share what a top Week 1 performer looks like, motivate continuation |

---

# ⚠️ AUTOMATION RISK CHECKLIST

Before deploying any automation, answer all of these:

- [ ]  Is the manual version of this process documented in an SOP?
- [ ]  Does the team know what to do if this automation breaks?
- [ ]  Is the automation tested with real data before going live?
- [ ]  Does the automation have a failure notification? (i.e. does someone get alerted if it stops working?)
- [ ]  Is there a single person responsible for maintaining this automation?
- [ ]  Has the cost been checked against current revenue (3x rule)?

**If any answer is No: do not deploy until fixed.**

---

# 🗓️ TOOL UPGRADE DECISION CHECKLIST

Use this before adding any paid tool:

- [ ]  Is there a free version that meets current needs?
- [ ]  Has the manual version been done for at least 4 weeks?
- [ ]  Does this tool solve a documented bottleneck (not a nice-to-have)?
- [ ]  Is monthly revenue at least 3x the tool cost?
- [ ]  Is there one person assigned to own and maintain this tool?

**All 5 must be Yes before purchasing.**

---

*Automation Roadmap — Built May 2026 | Part of Business Operating System*