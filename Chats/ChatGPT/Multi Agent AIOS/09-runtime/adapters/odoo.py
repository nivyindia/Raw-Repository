from __future__ import annotations

import os
import xmlrpc.client
from typing import Any

class OdooClient:
    """Minimal CRM adapter. Odoo remains the commercial system of record."""

    def __init__(self) -> None:
        self.url = os.getenv("ODOO_URL", "http://odoo:8069").rstrip("/")
        self.db = os.environ["ODOO_DB"]
        self.username = os.environ["ODOO_USERNAME"]
        self.password = os.environ["ODOO_PASSWORD"]
        common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common", allow_none=True)
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        if not self.uid:
            raise RuntimeError("Odoo authentication failed")
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object", allow_none=True)

    def _execute(self, model: str, method: str, *args: Any, **kwargs: Any) -> Any:
        return self.models.execute_kw(self.db, self.uid, self.password, model, method, list(args), kwargs)

    def upsert_lead(self, values: dict[str, Any], lead_id: int | None = None) -> int:
        allowed = {
            "name", "contact_name", "email_from", "phone", "website",
            "description", "partner_name", "type", "user_id", "team_id",
            "priority", "expected_revenue", "probability", "tag_ids",
        }
        safe_values = {key: value for key, value in values.items() if key in allowed}
        if lead_id:
            self._execute("crm.lead", "write", [lead_id, safe_values])
            return lead_id
        return int(self._execute("crm.lead", "create", safe_values))

    def find_by_email(self, email: str) -> list[int]:
        if not email:
            return []
        return list(self._execute("crm.lead", "search", [[("email_from", "=", email)]], limit=10))
