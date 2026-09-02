from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any

import httpx
import psycopg
import yaml
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
REGISTRY = yaml.safe_load((ROOT / "registry.yaml").read_text())
app = FastAPI(title="Billion Dreams United AIOS Runtime", version="1.3.0")

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

class OutboxAck(BaseModel):
    outbox_id: int
    consumer: str
    success: bool = True
    error: str | None = None
    retry_delay_seconds: int = 60

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
        conn.execute("BEGIN")
        conn.execute(
            """INSERT INTO aios_events
            (event_id,event_type,source,execution_id,agent_id,entity_type,entity_id,payload,provenance,schema_version)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s::jsonb,%s)""",
            (event_id, event_type, source, execution_id, agent_id, entity_type, entity_id, json.dumps(payload), json.dumps(provenance or {}), schema_version),
        )
        conn.execute(
            """INSERT INTO aios_outbox (event_id,event_type,payload)
            VALUES (%s,%s,%s::jsonb)""",
            (event_id, event_type, json.dumps({
                "event_id": event_id,
                "event_type": event_type,
                "execution_id": execution_id,
                "agent_id": agent_id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "source": source,
                "payload": payload,
                "provenance": provenance or {},
                "schema_version": schema_version,
            })),
        )
        conn.commit()
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

def require_db() -> str:
    url = db_url()
    if not url:
        raise HTTPException(status_code=503, detail={"error": "database_not_configured"})
    return url

@app.get("/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": "aios-runtime", "version": "1.3.0", "database": "configured" if db_url() else "not_configured"}

@app.get("/v1/agents")
def list_agents() -> dict[str, Any]:
    return {"agents": REGISTRY.get("agents", {}), "count": len(REGISTRY.get("agents", {}))}

@app.get("/v1/agents/{agent_id}")
def get_agent(agent_id: str) -> dict[str, Any]:
    return {"agent_id": agent_id, **agent(agent_id)}

@app.post("/v1/events")
def ingest_event(request: EventIn) -> dict[str, Any]:
    event_id = persist_event(request.event_type, request.execution_id, request.agent_id or "n8n", request.payload, request.source, request.entity_type, request.entity_id, request.provenance, request.schema_version)
    return {"status": "accepted", "event_id": event_id, "execution_id": request.execution_id, "event_type": request.event_type, "outbox": "queued"}

@app.get("/v1/outbox/claim")
def claim_outbox(consumer: str = Query(..., min_length=1, max_length=120), limit: int = Query(10, ge=1, le=100), lease_seconds: int = Query(300, ge=30, le=3600)) -> dict[str, Any]:
    url = require_db()
    with psycopg.connect(url) as conn:
        rows = conn.execute(
            """WITH candidates AS (
                SELECT o.outbox_id
                FROM aios_outbox o
                WHERE (o.status='pending' AND o.available_at <= NOW())
                   OR (o.status='processing' AND o.locked_at < NOW() - (%s * INTERVAL '1 second'))
                ORDER BY o.outbox_id
                FOR UPDATE SKIP LOCKED
                LIMIT %s
            )
            UPDATE aios_outbox o
            SET status='processing', attempts=o.attempts+1, locked_at=NOW(), locked_by=%s
            FROM candidates c
            WHERE o.outbox_id=c.outbox_id
            RETURNING o.outbox_id,o.event_id,o.event_type,o.payload,o.attempts""",
            (lease_seconds, limit, consumer),
        ).fetchall()
        conn.commit()
    return {"consumer": consumer, "count": len(rows), "events": [
        {"outbox_id": r[0], "event_id": str(r[1]), "event_type": r[2], "payload": r[3], "attempts": r[4]} for r in rows
    ]}

@app.post("/v1/outbox/ack")
def ack_outbox(request: OutboxAck) -> dict[str, Any]:
    url = require_db()
    with psycopg.connect(url) as conn:
        if request.success:
            row = conn.execute(
                """INSERT INTO aios_outbox_deliveries(outbox_id,consumer)
                VALUES (%s,%s) ON CONFLICT DO NOTHING RETURNING outbox_id""",
                (request.outbox_id, request.consumer),
            ).fetchone()
            conn.execute(
                """UPDATE aios_outbox SET status='delivered',delivered_at=COALESCE(delivered_at,NOW()),locked_at=NULL,locked_by=NULL
                WHERE outbox_id=%s""",
                (request.outbox_id,),
            )
            conn.commit()
            return {"status": "acked", "outbox_id": request.outbox_id, "new_delivery": bool(row)}
        attempts = conn.execute("SELECT attempts FROM aios_outbox WHERE outbox_id=%s", (request.outbox_id,)).fetchone()
        if not attempts:
            raise HTTPException(status_code=404, detail={"error": "unknown_outbox", "outbox_id": request.outbox_id})
        max_attempts = int(os.getenv("OUTBOX_MAX_ATTEMPTS", "8"))
        terminal = attempts[0] >= max_attempts
        conn.execute(
            """UPDATE aios_outbox SET status=%s,available_at=NOW()+(%s * INTERVAL '1 second'),locked_at=NULL,locked_by=NULL,last_error=%s
            WHERE outbox_id=%s""",
            ("dead_letter" if terminal else "pending", request.retry_delay_seconds, request.error or "delivery_failed", request.outbox_id),
        )
        conn.commit()
    return {"status": "dead_lettered" if terminal else "retry_scheduled", "outbox_id": request.outbox_id}

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
