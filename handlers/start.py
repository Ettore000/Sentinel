from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import load_user_data


def start(update: Update, context: CallbackContext) -> None:
    """Registra l'utente e mostra un messaggio di benvenuto."""
    chat_id = update.effective_chat.id
    load_user_data(chat_id)
    update.message.reply_text("Ciao! Sono Sentinel. Benvenuto.")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("start", start))
