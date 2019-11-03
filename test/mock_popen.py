"""Test class with a mocked Popen."""

import pytest

from testfixtures import Replacer
from testfixtures.popen import MockPopen


class BasicMockedPopen:
    """Class with a mocked popen for system calls.

    use self.popen.set_command(command, stdout=b'returned value')
    """

    @pytest.fixture(autouse=True)
    def mock_popen_clear_env(self):
        """Mock Popen around each test."""
        self.popen = MockPopen()
        self.replacer = Replacer()
        self.replacer.replace("universions._exec.Popen", self.popen)
        yield
        self.replacer.restore()
