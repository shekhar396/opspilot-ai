from sqlalchemy.orm import Session

from app.models.alert import AlertHistory


MAX_ALERT_LIMIT = 500


def _clamp_alert_limit(limit: int) -> int:
    return min(limit, MAX_ALERT_LIMIT)


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
        .limit(_clamp_alert_limit(limit))
        .all()
    )


def get_filtered_alerts(
    db: Session,
    severity: str | None = None,
    source: str | None = None,
    limit: int = 100,
) -> list[AlertHistory]:
    query = db.query(AlertHistory)

    if severity is not None:
        query = query.filter(AlertHistory.severity == severity)

    if source is not None:
        query = query.filter(AlertHistory.source == source)

    return (
        query.order_by(AlertHistory.created_at.desc())
        .limit(_clamp_alert_limit(limit))
        .all()
    )


def get_alert_summary(db: Session) -> dict:
    latest_alert = (
        db.query(AlertHistory)
        .order_by(AlertHistory.created_at.desc())
        .first()
    )

    return {
        "total_alerts": db.query(AlertHistory).count(),
        "warning_alerts": db.query(AlertHistory)
        .filter(AlertHistory.severity == "warning")
        .count(),
        "critical_alerts": db.query(AlertHistory)
        .filter(AlertHistory.severity == "critical")
        .count(),
        "system_alerts": db.query(AlertHistory)
        .filter(AlertHistory.source == "system")
        .count(),
        "docker_alerts": db.query(AlertHistory)
        .filter(AlertHistory.source == "docker")
        .count(),
        "latest_alert_time": latest_alert.created_at if latest_alert else None,
    }
