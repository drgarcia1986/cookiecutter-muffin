import muffin

# Project middlewares
from .common.middlewares import middleware_current_user


app = muffin.Application(
    'project',
    middlewares=[middleware_current_user]
)

# Register Handlers
from .public.handlers import *  # noqa
from .users.handlers import *  # noqa

# Register Commands
from .commands import *  # noqa

# Register context processor
from .common.utils import current_user_context  # noqa
