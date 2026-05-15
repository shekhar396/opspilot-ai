from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.alert import AlertResponse, AlertSummaryResponse
from app.services.alert_history_service import (
    get_alert_by_id,
    get_alert_summary,
    get_filtered_alerts,
    get_recent_alerts,
)

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get("/", response_model=list[AlertResponse])
def list_alerts(
    severity: str | None = None,
    source: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return get_filtered_alerts(db, severity=severity, source=source, limit=limit)


@router.get("/recent", response_model=list[AlertResponse])
def recent_alerts(limit: int = 10, db: Session = Depends(get_db)):
    return get_recent_alerts(db, limit=limit)


@router.get("/summary", response_model=AlertSummaryResponse)
def alert_summary(db: Session = Depends(get_db)):
    return get_alert_summary(db)


@router.get("/{alert_id}", response_model=AlertResponse)
def alert_detail(alert_id: int, db: Session = Depends(get_db)):
    alert = get_alert_by_id(db, alert_id)

    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    return alert
