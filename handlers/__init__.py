from .start import register as register_start
from .help import register as register_help
from .echo import register as register_echo
from .status import register as register_status


def register_handlers(dispatcher) -> None:
    """Registra tutti i command handler sul dispatcher."""
    for register in (register_start, register_help, register_echo, register_status):
        register(dispatcher)
