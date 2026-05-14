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
