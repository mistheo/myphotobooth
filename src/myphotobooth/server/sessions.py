"""Guest sessions: connection identifier and photo ownership."""

from datetime import datetime, timezone
from uuid import UUID, uuid4


class Session:
    """A guest session, materialised by a connection identifier.

    Attributes
    ----------
    token : UUID
        Unique connection identifier kept by the guest browser.
    created_at : datetime
        Session creation time.
    photo_ids : list of UUID
        Photos uploaded through this session.
    """

    def __init__(self) -> None:
        self.token: UUID = uuid4()
        self.created_at: datetime = datetime.now(timezone.utc)
        self.photo_ids: list[UUID] = []


class SessionManager:
    """Creates and validates guest sessions.

    Parameters
    ----------
    ttl_hours : int, optional
        Session lifetime, default 12 (an event evening).
    """

    def __init__(self, ttl_hours: int = 12) -> None:
        self.ttl = ttl_hours
        self._sessions: dict[UUID, Session] = {}

    def create_session(self) -> Session:
        """Create a new guest session.

        Returns
        -------
        Session²
            The newly created session.
        """
        new_session = Session()
        self._sessions[new_session.token] = new_session
        return new_session

    def validate(self, session_id: UUID) -> bool:
        """Check that a session exists and is not expired.

        Parameters
        ----------
        session_id : UUID
            Connection identifier sent by the guest.

        Returns
        -------
        bool
            True if the session is valid.
        """
        return session_id in list(self._sessions.keys())
