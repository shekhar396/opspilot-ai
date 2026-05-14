from sqlalchemy.orm import Session

from app.models.alert import AlertHistory


def create_alert(db: Session, alert_data: dict) -> AlertHistory:
    alert = AlertHistory(
        host=alert_data.get("host", "unknown-host"),
        issue=alert_data.get("issue", "Unknown Alert"),
        severity=alert_data.get("severity", "warning"),
        source=alert_data.get("source", "system"),
        details=alert_data.get("details", {}),
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert


def get_recent_alerts(db: Session, limit: int = 10) -> list[AlertHistory]:
    return (
        db.query(AlertHistory)
        .order_by(AlertHistory.created_at.desc())
        .limit(limit)
        .all()
    )


def get_alert_by_id(db: Session, alert_id: int) -> AlertHistory | None:
    return db.query(AlertHistory).filter(AlertHistory.id == alert_id).first()


def get_all_alerts(db: Session, limit: int = 100) -> list[AlertHistory]:
    return (
        db.query(AlertHistory)
        .order_by(AlertHistory.created_at.desc())
        .limit(limit)
        .all()
    )
