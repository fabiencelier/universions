"""Test the parsing of node version."""

from pathlib import Path

import pytest

from universions import Version
from universions.node import get_node_versions

from .mock_popen import BasicMockedPopen

ARGON = b"v4.9.1\n"
BORON = b"v6.17.1\n"
CARBON = b"v8.16.2\n"
DUBNIUM = b"v10.17.0\n"
ERBIUM = b"v12.13.0\n"

VERSIONS = [
    pytest.param(ARGON, Version(4, 9, 1)),
    pytest.param(BORON, Version(6, 17, 1)),
    pytest.param(CARBON, Version(8, 16, 2)),
    pytest.param(DUBNIUM, Version(10, 17, 0)),
    pytest.param(ERBIUM, Version(12, 13, 0)),
]


class TestNode(BasicMockedPopen):
    """Test the node version."""

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_default_node_version(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        self.popen.set_command("node --version", stderr=command)
        assert get_node_versions() == version

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_default_node_version_with_path(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        path = str(Path.home() / "node" / "bin")
        self.popen.set_command(f"{path} --version", stderr=command)
        assert get_node_versions(node_path=path) == version
