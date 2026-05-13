import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def format_alert_message(alert: dict) -> str:
    details = alert.get("details", {})

    message = (
        "🚨 OpsPilot AI Alert\n\n"
        f"Host: {alert.get('host')}\n"
        f"Issue: {alert.get('issue')}\n"
    )

    for key, value in details.items():
        message += f"{key.upper()}: {value}\n"

    message += f"Time: {alert.get('time')}"

    return message


def send_telegram_alert(alert: dict) -> bool:
    if not TELEGRAM_BOT_TOKEN:
        print("Telegram alert skipped: TELEGRAM_BOT_TOKEN missing")
        return False

    if not TELEGRAM_CHAT_ID:
        print("Telegram alert skipped: TELEGRAM_CHAT_ID missing")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": format_alert_message(alert),
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10,
        )

        data = response.json()

        if response.status_code != 200:
            print(
                f"Telegram API error | "
                f"status={response.status_code} | "
                f"response={data}"
            )
            return False

        if not data.get("ok"):
            print(
                f"Telegram delivery failed | "
                f"response={data}"
            )
            return False

        print("Telegram alert sent successfully")
        return True

    except requests.exceptions.Timeout:
        print("Telegram request timeout")
        return False

    except requests.exceptions.ConnectionError:
        print("Telegram connection error")
        return False

    except Exception as e:
        print(f"Unexpected Telegram alert error: {e}")
        return False