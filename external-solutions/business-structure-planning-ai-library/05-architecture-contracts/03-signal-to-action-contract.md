# Canonical Signal → Action Contract

Sources → Ingest → Normalize → Validate → Score → Contextualize → Decide → Route → Act → Verify → Measure → Learn

## Required fields
signal_id, source, timestamp, subject, signal_type, raw_payload, normalized_payload, confidence, score, context, policy_result, action, owner, outcome, evidence, version

## Controls
- Preserve source provenance.
- Validate timestamps and identity.
- Apply deduplication and confidence thresholds.
- Never turn a signal directly into an irreversible action without the required policy/approval gate.
- Record outcome for feedback and model evaluation.
