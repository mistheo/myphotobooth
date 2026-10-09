"""Persistent index of photos (JSON backend, swappable for SQLite)."""

from pathlib import Path
from uuid import UUID

from myphotobooth.storage.store import PhotoMeta
import pickle


class Index:
    """Persistence layer for photo metadata.

    Parameters
    ----------
    path : Path
        Path of the index file on disk.
    index : dict[UUID, Photometa]
        All photos indexed by photo ID.
    """

    def __init__(self, path: Path) -> None:
        self._path = path
        self._index: dict[UUID, PhotoMeta] = {}

    def load(self) -> None:
        """Load the index from disk into memory."""
        if self._path.exists():
            with open(self._path, "rb") as f: # reminder: rb means read bytes
                self._index: dict[UUID, PhotoMeta] = pickle.load(f)
        else:
            self._index: dict[UUID, PhotoMeta] = {}

    def save(self) -> None:
        """Persist the in-memory index to disk."""
        if self._path.parent.exists():
            with open(self._path, "wb") as f: #reminder: wb means write bytes
                pickle.dump(self._index, f)

    def upsert(self, meta: PhotoMeta) -> None:
        """Insert or update one photo entry.

        Parameters
        ----------
        meta : PhotoMeta
            Photo metadata to store.
        """
        self._index[meta.id] = meta

    def delete(self, id: UUID) -> PhotoMeta:
        """Remove one photo entry.

        Parameters
        ----------
        id : UUID
            Photo identifier.
        """
        return self._index.pop(id)

    def all(self) -> list[PhotoMeta]:
        """Return every photo entry.

        Returns
        -------
        list of PhotoMeta
            All indexed photos.
        """
        return list(self._index.values())
