"""mDNS discovery of existing photobooth hosts (F-SAT-01)."""

from zeroconf import Zeroconf


class DiscoveredHost:
    """A photobooth host found on the local network.

    Attributes
    ----------
    name : str
        Instance name of the host.
    ip : str
        IP address of the host.
    port : int
        HTTP port of the host.
    """

    def __init__(self) -> None:
        self.name: str
        self.ip: str
        self.port: int


class MdnsExplorer:
    """Browses _photobooth._tcp services to list existing hosts."""

    def __init__(self) -> None:
        self._zc: Zeroconf | None = None

    def browse(self, timeout: float = 3.0) -> list[DiscoveredHost]:
        """Browse the network for photobooth hosts.

        Parameters
        ----------
        timeout : float, optional
            Browse duration in seconds, default 3.0.

        Returns
        -------
        list of DiscoveredHost
            Every photobooth found on the local network.
        """
        raise NotImplementedError

    def on_service_state_change(self, cb) -> None:
        """Register a callback for service add/remove events.

        Parameters
        ----------
        cb : callable
            Callback receiving the service state change.
        """
        raise NotImplementedError
