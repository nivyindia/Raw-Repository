# Contributing to [Company Name] Company OS

## Adding or changing a document

1. Check `03_RESOURCES/Company_Master_Standards/GOVERNANCE/04-Classification-Naming-Rulebook.md` — classify your document (Department, Type, PARA Bucket, Code, Name, Folder).
2. If it's a small, everyday change — commit directly to `main` in the correct folder.
3. If it's a big/collaborative piece of work — create a branch: `research/<topic>`, `sop/<name>`, or `process/<name>` (see `GOVERNANCE/05-Repository-Branch-Workflow.md`).
4. Use the metadata header template from `GOVERNANCE/04-Classification-Naming-Rulebook.md` at the top of your document.
5. Open a Pull Request using the template — the relevant CODEOWNER (see `/CODEOWNERS`) must approve before it merges into `main`.
6. Once Approved, set `Lifecycle Status: Published` and `publish: true` in the metadata header when ready for company-wide visibility.

## Random / unsorted material

If you don't have time to classify something properly right now, put it in `Research-Inbox` (separate repository) instead of guessing a folder here. It will be classified and moved via a reviewed Pull Request later — see `GOVERNANCE/05-Repository-Branch-Workflow.md`, Section 5/7.

## Questions

Raise a GitHub Issue using the "New Document / SOP Task" template, or ask the Company OS AI Assistant.
