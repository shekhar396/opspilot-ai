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


class AlertSummaryResponse(BaseModel):
    total_alerts: int
    warning_alerts: int
    critical_alerts: int
    system_alerts: int
    docker_alerts: int
    latest_alert_time: datetime | None
