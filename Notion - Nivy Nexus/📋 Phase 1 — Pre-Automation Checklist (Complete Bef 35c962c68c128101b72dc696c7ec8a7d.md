# 📋 Phase 1 — Pre-Automation Checklist (Complete Before Touching n8n)

> Complete every item on this list before setting up any automation. Automating a broken process just creates fast failure. You need to understand the manual process first.
> 

---

# Why This Exists

Phase 2 automation (n8n + Puppeteer) will submit 50–100 contact forms per day on your behalf. If your message is wrong, your Gmail is flagged as spam, or your qualification process isn't working — automation amplifies the problem. This checklist ensures everything is proven before you scale it.

---

# ✅ Pre-Automation Checklist

## 1. Manual Execution Proven

- [ ]  Completed at least 20 full working days of Phase 1 manual execution
- [ ]  Submitted at least 200 contact forms manually
- [ ]  Had at least 30 DM conversations across all platforms
- [ ]  Booked at least 3 discovery calls
- [ ]  Closed at least 1 paying client
- [ ]  Identified which contact form message gets the best reply rate

## 2. Gmail Setup Ready for Volume

- [ ]  Gmail account is at least 30 days old (new accounts get spam-flagged faster)
- [ ]  SPF and DKIM records configured on any custom domain email
- [ ]  Gmail sending limit understood: 500 emails/day for standard Gmail, 2,000/day for Google Workspace
- [ ]  Unsubscribe link or opt-out line added to outreach message (reduces spam flags)
- [ ]  Test: sent 50 manual emails from the account with no spam flags

## 3. Contact Form Message Finalised

- [ ]  Best-performing manual message identified (highest reply rate)
- [ ]  Message is under 120 words (shorter = higher read rate on contact forms)
- [ ]  No spam trigger words ("free", "guaranteed", "act now", "limited offer")
- [ ]  Personalisation field identified: at minimum `[Company Name]` and `[City/Industry]`
- [ ]  Message reviewed for grammar and tone — must sound like a real human wrote it

## 4. Target List Structure Ready

- [ ]  Google Maps search queries tested and producing clean results (e.g. "digital marketing agency London")
- [ ]  Know which industries and cities produce the best leads from manual outreach
- [ ]  [Clutch.co](http://Clutch.co) filters saved for your top 3 target categories
- [ ]  Understand which company types respond (agencies respond more than sole traders)

## 5. Notion CRM Baseline

- [ ]  Lead Tracker has at least 30 entries from manual Phase 1
- [ ]  HOT / WARM / COLD tagging is consistent
- [ ]  Reply rate by platform is logged (so you can compare manual vs automated)

## 6. Tools Accounts Created

- [ ]  n8n account created (cloud: [n8n.io](http://n8n.io), or self-hosted on a VPS)
- [ ]  [Tally.so](http://Tally.so) form is live and tested end-to-end
- [ ]  Calendly is set up with a 30-minute "Discovery Call" slot
- [ ]  Gmail API access enabled in Google Cloud Console (needed for n8n Gmail node)

---

# Checklist Complete When:

- [ ]  All boxes above ticked
- [ ]  At least 1 paying client secured (proves the manual process works)
- [ ]  You can describe in one sentence what happens from contact form submission to discovery call

**When all done → move to Phase 2: n8n Automation Blueprint**