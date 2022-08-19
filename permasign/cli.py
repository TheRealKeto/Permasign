#!/usr/bin/env python3
#
# Permasign (cli.py)
# Command-line interface for Permasign

# Imports
import argparse
import permasign

# Create a list of available commands
# This list is later parsed; much more dynamic
options = [{
    "flags": ["-p"],
    "args": {
        "type": str,
        "dest": "path",
        "help": "specify path of local iPA"
    }
}, {
    "flags": ["-e"],
    "args": {
        "type": str,
        "dest": "entitlements",
        "help": "specify path of entitlements"
    }
}, {
    "flags": ["-k"],
    "args": {
        "type": str,
        "dest": "certificate",
        "help": "specify path of certificate"
    }
}]


def cli() -> None:
    # Start by specifying the argument parser
    # then, set up all available options in parsed args
    parser = argparse.ArgumentParser()

    for option in options:
        parser.add_argument(*option.get("flags"), **option.get("args"))

    args = parser.parse_args()

    # Actually start signing based on given args
    permasign.permasign(args.path, args.entitlements, args.certificate)


if __name__ == "__main__":
    cli()
