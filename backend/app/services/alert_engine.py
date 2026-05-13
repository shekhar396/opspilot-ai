from datetime import datetime, timedelta
from app.config.alert_config import (
    CPU_THRESHOLD,
    RAM_THRESHOLD,
    DISK_THRESHOLD,
    ALERT_COOLDOWN_SECONDS,
)

last_alert_sent = {}


def should_send_alert(alert_key: str) -> bool:
    now = datetime.now()

    if alert_key not in last_alert_sent:
        last_alert_sent[alert_key] = now
        return True

    last_time = last_alert_sent[alert_key]

    if now - last_time >= timedelta(seconds=ALERT_COOLDOWN_SECONDS):
        last_alert_sent[alert_key] = now
        return True

    return False


def create_alert(host: str, issue: str, details: dict) -> dict:
    return {
        "host": host,
        "issue": issue,
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
        alert_key = f"{host}:cpu"
        if should_send_alert(alert_key):
            alerts.append(
                create_alert(
                    host,
                    "High CPU Usage",
                    {
                        "cpu": cpu_percent,
                        "threshold": CPU_THRESHOLD,
                    },
                )
            )

    if memory_percent > RAM_THRESHOLD:
        alert_key = f"{host}:ram"
        if should_send_alert(alert_key):
            alerts.append(
                create_alert(
                    host,
                    "High RAM Usage",
                    {
                        "ram": memory_percent,
                        "threshold": RAM_THRESHOLD,
                    },
                )
            )

    if disk_percent > DISK_THRESHOLD:
        alert_key = f"{host}:disk"
        if should_send_alert(alert_key):
            alerts.append(
                create_alert(
                    host,
                    "High Disk Usage",
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
            alert_key = f"{host}:docker:{name}:stopped"
            if should_send_alert(alert_key):
                alerts.append(
                    create_alert(
                        host,
                        "Docker Container Stopped",
                        {
                            "container": name,
                            "status": status,
                        },
                    )
                )

        if health == "unhealthy":
            alert_key = f"{host}:docker:{name}:unhealthy"
            if should_send_alert(alert_key):
                alerts.append(
                    create_alert(
                        host,
                        "Docker Container Unhealthy",
                        {
                            "container": name,
                            "health": health,
                        },
                    )
                )

    return alerts