from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.alert import AlertResponse
from app.services.alert_history_service import (
    get_alert_by_id,
    get_all_alerts,
    get_recent_alerts,
)

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get("/", response_model=list[AlertResponse])
def list_alerts(limit: int = 100, db: Session = Depends(get_db)):
    return get_all_alerts(db, limit=limit)


@router.get("/recent", response_model=list[AlertResponse])
def recent_alerts(limit: int = 10, db: Session = Depends(get_db)):
    return get_recent_alerts(db, limit=limit)


@router.get("/{alert_id}", response_model=AlertResponse)
def alert_detail(alert_id: int, db: Session = Depends(get_db)):
    alert = get_alert_by_id(db, alert_id)

    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    return alert
