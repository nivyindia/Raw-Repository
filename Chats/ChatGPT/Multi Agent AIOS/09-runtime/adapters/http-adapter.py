from __future__ import annotations

import os
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="AIOS Runtime Adapter Bridge", version="1.0.0")

class Invocation(BaseModel):
    agent_id: str
    execution_id: str
    input: dict[str, Any] = Field(default_factory=dict)

def target_url() -> str | None:
    return os.getenv("ADAPTER_TARGET_URL")

@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "target_configured": bool(target_url())}

@app.post("/v1/agents/{agent_id}/invoke")
async def invoke(agent_id: str, request: Invocation) -> dict[str, Any]:
    if request.agent_id != agent_id:
        raise HTTPException(status_code=400, detail={"error": "agent_id_mismatch"})
    target = target_url()
    if not target:
        raise HTTPException(status_code=503, detail={"error": "adapter_target_not_configured"})
    try:
        async with httpx.AsyncClient(timeout=float(os.getenv("ADAPTER_TIMEOUT_SECONDS", "180"))) as client:
            response = await client.post(
                f"{target.rstrip('/')}/v1/agents/{agent_id}/invoke",
                json=request.model_dump(),
            )
            response.raise_for_status()
            result = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(status_code=502, detail={"error": "adapter_target_unreachable", "message": str(exc)}) from exc
    return {"execution_id": request.execution_id, "agent_id": agent_id, "adapter_result": result}
