#!/usr/bin/env bash
set -euo pipefail

# Dify is deployed from its official Docker directory so the full set of
# generated compose/env files stays version-aligned with upstream.
DIFY_REPO="${DIFY_REPO:-https://github.com/langgenius/dify.git}"
DIFY_REF="${DIFY_REF:-main}"
DIFY_DIR="${DIFY_DIR:-./.runtime/dify}"

mkdir -p "$(dirname "$DIFY_DIR")"

if [ ! -d "$DIFY_DIR/.git" ]; then
  git clone --depth 1 --branch "$DIFY_REF" "$DIFY_REPO" "$DIFY_DIR"
else
  git -C "$DIFY_DIR" fetch --depth 1 origin "$DIFY_REF"
  git -C "$DIFY_DIR" checkout -q "$DIFY_REF"
  git -C "$DIFY_DIR" reset --hard "origin/$DIFY_REF"
fi

cd "$DIFY_DIR/docker"

if [ ! -f .env ]; then
  if [ -f .env.example ]; then
    cp .env.example .env
  else
    echo "ERROR: Dify .env.example not found." >&2
    exit 1
  fi
fi

printf '\nDify source: %s\nDify ref: %s\nCompose directory: %s\n\n' "$DIFY_REPO" "$DIFY_REF" "$PWD"

echo "Review .env and replace all development/default secrets before any non-local deployment."
echo "Starting Dify with the upstream compose stack..."
docker compose up -d

echo
echo "Dify containers requested. Run: docker compose ps"
echo "Dify UI: http://localhost"
