# Vector + Object Storage

AIOS infrastructure component for persistent vector search and object/file storage.

## Services

- **Qdrant** — vector database for embeddings, semantic retrieval and agent memory.
- **MinIO** — S3-compatible object storage for documents, artifacts and model/application files.

## Start

```bash
docker compose up -d
```

## Local endpoints

- Qdrant REST: `http://127.0.0.1:6333`
- Qdrant gRPC: `127.0.0.1:6334`
- MinIO API: `http://127.0.0.1:9000`
- MinIO Console: `http://127.0.0.1:9001`

## Security

This development compose binds services to localhost. Qdrant authentication is enabled through `QDRANT_API_KEY`; MinIO uses root credentials. Replace all development defaults before shared or production deployment and move secrets to Vaultwarden/environment secret management.

Qdrant's official guidance notes that default deployments can be unauthenticated and recommends authentication/TLS and restricted network binding for secured deployments.

## Persistence

Named Docker volumes:

- `qdrant_storage`
- `minio_data`

## Runtime verification

```bash
docker compose ps
curl -H "api-key: $QDRANT_API_KEY" http://127.0.0.1:6333/healthz
```

MinIO should report healthy in `docker compose ps`.
