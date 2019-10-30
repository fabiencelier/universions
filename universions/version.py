"""Unique format for all the versions."""

from typing import Optional, NamedTuple


class Version(NamedTuple):
    """Class containing all the version info."""
    major: int
    minor: Optional[int] = None
    micro: Optional[int] = None
    releaselevel: Optional[str] = None
    serial: Optional[int] = None
