import logging
from telegram.ext import Updater

from util.config import get_token
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    token = get_token()
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    register_handlers(dispatcher)

    logger.info("Sentinel avviato")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
