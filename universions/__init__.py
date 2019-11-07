"""Universions is a tool to get the versions of other tools."""

from ._version import VERSION as __version__
from .cli import main as cli
from .version import Version, parse_semver
