-- Billion Dreams United AIOS runtime state + event bus.
-- Postgres owns execution/event/audit state; Odoo remains the commercial system of record.

CREATE TABLE IF NOT EXISTS aios_executions (
  execution_id TEXT PRIMARY KEY,
  agent_id TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('accepted','approval_required','runtime_not_configured','executing','succeeded','failed')),
  runtime TEXT,
  started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at TIMESTAMPTZ,
  input JSONB NOT NULL DEFAULT '{}'::jsonb,
  result JSONB,
  error JSONB
);

CREATE TABLE IF NOT EXISTS aios_events (
  event_id UUID PRIMARY KEY,
  schema_version TEXT NOT NULL DEFAULT '1.0',
  event_type TEXT NOT NULL,
  occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  source TEXT NOT NULL,
  execution_id TEXT,
  agent_id TEXT,
  entity_type TEXT,
  entity_id TEXT,
  payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  provenance JSONB NOT NULL DEFAULT '[]'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_aios_events_execution ON aios_events(execution_id);
CREATE INDEX IF NOT EXISTS idx_aios_events_entity ON aios_events(entity_type, entity_id);
CREATE INDEX IF NOT EXISTS idx_aios_events_type_time ON aios_events(event_type, occurred_at DESC);

CREATE TABLE IF NOT EXISTS aios_agent_runs (
  run_id UUID PRIMARY KEY,
  execution_id TEXT NOT NULL REFERENCES aios_executions(execution_id) ON DELETE CASCADE,
  agent_id TEXT NOT NULL,
  runtime TEXT NOT NULL,
  status TEXT NOT NULL,
  started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at TIMESTAMPTZ,
  input JSONB NOT NULL DEFAULT '{}'::jsonb,
  output JSONB,
  error JSONB
);

CREATE INDEX IF NOT EXISTS idx_aios_agent_runs_execution ON aios_agent_runs(execution_id);

CREATE TABLE IF NOT EXISTS aios_approvals (
  approval_id UUID PRIMARY KEY,
  execution_id TEXT NOT NULL REFERENCES aios_executions(execution_id) ON DELETE CASCADE,
  agent_id TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('pending','approved','rejected','expired')),
  requested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  resolved_at TIMESTAMPTZ,
  requested_by TEXT,
  resolved_by TEXT,
  reason TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_aios_approvals_status ON aios_approvals(status, requested_at DESC);

CREATE TABLE IF NOT EXISTS aios_outbox (
  outbox_id UUID PRIMARY KEY,
  event_id UUID NOT NULL REFERENCES aios_events(event_id) ON DELETE CASCADE,
  destination TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','sent','failed')),
  attempts INTEGER NOT NULL DEFAULT 0,
  next_attempt_at TIMESTAMPTZ,
  last_error TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  sent_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_aios_outbox_pending ON aios_outbox(status, next_attempt_at);
