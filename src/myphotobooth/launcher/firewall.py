"""Firewall assistance for first launch (F-HOTE-05, C-05)."""


class FirewallAssistant:
    """Ensures inbound rules exist for HTTP and mDNS ports."""

    @staticmethod
    def ensure_rules(port: int) -> None:
        """Create inbound rules for the HTTP port and UDP 5353.

        May require elevation; a clear French message is shown to the
        user. No-op on platforms without a host firewall.

        Parameters
        ----------
        port : int
            HTTP port to open.
        """
        raise NotImplementedError

    def is_allowed(self, port: int) -> bool:
        """Check whether inbound connections on the port are allowed.

        Parameters
        ----------
        port : int
            HTTP port to check.

        Returns
        -------
        bool
            True if the port is reachable from the network.
        """
        raise NotImplementedError
