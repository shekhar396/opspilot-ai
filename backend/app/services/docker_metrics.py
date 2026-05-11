from datetime import datetime, timezone
import docker


def bytes_to_mb(value: int) -> float:
    return round(value / (1024 * 1024), 2)


def calculate_cpu_percent(stats: dict) -> float:
    try:
        cpu_stats = stats.get("cpu_stats", {})
        precpu_stats = stats.get("precpu_stats", {})

        cpu_usage = cpu_stats.get("cpu_usage", {})
        precpu_usage = precpu_stats.get("cpu_usage", {})

        cpu_delta = (
            cpu_usage.get("total_usage", 0)
            - precpu_usage.get("total_usage", 0)
        )

        system_delta = (
            cpu_stats.get("system_cpu_usage", 0)
            - precpu_stats.get("system_cpu_usage", 0)
        )

        online_cpus = cpu_stats.get("online_cpus")

        if not online_cpus:
            online_cpus = len(cpu_usage.get("percpu_usage", [])) or 1

        if system_delta > 0 and cpu_delta > 0:
            return round((cpu_delta / system_delta) * online_cpus * 100, 2)

        return 0.0

    except Exception:
        return 0.0


def calculate_uptime(started_at: str) -> str:
    if not started_at:
        return "N/A"

    started = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    delta = now - started

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

    return f"{days}d {hours}h {minutes}m"


def get_docker_metrics() -> list[dict]:
    client = docker.from_env()
    containers = client.containers.list(all=True)

    result = []

    for container in containers:
        container.reload()
        attrs = container.attrs

        stats = container.stats(stream=False)

        memory_used = stats["memory_stats"].get("usage", 0)
        memory_limit = stats["memory_stats"].get("limit", 0)

        memory_percent = 0
        if memory_limit > 0:
            memory_percent = round((memory_used / memory_limit) * 100, 2)

        networks = stats.get("networks", {})
        rx_bytes = sum(net.get("rx_bytes", 0) for net in networks.values())
        tx_bytes = sum(net.get("tx_bytes", 0) for net in networks.values())

        health = (
            attrs.get("State", {})
            .get("Health", {})
            .get("Status", "not_configured")
        )

        result.append({
            "container_id": container.short_id,
            "name": container.name,
            "image": attrs["Config"]["Image"],
            "status": container.status,
            "running_state": attrs["State"].get("Running", False),
            "created_time": attrs.get("Created"),
            "started_time": attrs["State"].get("StartedAt"),
            "uptime": calculate_uptime(attrs["State"].get("StartedAt")),
            "restart_count": attrs.get("RestartCount", 0),
            "cpu_percent": calculate_cpu_percent(stats),
            "memory_used_mb": bytes_to_mb(memory_used),
            "memory_limit_mb": bytes_to_mb(memory_limit),
            "memory_percent": memory_percent,
            "network_rx_mb": bytes_to_mb(rx_bytes),
            "network_tx_mb": bytes_to_mb(tx_bytes),
            "storage_mb": None,
            "health": health,
        })

    return result