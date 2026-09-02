#!/usr/bin/env bash
set -euo pipefail

POSTAL_DIR="${POSTAL_DIR:-/opt/postal}"
POSTAL_HOSTNAME="${POSTAL_HOSTNAME:?Set POSTAL_HOSTNAME, e.g. postal.example.com}"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Run as root (or with sudo)." >&2
  exit 1
fi

command -v docker >/dev/null || { echo "Docker is required." >&2; exit 1; }
command -v git >/dev/null || { echo "Git is required." >&2; exit 1; }
command -v curl >/dev/null || { echo "curl is required." >&2; exit 1; }
command -v jq >/dev/null || { echo "jq is required." >&2; exit 1; }

git clone https://github.com/postalserver/install "$POSTAL_DIR/install" 2>/dev/null || git -C "$POSTAL_DIR/install" pull --ff-only
ln -sf "$POSTAL_DIR/install/bin/postal" /usr/local/bin/postal

mkdir -p "$POSTAL_DIR/config" "$POSTAL_DIR/caddy-data"

if [[ ! -f "$POSTAL_DIR/config/postal.yml" ]]; then
  cd "$POSTAL_DIR"
  postal bootstrap "$POSTAL_HOSTNAME"
  echo "Postal bootstrap generated config. Edit $POSTAL_DIR/config/postal.yml with real MariaDB/RabbitMQ credentials before continuing."
else
  echo "Postal config already exists: $POSTAL_DIR/config/postal.yml"
fi

cat <<'EOF'
Next steps:
  1. Configure DNS (A/AAAA, MX, SPF, DKIM, DMARC and tracking records).
  2. Provide a dedicated MariaDB >= 10.6 and RabbitMQ instance.
  3. Review postal.yml and secrets.
  4. Run: postal initialize
  5. Run: postal make-user
  6. Run: postal start
  7. Run: postal status

Postal should be deployed on a dedicated mail server; do not combine it with the main AIOS VPS unless capacity and mail-network requirements have been explicitly reviewed.
EOF
