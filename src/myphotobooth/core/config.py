"""Application configuration.

This module loads and exposes the runtime settings of the photobooth
application (instance name, HTTP port, slide duration, photos directory).
"""

from pathlib import Path

import yaml


class AppConfig:
    """Runtime configuration of the application.
    
    Notes
    -----
    Key in configuration have to be the same as the attribute names of the AppConfig class. 
    The configuration file is expected to be in YAML format. 
    If the configuration file is not found, default values are used.

    Attributes
    ----------
    http_port : int
        Port the HTTP server listens on.
    instance_name : str
        Human-readable name of this photobooth, shown on the welcome
        slide and announced via mDNS.
    slide_duration_sec : int
        Duration a photo stays on screen, in seconds.
    photos_dir : Path
        Directory where uploaded photos and thumbnails are stored.
    purge_on_start : bool
        If True, the photo directory is emptied on startup.
    """

    def __init__(self) -> None:
        self.http_port: int = 8000
        self.instance_name: str = "myphotobooth"
        self.slide_duration_sec: int = 8
        self.photos_dir: Path = Path("photos")
        self.purge_on_start: bool = False

    @staticmethod
    def load(path: Path | None = None) -> "AppConfig":
        """Load configuration from a YAML file, with defaults.

        Parameters
        ----------
        path : Path, optional
            Path to the YAML configuration file. If omitted, defaults
            are used.

        Returns
        -------
        AppConfig
            A populated configuration object.

        Raises
        ------
        ValueError
            If the file exists but contains invalid values.
        """
        config = AppConfig()
        if path is None:
            return config
        
        with open(path, "r",encoding="utf-8") as f:
            raw_config = yaml.safe_load(f)

        for key, value in raw_config.items():
            if hasattr(config, key):
                setattr(config, key, value)
        return config