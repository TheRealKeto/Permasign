# Permasign (cli.py)
# Command-line interface for Permasign

"""Usage: permasign [-h] [-V] -i IPA -e ENTS -k CERT [-z]

Options:
  -h, --help         Show this screen.
  -V, --version      Show version.
  -i, --ipa IPA      Set IPA file to be signed.
  -e, --ents ENTS    Specify entitlements to be applied.
  -k, --cert CERT    Specify certificate to use when signing.
  -z, --zip          Zip app bundle after signing.

"""

import permasign

from docopt import docopt


def cli() -> None:
    args = docopt(__doc__, version=permasign.__version__)

    permasign.permasign(
        args.get("--ipa"),
        args.get("--ents"),
        args.get("--cert"),
        zip_after=args.get("--zip")
    )


if __name__ == "__main__":
    cli()
