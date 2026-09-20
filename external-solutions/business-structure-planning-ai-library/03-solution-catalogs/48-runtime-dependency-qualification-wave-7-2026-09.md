# Runtime & Provenance Qualification — Wave 7 — 2026-09

## Purpose
Wave 7 advances exact-asset qualification from branch-level evidence to pinned source provenance and dependency/runtime evidence.

Pipeline: License → Provenance → Dependency → Runtime → Security/Data → Tests → Windows/Docker → Contract Adaptation → Human Approval → Qualified

## Exact source provenance

| Asset | Source | Pinned source commit | License | Current decision |
|---|---|---|---|---|
| EA-002 | GTM Agents — templates/recipes/generate-leads.md | 78e0419f4440bcb43bc80127e174ecf5adef1753 | Apache-2.0 | Runtime Pending |
| EA-004 | B2B SDR Agent Template — skills/delivery-queue/SKILL.md | 2c20788e5931f3f530023cade228ed4f74a38c84 | MIT | Runtime Pending |
| EA-008 | Claude Code Skills — engineering/skills/skill-tester/SKILL.md | e8affef3cb029267859e24c4538a78adc6f45caa | MIT | Runtime Pending |
| EA-012 | Openkoda — ChatGPTPromptService.java | f0590fc3f3cc416286fe63e01bb835d881171356 | MIT | Runtime Pending |

## Evidence collected

### EA-002 — GTM lead-generation recipe
- Source commit pinned.
- Markdown/documentation asset; not standalone executable.
- Uses source-specific plugin and CRM commands.
- Reusable value is the generic lead-generation recipe, not source command syntax.
- PII, outbound compliance and source-plugin availability remain unverified.

Decision: Runtime Pending; adapt generic workflow only.

### EA-004 — Delivery Queue
- Source commit pinned.
- Defines scheduling, segmentation, cancellation, flushing, timezone, quiet hours and retries.
- Referenced deliver.sh worker was not available through the inspected repository path in this pass.
- Executable runtime behavior was not reproduced.

Decision: Runtime Pending; extract queue contract and implement/test an Nivy-owned worker.

### EA-008 — Skill Tester
- Source commit pinned.
- SKILL.md states Python Standard Library Only and describes structure, syntax/import/runtime testing and scoring.
- Runtime implementation source was not independently retrieved/executed in this pass.

Decision: Runtime Pending; do not promote from documentation alone.

### EA-012 — Openkoda Dynamic Context Service
- Source commit pinned.
- Root Maven POM identifies Spring Boot 3.0.5 and project version 1.7.1.
- Service uses reflection, entity metadata, annotations, autocomplete services and prompt templates for dynamic context.
- Maven dependency resolution/build/runtime was not executed.

Decision: Runtime Pending; reproduce the allowlisted dynamic-context pattern in Nivy before importing source code.

## Qualification result

| ID | Provenance | License | Dependency evidence | Runtime evidence | Status |
|---|---|---|---|---|---|
| EA-002 | PASS | PASS | Pending | Not executed | Runtime Pending |
| EA-004 | PASS | PASS | Pending | Not executed | Runtime Pending |
| EA-008 | PASS | PASS | Pending | Not executed | Runtime Pending |
| EA-012 | PASS | PASS | Pending | Not executed | Runtime Pending |

## Important correction
Pinning a commit improves provenance but does not equal runtime qualification. No asset is promoted to Qualified or Implemented solely from repository inspection.

## Nivy adaptation targets
1. EA-002 → Lead Generation Skill: ICP, qualification, evidence, dedupe, enrichment, CRM output, outbound policy gate.
2. EA-004 → Universal Delivery Queue: schedule, timezone, quiet hours, retry, idempotency, cancellation, rate limits, approval/policy gate, audit.
3. EA-008 → Skill Evaluation Harness: structure, syntax/import, fixtures, output schema, security, regression, score/report.
4. EA-012 → Dynamic Context Assembly: field/method allowlist, role/department/tenant filtering, sensitive-data filtering, freshness/provenance, token budget, injection-resistant serialization, audit.

## Next gate
Run isolated runtime qualification with pinned source checkout, dependency lock capture, tests, network/secret inventory, security/data-flow review and reproducible pass/fail evidence.

Until those checks pass, all four assets remain Runtime Pending.