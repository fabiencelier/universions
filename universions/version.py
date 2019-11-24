"""Unique format for all the versions."""

import re
from typing import Any, NamedTuple, Optional

from .error import InvalidVersionFormatError


class Version(NamedTuple):
    """Class containing all the version info."""

    major: int
    minor: Optional[int] = None
    patch: Optional[int] = None
    prerelease: Optional[str] = None
    build: Optional[str] = None

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, tuple):
            return NotImplemented
        for i in [0, 1, 2]:
            if not _is_equal_position(self, other, i):
                return _is_lt_position(self, other, i)
        if not _is_equal_position(self, other, 3):
            # prerelease version is smaller than None
            if self.prerelease is None:
                return False
            if len(other) < 4 or other[3] is None:
                return True
            return _is_lt_position(self, other, 3)
        return False  #  build number cannot be used for precedence

    def __eq__(self, other: Any) -> bool:
        """Compare the versions.

        Build number is not used to dertermine equality.
        """
        if not isinstance(other, tuple):
            return NotImplemented
        for i in [0, 1, 2, 3]:
            if not _is_equal_position(self, other, i):
                return False
        return True

    # Define other operators as functools.total_ordering is not working with named tuples.
    #  See https://stackoverflow.com/q/32861074/4678661

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, tuple):
            return True
        return not self == other

    def __le__(self, other: Any) -> bool:
        return self == other or self < other

    def __gt__(self, other: Any) -> bool:
        return not self <= other

    def __gte__(self, other: Any) -> bool:
        return not self < other


def _is_equal_position(first: tuple, second: tuple, position):
    """Whether both position are equal in the given tuples."""
    if len(first) > position:
        if len(second) > position:
            return first[position] == second[position]
        return first[position] is None
    if len(second) > position:
        return second[position] is None
    return True


def _is_lt_position(first: tuple, second: tuple, position):
    """Compare the tuple at given position."""
    if len(first) > position and first[position] is not None:
        if len(second) > position and second[position] is not None:
            return first[position] < second[position]
        return False  # cannot be smaller if other position does not exist.
    # If not defined, always smaller if other is not None
    return len(second) > position and second[position] is not None


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
