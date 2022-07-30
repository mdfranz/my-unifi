from . import config, helpers
from pathlib import Path
from sh import ssh, scp, vector
import click, os
import os
import sys

class Environment:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.verbose = kwargs.get("verbose", False)
        self.work_dir = kwargs.get("work_dir", os.getcwd())
        self.script_file = Path(__file__).resolve()
        self.script_dir = Path(self.script_file / '..').resolve()
        self.project_dir = Path(self.script_dir / '..').resolve()
        self.files_dir = Path(self.project_dir / "files").resolve()
        self.config = config
        self.helpers = helpers

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

    def scp(self, *args, **kwargs):
        return scp('-Tqrp', *args, **kwargs)

    def ssh(self, *args, **kwargs):
        return ssh('-Tq', *args, **kwargs)

    def ssh_udm(self, *args, **kwargs):
        return self.ssh(self.config.UDM_HOST, *args, **kwargs)

    def push_dir(self, local, remote):
        self.scp(local, "{}:{}/".format(local, remote))

    def local_env(self):
        env = dict()
        env["VECTOR_CONFIG_DIR"] = str(self.files_dir / "vector" / "vector.d")
        return env

    def local_vector(self, *args, **kwargs):
        vector(_env=self.local_env(), *args, **kwargs)

