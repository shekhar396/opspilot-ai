from app.services.system_metrics import get_system_metrics
from app.services.alert_engine import (
    evaluate_jenkins_alerts,
    evaluate_system_alerts,
)
from app.services.alert_history_service import (
    create_alert,
    has_jenkins_build_alert,
)
from app.services.jenkins_service import (
    JenkinsConfigurationError,
    JenkinsJobNotFoundError,
    JenkinsRequestError,
    get_failed_jobs,
)
from app.services.telegram_alert_service import send_telegram_alert
from app.db.session import SessionLocal


def run_system_alert_check() -> list[dict]:
    metrics = get_system_metrics()

    alerts = evaluate_system_alerts(metrics)
    alerts.extend(_get_jenkins_alerts())

    db = SessionLocal()
    sent_alerts = []
    try:
        for alert in alerts:
            if _is_existing_jenkins_build_alert(db, alert):
                continue

            create_alert(db, alert)
            print(alert)
            send_telegram_alert(alert)
            sent_alerts.append(alert)
    finally:
        db.close()

    return sent_alerts


def _get_jenkins_alerts() -> list[dict]:
    try:
        failed_jobs = get_failed_jobs()
    except JenkinsConfigurationError as exc:
        print(f"Jenkins alert check skipped: {exc}")
        return []
    except JenkinsJobNotFoundError as exc:
        print(f"Jenkins alert check skipped: {exc}")
        return []
    except JenkinsRequestError as exc:
        print(f"Jenkins alert check skipped: {exc}")
        return []

    return evaluate_jenkins_alerts(failed_jobs)


def _is_existing_jenkins_build_alert(db, alert: dict) -> bool:
    if alert.get("source") != "jenkins":
        return False

    details = alert.get("details", {})
    build_number = details.get("build_number")

    if build_number is None:
        return False

    return has_jenkins_build_alert(
        db,
        alert.get("host", "unknown-job"),
        int(build_number),
    )
