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

import pathlib
import permasign

from docopt import docopt


def cli() -> None:
    args = docopt(__doc__, version=permasign.__version__)

    ipa = pathlib.Path(args["--ipa"])
    ents = pathlib.Path(args["--ents"])
    cert = pathlib.Path(args["--cert"])
    z_after = args["--zip"]

    permasign.permasign(ipa, ents, cert, zip_after=z_after)


if __name__ == "__main__":
    cli()
