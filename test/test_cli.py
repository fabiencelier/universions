"""Test the CLI."""

import os
from pathlib import Path
from subprocess import check_output

import universions
from universions._version import VERSION as universions_version


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


def test_cli_version():
    """Test the --version and -V arguments."""
    output = check_output(["universions", "--version"])
    assert str(output, encoding="utf-8").strip() == universions_version
    output = check_output(["universions", "-V"])
    assert str(output, encoding="utf-8").strip() == universions_version


def test_supported_tools():
    """Test that the CLI returns an entry for all supported tools.
    Because the tools may not be available on the platform, this
    calls the CLI with option -a. At least, all languages will be listed."""
    output = check_output(["universions", "--all"])
    output = str(output, encoding="utf-8")

    current_test_path = Path(__file__).resolve().parent
    lib_path = current_test_path / ".." / "universions"
    supported_tools = [
        entry for entry in os.listdir(lib_path) if (lib_path / entry).is_dir()
    ]

    for tool in supported_tools:
        assert f" - {tool} : " in output or f" - {tool}\n" in output
