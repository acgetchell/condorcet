import pytest
import subprocess


@pytest.fixture
def script_run():
    """
    Run script
    """
    return subprocess.run("python condorcet.py survey.txt", shell=True,
                          capture_output=True, text=True)


def test_run_script(script_run):
    """
    Script runs and has exit code 0
    """
    assert script_run.returncode == 0, "Running script failed!"


def test_results(script_run):
    """
    Script runs and declares C the winner
    """
    result = script_run.stdout.split('\n')
    assert result[2] == "The winner is C.", "Script output wrong!"
