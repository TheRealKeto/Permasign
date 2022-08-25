# Permasign (__init__.py)
# Initializer for Permasign

# Imports
from .utils import (
    find_tool,
    get_version,
    get_app_info,
    find_application
)
from .permasign import permasign

__version__: str = get_version()
