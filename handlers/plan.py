from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import load_user_data, save_user_data, load_plan


def piano(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    data = load_user_data(chat_id)
    plan = data.get('current_plan', 'default')
    update.message.reply_text(f"Piano attivo: {plan}")


def set_piano(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    if not context.args:
        update.message.reply_text('Uso: /set_piano nome_piano')
        return
    name = context.args[0]
    try:
        load_plan(name)
    except FileNotFoundError:
        update.message.reply_text('Piano non trovato.')
        return
    data = load_user_data(chat_id)
    data['current_plan'] = name
    save_user_data(chat_id, data)
    update.message.reply_text(f"Piano cambiato in {name}")

# Placeholder handlers for create/edit/delete

def create_piano(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('TODO: implementare /create_piano')


def edit_piano(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('TODO: implementare /edit_piano')


def delete_piano(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('TODO: implementare /delete_piano')


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("piano", piano))
    dispatcher.add_handler(CommandHandler("set_piano", set_piano))
    dispatcher.add_handler(CommandHandler("create_piano", create_piano))
    dispatcher.add_handler(CommandHandler("edit_piano", edit_piano))
    dispatcher.add_handler(CommandHandler("delete_piano", delete_piano))
