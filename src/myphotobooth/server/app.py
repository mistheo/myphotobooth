"""FastAPI application factory wiring all routes and services."""

from myphotobooth.core.config import AppConfig
from myphotobooth.media.pipeline import MediaPipeline
from myphotobooth.qr.qr_service import QrService
from myphotobooth.server.events import EventBus
from myphotobooth.server.sessions import SessionManager
from myphotobooth.storage.store import PhotoStore


class PhotoBoothServer:
    """Host-side server: HTTP routes, sessions, storage, event bus.

    Parameters
    ----------
    config : AppConfig
        Application configuration.
    store : PhotoStore
        Photo storage.
    sessions : SessionManager
        Guest session manager.
    pipeline : MediaPipeline
        Media processing pipeline.
    qr : QrService
        QR code generation service.
    events : EventBus
        Real-time event bus.
    """

    def __init__(
        self,
        config: AppConfig,
        store: PhotoStore,
        sessions: SessionManager,
        pipeline: MediaPipeline,
        qr: QrService,
        events: EventBus,
    ) -> None:
        self.config = config
        self.store = store
        self.sessions = sessions
        self.pipeline = pipeline
        self.qr = qr
        self.events = events

    def start(self) -> None:
        """Mount routers and start serving (blocking)."""
        raise NotImplementedError

    def stop(self) -> None:
        """Gracefully stop the server."""
        raise NotImplementedError
