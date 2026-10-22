"""mDNS discovery of existing photobooth hosts (F-SAT-01)."""

import time
from collections.abc import Callable

from zeroconf import (
    IPVersion,
    ServiceBrowser,
    ServiceInfo,
    ServiceStateChange,
    Zeroconf,
)


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

    def __repr__(self) -> str:
        return f"DiscoveredHost(name={self.name!r}, ip={self.ip!r}, port={self.port})"


class MdnsExplorer:
    """Browses _myphotobooth._http._tcp services to list existing hosts."""

    def __init__(self) -> None:
        self._zc: Zeroconf | None = None
        self._callbacks: list[Callable[[DiscoveredHost | None, str], None]] = []
        self._hosts: dict[str, DiscoveredHost] = {}  # keyed by service name

    def _on_state_change(self, zeroconf: Zeroconf, service_type: str, name: str,
                         state_change: ServiceStateChange) -> None:
        """Handle a service add/remove event fired by ``ServiceBrowser``.

        On ``Added``, resolves the service via the Zeroconf instance and
        stores the resulting host in the internal cache. On ``Removed``,
        drops the host from the cache. Registered callbacks are notified
        in both cases.

        Parameters
        ----------
        zeroconf : Zeroconf
            Zeroconf instance that fired the event, used to resolve the
            service address and port.
        service_type : str
            Type of the service that changed (e.g. ``_myphotobooth._http._tcp.local.``).
        name : str
            Full instance name of the service that changed.
        state_change : ServiceStateChange
            Kind of event, either ``Added`` or ``Removed``. ``Updated``
            events are ignored.

        Notes
        -----
        Exceptions raised inside this handler would be swallowed by the
        ServiceBrowser thread; resolution and host building are therefore
        kept defensive (unresolvable services are silently skipped).
        """
        if state_change is ServiceStateChange.Added:
            info = zeroconf.get_service_info(service_type, name)
            if info is None:
                return
            host = self._build_host(info)
            if host is None:
                return
            self._hosts[name] = host
            self._notify(host, "added")

        elif state_change is ServiceStateChange.Removed:
            host = self._hosts.pop(name, None)
            if host is not None:
                self._notify(host, "removed")

    @staticmethod
    def _build_host(info: ServiceInfo) -> DiscoveredHost | None:
        """Convert a resolved service record into a ``DiscoveredHost``.

        Prefers IPv4 addresses and falls back to any available address.
        The instance name is stripped of the service-type suffix so that
        ``DiscoveredHost.name`` holds the bare host name.

        Parameters
        ----------
        info : ServiceInfo
            Resolved service record containing addresses and port.

        Returns
        -------
        DiscoveredHost or None
            The populated host, or ``None`` if no address could be
            parsed from the record.
        """
        addresses = info.parsed_addresses(IPVersion.V4Only) or info.parsed_addresses()
        if not addresses:
            return None
        host = DiscoveredHost()
        host.name = info.name.removesuffix("." + "_myphotobooth._http._tcp.local.")
        host.ip = addresses[0]
        host.port = info.port
        return host

    def _notify(self, host: DiscoveredHost, event: str) -> None:
        """Dispatch a service event to every registered callback.

        Callbacks are invoked in registration order. A callback raising
        an exception is isolated so that one faulty consumer cannot
        break discovery or the other callbacks.

        Parameters
        ----------
        host : DiscoveredHost
            Host concerned by the event.
        event : str
            Either ``"added"`` or ``"removed"``.

        Notes
        -----
        Exceptions are caught and discarded silently; if callback errors
        should be logged in production, add a logger call in the
        ``except`` block.
        """
        for cb in self._callbacks:
            try:
                cb(host, event)
            except Exception: #noqa: S110 BLE001 # a bad callback must not break discovery 
                pass

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
        self._hosts.clear()
        self._zc = Zeroconf()
        try:
            ServiceBrowser(self._zc, "_myphotobooth._http._tcp.local.", handlers=[self._on_state_change])
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                time.sleep(0.1)
            return list(self._hosts.values())
        finally:
            self._zc.close()
            self._zc = None

    def on_service_state_change(self, cb) -> None:
        """Register a callback for service add/remove events.

        Parameters
        ----------
        cb : callable
            Callback receiving the service state change.
        """
        self._callbacks.append(cb)