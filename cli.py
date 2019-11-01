"""Main file to call universions from the CLI."""

import argparse

import universions.java as uj
import universions.node as un

TOOLS = {"java": uj.get_java_versions, "node": un.get_node_versions}


def parse_args():
    """Parses the arguments of the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "tool",
        help="Select the tool whose version is wanted",
        choices=list(TOOLS.keys()),
    )
    return parser.parse_args()


def main():
    """Main function to be run by the CLI tool."""
    args = parse_args()

    # if len(args) == 0:
    #     print("No action provided", file=sys.stderr)
    #     print_help(sys.stderr)
    #     return 1

    tool_name = args.tool
    get_version = TOOLS.get(tool_name)

    # if get_version is None:
    #     print(f"Unknown tool {tool_name}", file=sys.stderr)
    #     print_supported_tools(sys.stderr)
    #     return 1

    version = get_version()
    print(version)
    return 0


if __name__ == "__main__":
    main()
