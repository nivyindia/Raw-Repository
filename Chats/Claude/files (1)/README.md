# Phase 1 — Marketing Engine (n8n Workflows)

Ye folder Phase 1 ke actual **importable n8n workflows** rakhta hai — plan document (`n8n-Automated-Funnel-Plan.md`) ka implementation.

| Module | Folder | Status |
|---|---|---|
| 1.1 — Content → Social Factory | `1.1-content-social-factory/` | ✅ Built (import + configure ready) |
| 1.2 — SEO Automation (Weekly) | `1.2-seo-automation/` | ✅ Built (import + configure ready) |
| 1.3 — Website Lead Capture | *(agla batch)* | ⬜ Not started |
| 1.4 — Inbound Form Qualification | *(agla batch)* | ⬜ Not started |
| 1.5 — Central CRM Sync | *(agla batch)* | ⬜ Not started |

## Common Setup (dono modules ke liye zaroori)

Dono modules 2 cheezein share karte hain — pehle inhe ek baar setup kar lo:

### 1. n8n me Postgres credential banao
- **Credentials → New → Postgres**
- Odoo instance ki database ke connection details daalo (Host, Port, Database name, User, Password)
- Name: `Odoo Postgres` (dono workflows me isi naam se reference hai)

### 2. Ollama server chalu rakho
```bash
ollama serve
ollama pull qwen2.5:7b
```
Dono workflows `http://localhost:11434` assume karte hain — agar Ollama alag machine/container par hai to workflow ke HTTP nodes me URL update karna hoga.

## Import Order

1. Pehle `1.1-content-social-factory/workflow.json` import karo, uska README follow karke configure karo, test karo
2. Phir `1.2-seo-automation/workflow.json` import karo, uska README follow karke configure karo, test karo

Har module ke apne folder me detailed README hai (credentials, placeholders, test steps, known limitations).

## Master Plan File

Poora funnel plan, tool stack, aur progress tracker `n8n-Automated-Funnel-Plan.md` me hai — us file ke Section 9 me progress tracker update karte rehna jaise-jaise modules complete hote jaayein.
