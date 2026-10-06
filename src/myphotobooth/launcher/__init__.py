"""Kiosk launching with crash supervision and firewall assistance."""

from myphotobooth.launcher.firewall import FirewallAssistant
from myphotobooth.launcher.kiosk import SlideshowLauncher

__all__ = ["SlideshowLauncher", "FirewallAssistant"]
