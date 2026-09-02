# E.7 — Email Infrastructure

This step defines the AIOS email layer as two separate responsibilities:

- **Mautic** — marketing automation, contacts, campaigns and orchestration.
- **Postal** — transactional/delivery SMTP infrastructure and mail-server operations.

## Mautic

```bash
cd mautic
cp .env.example .env
# Replace all example passwords.
docker compose up -d
```

Mautic is exposed only on `127.0.0.1:8080` by default. Put it behind the approved reverse proxy/HTTPS layer before external exposure.

The compose uses the official Mautic Apache image and MariaDB. Mautic's official container documentation recommends Apache over FPM for the current Docker image family.

## Postal

Postal is intentionally **not** embedded in the main AIOS compose stack. Postal's own documentation recommends a dedicated server and lists Docker, Compose, MariaDB >= 10.6 and the Postal installation helper as prerequisites.

On a dedicated mail server:

```bash
export POSTAL_HOSTNAME=postal.example.com
sudo -E ./postal/bootstrap.sh
```

Then complete the DNS, MariaDB/RabbitMQ configuration and Postal initialization described by the generated output.

## AIOS integration boundary

`Mautic -> Postal` is the preferred marketing-email delivery boundary. Agents and workflows should not receive unrestricted SMTP credentials. Delivery actions must pass through the approved communication policy, suppression checks and the `svc-postal` service identity.

## Runtime status

GitHub implementation is complete. Runtime deployment/health verification must be performed on the target server. Do not mark E.7 as operational until Mautic is initialized and Postal reports healthy through `postal status`, with a controlled test email successfully delivered.
