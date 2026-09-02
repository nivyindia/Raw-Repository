# Cal.diy — AIOS Booking Layer

## Purpose
Self-hosted scheduling/booking layer for the Billion Dreams United OS. n8n can consume booking webhooks and update Odoo/PostgreSQL through governed workflows.

## Current choice
Use **Cal.diy** for the open-source/self-hosted community edition. In April 2026, Cal.com moved its open-source community code to Cal.diy under MIT; commercial/enterprise Cal.com is separate. The project remains intended for self-hosting.

## Start

```bash
cp .env.example .env
# Replace every change-me value with strong secrets.
docker compose up -d
```

Then verify:

```bash
docker compose ps
docker compose logs --tail=100 caldiy
curl -fsS http://127.0.0.1:3000/api/health
```

## Security
- Keep port 3000 bound to localhost behind the AIOS reverse proxy.
- Never commit `.env` or production secrets.
- Use a dedicated production PostgreSQL instance/credentials rather than development defaults.
- Put public TLS, DNS, rate limiting and authentication controls at the reverse-proxy layer.

## AIOS integration boundary
`Cal.diy -> webhook -> n8n -> policy/approval checks -> Odoo/PostgreSQL/event bus`.

Booking events must be idempotent and traceable with a correlation ID. External communication or other material actions remain subject to the AIOS communication and risk policies.

## Runtime note
The repository artifact is implemented, but actual Docker startup/booking verification must be performed on the target VPS/laptop.
