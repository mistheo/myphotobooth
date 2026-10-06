"""Static pages and media serving for both clients."""

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/")
async def index() -> FileResponse:
    """Serve the guest upload page (client P).

    Returns
    -------
    FileResponse
        ``web/guest/index.html``.
    """
    raise NotImplementedError


@router.get("/slideshow")
async def slideshow() -> FileResponse:
    """Serve the slideshow page (client D).

    Returns
    -------
    FileResponse
        ``web/slideshow/index.html``.
    """
    raise NotImplementedError


@router.get("/photos/{photo_id}")
async def serve_photo(photo_id: str) -> FileResponse:
    """Serve the full-size image file.

    Parameters
    ----------
    photo_id : str
        Photo identifier.

    Returns
    -------
    FileResponse
        The image file.
    """
    raise NotImplementedError


@router.get("/thumbnails/{photo_id}")
async def serve_thumbnail(photo_id: str) -> FileResponse:
    """Serve the thumbnail file.

    Parameters
    ----------
    photo_id : str
        Photo identifier.

    Returns
    -------
    FileResponse
        The thumbnail file.
    """
    raise NotImplementedError
