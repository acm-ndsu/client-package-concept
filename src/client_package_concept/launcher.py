import json
import random
import time
from enum import Enum

from rich import print_json
from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TimeElapsedColumn, ProgressColumn, Task
from rich.text import Text 

MAX_TICKS = 500
DEFAULT_TEXT_COLUMN = Progress.get_default_columns()[0]


class University(int, Enum):
    NDSU = 0
    UND = 1
    MSUM = 2

class TeamType(int, Enum):
    UNDERGRADUATE = 0
    GRADUATE = 1
    ALUMNI = 2


class RateColumn(ProgressColumn):
    """
    Renders human readable processing rate.
    https://github.com/Textualize/rich/discussions/2035#discussioncomment-3516405
    """

    def render(self, task: Task, unit_name: str = 'unit') -> Text:
        """Render the speed in iterations per second."""
        speed = task.speed or task.finished_speed
        if speed is None:
            return Text("", style="progress.percentage")
        return Text(f"{speed:.1f} {unit_name}s/s", style="progress.percentage")


class Engine:
    def loop(self):
        progress = Progress(
            DEFAULT_TEXT_COLUMN,
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            RateColumn(),
        )
        progress.start()
        try:
            simulate_id = progress.add_task("[bold]Simulating...", total=MAX_TICKS)
            saving_id = progress.add_task("[bold]Saving...", total=MAX_TICKS)
            while not progress.finished:
                if random.randint(1, 10) == 1:
                    print('jackpot')
                for t in progress.tasks:
                    progress.update(t.id, advance=random.randint(0, 10))
                time.sleep(0.001)
        finally:
            progress.stop()

class Visualizer:
    def loop(self):
        print("visualizing")

class Client:
    def register(self, team_name: str, team_type: TeamType, university: University):
        print(f'registering "{team_name}" who are {team_type}(S) from {university}')

def generate_map():
    progress = Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        RateColumn(),
    )
    progress.start()
    try:
        objects_generated = progress.add_task("[bold]Generating...", total=random.randint(300,500))
        while not progress.finished:
            progress.update(objects_generated, advance=1)
            time.sleep(0.005)
    finally:
        progress.stop()

