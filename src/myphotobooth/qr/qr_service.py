"""QR code generation from the detected local IP (F-HOTE-02/03, C-04)."""

import socket
import qrcode


class QrService:
    """Builds and renders the guest access URL and QR code."""

    def build_url(self, ip: str, port: int) -> str:
        """Build the guest access URL.

        Parameters
        ----------
        ip : str
            Detected local IP address.
        port : int
            HTTP port.

        Returns
        -------
        str
            URL such as ``http://192.168.1.42:8000``.
        """
        return f"http://{ip}:{port}"

    def render_png(self, url: str) -> bytes:
        """Render a URL as a PNG QR code.

        Parameters
        ----------
        url : str
            URL to encode.

        Returns
        -------
        bytes
            PNG image bytes.
        """
        qrobj = qrcode.make(url, error_correction=qrcode.ERROR_CORRECT_H)
        return qrobj.get_image().tobytes()

    @staticmethod
    def detect_local_ip() -> str:
        """Detect the local IP of the outgoing network interface.

        Returns
        -------
        str
            Local IPv4 address.
        """
        hostname = socket.gethostname()
        device_ip = socket.gethostbyname(hostname)

        return device_ip
