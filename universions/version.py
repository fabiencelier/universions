"""Unique format for all the versions."""

from typing import Tuple, Optional


class Version(Tuple[int, int, int, str, int]):
    """Class containing all the version info."""

    major: int
    minor: Optional[int]
    micro: int
    releaselevel: str
    serial: int
