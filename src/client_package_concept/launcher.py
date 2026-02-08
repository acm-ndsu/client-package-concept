from enum import Enum


class University(int, Enum):
    NDSU = 0
    UND = 1
    MSUM = 2

class TeamType(int, Enum):
    UNDERGRADUATE = 0
    GRADUATE = 1
    ALUMNI = 2


class Engine:
    def loop(self):
        print("running")

class Visualizer:
    def loop(self):
        print("visualizing")

class Client:
    def register(self, team_name: str, team_type: TeamType, university: University):
        print(f'Registering "{team_name}" who are {team_type} from {university}')

def generate_map():
    print("generating")

