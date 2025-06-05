from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import add_minutes


def aggiungi(update: Update, context: CallbackContext) -> None:
    """Incrementa il contatore di minuti per l'utente."""
    chat_id = update.effective_chat.id
    if not context.args:
        update.message.reply_text("Specificare i minuti, es. /aggiungi 10")
        return
    try:
        minutes = int(context.args[0])
    except ValueError:
        update.message.reply_text("Valore non valido.")
        return
    total = add_minutes(chat_id, minutes)
    update.message.reply_text(f"Aggiunti {minutes} minuti. Totale: {total} min")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("aggiungi", aggiungi))
