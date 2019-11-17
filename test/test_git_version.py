"""Test the Git version parser."""

import pytest

from universions import Version
from universions.git import get_git_version

from .mock_popen import BasicMockedPopen

MAC_GIT = b"git version 2.10.1 (Apple Git-78)"
UNIX_GIT = b"git version 2.23.0"
OLD_GIT = b"git version 1.7.7.3"
WINDOWS_GIT = b"git version 2.24.0.windows.1"
CYGWIN_GIT = b"git version 1.9.5.msysgit.0"

GIT_VERSIONS = [
    pytest.param(MAC_GIT, Version(2, 10, 1, None, "Apple Git-78")),
    pytest.param(UNIX_GIT, Version(2, 23, 0)),
    pytest.param(OLD_GIT, Version(1, 7, 7, None, "3")),
    pytest.param(WINDOWS_GIT, Version(2, 24, 0, None, "windows.1")),
    pytest.param(CYGWIN_GIT, Version(1, 9, 5, None, "msysgit.0")),
]


class TestGit(BasicMockedPopen):
    """Test the Git version"""

    @pytest.mark.parametrize("command,version", GIT_VERSIONS)
    def test_git_vesion(self, command: bytes, version: Version):
        """Test that the correct version is returned."""
        self.popen.set_command("git --version", stdout=command)
        assert get_git_version() == version
