from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from odoo import OdooClient

app = FastAPI(title="AIOS Odoo CRM Sync", version="1.0.0")

class LeadUpsert(BaseModel):
    lead_id: int | None = None
    values: dict[str, Any] = Field(default_factory=dict)

class EmailLookup(BaseModel):
    email: str

@app.get("/health")
def health() -> dict[str, Any]:
    try:
        OdooClient()
        return {"status": "ok", "odoo": "connected"}
    except Exception as exc:
        return {"status": "degraded", "odoo": "not_connected", "message": str(exc)}

@app.post("/v1/crm/leads/upsert")
def upsert(request: LeadUpsert) -> dict[str, Any]:
    client = OdooClient()
    lead_id = client.upsert_lead(request.values, request.lead_id)
    return {"status": "upserted", "lead_id": lead_id}

@app.post("/v1/crm/leads/find-by-email")
def find_by_email(request: EmailLookup) -> dict[str, Any]:
    client = OdooClient()
    return {"status": "ok", "lead_ids": client.find_by_email(request.email)}
