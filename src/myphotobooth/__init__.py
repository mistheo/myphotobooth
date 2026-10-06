"""Photobooth Wi-Fi: a participatory photo wall for local events.

Name and version come from pyproject.toml via importlib.metadata:
single source of truth, never redefined here.
"""

from importlib.metadata import PackageNotFoundError, metadata, version


def get_version() -> str:
    """Return the application version from installed package metadata.

    Returns
    -------
    str
        Version string declared in pyproject.toml.
    """
    return version("myphotobooth")


def get_app_name() -> str:
    """Return the human-readable application name.

    Returns
    -------
    str
        Name declared in pyproject.toml, with fallback on error.
    """
    try:
        return metadata("myphotobooth")["Name"]
    except PackageNotFoundError:
        return "myphotobooth"


__version__ = get_version()
