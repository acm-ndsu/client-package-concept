import typer
from typing import Annotated
from rich import print

from .launcher import *


app = typer.Typer(
    pretty_exceptions_enable=False,
    pretty_exceptions_short=False,
)


@app.command()
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

@app.command()
def register(
    team_name: Annotated[str, typer.Option(help="Your desired team name")],
    team_type: Annotated[TeamType, typer.Option(prompt="Have you graduated?")],
    university: Annotated[University, typer.Option(help="Your university")],
):
    Client().register(team_name, team_type, university)

@app.command()
def error():
    raise ArithmeticError() from KeyError()

@app.command()
def echo():
    print(input("echo what? "))


if __name__ == "__main__":
    app()
