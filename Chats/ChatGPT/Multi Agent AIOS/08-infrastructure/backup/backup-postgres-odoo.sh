#!/usr/bin/env bash
set -Eeuo pipefail

# Billion Dreams United OS — E.10 PostgreSQL/Odoo backup
# Runs pg_dump in custom format and captures cluster globals.
# Intended for cron/systemd execution on the Docker host.

BACKUP_DIR="${BACKUP_DIR:-./backups/postgres}"
RETENTION_DAYS="${RETENTION_DAYS:-14}"
POSTGRES_CONTAINER="${POSTGRES_CONTAINER:-billion-dreams-united-aios-dev-postgres-1}"
POSTGRES_DB="${POSTGRES_DB:-odoo}"
POSTGRES_USER="${POSTGRES_USER:-odoo}"

mkdir -p "$BACKUP_DIR"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
ARCHIVE="$BACKUP_DIR/${POSTGRES_DB}-${STAMP}.dump"
GLOBALS="$BACKUP_DIR/globals-${STAMP}.sql"
CHECKSUM="$ARCHIVE.sha256"

if ! docker inspect -f '{{.State.Running}}' "$POSTGRES_CONTAINER" 2>/dev/null | grep -qx true; then
  echo "ERROR: PostgreSQL container is not running: $POSTGRES_CONTAINER" >&2
  exit 1
fi

echo "[1/4] Creating PostgreSQL custom-format backup..."
docker exec "$POSTGRES_CONTAINER" pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc > "$ARCHIVE"

echo "[2/4] Capturing cluster globals..."
docker exec "$POSTGRES_CONTAINER" pg_dumpall -U "$POSTGRES_USER" --globals-only > "$GLOBALS"

echo "[3/4] Verifying archive integrity/listing..."
docker run --rm -v "$(cd "$BACKUP_DIR" && pwd):/backup:ro" postgres:16-alpine pg_restore -l "/backup/$(basename "$ARCHIVE")" >/dev/null
sha256sum "$ARCHIVE" > "$CHECKSUM"

echo "[4/4] Applying retention policy: ${RETENTION_DAYS} days..."
find "$BACKUP_DIR" -type f \( -name '*.dump' -o -name '*.sql' -o -name '*.sha256' \) -mtime "+$RETENTION_DAYS" -delete

echo "BACKUP_OK archive=$ARCHIVE globals=$GLOBALS checksum=$CHECKSUM"
