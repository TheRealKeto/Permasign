# Permasign (permasign.py)
# Sign any application, permanently

# Imports
import subprocess

from .utils import (
    find_tool,
    find_application,
)
from pathlib import Path
from zipfile import ZipFile

__working_dir = Path(".").resolve()


def permasign(
    ipa_file: str,
    entitlements: str,
    certificate: str
) -> None:
    # First, find dependencies in PATH or locally
    # then, get the path of any given required file
    print("[*] Checking for dependencies...")
    ldid = find_tool("ldid")

    application = __working_dir / ipa_file
    entitlements = __working_dir / entitlements
    certificate = __working_dir / certificate

    # Create a temp folder to keep things clean
    # then, extract the given IPA file to it...
    (tmp := __working_dir / "tmp").mkdir(exist_ok=True)
    print(f"[*] Extracting {application}")
    with ZipFile(application, "r") as ziparchive:
        ziparchive.extractall(str(tmp))

    # Find the application in temp folder
    # then, proceed to sign the found app with ldid
    found_app = find_application(tmp)
    print(f"[*] Signing {found_app} with ldid")
    subprocess.run([
        str(ldid),
        f"-S{entitlements}",
        "-M",
        f"-K{certificate}",
        "-Upassword",
        str(found_app)
    ])
