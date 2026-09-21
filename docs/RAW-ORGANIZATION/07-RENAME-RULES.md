# Rename Rules

## Goal

Make filenames human-readable and stable without changing substantive content during the first organization pass.

## Transformation

1. Determine the semantic title from document content.
2. Remove source-export IDs and random hashes.
3. Remove redundant leading/trailing emoji where they do not carry meaning.
4. Normalize separators to spaces or ` - `.
5. Use Title Case for ordinary human-facing document titles.
6. Preserve meaningful acronyms such as AI, OS, CRM, SEO, CPA, HR, SOP.
7. Add brand to the filename only when it materially improves disambiguation.
8. Do not encode dates unless the date is part of the document's identity/version.
9. Do not rename unresolved `Untitled`/placeholder material until content classification is complete.

## Examples

```text
Nivy Advisory 30-Day Online Presence Plan <id>.md
→ Nivy Advisory - 30-Day Online Presence Plan.md

Nivy Advisory Brand Color Palette <id>.md
→ Nivy Advisory - Brand Color Palette.md

Nivy c0a97d9....md
→ Nivy - Workspace Membership Record.md   # only if content confirms this meaning
```

## Collision handling

If two source files normalize to the same name:
- compare content;
- classify as duplicate/version/related-but-distinct;
- use a meaningful qualifier such as `- v2`, `- Research`, or `- Export` only when evidence supports it;
- never overwrite one with another.

## Provenance requirement

Every rename must be represented in `indexes/MIGRATION-MANIFEST.md` with the original path, new path, reason, confidence and verification state.
