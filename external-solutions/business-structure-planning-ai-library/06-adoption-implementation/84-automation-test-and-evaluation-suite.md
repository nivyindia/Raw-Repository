# Automation Test & Evaluation Suite

**Status:** v1.0 — 2026-09-16

## Purpose

Prevent promotion based on demos alone.

## Test layers

### Functional

- normal input
- missing input
- malformed input
- duplicate event
- conflicting records
- empty result
- tool timeout
- tool error

### Control

- unauthorized user
- unauthorized agent
- unauthorized tool
- sensitive-data boundary
- approval bypass attempt
- expired approval
- wrong-system write
- excessive autonomy

### Operational

- retry
- timeout
- partial failure
- duplicate webhook
- downstream outage
- queue backlog
- rollback
- manual fallback

### Quality

- factuality
- source/provenance completeness
- structured-output validity
- instruction adherence
- hallucination rate
- human correction rate

### Economic

- average latency
- p95 latency
- model cost
- tool/API cost
- workflow cost
- human review time
- cost per successful outcome

## Minimum test record

`test_id | workflow_id | scenario | input_ref | expected | actual | pass/fail | severity | evidence | model/version | date | reviewer`

## Promotion thresholds

A production workflow must have:

- zero unresolved critical control failures
- no known unauthorized write path
- tested rollback/manual fallback
- documented owner
- reproducible regression set
- acceptable cost/latency for its business value
- explicit approval policy

Quality thresholds should be workflow-specific rather than one universal score.

## Continuous evaluation

Run regression tests when:

- model changes
- prompt/skill changes
- connector changes
- workflow changes
- policy changes
- source system schema changes
- agent autonomy changes

## Red-team cases

Attempt to make the agent:

- reveal secrets
- exceed permissions
- bypass approval
- invent evidence
- act on stale context
- duplicate financial/customer actions
- follow untrusted instructions from external content
- continue after kill/quarantine

## Evidence

Every failed test creates a remediation item before promotion.
