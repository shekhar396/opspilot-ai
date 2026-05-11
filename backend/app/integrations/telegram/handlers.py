def bytes_to_gb(value: int) -> float:
    return round(value / (1024 ** 3), 2)


def format_system_status(metrics: dict) -> str:
    return (
        "🖥 OpsPilot AI System Status\n\n"
        f"Host: {metrics['hostname']}\n"
        f"Platform: {metrics['platform']}\n\n"
        f"CPU: {metrics['cpu_percent']}%\n"
        f"RAM: {metrics['memory']['percent']}% "
        f"({bytes_to_gb(metrics['memory']['used'])} GB / "
        f"{bytes_to_gb(metrics['memory']['total'])} GB)\n"
        f"Disk: {metrics['disk']['percent']}% "
        f"({bytes_to_gb(metrics['disk']['used'])} GB / "
        f"{bytes_to_gb(metrics['disk']['total'])} GB)"
    )

def format_docker_status(containers: list[dict]) -> str:
    if not containers:
        return "🐳 Docker Status\n\nNo containers found."

    lines = ["🐳 Docker Status\n"]

    for container in containers:
        icon = "✅" if container.get("running_state") else "❌"

        lines.append(
            f"{icon} {container.get('name')}\n"
            f"ID: {container.get('container_id')}\n"
            f"Image: {container.get('image')}\n"
            f"Status: {container.get('status')}\n"
            f"Running: {container.get('running_state')}\n"
            f"Uptime: {container.get('uptime')}\n"
            f"Auto Restart Count: {container.get('restart_count')}\n"
            f"CPU: {container.get('cpu_percent')}%\n"
            f"RAM: {container.get('memory_used_mb')}MB / {container.get('memory_limit_mb')}MB "
            f"({container.get('memory_percent')}%)\n"
            f"NET: ↓{container.get('network_rx_mb')}MB ↑{container.get('network_tx_mb')}MB\n"
            f"Storage: {container.get('storage_mb') or 'N/A'}MB\n"
            f"Health: {container.get('health')}\n"
        )

    return "\n".join(lines)