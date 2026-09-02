#!/usr/bin/env bash
set -Eeuo pipefail

# E.10 restore test. Creates an isolated temporary database, restores the latest
# custom-format dump, and verifies that Odoo's database is structurally readable.

BACKUP_DIR="${BACKUP_DIR:-./backups/postgres}"
POSTGRES_CONTAINER="${POSTGRES_CONTAINER:-billion-dreams-united-aios-dev-postgres-1}"
POSTGRES_USER="${POSTGRES_USER:-odoo}"
SOURCE_DB="${SOURCE_DB:-odoo}"
TEST_DB="${TEST_DB:-odoo_restore_test}"

LATEST="$(find "$BACKUP_DIR" -type f -name "${SOURCE_DB}-*.dump" -print | sort | tail -n 1)"
if [[ -z "$LATEST" ]]; then
  echo "ERROR: no PostgreSQL backup found in $BACKUP_DIR" >&2
  exit 1
fi

if ! docker inspect -f '{{.State.Running}}' "$POSTGRES_CONTAINER" 2>/dev/null | grep -qx true; then
  echo "ERROR: PostgreSQL container is not running: $POSTGRES_CONTAINER" >&2
  exit 1
fi

# Ensure a clean isolated test database.
docker exec "$POSTGRES_CONTAINER" psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 \
  -c "DROP DATABASE IF EXISTS ${TEST_DB};" \
  -c "CREATE DATABASE ${TEST_DB} OWNER ${POSTGRES_USER};"

# Copy the archive into the container and restore it.
docker cp "$LATEST" "$POSTGRES_CONTAINER:/tmp/restore-test.dump"
docker exec "$POSTGRES_CONTAINER" pg_restore -U "$POSTGRES_USER" -d "$TEST_DB" --exit-on-error /tmp/restore-test.dump

# Basic structural verification.
TABLE_COUNT="$(docker exec "$POSTGRES_CONTAINER" psql -U "$POSTGRES_USER" -d "$TEST_DB" -Atc "SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog','information_schema');")"
if [[ "$TABLE_COUNT" -le 0 ]]; then
  echo "ERROR: restore completed but no application tables were found" >&2
  exit 1
fi

docker exec "$POSTGRES_CONTAINER" psql -U "$POSTGRES_USER" -d postgres -v ON_ERROR_STOP=1 -c "DROP DATABASE ${TEST_DB};"
docker exec "$POSTGRES_CONTAINER" rm -f /tmp/restore-test.dump

cat <<EOF
RESTORE_TEST_OK
source=$LATEST
test_database=$TEST_DB
application_table_count=$TABLE_COUNT
EOF
