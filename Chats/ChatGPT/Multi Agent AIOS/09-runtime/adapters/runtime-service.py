from __future__ import annotations

import os
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

KIND = os.getenv("RUNTIME_KIND", "generic").lower()
TARGET = os.getenv("RUNTIME_TARGET_URL", "").rstrip("/")
API_KEY = os.getenv("RUNTIME_API_KEY", "")
ASSISTANT_ID = os.getenv("LANGGRAPH_ASSISTANT_ID", "")
WORKFLOW_ID = os.getenv("DIFY_WORKFLOW_ID", "")

app = FastAPI(title=f"AIOS {KIND} Runtime Adapter", version="1.0.0")

class Invocation(BaseModel):
    agent_id: str
    execution_id: str
    input: dict[str, Any] = Field(default_factory=dict)


def headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}


def build_request(request: Invocation) -> tuple[str, dict[str, Any], dict[str, str]]:
    if not TARGET:
        raise HTTPException(status_code=503, detail={"error": "runtime_target_not_configured", "runtime": KIND})
    h = headers()
    if KIND == "langgraph":
        path = os.getenv("LANGGRAPH_INVOKE_PATH", "/runs/wait")
        body = {"assistant_id": ASSISTANT_ID or request.agent_id, "input": request.input, "metadata": {"execution_id": request.execution_id, "agent_id": request.agent_id}}
    elif KIND == "dify":
        path = os.getenv("DIFY_INVOKE_PATH", "/workflows/run")
        body = {"inputs": request.input, "response_mode": "blocking", "user": request.execution_id}
        if WORKFLOW_ID:
            body["workflow_id"] = WORKFLOW_ID
    else:
        path = os.getenv("RUNTIME_INVOKE_PATH", f"/v1/agents/{request.agent_id}/invoke")
        body = request.model_dump()
    return f"{TARGET}{path}", body, h


@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "runtime": KIND, "target_configured": bool(TARGET)}


@app.post("/v1/agents/{agent_id}/invoke")
async def invoke(agent_id: str, request: Invocation) -> dict[str, Any]:
    if agent_id != request.agent_id:
        raise HTTPException(status_code=400, detail={"error": "agent_id_mismatch"})
    url, body, h = build_request(request)
    try:
        async with httpx.AsyncClient(timeout=float(os.getenv("ADAPTER_TIMEOUT_SECONDS", "180"))) as client:
            response = await client.post(url, json=body, headers=h)
            response.raise_for_status()
            result = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(status_code=502, detail={"error": "runtime_target_failed", "runtime": KIND, "message": str(exc)}) from exc
    return {"status": "executed", "runtime": KIND, "agent_id": agent_id, "execution_id": request.execution_id, "result": result}
