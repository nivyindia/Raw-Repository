# 🏗️ Global Systems Hub — Cross-Brand SOPs, HR, Finance, Legal, Partner Ecosystem

> **Purpose:** Every system, SOP, and framework that 2+ Nivy brands share. Nothing here is duplicated per brand. Brands link here instead.
> 

> **Owner:** Claude + Founder | Built: May 18, 2026 | Phase 5
> 

---

## 🌐 1. Universal Outreach SOP

Applies to: Nivy Next, Nivy Advisory, Nivy Jobs, Nivy Nexus

**The Universal Outreach Framework applies across all brands. Each brand customises the messaging, not the process.**

### Step-by-step

1. **Identify target** — Use ICP criteria specific to the brand (see Brand OS > Strategy)
2. **Enrich the contact** — Verify LinkedIn, email, company size, region
3. **Write personalised first line** — Reference a specific trigger (post, news, event)
4. **Send via primary channel** — Cold email for B2B; LinkedIn DM for warm leads; WhatsApp for existing relationships
5. **Follow up on Day 3, 7, 14** — Change medium on Day 7 (email → LinkedIn)
6. **Log every touchpoint** — Outreach Log DB: Date | Channel | Status | Response | Next Step
7. **Qualify or disqualify after 3 touches** — Move to CRM (HubSpot) or Archive

**Quality standard:** Every outreach message must pass the 5-second test — would the recipient immediately understand who we are, why we're reaching out, and what the next step is?

---

## 👥 2. Universal HR Policies

Applies to: All brands. Brand-specific addenda go in Brand OS > HR & People.

### Leave Policy

- Annual leave: 18 days per year (pro-rated for part-year joiners)
- Sick leave: 10 days per year (requires notification before 10 AM same day)
- Public holidays: As per local jurisdiction
- Requesting leave: Submit in tasks_database 5+ days in advance for planned leave
- Carry-forward: Max 5 days per calendar year

### Code of Conduct

- Treat every colleague, client, and partner with respect
- No disclosure of confidential business information, client names, or financials externally
- Conflicts of interest must be declared to the CEO in writing
- All work outputs remain the property of Nivy
- Violations escalate: verbal warning → written warning → termination

### Performance Appraisal

- Cadence: Quarterly review + annual appraisal
- Format: Self-assessment + manager assessment + KPI review
- Outcomes: salary adjustment, promotion, improvement plan, or exit
- Documented in: reports_database (Report Type = Appraisal)

### Onboarding Checklist (Days 1–7)

See Universal Training Hub → Day-by-Day Track below.

---

## 💵 3. Group Finance & Legal

Applies to: All brands sharing group-level financial and legal standards.

### Expense Reimbursement Standards

- Pre-approved expenses: software tools, travel, client meals (with receipts)
- Approval required above £50 / $50 / AED 200 per item
- Submit via company_documents_database within 7 days of expense
- No personal expenses reimbursed

### NDA Template (Standard)

All client engagements, partnerships, and VA onboardings require a signed NDA before any sensitive information is shared. Template stored in: templates_database (Use Case = Legal).

### Audit Policy

- Internal audit: quarterly review of all financial records by CFO/Finance lead
- External audit: annual, by certified accountant
- Audit records stored in: company_documents_database (Type = Audit)

### Compliance Standards

- UK: GDPR compliance for all client data
- UAE: Data protection as per UAE Federal Decree-Law No. 45 of 2021
- US / AUS / Canada: Local data protection laws apply (see Nivy Advisory for jurisdiction-specific guidance)

---

## 🤝 4. Partner Ecosystem Hub

Applies to: All brands using freelancers, sales partners, alliance partners, or franchise models.

> **This consolidates the 10+ overlapping Freelancer and Partner pages previously scattered across the workspace into one structured hub.**
> 

### 4A — Freelancer Program

- **Purpose:** Hire and manage freelance contractors for delivery tasks
- **Intake:** Application → Portfolio review → Test task → Contract + NDA → Onboarding
- **SOPs:** See sop_database (Function = Delivery, Brand = Global)
- **Rates:** Documented per role type in templates_database (Use Case = HR)
- **Management:** Weekly check-in, output log in tasks_database
- **Offboarding:** Output handover → system access revoked → final payment within 14 days

### 4B — Sales Partner Program

- **Purpose:** Commission-based referral and reseller partners
- **Tiers:** L1 Referral (5–10% one-time) | L2 Reseller (15–20% recurring) | L3 Strategic (custom)
- **Intake:** Application → Fit call → Partner Agreement + NDA → Onboarding kit
- **Tracking:** clients_database (Source = Sales Partner) | reports_database (Type = Partner Report)
- **SOPs:** See sop_database (Function = Sales, Brand = Global)

### 4C — Alliance Framework (Nivy Alliance)

- **Purpose:** Strategic B2B partnerships between Nivy brands and external organisations
- **Scope:** Joint ventures, co-marketing, referral agreements, white-labelling
- **Process:** Opportunity identified → Due diligence → MOU → Pilot → Full agreement
- **Legal:** All agreements go through company_documents_database

### 4D — Franchise Framework (Nivy Next)

- **Purpose:** Enable third parties to operate under the Nivy Next brand
- **Requirements:** Capital, territory, training completion, quality standards met
- **Onboarding:** Franchise agreement → Training program → Systems access → Soft launch → Full launch
- **Quality control:** Monthly QC review, KPI tracking, bi-annual audit

---

## 🤖 5. Automation Workflows (Global Automation Map)

> **Status:** Planning document — 0% built. This map defines every automation needed across all brands. Build order: Phase 9.
> 

| Automation | Tool | Trigger | Action | Priority |
| --- | --- | --- | --- | --- |
| Task status → QC update | Notion Native | Task Status = Done | Set QC Status = Pending | High |
| SOP needs review | Notion Native | SOP Status = Needs Review | Notify owner | High |
| KPI below threshold | Notion Native | Alert checkbox = checked | Notify manager | High |
| Form → Task | [Make.com](http://Make.com) | Website form submitted | Create task in tasks_database | High |
| ChatGPT chat saved | [Make.com](http://Make.com) | New entry in ChatGPT DB | Add to Research Inbox | Medium |
| Weekly review task | [Make.com](http://Make.com) | Every Monday 9 AM | Create review task per dept head | Medium |
| KPI below threshold | [Make.com](http://Make.com) | Notion webhook | Slack/email alert | Medium |
| Lead follow-up | [Make.com](http://Make.com) | Outreach Log = No Response Day 3 | Queue follow-up task | Medium |

---

## 📋 6. Client Acquisition System

Applies to: Nivy Next, Nivy Advisory, Nivy Jobs, Nivy Nexus

**Stage flow:**

```
Awareness → Lead Captured → Qualified → Proposal Sent → Negotiation → Won/Lost → Onboarded
```

- **Lead Capture:** Website form, LinkedIn DM, cold email, referral, directory listing
- **Qualification criteria:** ICP match (industry, size, region, budget, timeline, pain point)
- **Proposal:** Template in templates_database (Use Case = Proposals)
- **CRM:** All leads in clients_database | Deal stages in HubSpot
- **Onboarding:** Signed agreement → NDA → Kick-off call → Project setup in projects_database

---

> 🤖 Built by Claude (Anthropic) | Phase 5 — May 18, 2026
> 

[🧰 Global Tools Index — All Brands (Filterable by Brand / Dept / Function)](%F0%9F%A7%B0%20Global%20Tools%20Index%20%E2%80%94%20All%20Brands%20(Filterable%20by%20B%20363eb94b1a2a81bf830fd70d4f6465cd.md)

[⚡ Phase 9 — Automation & Self-Sustaining Systems (Master Hub)](%E2%9A%A1%20Phase%209%20%E2%80%94%20Automation%20&%20Self-Sustaining%20Systems%20(%20363eb94b1a2a81cdaab9f5a8fd63452e.md)