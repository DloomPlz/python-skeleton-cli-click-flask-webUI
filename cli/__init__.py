import click

@click.group()
def root():
    pass

from .example import hello,addition
from .web import web
root.add_command(hello)
root.add_command(addition)
root.add_command(web)