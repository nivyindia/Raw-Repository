from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any

import httpx
import psycopg
import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
REGISTRY = yaml.safe_load((ROOT / "registry.yaml").read_text())
app = FastAPI(title="Billion Dreams United AIOS Runtime", version="1.2.0")

class Invocation(BaseModel):
    input: dict[str, Any] = Field(default_factory=dict)
    execution_id: str | None = None
    approval_token: str | None = None

class EventIn(BaseModel):
    event_type: str
    execution_id: str
    agent_id: str | None = None
    entity_type: str | None = None
    entity_id: str | None = None
    source: str = "n8n"
    payload: dict[str, Any] = Field(default_factory=dict)
    provenance: dict[str, Any] = Field(default_factory=dict)
    schema_version: str = "1.0"

def runtime_url(runtime: str) -> str | None:
    return os.getenv(REGISTRY["runtimes"][runtime]["base_url_env"])

def agent(agent_id: str) -> dict[str, Any]:
    record = REGISTRY.get("agents", {}).get(agent_id)
    if not record:
        raise HTTPException(status_code=404, detail={"error": "unknown_agent", "agent_id": agent_id})
    return record

def db_url() -> str | None:
    return os.getenv("AIOS_DATABASE_URL")

def persist_event(event_type: str, execution_id: str, agent_id: str, payload: dict[str, Any], source: str = "aios-runtime", entity_type: str | None = None, entity_id: str | None = None, provenance: dict[str, Any] | None = None, schema_version: str = "1.0") -> str:
    event_id = str(uuid.uuid4())
    url = db_url()
    if not url:
        return event_id
    with psycopg.connect(url) as conn:
        conn.execute(
            """INSERT INTO aios_events
            (event_id,event_type,source,execution_id,agent_id,entity_type,entity_id,payload,provenance,schema_version)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s::jsonb,%s)""",
            (event_id, event_type, source, execution_id, agent_id, entity_type, entity_id, json.dumps(payload), json.dumps(provenance or {}), schema_version),
        )
    return event_id

def persist_execution(execution_id: str, agent_id: str, status: str, runtime: str, input_data: dict[str, Any], result: Any = None, error: Any = None, completed: bool = False) -> None:
    url = db_url()
    if not url:
        return
    with psycopg.connect(url) as conn:
        conn.execute(
            """INSERT INTO aios_executions (execution_id,agent_id,status,runtime,input,result,error,completed_at)
            VALUES (%s,%s,%s,%s,%s::jsonb,%s::jsonb,%s::jsonb,CASE WHEN %s THEN NOW() ELSE NULL END)
            ON CONFLICT (execution_id) DO UPDATE SET status=EXCLUDED.status,result=EXCLUDED.result,error=EXCLUDED.error,completed_at=EXCLUDED.completed_at""",
            (execution_id, agent_id, status, runtime, json.dumps(input_data), json.dumps(result), json.dumps(error), completed),
        )

@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": "aios-runtime", "version": "1.2.0", "database": "configured" if db_url() else "not_configured"}

@app.get("/v1/agents")
def list_agents() -> dict[str, Any]:
    return {"agents": REGISTRY.get("agents", {}), "count": len(REGISTRY.get("agents", {}))}

@app.get("/v1/agents/{agent_id}")
def get_agent(agent_id: str) -> dict[str, Any]:
    return {"agent_id": agent_id, **agent(agent_id)}

@app.post("/v1/events")
def ingest_event(request: EventIn) -> dict[str, Any]:
    event_id = persist_event(request.event_type, request.execution_id, request.agent_id or "n8n", request.payload, request.source, request.entity_type, request.entity_id, request.provenance, request.schema_version)
    return {"status": "accepted", "event_id": event_id, "execution_id": request.execution_id, "event_type": request.event_type}

@app.post("/v1/agents/{agent_id}/invoke")
async def invoke(agent_id: str, request: Invocation) -> dict[str, Any]:
    config = agent(agent_id)
    runtime = config["runtime"]
    execution_id = request.execution_id or str(uuid.uuid4())

    if config.get("approval_required") and not request.approval_token:
        persist_execution(execution_id, agent_id, "approval_required", runtime, request.input)
        persist_event("agent.approval_requested", execution_id, agent_id, {"runtime": runtime})
        return {"status": "approval_required", "agent_id": agent_id, "runtime": runtime, "execution_id": execution_id}

    base_url = runtime_url(runtime)
    if not base_url:
        persist_execution(execution_id, agent_id, "runtime_not_configured", runtime, request.input)
        persist_event("agent.runtime_not_configured", execution_id, agent_id, {"runtime": runtime})
        return {"status": "runtime_not_configured", "agent_id": agent_id, "runtime": runtime, "execution_id": execution_id, "required_env": REGISTRY["runtimes"][runtime]["base_url_env"]}

    persist_execution(execution_id, agent_id, "executing", runtime, request.input)
    persist_event("agent.execution_started", execution_id, agent_id, {"runtime": runtime})
    payload = {"agent_id": agent_id, "execution_id": execution_id, "input": request.input}
    try:
        async with httpx.AsyncClient(timeout=float(os.getenv("RUNTIME_TIMEOUT_SECONDS", "120"))) as client:
            response = await client.post(f"{base_url.rstrip('/')}/v1/agents/{agent_id}/invoke", json=payload)
            response.raise_for_status()
            downstream = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        error = {"error": "runtime_unreachable", "runtime": runtime, "message": str(exc)}
        persist_execution(execution_id, agent_id, "failed", runtime, request.input, error=error, completed=True)
        persist_event("agent.execution_failed", execution_id, agent_id, error)
        raise HTTPException(status_code=502, detail={**error, "agent_id": agent_id}) from exc

    persist_execution(execution_id, agent_id, "succeeded", runtime, request.input, result=downstream, completed=True)
    persist_event("agent.execution_succeeded", execution_id, agent_id, {"runtime": runtime, "result": downstream})
    return {"status": "executed", "agent_id": agent_id, "runtime": runtime, "execution_id": execution_id, "result": downstream}
