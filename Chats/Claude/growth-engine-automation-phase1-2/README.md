# Nivy Automated Funnel — n8n Workflows

Ye folder poore funnel ke ab tak ke **importable n8n workflows** rakhta hai — plan document (`n8n-Automated-Funnel-Plan.md`) ka implementation.

## Phase 1 — Marketing Engine (Traffic → Qualified Lead)

| Module | Folder | Status |
|---|---|---|
| 1.1 — Content → Social Factory | `growth-engine-automation/phase-1/1.1-content-social-factory/` | ✅ Built (import + configure ready) |
| 1.2 — SEO Automation (Weekly) | `growth-engine-automation/phase-1/1.2-seo-automation/` | ✅ Built (import + configure ready) |
| 1.3 — Website Lead Capture | `growth-engine-automation/phase-1/1.3-website-lead-capture/` | ✅ Built (import + configure ready) |
| 1.4 — Inbound Form Qualification | `growth-engine-automation/phase-1/1.4-inbound-form-qualification/` | ✅ Built (import + configure ready) |
| 1.5 — Central CRM Sync | `growth-engine-automation/phase-1/1.5-central-crm-sync/` | ✅ Built (import + configure ready) |

Phase 1 (1.1 → 1.5) **complete** hai.

## Phase 2 — Sales + Delivery Engine (Lead → Paying Client → Delivery)

| Module | Folder | Status |
|---|---|---|
| 2.1 — Multi-channel Outreach | `growth-engine-automation/phase-2/2.1-multichannel-outreach/` | ✅ Built (import + configure ready) |
| 2.2 — Nurture Sequence | `growth-engine-automation/phase-2/2.2-nurture-sequence/` | ✅ Built (import + configure ready) |
| 2.3 — Booking Sync | *(agla batch)* | ⬜ Not started |
| 2.4 — Proposal Generation | *(agla batch)* | ⬜ Not started |
| 2.5 — Contract + E-sign | *(agla batch)* | ⬜ Not started |
| 2.6 — Invoice + Payment | *(agla batch)* | ⬜ Not started |
| 2.7 — Client Onboarding | *(agla batch)* | ⬜ Not started |
| 2.8 — Delivery + Reporting | *(agla batch)* | ⬜ Not started |
| 2.9 — Renewal + Revenue Ops | *(agla batch)* | ⬜ Not started |

**Zaroori:** Module 2.1 import karne ke baad uska workflow ID copy karke `1.5-central-crm-sync/workflow.json` ke `Execute Workflow - 2.1 Outreach` node me daalo, taaki Phase 1 → Phase 2 ka connection actually live ho jaaye (Master Plan Section 5.2).

## Common Setup (sabhi modules ke liye zaroori)

Sab modules 2 cheezein share karte hain — pehle inhe ek baar setup kar lo:

### 1. n8n me Postgres credential banao
- **Credentials → New → Postgres**
- Odoo instance ki database ke connection details daalo (Host, Port, Database name, User, Password)
- Name: `Odoo Postgres` (sab workflows me isi naam se reference hai)

### 2. `clients_master` control table banao (ek baar, Postgres par)
```sql
CREATE TABLE clients_master (
  id SERIAL PRIMARY KEY,
  odoo_lead_id INTEGER UNIQUE,
  name TEXT,
  email TEXT,
  phone TEXT,
  company TEXT,
  service_type TEXT,
  intent_summary TEXT,
  urgency TEXT,
  score TEXT,
  score_reason TEXT,
  source TEXT,
  status TEXT DEFAULT 'New',
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);
```
Ye Master Plan ke Section 5.1 wala central sync table hai — Module 1.3, 1.4, aur 1.5 sab isi ko read/write karte hain.

### 3. Ollama server chalu rakho
```bash
ollama serve
ollama pull qwen2.5:7b
```
Sab workflows `http://localhost:11434` assume karte hain — agar Ollama alag machine/container par hai to har workflow ke HTTP nodes me URL update karna hoga.

### 4. Odoo API access (Modules 1.3, 1.4, 1.5 ke liye)
n8n → Settings → Variables me ye set karo:

| Variable | Kya daalna hai |
|---|---|
| `ODOO_URL` | Odoo instance ka base URL |
| `ODOO_DB` | Odoo database ka naam |
| `ODOO_UID` | API user ka internal user ID |
| `ODOO_API_KEY` | Odoo → Settings → Users → API Key |
| `ODOO_DISCUSS_CHANNEL_ID` | Sales team ke Discuss channel ID |
| `ODOO_LINKEDIN_ACTIVITY_TYPE_ID` | Odoo Activity Type ID (Module 2.1 ke LinkedIn task ke liye) |
| `ODOO_SALES_USER_ID` | Sales rep ka Odoo user ID (Module 2.1 ke LinkedIn task assignee) |
| `WAHA_URL`, `WAHA_API_KEY`, `WAHA_SESSION` | Waha WhatsApp gateway details (Module 2.1, 2.2 ke liye) |

## Import Order

1. `1.1-content-social-factory/workflow.json` — import, README follow karo, test karo
2. `1.2-seo-automation/workflow.json` — import, README follow karo, test karo
3. `1.3-website-lead-capture/workflow.json` — import, Typebot webhook connect karo, test karo
4. `1.4-inbound-form-qualification/workflow.json` — import, Odoo Automation Rule connect karo, test karo
5. `2.1-multichannel-outreach/workflow.json` — import, credentials set karo, workflow ID copy karo
6. `2.2-nurture-sequence/workflow.json` — import, README follow karo, test karo
7. `1.5-central-crm-sync/workflow.json` — sabse last import karo — ab is workflow ke `Execute Workflow - 2.1 Outreach` node me Step 5 ka workflow ID daal do (2.5/2.7 abhi disabled rehne do, wo agle batch me banenge)

Har module ke apne folder me detailed README hai (credentials, placeholders, test steps, known limitations).

## Master Plan File

Poora funnel plan, tool stack, aur progress tracker `n8n-Automated-Funnel-Plan.md` me hai — us file ke Section 9 me progress tracker update kiya gaya hai (1.1–1.5 sab ✅ Done).
