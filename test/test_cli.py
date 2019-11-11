"""Test the CLI."""

from subprocess import check_output

import universions


def test_cli_help():
    """Check 'universions -h'."""
    output = check_output(["universions", "-h"])
    assert str(output, encoding="utf-8").startswith("usage: universions")
    output = check_output(["universions", "--help"])
    assert str(output, encoding="utf-8").startswith("usage: universions")


def test_cli_universions():
    """Test 'universions universions'."""
    output = check_output(["universions", "universions"])
    expected = ".".join(universions.__version__.split(".")[0:2])
    assert str(output, encoding="utf-8").strip() == expected


def test_cli_universions_verbosity():
    """Test 'universions universions'."""
    expected = ".".join(universions.__version__.split(".")[0:3])
    output = check_output(["universions", "universions", "-v"])
    assert str(output, encoding="utf-8").strip() == expected
    output = check_output(["universions", "universions", "-vv"])
    assert str(output, encoding="utf-8").strip() == expected


def test_cli_all():
    """Test the --all flag of the CLI."""
    output = check_output(["universions", "--all"])
    assert str(output, encoding="utf-8").startswith("Versions :")
