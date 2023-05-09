# Permasign (permasign.py)
# Sign any application, permanently

# Imports
import shutil
import pathlib
import subprocess

from zipfile import ZipFile
from .utils import (
    find_tool,
    get_app_info,
    find_application
)


def permasign(
    ipa_file: pathlib.Path,
    ents: pathlib.Path,
    cert: pathlib.Path,
    *,
    zip_after: bool = False
) -> None:
    # First, find dependencies locally or in PATH
    # then, get the path of any given required file
    print("[*] Checking for dependencies...")
    ldid = find_tool("ldid")

    # Create a temp folder to keep things clean
    # then, extract the given IPA file to it...
    (tmp := pathlib.Path("tmp")).mkdir(exist_ok=True)
    print(f"[*] Extracting {ipa_file}")
    with ZipFile(ipa_file, "r") as ziparchive:
        ziparchive.extractall(tmp)

    # Find extracted application in tmp folder
    # then, sign + change perms of the app with ldid
    found_app = find_application(tmp)
    app_name = get_app_info(found_app, "CFBundleName")

    print(f"[*] Signing {found_app} with ldid")
    subprocess.run([
        str(ldid),
        f"-S{ents}",
        "-M",
        f"-K{cert}",
        "-Upassword",
        str(found_app)
    ])
    print("[*] Changing permissions...")
    (found_app / app_name).chmod(0o755)

    # Archive the signed bundle as a zip archive
    # This is only done if the user decided to do so
    if zip_after:
        print("[*] Zipping signed app bundle...")
        app_rpath = tmp / "Payload"
        appzip_file = tmp / f"{app_name}.zip"
        with ZipFile(appzip_file, "w") as appzip:
            for app_file in found_app.rglob("*"):
                arcname = app_file.relative_to(app_rpath)
                appzip.write(app_file, arcname)

        # As an extra measure, let's clean up
        # Using shutil is the only to do it, sadly
        shutil.rmtree(app_rpath, ignore_errors=True)

    print(f"Successfully permasigned {ipa_file}!")
