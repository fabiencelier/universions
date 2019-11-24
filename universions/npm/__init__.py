"""Module for NPM versions."""

# NPM is simple as it immediately returns the version we need

from pathlib import Path
from typing import Optional, Union

from universions._exec import exec_command
from universions.version import Version, parse_semver


def get_npm_version(npm_path: Optional[Union[Path, str]] = None) -> Optional[Version]:
    """Get the NPM version.

    Args:
        npm_path: The path to `npm` to check. If not defined, it uses "npm"
    Returns:
        The Node version.

    """
    if npm_path is None:
        npm_path = "npm"
    version_string = exec_command([npm_path, "--version"])
    return parse_semver(version_string)
