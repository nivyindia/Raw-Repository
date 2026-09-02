#!/usr/bin/env bash
set -euo pipefail

# E.1 — Docker install + verification bootstrap for Billion Dreams United AIOS
# Supported target: Debian/Ubuntu-like Linux VPS/laptop.
# Run with sudo privileges on the target machine.

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "This bootstrap targets Linux. Use the official Docker installation method for other OSes."
  exit 1
fi

if command -v docker >/dev/null 2>&1; then
  echo "Docker already installed: $(docker --version)"
else
  echo "Installing Docker Engine using Docker's convenience installer..."
  curl -fsSL https://get.docker.com | sh
fi

# Verify Docker CLI and daemon.
docker --version
sudo docker version
sudo docker info >/dev/null

# Verify Compose v2 plugin.
if docker compose version >/dev/null 2>&1; then
  docker compose version
else
  echo "ERROR: Docker Compose v2 plugin is unavailable. Install/enable the Compose plugin before E.2."
  exit 1
fi

# Functional smoke test.
sudo docker run --rm hello-world

cat <<'EOF'

E.1 verification passed:
- Docker CLI available
- Docker daemon reachable
- Docker Compose v2 available
- hello-world container executed successfully

Next: E.2 — create the development Docker Compose stack for Odoo + PostgreSQL.
EOF
