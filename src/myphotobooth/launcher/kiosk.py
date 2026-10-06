"""Kiosk slideshow launcher with crash supervision (F-HOTE-06/08)."""

MAX_CRASHES = 3


class SlideshowLauncher:
    """Launches and supervises the local slideshow client."""

    def __init__(self) -> None:
        self._crash_count: int = 0

    def launch_kiosk(self) -> None:
        """Start the slideshow in kiosk mode as a subprocess."""
        raise NotImplementedError

    def on_exit(self, callback) -> None:
        """Register a callback run when the slideshow exits cleanly.

        Parameters
        ----------
        callback : callable
            Called on clean exit (triggers full shutdown, F-HOTE-09).
        """
        raise NotImplementedError

    def _restart(self) -> None:
        """Restart the slideshow after a crash, or fall back."""
        raise NotImplementedError

    def _fallback_browser(self) -> None:
        """Fall back to a browser in kiosk mode after repeated crashes."""
        raise NotImplementedError
