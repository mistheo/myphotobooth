"""Event export as a single timestamped ZIP (F-HOTE-14/15/16)."""

from pathlib import Path


class ZipExporter:
    """Bundles originals, thumbnails and index into one archive.

    Parameters
    ----------
    store
        Photo store providing files and index.
    """

    def __init__(self, store) -> None:
        self._store = store

    def export(self, destination: Path) -> Path:
        """Create the export ZIP.

        Parameters
        ----------
        destination : Path
            Directory chosen via the native file dialog.

        Returns
        -------
        Path
            Path of the created ZIP archive.
        """
        raise NotImplementedError
