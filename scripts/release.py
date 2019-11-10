"""Release script."""

import argparse
import subprocess
from os import path
from pathlib import Path

from update_version import update_version

PROJECT_DIR = Path(path.abspath(path.dirname(__file__))).parent


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


def main():
    """Main script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="Version to release")
    args = parser.parse_args()
    version = args.version

    update_version(version)
    package()
    upload_to_pypi()


if __name__ == "__main__":
    main()
