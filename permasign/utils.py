# Permasign (utils.py)
# Utilities used by Permasign

# Imports
import sys
import shutil

import pathlib
import plistlib

from importlib import metadata
from typing import (
    Any,
    Union
)


def find_tool(tool: str, /) -> Union[str, pathlib.Path]:
    # Check if tool is in PATH
    available = shutil.which(tool)
    if available is not None:
        return available

    # If tool is not in PATH, check working dir
    # Using pathlib, we can check if tool exists
    available_local = pathlib.Path(".").resolve() / tool
    if not available_local.exists():
        sys.exit(f"Could not find {tool} locally or in PATH")

    return available_local


def find_application(where: pathlib.Path, /) -> pathlib.Path:
    # Check if the temporary Payload folder exists
    # If not, then it's likely not extracted (?)
    if not (app_path := where / "Payload").exists():
        sys.exit("Could not find application bundle.")

    # Cycle through all the files until we find the right one
    found_app = [app for app in app_path.iterdir()]
    return next(iter(found_app))


def get_app_info(app_path: pathlib.Path, info: str, /) -> Any:
    # For now, this only gets the app's name
    # TODO: Find a better use case for this...

    # Use the given app path to find what we need
    with open(f"{app_path}/Info.plist", "rb") as f:
        app_info = plistlib.load(f)

    return app_info.get(info)


def get_version() -> str:
    # Get the version of the installed package
    # This's specific to the value used by Poetry
    try:
        version = metadata.version(__package__)
    # Return a dummy version if the package doesn't exist
    except metadata.PackageNotFoundError:
        version = "0, from archive/source"

    return version
