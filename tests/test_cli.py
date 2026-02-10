from typer.testing import CliRunner

from client_package_concept.cli import app
from client_package_concept.launcher import TeamType, University

runner = CliRunner()


def test_game_generate():
    result = runner.invoke(app, ['game', '-g'])
    assert result.exit_code == 0
    assert 'generating' in result.output.lower()

def test_register():
    team_name = 'mymegalongteamname'
    team_type = TeamType.UNDERGRADUATE
    university = University.NDSU
    result = runner.invoke(app, ['register'], input=f'{team_name}\n{team_type.value}\n{university.value}')
    assert result.exit_code == 0
    assert 'register' in result.output
