from datetime import datetime, timedelta
from app.config.alert_config import (
    CPU_THRESHOLD,
    RAM_THRESHOLD,
    DISK_THRESHOLD,
    ALERT_COOLDOWN_SECONDS,
)

last_alert_sent = {}


def build_alert_key(host: str, issue: str, source: str) -> str:
    # Cooldown identity must match the alert fields we persist and notify on.
    return f"{host}:{issue}:{source}".lower()


def should_send_alert(host: str, issue: str, source: str) -> bool:
    # Alerts are suppressed before they are returned to the runner, which prevents
    # both duplicate DB inserts and duplicate Telegram notifications.
    alert_key = build_alert_key(host, issue, source)
    now = datetime.now()

    if alert_key not in last_alert_sent:
        last_alert_sent[alert_key] = now
        return True

    last_time = last_alert_sent[alert_key]

    if now - last_time >= timedelta(seconds=ALERT_COOLDOWN_SECONDS):
        last_alert_sent[alert_key] = now
        return True

    return False


def create_alert(
    host: str,
    issue: str,
    details: dict,
    severity: str = "warning",
    source: str = "system",
) -> dict:
    return {
        "host": host,
        "issue": issue,
        "severity": severity,
        "source": source,
        "details": details,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def evaluate_system_alerts(metrics: dict) -> list[dict]:
    alerts = []

    host = metrics.get("hostname", "unknown-host")

    cpu_percent = metrics.get("cpu_percent", 0)
    memory_percent = metrics.get("memory", {}).get("percent", 0)
    disk_percent = metrics.get("disk", {}).get("percent", 0)

    if cpu_percent > CPU_THRESHOLD:
        issue = "High CPU Usage"
        if should_send_alert(host, issue, "system"):
            alerts.append(
                create_alert(
                    host,
                    issue,
                    {
                        "cpu": cpu_percent,
                        "threshold": CPU_THRESHOLD,
                    },
                )
            )

    if memory_percent > RAM_THRESHOLD:
        issue = "High RAM Usage"
        if should_send_alert(host, issue, "system"):
            alerts.append(
                create_alert(
                    host,
                    issue,
                    {
                        "ram": memory_percent,
                        "threshold": RAM_THRESHOLD,
                    },
                )
            )

    if disk_percent > DISK_THRESHOLD:
        issue = "High Disk Usage"
        if should_send_alert(host, issue, "system"):
            alerts.append(
                create_alert(
                    host,
                    issue,
                    {
                        "disk": disk_percent,
                        "threshold": DISK_THRESHOLD,
                    },
                )
            )

    return alerts


def evaluate_docker_alerts(containers: list[dict], host: str = "local-docker") -> list[dict]:
    alerts = []

    for container in containers:
        name = container.get("name", "unknown-container")
        status = container.get("status", "").lower()
        health = container.get("health", "").lower()

        if status in ["exited", "dead"]:
            issue = "Docker Container Stopped"
            if should_send_alert(host, issue, "docker"):
                alerts.append(
                    create_alert(
                        host,
                        issue,
                        {
                            "container": name,
                            "status": status,
                        },
                        source="docker",
                    )
                )

        if health == "unhealthy":
            issue = "Docker Container Unhealthy"
            if should_send_alert(host, issue, "docker"):
                alerts.append(
                    create_alert(
                        host,
                        issue,
                        {
                            "container": name,
                            "health": health,
                        },
                        source="docker",
                    )
                )

    return alerts
