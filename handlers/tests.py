from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def test_giornaliero(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('TODO: generare grafico giornaliero')


def test_settimanale(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('TODO: generare grafico settimanale')


def register(dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("test_giornaliero", test_giornaliero))
    dispatcher.add_handler(CommandHandler("test_settimanale", test_settimanale))
