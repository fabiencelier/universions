"""Main file to call universions from the CLI."""

import argparse

from universions.java import get_java_version
from universions.node import get_node_version
from universions.python import get_python_version
from universions.version import parse_semver

from ._version import VERSION as universions_version
from .version import Version


def get_self_version() -> Version:
    """Gets the version of this exact module."""
    version = universions_version.replace(".dev", "-dev")
    return parse_semver(version)


TOOLS = {
    "java": get_java_version,
    "node": get_node_version,
    "python": get_python_version,
    "universions": get_self_version,
}


def parse_args():
    """Parses the arguments of the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "tool",
        help="Select the tool whose version is wanted",
        choices=list(TOOLS.keys()),
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help="Configures the verbosity level of the printed version",
        action="count",
        default=0,
    )
    return parser.parse_args()


def print_version(version, verbosity) -> str:
    """Converts the version into the string matching the verbosity level."""
    if verbosity == 0:
        return f"{version.major}.{version.minor}"
    if 1 <= verbosity < 3:
        return f"{version.major}.{version.minor}.{version.patch}"
    return str(version)


def main() -> int:
    """Main function to be run by the CLI tool."""
    args = parse_args()

    tool_name = args.tool
    get_version = TOOLS.get(tool_name)
    version = get_version()
    print(print_version(version, args.verbosity))

    return 0


if __name__ == "__main__":
    main()
