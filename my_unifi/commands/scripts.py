import click
from my_unifi import pass_environment, Environment

@click.group()
def cli():
    pass

@cli.command()
@pass_environment
def push(ctx: Environment):
    ctx.push_dir("scripts", ctx.config.CONFIG_DIR)
    ctx.ssh_udm("chmod -c 700 {}/*".format(ctx.config.SCRIPTS_DIR))
