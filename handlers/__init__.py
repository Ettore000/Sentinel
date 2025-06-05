from .start import register as register_start
from .help import register as register_help
from .echo import register as register_echo
from .status import register as register_status
from .add_minutes import register as register_add
from .cancel import register as register_cancel
from .pause import register as register_pause
from .current import register as register_current
from .plan import register as register_plan
from .tests import register as register_tests


def register_handlers(dispatcher) -> None:
    """Registra tutti i command handler sul dispatcher."""
    for register in (
        register_start,
        register_help,
        register_echo,
        register_status,
        register_add,
        register_cancel,
        register_pause,
        register_current,
        register_plan,
        register_tests,
    ):
        register(dispatcher)
