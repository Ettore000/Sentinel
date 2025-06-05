from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from util import load_user_data, load_plan, get_current_event


def attuale(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    data = load_user_data(chat_id)
    plan_name = data.get('current_plan', 'default')
    try:
        plan = load_plan(plan_name)
    except FileNotFoundError:
        update.message.reply_text('Nessun piano trovato.')
        return
    prev, next_ev = get_current_event(plan)
    if prev:
        msg = f"Adesso: {prev['description']}"
        if next_ev:
            msg += f"\nHai tempo fino alle {next_ev['time']}, poi {next_ev['description']}"
        update.message.reply_text(msg)
    else:
        update.message.reply_text('Nessuna attività in corso.')


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("attuale", attuale))
