from typer.testing import CliRunner

from client_package_concept.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["game", "-g"])
    assert result.exit_code == 0
    assert "generating" in result.output
