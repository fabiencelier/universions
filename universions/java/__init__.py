"""Module to get the Java version."""

from pathlib import Path
from typing import Optional, Union
from os import environ

from universions.version import Version

JAVA_HOME_VAR = "JAVA_HOME"


def get_java_versions(java_path: Optional[Union[Path, str]] = None) -> Optional[Version]:
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
            java_path = Path(environ[JAVA_HOME_VAR]) / "bin" / "java"
        else:
            java_path = "java"
    if isinstance(java_path, Path):
        java_path = str(java_path.absolute())
    try:
        cmd_result = _get_command_result(java_path)
        version_string = _parse_version_string(cmd_result)
        version = _parse_version(version_string)
    except Exception as exe:
        raise Exception("Could not get the Java version.", exe)


def _get_command_result(java_path: str) -> str:
    """Get the result of the command "java -version".

    Args:
        java_path: The path to use for Java in the command.
    Returns:
        The result of the command.

    """
    print(java_path)
    return "TODO"


def _parse_version(version_string: str) -> Version:
    """Parse the version string to return a version.

    Args:
        version_string: The version string such as "1.8.0_151"
    Returns:
        The Java version.
    """
    print(version_string)
    return Version(1)


def _parse_version_string(cmd_result: str) -> str:
    """Parse the command result into a string.

    Args:
        cmd_result: The result ofthe command to get the version.
    Results:
        The string of the version such as "1.8.0_151"

    """
    lines = cmd_result.splitlines()
    print(lines)
    split_lines = [line.split(" ") for line in lines]
    print(split_lines)
    version_line = [
        line for line in split_lines if len(line) > 0 and line[1] == "version"
    ][0]
    version_string = version_line[2].replace('"', "")
    return version_string
