"""Module for node versions."""

import re
import subprocess
from pathlib import Path
from typing import Optional, Tuple, Union

from universions._exec import exec_command
from universions.error import InvalidVersionFormatError
from universions.version import Version, parse_semver

_REGEX = re.compile(
    r"""
      ^
      git\ version
      \ (?P<version>\d+\.\d+\.\d+)
      (\.(?P<complement>[^ ]+))?
      (\ \((?P<info>.+)\))?
      $
    """,
    re.VERBOSE,
)

ParsingInfo = Tuple[str, Optional[str], Optional[str]]


def _extract_version(output: str) -> ParsingInfo:
    """Extracts the version from the command output

  Args:
      output: command output to parse
  Returns:
      The string representing the version
  """
    match = _REGEX.match(output)
    if match is None:
        raise InvalidVersionFormatError(output, "Unexpected Git output.")

    groups = match.groupdict()
    return (groups["version"], groups["complement"], groups["info"])


def create_version(info: ParsingInfo) -> Version:
    """Transforms the parsing info into an actual version"""
    version, complement, detail = info
    base_version = parse_semver(version)

    if complement and detail:
        build = f"{complement} {detail}"
    elif complement:
        build = complement
    elif detail:
        build = detail
    else:
        build = None

    if build is None:
        return base_version

    return Version(
        base_version.major, base_version.minor, base_version.patch, None, build
    )


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
    return create_version(version_string)
