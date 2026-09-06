# 05 — Repository, Branch & GitHub Workflow Architecture (FINAL)

> **Status: FINAL.** This is the decided architecture, not a proposal. It governs how GitHub itself (organization, repositories, branches, Issues, Projects, Pull Requests, Actions, permissions) is structured and used. Docs 01–04 govern *what goes inside* files/folders; this document governs *the GitHub machinery around them*.
> **Owner:** Workspace Admin / CTO

---

## 1. Full Organization Structure

```
                         YOUR GITHUB ORGANIZATION
                                    │
        ┌───────────────┬──────────┼──────────┬───────────────┐
        ↓               ↓          ↓          ↓               ↓
   Shared-OS      [Company-A]-OS  [Company-B]-OS  ...more   Research-Inbox
        │               │          │          companies         │
   Global Policies   Own Depts   Own Depts    as needed      Temporary
   Common SOPs       Own SOPs    Own SOPs                    dump zone
   Common Templates  Own Research Own Research                (Section 5)
   Governance docs   Own People  Own People
   (Docs 01–09
    themselves)
```

**Rule 1:** A repository = a Company/OS boundary, or a genuinely separate access/lifecycle domain (Shared-OS, Research-Inbox). **Never** one repository per department, per team, per project, or per SOP — that is what causes "repository explosion" once you have several companies/brands.

**Rule 2:** Start with **one company repository** even if more companies are planned. Split into a second repository only when a real boundary appears — different legal entity, different employee access group, or different lifecycle. Don't pre-create empty repos for hypothetical future companies.

**Rule 3 — Shared-OS:** Anything genuinely common across companies (global policies, shared SOP templates, brand-agnostic governance, the Docs 01–09 standard itself) lives in `Shared-OS` exactly once. Every company repository **references/links** to it — it is never copy-pasted into each company repo. This prevents 8–10 companies from silently drifting into 8–10 slightly different versions of "the same" policy.

---

## 2. Branch Strategy — Branch Means Lifecycle, Never Organization

This is the single most important rule in this whole document:

```
   Branch  =  STATE / LIFECYCLE of the work        (temporary)
   Folder  =  ORGANIZATIONAL STRUCTURE               (permanent)
```

### Branches that exist:

```
main
 │
 ├── research/<topic>        e.g. research/australia-accounting-market
 ├── sop/<sop-name>          e.g. sop/cold-email-v2
 ├── process/<process-name>  e.g. process/ai-lead-qualification
 ├── feature/<feature-name>  e.g. feature/n8n-sales-automation
 └── hotfix/<issue>          e.g. hotfix/broken-onboarding-link
```

### Branches that do NOT exist (these are folders instead — see Doc 03):

```
✗ Sales            ✗ Marketing          ✗ HR
✗ Finance          ✗ Company-A          ✗ RND
```

### When to actually create a branch

```
CREATE A BRANCH FOR:                        DO NOT CREATE A BRANCH FOR:
──────────────────────                      ─────────────────────────
✓ A major research project                  ✗ Every small research note
✓ A new SOP with multiple contributors       ✗ Every single document
✓ A significant process redesign             ✗ Every version bump (v1.0→v1.1)
✓ A new automation/workflow build            ✗ Every employee's personal work
✓ Rewriting an already-Approved document      ✗ Quick one-line edits
```

Small, everyday work (a quick research note, a one-line SOP fix) happens **directly on `main` as folder + commit** — no branch needed. Branches exist only when work is big enough, or collaborative enough, that it genuinely needs isolation before review.

### Why not one branch per department?
If every department got its own permanent branch, you'd end up maintaining 10+ branches forever, each drifting further from `main`, each needing its own merge strategy. Departments are **folders** (Doc 03: `01_AREAS/[Dept]/`) precisely so this doesn't happen — folders don't need "merging," they just sit there as permanent structure.

---

## 3. The Knowledge Flow — Full Lifecycle Diagram

```
   RAW IDEA / QUICK NOTE
          │
          ↓
   ┌─────────────────┐
   │  Research-Inbox   │  ← zero structure required, dump anything (Section 5)
   └────────┬─────────┘
            │  AI classifies + opens a Pull Request
            ↓
   ┌─────────────────────┐
   │  research/<topic>     │  ← branch, if it's a big/collaborative project
   │  branch                │     (small stuff skips straight to the next step)
   └────────┬─────────────┘
            │  Pull Request: research/* → main
            ↓
   ┌─────────────────────┐
   │  Human Review          │  ← CODEOWNER for that department (Section 6)
   │  (Sales Manager,       │
   │   Ops Head, etc.)       │
   └────────┬─────────────┘
            │  Approved → Merge
            ↓
   ┌─────────────────────┐
   │      main               │  ← official internal company knowledge
   │  (01_AREAS/[Dept]/...)  │     (Doc 03/04 rules apply from here on)
   └────────┬─────────────┘
            │  metadata tag: publish: true  (Doc 04 header)
            ↓
   ┌─────────────────────┐
   │  GitHub Action          │  ← automatic, no manual copy-paste
   │  auto-sync                 │
   └────────┬─────────────┘
            │
            ↓
   ┌─────────────────────┐
   │  Employee-Facing         │  ← Notion / Wiki.js / GitHub Pages
   │  Published Space          │     (only the tagged, approved subset)
   └────────┬─────────────┘
            │
            ↓
        EMPLOYEES  ←→  AI ASSISTANT (Section 7)
```

**Why not a permanent `publish` branch?** A permanent branch that mirrors 5% of `main`'s content tends to drift out of sync and needs constant manual merging. Instead: tag the document `publish: true` in its Doc 04 metadata header once Approved, and a GitHub Action watches `main` for that tag and auto-syncs those specific documents outward. `main` stays the single internal source of truth; the external employee-facing space is always a generated mirror, never edited directly by anyone.

---

## 4. GitHub-Native Feature Map — Full Table

| GitHub Feature | Meaning in Your Company | Rule |
|---|---|---|
| **Organization** | The whole business/group | One org holds Shared-OS + all company repos |
| **Repository** | A company / Shared-OS / Research-Inbox | See Section 1 |
| **Branch** | Research / SOP-dev / Process-dev / Feature / Hotfix lifecycle | See Section 2 — never a department |
| **Folder** | Department, sub-department, team, topic (Doc 03) | Permanent structure |
| **File** | The actual document | Named per Doc 02/04 |
| **Issue** | One task/work item — e.g. "Create Cold Email SOP" | Tagged with Department (Doc 01), Type (Doc 02), Priority |
| **Project (Kanban board)** | Visual pipeline of all ongoing work | Columns: `Backlog → Research → Draft → Review → Approved → Published` |
| **Pull Request** | The only way work moves from a branch into `main` | Needs at least one CODEOWNER approval |
| **GitHub Actions** | Automation | Auto-publish tagged docs, metadata validation, broken-link checks, stale-content flags |
| **CODEOWNERS** | Who must approve changes in which folder | e.g. `01_AREAS/Sales/* @sales-lead` |
| **Branch Protection / Rulesets** | Blocks direct pushes to `main` | All changes to `main` go through a reviewed PR — no exceptions |
| **Labels** | Department / Type / Priority tags on Issues & PRs | Applied consistently, matching Doc 01/02 codes |
| **Milestones** | Quarterly goals | Issues linked to the quarter they support |
| **Discussions** | Open questions / "should we?" ideas | Kept separate from Issues (Issues = committed work) |
| **Teams + Permissions** | Employee access, scoped by department/role | AI and employees only ever see what their GitHub permission allows |
| **Tags/Releases** | Big stable milestones (v1.0, v2.0) | Used for major version markers, not every small edit |
| **Wiki / external published space** | The actual employee-facing documentation interface | Raw internal `main` content is never shown directly to employees |

---

## 5. Real Example — Full Walkthrough

**Scenario:** Sales department needs a "Cold Email SOP."

```
STEP 1 — Task created
   GitHub Issue: "Create Cold Email SOP"
   Labels: [Department: SALES] [Type: SOP] [Priority: P2]
   Owner: Sales Manager | Deadline: set

STEP 2 — Enters the pipeline
   Project board: Backlog → moved to → Research

STEP 3 — Work happens
   Branch: sop/cold-email
   Content built inside: 01_AREAS/Sales/SOPs/ (working copy on the branch)

STEP 4 — Document ready
   Pull Request opened: sop/cold-email → main
   Reviewer: Sales Manager (CODEOWNER for 01_AREAS/Sales/*)

STEP 5 — Approval
   PR approved → merged into main
   Document is now: SALES-SOP-00X — Cold Email Outreach (Doc 02/04 naming applies)
   This is now official internal company knowledge.

STEP 6 — Publish
   Metadata header (Doc 04) set to: publish: true
   GitHub Action detects the tag → auto-pushes to the employee-facing
   Wiki/Notion space

STEP 7 — Task closed
   Issue auto-closes (or closed manually) once Step 6 completes
```

### Roles, remembered as one mental model
```
Company / Shared-OS   →  Repository
Research/SOP/Process   →  Branch
Department/Team/Topic   →  Folder
Actual knowledge          →  File
Work to be done            →  Issue
Dashboard of all work       →  Project
Review + approval             →  Pull Request
Automation                     →  Actions
Employee access                 →  Teams + Permissions
Getting knowledge to employees   →  Actions → Wiki/Notion
```

---

## 6. CODEOWNERS & Approval Authority

Every folder in `01_AREAS/[Dept]/` has exactly one CODEOWNER role (per Doc 01's Owner Role column). Example:
```
01_AREAS/Sales/*        @sales-head
01_AREAS/RND/*           @rnd-head
01_AREAS/Finance/*        @cfo
03_RESOURCES/*             @workspace-admin
```
A Pull Request touching a folder cannot merge into `main` without approval from that folder's CODEOWNER. This is enforced by GitHub's branch protection rules on `main` (Section 4) — not by convention or trust alone.

---

## 7. Research-Inbox — Full Detail

```
   YOU, IN A HURRY
          │  dump anything — screenshot, half-note, raw link, voice transcript
          ↓
   ┌─────────────────────────┐
   │      Research-Inbox         │   Rule: temporary staging, NEVER a
   │      (separate repository)   │   source of truth. Nothing lives
   └────────┬─────────────────┘   here permanently.
            │
            │  AI classification pass runs:
            │    → Which Company?
            │    → Which Department (Doc 01)?
            │    → Which Document Type (Doc 02)?
            │    → What Title / Code (Doc 04)?
            │    → What Metadata header (Doc 04)?
            ↓
   ┌─────────────────────────┐
   │  AI opens a Pull Request     │   Moves the item into the correct
   │  into the company repo        │   01_AREAS/[Dept]/ folder, with the
   └────────┬─────────────────┘   metadata header pre-filled
            │
            │  Human review (you, or the relevant Department Owner)
            ↓
         Approved → merged into main, now Draft/Under-Review status
                     (Doc 04 Lifecycle takes over from here)
```
**Rule: AI never moves anything directly without a Pull Request.** Every Inbox-to-repo move is reviewable and reversible before it becomes part of official company knowledge.

---

## 8. AI Access Rules — Full Detail

```
   AI CAN:                              AI CANNOT:
   ─────────                            ───────────
   ✓ Search                             ✗ Publish
   ✓ Read                                ✗ Approve
   ✓ Explain                              ✗ Delete
   ✓ Summarize                             ✗ Modify official (main) content directly
   ✓ Navigate
   ✓ Draft PRs for Research-Inbox items
```

```
   GitHub Permissions
          ↓
   Employee Access
          ↓
   AI Access  ←  same scope, never more
```
The AI never bypasses an employee's own GitHub permissions to show them something they couldn't otherwise see — even if the AI itself technically has broader read access.

**Golden Rule, to be taught to every employee on Day 1:**
> *An AI answer is not official. The Published document is official. If they ever conflict, the Published document wins.*

Every AI answer to an employee query must include its source, in this format:
```
Answer: ...

Source: 01_AREAS/Sales/SOPs/SALES-SOP-002 — v2.1
```

---

## 9. Governance-as-Code

The rules in Docs 01–09 themselves live inside the repository, version-controlled — not "in someone's head" or scattered across chat history:

```
Shared-OS/
 └── 03_RESOURCES/Company_Master_Standards/GOVERNANCE/
      ├── 01-Department-Code-Registry.md
      ├── 02-Document-Type-Code-Registry.md
      ├── 03-Folder-Structure-Map.md
      ├── 04-Classification-Naming-Rulebook.md
      ├── 05-Repository-Branch-Workflow.md      ← this file
      ├── 06-Navigation-Standard.md
      ├── 07-Governance-Health-AI-Policy.md
      ├── 08-Audit-New-vs-Repeated.md
      └── 09-Final-Change-Plan.md
```
Any change to these governance documents follows the exact same Pull Request + CODEOWNER approval flow as any other document (Section 5) — governance is not exempt from its own rules.
