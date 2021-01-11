import argparse
import logging
import sys

from python_log_indenter import IndentedLoggerAdapter

from constants import FORMAT
from od_items import RollPlunder

# logging.basicConfig(format=FORMAT)


class SWNTools:
    def __init__(self):
        # Create the parser
        parser = argparse.ArgumentParser(
            description="Command-Line scripts for Stars Without Number",
            usage="""swntools <command> [<args>]

Current commands are:
    plunder         Roll on the Other Dust plunder table

All commands share the following args:
    -v, --verbose   Increase verbosity and show dice rolls
    -d, --debug     Print debug information
""",
        )

        # Add the arguments
        parser.add_argument("command", help="Subcommand to run")

        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def plunder(self):
        parser = argparse.ArgumentParser(description="Roll on the Other Dust plunder table")
        parser.add_argument("-v", "--verbose", help="Increase verbosity and show dice rolls", action="store_true")
        parser.add_argument("-d", "--debug", help="Print debug information", action="store_true")
        parser.add_argument("plunder_id", help="The 'Type' ID of the plunder row from SWN:Other Dust page 105")

        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)
        args = parser.parse_args(sys.argv[2:])

        if args.debug:
            logging.basicConfig(level=logging.DEBUG, format=FORMAT)
        elif args.verbose:
            logging.basicConfig(level=logging.INFO, format=FORMAT)

        print(RollPlunder(args.plunder_id))


if __name__ == "__main__":
    SWNTools()
