import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from app.integrations.telegram.handlers import format_docker_status, format_system_status
from app.services.system_metrics import get_system_metrics
from app.services.docker_metrics import get_docker_metrics


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to OpsPilot AI 🚀\n\nUse /help to see available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start bot\n"
        "/help - Show help\n"
        "/health - Check bot health\n"
        "/status - Check system status\n"
        "/docker - Check Docker containers"
    )


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("OpsPilot AI bot is running ✅")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    metrics = get_system_metrics()
    message = format_system_status(metrics)

    await update.message.reply_text(message)

async def docker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    containers = get_docker_metrics()

    message = format_docker_status(containers)

    await update.message.reply_text(message)


def run_telegram_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is missing")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("health", health))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("docker", docker))

    print("Telegram bot is running...")
    app.run_polling()