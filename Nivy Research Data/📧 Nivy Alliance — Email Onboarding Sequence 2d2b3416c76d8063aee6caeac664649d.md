# 📧 Nivy Alliance — Email Onboarding Sequence

START
│
├─ Contact Added to Segment: Alliance – Outreach
│
├─ EMAIL O1: Private Invitation (Outreach)
│     ├─ Link A: Apply for Review
│     └─ Link B: Not Relevant Right Now
│
├─ DECISION (Link Click?)
│     │
│     ├─ IF Clicked Link A (Apply)
│     │     ├─ Tag: Interested
│     │     ├─ Move to Segment: Alliance – Applied
│     │     ├─ EXIT Outreach Campaign
│     │     └─ ENTER Application Campaign
│     │
│     ├─ IF Clicked Link B (Not Interested)
│     │     ├─ Tag: Not Interested
│     │     ├─ Move to Segment: Alliance – Suppressed
│     │     └─ STOP (No further emails)
│     │
│     └─ IF No Click
│           ├─ WAIT 2 Days
│           ├─ EMAIL O2: Soft Reminder
│           │     ├─ Link A: Apply for Review
│           │     └─ Link B: Not Relevant
│           │
│           ├─ DECISION (Any Click?)
│           │     ├─ IF Clicked Link A → Same as above (Applied Path)
│           │     ├─ IF Clicked Link B → Suppressed Path
│           │     └─ IF No Click
│           │           ├─ WAIT 3 Days
│           │           ├─ EMAIL O3: Break-Up / Closure
│           │           ├─ Tag: No Response
│           │           └─ STOP
│
├─ ENTER Campaign: Alliance – Application
│
├─ TRIGGER: Application Form Submitted
│
├─ EMAIL A1: Application Received
│
├─ WAIT 2 Days
│
├─ EMAIL A2: How Nivy Alliance Works
│
├─ WAIT 2 Days
│
├─ EMAIL A3: Who It’s For / Who It’s Not
│
├─ DECISION: Application Status (Admin Controlled)
│     │
│     ├─ IF Status = Approved
│     │     ├─ Move to Segment: Alliance – Approved
│     │     ├─ EXIT Application Campaign
│     │     └─ ENTER Activation Campaign
│     │
│     └─ IF Status = Rejected / On Hold
│           ├─ EMAIL R1: Polite Hold / Rejection
│           ├─ Tag: Application Hold
│           └─ STOP
│
├─ ENTER Campaign: Alliance – Activation
│
├─ EMAIL J1: Approval + Submit Requirement
│     └─ Link: Requirement Submission Form
│
├─ DECISION: Requirement Form Submitted?
│     │
│     ├─ IF Yes
│     │     ├─ Tag: Requirement Submitted
│     │     ├─ EMAIL J2: Welcome to Nivy Alliance
│     │     ├─ Move to Segment: Alliance – Active Members
│     │     └─ END (Active Member)
│     │
│     └─ IF No
│           ├─ WAIT 2 Days
│           ├─ EMAIL J1B: Requirement Reminder
│           ├─ WAIT 3 Days
│           ├─ IF Still No Submission
│           │     ├─ Tag: Approved but Inactive
│           │     └─ STOP (No chasing)
│
END

# 🧠 KEY DESIGN PRINCIPLES THIS FLOW FOLLOWS

- **Intent-driven** (clicks decide everything)
- **Hard exits** for non-interest
- **No infinite loops**
- **Admin authority preserved**
- **Zero manual follow-ups**
- **Mautic-native logic only**

---

# 🔑 GOLDEN RULE USED IN THIS FLOW

> Silence = disinterest
> 
> 
> **Click = consent**
> 
> **Approval = privilege**
> 

Perfect. Below is **EVERY SINGLE EMAIL** in the **Nivy Alliance automation**, written **clean, Tier-1, non-salesy**, and **ready to paste into Mautic**.

I’ve grouped them **by stage**, exactly matching the flowchart you approved.

---

# 🟦 STAGE 1: OUTREACH (INTENT DETECTION)

---

### 📧 EMAIL O1 — Initial Outreach (Invitation)

Hello,

We’re reaching out to a limited number of companies regarding a private initiative called **Nivy Alliance**.

Nivy Alliance is **not a marketplace** or lead-selling platform.

It’s a **verified, admin-facilitated business exchange** where companies share real outsourcing requirements and receive relevant introductions—confidentially.

This is suitable for organizations that:

- Regularly outsource services
- Prefer quality over volume
- Value professional, quiet partnerships

If this aligns with how your company works, you may apply for review below.

🔗 Apply for Review

[APPLICATION LINK]

If this isn’t relevant right now:

🔗 Not Relevant at This Time

[DECLINE LINK]

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL O2 — Soft Follow-Up

Hello,

Following up on our earlier invitation to **Nivy Alliance**.

We’re closing the current review window soon and wanted to check if this initiative aligns with your organization’s partnership approach.

There’s no obligation—applications are reviewed selectively to maintain ecosystem quality.

🔗 Apply for Review

[APPLICATION LINK]

🔗 Not Relevant at This Time

[DECLINE LINK]

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL O3 — Break-Up / Closure (No Response)

Hello,

We haven’t heard back regarding our invitation to **Nivy Alliance**, so we’ll pause outreach from our side.

Nivy Alliance is a private ecosystem, and we reach out only where there appears to be potential alignment.

If this isn’t relevant at the moment, no action is required.

Should your organization’s needs change, you’re welcome to apply in the future.

Wishing you continued success.

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL O-EXIT — “Not Interested” Reply Handling

Hello,

Thank you for letting us know.

We’ll update our records and won’t follow up further.

If your organization ever prefers **confidential, admin-facilitated business introductions**, you’re welcome to reconnect anytime.

Wishing you continued success.

Regards,

**Nivy Alliance – Membership Desk**

---

# 🟦 STAGE 2: APPLICATION & TRUST BUILDING

---

### 📧 EMAIL A1 — Application Received

Hello,

Thank you for applying to **Nivy Alliance**.

Your application has been received and is currently under review by our admin team.

Nivy Alliance is a **reciprocity-based business exchange** built on:

- Verified companies
- Confidential requirement sharing
- Admin-controlled introductions

This is not an open network or lead platform.

You’ll receive an update within **48–72 hours**.

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL A2 — How Nivy Alliance Works

Hello,

Before completing your review, here’s a brief overview of **how Nivy Alliance operates**.

- Members join as **companies**, not sellers
- Access is earned by sharing **real requirements**
- Buyer identities remain confidential
- All introductions are admin-facilitated

### Reciprocity Rule:

To receive value, members must:

✔ Share a genuine outsourcing requirement

✔ OR declare what they outsource regularly

This keeps the ecosystem focused and spam-free.

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL A3 — Who It’s For / Who It’s Not

Hello,

To maintain quality, **Nivy Alliance is intentionally selective**.

### Ideal for:

- Companies outsourcing services consistently
- Founders, CXOs, Operations Heads
- Established vendors with delivery credibility

### Not designed for:

- Freelancers or solo consultants
- Cold outreach or mass promotions
- Unverified or anonymous entities

We’ll update you shortly regarding your application status.

Regards,

**Nivy Alliance – Membership Desk**

---

# 🟦 STAGE 3: APPROVAL / HOLD

---

### 📧 EMAIL R1 — Polite Hold / Rejection

Hello,

Thank you for your interest in **Nivy Alliance**.

After review, we’re unable to proceed at this stage.

This decision reflects **current ecosystem balance**, not company capability.

You’re welcome to reapply in the future as your organization’s needs evolve.

We appreciate your interest.

Regards,

**Nivy Alliance – Membership Desk**

---

# 🟦 STAGE 4: ACTIVATION & JOINING

---

### 📧 EMAIL J1 — Approved + Requirement Submission

Hello,

We’re pleased to inform you that your company has been **approved** for **Nivy Alliance**.

To activate participation, please submit **one** of the following:

- A current business requirement
- OR services your organization regularly outsources

Once verified:

- Your requirement is posted anonymously
- Relevant partners are matched
- Introductions occur only upon mutual fit

🔗 Submit Requirement

[REQUIREMENT LINK]

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL J1B — Requirement Reminder

Hello,

This is a gentle reminder to submit your **first business requirement** to activate your Nivy Alliance access.

Until submission:

- Viewing opportunities remains restricted
- Introductions cannot be initiated

🔗 Submit Requirement

[REQUIREMENT LINK]

Regards,

**Nivy Alliance – Membership Desk**

---

### 📧 EMAIL J2 — Official Welcome / Joined

Hello,

Your requirement has been received and verified.

You are now **officially active** inside **Nivy Alliance**.

### What happens next:

- Your requirement is live (anonymously)
- Potential partners are evaluated by admins
- Introductions are made only when relevance is confirmed

Welcome to a **quiet, professional way of building business partnerships**.

Regards,

**Nivy Alliance – Membership Desk**

---

# ✅ SUMMARY (FOR MAUTIC)

- **Total Emails:** 11
- **All click-driven**
- **Hard exits included**
- **Zero chasing**
- **Premium authority preserved**

---

## NEXT (IMPLEMENTATION PHASE)

I can now:

1. Convert this into **exact Mautic campaign steps**
2. Create **email HTML structure**
3. Define **tags + custom fields**
4. Build **6-month re-invite automation**
5. Add **WhatsApp mirror flow**

Tell me **what to build next**, and I’ll go implementation-level.