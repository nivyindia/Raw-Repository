-- Durable AIOS runtime state and outbox.
-- This file runs only on first PostgreSQL volume initialization.
CREATE TABLE IF NOT EXISTS aios_executions (
    execution_id TEXT PRIMARY KEY,
    agent_id TEXT NOT NULL,
    status TEXT NOT NULL,
    runtime TEXT NOT NULL,
    input JSONB NOT NULL DEFAULT '{}'::jsonb,
    result JSONB,
    error JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS aios_events (
    event_id UUID PRIMARY KEY,
    event_type TEXT NOT NULL,
    source TEXT NOT NULL,
    execution_id TEXT NOT NULL,
    agent_id TEXT,
    entity_type TEXT,
    entity_id TEXT,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    provenance JSONB NOT NULL DEFAULT '{}'::jsonb,
    schema_version TEXT NOT NULL DEFAULT '1.0',
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_aios_events_type_occurred
    ON aios_events (event_type, occurred_at DESC);
CREATE INDEX IF NOT EXISTS idx_aios_events_execution
    ON aios_events (execution_id);

CREATE TABLE IF NOT EXISTS aios_outbox (
    outbox_id BIGSERIAL PRIMARY KEY,
    event_id UUID NOT NULL UNIQUE REFERENCES aios_events(event_id) ON DELETE CASCADE,
    event_type TEXT NOT NULL,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','processing','delivered','dead_letter')),
    attempts INTEGER NOT NULL DEFAULT 0,
    available_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    locked_at TIMESTAMPTZ,
    locked_by TEXT,
    delivered_at TIMESTAMPTZ,
    last_error TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_aios_outbox_claim
    ON aios_outbox (status, available_at, outbox_id);

CREATE TABLE IF NOT EXISTS aios_outbox_deliveries (
    outbox_id BIGINT NOT NULL REFERENCES aios_outbox(outbox_id) ON DELETE CASCADE,
    consumer TEXT NOT NULL,
    delivered_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (outbox_id, consumer)
);
