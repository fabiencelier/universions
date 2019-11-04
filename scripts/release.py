"""Release script."""

import subprocess
from os import path
from pathlib import Path
from update_version import update_version

PROJECT_DIR = Path(path.abspath(path.dirname(__file__))).parent

update_version()


def package():
    """Package the library."""
    to_delete = str(PROJECT_DIR / "dist" / "*")
    subprocess.check_output(["rm", to_delete, "--force"])
    subprocess.check_output(["pipenv", "run", "python", "setup.py", "sdist"])


def upload_to_pypi():
    """Upload to Pypi."""
    to_upload = str(PROJECT_DIR / "dist" / "*")
    subprocess.check_output(
        ["pipenv", "run", "twine", "upload", to_upload, "--username", "__token__"]
    )


if __name__ == "__main__":
    package()
    upload_to_pypi()
