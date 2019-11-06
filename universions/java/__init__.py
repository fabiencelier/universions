"""Module to get the Java version."""

import re
from os import environ, path
from pathlib import Path
from typing import Optional, Union

from universions._exec import exec_command
from universions.error import InvalidVersionFormatError
from universions.version import Version

JAVA_HOME_VAR = "JAVA_HOME"

_JAVA_REGEX = re.compile(
    r"""
        ^
        (?P<major>(?:0|[1-9][0-9]*))
        (
            \.(?P<minor>(?:0|[1-9][0-9]*))
        )?
        (
            \.(?P<patch>(?:0|[1-9][0-9]*))
        )?
        (\-(?P<prerelease>
            (?:0|[1-9A-Za-z-][0-9A-Za-z-]*)
            (\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*
        ))?
        (\_(?P<legacy_patch>
            [0-9]+
        ))?
        $
        """,
    re.VERBOSE,
)


def get_java_version(java_path: Optional[Union[Path, str]] = None) -> Optional[Version]:
    """Get the Java versions.

    Args:
        java_path: The path to the Java to check. If not defined, it uses JAVA_HOME
                  from the enviroment variables to try $JAVA_HOME/bin/java.
                  If JAVA_HOME is not defined either it tries only "java".
    Returns:
        The Java version.

    """
    if java_path is None:
        if JAVA_HOME_VAR in environ:
            java_path = path.join(environ[JAVA_HOME_VAR], "bin", "java")
        else:
            java_path = "java"
    if isinstance(java_path, Path):
        java_path = str(java_path)
    try:
        cmd_result = _get_command_result(java_path)
        version_string = _parse_version_string(cmd_result)
        return _parse_version(version_string)
    except Exception as exe:
        raise Exception("Could not get the Java version.", exe)


def _get_command_result(java_path: str) -> str:
    """Get the result of the command "java -version".

    Args:
        java_path: The path to use for Java in the command.
    Returns:
        The result of the command.

    """
    return exec_command([java_path, "-version"], use_stderr=True)


def _parse_version(version_string: str) -> Version:
    """Parse the version string to return a version.

    Supported versions strings include :
      - 1.8.0_151
      - 11.0.2
      - 14-ea

    Args:
        version_string: The version string such as "1.8.0_151"
    Returns:
        The Java version.
    """
    #  First split the prerelease number if any :
    match = _JAVA_REGEX.match(version_string)
    if match is None:
        raise InvalidVersionFormatError(
            version_string, "It is not valid Java version string."
        )

    parts = match.groupdict()
    major = int(parts["major"])
    minor = int(parts["minor"]) if parts["minor"] is not None else None
    if parts["legacy_patch"] is not None:
        patch = int(parts["legacy_patch"])
    elif parts["patch"] is not None:
        patch = int(parts["patch"])
    else:
        patch = None
    prerelease = parts["prerelease"]
    return Version(major, minor, patch, prerelease, None)


def _parse_version_string(cmd_result: str) -> str:
    """Parse the command result into a string.

    Args:
        cmd_result: The result ofthe command to get the version.
    Results:
        The string of the version such as "1.8.0_151"

    """
    lines = cmd_result.splitlines()
    split_lines = [line.split(" ") for line in lines]
    version_line = [
        line for line in split_lines if len(line) > 0 and line[1] == "version"
    ][0]
    version_string = version_line[2].replace('"', "")
    return version_string
