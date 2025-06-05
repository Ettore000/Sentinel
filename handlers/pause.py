from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import set_paused


def ferma(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    set_paused(chat_id, True)
    update.message.reply_text("Reminder in pausa")


def riprendi(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    set_paused(chat_id, False)
    update.message.reply_text("Reminder ripresi")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("ferma", ferma))
    dispatcher.add_handler(CommandHandler("riprendi", riprendi))
