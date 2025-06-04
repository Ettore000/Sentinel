from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def status(update: Update, context: CallbackContext) -> None:
    """Risponde con lo stato attuale del bot."""
    update.message.reply_text("Sentinel è in esecuzione.")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("status", status))
