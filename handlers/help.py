from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def help_cmd(update: Update, context: CallbackContext) -> None:
    """Risponde al comando /help con la lista dei comandi disponibili."""
    update.message.reply_text(
        "Comandi disponibili:\n/start - Avvia il bot\n/help - Mostra questo messaggio\n/echo - Ripete il messaggio\n/status - Mostra lo stato del bot"
    )


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("help", help_cmd))
