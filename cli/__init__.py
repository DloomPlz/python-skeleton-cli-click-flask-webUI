import click

@click.group()
def root():
    pass

from .example import LinuxLaunch
root.add_command(LinuxLaunch)