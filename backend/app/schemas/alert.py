from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class AlertResponse(BaseModel):
    id: int
    host: str
    issue: str
    severity: str
    source: str
    details: dict[str, Any]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
