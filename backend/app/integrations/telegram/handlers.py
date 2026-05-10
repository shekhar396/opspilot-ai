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