"""Main file to call universions from the CLI."""

import os
import sys

def print_help(output=sys.stdout):
    """Prints the help for the CLI tool."""
    print(
        """
Help: %s

Arguments: <tool>

Options:
  -h, --help: Prints this message
""" % (os.path.basename(sys.argv[0])),
        file = output)

def parse_args(args):
    i = 0
    options = {}
    params = []
    while i < len(args):
        arg = args[i]
        if arg == '--':
            i += 1
            break
        if arg == '-h' or arg == '--help':
            options['help'] = True
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
    if 'help' in options:
        print_help()
        sys.exit(0)

    if len(args) == 0:
        print("No action provided", file=sys.stderr)
        print_help(sys.stderr)
        sys.exit(1)

    # TODO do the actual dispatch
    print(f"Program {args[0]}")
