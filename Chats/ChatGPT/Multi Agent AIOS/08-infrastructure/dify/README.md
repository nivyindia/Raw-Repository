# Dify — isolated AIOS deployment

## Purpose

Dify is deployed as a separate Docker Compose stack rather than being merged into the core Odoo/PostgreSQL/n8n compose file. This matches the AIOS architecture and keeps Dify's upstream service dependencies isolated.

## Source of truth

- Repository: `https://github.com/langgenius/dify`
- Deployment directory: upstream `docker/`
- Upstream generated compose is used instead of maintaining a copied, potentially stale compose file in AIOS.

## Bootstrap

From this directory:

```bash
chmod +x bootstrap.sh
./bootstrap.sh
```

Optional pinning:

```bash
DIFY_REF=<tag-or-commit> ./bootstrap.sh
```

## Runtime

The bootstrap script clones the upstream Dify repository into `./.runtime/dify`, creates `.env` from the upstream example when required, and runs the upstream Docker Compose stack.

Before any staging/production deployment:

1. Pin `DIFY_REF` to a reviewed release/tag or commit.
2. Replace every development/default secret in `.env`.
3. Configure persistent storage and backups.
4. Put Dify behind the approved reverse proxy/TLS layer.
5. Restrict network access according to the AIOS IAM and risk policies.
6. Verify Dify health and login manually.

## AIOS integration boundary

Dify is the AI application/RAG/workflow layer. Core business records remain governed by Odoo/PostgreSQL; orchestration remains with n8n/LangGraph; secrets remain governed by the IAM policy.

## Verification gate

E.4 is artifact-complete when this deployment wrapper exists. It becomes **runtime-complete only after Docker Compose is actually started and Dify is manually health/login verified on the target machine**.
