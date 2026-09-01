# Implementation Plan — Automated Online Profile Publishing

**Goal for this plan:** take the approved Master Profile in `company-profile/` and get it
published/kept-in-sync across Nivy Next's online profiles (social platforms, directories,
Google Business Profile, etc.) with minimal manual re-typing — using official APIs where
they exist, and a clearly-labeled manual queue everywhere they don't.

This is a **subset** of the full MASTER COMMAND (that doc covers SEO, GEO, content
marketing, dashboards, etc. too) narrowed to the one workflow you asked for right now:
*"automate the process of uploading data to online profiles."* Phases below map onto
MASTER COMMAND phases 4, 6, 7, 8, 9, and the relevant slice of 13 — reordered and scoped
around this single goal so it's buildable incrementally and each phase ships something
you can actually use.

Everything is built against files already in `nivy-company-os.zip` — this plan doesn't
start from zero.

---

## Phase 0 — Prerequisites (blocking everyone below)

Nothing in Phase 1+ can move without these. This is the honest bottleneck.

| # | What's needed | Why it blocks everything |
|---|---|---|
| 0.1 | A real GitHub repository (existing or new) to hold this code, with a URL you give me | Source-of-truth webhook has nowhere to point without it |
| 0.2 | Where this will run — your own server / VM / cloud account for Docker (Postgres, n8n, Ollama, the API service) | I can write all the config; I can't host it |
| 0.3 | Corrected `company-profile/` data — at minimum: legal entity name, real phone number, confirmed social handles, confirmed HQ address | Publishing placeholder/`needs_review` data to real profiles is the one thing this whole system is designed to prevent |
| 0.4 | A decision, per platform, on **who owns the account** (which email/login created each profile) | API credential setup requires being logged into the actual account |

**You don't have to solve all of 0.1–0.4 before I start building** — Phase 1 (below) is
pure file/schema/code work I can do right now without them. But nothing actually *publishes
to a real profile* until 0.1–0.4 are in place.

---

## Phase 1 — Platform Profile Generator (no publishing yet, just correct drafts)
*Status: buildable now, no external dependencies.*

Turn the approved Master Profile into platform-correct drafts — right length, right
format, right fields — for every platform in `docs/platform-matrix.md`. Nothing gets sent
anywhere yet; this phase produces reviewable text.

- [ ] `ai/profile-generator/` — code that reads `company-profile/*.yaml`, applies the
      Ollama prompt pattern from `ai/prompts/profile-adaptation.md`, and outputs one draft
      per platform per field (bio, headline, about, tagline, CTA) respecting each
      platform's character limit
- [ ] Store drafts in the `platform_profiles` / `platform_profile_fields` tables (schema
      already exists in `database/schema.sql`)
- [ ] `profile-completeness` scoring (per §24 of the master command): % of required fields
      filled per platform
- [ ] Output: a reviewable report (markdown or simple web page) showing, per platform,
      every proposed field value side-by-side with the source fact it came from

**Deliverable at end of Phase 1:** you can see exactly what would be typed into LinkedIn,
Instagram, Google Business Profile, etc. — before anything is sent anywhere.

---

## Phase 2 — Approval Queue
*Status: buildable now, no external dependencies.*

Every generated draft needs a gate before publishing (Rule 7: human approval required for
important factual changes).

- [ ] `approval_requests` table (already in schema) wired to a simple review UI or even a
      generated markdown/CSV checklist to start
- [ ] Status flow: `DRAFT → VALIDATION → APPROVAL_REQUIRED → APPROVED → PUBLISHED`
- [ ] Default every platform to `APPROVAL_REQUIRED` (no silent auto-publish) until you
      explicitly mark specific low-risk platforms/fields as `AUTO`
- [ ] `DRY_RUN=true` by default (already in `.env.example`) — Phase 3+ never actually
      writes to a live platform while this is on

**Deliverable:** a queue you can approve/reject drafts from, one platform/field at a time.

---

## Phase 3 — Manual Action Queue (covers every platform with no API)
*Status: buildable now.*

Per `docs/platform-matrix.md`, a large chunk of target platforms (most business
directories: Clutch, GoodFirms, Yelp, BBB, Crunchbase, etc.) have **no write API** — they
require manual claim-and-edit through their own portal.

- [ ] `manual_actions` table (already in schema) — auto-create one task per
      `MANUAL_ONLY` platform whenever the Master Profile changes in a way that affects it
- [ ] Each task includes: platform, exact field(s) that changed, the new approved value to
      paste in, and a link to that platform's edit page
- [ ] Dashboard view (even a simple filtered list to start) clearly labeled **"MANUAL
      ACTION REQUIRED"** — never silently marked done

**Deliverable:** instead of automation quietly failing on non-API platforms, you get a
checklist telling you exactly what to copy-paste where.

---

## Phase 4 — First Real API Integrations (start with 2–3 platforms, not all 15+)
*Status: blocked on Phase 0.2 (hosting) + 0.4 (account ownership) + real OAuth app registration.*

Rather than building all API adapters from §27 at once, pick the platforms that matter
most for Nivy Next first. Suggested order, based on what's actually official/stable per
`docs/platform-matrix.md`:

1. **Google Business Profile** — most business-critical for local SEO, has an official API
2. **LinkedIn Company Page** — primary B2B channel, but access is approval-gated; register
   the app and apply early since approval can take time
3. **Facebook Page / Instagram Business** (via Meta Graph API) — single OAuth covers both

For each platform:
- [ ] Register a developer app under Nivy Next's own account (needs you, not me — I can
      walk you through it once we're here)
- [ ] Store credentials via env vars / Docker secrets — never in code (per Rule: never
      hardcode credentials)
- [ ] Implement the standard adapter interface already defined in the master command:
      `authenticate()`, `getProfile()`, `updateProfile()`, `publish()`, `getAnalytics()`,
      `verify()` — only the methods that platform's API actually supports
- [ ] `integrations/google/`, `integrations/linkedin/`, `integrations/meta/` — scaffolded
      folders already exist, need real code here

**Deliverable:** approving a draft in Phase 2's queue for one of these 3 platforms actually
updates the live profile, with a `verify()` step confirming it stuck.

---

## Phase 5 — n8n Orchestration (wire Phases 1–4 into one flow)
*Status: blocked on Phase 0.1/0.2 (repo + hosting).*

The `github_profile_webhook.json` skeleton already exists. This phase makes the whole
pipeline automatic end-to-end:

- [ ] `github_profile_sync.json` — full webhook → validate → parse → Postgres sync
- [ ] `profile_change_detector.json` — diff old vs new profile, list only the platforms
      actually affected by what changed (per §25: "do not unnecessarily modify unrelated
      profiles")
- [ ] `platform_profile_generator.json` — triggers Phase 1's generator only for affected
      platforms
- [ ] `approval_queue.json` — routes drafts into Phase 2's queue
- [ ] `platform_api_sync.json` — on approval, calls the Phase 4 adapters
- [ ] `manual_action_queue.json` — on approval, creates Phase 3 tasks for non-API platforms
- [ ] `error_retry.json`, `platform_health_check.json` — basic resilience

**Deliverable:** you edit `company-profile/master-profile.md`, commit, and (after your own
approval click) the change flows out to every live profile it affects — automatically for
API platforms, as a checklist for manual ones.

---

## Phase 6 — Expand Platform Coverage
*Status: incremental, add platforms one at a time as Phase 4's pattern is proven.*

Once the pipeline works end-to-end for 2–3 platforms, extend `integrations/` to the rest
of the platforms marked `OFFICIAL_API` in `docs/platform-matrix.md` — X/Twitter, YouTube,
Pinterest, Reddit, WordPress, etc. — in whatever order matters most to you. Each one
follows the exact same adapter pattern from Phase 4, so this is mostly repetition, not new
design work.

---

## Phase 7 — Consistency & Reporting
*Status: after Phase 5 is live.*

- [ ] `nap_consistency.json` — Name/Address/Phone consistency check across every connected
      platform, flags mismatches
- [ ] `profile_completeness.json` scheduled run + dashboard
- [ ] Weekly "platform health" and "profile completeness" reports
- [ ] `rollback` support: if a GitHub commit is reverted, the same pipeline detects it and
      generates reversal drafts (through the same approval queue, never auto-applied)

---

## What I can start on right now, today, without anything from you

Phases **1, 2, and 3** need no external accounts, no hosting, and no repo URL — they're
pure code/schema/prompt work against the files already in `nivy-company-os.zip`. If you
say go, I'll start there next: build the profile-generator code, the approval-queue schema
wiring, and the manual-action auto-creation logic.

Everything from **Phase 4 onward** needs Phase 0 resolved first — specifically, I'll need
you to tell me which platforms to prioritize and confirm you (not me) will handle the
actual developer-app registrations, since those require being logged into Nivy Next's own
accounts.

## Suggested immediate next step
Tell me:
1. Should I start Phase 1 (profile draft generator) now?
2. Which 2–3 platforms matter most for Phase 4, once we get there — Google Business
   Profile, LinkedIn, and Meta are my default guess based on what's in your profile data,
   but confirm or correct that.
