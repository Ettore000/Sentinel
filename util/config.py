import os


def get_token() -> str:
    """Retrieve the Telegram bot token from the environment."""
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise EnvironmentError("TELEGRAM_TOKEN not set")
    return token
