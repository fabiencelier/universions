"""Unique format for all the versions."""

import re
from functools import total_ordering
from typing import NamedTuple, Optional

from .error import InvalidVersionFormatError


def lt_version_number(a, b):
    if a == b:
        return None
    return a < b


def lt_version_option(a, b):
    if a == b:
        return None
    if a is None:
        return False
    if b is None:
        return True

    return a < b


def option_rank(version):
    return (10 if version.prerelease is None else 0) + (
        1 if version.build is None else 0
    )


COMPARE_ORDER = [lambda a: a.major, lambda a: a.minor, lambda a: a.patch, option_rank]
COMPARE_DETAILS = [lambda a: a.prerelease, lambda a: a.build]


@total_ordering
class Version:
    """Class containing all the version info."""

    def __init__(
        self,
        major: int,
        minor: Optional[int] = None,
        patch: Optional[int] = None,
        prerelease: Optional[str] = None,
        build: Optional[str] = None,
    ):
        self.major = major
        self.minor = minor or 0
        self.patch = patch or 0
        self.prerelease = prerelease
        self.build = build

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented

        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
            and self.prerelease == other.prerelease
            and self.build == other.build
        )

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented

        for attribute in COMPARE_ORDER:
            result = lt_version_number(attribute(self) or 0, attribute(other) or 0)
            if result is not None:
                return result

        for attribute in COMPARE_DETAILS:
            result = lt_version_option(attribute(self), attribute(other))
            if result is not None:
                return result

        return False

    def __str__(self):
        return f"Version(major={self.major}, minor={self.minor}, patch={self.patch}, prerelease={self.prerelease}, build={self.build})"

    def __repr__(self):
        return Version.__str__(self)


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


def parse_semver(version_string: str, remove_initial_v=False) -> Version:
    """Parse the semver version.

    credit to https://github.com/k-bx/python-semver

    Args:
        version_string: the string to parse.
        remove_initial_v: strip the initial "v" if the version string has it.
    Returns:
        The semver.

    """
    if remove_initial_v and version_string.startswith(("v", "V")):
        version_string = version_string[1:]

    match = _REGEX.match(version_string)
    if match is None:
        raise InvalidVersionFormatError(
            version_string, "It is not valid SemVer string."
        )

    version_parts = match.groupdict()

    return Version(
        int(version_parts["major"]),
        int(version_parts["minor"]),
        int(version_parts["patch"]),
        version_parts["prerelease"],
        version_parts["build"],
    )
