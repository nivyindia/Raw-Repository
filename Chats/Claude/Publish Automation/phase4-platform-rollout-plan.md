# Phase 4 — Platform Rollout Plan (Sub-Stages)

Scope: `integrations/<platform>/` adapters implementing the standard
`authenticate / getProfile / updateProfile / publish / getAnalytics / verify` interface,
per `implementation-plan-profile-publishing.md` Phase 4. This breaks that single phase
into buildable batches of 2–3 platforms, pulled from the **Social Platforms** table in
`docs/platform-matrix.md` (plus the closely-related Video Platforms row for YouTube).

Each batch is built the same way as Batch 1: real adapter code against confirmed current
API behavior, an honest `PlatformCapabilityError` wherever a platform's API genuinely
can't do something (never a fabricated endpoint), a one-time OAuth helper script, and a
setup README. Still blocked on Phase 0 (hosting + real credentials + your account logins)
regardless of batch — every batch ships code that *can* run, not something already
running.

Grouped by how similar the integration work is, not alphabetically — platforms in the
same batch share an auth pattern or a access-approval profile, so building them together
is genuinely less work than building them separately.

---

## Batch 1 — Highest business priority, single-OAuth-covers-two ✅ DONE

| Platform | Adapter built | `updateProfile()` | `publish()` | Notes |
|---|---|---|---|---|
| [x] Google Business Profile | ✅ | ✅ 4 fields | ❌ (Local Posts out of scope) | Business Information + Performance API |
| [x] LinkedIn (Company Page) | ✅ | ❌ throws on purpose | ✅ | Profile-field writes need MDP partner access, not built |
| [x] Facebook Page | ✅ | ✅ | ✅ | via Meta adapter |
| [x] Instagram (Business) | ✅ | ❌ throws on purpose (no bio write endpoint exists) | ✅ (2-step media flow) | via Meta adapter, same OAuth app as Facebook |

Delivered in `nivy-company-os-phase4-batch1.zip`. Each has `integrations/<platform>/{adapter.js, oauth.js, README.md, package.json}`.

---

## Batch 2 — Straightforward official APIs, no lengthy partner review

Picked together because none of these three require the kind of drawn-out
partnership/case-by-case approval LinkedIn's profile-write access does — standard
developer-portal app registration is enough to get posting + read access.

- [ ] **X / Twitter** — X API v2. Free tier is heavily rate-limited; re-verify current
      paid-tier pricing before assuming a given call volume is affordable. Bio/profile
      fields have partial API coverage — confirm exact writable fields before building
      `updateProfile()`, don't assume parity with posting access.
- [ ] **YouTube** — YouTube Data API v3, via Google Cloud Console (same account you'll
      already have set up for Google Business Profile in Batch 1 — some credential reuse
      possible, but scopes are separate). Channel branding/description is confirmed
      writable via API.
- [ ] **Pinterest** — Pinterest API. Confirmed profile update + publish support per the
      platform matrix; standard app review, no special partner tier known.

---

## Batch 3 — Different automation paradigm (bots/communities, not "profiles")

These three don't map cleanly onto the six-method adapter interface — a Telegram
channel or Discord server isn't a "brand profile" the way a Facebook Page is. Grouping
them together so the interface deviation is handled once, consistently, rather than
improvised per-platform.

- [ ] **Reddit** — Reddit API, OAuth. Automation must respect individual subreddit rules
      on top of Reddit's own API terms — this adapter will need a per-subreddit
      allow-list, not just a global on/off switch. Commercial API pricing changed in
      2023; re-verify current terms before relying on free-tier access.
- [ ] **Telegram** — Bot API, bot tokens (not OAuth). `getProfile`/`updateProfile` don't
      really apply to a bot/channel; this adapter will mostly implement `publish()` (post
      to channel) and skip the rest with a documented "N/A, not applicable to this
      platform's model" rather than a generic capability error.
- [ ] **Discord** — Discord API, bot token + OAuth for server management. Same
      N/A-for-profile-fields situation as Telegram — a Discord server isn't a brand
      profile. `publish()` (post via bot) is the realistic scope.

---

## Batch 4 — Newer / decentralized platforms with confirmed write APIs

Grouped because all four have straightforward, confirmed-writable profile APIs (unlike
Batch 1's LinkedIn/Instagram gaps) — this batch should be the fastest to build once
reached, mostly repetition of Batch 1/2's pattern.

- [ ] **Threads** (via Meta) — Threads API. Newer API surface — re-verify current scope
      coverage before assuming parity with the Instagram/Facebook adapter from Batch 1.
      Likely extends the existing Meta adapter rather than a fully separate one, since
      it shares Meta's OAuth app model.
- [ ] **Tumblr** — Tumblr API, confirmed profile update + publish support.
- [ ] **Mastodon** — Per-instance REST API — note this is architecturally different:
      the adapter needs an instance base URL as a config value, not a fixed one, since
      API surface depends on which Mastodon instance Nivy Next's account lives on.
- [ ] **Bluesky** — AT Protocol / Bluesky API, app-password or OAuth. Confirmed writable
      profile fields.

---

## Batch 5 — Approval-gated / limited (expect friction, start applications early)

Like LinkedIn in Batch 1, these have real access friction — worth starting the
application/approval process in parallel with earlier batches rather than waiting.

- [ ] **TikTok** — TikTok for Developers / Content Posting API. Access is
      application/approval-gated; profile-field updates are "Limited" per the platform
      matrix — confirm exactly which fields before promising `updateProfile()` coverage.
- [ ] **Snapchat** — Snap Kit / Marketing API is primarily an **ads** API, not an organic
      profile API. Likely conclusion once reached: no real `updateProfile()`/`publish()`
      adapter is buildable here at all — this may resolve to "not building an adapter,
      route to manual" rather than code. Flagging now so it's not a surprise later.

---

## Not going into `integrations/` at all — permanent manual-action queue

Per `docs/platform-matrix.md`, these have no public write API for profile management —
building an adapter would mean fabricating an endpoint that doesn't exist. These stay in
Phase 3's `manual_actions` queue indefinitely, regardless of how many other batches ship:

Yelp, BBB, Crunchbase, Clutch, GoodFirms, DesignRush, Sortlist, UpCity, G2, Capterra,
Trustpilot, Yellow Pages, MapQuest, Hotfrog, Manta, Chamber of Commerce, Foursquare,
Tripadvisor, Substack, Quora (unconfirmed API), Medium (public API deprecated for new
apps).

---

## How to proceed

Tell me **"continue batch 2"** (or name specific platforms out of order — e.g. "just
build YouTube next") and I'll build that batch the same way as Batch 1: real code,
verified current API facts, honest capability limits, OAuth helper, README — and check
it off in this file before delivering the zip.
