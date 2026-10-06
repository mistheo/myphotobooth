/**
 * Guest page (client P) — Alpine.js component.
 *
 * Responsibilities: photo upload, session identifier handling
 * (localStorage), listing and deleting own photos.
 */
const guestApp = () => ({
  /** Session identifier kept in localStorage. */
  sessionToken: null,

  /** Initialise the session identifier on page load. */
  init() {
    throw new Error("Not implemented");
  },

  /**
   * Send selected photos to the server.
   * @param {FileList} files - Photos chosen by the guest.
   * @returns {Promise<Object>} Upload result per file.
   */
  async sendPhotos(files) {
    throw new Error("Not implemented");
  },

  /**
   * Load thumbnails of the photos sent by this guest.
   * @returns {Promise<Array>} List of the guest's photos.
   */
  async loadMyPhotos() {
    throw new Error("Not implemented");
  },

  /**
   * Delete one of the guest's own photos.
   * @param {string} id - Photo identifier.
   * @returns {Promise<Object>} Deletion result.
   */
  async deletePhoto(id) {
    throw new Error("Not implemented");
  },
});
