"""Test the Pip version."""

from pathlib import Path

import pytest

from universions import Version
from universions.pip import get_pip_version

from .mock_popen import BasicMockedPopen

PIP_19_3_1 = b"pip 19.3.1 from /path/python3.7/site-packages/pip (python 3.7)"
PIP_10_0_0B2 = b"pip 10.0.0b2 from /path/lib/python2.7/site-packages/pip (python 2.7)"
PIP_18_1 = b"pip 18.1 from /path/lib/python3.6/site-packages/pip (python 3.6)"

VERSIONS = [
    pytest.param(PIP_19_3_1, Version(19, 3, 1)),
    pytest.param(PIP_10_0_0B2, Version(10, 0, 0, "b2")),
    pytest.param(PIP_18_1, Version(18, 1, 0)),
]


class TestPip(BasicMockedPopen):
    """Test the Pip version."""

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_default_pip_version(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        self.popen.set_command("pip --version", stderr=command)
        assert get_pip_version() == version

    @pytest.mark.parametrize("command,version", VERSIONS)
    def test_pip_version_with_path(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        path = str(Path.home() / "pip" / "bin" / "pip")
        self.popen.set_command(f"{path} --version", stderr=command)
        assert get_pip_version(path=path) == version
