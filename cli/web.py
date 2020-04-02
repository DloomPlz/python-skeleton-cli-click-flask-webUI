import click

from web.flask import app

@click.command(name="web")
def web():
    click.echo('Launching web UI ...')
    app.run(host="0.0.0.0",debug = True)