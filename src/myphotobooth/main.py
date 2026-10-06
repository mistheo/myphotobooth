"""Application entry point."""

from myphotobooth.core.config import AppConfig
from myphotobooth.core.supervisor import RoleSupervisor


def main() -> int:
    """Load configuration and run the role supervisor.

    Returns
    -------
    int
        Process exit code.
    """
    config = AppConfig.load()
    return RoleSupervisor(config).run()


if __name__ == "__main__":
    raise SystemExit(main())
