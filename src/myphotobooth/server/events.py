"""Real-time event bus broadcasting slideshow updates (OBJ-2)."""

from datetime import datetime
from typing import Any
from uuid import UUID


class SlideEvent:
    """An event broadcast to slideshow clients.

    Attributes
    ----------
    type : str
        Event type: "photo_added" or "photo_removed".
    photo_id : UUID
        Identifier of the concerned photo.
    timestamp : datetime
        Emission time, used by satellites for soft synchronisation.
    url : str
        URL of the full-size image.
    thumb_url : str
        URL of the thumbnail.
    """

    def __init__(self, type: str, photo_id: UUID, url: str, thumb_url: str) -> None:
        self.type = type
        self.photo_id = photo_id
        self.timestamp = datetime.now()
        self.url = url
        self.thumb_url = thumb_url


class EventBus:
    """Pub/sub hub between HTTP routes and WebSocket slideshow clients."""

    def __init__(self) -> None:
        self._subscribers: list[Any] = []

    def publish(self, event: SlideEvent) -> None:
        """Broadcast an event to every connected slideshow client.

        Parameters
        ----------
        event : SlideEvent
            The event to broadcast.
        """
        raise NotImplementedError

    def subscribe(self, conn: Any) -> None:
        """Register a WebSocket connection.

        Parameters
        ----------
        conn : Any
            WebSocket connection to register.
        """
        raise NotImplementedError

    def unsubscribe(self, conn: Any) -> None:
        """Unregister a WebSocket connection.

        Parameters
        ----------
        conn : Any
            WebSocket connection to remove.
        """
        raise NotImplementedError
