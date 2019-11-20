"""Main file to call universions from the CLI."""

import argparse
from pathlib import Path

from universions.git import get_git_version
from universions.java import get_java_version
from universions.node import get_node_version
from universions.pip import get_pip_version
from universions.python import get_python_version
from universions.version import parse_semver

from ._version import VERSION as universions_version
from .error import InvalidVersionFormatError, NotFoundError
from .version import Version


def get_self_version() -> Version:
    """Gets the version of this exact module."""
    version = universions_version.replace(".dev", "-dev")
    return parse_semver(version)


ISSUE_URL = "https://github.com/fabiencelier/universions/issues"

TOOLS = {
    "git": get_git_version,
    "java": get_java_version,
    "node": get_node_version,
    "pip": get_pip_version,
    "python": get_python_version,
    "universions": get_self_version,
}


def get_args_parser():
    """Get the arguments parser of the program."""
    parser = argparse.ArgumentParser()
    tool_group = parser.add_argument_group()
    tool_group.add_argument(
        "tool",
        help="select the tool whose version is wanted",
        nargs="?",
        choices=list(TOOLS.keys()),
    )
    tool_group.add_argument(
        "-p", "--path", help="Sets the path to the tool to inspect", default=None
    )
    parser.add_argument(
        "-a", "--all", action="store_true", help="display all the tools version"
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help="configure the verbosity level of the printed version",
        action="count",
        default=0,
    )
    parser.add_argument(
        "-V", "--version", action="version", version=universions_version
    )
    return parser


def print_version(version: Version, verbosity: int) -> str:
    """Converts the version into the string matching the verbosity level."""
    if verbosity == 0:
        return f"{version.major}.{version.minor}"
    if 1 <= verbosity < 3:
        return f"{version.major}.{version.minor}.{version.patch}"
    return str(version)


def print_all_versions(verbosity: int):
    """Print all the versions."""
    versions = dict()
    not_found = []
    failures = []
    for tool, cmd in TOOLS.items():
        try:
            versions[tool] = cmd()
        except NotFoundError:
            not_found.append(tool)
        except InvalidVersionFormatError:
            failures.append(tool)

    print("Versions :")
    for (tool, version) in versions.items():
        print(f"  - {tool} : {print_version(version, verbosity)}")
    if len(not_found) > 0:
        print("\nNot found:")
        for tool in not_found:
            print(f"  - {tool}")
    if len(failures) > 0:
        print("\nFailures:")
        for tool in failures:
            print(f"  - {tool}")
        print(f"Please report the failures at {ISSUE_URL}")


def main() -> int:
    """Main function to be run by the CLI tool."""
    parser = get_args_parser()
    args = parser.parse_args()
    if args.all:
        print_all_versions(args.verbosity)
        return 0
    tool_name = args.tool
    if tool_name is None:
        parser.print_help()
        return 0
    get_version = TOOLS.get(tool_name)
    if args.path is not None:
        tool_path = Path(args.path)
        version = get_version(tool_path)
    else:
        version = get_version()

    print(print_version(version, args.verbosity))

    return 0


if __name__ == "__main__":
    main()
