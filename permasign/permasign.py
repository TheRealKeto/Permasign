# Permasign (permasign.py)
# Sign any application, permanently

# Imports
import subprocess

from .utils import (
    find_tool,
    get_app_info,
    find_application
)
from pathlib import Path
from zipfile import ZipFile


def permasign(
    ipa_file: str,
    ents: str,
    cert: str,
    *,
    zip_after: bool = False
) -> None:
    # First, find dependencies locally or in PATH
    # then, get the path of any given required file
    print("[*] Checking for dependencies...")
    ldid = find_tool("ldid")

    working_dir = Path(".").resolve()
    application = working_dir / ipa_file
    entitlements = working_dir / ents
    certificate = working_dir / cert

    # Create a temp folder to keep things clean
    # then, extract the given IPA file to it...
    (tmp := working_dir / "tmp").mkdir(exist_ok=True)
    print(f"[*] Extracting {application}")
    with ZipFile(application, "r") as ziparchive:
        ziparchive.extractall(tmp)

    # Find extracted application in tmp folder
    # then, sign + change perms of the app with ldid
    found_app = find_application(tmp)
    app_name = get_app_info(found_app, "CFBundleName")

    print(f"[*] Signing {found_app} with ldid")
    subprocess.run([
        str(ldid),
        f"-S{entitlements}",
        "-M",
        f"-K{certificate}",
        "-Upassword",
        str(found_app)
    ])
    print("[*] Changing permissions...")
    (found_app / app_name).chmod(0o755)

    # Archive the signed bundle as a zip archive
    # This is only done if the user decided to do so
    if zip_after is not False:
        print("[*] Zipping signed app bundle...")
        appzip_file = tmp / f"{app_name}.zip"
        with ZipFile(appzip_file, "w") as appzip:
            for app_file in found_app.rglob("*"):
                arcname = app_file.relative_to(found_app)
                appzip.write(app_file, arcname)

    print(f"Successfully permasigned {application}!")
