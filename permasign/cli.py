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
        "required": True,
        "help": "specify local path of the IPA to be signed",
    }
}, {
    "flags": ["-e"],
    "args": {
        "type": str,
        "dest": "entitlements",
        "required": True,
        "help": "specify entitlements that will be applied"
    }
}, {
    "flags": ["-k"],
    "args": {
        "type": str,
        "dest": "certificate",
        "required": True,
        "help": "specify root cerficiate to use"
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
