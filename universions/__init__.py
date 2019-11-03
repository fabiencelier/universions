"""Universions is a tool to get the versions of other tools."""

from .version import Version, parse_semver
from .cli import main as cli
