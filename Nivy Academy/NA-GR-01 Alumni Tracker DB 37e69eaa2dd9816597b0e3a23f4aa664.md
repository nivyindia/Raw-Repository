# NA-GR-01 | Alumni Tracker DB

**Doc ID:** NA-GR-01 | **Department:** Growth & Alumni | **Status:** 🟢 Live | **Audience:** Internal | **Phase:** Phase 4

---

# NA-GR-01 | Alumni Tracker — Database Structure

---

## Purpose

Tracks graduates post-placement to measure long-term outcomes, feed testimonials, and identify referral/upsell candidates.

---

## Database Fields

<table header-row="true"><tr><td>Field</td><td>Type</td><td>Description</td></tr><tr><td>Student Name</td><td>Text</td><td>Linked to Student Enrollment DB (NA-SM-01) and Placement Tracker (NA-PP-05)</td></tr><tr><td>Batch</td><td>Select</td><td>Batch number</td></tr><tr><td>Graduation Tier</td><td>Select</td><td>Tier completed</td></tr><tr><td>Current Status</td><td>Select</td><td>Employed / Freelancing (GFA) / Freelancing (Independent) / Studying Further / Not Active</td></tr><tr><td>Company / Client</td><td>Text</td><td>Current employer or main client</td></tr><tr><td>Role</td><td>Text</td><td>Current role/title</td></tr><tr><td>Salary/Income Band</td><td>Select</td><td>Confidential band for reporting only</td></tr><tr><td>6-Month Check-in Done</td><td>Checkbox</td><td>Mentor follow-up completed</td></tr><tr><td>12-Month Check-in Done</td><td>Checkbox</td><td>Annual follow-up completed</td></tr><tr><td>Testimonial Status</td><td>Select</td><td>Not Asked / Requested / Received / Published</td></tr><tr><td>Referral Count</td><td>Number</td><td>Number of new students referred</td></tr><tr><td>Upsell Status</td><td>Select</td><td>None / Considering / Enrolled in Next Tier/Program</td></tr></table>

---

## Views Needed

- **Active Pipeline** — grouped by Current Status
- **Check-in Due** — filtered by upcoming 6/12-month check-ins
- **Testimonial Candidates** — filtered to Employed/Freelancing with no testimonial yet

---

## Usage Notes

This tracker is the source of truth for all alumni success stats used in marketing (NA-MK series) and partner pitch decks (NA-PP-02). Figures must be pulled live, never estimated.