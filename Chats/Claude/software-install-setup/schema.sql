-- Sales Funnel n8n workflow - Postgres schema
-- Run this once against the database your "postgresLeadsDb" credential points at,
-- before importing/running the workflows.

-- Phase 1: dedupe check against inbound leads
CREATE TABLE IF NOT EXISTS leads (
    id          SERIAL PRIMARY KEY,
    domain      TEXT,
    email       TEXT,
    company     TEXT,
    created_at  TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_leads_domain ON leads (domain);
CREATE INDEX IF NOT EXISTS idx_leads_email ON leads (email);

-- Phase 5: lost-deal reasons (Price / Competitor / No Budget / Timing / No Response)
CREATE TABLE IF NOT EXISTS lost_deals (
    id          SERIAL PRIMARY KEY,
    company     TEXT,
    email       TEXT,
    lost_reason TEXT,
    lead_score  NUMERIC,
    lost_at     TIMESTAMPTZ DEFAULT now()
);

-- Phase 5: onboarding checklist items for newly-won customers
CREATE TABLE IF NOT EXISTS onboarding_tasks (
    id          SERIAL PRIMARY KEY,
    company     TEXT,
    email       TEXT,
    task        TEXT,
    status      TEXT DEFAULT 'Pending',
    created_at  TIMESTAMPTZ DEFAULT now()
);

-- Phase 5: renewal/upsell reminder dates for won customers
CREATE TABLE IF NOT EXISTS renewal_reminders (
    id            SERIAL PRIMARY KEY,
    company       TEXT,
    email         TEXT,
    renewal_date  DATE,
    reminder_type TEXT DEFAULT 'Renewal',
    sent          BOOLEAN DEFAULT false
);

-- Phase 6: nightly account re-scoring history, used to compute score_delta
CREATE TABLE IF NOT EXISTS account_score_history (
    id            SERIAL PRIMARY KEY,
    company       TEXT,
    email         TEXT,
    current_score NUMERIC,
    score_delta   NUMERIC,
    scored_at     TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_score_history_email_scored_at
    ON account_score_history (email, scored_at DESC);
