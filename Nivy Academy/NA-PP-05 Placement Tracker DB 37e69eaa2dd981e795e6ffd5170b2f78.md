# NA-PP-05 | Placement Tracker DB

**Doc ID:** NA-PP-05 | **Department:** Partnerships & Placement | **Status:** 🟢 Live | **Audience:** Internal | **Phase:** Phase 3

---

# NA-PP-05 | Placement Tracker — Database Structure

---

## Purpose

Tracks every student's journey from graduation through to job/freelance placement, enabling Nivy Academy to report placement success rates to partners and prospective students.

---

## Database Fields

<table header-row="true"><tr><td>Field</td><td>Type</td><td>Description</td></tr><tr><td>Student Name</td><td>Text</td><td>Full name, linked to Student Enrollment DB (NA-SM-01)</td></tr><tr><td>Batch</td><td>Select</td><td>Batch 1, 2, 3...</td></tr><tr><td>Tier</td><td>Select</td><td>Trailblazer / Starter / Practitioner / Accelerator / Elite</td></tr><tr><td>Graduation Date</td><td>Date</td><td>Date of Final Graduation Assessment completion</td></tr><tr><td>Placement Status</td><td>Select</td><td>Not Started / Applied / Interviewing / Offer / Joined / Not Seeking</td></tr><tr><td>Placement Type</td><td>Select</td><td>Full-time / Freelance / GFA / Internal Hire</td></tr><tr><td>Company / Client</td><td>Text</td><td>Name of employer or client</td></tr><tr><td>Role</td><td>Text</td><td>Job title or project type</td></tr><tr><td>Salary / Rate</td><td>Text</td><td>Compensation (optional, confidential field)</td></tr><tr><td>Placement Source</td><td>Select</td><td>Model 1-5 (per NA-PP-01)</td></tr><tr><td>Date Joined</td><td>Date</td><td>Confirmed start date</td></tr><tr><td>Follow-up 30-Day Check</td><td>Checkbox</td><td>Mentor confirmed student is settled and active</td></tr></table>

---

## Views Needed

- **By Status** — Kanban grouped by Placement Status
- **By Batch** — Table grouped by Batch, for cohort-level reporting
- **Placement Rate Dashboard** — % Joined / Total Graduated, filterable by Tier and Batch

---

## Reporting Use

This tracker feeds the placement statistics quoted in marketing materials (landing pages, brochures) and partner pitch decks — figures must always be pulled live from this database, never estimated.