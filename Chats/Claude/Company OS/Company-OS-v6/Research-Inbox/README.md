# Research-Inbox

**This is a temporary staging area, not a source of truth.** Nothing here is official company knowledge.

## How to use this repo

Just drop anything into the `dump/` folder — a screenshot, a half-written note, a raw research finding, a voice-note transcript, a pasted article. **Zero structure required.** Filename doesn't matter. Formatting doesn't matter.

```
dump/
 └── whatever-you-name-it.md   (or .txt)
```

## What happens automatically

```
You push a file into dump/
        ↓
   GitHub Action triggers (.github/workflows/classify-and-pr.yml)
        ↓
   Claude API classifies it:
     → Which Department? (per Company-OS/GOVERNANCE/01-Department-Code-Registry.md)
     → Which Document Type? (per GOVERNANCE/02-Document-Type-Code-Registry.md)
     → PARA Bucket, Code, Filename, Folder Path
     → Formats it into the full Company-OS document template
       (metadata header + breadcrumb, per GOVERNANCE/04 and /06)
        ↓
   Action opens a Pull Request directly in the Company-OS repository,
   with the formatted document sitting in its correct department folder
        ↓
   The relevant Department CODEOWNER reviews the PR (per /CODEOWNERS)
        ↓
   In the same run, the workflow removes the original raw file from
   dump/ here in Research-Inbox — cleanup happens as soon as the PR is
   opened, not when it's merged
        ↓
   Approved & merged → the document is now official, in the right place,
   in the right format — no manual copy-paste. A confirmation comment is
   posted on the PR (.github/workflows/inbox-merge-confirmation.yml in
   Company-OS) noting the raw file was already cleaned up earlier
```

## Rules
- The AI never merges anything directly — every classification ends at a Pull Request, a human always approves.
- If the AI can't confidently classify something (department/type genuinely unclear), it will open the PR anyway but flag it clearly in the PR description for the reviewer to resolve — it will not guess silently.
- Files sitting in `dump/` for more than 14 days with no PR created (e.g. Action failed) will get a reminder — see the weekly health check in Company-OS.
