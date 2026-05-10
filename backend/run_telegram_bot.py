from dotenv import load_dotenv
from app.integrations.telegram.bot import run_telegram_bot

load_dotenv()

if __name__ == "__main__":
    run_telegram_bot()