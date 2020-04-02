import click
from core import actions

@click.command()
@click.option('--name', required=True, help='The name of the user!', multiple=False)
@click.option('--alive', is_flag=True, required=False, help='The user is alive', multiple=False)
def hello(name, alive):
    result = actions.say_hello(name,alive)
    print(result)

@click.command()
@click.option('--nb1', required=True, help='The first number to addition', multiple=False)
@click.option('--nb2', required=True, help='The second number to addition', multiple=False)
def addition(nb1, nb2):
    result = actions.do_addition(nb1,nb2)
    print(result)
    