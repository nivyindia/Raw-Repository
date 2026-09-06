# PC pe kya install karna hai — Step by Step Guide

## Sabse pehle: Docker Desktop (yeh sabse zaroori hai)

Docker ek "container" system hai jo har software ko apne alag box mein chalata hai —
isse tumhe Postgres, n8n, Odoo waghera manually install nahi karne padenge, sab ek
saath ek command se start ho jayenge.

**Windows pe:**
1. https://www.docker.com/products/docker-desktop se Docker Desktop download karo.
2. Installer chalao, restart maango to restart kar do.
3. Docker Desktop open karo, sign-in skip kar sakte ho (free hai).
4. WSL2 maangega agar pehle se nahi hai — installer khud guide karega.

**Mac pe:** Same link se Mac version download, drag-drop Applications mein, open karo.

**Linux pe:**
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# phir logout/login karo
```

Check karo Docker install ho gaya:
```bash
docker --version
docker compose version
```

---

## Step 2: Is folder ki 2 files ek jagah rakho

- `docker-compose.yml` (isi zip mein hai)
- `schema.sql` (pichli zip mein diya tha — same folder mein copy kar lo)

Dono ek hi folder mein hone chahiye, kyunki compose file `schema.sql` ko automatically
leads database mein load karegi.

---

## Step 3: Sab services ek command se start karo

Terminal/PowerShell us folder mein khol ke:

```bash
docker compose up -d
```

Yeh pehli baar 5-10 minute lega (images download honge). Uske baad ye sab chalu ho
jayega:

| Software | Kahan khulega | Kis liye |
|---|---|---|
| n8n | http://localhost:5678 | Workflow banane/chalane ke liye |
| Odoo | http://localhost:8069 | CRM (leads, deals) |
| Postgres (leads db) | localhost:5432 | Dedupe, lost deals, onboarding data |
| Gotenberg | http://localhost:3000 | Proposal PDF banane ke liye |
| Reacher | http://localhost:8085 | Email verify karne ke liye |

Check karo sab chal rahe hain:
```bash
docker compose ps
```

Band karna ho to:
```bash
docker compose down
```

---

## Step 4: Odoo first-time setup

1. http://localhost:8069 kholo.
2. Pehli baar database create karega — koi bhi naam do (e.g. `growth`), admin
   email/password set karo.
3. Apps menu se **CRM** app install karo.
4. Settings → Technical mode on karo, phir Studio se `x_studio_score_tier` aur
   `x_studio_decision_makers` fields `crm.lead` model pe banao (jaise pehle bataya tha).

---

## Step 5: n8n first-time setup

1. http://localhost:5678 kholo — pehli baar owner account banayega (email/password).
2. Settings → Environment Variables mein saare `ODOO_URL`, `APOLLO_API_KEY` waghera
   daal do (poori list `DEPLOYMENT.md` mein hai).
3. Zip ki workflow JSON files import karo (Workflows → Import from File).
4. Credentials attach karo — Postgres credential ke liye host `leads-db`, port `5432`,
   user `leads_user`, password wahi jo compose file mein daala tha.

---

## In software ke alawa, in cheezon ka bhi intezaam karna hoga (Docker se nahi milega)

Ye services aise nahi hain jo tumhare PC pe local chal sakein achhe se — inke liye
cloud/hosted version lena zyada aasaan hai:

| Cheez | Kya karo |
|---|---|
| **Apollo.io** | Website pe account banao, API key lo — ye ek paid/freemium SaaS hai, self-host nahi hota. |
| **Cal.com** | Free plan pe cloud version use karo (https://cal.com) — self-host bhi ho sakta hai par zaroori nahi, cloud simple hai. |
| **Mattermost/Slack webhook** | Slack use kar rahe ho to free "Incoming Webhook" bana lo (koi install nahi chahiye). Mattermost chahiye to alag se self-host karna padega — shuru mein Slack easier hai. |
| **SMTP (email bhejne ke liye)** | Gmail App Password use kar sakte ho shuru mein, ya koi bhi SMTP provider (Zoho, Brevo, etc.) ka free tier. |
| **Scraper microservice** | Ye khud ka Node.js + Playwright service hai jo tumhe likhna/host karna padega — ye readymade software nahi hai, custom code hai. Shuru mein isse skip bhi kar sakte ho aur sirf webhook-based lead capture use kar sakte ho. |
| **Ollama (optional, AI scoring/email ke liye)** | https://ollama.com se installer download karo apne OS ke liye, phir `ollama pull llama3` jaisa model chala lo. Yeh optional hai — bina AI ke bhi rule-based scoring already kaam karta hai. |

---

## Priority order — kya pehle install karo

Agar sab ek saath overwhelming lag raha hai, is order mein karo:

1. **Docker Desktop** — sabse pehle, baaki sab isi pe depend karta hai.
2. **docker compose up -d** — n8n + Postgres + Odoo + Gotenberg + Reacher ek saath aa
   jayenge.
3. **n8n mein workflow import** + Postgres credential attach — taaki dedupe/logging
   test kar sako.
4. **Odoo setup** — CRM app + custom fields.
5. Baaki (Apollo key, SMTP, Cal.com) — jab tak inn ka setup na ho, sirf unn nodes ko
   test mat karo, baaki sab already chalu rahega.

Koi bhi ek step pe atak jao to bata dena, saath mein karte hain.
