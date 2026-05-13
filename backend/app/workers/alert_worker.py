# backend/app/workers/alert_worker.py

import time

from app.services.alert_runner import run_system_alert_check


def main():
    print("OpsPilot AI Alert Worker started...")

    while True:
        try:
            run_system_alert_check()
        except Exception as e:
            print(f"Alert worker error: {e}")

        time.sleep(60)


if __name__ == "__main__":
    main()