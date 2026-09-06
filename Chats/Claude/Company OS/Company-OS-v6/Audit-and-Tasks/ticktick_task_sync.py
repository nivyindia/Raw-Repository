"""
ticktick_task_sync.py
======================
Company OS -> TickTick task publisher.

Kya karta hai:
1. Tasks ko extract karta hai ek source se (is script mein 3 source options diye hain:
   markdown checklist file, GitHub Issues, ya seedha ek Python list/JSON).
2. Har task ke liye TickTick mein ek naya task banata hai — title, project,
   due date, priority, aur reminder (before due date) ke saath.
3. TickTick ki official Open API (OAuth2) use karta hai, isliye ChatGPT Custom GPT
   ke "Actions" feature mein bhi isi API schema se plug kiya ja sakta hai
   (neeche "ChatGPT Custom GPT setup" section dekho).

Setup (one-time):
1. https://developer.ticktick.com par jaake ek app register karo -> Client ID
   aur Client Secret milega. Redirect URI kuch bhi de sakte ho (e.g. http://localhost:8080/callback).
2. `pip install requests`
3. Neeche CONFIG section mein CLIENT_ID / CLIENT_SECRET daal do.
4. Pehli baar script run karoge to browser khulega -> TickTick login -> authorize
   -> access token mil jayega aur `ticktick_token.json` mein save ho jayega
   (agli baar dobara login nahi maangega jab tak token expire na ho).

Task source formats supported:
  A) Markdown checklist  (recommended for Company OS audit-derived tasks)
     - [ ] Fix cleanup-after-merge.yml reference | due: 2026-08-31 | priority: high
     - [ ] Set up 02_PROJECTS board                | due: 2026-08-28 | priority: high
  B) GitHub Issues (open issues in a repo become tasks automatically)
  C) Plain Python list of dicts (programmatic use)
"""

import json
import os
import re
import time
import webbrowser
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlencode, urlparse, parse_qs

import requests

# ============================== CONFIG ===============================

CLIENT_ID = "YOUR_TICKTICK_CLIENT_ID"
CLIENT_SECRET = "YOUR_TICKTICK_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8080/callback"
TOKEN_FILE = "ticktick_token.json"

# TickTick project (list) jisme tasks create honge. Blank chhod do (None) to use
# Inbox, ya TickTick app se project ID copy karke yahan daal do.
TARGET_PROJECT_ID = None

# Default reminder: due date se kitni der pehle alert aaye
DEFAULT_REMINDER_BEFORE_MINUTES = 60  # 1 hour before

# Priority mapping (TickTick codes: 0=None, 1=Low, 3=Medium, 5=High)
PRIORITY_MAP = {"none": 0, "low": 1, "medium": 3, "high": 5}

AUTH_URL = "https://ticktick.com/oauth/authorize"
TOKEN_URL = "https://ticktick.com/oauth/token"
API_BASE = "https://api.ticktick.com/open/v1"

# ============================ OAUTH FLOW ==============================


class _CallbackHandler(BaseHTTPRequestHandler):
    """Ek chhota local server jo TickTick ke redirect se 'code' pakadta hai."""

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        self.server.auth_code = query.get("code", [None])[0]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h2>Authorized. Ye tab band kar sakte ho.</h2>")

    def log_message(self, *args):
        pass  # console spam mat karo


def _get_auth_code():
    params = {
        "client_id": CLIENT_ID,
        "scope": "tasks:write tasks:read",
        "state": "companyos",
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
    }
    url = f"{AUTH_URL}?{urlencode(params)}"
    print(f"Browser mein authorize karo: {url}")
    webbrowser.open(url)

    server = HTTPServer(("localhost", 8080), _CallbackHandler)
    server.handle_request()  # ek hi request ke baad ruk jayega
    return server.auth_code


def _fetch_token(auth_code):
    resp = requests.post(
        TOKEN_URL,
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
        },
    )
    resp.raise_for_status()
    return resp.json()


def get_access_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            token_data = json.load(f)
        # Note: TickTick access tokens are long-lived; agar expire ho jaye to
        # ye file delete karke script dobara chalao, naya login flow start hoga.
        return token_data["access_token"]

    code = _get_auth_code()
    if not code:
        raise RuntimeError("Authorization fail hui — auth code nahi mila.")
    token_data = _fetch_token(code)
    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f)
    return token_data["access_token"]


# ============================ TASK EXTRACTION ==========================


def extract_tasks_from_markdown(filepath):
    """
    Parse karta hai markdown checklist lines jaise:
    - [ ] Task title | due: YYYY-MM-DD | priority: high
    `due:` aur `priority:` optional hain.
    """
    tasks = []
    line_re = re.compile(r"^\s*-\s*\[ \]\s*(.+)$")
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            m = line_re.match(line)
            if not m:
                continue
            body = m.group(1)
            parts = [p.strip() for p in body.split("|")]
            title = parts[0]
            due = None
            priority = "medium"
            for p in parts[1:]:
                if p.lower().startswith("due:"):
                    due = p.split(":", 1)[1].strip()
                elif p.lower().startswith("priority:"):
                    priority = p.split(":", 1)[1].strip().lower()
            tasks.append({"title": title, "due": due, "priority": priority})
    return tasks


def extract_tasks_from_github_issues(repo, github_token, state="open"):
    """
    repo format: 'owner/repo'. Har open GitHub Issue ek task ban jata hai.
    Issue body mein agar 'Due: YYYY-MM-DD' likha hai to wo due date use hoga,
    warna default (7 din baad) set hoga.
    """
    headers = {"Authorization": f"token {github_token}"}
    url = f"https://api.github.com/repos/{repo}/issues"
    resp = requests.get(url, headers=headers, params={"state": state})
    resp.raise_for_status()
    tasks = []
    for issue in resp.json():
        if "pull_request" in issue:
            continue  # PRs skip
        body = issue.get("body") or ""
        due_match = re.search(r"Due:\s*(\d{4}-\d{2}-\d{2})", body)
        due = due_match.group(1) if due_match else None
        labels = [l["name"].lower() for l in issue.get("labels", [])]
        priority = "high" if "priority:high" in labels else "medium"
        tasks.append({"title": issue["title"], "due": due, "priority": priority})
    return tasks


# ============================ TICKTICK PUBLISH =========================


def _to_ticktick_datetime(date_str):
    """'2026-08-31' -> TickTick ISO format with default time 18:00 local."""
    if not date_str:
        # date nahi di gayi to default: 7 din baad
        dt = datetime.now() + timedelta(days=7)
    else:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        dt = dt.replace(hour=18, minute=0)
    return dt.strftime("%Y-%m-%dT%H:%M:%S+0000")


def create_ticktick_task(access_token, title, due=None, priority="medium",
                          reminder_minutes_before=DEFAULT_REMINDER_BEFORE_MINUTES,
                          project_id=TARGET_PROJECT_ID):
    due_dt = _to_ticktick_datetime(due)
    payload = {
        "title": title,
        "dueDate": due_dt,
        "priority": PRIORITY_MAP.get(priority, 3),
        "reminders": [f"TRIGGER:-PT{reminder_minutes_before}M"],
        "timeZone": "Asia/Kolkata",
    }
    if project_id:
        payload["projectId"] = project_id

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    resp = requests.post(f"{API_BASE}/task", headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()


def publish_tasks(tasks):
    token = get_access_token()
    results = []
    for t in tasks:
        try:
            created = create_ticktick_task(
                token, t["title"], due=t.get("due"), priority=t.get("priority", "medium")
            )
            print(f"✅ Created: {t['title']}  (due {t.get('due') or 'in 7 days'})")
            results.append(created)
        except requests.HTTPError as e:
            print(f"❌ Failed: {t['title']} — {e}")
        time.sleep(0.3)  # rate-limit ke liye halka sa gap
    return results


# =================================== MAIN ===============================

if __name__ == "__main__":
    # Option A: markdown checklist se (Company_OS_Task_List.md jaisi file banao,
    # is audit ke "Priority Ranking" section ko checklist format mein convert karke)
    tasks = extract_tasks_from_markdown("Company_OS_Task_List.md")

    # Option B: GitHub Issues se (agar 02_PROJECTS ki jagah GitHub Issues use kar rahe ho)
    # tasks = extract_tasks_from_github_issues("your-org/Company-OS", "ghp_xxx")

    # Option C: seedha hardcode / kisi aur script se pass karo
    # tasks = [{"title": "Fix cleanup-after-merge.yml", "due": "2026-08-31", "priority": "high"}]

    publish_tasks(tasks)
