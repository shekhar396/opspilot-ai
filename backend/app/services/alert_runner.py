from app.services.system_metrics import get_system_metrics
from app.services.alert_engine import evaluate_system_alerts
from app.services.telegram_alert_service import send_telegram_alert


def run_system_alert_check() -> list[dict]:
    metrics = get_system_metrics()

    alerts = evaluate_system_alerts(metrics)

    for alert in alerts:
        print(alert)
        send_telegram_alert(alert)

    return alerts