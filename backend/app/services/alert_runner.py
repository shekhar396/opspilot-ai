from app.services.system_metrics import get_system_metrics
from app.services.alert_engine import evaluate_system_alerts
from app.services.alert_history_service import create_alert
from app.services.telegram_alert_service import send_telegram_alert
from app.db.session import SessionLocal


def run_system_alert_check() -> list[dict]:
    metrics = get_system_metrics()

    alerts = evaluate_system_alerts(metrics)

    db = SessionLocal()
    try:
        for alert in alerts:
            create_alert(db, alert)
            print(alert)
            send_telegram_alert(alert)
    finally:
        db.close()

    return alerts
