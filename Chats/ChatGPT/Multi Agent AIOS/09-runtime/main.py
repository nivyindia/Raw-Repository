from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import httpx
import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
REGISTRY = yaml.safe_load((ROOT / "registry.yaml").read_text())

app = FastAPI(title="Billion Dreams United AIOS Runtime", version="1.0.0")


class Invocation(BaseModel):
    input: dict[str, Any] = Field(default_factory=dict)
    execution_id: str | None = None
    approval_token: str | None = None


def runtime_url(runtime: str) -> str | None:
    env_name = REGISTRY["runtimes"][runtime]["base_url_env"]
    return os.getenv(env_name)


def agent(agent_id: str) -> dict[str, Any]:
    record = REGISTRY.get("agents", {}).get(agent_id)
    if not record:
        raise HTTPException(status_code=404, detail={"error": "unknown_agent", "agent_id": agent_id})
    return record


@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": "aios-runtime", "version": "1.0.0"}


@app.get("/v1/agents")
def list_agents() -> dict[str, Any]:
    return {"agents": REGISTRY.get("agents", {}), "count": len(REGISTRY.get("agents", {}))}


@app.get("/v1/agents/{agent_id}")
def get_agent(agent_id: str) -> dict[str, Any]:
    return {"agent_id": agent_id, **agent(agent_id)}


@app.post("/v1/agents/{agent_id}/invoke")
async def invoke(agent_id: str, request: Invocation) -> dict[str, Any]:
    config = agent(agent_id)
    runtime = config["runtime"]

    if config.get("approval_required") and not request.approval_token:
        return {
            "status": "approval_required",
            "agent_id": agent_id,
            "runtime": runtime,
            "message": "This agent is governed as an approval-gated action. No downstream execution was attempted.",
        }

    base_url = runtime_url(runtime)
    if not base_url:
        return {
            "status": "runtime_not_configured",
            "agent_id": agent_id,
            "runtime": runtime,
            "required_env": REGISTRY["runtimes"][runtime]["base_url_env"],
            "message": "Configure the runtime adapter URL before execution.",
        }

    payload = {
        "agent_id": agent_id,
        "execution_id": request.execution_id,
        "input": request.input,
    }
    try:
        async with httpx.AsyncClient(timeout=float(os.getenv("RUNTIME_TIMEOUT_SECONDS", "120"))) as client:
            response = await client.post(f"{base_url.rstrip('/')}/v1/agents/{agent_id}/invoke", json=payload)
            response.raise_for_status()
            downstream = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail={"error": "runtime_unreachable", "runtime": runtime, "agent_id": agent_id, "message": str(exc)},
        ) from exc

    return {
        "status": "executed",
        "agent_id": agent_id,
        "runtime": runtime,
        "result": downstream,
    }
