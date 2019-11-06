"""Module to update the version."""


import datetime
import re
import subprocess
from os import path
from pathlib import Path

PROJECT_DIR = Path(path.abspath(path.dirname(__file__))).parent
VERSION_FILE = path.join(PROJECT_DIR, "universions", "_version.py")


def set_version_number(current_version, new_version: str):
    """Set the version."""
    with open(VERSION_FILE, "r+b") as file:
        f_content = file.read().decode("utf-8")
        f_content = re.sub(current_version, new_version, f_content)
        file.seek(0)
        file.truncate()
        file.write(f_content.encode())


def get_current_version() -> str:
    """Read the version of the package.
    See https://packaging.python.org/guides/single-sourcing-package-version
    """
    version_exports = {}
    with open(VERSION_FILE) as file:
        exec(file.read(), version_exports)  # pylint: disable=exec-used
    return version_exports["VERSION"]


def get_dev_version() -> str:
    """Get the dev version with date."""
    version = get_current_version()
    now = datetime.datetime.now()
    date_part = now.strftime("%Y%m%d%H%M")
    # commit_part = subprocess.check_output(
    #    ["git", "show", "-s", "--abbrev=7", "--format=%h"]
    # )
    #  commit_part = str(commit_part, encoding="utf-8").strip()
    return version + date_part


def update_version():
    """Update the version."""
    set_version_number(get_current_version(), get_dev_version())
