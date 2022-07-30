import os
import click

class CLI(click.MultiCommand):

    def list_commands(self, _ctx):
        command_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        command_files = [ f for f in os.listdir(command_dir) if f.endswith('.py') and not f.startswith("_") ]
        command_names = [ f.replace(".py","") for f in command_files ]
        command_names.sort()
        return command_names

    def get_command(self, _ctx, name):
        try:
            mod = __import__(f"my_unifi.commands.{name}", None, None, ["cli"])
        except ImportError as e:
            print(e)
            return
        return mod.cli

