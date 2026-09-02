#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-llama3.2:3b}"

# Pull the small default local model, then verify it is registered.
docker compose -f docker-compose.yml exec -T ollama ollama pull "$MODEL"
docker compose -f docker-compose.yml exec -T ollama ollama list

# Verify LiteLLM can reach the local model gateway.
curl -fsS http://localhost:4000/health/liveliness >/dev/null
echo "E.5 bootstrap verification passed for $MODEL"
