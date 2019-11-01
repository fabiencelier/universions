"""Main file to call universions from the CLI."""

import os
import sys

import universions.java as uj
import universions.node as un

tools = {
    "java": uj.get_java_versions,
    "node": un.get_node_versions
}

def print_help(output=sys.stdout):
    """Prints the help for the CLI tool."""
    print(
        """
Help: %s

Arguments: <tool>

Options:
  -h, --help: Prints this message
  -l, --list-tools: List all supported tools
""" % (os.path.basename(sys.argv[0])),
        file = output)

def print_supported_tools(output=sys.stdout):
    print(
        """
Supported tools:
%s
""" % ('\n'.join(tools.keys())),
        file=output)

def parse_args(args):
    i = 0
    options = {}
    params = []
    while i < len(args):
        arg = args[i]
        if arg == "--":
            i += 1
            break
        if arg == "-h" or arg == "--help":
            options['help'] = True
        if arg == "-l" or arg == "--list-tools":
            options["listing"] = True
        elif arg[0] == '-':
            raise ValueError(f"Unrecognized option {arg}")
        else:
            params.append(arg)

        i += 1

    params += args[i:]

    return (params, options)

def main():
    """Main function to be run by the CLI tool."""
    args, options = parse_args(sys.argv[1:]) # Skip the name of the program
    if "help" in options:
        print_help()
        return 0

    if "listing" in options:
        print_supported_tools()
        return 0

    if len(args) == 0:
        print("No action provided", file=sys.stderr)
        print_help(sys.stderr)
        return 1

    # TODO do the actual dispatch
    tool_name = args[0]
    get_version = tools.get(tool_name)
    if get_version is not None:
        version = get_version()
        print(version)
        return 0
    else:
        print(f"Unknown tool {tool_name}", file=sys.stderr)
        print_supported_tools(sys.stderr)
        return 1

if __name__ == "__main__":
    main()