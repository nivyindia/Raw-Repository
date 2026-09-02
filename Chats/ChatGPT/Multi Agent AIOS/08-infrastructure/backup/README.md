# E.10 — PostgreSQL + Odoo Backup and Restore

## Scope

This backup layer protects the PostgreSQL database used by Odoo. PostgreSQL `pg_dump` produces a consistent database backup and custom-format archives can be restored with `pg_restore`. citeturn0search7turn0search4

## Automated backup

```bash
chmod +x backup-postgres-odoo.sh
BACKUP_DIR=/srv/aios/backups/postgres ./backup-postgres-odoo.sh
```

The script:

1. Verifies the PostgreSQL container is running.
2. Creates a compressed custom-format `pg_dump` archive.
3. Captures cluster globals.
4. Verifies the archive can be listed by `pg_restore`.
5. Writes a SHA-256 checksum.
6. Applies a configurable retention period.

Default retention is 14 days.

## Restore test

After at least one backup exists:

```bash
chmod +x restore-test.sh
BACKUP_DIR=/srv/aios/backups/postgres ./restore-test.sh
```

The test restores the latest backup into an isolated temporary database, verifies application tables exist, then removes the test database.

## Scheduling

Use cron or a systemd timer on the Docker host. Recommended initial schedule: daily during the lowest expected database activity window. Keep backups outside the application repository and preferably on separate storage.

## E.10 completion gate

The repository artifacts are implemented. **E.10 is not runtime-complete until the backup script has produced a real archive and `restore-test.sh` has completed successfully on the target Docker host.**

The restore test is intentionally separate from repository CI because it requires a running PostgreSQL/Odoo environment and real backup data.

## Security

Do not commit generated backups, database credentials, `.env` files, or backup storage into Git. Restrict backup files to authorized operators and encrypt off-host storage.
