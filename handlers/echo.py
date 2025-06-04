from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def echo(update: Update, context: CallbackContext) -> None:
    """Risponde con lo stesso testo che l'utente ha inviato."""
    if update.message.text:
        update.message.reply_text(update.message.text)


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("echo", echo))
