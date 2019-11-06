"""Module to execute a command line and clean it."""

import subprocess
from pathlib import Path
from subprocess import PIPE, Popen
from typing import List, Union


def exec_command(
    parts: List[Union[str, Path]], clean: bool = True, use_stderr: bool = False
) -> str:
    """Exec the command and clean the result.

    Args:
        parts: Part of the command to execute.
        clean: Whether to clean the result.
        use_stderr: Whether to use the stderr
    Returns:
        The result of the command.

    """
    #  cmd = " ".join([str(part) for part in parts])
    cmd = [str(part) for part in parts]
    stderr = subprocess.STDOUT if use_stderr else PIPE
    result_string, _ = Popen(cmd, stdout=PIPE, stderr=stderr).communicate()
    if isinstance(result_string, bytes):
        result_string = str(result_string, encoding="utf-8")
    if clean:
        result_string = result_string.strip()
    return result_string
