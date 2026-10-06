"""Media processing: EXIF orientation, rescale, thumbnails (NF-05)."""

from myphotobooth.storage.store import PhotoMeta


class MediaPipeline:
    """Transforms an uploaded file into stored photos and metadata."""

    def process(self, upload_data: bytes, session_id, filename: str) -> PhotoMeta:
        """Full processing of one uploaded photo.

        Parameters
        ----------
        upload_data : bytes
            Raw uploaded bytes.
        session_id
            Owner session identifier.
        filename : str
            Original filename.

        Returns
        -------
        PhotoMeta
            Metadata of the processed photo.
        """
        raise NotImplementedError

    def _fix_exif(self, img) -> "Image":
        """Apply EXIF orientation to an image (F-DIA-03).

        Parameters
        ----------
        img : Image
            Input PIL image.

        Returns
        -------
        Image
            Upright image.
        """
        raise NotImplementedError

    def _rescale(self, img) -> "Image":
        """Rescale to projector resolution limits.

        Parameters
        ----------
        img : Image
            Input PIL image.

        Returns
        -------
        Image
            Rescaled image.
        """
        raise NotImplementedError

    def _make_thumbnail(self, img) -> "Image":
        """Generate a small thumbnail for guest pages.

        Parameters
        ----------
        img : Image
            Input PIL image.

        Returns
        -------
        Image
            Thumbnail image.
        """
        raise NotImplementedError
