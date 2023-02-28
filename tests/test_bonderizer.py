import fire

from bonderizer.bonderizer import cli


def test_greet_cli(capsys):
    fire.Fire(cli, "new")
    captured = capsys.readouterr()
    result = captured.out
    assert result is not None
