"""Unique format for all the versions."""

from typing import Optional, NamedTuple
import re


class Version(NamedTuple):
    """Class containing all the version info."""

    major: int
    minor: Optional[int] = None
    patch: Optional[int] = None
    prerelease: Optional[str] = None
    build: Optional[str] = None


_REGEX = re.compile(
    r"""
        ^
        (?P<major>(?:0|[1-9][0-9]*))
        \.
        (?P<minor>(?:0|[1-9][0-9]*))
        \.
        (?P<patch>(?:0|[1-9][0-9]*))
        (\-(?P<prerelease>
            (?:0|[1-9A-Za-z-][0-9A-Za-z-]*)
            (\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*
        ))?
        (\+(?P<build>
            [0-9A-Za-z-]+
            (\.[0-9A-Za-z-]+)*
        ))?
        $
        """,
    re.VERBOSE,
)


def parse_semver(version_string: str) -> Version:
    """Parse the semver version.

    credit to https://github.com/k-bx/python-semver

    Args:
        version_string: the string to parse.
    Returns:
        The semver.

    """
    match = _REGEX.match(version_string)
    if match is None:
        raise ValueError("%s is not valid SemVer string" % version_string)

    version_parts = match.groupdict()

    return Version(
        int(version_parts["major"]),
        int(version_parts["minor"]),
        int(version_parts["patch"]),
        version_parts["prerelease"],
        version_parts["build"],
    )
