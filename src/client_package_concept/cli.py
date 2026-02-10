import typer
from typing import Annotated
from rich import print

from .launcher import *


app = typer.Typer(
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    pretty_exceptions_enable=False,
    pretty_exceptions_short=False,
    no_args_is_help=True,
)


@app.command(help="Generate/run/visualize a game", no_args_is_help=True)
def game(
    generate: Annotated[bool, typer.Option("-g", "--generate", help="Generate a new map?")] = False,
    run: Annotated[bool, typer.Option("-r", "--run", help="Run a game?")] = False,
    visualize: Annotated[bool, typer.Option("-v", "--visualize", help="Visualize the last game?")] = False,
):
    if generate:
        generate_map()
    if run:
        Engine().loop()
    if visualize:
        Visualizer().loop()

@app.command(help="Register a new team")
def register(
    team_name: Annotated[str, typer.Option(help="Your desired team name", prompt=True)],
    team_type: Annotated[TeamType, typer.Option(help="Your team type", prompt=True)],
    university: Annotated[University, typer.Option(help="Your university", prompt=True)],
):
    Client().register(team_name, team_type, university)

@app.command(help="Raises an error")
def error():
    raise ArithmeticError() from KeyError()

@app.command(help="Prints user input")
def echo():
    print(input("echo what? "))


if __name__ == "__main__":
    app()
