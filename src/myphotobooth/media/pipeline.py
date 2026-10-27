"""Media processing: EXIF orientation, rescale, thumbnails (NF-05)."""

from myphotobooth.storage.store import PhotoMeta
from uuid import UUID
from PIL.Image import Image, open

from PIL.ImageOps import exif_transpose
from io import BytesIO
from datetime import UTC, datetime as dt


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
        img_obj = open(BytesIO(upload_data))

        photometa = PhotoMeta()
        photometa.id = UUID()
        photometa.session_id = session_id
        photometa.uploaded_at = dt.timestamp(UTC)
        photometa.filename = filename
        photometa.session_id = session_id
        photometa.width = img_obj.width
        photometa.height = img_obj.height
        
        return photometa

    def _fix_exif(self, img: Image) -> "Image":
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
        img_exif = exif_transpose(img)
        return img_exif
        
    def _rescale(self, img: Image) -> "Image":
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
        resized_img_obj = img.reduce(5)
        return resized_img_obj

    def _make_thumbnail(self, img: Image) -> "Image":
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
        thumbnail_img_obj = img.thumbnail( (img.height / 5, img.width / 5) )
        return thumbnail_img_obj
