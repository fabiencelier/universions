"""Test the CLI."""

from subprocess import check_output


def test_cli_help():
    """Check 'universions -h'."""
    output = check_output(["universions", "-h"])
    assert str(output, encoding="utf-8").startswith("usage: universions")
    output = check_output(["universions", "--help"])
    assert str(output, encoding="utf-8").startswith("usage: universions")


def test_cli_help():
    output = check_output(["universions", "java"])
    assert str(output, encoding="utf-8").startswith("usage: universions")
