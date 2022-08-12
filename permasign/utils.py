# Permasign (utils.py)
# Utilities used by Permasign

# Imports
import sys
import shutil

from pathlib import Path


def find_tool(tool: str) -> str:
    # Check if tool is in PATH
    available = shutil.which(tool)
    if available is not None:
        return available

    # If tool is not in PATH, check working dir
    # Using pathlib, we can check if tool exists
    available = Path(".").resolve() / tool
    if not available.exists():
        sys.exit(f"Could not find {tool} in PATH or locally")

    return available


def find_application(where: Path) -> Path:
    # Check if the temporary Payload folder exists
    # If not, then it's likely not extracted (?)
    if not (app_path := where / "Payload").exists():
        sys.exit("Could not find application files.")

    # Cycle through all the files until we find the right one
    for application in app_path.iterdir():
        if str(application).endswith(".app"):
            found_app = application

    return found_app
