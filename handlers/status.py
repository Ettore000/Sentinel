from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import load_user_data


def status(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    data = load_user_data(chat_id)
    hours = data['counter'] // 60
    minutes = data['counter'] % 60
    update.message.reply_text(f"Attività: {hours}h {minutes}m")


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("status", status))
