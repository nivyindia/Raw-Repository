# Repository Structure

The content hierarchy is logical. Git branches represent workflow/state; folders represent the durable organization of research.

```text
Research-Repository/
├── 00-inbox/
│   ├── links/
│   ├── repos/
│   ├── agents/
│   ├── skills/
│   ├── prompts/
│   ├── workflows/
│   ├── documents/
│   └── other/
│
├── 10-research/
│   ├── ai-agents/
│   ├── skills/
│   ├── workflows/
│   ├── prompts/
│   ├── dashboards/
│   ├── business-solutions/
│   ├── company-os/
│   └── integrations/
│
├── 20-analysis/
│   ├── classification/
│   ├── deduplication/
│   ├── comparisons/
│   ├── gap-analysis/
│   └── destination-mapping/
│
├── 30-curated/
│   ├── reusable/
│   ├── adaptable/
│   ├── reference/
│   └── rejected/
│
├── 40-validation/
│   ├── pending/
│   ├── passed/
│   └── failed/
│
├── 50-transfer-ready/
│   ├── agents/
│   ├── skills/
│   ├── workflows/
│   ├── prompts/
│   ├── docs/
│   └── integrations/
│
├── registry/
│   ├── research-registry.md
│   ├── destination-registry.md
│   └── source-registry.md
│
├── trackers/
│   ├── research-tracker.md
│   ├── promotion-tracker.md
│   └── gap-registry.md
│
└── docs/RESEARCH-SYSTEM/
```

### Important Rule

Existing historical/raw folders are **not moved in the initial implementation**. First implement the control system. Then inventory and migrate content in controlled batches.
