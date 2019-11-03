"""Module for node versions."""

import subprocess
from typing import Optional, Union
from pathlib import Path
from universions import Version, parse_semver
from universions._exec import exec_command


def get_node_versions(
    node_path: Optional[Union[Path, str]] = None
) -> Optional[Version]:
    """Get the Java versions.

    Args:
        node_path: The path to the node to check. If not defined, it uses "node"
    Returns:
        The Node version.

    """
    if node_path is None:
        node_path = "node"
    version_string = exec_command([node_path, "--version"], use_stderr=True)
    return parse_semver(version_string, remove_initial_v=True)
