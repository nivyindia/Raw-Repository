# 🎯 CTA Hierarchy & Mobile-First Design Brief — Site-Wide

**Status:** ✅ Drafted (Claude improvement pass, June 2026) — ready for dev handoff

**Covers:** Phase C2 (CTA Hierarchy & Placement) and Phase C4 (Mobile-First Design Notes)

**Note:** Phase C1 (Lead Capture Strategy) and C3 (Form Design) are implemented directly on the Contact page and Home page drafts — see those sub-pages for the actual copy. This page covers the rules that apply *across every page*, which a single content draft can't hold on its own.

---

# CTA Hierarchy & Placement — Site-Wide Rules

## The Core Rule

Every page gets exactly one **primary CTA** and one **secondary CTA**. Never zero, never three. Visitors who aren't ready for "Book a Call" need a lower-commitment exit that still converts.

| Page Type | Primary CTA | Secondary CTA |
| --- | --- | --- |
| Home | Book a Free Consultation | Download Tax Deadline Calendar |
| Country pages | Book a Call for [Country] Tax | Download [Country] Deadline Calendar |
| Service pages | Get Started with [Service Topic] | See Pricing |
| Pricing | Book a Free Consultation | (tier-specific "Get Started" buttons act as the primary on this page) |
| Blog articles | Download relevant guide/calendar | Book a Call |
| FAQ | Book a Call | Browse Services |

**Why CTA copy must echo the page topic:** "Get Started with CPA-Prepared Tax Filing" converts better than a generic "Get Started" because it confirms to the visitor they're still on-topic — generic CTA copy creates a small but real moment of doubt right at the conversion point.

## Country Page CTA Test

Country pages should test specific vs. generic CTA copy once there's enough traffic to split-test:

- **Variant A (specific):** "Book a Call for UK Tax"
- **Variant B (generic):** "Book a Free Consultation"

Flag this as a Phase 2 (post-launch) CRO test, not a pre-launch decision — don't delay launch waiting for a test result.

## Sticky Header CTA

- Every page: sticky header containing logo + primary CTA button, visible on scroll.
- On mobile, the sticky CTA collapses to a single thumb-reachable button (bottom-anchored, not top-anchored — top sticky headers get scrolled past attention on mobile, bottom-anchored bars stay in the thumb zone).
- Sticky CTA copy is always the page's primary CTA, never a third option.

---

# Mobile-First Design Brief (for Dev)

## Why This Matters

Financial-services prospects increasingly research on mobile before committing on desktop. A table-heavy, form-heavy site that isn't mobile-first will lose qualified leads at the exact moment they're most motivated (mid-research, on their phone, between meetings).

## Non-Negotiable Rules

1. **Every CTA must be thumb-reachable.** Design for one-handed use — primary buttons sit in the bottom third of the viewport, not buried at the top of a long page.
2. **Table-heavy pages (country pages, pricing) get accordion or horizontal-scroll treatment on mobile** — never force a 6-column table to shrink-to-fit on a 375px screen. This applies to:
    - Deadline tables (US/UK/Canada country pages)
    - Entity type comparison tables (all country pages)
    - UAE Free Zone vs. Mainland table
    - Pricing comparison table
3. **Country flag strip on Home:** touch-friendly horizontal scrollable row on mobile, not the desktop grid layout. Each flag/country tile should be large enough for an accurate tap (minimum 44x44px touch target).
4. **Forms collapse to single-column on mobile** — no side-by-side fields below 600px viewport width.
5. **Sticky CTA bar:** bottom-anchored on mobile (see above), top-anchored on desktop is fine.
6. **Lead magnet banner (Home Section 4B):** on mobile, render as a full-width card, not a thin strip — the email field and button need adequate tap targets.

## Handoff Checklist for Dev

- [ ]  All tables identified above have an explicit mobile breakpoint treatment specified in the design file
- [ ]  All CTA buttons meet 44x44px minimum touch target
- [ ]  Sticky CTA bar behavior confirmed: bottom-anchored mobile / top-anchored desktop
- [ ]  Contact form tested at 320px, 375px, and 414px viewport widths
- [ ]  Country flag strip tested for scroll behavior on touch devices (no accidental navigation on scroll)

---

> **Cross-reference:** Lead capture copy lives on the 📞 Contact / Book a Call Page and 🏠 Home Page content drafts. This page only covers placement/hierarchy/mobile rules that apply across the whole site.
>