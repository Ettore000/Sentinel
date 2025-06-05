from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import remove_last_entry


def annulla(update: Update, context: CallbackContext) -> None:
    """Rimuove l'ultima voce dal conteggio."""
    chat_id = update.effective_chat.id
    remove_last_entry(chat_id)
    update.message.reply_text("Ultima aggiunta annullata.")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("annulla", annulla))
