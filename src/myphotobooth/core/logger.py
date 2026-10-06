"""File logging for the photobooth application.

No console window is shown to end users (F-HOTE-01); all diagnostics go
to a timestamped log file for remote support (NF-07).
"""

import logging
from pathlib import Path


class Logger:
    """Thin wrapper around the standard logging module."""

    @staticmethod
    def setup(log_dir: Path) -> None:
        """Configure the root logger to write into ``log_dir``.

        Parameters
        ----------
        log_dir : Path
            Directory where the log file is created.
        """
        raise NotImplementedError

    @staticmethod
    def info(msg: str) -> None:
        """Log an informational message.

        Parameters
        ----------
        msg : str
            Message to log.
        """
        raise NotImplementedError

    @staticmethod
    def error(msg: str) -> None:
        """Log an error message.

        Parameters
        ----------
        msg : str
            Message to log.
        """
        raise NotImplementedError
