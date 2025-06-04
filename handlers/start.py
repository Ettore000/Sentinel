from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def start(update: Update, context: CallbackContext) -> None:
    """Risponde al comando /start."""
    update.message.reply_text("Ciao! Sono Sentinel.")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("start", start))
