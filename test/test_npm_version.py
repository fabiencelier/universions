"""Test the npm version."""

from pathlib import Path

import pytest

from universions import Version
from universions.npm import get_npm_versions

from .mock_popen import BasicMockedPopen

MAC_OUT = b"5.0.4"
LINUX_OUT = b"6.4.1"

VERSIONS = [
    pytest.param(MAC_OUT, Version(5, 0, 4)),
    pytest.param(LINUX_OUT, Version(6, 4, 1)),
]


class TestNpm(BasicMockedPopen):
    """Test the Npm version."""

    @pytest.mark.parametrize("output,version", VERSIONS)
    def test_default_npm_version(self, output: bytes, version: Version):
        """Test that the correct version is returned."""
        self.popen.set_command("npm --version", stdout=output)
        assert get_npm_versions() == version

    def test_npm_version_with_path(self):
        """Test that the correct version is returned when specifying path."""
        path = str(Path.home() / "npm-here" / "bin" / "npm.bin")
        self.popen.set_command(f"{path} --version", stdout=LINUX_OUT)
        assert get_npm_versions(npm_path=path) == Version(6, 4, 1)
