/**
 * Slideshow page (client D) — local and remote display.
 *
 * Responsibilities: WebSocket subscription, display loop with
 * transitions, QR welcome slide, organiser delete control,
 * local cache for network outages.
 */
const slideshowApp = () => ({
  /** Photos currently in rotation, backed by the local cache. */
  photos: [],
  /** WebSocket connection, null when disconnected. */
  socket: null,

  /**
   * Connect to the host event stream.
   * @param {string} url - WebSocket URL of the host.
   */
  connect(url) {
    throw new Error("Not implemented");
  },

  /**
   * Register a handler for incoming slide events.
   * @param {Function} cb - Event handler.
   */
  onEvent(cb) {
    throw new Error("Not implemented");
  },

  /**
   * Render a slide event (add or remove a photo in rotation).
   * @param {Object} event - SlideEvent received over WebSocket.
   */
  render(event) {
    throw new Error("Not implemented");
  },

  /** Show the QR welcome slide. */
  showQrSlide() {
    throw new Error("Not implemented");
  },

  /**
   * Organiser control: request deletion of the displayed photo
   * after confirmation (F-DIA-06/07).
   */
  requestDeleteCurrent() {
    throw new Error("Not implemented");
  },
});
