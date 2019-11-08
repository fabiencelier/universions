"""Main file to call universions from the CLI."""

import argparse

import universions.java as uj
import universions.node as un
from universions.version import parse_semver

from ._version import VERSION as universions_version


def get_self_version():
    """Gets the version of this exact module."""
    version = universions_version.replace(".dev", "-dev")
    return parse_semver(version)


TOOLS = {
    "java": uj.get_java_version,
    "node": un.get_node_versions,
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


def print_version(version, verbosity):
    """Converts the version into the string matching the verbosity level."""
    if verbosity == 0:
        return f"{version.major}.{version.minor}"
    if 1 <= verbosity < 3:
        return f"{version.major}.{version.minor}.{version.patch}"
    return str(version)


def main():
    """Main function to be run by the CLI tool."""
    args = parse_args()

    tool_name = args.tool
    get_version = TOOLS.get(tool_name)
    version = get_version()
    print(print_version(version, args.verbosity))

    return 0


if __name__ == "__main__":
    main()
