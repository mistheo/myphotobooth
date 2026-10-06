"""mDNS announcement of the host on the local network (F-HOTE-04)."""

from zeroconf import ServiceInfo, Zeroconf


class MdnsAnnouncer:
    """Publishes ``<name>.local`` and the _photobooth._tcp service."""

    def __init__(self) -> None:
        self._zc: Zeroconf | None = None
        self._info: ServiceInfo | None = None

    def announce(self, ip: str, port: int, name: str) -> None:
        """Start announcing this host.

        Parameters
        ----------
        ip : str
            Local IP address to announce.
        port : int
            HTTP port.
        name : str
            Instance name, e.g. ``myphotobooth``.
        """
        raise NotImplementedError

    def unannounce(self) -> None:
        """Unregister the service and close the Zeroconf object."""
        raise NotImplementedError
