"""mDNS announcement of the host on the local network (F-HOTE-04)."""

from zeroconf import ServiceInfo, Zeroconf

import re

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
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip) is None:
            raise ValueError(f"Invalid IP address: {ip}")
        if not name or not re.match(r"^[a-zA-Z0-9_-]+$", name):
            raise ValueError(f"Invalid name: '{name}'")
        
        service_type_str = "_myphotobooth._tcp.local."        
        self._info = ServiceInfo(
            service_type_str,
            f"{name}.{service_type_str}",
            addresses=[bytes(map(int, ip.split(".")))],
            port=port,
            properties={},
            server=f"{name}.local.",
        )
    
        self._zc = Zeroconf()
        try:
            self._zc.register_service(self._info)
        except Exception:
            self.unannounce()
            raise


    def unannounce(self) -> None:
        """Unregister the service and close the Zeroconf object."""
        if self._zc and self._info:
            try:
                self._zc.unregister_service(self._info)
            finally:
                self._zc.close()
                self._zc = None
                self._info = None