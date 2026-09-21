# Canonical Dynamic Context Assembly Contract

Entity/Data Model → Allowed Fields/Methods → Relations → Hints → Policy Filter → Context Assembly → Prompt/Tool Request → Output Validation

## Purpose
Provide agents and executives with relevant enterprise context without exposing the entire underlying data model.

## Required controls
- Explicit allowlist of fields/methods.
- Tenant/department/role scoping.
- Sensitive-data filtering.
- Context size/token budget.
- Provenance for supplied facts.
- Freshness metadata.
- Injection-resistant serialization.
- Audit of context supplied to consequential actions.
