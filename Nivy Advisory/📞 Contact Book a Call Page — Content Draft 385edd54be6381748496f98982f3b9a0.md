# 📞 Contact / Book a Call Page — Content Draft

**Status:** ✅ Updated — form spec, pre-qualification, Calendly note, confirmation flow added (Claude improvement pass, June 2026)

**Source:** Part 5.7 (Time-Zone-Aware Booking)

---

## Hero

**Headline:** Let's Talk About Your Cross-Border Setup

**Subheadline:** Book a free 30-minute consultation. We'll map your current situation across every country you operate in and recommend the right scope — no pressure.

---

## Section 1 — Booking Widget (embed placeholder)

*Time-zone-aware booking widget required per Part 5.7 — must clearly show available slots adjusted to visitor's local time zone, given the 12-hour spread between UAE/Singapore and US/Canada office hours.*

**Microcopy under widget:** Times shown in your local time zone.

**Implementation note:** Embed Calendly (or equivalent) directly on this page — never link out to a separate booking site. An off-site redirect at the final conversion step measurably increases drop-off. The embed should sit above the alternative-contact section so it's the first thing visible.

---

## Section 1B — Pre-Qualification (before showing booking slots)

**Heading:** What are you looking for?

**Field type:** Single-select dropdown, required, shown above the booking widget

**Options:**

- Business tax
- Individual / expat tax
- Bookkeeping
- Advisory / CFO services
- Not sure yet

**Purpose:** Routes the visitor's selection into the booking confirmation/intake form so the advisor preparing for the call already has context — removes the generic-intro problem flagged in Section 4 below.

---

## Section 1C — Quick Contact Form (for visitors not ready to book a call)

**Fields (4 maximum):**

1. Name
2. Email
3. Country (dropdown, all 6 served countries + "Other")
4. Brief description (short text, 1–2 sentences)

**Plus:**

- Preferred contact time (time picker)
- Time zone (auto-detected from browser, editable dropdown) — critical given the 12-hour APAC/Americas spread

**CTA button:** Send Message

**Design note:** Keep this visually secondary to the booking widget — it's the lower-intent fallback path, not the primary CTA.

---

## Section 2 — Alternative Contact Methods

- **General inquiries:** [email placeholder]
- **Existing clients:** [support email / portal link placeholder]
- **Phone:** [regional numbers placeholder — per hub, see Part 5.8 hub-and-local-partner model]

---

## Section 3 — Office Hours by Region (explicit per Part 5.7)

| Region | Hours (local time) |
| --- | --- |
| US / Canada | [to be confirmed] |
| UK | [to be confirmed] |
| Australia | [to be confirmed] |
| UAE / Singapore | [to be confirmed] |

---

## Section 4 — What Happens After You Book (Confirmation Page Copy)

**Confirmation page heading:** You're Booked — Here's What Happens Next

1. You'll receive a confirmation email with a short intake form (current entities, countries, rough scope) — pre-filled with whatever you selected in the "What are you looking for?" step.
2. We review your intake before the call so it's not a generic intro — we come with questions specific to your situation.
3. On the call: we map your cross-border exposure and recommend a tier (Essentials / Growth / Global Partner).
4. No obligation — you'll leave with clarity even if you don't move forward.

**Confirmation page must explicitly state:** what happens next, expected response time (e.g. "intake form arrives within 5 minutes"), and who will contact them (advisor name, or "a member of our [region] team").

---

## Trust Strip

CPA / ACCA / CA credentialed team · SOC 2-aligned data security · Your information is never shared without consent

---

## Notes for Design/Dev

- Form fields must comply with region-aware data retention language per Part 5.2 (GDPR/PIPEDA/Privacy Act/PDPA).
- Security/compliance badges required on this page per Part 1.8 (it's a form-facing page).