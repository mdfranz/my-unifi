import click
from sh import vector
from my_unifi import pass_environment, Environment

@click.group()
def cli():
    pass

@cli.command()
@pass_environment
def push(ctx: Environment):
    ctx.push_dir("vector", ctx.config.DATA_DIR)

@cli.command()
@pass_environment
def validate(ctx: Environment):
    """Ensure that a vector config is valid (locally)."""
    ctx.local_vector("validate")
