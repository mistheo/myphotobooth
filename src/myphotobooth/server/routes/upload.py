"""Upload endpoint receiving photos from guest phones (F-INV-02/03)."""

from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post("/api/upload")
async def upload(session_id: str, files: list[UploadFile]) -> dict:
    """Receive one or more photos from a guest.

    Parameters
    ----------
    session_id : str
        Guest connection identifier.
    files : list of UploadFile
        Uploaded image files.

    Returns
    -------
    dict
        Upload result per file: accepted photos and failures.
    """
    raise NotImplementedError
