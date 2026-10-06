"""Photo storage: files on disk plus persistent index."""

from datetime import datetime
from pathlib import Path
from uuid import UUID

from myphotobooth.storage.index import Index


class PhotoMeta:
    """Metadata of one stored photo.

    Attributes
    ----------
    id : UUID
        Unique photo identifier.
    session_id : UUID
        Owner session identifier.
    uploaded_at : datetime
        Reception time.
    filename : str
        Stored filename on disk.
    width : int
        Image width in pixels.
    height : int
        Image height in pixels.
    """

    def __init__(self) -> None:
        self.id: UUID
        self.session_id: UUID
        self.uploaded_at: datetime
        self.filename: str
        self.width: int
        self.height: int


class PhotoStore:
    """Stores photo files and keeps the index in sync.

    Parameters
    ----------
    photos_dir : Path
        Directory for full-size photos.
    thumbs_dir : Path
        Directory for thumbnails.
    index : Index
        Persistent index backend.
    """

    def __init__(self, photos_dir: Path, thumbs_dir: Path, index: Index) -> None:
        self._photos_dir = photos_dir
        self._thumbs_dir = thumbs_dir
        self._index = index

    def add(self, meta: PhotoMeta) -> None:
        """Record a new photo in storage and index."""
        raise NotImplementedError

    def remove(self, id: UUID) -> bool:
        """Remove a photo from storage and index.

        Parameters
        ----------
        id : UUID
            Photo identifier.

        Returns
        -------
        bool
            True if the photo existed and was removed.
        """
        raise NotImplementedError

    def list_all(self) -> list[PhotoMeta]:
        """List all photos.

        Returns
        -------
        list of PhotoMeta
            All stored photo metadata.
        """
        raise NotImplementedError

    def get(self, id: UUID) -> Path | None:
        """Return the file path of a photo.

        Parameters
        ----------
        id : UUID
            Photo identifier.

        Returns
        -------
        Path or None
            File path, or None if unknown.
        """
        raise NotImplementedError

    def purge(self) -> None:
        """Delete every photo, thumbnail and index entry (F-HOTE-10)."""
        raise NotImplementedError
