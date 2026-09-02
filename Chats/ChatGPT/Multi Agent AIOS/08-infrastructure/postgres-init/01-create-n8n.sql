-- Development-only bootstrap for the dedicated n8n database.
-- Password is supplied through the same environment variable used by n8n.
CREATE USER n8n WITH PASSWORD 'change-me-dev-only';
CREATE DATABASE n8n OWNER n8n;
GRANT ALL PRIVILEGES ON DATABASE n8n TO n8n;
