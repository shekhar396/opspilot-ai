# backend/app/workers/alert_worker.py

import time

from app.services.alert_runner import run_system_alert_check


def main():
    print("OpsPilot AI Alert Worker started...")

    try:
        while True:
            try:
                run_system_alert_check()
            except Exception as e:
                print(f"Alert worker error: {e}")

            time.sleep(60)
    except KeyboardInterrupt:
        print("Alert worker stopped by user.")


if __name__ == "__main__":
    main()
