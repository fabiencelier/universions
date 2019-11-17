"""Parser for python version."""

import re

from ..error import InvalidVersionFormatError
from ..version import Version

PYTHON_REGEX = re.compile(
    r"""
        ^
        (?P<major>(?:0|[1-9][0-9]*))
        \.
        (?P<minor>(?:0|[1-9][0-9]*))
        (
            \.
            (?P<patch>(?:0|[1-9][0-9]*))
        )?
        (?P<prerelease>
            (?:[A-Za-z-][0-9A-Za-z-]*\+?)
        )?
        $
        """,
    re.VERBOSE,
)


def parse_python_version(version: str) -> Version:
    """Parse the python version.

    Args:
        version: the version string such as "3.9.0a0"
    Returns:
        THe parsed version object.

    """
    match = PYTHON_REGEX.match(version)
    if match is None:
        raise InvalidVersionFormatError(
            version, "It is not valid Python version string."
        )

    version_parts = match.groupdict()

    return Version(
        int(version_parts["major"]),
        int(version_parts["minor"]),
        int(version_parts["patch"]) if version_parts["patch"] is not None else 0,
        version_parts["prerelease"],
    )
