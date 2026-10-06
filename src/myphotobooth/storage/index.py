"""Persistent index of photos (JSON backend, swappable for SQLite)."""

from uuid import UUID

from myphotobooth.storage.store import PhotoMeta


class Index:
    """Persistence layer for photo metadata.

    Parameters
    ----------
    path : Path
        Path of the index file on disk.
    """

    def __init__(self, path) -> None:
        self._path = path

    def load(self) -> None:
        """Load the index from disk into memory."""
        raise NotImplementedError

    def save(self) -> None:
        """Persist the in-memory index to disk."""
        raise NotImplementedError

    def upsert(self, meta: PhotoMeta) -> None:
        """Insert or update one photo entry.

        Parameters
        ----------
        meta : PhotoMeta
            Photo metadata to store.
        """
        raise NotImplementedError

    def delete(self, id: UUID) -> None:
        """Remove one photo entry.

        Parameters
        ----------
        id : UUID
            Photo identifier.
        """
        raise NotImplementedError

    def all(self) -> list[PhotoMeta]:
        """Return every photo entry.

        Returns
        -------
        list of PhotoMeta
            All indexed photos.
        """
        raise NotImplementedError
