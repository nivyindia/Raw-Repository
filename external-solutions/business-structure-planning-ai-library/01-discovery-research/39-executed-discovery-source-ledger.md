# Executed Discovery Source Ledger — Cross-Cutting Layers

**Research date:** 2026-09-16
**Status:** Initial execution batch complete; this is a living source ledger, not a claim of exhaustive internet coverage.

## Enterprise architecture

| Source | Reusable content | Access/license note |
|---|---|---|
| Archie EA | TOGAF/ArchiMate EA, capability maps, value streams, application portfolio, governance | AGPL-3.0; commercial license option |
| Turbo EA | Self-hosted EA + embedded BPM, configurable metamodel | Open source; verify exact repo license before deployment |
| Enterprise Architecture Reference Catalog | Large machine-readable capability/process/value-stream catalog | Free/open source |

## Identity/access

| Source | Reusable content | Access/license note |
|---|---|---|
| ZITADEL | SSO, MFA, passkeys, OIDC, SAML, SCIM, multi-tenancy | Open source |
| Keycloak | IAM/SSO/OIDC/SAML/RBAC foundation | Open source; verify current license/version |
| Authentik | Identity provider, SSO and access management | Open source; verify current license/version |

## AI governance / AgentOps

| Source | Reusable content | Access/license note |
|---|---|---|
| SAFi | Agent policy enforcement, tool-call governance, audit records, supervision | Open source; verify license |
| Open Enterprise AgentOps Mesh | Evaluation lab, agent registry, evidence vault, policy-as-code, trace ledger, connector sandbox | Open source/reference implementation; not automatically production-ready |
| Alignment Governance Stack | Delegated AI authority, policy, receipts, governance memory | Open source/reference architecture |
| PALO Framework | Operational AI governance lifecycle and assurance | Open source framework |
| OGAC | Private governed enterprise AI gateway, evals, guardrails, lineage, knowledge, audit, FinOps | Source-available; verify terms before commercial use |

## Data governance

| Source | Reusable content | Access/license note |
|---|---|---|
| OpenMetadata | Catalog, metadata, lineage, quality, policies, data contracts, MCP, organizational memory | Open source |
| OpenLineage | Standardized run/job/dataset lineage events | Open source/open standard |
| DataHub | Catalog, discovery, lineage, governance | Open source; verify current license |
| Awesome Data Catalogs | Discovery map for data catalogs/observability/governance | Curated open-source directory; inspect each linked project |

## AI evaluation

| Source | Reusable content | Access/license note |
|---|---|---|
| AgentGovBench | 48 governance scenarios mapped to NIST AI RMF | MIT |
| proofagent-harness | Adversarial, artifact, context, compliance and governance evaluation; CI gates | Open source; verify current license |
| Awesome AI Agent Evaluation | Discovery index for evaluation, acceptance, observability and red teaming | Curated list; inspect each asset individually |

## Resilience

| Source | Reusable content | Access/license note |
|---|---|---|
| jposluns/grc_library | Backup/recovery and broader GRC document patterns | Backup/recovery procedure states CC BY-SA 4.0; verify file-level license before reuse |

## Reusable standards/methods to investigate

- BPMN 2.0 — process modeling
- TOGAF ADM — enterprise architecture lifecycle
- ArchiMate — architecture modeling
- RACI — responsibility assignment
- SIPOC — process scoping
- ITIL practices — IT service management
- NIST AI RMF — AI risk management
- ISO/IEC 42001 — AI management system
- ISO 27001 — information security management
- ISO 22301 — business continuity management
- OpenLineage — data/process lineage
- OpenTelemetry — observability/telemetry
- PDCA — continuous improvement
- DMAIC — process improvement
- A3 — structured problem solving
- OKR — objectives and key results

## Evidence notes

Current web research confirms that Archie provides an open-source governed EA platform with capability maps and value streams; OpenMetadata provides catalog, lineage, quality, governance and MCP capabilities; AgentGovBench and proofagent-harness provide reusable agent evaluation/testing infrastructure; and ZITADEL provides open-source IAM capabilities. These sources should be re-verified at adoption time because licenses, releases and feature sets change. citeturn0search0turn0search6turn1search0turn1search1turn1search2

## Adoption status

| Asset | Current Nivy status | Next action |
|---|---|---|
| Archie EA | DISCOVERED | Compare with Turbo EA/other EA tools |
| Turbo EA | DISCOVERED | Inspect GitHub license/features |
| EA Reference Catalog | DISCOVERED | Import capability/value-stream vocabulary |
| ZITADEL | DISCOVERED | Compare with Keycloak/AuthentiK |
| SAFi | DISCOVERED | Inspect architecture and license |
| AgentOps Mesh | DISCOVERED | Evaluate as governance reference |
| OpenMetadata | DISCOVERED | Evaluate as data/AI context layer |
| OpenLineage | DISCOVERED | Evaluate for lineage standard |
| AgentGovBench | DISCOVERED | Use governance scenarios in agent test suite |
| proofagent-harness | DISCOVERED | Evaluate CI/agent regression testing |
| jposluns/grc_library | DISCOVERED | Extract generic resilience templates subject to license check |

**Important:** Discovery does not mean adoption. No source is considered production-approved merely because it appears here.
