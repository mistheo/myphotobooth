"""Session endpoints: listing and deleting own photos (F-INV-05/06)."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/api/my-photos")
async def my_photos(session_id: str) -> list[dict]:
    """List photos uploaded by a guest.

    Parameters
    ----------
    session_id : str
        Guest connection identifier.

    Returns
    -------
    list of dict
        Metadata of the guest's photos.
    """
    raise NotImplementedError


@router.delete("/api/photos/{photo_id}")
async def delete_photo(photo_id: str, session_id: str) -> dict:
    """Delete a photo, restricted to its owner (NF-08).

    Parameters
    ----------
    photo_id : str
        Identifier of the photo to delete.
    session_id : str
        Guest connection identifier; must match the photo owner.

    Returns
    -------
    dict
        Deletion result.
    """
    raise NotImplementedError
