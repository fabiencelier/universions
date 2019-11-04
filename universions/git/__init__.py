"""Module for node versions."""

from pathlib import Path
import re
import subprocess
from typing import Optional, Union
from universions._exec import exec_command
from universions.error import InvalidVersionFormatError
from universions.version import Version, parse_semver

_REGEX = re.compile(
    r"""
      ^
      git\ version
      \ (?P<version>.+)
      \ \(.+\)
      $
    """,
    re.VERBOSE,
)


def _extract_version(output: str) -> str:
    """Extracts the version from the command output

  Args:
      output: command output to parse
  Returns:
      The string representing the version
  """
    match = _REGEX.match(output)
    print(f"[{output}] {match}")
    if match is None:
        raise InvalidVersionFormatError(output, "Unexpected Git output.")

    return match.groupdict()["version"]


def get_git_version(git_path: Optional[Union[Path, str]] = None) -> Optional[Version]:
    """Get the Git versions.

    Args:
        git_path: The path to the Git binary to check. If not defined, it uses "node"
    Returns:
        The Git version.

    """
    if git_path is None:
        git_path = "git"
    output = exec_command([git_path, "--version"])
    version_string = _extract_version(output)
    return parse_semver(version_string, remove_initial_v=True)
