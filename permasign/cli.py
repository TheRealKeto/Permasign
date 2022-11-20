# Permasign (cli.py)
# Command-line interface for Permasign

# Imports
import argparse
import permasign

from typing import (
    Any,
    List,
    Dict
)

# Create a list of available commands
# This list is later parsed; much more dynamic
options: List[Dict[str, Any]]= [{
    "flags": ["-V", "--version"],
    "args": {
        "action": "version",
        "version": permasign.__version__
    }
}, {
    "flags": ["-i", "--ipa"],
    "args": {
        "type": str,
        "dest": "ipa",
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
}, {
   "flags": ["-z", "--zip"],
   "args": {
        "dest": "zip_after",
        "action": "store_true",
        "help": "zip app bundle after signinig"
   }
}]


def cli() -> None:
    # Start by specifying the argument parser
    # then, set up all available options in parsed args
    parser = argparse.ArgumentParser()

    for option in options:
        parser.add_argument(
            *option.get("flags"),  # type: ignore
            **option.get("args")  # type: ignore
        )

    # Parse arguments, then start signing!
    args = parser.parse_args()
    permasign.permasign(
        args.ipa,
        args.entitlements,
        args.certificate,
        zip_after=args.zip_after
    )


if __name__ == "__main__":
    cli()
