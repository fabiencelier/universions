"""Module for node versions."""

import subprocess
from typing import Optional, Union
from pathlib import Path
from universions import Version, parse_semver


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
    if isinstance(node_path, Path):
        node_path = str(node_path.absolute())
    version_string = subprocess.check_output(["node", "--version"])
    print(version_string)
    print(type(version_string))
    stripped = str(version_string, encoding="utf-8").lstrip("v").rstrip()
    return parse_semver(stripped)
