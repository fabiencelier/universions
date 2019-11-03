"""Main file to call universions from the CLI."""

import argparse
import pkg_resources

import universions
import universions.java as uj
import universions.node as un


def get_self_version():
    """
    Gets the version of this exact module.
    From the advised alternatives in
    https://packaging.python.org/guides/single-sourcing-package-version/, this reads from setup.py.
    But there is a little problem: for a version such as 0.1.0-dev21, the attribute version returns
    '0.1.0.dev21'. This issue is that the '-' is replaced by a '.', which makes it an invalid semver
    """
    raw_version = pkg_resources.require("universions")[0].version
    version = raw_version.replace(".dev", "-dev")
    return universions.parse_semver(version)


TOOLS = {
    "java": uj.get_java_versions,
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
