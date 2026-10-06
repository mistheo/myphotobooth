"""Role supervision: decides host vs satellite at startup (F-SAT-01/02)."""

from enum import Enum

from myphotobooth.core.config import AppConfig
from myphotobooth.mdns.explorer import DiscoveredHost, MdnsExplorer


class Role(Enum):
    """Role the application instance plays on the network."""

    HOST = "host"
    SATELLITE = "satellite"


class RoleSupervisor:
    """Entry point deciding the role of this instance at startup.

    Parameters
    ----------
    config : AppConfig
        Loaded application configuration.
    """

    def __init__(self, config: AppConfig) -> None:
        self._config = config
        self._explorer = MdnsExplorer()

    def run(self) -> int:
        """Run the application until shutdown.

        Returns
        -------
        int
            Process exit code.
        """
        raise NotImplementedError

    def _decide_role(self) -> Role:
        """Browse the network and decide host or satellite.

        Returns
        -------
        Role
            HOST if no photobooth is discovered, SATELLITE otherwise.
        """
        raise NotImplementedError


class HostRole:
    """Host mode: runs the server, announces mDNS, supervises kiosk.

    Parameters
    ----------
    config : AppConfig
        Application configuration.
    """

    def __init__(self, config: AppConfig) -> None:
        self.config = config
        # server, announcer, launcher wired at construction (J1).
        raise NotImplementedError

    def start(self) -> None:
        """Start server, mDNS announcement and local slideshow."""
        raise NotImplementedError

    def stop(self) -> None:
        """Stop everything cleanly (F-HOTE-09): kiosk, mDNS, server."""
        raise NotImplementedError


class SatelliteRole:
    """Satellite mode: connects to a host as a remote slideshow screen."""

    def __init__(self) -> None:
        self._host: DiscoveredHost | None = None

    def start(self, host: DiscoveredHost) -> None:
        """Connect to the selected host and start displaying.

        Parameters
        ----------
        host : DiscoveredHost
            The photobooth host selected by the user (F-SAT-03/04).
        """
        raise NotImplementedError

    def stop(self) -> None:
        """Disconnect from the host and release resources."""
        raise NotImplementedError
