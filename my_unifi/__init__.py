from click import command, option, make_pass_decorator
from .config import *
from .environment import Environment
from .cli import CLI
from .commands import *
from .helpers import *
from .database import db

pass_environment = make_pass_decorator(Environment, ensure=True)
CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")

@command(cls=CLI, context_settings=CONTEXT_SETTINGS)
@option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@pass_environment
def main(ctx, verbose):
    """My Unifi Command-Line Interface."""
    ctx.db = db
    ctx.verbose = verbose
    ctx.config = config
