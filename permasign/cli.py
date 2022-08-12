#!/usr/bin/env python3
#
# Permasign (cli.py)
# Command-line interface for Permasign

# Imports
import argparse
import permasign

# Create a list of commands
# This is more flexible and dynamic
opts_info = [{
    "flags": ["-p"],
    "args": {
        "type": str,
        "dest": "path",
        "help": "Specify path of local iPA"
    }
}, {
    "flags": ["-e"],
    "args": {
        "type": str,
        "dest": "entitlements",
        "help": "Specify path of entitlements"
    }
}, {
    "flags": ["-k"],
    "args": {
        "type": str,
        "dest": "certificate",
        "help": "Specify path of certificate"
    }
}]


def cli() -> None:
    # Start by specifying the argument parser
    # then, set up all available options...
    parser = argparse.ArgumentParser()

    for option in opts_info:
        parser.add_argument(
            *option.get("flags"),
            **option.get("args")
        )

    args = parser.parse_args()

    # Actuall start signing based on given args
    permasign.permasign(
        args.path,
        args.entitlements,
        args.certificate
    )


if __name__ == "__main__":
    cli()
