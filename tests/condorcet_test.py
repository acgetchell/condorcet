import subprocess


def test_run_script():
    """
    Script runs and has exit code 0
    """
    return_code = subprocess.call("python condorcet.py survey.txt", shell=True)
    assert return_code == 0, "Running script failed!"


def test_results():
    """
    Script runs and declares C the winner
    """
    output = subprocess.run("python condorcet.py survey.txt", shell=True,
                            capture_output=True, text=True)
    result = output.stdout.split('\n')
    assert result[2] == "The winner is C.", "Script output wrong!"
