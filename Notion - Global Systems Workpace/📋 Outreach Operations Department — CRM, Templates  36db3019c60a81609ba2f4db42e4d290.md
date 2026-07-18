# 📋 Outreach Operations Department — CRM, Templates & Lead System

# 📋 Outreach Operations Department — Full Operating System

> **Department Purpose:** Generate consistent, qualified lead pipelines that feed the freelancer closing team. This department is the revenue engine.
> 

> **Owner:** Outreach Lead (Founder Phase 1 → Senior Operator Phase 2+)
> 

> **Staffed By:** Operators + Learners (supervised)
> 

> **Last Updated:** May 2026
> 

---

# 🧭 WHY THIS DEPARTMENT EXISTS

Without structured outreach operations:

- Freelancers waste time finding their own leads (they should only be closing)
- No data is collected so nothing can be improved
- Outreach is random and inconsistent
- Revenue pipeline dries up unpredictably

With this department:

- Freelancers receive ready-to-call appointments
- Every message is tracked
- Every number is measured
- The pipeline is predictable and improvable

**The rule: Outreach Ops fills the calendar. Freelancers close the calendar. Never confuse the two.**

---

# 🗺️ THE 4-LAYER OUTREACH SYSTEM

```
Layer 1: Lead Research
    ↓ (Clean, verified prospect list)
Layer 2: CRM Management
    ↓ (Organized, tracked, updated)
Layer 3: Outreach Execution
    ↓ (Messages sent, responses captured)
Layer 4: Follow-Up System
    ↓ (Consistent follow-through to meetings)
         ↓
    [Qualified Appointments → Freelancer Closers]
```

---

# LAYER 1 — LEAD RESEARCH

## What Is Lead Research?

Lead research is the process of identifying people or businesses who could benefit from your services, collecting their contact information, and organizing it in a usable format.

**Who does it:** Beginner Learners (under Operator supervision)

**When:** Daily. Minimum 20 leads per active learner per day.

**Output:** Completed rows in the Standard Lead Sheet

---

## Target Niche Selection — How to Choose Who to Reach

Don't research everyone. Research the right people. Each batch is assigned a niche by the Outreach Lead.

### Niche Priority Matrix

| Niche | Why Target Them | Service Fit | Difficulty |
| --- | --- | --- | --- |
| Small accounting firms | Need bookkeeping support, admin help | Bookkeeping support, VA | Medium |
| Freelance consultants | Need LinkedIn optimization, outreach help | LinkedIn opt., outreach support | Low |
| Digital marketing agencies | Need lead gen, outreach operators | Lead gen, outreach support | Medium |
| E-commerce businesses | Need VA, admin, product research | Virtual assistance | Low |
| Coaching / training businesses | Need outreach, content scheduling | Outreach support, content scheduling | Low |
| B2B SaaS startups | Need lead gen, outreach | Lead generation | High |

> ⚠️ **Phase 1 rule:** Start with Low and Medium difficulty niches only. High difficulty requires experienced operators.
> 

---

## Standard Lead Sheet — Required Format

> Every lead entered must have ALL required fields. Incomplete rows are returned for correction.
> 

| Field | Required? | Notes |
| --- | --- | --- |
| Full Name | Yes | First + Last |
| Company Name | Yes | Exact name |
| Role / Title | Yes | As listed on LinkedIn |
| LinkedIn URL | Yes | Direct profile link |
| Email | If found | Apollo, [Hunter.io](http://Hunter.io), manual |
| City / Country | Yes |  |
| Niche | Yes | From approved niche list |
| Lead Source | Yes | LinkedIn / Apollo / Manual |
| Date Added | Yes | Auto-fill or manual |
| Verification Status | Yes | Verified / Unverified |
| Notes | Optional | Anything relevant |

### Lead Quality Standards

**Verified lead:** LinkedIn profile is active (recent activity), role matches target criteria, company is real and operating.

**Unverified lead:** Found the name and URL but haven't confirmed activity or company status.

**Rejected lead:** Duplicate, wrong niche, broken LinkedIn URL, inactive profile (no activity in 6+ months).

> **Quality rule:** Operator spot-checks 10% of every lead batch before it enters the CRM. Any batch with >20% rejected leads is returned to the learner for correction.
> 

---

## Lead Research Tools (Free Tier)

| Tool | What It Does | Free Limit | Best For |
| --- | --- | --- | --- |
| LinkedIn (manual) | Browse and find profiles | Unlimited (with limitations) | B2B contacts |
| [Apollo.io](http://Apollo.io) (free) | Lead database with emails | 50 exports/month | Email finding |
| [Hunter.io](http://Hunter.io) (free) | Email finder by domain | 25 searches/month | Email verification |
| Google Search | Company + role search | Unlimited | Niche-specific search |
| LinkedIn Sales Navigator | Advanced search | Paid (Phase 3+) | Scale |

### LinkedIn Search Strings (Teach These to Learners)

```
Find freelance consultants in India:
    site:linkedin.com/in "freelance consultant" "India"

Find accounting firm owners:
    site:linkedin.com/in "accounting firm" "founder" OR "owner" "India"

Find digital marketing agency owners:
    site:linkedin.com/in "digital marketing agency" "founder" OR "CEO"
```

---

# LAYER 2 — CRM MANAGEMENT

## Why CRM Management Is Non-Negotiable

Without CRM discipline:

- The same person gets messaged 4 times by different operators (embarrassing)
- Follow-ups are forgotten
- No one knows what stage each lead is at
- Revenue opportunities disappear silently

**The CRM is the memory of the outreach system. It must be accurate, always.**

---

## CRM Structure — Lead Status Stages

| Stage | What It Means | Who Updates It |
| --- | --- | --- |
| 🔵 Not Contacted | Lead added, no message sent yet | Learner (on add) |
| 📤 Connection Sent | LinkedIn connection request sent | Operator |
| ✅ Connected | They accepted the connection | Operator |
| 💬 Messaged | First DM sent | Operator |
| 📩 Replied | They replied (any response) | Operator |
| 📅 Meeting Booked | Call/meeting scheduled | Operator / Freelancer |
| 🤝 Meeting Done | Call completed | Freelancer |
| 💼 Proposal Sent | Quote or proposal shared | Freelancer |
| ✅ Closed Won | Client signed / paid | Freelancer |
| ❌ Closed Lost | Not interested, explicit no | Operator / Freelancer |
| 🔄 Follow-Up Pending | Waiting for their response, follow-up due | Operator |
| 🚫 Do Not Contact | Requested not to be contacted | Any |

---

## CRM Fields — Full Schema

| Field | Type | Required? |
| --- | --- | --- |
| Lead Name | Text | Yes |
| Company | Text | Yes |
| Role | Text | Yes |
| LinkedIn URL | URL | Yes |
| Email | Text | If found |
| Niche | Select | Yes |
| Status | Select (from stages above) | Yes |
| Assigned Operator | Text | Yes |
| Last Contact Date | Date | Yes |
| Next Follow-Up Date | Date | Yes |
| Touch Count | Number | Yes (auto-increment) |
| Last Message Sent | Text | Summary only |
| Response Summary | Text | Brief summary of their reply |
| Meeting Date | Date | If booked |
| Notes | Text | Running log |
| Assigned Freelancer | Text | When meeting booked |

---

## CRM Update Rules (SOP-OUTREACH-004)

1. Every outreach action must be logged in the CRM **within 2 hours** of happening
2. Status must be updated **immediately** when it changes
3. No status can remain "Messaged" for more than 7 days without a follow-up or status change
4. "Follow-Up Pending" must always have a Next Follow-Up Date filled
5. Weekly CRM audit: Operator Lead checks for stale entries (no update in 7+ days)

---

# LAYER 3 — OUTREACH EXECUTION

## Channel Strategy

| Channel | Best For | Volume/Day | Operator Level |
| --- | --- | --- | --- |
| LinkedIn DM | B2B, warm connection | 30–50 | Level 1+ |
| Cold Email | Volume outreach | 20–40 | Level 1+ |
| LinkedIn Comment Engagement | Relationship building | 10–20 | Level 1+ |
| WhatsApp (warm leads only) | Post-reply follow-up | 5–10 | Level 2+ |
| Instagram DM | Coaches, creators | 10–20 | Level 2+ |

---

## Master Message Library

> These are the core templates. Every operator should understand WHY each message is written the way it is, not just copy-paste it.
> 

### LinkedIn — Connection Request

**Template A (General):**

> *Hi [Name], I noticed your work in [area]. I'm building skills in [service] and would love to connect with professionals in your space.*
> 

**Template B (Niche-specific):**

> *Hi [Name], your [accounting firm / agency / consulting work] in [city] caught my attention. Would love to connect with someone doing real work in this space.*
> 

**Template C (Mutual interest):**

> *Hi [Name], I read your post on [topic] — really resonated with me. Would love to stay connected.*
> 

> ⚠️ **Rule:** Connection requests must be under 300 characters. No pitch. No "I want to offer you...". Just a genuine reason to connect.
> 

---

### LinkedIn — First DM (After Connection Accepted)

**Template A (Curiosity-led):**

> *Hi [Name], thanks for connecting! I've been following [specific thing about their work] — really interesting space. I work in [service area] and am always curious how people in your field handle [relevant challenge]. No agenda — just keen to learn from people actually in the field.*
> 

**Template B (Value-first):**

> *Hi [Name], thanks for connecting. I put together a quick [checklist / resource / insight] on [topic relevant to their niche] that a few [role type] found useful. Happy to share if you'd find it helpful.*
> 

**Template C (Direct but soft):**

> *Hi [Name], appreciate the connection. I help [type of business] with [specific service]. Noticed your [company/work] might benefit from this. Would a quick 15-minute conversation make sense? Happy either way.*
> 

> ⚠️ **Rule:** First DMs must be under 100 words. No attachments. No "please check my profile." One soft CTA maximum.
> 

---

### Cold Email Templates

**Subject Line Options:**

- `Quick question, [First Name]`
- `[Their Company] — had a thought`
- `Noticed something about [Company Name]`
- `15 minutes? — [Your Name]`

**Email Body Template:**

```
Hi [Name],

I came across [Company Name] while researching [niche] businesses in [location].

I help [type of business] with [specific service] — specifically [one clear outcome].

Would it make sense to have a 15-minute conversation to see if there's a fit?

No pressure either way.

[Your Name]
[Your LinkedIn URL]
```

> ⚠️ **Rules for cold email:**
> 

> - Subject line under 7 words
> 

> - Body under 100 words
> 

> - One CTA only ("15-minute call")
> 

> - No attachments on first email
> 

> - No buzzwords ("synergy", "value proposition", "leverage")
> 

> - Personalize at least the company name and niche reference
> 

---

## Outreach Quality Checklist (Run Before Sending)

- [ ]  Is the message under the word limit?
- [ ]  Is there at least one personalized element (name, company, or relevant detail)?
- [ ]  Is there ZERO pitch or product mention in a connection request?
- [ ]  Does the CTA ask for one small thing only (connect, reply, 15 min)?
- [ ]  Is the lead's status in the CRM set to "Connection Sent" or "Messaged"?
- [ ]  Is the send date logged in the CRM?

---

# LAYER 4 — THE FOLLOW-UP SYSTEM

## Why Follow-Ups Are the Most Important Thing

Research consistently shows:

- 80% of sales require 5+ follow-ups
- 44% of salespeople give up after 1 follow-up
- The people who follow up 5+ times close most of the business

**Teaching this to operators is not optional. It is the single biggest lever in this system.**

---

## The 5-Touch Follow-Up Sequence

> One sequence per lead. Run systematically. Never improvise without documenting.
> 

| Touch | Day | Channel | Message Type | Goal |
| --- | --- | --- | --- | --- |
| Touch 1 | Day 0 | LinkedIn DM / Email | Opening message | Start conversation |
| Touch 2 | Day 3–4 | Same channel | Value-add (resource, insight, question) | Keep conversation open |
| Touch 3 | Day 7–8 | Same channel | Soft re-engagement | "Just checking in" |
| Touch 4 | Day 14 | Same channel + try second channel | Direct ask | "Would a quick call make sense?" |
| Touch 5 | Day 21 | Final message | Graceful close + resource leave | "Last message — here's something useful anyway" |

---

## Touch-by-Touch Templates

**Touch 2 — Value Add:**

> *Hi [Name], following up on my last message. I recently [read / put together / came across] something on [topic relevant to their work] that I thought might be useful for someone in your position. Happy to share if you'd like. No pitch attached — just found it genuinely relevant.*
> 

**Touch 3 — Soft Re-engagement:**

> *Hi [Name], just circling back. I know you're probably busy — no worries at all. Just wanted to stay on your radar in case [service] ever becomes relevant. What does your current approach to [relevant challenge] look like?*
> 

**Touch 4 — Direct Ask:**

> *Hi [Name], I'll be direct — I help [business type] with [service], and based on what I've seen of your work, I think there could be a fit. Would a 15-minute call this week or next make sense? If not, totally fine — just wanted to ask clearly.*
> 

**Touch 5 — Final Goodbye:**

> *Hi [Name], this will be my last message so I don't clog your inbox. If [service] ever becomes relevant down the line, I'd love to reconnect. In the meantime, here's [useful resource / insight]. Wishing you well with [their work / company].*
> 

> After Touch 5: Update CRM status to "Closed Lost" unless they replied at any point. Do NOT keep following up beyond Touch 5 unsolicited.
> 

---

## Follow-Up Discipline Checklist

> Operators run this every morning before starting outreach.
> 
1. Open CRM
2. Filter by "Follow-Up Pending" + Next Follow-Up Date = today or past
3. For each: send the appropriate touch (check Touch Count field to know which touch)
4. Update CRM: Last Contact Date, Touch Count (+1), Next Follow-Up Date
5. If they replied: update status to "Replied", log response summary

---

# 📊 OUTREACH METRICS — WHAT WE TRACK

## Daily Metrics (Tracked in Google Sheets)

| Metric | Who Tracks | Target (Per Operator/Day) |
| --- | --- | --- |
| Leads added to CRM | Learner / Operator | 20–30 |
| Connection requests sent | Operator | 20–30 |
| First DMs sent | Operator | 15–25 |
| Follow-ups sent | Operator | 10–20 |
| Replies received | Operator | Track (no daily target) |
| Meetings booked | Operator | 1–2 per week |

## Weekly Metrics (Reviewed Every Monday)

| Metric | Formula | Benchmark |
| --- | --- | --- |
| Reply Rate | (Replies / Messages Sent) × 100 | 3–7% (industry normal) |
| Meeting Rate (from replies) | (Meetings Booked / Replies) × 100 | 15–25% |
| Follow-up Completion Rate | (Follow-ups Sent / Follow-ups Due) × 100 | 80%+ |
| Lead Research Quality | (Verified Leads / Total Added) × 100 | 85%+ |
| CRM Accuracy Rate | (Updated Entries / Total Active) × 100 | 90%+ |

## Monthly Funnel Report

```
Monthly Outreach Funnel — [Month/Year]

Total leads in CRM (new this month):     ____
Total messages sent:                      ____
Total replies received:                   ____
Reply rate:                               ____%
Meetings booked:                          ____
Meeting rate (from replies):              ____%
Deals closed (via freelancers):           ____
Close rate (from meetings):               ____%
Revenue generated:                        ____

Top performing operator:                  ____
Top performing niche:                     ____
Biggest bottleneck this month:            ____
Action for next month:                    ____
```

---

# 🔄 CRM AUDIT PROTOCOL — Weekly

> Outreach Lead runs this every Monday morning. 20–30 minutes.
> 

**Step 1:** Filter CRM by "Last Updated" = more than 7 days ago

**Step 2:** For each stale entry:

- Is there a Next Follow-Up Date set? If yes: assign to operator for today
- Is it past Touch 5? If yes: close as Lost
- Is the status unclear? Clarify with the operator who owns it

**Step 3:** Filter by "Meeting Booked" status

- Confirm meeting date and assigned freelancer
- Ensure freelancer has the lead's details and context

**Step 4:** Check for duplicates (same LinkedIn URL appearing twice)

- Merge or delete duplicate

**Step 5:** Generate weekly numbers (leads added, messages sent, reply rate) for Monday report

---

# 📁 SOP LIBRARY — OUTREACH DEPARTMENT

---

## SOP-OUTREACH-001 — LinkedIn Outreach Execution

**Purpose:** Standardize how LinkedIn outreach is sent to protect brand reputation.

**Trigger:** Operator starts daily outreach session

**Owner:** Operator (supervised by Outreach Lead)

**Steps:**

1. Open CRM. Filter: Status = "Not Contacted" + assigned to you
2. Open each lead's LinkedIn profile. Check: Is it active? Is niche correct?
3. If profile is stale or irrelevant: mark CRM status "Rejected", note reason
4. For valid leads: send Connection Request using approved template (personalized)
5. Log in CRM: Status → "Connection Sent", Last Contact Date = today
6. After 24–48 hours: Check if connection was accepted
7. If accepted: send First DM within 24 hours. Update CRM: Status → "Messaged"
8. Set Next Follow-Up Date = 3 days from DM send
9. If connection not accepted after 7 days: mark as "Follow-Up Pending" and try again in 14 days

**Checkpoint:** No message sent without a CRM update.

**Failure signal:** Leads marked "Messaged" with no Next Follow-Up Date.

---

## SOP-OUTREACH-002 — Cold Email Outreach

**Purpose:** Standardize cold email quality and protect sender reputation.

**Trigger:** Operator has verified email and begins email campaign

**Owner:** Operator Level 2+

**Steps:**

1. Verify email using [Hunter.io](http://Hunter.io) before sending (don't send to unverified emails)
2. Personalize subject line and opening line for each email (no batch-copy)
3. Use approved email template. Max 100 words body.
4. Send from designated outreach email address (not personal Gmail)
5. Log in CRM: Status → "Messaged", channel = Email, date = today
6. Set Next Follow-Up Date = 3 days
7. If reply received: update CRM immediately, escalate to Outreach Lead if meeting-worthy

**Checkpoint:** No email sent to unverified address.

**Failure signal:** Bounce rate above 10% (means emails are unverified).

---

## SOP-OUTREACH-003 — Follow-Up Sequence Execution

**Purpose:** Ensure every lead goes through the full 5-touch sequence consistently.

**Trigger:** Every morning, before new outreach begins

**Owner:** Operator

**Steps:**

1. Open CRM. Filter: Next Follow-Up Date = today or earlier + Status = "Follow-Up Pending"
2. For each lead: check Touch Count to know which touch to send
3. Send the correct touch using the master template library
4. Update CRM: Touch Count +1, Last Contact Date = today, Next Follow-Up Date = per sequence schedule
5. If they reply at any touch: immediately update Status → "Replied", log summary
6. After Touch 5 with no reply: update Status → "Closed Lost". Note: "Completed 5-touch, no response."

**Checkpoint:** All "Follow-Up Pending" leads processed before new outreach begins.

**Failure signal:** Leads sitting in "Follow-Up Pending" for 3+ days past their due date.

---

## SOP-OUTREACH-004 — CRM Update Standards

**Purpose:** Keep CRM accurate so the entire team makes decisions based on real data.

**Trigger:** After any outreach action

**Owner:** All operators

**Non-negotiable rules:**

1. Every action logged within 2 hours of happening
2. Status updated every time it changes
3. Follow-up date always set for any open lead
4. Response summaries written in plain language (2–3 sentences max)
5. No two operators own the same lead (check before taking a lead)
6. Duplicates flagged immediately to Outreach Lead

---

## SOP-OUTREACH-005 — Meeting Handoff to Freelancer

**Purpose:** Ensure a smooth, professional transition when a meeting is booked.

**Trigger:** Operator marks a lead as "Meeting Booked"

**Owner:** Operator (handoff) + Outreach Lead (oversight)

**Steps:**

1. Operator notifies Outreach Lead: "Meeting booked — [Lead Name] — [Date/Time]"
2. Outreach Lead assigns the meeting to appropriate Freelancer Closer
3. Operator prepares Lead Brief:
    - Name, company, role
    - What service they expressed interest in
    - Summary of conversation so far (2–3 lines)
    - Any specific concerns or context mentioned
4. Lead Brief shared with Freelancer via WhatsApp or Slack (24 hours before meeting)
5. Freelancer confirms receipt of brief
6. After meeting: Freelancer updates CRM with outcome

**Checkpoint:** Freelancer never enters a meeting cold (no context).

**Failure signal:** Freelancer asks "who is this person?" on the day of the call.

---

# 🛡️ OUTREACH PROTECTION RULES

## Brand Protection

> One bad outreach message can damage the company's reputation. These rules are enforced strictly.
> 

| Rule | Why |
| --- | --- |
| Never pitch in a connection request | LinkedIn flags this as spam. Connection accepted rate drops 50%. |
| Never send more than 50 LinkedIn requests/day per account | LinkedIn limits and may restrict account |
| Never use misleading subject lines | Can trigger spam filters and damage trust |
| Never follow up more than 5 times without a reply | After 5 touches, it becomes harassment |
| Never send a generic copy-paste DM | Detected as spam, damages reply rate |
| Always honor "Do Not Contact" requests | Legal and ethical requirement |
| Never claim a meeting is already booked (fake urgency) | Destroys trust immediately |

---

# ⚠️ OUTREACH RISKS & FAILURE POINTS

| Risk | Signal | Prevention |
| --- | --- | --- |
| Operator sends spam-like messages | Reply rate drops below 1% | Weekly message quality review |
| CRM gets outdated and unusable | Operators start maintaining personal spreadsheets | Weekly CRM audit protocol |
| Leads receive duplicate outreach | Complaints, embarrassment | Shared CRM with ownership field |
| Outreach volume too low to see results | No meetings after 4 weeks | Daily tracking, minimum volume enforcement |
| Outreach volume too high (burn accounts) | LinkedIn account restricted | Daily limits enforced per operator |
| Follow-ups forgotten | Leads go cold forever | Follow-up Due filter reviewed every morning |

---

# 📊 OUTREACH OPERATIONS — TOOL SETUP CHECKLIST

| Tool | Purpose | Setup Status |
| --- | --- | --- |
| Google Sheets — Master Lead Sheet | Lead research storage | ⬜ Build |
| Google Sheets — CRM Tracker | Pipeline tracking | ⬜ Build |
| Google Sheets — Daily Outreach Log | Daily numbers | ⬜ Build |
| [Apollo.io](http://Apollo.io) (free account) | Lead prospecting | ⬜ Create |
| [Hunter.io](http://Hunter.io) (free account) | Email verification | ⬜ Create |
| Loom or screen recorder | Outreach walkthroughs | ⬜ Set up |
| Calendly (free) | Appointment scheduling | ⬜ Set up |
| Gmail — outreach address | Cold email sending | ⬜ Create |
| WhatsApp group — Outreach Ops | Team communication | ⬜ Create |

---

# 🔗 NEXT PAGES TO BUILD

- [ ]  🤝 Freelancer Partnership Department — receives leads from this department
- [ ]  🏫 Institute Partnership Department — provides learners to this department
- [ ]  📊 Performance Management — tracks this department's KPIs
- [ ]  📁 SOP Master Library — all SOPs indexed

---

*Outreach Operations Department OS — Built May 2026 | Part of Business Operating System*