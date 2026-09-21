# 02 — Document Type & Code Registry

> **Purpose:** The fixed list of document types and their codes. Every document must be classified as exactly one type from this table.
> **Version:** 1.0 | **Owner:** Workspace Admin | **Status:** Approved

| Code | Type | What It Covers | Example |
|---|---|---|---|
| POL | Policy | Company-wide rule or mandate; rarely changes | FIN-POL-001 — Expense Approval Policy |
| SOP | Standard Operating Procedure | Step-by-step "how we do X" | RND-SOP-004 — New Product Testing Process |
| WI | Work Instruction | Narrower/more technical than an SOP — single-task detail | TECH-WI-012 — Server Backup Steps |
| TPL | Template | Reusable blank format to copy | MKT-TPL-007 — Campaign Brief Template |
| REP | Report | Periodic output (financial, performance, research) | SALES-REP-Q1-2026 — Quarterly Sales Report |
| REC | Record | Evidence/log of something that happened (approvals, checklists filled in, meeting minutes) | HR-REC-014 — Onboarding Completion Record |
| KB | Knowledge Base / Reference | Explains a concept, glossary entry, FAQ | ALL-KB-002 — What is a Lead |
| PROJ-DOC | Project Document | Charter, plan, or status doc tied to a specific project | PROJ-DOC-Website2026 — Website Redesign Plan |
| STRAT | Strategy Document | Forward-looking plan, roadmap, vision doc | STR-STRAT-003 — 2026 Growth Roadmap |
| FORM | Form / Checklist | Fillable structured input | QA-FORM-002 — QC Checklist |
| MEET | Meeting Notes | Notes/minutes from a specific meeting | OPS-MEET-2026-05-01 — Weekly Sync |
| ARCH | Archived (status, not a fresh type) | A retired version of any type above — code and folder stay the same, only Lifecycle Status changes (see Doc 04) | — |

---

## Rules

1. If a document doesn't clearly fit one type, ask: "Is this telling someone how to do something (SOP/WI), what happened (REP/REC), what to fill in (FORM), or what to know (KB)?" — that answers it.
2. New types are added here first, never invented inside a folder ad hoc.
3. `ARCH` is never combined into the code — a document keeps its original type code forever (e.g. `RND-SOP-004`) and only its **Lifecycle Status** field changes to Retired/Archived.
